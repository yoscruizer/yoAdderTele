#!/bin/env python3

"""

you can re run setup.py 
if you have added some wrong value

"""
import os, sys
import configparser
re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"
def banner():
	os.system('clear')
	print(f"""
	{re}╔═╗{cy}┌─┐┌┬┐┬ ┬┌─┐
	{re}╚═╗{cy}├┤  │ │ │├─┘
	{re}╚═╝{cy}└─┘ ┴ └─┘┴
	
	{re}       Y0$cru1z3r
	{cy}www.github.com/yoscruizer
	""")
banner()
print(gr+"[+] Menginstall pelengkap ...")
os.system('python3 -m pip install telethon')
os.system('pip3 install telethon')
banner()
os.system("touch config.data")
cpass = configparser.RawConfigParser()
cpass.add_section('cred')
xid = input(gr+"[+] masukan api ID : "+re)
cpass.set('cred', 'id', xid)
xhash = input(gr+"[+] masukan hash ID : "+re)
cpass.set('cred', 'hash', xhash)
xphone = input(gr+"[+] masukan phone number : "+re)
cpass.set('cred', 'phone', xphone)
setup = open('config.data', 'w')
cpass.write(setup)
setup.close()
print(gr+"[+] setup selesai !")
print(gr+"[+] now you can run any tool !")
