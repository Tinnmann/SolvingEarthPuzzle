#solving earth puzzle
#Tinashe Madzingaidzo

import time
from itertools import permutations

start = time.perf_counter()
letters = ["A", "E", "H", "N", "O", "R", "S", "T", "U", "W"]

directions = ["NORTH", "EAST", "SOUTH", "WEST"]

solutions = []
sol=[]
list_dicts = []
ans = ""
num = ""
tot=0


combos_earth = permutations(range(10),5)
combos_letters = permutations(range(10), 10)

for each in combos_earth:
    a = list(each)
    b = [str(i) for i in a]
    number = "".join(b)
    solutions.append(int(number))

for each in combos_letters:
    j = [str(x) for x in each]
    
    earth_dict = dict(zip(letters, j))
    
    #north + east + south + west = tot
    for i in range(len(directions)):
        for char in directions[i]:
            ans += char
        for char in ans:
            num += earth_dict[char]
     
        tot += int(num)
        
        ans = ""
        num = ""
    
    if tot <= max(solutions):
        sol.append(tot)
        # list_dicts.append(earth_dict)
    
    tot=0
    


   
same = set(solutions) & set(sol)
if same:
    print(same)
end = time.perf_counter()

elapsed = end - start

print(f'Time taken: {elapsed:.6f} seconds')
        