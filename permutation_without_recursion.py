string = str(input("Enter a string:"))
count = 1
o = list(string)
print(string)
a=[[]]
for i in range(len(o)-2,-1,-1):
    at = []
    for j in range(i+1,len(o)):
        for k in range(len(a)):
            temp =[]
            temp.append((i,j))
            temp += a[k]
            oc = o[:]
            for l in temp:
                oc[l[0]],oc[l[1]] = oc[l[1]], oc[l[0]]
                print("".join(oc))
                count+=1
            at.append(temp)
    a = at[:]

print('number of permutation:', count)
