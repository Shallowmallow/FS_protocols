import sys
import re

inFile = sys.argv[1]


allNumbers_reg = re.compile("^(\d+)$")

skaters_info = []
skater_info = {}
event_name = ""
event_type = ""

with open(inFile) as f:
	i= 0
	startL = 0
	for line in f:
		if (i is 0):
			event_type = line
		if ("Planned Program Content" in line):
			startL = i
			print(skater_info)
			skater_info ={}
			skaters_info.append(skater_info);
			
		if (i == startL+1):
			skater_info["name"] =  line.strip()
		if ( "SP/SD" in line):
			elements = []
			skater_info["sp"] = elements
		if ( "FS/FD" in line):
			elements = []
			skater_info["fs"] = elements
			

		l = re.split("\s\s+",line.replace("\n", ""))

		if (allNumbers_reg.match(l[0]) and len(l)>1):
			print(l)
			print(len(l))
			element = l[1]
			elements.append(element)
		i = i+1	


print(skaters_info)

inFile = inFile.replace(".txt", "")
event_type = event_type.replace("-", "")
with open(inFile + "_SP", "w") as f: 
	f.write("event type: " + event_type.strip() +" SP" +"\n")
	#f.write("SP: " "\n" ) 
	for s in skaters_info:
		
		f.write(s.get("name") + ": " ) 
		for e in s.get("sp"):

			f.write("" + e)
			f.write("\t")
		f.write("\n")

with open(inFile + "_FS", "w") as f: 
	f.write("event type: " + event_type.strip() + " FS" + "\n")
	#f.write("LP: " "\n" ) 
	for s in skaters_info:
		
		f.write(s.get("name") + ": " ) 
		for e in s.get("fs"):

			f.write("" + e)
			f.write("\t")
		f.write("\n")

