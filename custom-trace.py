from scapy.all import *
dest = input("Please enter the destination IP: ")

ttl = 1
while ttl < 30:
	a = IP()
	a.dst = dest
	b = ICMP()
	a.ttl = ttl
	reply = sr1(a/b, verbose=0, timeout=3)
	if reply is None:
		print("Timed out")
	else:
		print(reply.src)
		if reply.src == dest:
			break
	ttl += 1

print("Trace finished")