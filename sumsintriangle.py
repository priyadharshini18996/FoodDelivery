
lst =[]
no=int(input('Enter no of rows and columns : '))
for i in range(no):
  
   lst1=list(map(int,input().split()))[:i+1]
    
   lst.append(lst1)

for j in range(no-1,-1,-1):
     for k in range(j):
             if lst[j][k]>lst[j][k+1]:
                lst[j-1][k]+=lst[j][k]
             else:
                lst[j-1][k]+=lst[j][k+1]

print("sums of triangle is =", (lst[0][0]))
