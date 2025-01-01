#solving earth puzzle
#Tinashe Madzingaidzo

import time
from itertools import permutations


start_time = time.perf_counter()
letters = ["A", "E", "H", "N", "O", "R", "S", "T", "U", "W"]

directions = ["NORTH", "EAST", "SOUTH", "WEST"]

solutions_earth, solutions_letters, direction, num, tot = [], [], "", "", 0

perms_earth, perms_letters = permutations(range(10),5), permutations(range(10), 10)


for each in perms_earth:
    a = [str(i) for i in each]
    number = "".join(a)
    solutions_earth.append(int(number))

for each in perms_letters:
    j = [str(x) for x in each]
    
    earth_dict = dict(zip(letters, j))
    
    #north + east + south + west = tot
    for i in range(len(directions)):
        for j in directions[i]:
            direction += j
        for char in direction:
            num += earth_dict[char]
     
        tot += int(num)
        direction, num = "", ""

    if tot <= solutions_earth[-1]:
        solutions_letters.append(tot)
    
    tot=0   
 
same = set(solutions_earth) & set(solutions_letters)
if same:
    size = len(same)
    print(f"The number of possible solutions is {size}:")
    print(same)
    
end_time = time.perf_counter()

elapsed_time = end_time - start_time

print(f"Total time taken: {elapsed_time:.3f} seconds")
        