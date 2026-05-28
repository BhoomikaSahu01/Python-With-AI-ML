# python dictionary
'''pol_eng_dictionary = {
  "zamek": "castle",
   "woda": "water",
  "gleba" : "soil"

}

if "zamek1" in pol_eng_dicitonary:
    print("yes zamek 1 is present in the dictionary")
else:
    print("No zamek1 is not present in the dictionary")
    
print(pol_eng_dictionary)
print(len(pol_eng_dictionary))

del pol_eng_dictionary["zamek"]
print(pol_eng_dictionary)
print(len(pol_eng_dictionary))

pol_eng_dictionary.clear()
print(pol_eng_dictionary)
print(len(pol_eng_dictionary))

del pol_eng_dictionary
print(Pol_)

sd = {}

while True:
    name = input("enter student's name:")
    if name == "":
        break
    score = int(input(f"Enter {name}'s score:"))
    
    if score not in range(1, 11):
        break
    if name in sd:
        sd[name] += (score,)
    else:
        sd[name] = (score,)
        
    
print(sd)

for name,mark in sd.items():
    sum = 0
    for m in mark:
        
        sum += m
    print(name, "->", sum/len(mark))'''
        
