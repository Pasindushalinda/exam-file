# Q03b

numberList = [5, 9, 13, 63, 65, 79, 86, 100]
start = 0
middle = 0
end = len(numberList) - 1
found = False
count = 0

# Add your code here
Item = int(input("Enter a number : "))
while start>= end and found == False:
    middle = (start+end)/2
    if numberList[middle]==item:
        found = True
    elif Item<numberList[middle]:
        end = middle-1
    else:
        start = middle+1

count+=1
# Do not add your own code below this line
    
# Result of the search is displayed (this has been done for you)

if found == True:
    print(Item, "was found in the list")
else:
    print(Item, "is not in the list")
