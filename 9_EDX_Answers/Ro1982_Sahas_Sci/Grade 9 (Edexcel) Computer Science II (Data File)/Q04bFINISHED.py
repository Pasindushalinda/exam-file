# Q04b

# -----------------------------------------------------
# Write your code below this line
Numbers=[10,6,1,9,3]
Count=0
Lengh=4
Midpoint=2
Temp=0
while Count<Midpoint:
    Temp=Numbers[Count]
    Numbers[Count]=Numbers[Lengh-Count]
    Numbers[Lengh-Count]=Temp
    Count=Count+1
    
    
    



