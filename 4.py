import re
lines = list((open('data-4.txt', 'r').read().split("\n\n")))
#print(lines[0].split())

def convert(lst):
    data = []
    for i in lst:
        i = i.split()        
        dct = {i[j][0:3]: i[j][4:] for j in range(len(i))}
        data.append(dct)
    return data

def chck_byr(byr):
    if 1920 <= int(byr) <= 2002:
        return True
    else:
        return False

def chck_iyr(iyr):
    if 2010 <= int(iyr) <= 2020:
        return True
    else:
        return False

def chck_eyr(eyr):
    if 2020 <= int(eyr) <= 2030:
        return True
    else:
        return False

def chck_hgt(hgt):
    if (hgt[-2:] == "cm") and (150 <= int(hgt[:-2]) <= 193):
        return True
    elif (hgt[-2:] == "in") and (59 <= int(hgt[:-2]) <= 76):
        return True
    else:
        return False

def chck_hcl(hcl):
    if (hcl[0] == "#") and (len(hcl) == 7) and (re.match("^[0-9a-f]*$",hcl[1:])):
        return True
    else:
        return False

def chck_ecl(ecl):
    if ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return True
    else:
        return False

def chck_pid(pid):
    if len(pid) == 9:
        return True
    else:
        return False

valid = 0
data = convert(lines)
keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
for i in data:
    count = 0
    for j in keys:
        if j not in i:
            count += 1
            #print("Brak: {}".format(j))
    if count < 1 and (chck_byr(i["byr"]) & chck_iyr(i["iyr"]) & chck_eyr(i["eyr"]) & chck_hgt(i["hgt"]) & chck_hcl(i["hcl"]) & chck_ecl(i["ecl"]) & chck_pid(i["pid"])):

        valid += 1 # tutaj funkcje sprawdzające poszczególne pola
print(valid)