import os
os.system('clear')

print("[+] login in termux")
print("[+] coded by: salism3\n")
h = "\033[92m"
p = "\033[0m"
a = str(input('[?] input username: '))
b = str(input('[?] input password: '))
print("\n[+] set username to: " + h + a + p)
print("[+] set password to: " + h + b + p + "\n")
c = str(input('[+] input "yes" to confirm: '))
if c == "yes":
	pass
else:
	print("[+] failed!")
	exit()

#gas
file = open('file.txt').read()
open('/data/data/com.termux/files/home/data.txt', 'w').write(a + "\n" + b)
open('/data/data/com.termux/files/home/.home', 'w').write(file)
os.system('rm /data/data/com.termux/files/usr/etc/bash.bashrc')
open('/data/data/com.termux/files/usr/etc/bash.bashrc', 'w').write('python .home')
print("[+] success, please restart your Termux")
