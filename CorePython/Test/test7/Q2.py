# Write a python  program  that takes a list of strings as input 
# and return a new list containing the 
# uppercase versions of the strings using list comprehension

li=['apple','banana','cherry','dragonfruit']

li=[x.upper() for x in li]
print(li)