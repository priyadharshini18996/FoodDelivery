
lst =[]
no=int(input('Enter no of rows and columns : '))
for i in range(no):
  
   lst1=list(map(int,input().split()))[:i+1]
    
   lst.append(lst1)

for row in range(no-1,-1,-1):
     for column in range(row):
             if lst[row][column]>lst[row][column+1]:
                lst[row-1][column]+=lst[row][column]
             else:
                lst[row-1][column]+=lst[row][column+1]

print("sums of triangle is =", (lst[0][0]))
