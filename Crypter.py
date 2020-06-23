import compileall
from os import system
from time import sleep

system('clear')


print ('''\033[1;33m 					    ____                  _            
					    / ___|_ __ _   _ _ __ | |_ ___ _ __ 
					   | |   | '__| | | | '_ \| __/ _ \ '__|
					   | |___| |  | |_| | |_) | ||  __/ |   
					    \____|_|   \__, | .__/ \__\___|_|   
					               |___/|_|                 

''')

compileall.compile_dir(raw_input('\033[1;36mEnter The Name and Place of Directory or Script You Wanna Make Them Crypted : '))
print ('						\033[1;32mDone !')
sleep(3)
system('clear')
exit()
