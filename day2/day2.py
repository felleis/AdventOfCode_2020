from pprint import pprint

with open('day2input.txt', 'r') as fd:
	lines = fd.read().split("\n")


pwlist = lines
# pprint(pwlist)


# for i in range(0,len(pwlist)):

counter = 0 
#for i in range(0,22):	
for elem in pwlist: 

	minocc = int(elem[ 0 : elem.index("-") ])
	maxocc = int(elem[ elem.index("-")+1 : elem.index(" ") ])
	letter = elem[ elem.index(":")-1 : elem.index(":")]
	password = elem[ elem.index(": ")+2 : len(elem)]
	
	if password.count(letter) >= minocc and password.count(letter) <= maxocc: 
		counter = counter + 1


	print(minocc, maxocc, letter, password)
print("Insgesamt:", counter)


print("--------------------Aufgabe 2--------------------")

counter2 = 0

for elem in pwlist: 

	pos1 = int(elem[ 0 : elem.index("-") ])
	pos2 = int(elem[ elem.index("-")+1 : elem.index(" ") ])
	letter = elem[ elem.index(":")-1 : elem.index(":")]
	password = elem[ elem.index(": ")+2 : len(elem)]

	if (password[pos1-1] is letter and password[pos2-1] is not letter) or (password[pos2-1] is letter and password[pos1-1] is not letter): 
		counter2 = counter2 + 1
print("insgesamt:", counter2)
