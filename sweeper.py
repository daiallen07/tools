#ONLY USE FOR COMPETITION


#if given 10.12.10.4/8, just enter the ip as 10.0.0.0/8 and ping
#the entire net.
#ip changes depending on the mask which could be /23 or /22

#args: ip, submask (#), exclude file name
#example use: python3 sweeper.py 192.168.10.0 24 exclude

import sys
import subprocess
import threading

#binary to decimal
def bintodec(octet):
	decimal = 0
	for digit in octet:
		decimal = decimal*2 + int(digit)
	return decimal

#submask checker
def submaskCheck(decimal):
	if decimal == 255:
		return 1
	else:
		return 0	

#will find the final ip
def ipSwitch():
	itr = 0
	#could probs be condensed
	if submaskCheck(firstDecimal):
		itr += 1
	if submaskCheck(secondDecimal):
		itr += 1
	if submaskCheck(thirdDecimal):
		itr += 1
	if submaskCheck(fourthDecimal):
		itr += 1
	return itr

#ping
def ping(ipVar):
	try:
		result = subprocess.run(['ping', '-c', '1', ipVar], text=True, capture_output=True)

		if "bytes from" in result.stdout:
			print(result.stdout.strip())
	except Exception as e:
		print(f"Error pinging {ip}: {e}")


#read exclude file
argList = sys.argv[3]
try:
    with open(argList, 'r') as fp:
        file = fp.read().replace('\n', ' ')
except FileNotFoundError:
    print('File not found')
    exit()

ip, CIDR = sys.argv[1], sys.argv[2]
submask = ''
ipList = []
#convert the /xx into binary form
i = 0
while i < 32:
	if i < int(CIDR):
		submask = submask + '1'
		i += 1
	else:
		submask = submask + '0'
		i += 1 

#convert each octet into decimal (using the function)
#could probs be condensed
firstDecimal = bintodec(submask[0:8])
secondDecimal = bintodec(submask[8:16])
thirdDecimal = bintodec(submask[16:24])
fourthDecimal = bintodec(submask[24:32])

#get pingable ip address
ipSplit = ip.split('.')
finalIP = ''
i = 0
tempITR = ipSwitch()

while i < tempITR:
	if i == tempITR - 1:
		finalIP = finalIP + ipSplit[i]
	else:
		finalIP = finalIP + ipSplit[i] + '.'
	i += 1

if i < 4:
	finalIP = finalIP + '.'

#ping sweep (could probs be condensed)
#0 will not be used (no one uses /0 but here just in case lmao)
if tempITR == 0:
	for i in range(firstDecimal, 255):
		for j in range(secondDecimal, 255):
			for k in range(thirdDecimal, 255):
				for l in range(fourthDecimal, 255):
					tmpFinalIP = finalIP + str(i) + '.' + str(j) + '.' + str(k) + '.' + str(l)
					print(tmpFinalIP)
					l += 1
				k += 1
			j += 1
		i += 1
#1 will most likely not be used in competition since it is too big
elif tempITR == 1:
	for i in range(secondDecimal, 255):
		for j in range(thirdDecimal, 255):
			for k in range(fourthDecimal, 255):
				tmpFinalIP = finalIP + str(i) + '.' + str(j) + '.' + str(k)
				print(tmpFinalIP)
				k += 1
			j += 1
		i += 1
#good chance it will be used for /16
elif tempITR == 2:
	for i in range(thirdDecimal, 255):
		for j in range(fourthDecimal, 255):
			tmpFinalIP = finalIP + str(i) + '.' + str(j)
			if tmpFinalIP in file:
				pass
			else:
				thread = threading.Thread(target=ping, args=(tmpFinalIP,))
				threads.append(thread)
				thread.start()
			for thread in threads:
				thread.join()
			j += 1
		i += 1
#very likely since it is /24
elif tempITR == 3:
	for i in range(fourthDecimal, 255):
		tmpFinalIP = finalIP + str(i)
		if tmpFinalIP in file:
			pass
		else:
			if ping(finalIP):
				print('wurk')
			else:
				print('gg')
		i += 1
#bro just nmap it
elif tempITR == 4:
	if ping(finalIP):
		print('work?')
	else:
		print('gg')
