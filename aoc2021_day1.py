#question 1
f = open("input.csv", "r")
j = ""
counter = 0
for x in f: 
    i = x
    counter +=1 if j < i else False
    j = i
print(counter)

#question 2
f = open("input.csv", "r")
counter,j,k,l=0,int(f.readline().strip()),int(f.readline().strip()),int(f.readline().strip())
for i in f:
    counter += 1 if int(i)+j+k > j+k+l else False
    j,k,l=int(i),j,k
print(counter)
