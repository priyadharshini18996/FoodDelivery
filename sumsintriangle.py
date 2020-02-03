
lst =[]
no=int(input('Enter no of rows and columns : '))
for i in range(no):
  
   lst1=list(map(int,input().split()))[:i+1]
   
   lst.append(lst1)
   

if no > 1: 
        lst[1][1] = lst[1][1]+lst[0][0] 
        lst[1][0] = lst[1][0]+lst[0][0] 
# Traverse remaining rows 
for row in range(2, no): 
        lst[row][0] = lst[row][0] + lst[row-1][0] 
        lst[row][row] = lst[row][row] + lst[row-1][row-1] 

    # Loop to traverse columns 
        for column in range(2,row): 
           
            if lst[row][column]+lst[row-1][column-1] >= lst[row][column]+lst[row-1][column]: 
                lst[row][column] = lst[row][column] + lst[row-1][column-1] 
            else: 
                lst[row][column] = lst[row][column]+lst[row-1][column] 

print("sum in triangle is:",(max(lst[no-1])))