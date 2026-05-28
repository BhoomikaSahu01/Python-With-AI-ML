# Tuple
'''my_tuple = (10, 100, 1000)
my_tuple += (10000, 100000)
print(my_tuple)'

tuple_1 = (1, 2, 3)
for elem in tuple_1:
    print(elem)
    
tuple_2 = (1, 2, 3, 4)
print(5 in tuple_2)
print(5 not in tuple_2)

tuple_3 = (1, 2, 3, 4)
print(len(tuple_3))
print(5 not in tuple_3)

tuple_4 = tuple_1 + tuple_2
tuple_5 = tuple_3 * 2
print(tuple_4)
print(tuple_5)

my_tuple = tuple((1, 2, "string"))
print(my_tuple)
print(type(my_tuple))

my_list = [2, 4, 6]
print(my_list)
print(type(my_list))
tup = tuple(my_list)
print(tup)
print(type(tup))

var = 123
t1 = (1,)
t2 = (2,)
t3 = (3, var)
t1, t2, t3 = t2, t3, t1
print(t1, t2, t3)

# how to make a dictionary
dictionary = {
    "cat" : "chat",
    "dog" : "chien",
    "horse": "cheval"
}

phone_numbers = {
         'boss': 553672873, 'suzy': 894673893
}
empty_dictionary = {}

print(dictionary)
print(phone_numbers)
print(empty_dictionary)
print(dictionary['cat'])
print(phone_numbers['suzy'])
# print(phone_numbers['president'])
words = ['cat', 'lion', 'horse']
for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word," is not in dictionary")
        
print(dictionary.keys())
for key in dictionary.keys():
    print(key, "->", dictionary[key])
    
print(dictionary.items())
    
for key, value in dictionary.items():
     print(key, "->", value)
     print(dictionary.values())
     
for value in dictionary.values():
    print(value)
        
# Keys method

pol_eng_dictionary = {
    "zamek": "castle",
    "woda": "water",
    'gleba': "soil"
    
}
print("pol_eng_dictionary: ",pol_eng_dictionary)
copy_dictionary = pol_eng_dictionary.copy()
print("copy_dictionary:", copy_dictionary)

pol_eng_dictionary["zamek"] = "lock"
item = pol_eng_dictionary["zamek"]
print(item)

phonebook = {}
print(phonebook)
phonebook["Adam"] = 78367837457 
print(phonebook)

del phonebook["Adam"]
print(phonebook) '''

pol_eng_dictionary = {"kwiat": "flower"}

pol_eng_dictionary.update(
    {
        "gleba": "soil"
    }
)
print(pol_eng_dictionary)
pol_eng_dictionary.popitem()
print(pol_eng_dictionary)
        
