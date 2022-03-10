
with open('day1input.txt', 'r') as fd:
	lines = fd.read().split("\n")
	for i in range(0, len(lines)):
		lines[i] = int(lines[i])
	print(lines) 
	print("\n")

expenseslist = lines

# last_elem = len(expenses)-1
# expenses[last_elem]


for i in range(0,len(expenseslist)):
	for j in range (0, len(expenseslist)):
		if i is not j: 
			if expenseslist[i] + expenseslist[j] == 2020: 
				print(expenseslist[i], expenseslist[j], "is 2020")
				print("Das Produkt lautet", expenseslist[i]*expenseslist[j])
				print()
				
	
#print(expenseslist)


print("--------------------Aufgabe 2--------------------")

for i in range (0, len(expenseslist)): 
	for j in range (0, len(expenseslist)): 
		for k in range (0, len(expenseslist)): 
			if i is not j and i is not k and j is not k: 
						if expenseslist[i] + expenseslist[j] + expenseslist[k] == 2020:
							print (expenseslist[i], expenseslist[j], expenseslist[k])
							print ("Das Produkt lautet", expenseslist[i]*expenseslist[j]*expenseslist[k])
							print()
