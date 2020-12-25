class Passport:
    attrs = ['byr', 'iyr','eyr', 'hgt', 'hcl', 'ecl', 'pid']

    def fromtxt(self, line):
        for pair in line.split():
            attr, value = pair.split(':')[0], pair.split(':')[1]
            self.__dict__[attr] = value

    def hasvalidattrs(self):
        if all([attr in self.__dict__.keys() for attr in self.attrs]):
            return True
        else:
            return False

    def hasvalidvalues(self):
        if not self.hasvalidattrs():
            return False
        # byr
        try:
            if not (1920 <= int(self.byr) <= 2002):
                return False
        except:
            return False
        # iyr
        try:
            if not (2010 <= int(self.iyr) <= 2020):
                return False
        except:
            return False
        # eyr
        try:
            if not (2020 <= int(self.eyr) <= 2030):
                return False
        except:
            return False
        # hgt
        if self.hgt[-2:] not in ['in', 'cm']:
            return False
        try:
            h = int(self.hgt[:-2])
        except:
            return False
        if not ((self.hgt[-2:] == 'in' and 59<=h<=76)
                or
                (self.hgt[-2:] == 'cm' and 150<=h<=193)):
            return False
        # hcl
        if not (len(self.hcl) == 7
                and
                self.hcl[0] == '#'
                and
                all((('0'<=ch<='9') or ('a'<=ch<='f')) for ch in self.hcl[1:])
                ):
            return False
        # ecl
        if not self.ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            return False
        # pid
        if not len(self.pid) == 9:
            return False
        try:
            int(self.pid)
        except:
            return False
        return True

passbase = []

with open('day04input.sql') as inpfile:
    txtbase = inpfile.readlines()
    inpfile.close()

p = Passport()
for line in txtbase:
    if line.strip() == '':
        passbase.append(p)
        p = Passport()
        continue
    p.fromtxt(line)
passbase.append(p)

print("There are {} passports in base".format(len(passbase)))

# part 1
valid_count = 0
for p in passbase:
    if p.hasvalidattrs():
        valid_count +=1

print("There are {} passports with required fields in base".format(valid_count))

# part 2

valid_count = 0
for p in passbase:
    if p.hasvalidvalues():
        valid_count +=1

print("There are {} passports with valid values in base".format(valid_count))
