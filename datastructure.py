#Arrays [1,2,3,4,5]
# variable = [11,2,34,56,7,8]
# variable = ["ABCD",1,5,True,1.5]
# print(variable)

# variable = list() # [] -> [50,60]
# variable.append(50)
# variable.append(60)
# print(variable)

#Set
# variable2 = [1,2,2]
# variable = {1,2,2} #set unique Values
# print(variable)
# print(variable2)

#Tuple
#Dict
# diction = { #KEY- VALUE Pairs #KEYS -> UNIQUE, #VALUES DUPLICATES 
#     "id":1,
#     "Name":"ANish Kumar"
# }
# diction["Company"] = "ABC"
# diction["id"] = "Anish KUMAR"
# print(diction["id"])
# print(diction["Name"])
# print(diction)

# dicta = {"id":[],"PYTHON":1,"Asdasd":"ugga bugga"}
# dicta["id"].append(50)
# print(dicta.keys())

# immutable
# st = "THIS IS GREAT WORLD" + "******######123019u30uqwdnsakx a;lcmasdakdmam091308943u60564464+645-g55"
# temp = st[0]
# print(temp)
# st2 = " BUT I Don't LIKE It"
# temp = st+st2 +"  AM HAPPY"
# print(temp)
# print(len(st))

# QUESTION LIST SMallest
# ls = [9,1,10,0,21,24,45]
# ls.sort()
# print(ls[0])

# ls[0] = 12
# print(ls)

# tup = ("MILKSHAKE","BANANA","ICECREAM","", "QWEC")
# t1 = ("CHOCOLATE CAKE",)
# tupla = tup + t1
# print(tupla)
# print(tup)
# print(type(tup))
# tup = list(tup) #TYPECASTING
# print(type(tup))
# tup.append("VANILLA CAKE")
# tup = tuple(tup)
# print(tup)
# st = {1,1,1,1,1,1} # DUPLICATES ELEMENT NOT TAKEN HERE, UNIQUE ELEMENT
# print(st)
# st.add(45)
# st.remove(45)
# print(st[0])





# ls = [1,2,3,4,5,6,7,8,9,10]
# ls = [1,7,43,9,5,1,0]
# print(ls)
# ls.sort()
# print(ls)
# ls.append(5)
# ls.append(6)
# ls.append(1) # [5,6,1]
# temp = ls[1:10]
# print(temp)
# temp2 = ls[5:]
# print(temp2)
# temp3 = ls[-5:]
# print(temp3)
# print("FIRT ELEMENT", ls[0])
# print("LAST ELEMENT", ls[2])
# print("LAST ELEMENT", ls[-1])
# ls.append("BANANA")
# print(ls)
# ls.remove(5)
# print(ls)
# ls.pop()
# print(ls)

# set1 = {1,2,3,4,5}
# set2 = {5,6,7,8}
# set3 = set1.union(set2)
# set4 = set1.intersection(set2)
# print(set1.union(set2))
# print(set4)


dictionary = {"Roll No." : 1,
              "Name":["Kumar","Kumar2"],
              1 : ["Asdadsa"]} #key-value pairs store krna
# print(dictionary)
# print(dictionary["Name"])
# print(dictionary["Roll No."])
# print(dictionary[1])

dictionary["Roll No."] = 3
#print(dictionary)
tup = (("Roll NO.",3),("Name",["Kumar","Kumar2"]))
# for i,j in tup:
#     print(i,j)

print(dictionary.items())
# for i,j in dictionary.items():
#     print(i,j)