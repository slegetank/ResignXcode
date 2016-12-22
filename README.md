<div id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#sec-1">1. ResignXcode</a></li>
<li><a href="#sec-2">2. Use</a></li>
<li><a href="#sec-3">3. You should know</a></li>
<li><a href="#sec-4">4. Simple explain</a></li>
<li><a href="#sec-5">5. Other things</a></li>
</ul>
</div>
</div>


# ResignXcode<a id="sec-1" name="sec-1"></a>

This little script's purpose is just for resign Xcode with a self-signed certificate.  
From Xcode8, apple just stops the use of plugins to give programmers more security. This is really inconvenience for me. Everytime Xcode updates, I have to resign Xcode mannually to continue use so much good plugins[(Manual From XVim)](https://github.com/XVimProject/XVim/blob/master/INSTALL_Xcode8.md). So, this weapon is born.  

# Use<a id="sec-2" name="sec-2"></a>

    python ResignXcode.py

# You should know<a id="sec-3" name="sec-3"></a>

1.  If you don't know what's going on with this script, then don't use it, because it'll put you under risk.
2.  You can read the code to decide if you want to use it.

# Simple explain<a id="sec-4" name="sec-4"></a>

1.  Use openssl to generate 2048 RSA self-signed certificate.
2.  Import the cer into your keychain.
3.  Resign your Xcode.

# Other things<a id="sec-5" name="sec-5"></a>

-   Good app: <https://github.com/fpg1503/MakeXcodeGr8Again#should-i-use-it>
-   Discuss: <https://github.com/alcatraz/Alcatraz/issues/475>
-   openssl req file format: <https://wiki.openssl.org/index.php/Manual:Req(1)>
-   Generate right self-signed cer: <http://security.stackexchange.com/questions/17909/how-to-create-an-apple-installer-package-signing-certificate?answertab=votes#tab-top>
