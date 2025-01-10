#CheatSheet

#Dictionary (also know as a hashmap):
#Creation: 
CharMaps = {}
#Can use 
charMaps = defaultdict(list) 
#to make it so the dictionary automatically creates a key value pair with an empty list (or w/e I choose)
#Appending:
CharMaps["thing"] = "this"
#Checking Existence:
if "thing" in CharMaps:
#Update
my_dict.update({"b": 2}) # Adds "b" to the dictionary
#Can be used to create or to update a dictionary
#Sorting a Dictionary
sorted(topK.items(), key=lambda item: item[1], reverse=True)
#Find if a value is in a dictionary
board[r][c] in cols[c] # Just put what every value followed by the dictionary you want to check.. This may be more of a set function as that is what was used


#List:
#Creation
#list can be created with just [0,1]
myList = []
#append
myList.append(k)
#Enumerate:
#Use this when you want to iterate over a list and reference the indices
for j, num in enumerate(nums):
#SET

#Pros of set:
#Efficient Membership Checks:

#O(1) on average due to hash table implementation.
#Example: board[r][c] in cols[c].
#Handles Duplicates Automatically:

#Since set does not allow duplicate values, you don’t need to write additional logic to prevent adding the same number multiple times.
#Fast Insertions:

#Adding elements to a set is O(1) on average.


#Useful Python Functions:
#Sorted: takes any iterable (e.g., a string, list, tuple, etc.) and returns a new sorted list of its elements.
result = sorted("hello")
print(result) # Output: ['e', 'h', 'l', 'l', 'o']
#Cool Use to sort dictionaries
sorted(topK.items(), key=lambda item: item[1], reverse=True)
#join: 
#method takes a list (or any iterable) of strings and combines them into a single string. 
"".join(['a', 'e', 't']) # Output: "aet"


#Linked List
#Reference the classes given you to find the child node. It's easy to go back and forth setting child and parent to other nodes.