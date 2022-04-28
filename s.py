# QUESTIONS
# str1 = "Welcome to my Blog"
# print(len(str1.rstrip('og')))
# print(len(str1.lstrip('We')))
# print(len(str1.strip('Welog')))
# print(len(str1))
# translate function

# S = "Welcome to my Blog"
# print(S[2 : 3])
# print(S[2 : 10])
# print(S[-2 : ]) 

# print(S[-10 : -2 : 2])

# str1= "Amit"
# str2 = "My Blog"
# str3 = "#blog"
# str4 = "My 1st Blog"
# print(str1.isalpha())
# print(str2.isalpha())
# print(str3.isalpha())
# print(str4.isalpha())

# s=   "  "
# print(s.upper())
# print(s.lower())
# print(s.islower())
# print(s.isupper())
# print(s.isalpha())
# print(s.translate("My"))
# print(s.isspace())

# str2 = "  ###Welcome to my Blog  " 
# print(len(str2))
# print((str2.lstrip()))

# str1 = "lelcoMe To my Blog"
# print(len(str1))
# print(str1.capitalize())

# str1 = "Welcome to my Blog"
# x = str1.split()
# print(x)

# a = "Mummy?Papa?Brother?Sister?Uncle" 
# print(a.split())
# print(a.split('?'))
# print(a.split('?',1))
# print(a.split('?',3))
# print(a.split('?',10))
# print(a.split('?',-1))

# x = 100
# y = 50
# print(x and y)

# a = 4
# b = 11
# print(a | b)
# print(a >> 2)

# print(3**2 ** 2)
# print(2 * 3 ** 3 * 4)
# print(4/(3*(2-1)) and 4/3*(2-1))

# A=16
# B=15
# print(60// 20%2)
  
# x = int(43.55+2/2)
# print(x)

# print(2+4.00 and 2**4.0)
# print(8/4/2)

# print(['hello', 'morning'][bool('')])
# l=[1, 0, 2, 0, 'hello', '', []]
# print(list(map(bool, l)))

# class Truth:
#      pass
# x=Truth()
# print(bool(x))

# EXPANDED FORM
# name1=int(input("enter number"))
# name2=str(name1)
# s=""
# for i in range(len(name2)):
#      length=len(name2)-i-1
#      s+=name2[i]+"0"*length
#      if length==0:
#           pass
#      else:
#          s+="+" 
# print(s)

# a=["s001","s002","s003"]
# b=["sakshi","achal","shreya"]
# c=[20,30,40]
# d={}
# for i in range(len(a)):
#      d.update({a[i]:{}})
# # print(d)
# for i in range(len(d)):
#     d[i].update({b[i]:c[i]}) 
# print(d)

# g=[]
# d={}
# for i in range(len(a)):
#      s={}
#      for j in range(1):
#           s.update({b[i]:c[i]})
#           d.update({a[i]:s})
# g.append(d)
# print(g)

# import random
# l=['Python', 'list', 'exercises', 'practice', 'solution']
# random.shuffle(l)
# print(l)

# dict={"a":{"b":{}},"d":{"e":{}},"f":{"g":{}}}
# dic={}
# for i in dict:
#    for j in dict[i]:
#      # i,j=j,i 
#      dict["a"]=dict["b"]
#      print(dict)

# l=['1', '2', '3', '4', '5', '6', '7', '8']
# # ['12', '34', '56', '78']
# d=[]
# i=0
# while i<len(l):
#      j=0
#      while j<len(l)-1:
#           s=j+1
#           if l[i] not in d:
#                d.append(l[i])
#                d.append(l[s])
#           j=j+1
#      i=i+1
# print(d)

# n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
# x=[]
# i=0
# while i<len(n):
#       j=0
#       count=0
#       while j<len(n):
#             if n[i]==n[j]:                   
#                count=count+1                                      
#             j=j+1 
#       print(n[i],"count",count)      
#       if n[i] not in x:
#          x.append(n[i])
#       else:
#          count=count+1                    
     #     print(n[i],count)                          
     #  i=i+1

# l=[1,2,6,8,4,3,9,5]
# b=[]
# i=0
# while i<len(l)-1:
#     j=i+1
#     k=str(l[i])+str(l[j])
#     b.append(k)
#     i=i+2
# print(b) 

# list1=['one','two','three','four','five']
# list2=[1,2,3,4,5] 
# c={}            
# for i in range(len(list1)):
#     c[list1[i]]= list2[i]
# print(c)

# dict1 =  {
#    'Alex': ['subj1', 'subj2', 'subj3'], 
#    'David': ['subj1', 'subj2']}
# count=0
# for i in dict1:
#    for j in dict1[i]:                 
#       count=count+1
#       print(i,j)
# print(count)

# l=[1, 3, 5, 7, 9, 11, 0, 2, 4, 6, 8, 10, 8, 9, 0, 4, 3, 0]
#  op-[1, 3, 5, 7, 20, 9, 11, 0, 2, 20, 4, 6, 8, 10, 20, 8, 9, 0, 4, 20, 3, 0]
# i=4
# while i<len(l):
#     l.insert(i,20)
#     i=i+4
# print(l)

# aList = [4, 6, 8, 24, 12, 2]
# aList.sort(reverse=True)
# print(aList.pop(0))

# DICTIONARY

# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# for i in d1:
#     if i in d2:    
#         d2.update({i:d1[i]+d2[i]})
#     else:
#         d2.update({i:d1[i]})
# print(d2)
    
# s='w3resource'
# d={}
# for i in s:
#    count=0       
#    for j in s:
#        if i==j:
#            count+=1      
#        d.update({i:count})
# print(d)
 
# dic={1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# # ascending order by value :  [(0, 0), (2, 1), (1, 2), (4, 3), (3, 4)]
# # descending order by value :  {3: 4, 4: 3, 1: 2, 2: 1, 0: 0}
# for i in dic.keys():
#     dic.sort(i)
# print(dic)

# lis=[[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]
# # Convert the said list of lists to a dictionary:
# # {1: ['Jean Castro', 'V'], 2: ['Lula Powell', 'V'], 3: ['Brian Howell', 'VI'], 4: ['Lynne Foster', 'VI'], 5: ['Zachary Simon', 'VII']}
# dic={}
# for i in range(len(lis)):
#       l=[]
#       s=0      
#       for j in range(len(lis[i])):
#           p=""  
#           if (type(lis[i][j])==str):  
#               p+=lis[i][j]
#               l.append(p) 
#           else:
#               s+=lis[i][j] 
#       dic.update({s:l})
# print(dic)

# dic={'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 'h': 8, 'i': 100}
# op-['f', 'i', 'g', 'd', 'c']
# l=[]
# max=0
# for i in dic:
#     if dic[i]>max:
#         max=dic[i]
#         s=i
# l.append(s)
# dic.pop(s)
# smax=0
# for j in dic:
#     if dic[i]>smax:
#         smax=dic[i]
#         p=i
# l.append(p)
# dic.pop(s)

# dict1={1:10, 2:20}
# dict2={3:30,4:40}
# dict3={5:50,6:60}
# DICT={}
# for i in (dict1,dict2,dict3):
#     DICT.update(i)
# print(DICT)

# dict_num={1:10,2:20,3:30,4:40,5:50,6:60}
# count=0
# print("keys","values","count") 
# for i in dict_num:
#     count=count+1
#     print(i,"  ",dict_num[i],"   ",count)

# ans={'yellow':[1,3],'blue':[2,4],'red':[1]}
# dic=[('yellow',1),('blue',2),('yellow',3),('blue',4),('red',1)]
# Dic={}
# s=[]
# for i in range(len(dic)):            
#     for j in dic[i]:                         
#         for k in dic[i]:
#             if j==k:
#                 Dic.update({j:[j]})     
# print(Dic)                           

# DIC={'science':[88,89,62,95],'language':[77,78,84,80]}
# dict1={}
# lis=[]
# for i in DIC:
#    for j in range(len(DIC[i])):
#         dict1[i]=DIC[i][j]
#         lis.append(dict1)
# print(lis)