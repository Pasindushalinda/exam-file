# Q04b

# -----------------------------------------------------
# Write your code below this line
Numbers[0]=10
Numbers[1]=6
Numbers[2]=1
Numbers[3]=9
Numbers[4]=3

Count=0
Length=4
Midpoint=2
Temp=0
while True:
    if Count<Midpoint:
        Temp=Numbers[Count]:
            Numbers[Count]=Numbers[Length-Count]
            Numbers[length-count]=Temp
            Count=Count+1
   else:
       print("Stop")
       
