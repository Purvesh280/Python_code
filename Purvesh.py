print("hello world")
#string are anything in python include in single or double qoutes
str1 = 'yasham academy'
print(type(str1)) 

#operation  on strings'
#indexing

print(str1[0]) #positive indexing
print(str1[-14]) #negative indexing

#slicing
print(str1[0:6])
print(str1[-14:-8])
print(str1[-8:-14])

#step size
print(str1[0: :3])

#concatanation
str2 = 'is very good'
print(str1+str2)

print(str1,str2)

#Q1

str3= "Twinkle, twinkle, little star, \n \t How I wonder what you are!/n/t/t Up above the world so high, \n\t\t  Like a diamond in the sky. Twinkle, twinkle, little star, \n\t How I wonder what you are"
print(str3)

#Q2

#Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.

n1=input('Enter your first name=')
n2=input('Enter your last name=')
print(n2+' '+n1)