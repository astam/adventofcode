import re

input_file = '2020/day4/input_example2.txt'
input_file = '2020/day4/input.txt'
with open(input_file) as f:
    lines = [line.strip() for line in f.readlines()]
# print(lines)

# fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid','cid']
required = ['byr','iyr','eyr','hgt','hcl','ecl','pid']

# Part 1
passports = []
passport = ""
for line in lines:
    if line != '':
        passport = passport + ' ' + line
    else:
        passports.append(passport.strip())
        passport = ""
passports.append(passport.strip())
# print(passports)
invalid = 0
passport_list = []
for passport in passports:
    print(passport)
    fields = passport.split(' ')
    field_names = [x.split(':')[0] for x in fields]
    field_list = ([x.split(':') for x in fields])
    # print(field_values)
    missing_fields = [x for x in required if x not in field_names]
    # print(missing_fields)
    if len(missing_fields) > 0:
        invalid += 1
    else:
        for field in field_list:
            print(field)
            # - byr (Birth Year) - four digits; at least 1920 and at most 2002.
            # if field[0] == 'byr' and (1920 > int(field[1]) < 2002):
            if field[0] == 'byr' and not re.fullmatch(r'^(19[2-9][0-9]|200[0-2])$', field[1]):
                invalid += 1
                break
            # - iyr (Issue Year) - four digits; at least 2010 and at most 2020.
            # if field[0] == 'iyr' and (2010 > int(field[1]) < 2020):
            if field[0] == 'iyr' and not re.fullmatch(r'^20(1[0-9]|20)$', field[1]):
                invalid += 1
                break
            # - eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
            # if field[0] == 'eyr' and (2020 > int(field[1]) < 2030):
            if field[0] == 'eyr' and not re.fullmatch(r'^20(2[0-9]|30)$', field[1]):
                invalid += 1
                break
            # - hgt (Height) - a number followed by either cm or in:
            #       If cm, the number must be at least 150 and at most 193.
            #       If in, the number must be at least 59 and at most 76.
            if field[0] == 'hgt' and not re.fullmatch(r'^(1([5-8][0-9]|[9][0-3])cm|(59|6[0-9]|7[0-6])in)$', field[1]):
                invalid += 1
                break
            # - hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
            if field[0] == 'hcl' and not re.fullmatch(r'^#[0-9a-f]{6}$', field[1]):
                invalid += 1
                break
            # - ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
            if field[0] == 'ecl' and not re.fullmatch(r'^(amb|blu|brn|gry|grn|hzl|oth)$', field[1]):
                invalid += 1
                break
            # - pid (Passport ID) - a nine-digit number, including leading zeroes.
            if field[0] == 'pid' and not re.fullmatch(r'^[0-9]{9}$', field[1]):
                invalid += 1
                break
    print()
print(len(passports) )
print(invalid)
print(len(passports) - invalid)