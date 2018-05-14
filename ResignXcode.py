import sys, os, getopt

import re
import getpass

TEMP_DIR = os.path.expanduser("~/resigntemp")
RESIGN_CER_ID = "XcodeResigner"

if __name__ == '__main__':
    print("\033[31mCaution: These steps may put your Xcode under risk, so if you don't know what's going on, please stop.\033[0m")
    print("Resign will kill your Xcode, and may take a while; During the process, please don't open it.")
    choice = input('Would you like to start? (y/n)\n')
    
    if choice != 'y':
        print("abort.")
        sys.exit(0)

    if len(os.popen("pgrep -x Xcode").read()) != 0:
        print("Kill Xcode.")
        os.system('killall Xcode')

    # generate key pair
    keyPath = '%s/private.key' % TEMP_DIR
    cerPath = '%s/cert.crt' % TEMP_DIR
    p12Path = "%s/%s.p12" % (TEMP_DIR, RESIGN_CER_ID)
    confPath = "%s/apple.conf" % TEMP_DIR

    loginKeychain = os.popen('security login-keychain').read().strip()
    if len(os.popen("security find-certificate -c %s %s" % (RESIGN_CER_ID, loginKeychain)).read().strip()) == 0:
        if not os.path.exists(TEMP_DIR):
            os.system('mkdir %s' % TEMP_DIR)

        # config file
        confContent = "[ req ]\ndistinguished_name = req_name\nprompt = no\n[ req_name ]\nCN = %s\n[ extensions ]\nkeyUsage=critical,digitalSignature\nextendedKeyUsage=critical,codeSigning\n" % RESIGN_CER_ID
        with open(confPath, 'w') as f:
            data = f.write(confContent)
        
        os.system("openssl genrsa -out %s 2048" % keyPath)
        os.system("openssl req -x509 -new -config %s -nodes -key %s -extensions extensions -sha256 -out %s" % (confPath, keyPath, cerPath))
        print("\033[31mEnter pass for your p12, can't ignore.\033[0m")

        os.system("openssl pkcs12 -export -inkey %s -in %s -out %s" % (keyPath, cerPath, p12Path))

        # import into keychain
        print("\033[31mEnter the pass you just entered a moment ago.\033[0m")
        os.system('security import %s -k %s' % (p12Path, loginKeychain))
    
    # resign
    # get xcode path
    xcodePath = re.search(r".*?Xcode.app", os.popen("xcode-select -print-path").read()).group()
    rootPass = getpass.getpass('Resign Xcode needs your root permission. Please enter your root pass: ')
    print("\033[31mBegin resign, this will take a while... \033[0m")
    os.system("echo %s | sudo -S codesign -f -s %s %s" % (rootPass, RESIGN_CER_ID, xcodePath))

    if os.path.exists(TEMP_DIR):
        os.system('rm -rf %s' % TEMP_DIR)

    print('\xF0\x9f\x8d\xba  Resign finished. Have fun!')
    
    
