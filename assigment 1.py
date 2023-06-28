#!/usr/bin/env python
# coding: utf-8

# # Q2..
# 

# In[1]:


#sum of 10 natural number using for loops
sum=0
for i in range(11):
    sum+=i
print(sum)


# In[2]:


#product of 10 natural number using for loop
pro=1
for i in range(1,11):
    pro=pro*i
print(pro)


# In[5]:


#sum of 10 natural number using while loop

i=1
sum=0
while(i<=10):
    sum=sum+i
    i=i+1
print(sum)


# In[6]:


#product of 10 number using for while loop
i=1
pro=1
while(i<=10):
    pro*=i
    i+=1
print(pro)


# # Q3..

# In[6]:


m=eval(input("Enter the units number"))
if( m<=100 and m>0):
    print ("the user will be charge Rs. 4.5 per unite and the total charge is  " , m*4.5)
elif(m<=200 and m>100):
    print(" the user will be charge Rs. 6 per unite and the total charge is :",m*6)
elif(m<=300 and m>200):
    print("the user will be charge Rs. 10 per unite  and the total charge is :",m*10)
else:
    print (" the user will be chare Rs.20 per unite and the total charge is :",m*20)


# # Q5...

# In[15]:


string = "I want to become a data scientist"

print ("the number of a is given string ")
print(string.count("a"))
print ("the number of e is given string ")
print(string.count("e"))
print ("the number of i is given string ")
print(string.count("i"))
print ("the number of o is given string ")

print(string.count("o"))
print ("the number of u is given string ")

print(string.count("u"))
print ("the number of I is given string ")
print(string.count("I"))



    


# # Q4...

# In[32]:


l=[]
for i in range(1, 101):
    print(i**3)
  


# In[ ]:




