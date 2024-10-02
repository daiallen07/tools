#pingsweep using ipaddr

import ipaddress
import subprocess

def ping_ip(ip):
	try:
		# For Windows, use 'ping -n 1'
		output = subprocess.run(["ping", "-c", "1", str(ip)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		return output.returncode == 0
	except Exception as e:
	print(f"Error pinging {ip}: {e}")
	return False

def ip_sweeper(network):
	try:
		net = ipaddress.ip_network(network)
	except ValueError as e:
	print(f"Invalid network: {e}")
	return

	print(f"Scanning network: {network}")
	for ip in net.hosts():
		if ping_ip(ip):
			print(f"{ip} is reachable")
		else:
			print(f"{ip} is not reachable")

if __name__ == "__main__":
	network_input = input("Enter the network (e.g., 192.168.1.0/24): ")
	ip_sweeper(network_input)

