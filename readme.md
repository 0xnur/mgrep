It's simple script includes some usefull regex to grep data from a text file.

For now it just include IP,IPwithLine,email and url.

### Usage

python mgrep.py ip sample.txt
1.1.1.1

python mgrep.py url sample.txt
http://www.google.com
http://abc.com/withurl

python mgrep.py email sample.txt
abc@abc.com.tr
email@subdomain.test.com
email@test.com
email.email@test.com

### Install
If you want to install system wide, download mgrep.py:

cp mgrep.py /usr/bin/mgrep && chmod +x /usr/bin/mgrep

### To Do
Date, Domain
