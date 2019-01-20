1) WINDOWS : Upgrade de la version de PIP
   --------------------------------------
Powershell en mode admin :

PS C:\WINDOWS\system32> python -m pip install --upgrade pip
Requirement already up-to-date: pip in c:\program files\python36\lib\site-packages (18.1)

2) WINDOWS : Mise à jour des paquets avec PIP
   --------------------------------------
Powershell en mode admin :

PS C:\WINDOWS\system32> pip install --upgrade ((pip freeze) -replace '==.+','')


3) WINDOWS  : Mise à jour avec PIP derrière un proxy 
   --------------------------------------
Solution1 (temporaire) :

Ajouter à la ligne de commande de PIP le paramètre : 

--proxy http://user:pass@proxyAddress:proxyPort


Solution2 (pérenne) :

1. In Windows navigate to your user profile directory and create a folder named "pip" : On Windows the configuration file is %APPDATA%\pip\pip.ini

2. In this file (Ex. C:\Users\Sync\pip\pip.ini) , enter the following into it:

    [global]
    trusted-host = pypi.python.org
                   pypi.org
                   files.pythonhosted.org
    proxy = http://[domain name]%5C[username]:[password]@[proxy address]:[proxy port]

Replace [domain name], [username], [password], [proxy address] and [proxy port] with your own information.

3. At this point I was able to run "pip install" without any issues.

P.S.: This may pose a security concern because of having your password stored in plain text. If this is an issue, consider setting up CNTLM using this article (https://stormpoopersmith.com/2012/03/20/using-applications-behind-a-corporate-proxy/ , allows using hashed password instead of plain text). Afterwards set proxy = 127.0.0.1:3128in the "pip.ini" file mentioned above.

