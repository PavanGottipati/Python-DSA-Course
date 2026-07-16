arr=[1,5,8,0,1,8,1,5,1]
dictionary={}
for i in arr:
    if i in dictionary:
        if dictionary[i]:
            dictionary[i]+=1
    else:
            dictionary[i]=1
print(dictionary)

dictionary[10]=[1,5,8,0,1,8,1,5,1]
print(dictionary)
dictionary[10,20]=[1,5,8,0,5,1]
print(dictionary)

