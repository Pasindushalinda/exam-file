# Q05c-------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------

# Three arrays containing competitor details

Names = [["Smith", "John"], ["Perera", "Amal"], ["Fernando", "Nimal"]]

RaceScores = [[85, 92, 88], [95, 87, 90], [80, 85, 89]]

StrokeScores = [[70, 100, 80, 90],  [85, 80, 90, 95],   [60, 70, 75, 80]]

# Variables to store the championship winner
HighestPerformance = -1
WinnerIndex = -1


# =====> Write your code here

    


# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------
# =====> Write your code here
for index in range(0,len(Names)):
    print(Names[index][0]+" "+Names[index][1])
    highestvalue=-1
    lowestvalue=10000
    indexvalue=0
    while indexvalue<3:
        if RaceScores[index][indexvalue]<lowestvalue:
            lowestvalue=RaceScores[index][indexvalue]
            indexvalue=indexvalue+1
        else:
            indexvalue=indexvalue+1
    score=0
    while score<4:
        if StrokeScores[index][score]>highestvalue:
            highestvalue=StrokeScores[index][score]
            score=score+1
        else:
            score=score+1
    perfscore=lowestvalue+highestvalue
    print(perfscore)

    #Calculating the stroke rating
    highest=-1
    lowest=10000
    stroke=0
    while stroke<4:
        if StrokeScores[index][stroke]>highest:
            highest=StrokeScores[index][stroke]
            stroke=stroke+1
        elif StrokeScores[index][stroke]<lowest:
            lowest=StrokeScores[index][stroke]
            stroke=stroke+1
        else:
            stroke=stroke+1
        print(
            
# Process each competitor
    if perfscore>HighestPerformance:
        HighestPerformance=perfscore
        WinnerIndex=index
# Display championship medal winner
print("The winner is: ",Names[WinnerIndex][0],Names[WinnerIndex][1],"-",str(HighestPerformance))
