from pprint import pprint

with open('day4input.txt', 'r') as fd:
  lines = fd.read().split("\n\n")

validpp = 0


for line in lines: 
  line = line.replace("\n", " ")
  line = line + " "
  print(line)
  #print()

  if (line.find("eyr") != -1) and (line.find("byr") != -1) and (line.find("iyr") != -1) \
   and (line.find("hgt") != -1) and (line.find("hcl") != -1) and (line.find("ecl") != -1) \
   and (line.find("pid") != -1):
     print(line.index("eyr:")+4, line.index(" ")-1)
     eyr = int(line[ line.index("eyr:")+4 : line.index(" ")-1])
     iyr = (line[ line.index("iyr:")+4 : line.index(" ")-1])
     byr = (line[ line.index("byr:")+4 : line.index(" ")-1])
     hcl = (line[ line.index("hcl:")+4 : line.index(" ")-1])
     ecl = (line[ line.index("ecl:")+4 : line.index(" ")-1])
     pid = (line[ line.index("pid:")+4 : line.index(" ")-1])
     if (line.find("cm") != -1):
       hgtcm = int(line[ line.index("hgt")+4 : line.index("hgt")+7])
       print("eyr=", eyr, "iyr=", iyr, "byr=", byr, "hgt=", hgtcm, "hcl=", hcl, "ecl=", ecl, "pid=", pid)
       if (eyr >= 2020 and eyr <=2030) and \
       (iyr >=2010 and iyr <=2020) and \
       (byr >=1920 and byr <= 2002) and \
       (ecl == "amb" or ecl == "blu" or ecl == "brn" or ecl == "gry" or ecl == "grn" or ecl == "hzl" or ecl == "oth") and \
       (hgtcm >= 150 and hgtcm <= 193):
         validpp = validpp+1
         print("eyr, iyr, byr and ecl valid")

     if (line.find("in") != -1):
       hgtin = line[ line.index("hgt")+4 : line.index("in")]
     print("eyr=", eyr, "iyr=", iyr, "byr=", byr, "hgt=") #hgtin, "hcl=", hcl, "ecl=", ecl, "pid=", pid)