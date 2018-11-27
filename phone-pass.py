#!/usr/bin/python3


from time import sleep
import os,sys

def banner():
	print("____________________  ________ ")
	print("\______   \______   \/  _____/ ")
	print(" |     ___/|     ___/   \  ___ ")
	print(" |    |    |    |   \    \_\  \ ")
	print(" |____|    |____|    \______  / ")
	print("                            \/ ")

def message(msg):
        for char in msg:
                sleep(0.05)
                sys.stdout.write(char)
                sys.stdout.flush()

def fix():
	os.system('clear')
	banner()
	target = input('\033[1;33m[*]\033[1;m enter your wilaya ex:035 >')
	phone = 100000
	phone_f = 999999
	while (phone != phone_f):
        	phone = phone + 1
        	phone_gen = target+str(phone)+'\n'
        	file_open.write(phone_gen)
	print('\033[1;32m[+]\033[1;m creating finished .')
	file_open.close()
	exit(0)

def mobile():
	os.system('clear')
	banner()
	phone = 10000000
	phone_f = 99999999
	print('1 - ooredoo')
	print('2 - djezzy')
	print('3 - mobilis')
	print('4 - back to home menu')
	print('5 - exit')
	choose = input('choose >')
	if choose == '1':
		message('\033[1;33m[*]\033[1;m creating file ...\n')
		while (phone != phone_f):
			phone = phone + 1
			phone_gen = '05'+str(phone)+'\n'
			file_open.write(phone_gen)
		print('\033[1;32m[+]\033[1;m creating finished .')
		file_open.close()
		exit(0)
	elif choose == '2':
		message('\033[1;33m[*]\033[1;m creating file ...\n')
		while (phone != phone_f):
			phone = phone + 1
			phone_gen = '07'+str(phone)+'\n'
			file_open.write(phone_gen)
		print('\033[1;32m[+]\033[1;m creating finished .')
		file_open.close()
		exit(0)
	elif choose == '3':
		message('\033[1;33m[*]\033[1;m creating file ...\n')
		while (phone != phone_f):
			phone = phone + 1
			phone_gen = '06'+str(phone)+'\n'
			file_open.write(phone_gen)
		print('\033[1;32m[+]\033[1;m creating finished .')
		file_open.close()
		exit(0)
	elif choose == '4':
		choose_type()
	elif choose == '5':
		exit(0)

def choose_type():
	os.system('clear')
	banner()
	print('1 - Fix')
	print('2 - Mobile')
	print('3 - Exit')
	choose = input('choose >')
	if choose == '1':
		fix()
	elif choose == '2':
		mobile()
	elif choose == '3':
		exit(0)
def main():
	choose_type()


if __name__=='__main__':
	file_open = open('phone-pass.txt','w')
	main()
