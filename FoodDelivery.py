input1 = raw_input().split() 
input1 = [int(i) for i in input1]
No_of_orders,deliveryman1_orders,deliveryman2_orders = input1 

input2 = raw_input().split()  
input2 = [int(i) for i in input2]
deliveryman1 = input2

input3 = raw_input().split() 
input3 = [int(i) for i in input3]
deliveryman2 = input3

input2.sort()
input2.reverse()
input3.sort()
input3.reverse()

deliveryman1_tips = 0
deliveryman2_tips  = 0
maximum_tip = 0
for i in range(No_of_orders):

        
    if (deliveryman1_tips  < deliveryman1_orders and deliveryman2_tips  < deliveryman2_orders and deliveryman1[deliveryman1_tips] >= deliveryman2[deliveryman2_tips]):
        maximum_tip += deliveryman1[deliveryman1_tips ]
        deliveryman1_tips  += 1
       
            
    elif (deliveryman1_tips  < deliveryman1_orders and deliveryman2_tips < deliveryman2_orders and deliveryman1[deliveryman1_tips] < deliveryman2[deliveryman2_tips]):
        maximum_tip += deliveryman2[deliveryman2_tips]
        deliveryman2_tips+=1
     
    elif (deliveryman1_tips  < deliveryman1_orders):
        maximum_tip += deliveryman1[deliveryman1_tips ]
        deliveryman1_tips  += 1
            
    elif (deliveryman2_tips < deliveryman2_orders):
        maximum_tip += deliveryman2[deliveryman2_tips]
        deliveryman2_tips += 1
    
        
print(maximum_tip)

   