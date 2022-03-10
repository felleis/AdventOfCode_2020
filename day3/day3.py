from pprint import pprint

with open('day3input.txt', 'r') as fd:
	lines = fd.read().split("\n")


schlittenposition = 0
baume = 0

# pprint(lines)
for line in lines:
	# print(schlittenposition, len(line))
	if line[schlittenposition] == "#":  
		baume = baume +1
	schlittenposition = schlittenposition+3
	if schlittenposition >= len(line):
		schlittenposition = schlittenposition % len(line)

print(baume)


print("--------------------Aufgabe 2--------------------")




def traverse(rechts,runter): 
	# pprint(lines)

	schlittenposition = 0
	baume = 0

	# for line in lines:
	for i in range(0, len(lines)):
		line = lines[i]

		if i % runter == 0: 
			# print(schlittenposition, len(line))
			if line[schlittenposition] == "#":  
				baume = baume +1
			schlittenposition = schlittenposition+rechts
			if schlittenposition >= len(line):
				schlittenposition = schlittenposition % len(line)

	return baume 

treesroute1 = traverse(1,1)

treesroute2 = traverse(3,1)

treesroute3 = traverse(5,1)

treesroute4 = traverse(7,1)

treesroute5 = traverse(1,2)

print(treesroute1 * treesroute2 * treesroute3 * treesroute4 * treesroute5)