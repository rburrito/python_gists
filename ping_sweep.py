def ping():
	ipAddress=input("What is the ip address range you would like to do a ping sweep on? Sample Input: 10.11.1.1-254\n")
	ipAddress=ipAddress.rstrip().split('.')
	ipAddr='.'.join(ipAddress[0:-1])
	ipRange=ipAddress[-1].split('-')
	rangeBegin=int(ipRange[0])
	rangeEnd=int(ipRange[1])+1
	for i in range(rangeBegin,rangeEnd):
		newIPAddr=ipAddr + '.' + str(i)
		response=subprocess.call(['ping','-c', '1', newIPAddr])
		
def main():
	return ping()
	sys.exit()


if __name__=="__main__":
	print(main())
