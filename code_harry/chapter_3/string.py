#string can be written in 3 ways 

name='harry'
name1= "harry"
name2="'harry'" #this triple inverted comma is use to write multiple string

#string is immutable = means we cannot change it

nameshort= name[0:3] #here we use indexing and find the number from 0 index to 2 not 3
print(nameshort)  #result = har (means 0 to 2 index not 3 included)

namenum = name[4]
print(namenum) #its use to find character on particular index

print(len(name)) #length of string is print

#negative slicing
print(name[-4:-1])