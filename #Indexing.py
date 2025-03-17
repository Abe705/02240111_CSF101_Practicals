#Indexing
str = "college"
print(str[-4:-1])

#endswith

str = "i am Abeshek"
print(str.endswith("shek"))
print(str.capitalize()) #Capitalize(inside the bracket nothing needed)
print(str.replace("a" , "o")) #Replaceing a with o
print(str.replace("Abeshek" , "Ronaldo"))
print(str.find("am")) # Be cautions as it counts from 0,1,2,..etc
print(str.count("e")) #it counts the repeated words

# Write a program to input users first name and find the length of it # find the occurance of the word
Name = input("Enter Your Name:")
print("So the length of your name is:", len(Name))


