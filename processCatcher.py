#Programs can either execute a new process or fork and make a child process.
#Executing any shell commands is a huge issue
import subprocess
import os
#TO DO
#Find workaround for the processes created by subprocess and os
#Patch security vuln to processes named ps, sh, and tpvmlp


print("Setting current running processes as baseline")

processes = dict()

DEVNULL = open(os.devnull, "w")
cmd = "ps -e"
ps = str(subprocess.check_output(cmd,shell=True, stderr=DEVNULL))
ps = ps.split()
x = 0
size = 0

while x < (len(ps) - 3):
	processes[ps[x]] = ps[x+3]
	x += 4


#Continue checking processes, if not in the original, then kill the process
while True:
	cmd = "ps -e"
	psTemp = subprocess.check_output(cmd,shell = True, stderr = DEVNULL)
	psTemp = psTemp.split()
	y = 0
	while y < (len(ps) - 3):
		if psTemp[y+3] == "ps" or psTemp[y+3] == "sh" or psTemp[y+3] == "tpvmlp":
			y += 4
			continue 
		if psTemp[y] not in processes:
			print("Illegal Processes Found")
			print("Killing PID " + psTemp[y] + " named " + psTemp[y+3])
			#cmd = "kill " + psTemp[y]
			try:
				os.kill(int(psTemp[y]),9)
			except OSError:
				print("Attempt to remove failed")
		y += 4