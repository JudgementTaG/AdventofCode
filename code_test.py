## DAY ONE ##
"""
elf_totals = {}
with open("input.txt","r") as file:
    elf_num = total = 0
    for line in file:
        if line == "\n":
            elf_totals[f'elf {elf_num}'] = total
            elf_num += 1
            total = 0
        else:
            total += int(line)

num = 1
total = 0
for key,value in sorted(elf_totals.items(), key= lambda x: x[1],reverse= True):
    if num > 3:
        break
    num += 1
    total += value
    print(key, ":  ", value)

print(f"toal carried by top 3:  total")
"""       

## DAY TWO ##

# RPS - you: R.P.S = A.B.C     them R.P.S = X.Y.Z 
"""
your_score = 0
with open("RPS_input.txt","r") as file:
    for line in file:
        if line[0] == "A":
            if line[2] == "X":
                your_score += 4
            elif line[2] == "Y":
                your_score += 8
            elif line[2] == "Z":
                your_score += 3
        
        elif line[0] == "B":
            if line[2] == "X":
                your_score += 1
            elif line[2] == "Y":
                your_score += 5
            elif line[2] == "Z":
                your_score += 9
    
        elif line[0] == "C":
            if line[2] == "X":
                your_score += 7
            elif line[2] == "Y":
                your_score += 2
            elif line[2] == "Z":
                your_score += 6
    

print(f"Total score:  {your_score}")
            
your_score = 0
with open("RPS_input.txt","r") as file:
    for line in file:
        if line[0] == "A" and line[2] == "X":
            your_score += 3
        elif line[0] == "A" and line[2] == "Y":
            your_score += 4
        elif line[0] == "A" and line[2] == "Z":
            your_score += 8

        elif line[0] == "B" and line[2] == "X":
            your_score += 1
        elif line[0] == "B" and line[2] == "Y":
            your_score += 5
        elif line[0] == "B" and line[2] == "Z":
            your_score += 9

        elif line[0] == "C" and line[2] == "X":
            your_score += 2
        elif line[0] == "C" and line[2] == "Y":
            your_score += 6
        elif line[0] == "C" and line[2] == "Z":
            your_score += 7

print(f"Win Clause result: {your_score}")    
"""

## DAY 3 ##
"""
letters = [chr(x) for x in range(97,123)]
shared_letters = []
for x in range(65,91):
    letters.append(chr(x))

with open("rucksacks.txt","r") as file1:
    for line in file1:
        pocket_1, pocket_2 = line[:len(line) // 2], line[len(line) // 2:]
        for value,letter in enumerate(letters):
            if letter in pocket_1 and letter in pocket_2:
                shared_letters.append([letter,value+1])

total_shared_values = 0
for pair in shared_letters:
     total_shared_values += pair[1]

#for entry in shared_letters:
    #print(entry)

print(total_shared_values)

teams_list = []
elf_team = []
count = 0
with open("rucksacks.txt","r") as file2:
    for line in file2:
        if count < 3:
            count += 1
            line = line.replace("\n","")
            elf_team.append(line)
            if count == 3:
                teams_list.append(elf_team)
                elf_team = []
                count = 0


print(teams_list[0])
print(teams_list[1])
print(teams_list[2])

token_values = []
token_total = 0
for team in teams_list:
    for value,character in enumerate(letters):
        if character in team[0] and character in team[1] and character in team[2]:
            token_values.append((character, value+1))
        else:
            pass

for entry in token_values:
    token_total += entry[1]
print(token_total)
"""

## DAY 4 ##
"""
overlap_team_num = []
partial_overlap_pairs = []
in_range = True


with open("pairs.txt", "r") as file1:
    for num,line in enumerate(file1):
        line = line.replace("\n","")
        elf1,elf2 = line.split(',')
        elf1_start,elf1_finish = elf1.split('-')
        elf2_start,elf2_finish = elf2.split('-')
        elf1_range = [x for x in range(int(elf1_start),int(elf1_finish)+1)]
        elf2_range = [x for x in range(int(elf2_start),int(elf2_finish)+1)]
        if elf1_start == elf1_finish:
            elf1_range = [int(elf1_start)]
        if elf2_start == elf2_finish:
            elf2_range = [int(elf2_start)]

        num_in_range1 = 0
        for number in elf1_range:
            if number in elf2_range:
                num_in_range1 += 1
        
        if num_in_range1 == len(elf2_range):
            overlap_team_num.append(num+1)
            continue
        
        num_in_range2 = 0
        for number in elf2_range:
            if number in elf1_range:
                num_in_range2 += 1
            
        if num_in_range2 == len(elf1_range):
            overlap_team_num.append(num+1)


with open("pairs.txt", "r") as file1:
    for num,line in enumerate(file1):
        line = line.replace("\n","")
        elf1,elf2 = line.split(',')
        elf1_start,elf1_finish = elf1.split('-')
        elf2_start,elf2_finish = elf2.split('-')
        elf1_range = [x for x in range(int(elf1_start),int(elf1_finish)+1)]
        elf2_range = [x for x in range(int(elf2_start),int(elf2_finish)+1)]
        if elf1_start == elf1_finish:
            elf1_range = [int(elf1_start)]
        if elf2_start == elf2_finish:
            elf2_range = [int(elf2_start)]
        any_overlap = 0

        for number in elf2_range:
            if number in elf1_range:
                any_overlap = 1
                continue
        
        for number in elf1_range:
            if number in elf2_range:
                any_overlap = 1

        if any_overlap >= 1:
            partial_overlap_pairs.append(num+1)


print("Teams with fully contained sections: ")
print(partial_overlap_pairs)
print()
print(f"Number of teams with full containment:  {len(overlap_team_num)}")
print(f"Number of team with partial overlap:    {len(partial_overlap_pairs)}")
"""

## DAY 5 ##
"""
stacks = [[],
["T","D","W","Z","V","P"],
["L","S","W","V","F","D","J"],
["Z","M","L","S","V","T","B","H"],
["R","S","J"],
["C","Z","B","G","F","M","L","W"],
["Q","W","V","H","Z","R","G","B"],
["V","J","P","C","B","D","N"],
["P","T","B","Q"],
["H","G","Z","R","C"]]


def prune_movements(line):
    line= line.strip('move ')
    for word in [' from ',' to ']:
        line = line.replace(word,'-')
    amount, start, end = line.split('-')
    return [int(amount),int(start),int(end)]

print(stacks[2][-1])

with open("crates.txt","r") as file:
    for line_num,line in enumerate(file):
        if line_num <= 9:
            continue
        if line_num > 9:
            command = prune_movements(line)
            amount, start, end = command

            for n in range(amount):
                stacks[end].append(str(stacks[start][-1]))
                stacks[start].pop(-1)


    top_crates = ""
    for stack_num,stack in enumerate(stacks):
        print(f"{stack_num}:  {stack}")
        if stack_num > 0:
            top_crates += (str(stack[-1]))
    
    for stack in stacks:
        print(stack)
    print(top_crates)
    
stacks = [[],
["T","D","W","Z","V","P"],
["L","S","W","V","F","D","J"],
["Z","M","L","S","V","T","B","H"],
["R","S","J"],
["C","Z","B","G","F","M","L","W"],
["Q","W","V","H","Z","R","G","B"],
["V","J","P","C","B","D","N"],
["P","T","B","Q"],
["H","G","Z","R","C"]] 

with open("crates.txt","r") as file:
    for line_num,line in enumerate(file):
        if line_num <= 9:
            continue
        if line_num > 9:
            command = prune_movements(line)
            amount, start, end = command

            for n in range(amount):
                stacks[0].append(str(stacks[start][-1]))
                stacks[start].pop(-1)

            for n in range(amount):
                stacks[end].append(str(stacks[0][-1]))
                stacks[0].pop(-1)
        

    top_crates = ""
    for stack_num,stack in enumerate(stacks):
        print(f"{stack_num}:  {stack}")
        if stack_num > 0:
            top_crates += (str(stack[-1]))
    
    for stack in stacks:
        print(stack)
    print(top_crates)   
"""
## DAY 6 ##
"""
character_required = 0
character_total = 0

with open("message.txt", "r") as file:
    for line in file:
        for index,character in enumerate(line):
            character_total += 1
            try:
                string_of_4 = str(f'{str(line[index])}{str(line[index+1])}{str(line[index+2])}{str(line[index+3])}')
                if string_of_4.count(string_of_4[0]) == 1 and string_of_4.count(string_of_4[1]) == 1 and string_of_4.count(string_of_4[2]) == 1:
                    if character_required == 0:
                        print(f'characters required =   {(index+3)+1}')
                        print(f'ID String =   {string_of_4}')
                        break
        
            except IndexError:
                print('End of file')

"""

character_required = 0
character_total = 0
with open("message.txt", "r") as file:
    for line in file:
        for index,character in enumerate(line):
            character_total += 1
            try:
                string_of_14 = ''
                for n in range(14):
                    string_of_14 += str(f'{str(line[index+n])}')
                valid = 0
                for m in range(len(string_of_14)):
                    if string_of_14.count(string_of_14[m]) == 1:
                        valid += 1
                        if valid == 14 and character_required == 0:
                            print(f'characters required =   {(index+13)+1}')
                            print(f'ID String =   {string_of_14}')
                            break
                    else:
                        continue
        
            except IndexError:
                print('End of file')
                break
