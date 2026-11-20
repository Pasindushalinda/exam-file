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
lowestRace = -1
NList = []
highest = 0
    
performanceScore = 0
lowestRace = 0
# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------
# =====> Write your code here
for name in Names:
    surname = name[0]
#Calculate lowest Race----------------------------------    
for index in range(len(RaceScores)):
    if RaceScores[index][0] < RaceScores[index][1]:
        lowestRace = RaceScores[index][0]
    elif RaceScores[index][1] < RaceScores[index][2]:
        lowestRace = RaceScores[index][1]
    else:
        lowestRace = RaceScores[index][2]
    #Calculate Highest Stroke--------------------------------
    for index in range(0,len(StrokeScores)):
        if StrokeScores[index][0] > StrokeScores[index][1]:
            highest = StrokeScores[index][0]
        if StrokeScores[index][1] > StrokeScores[index][2]:
            highest = StrokeScores[index][1]
        if StrokeScores[index][2] > StrokeScores[index][3]:
            highest = StrokeScores[index][2]
        else:
            highest = StrokeScores[index][3]
            
        print(highest)

    #Calculate performance Score------------------------
    performanceScore = lowestRace + highest

    NList.append(performanceScore)
print(NList)
#Checking highest performance-------------------------------
if NList[0] > NList[1]:
    HighestPerformance = NList[0]
elif NList[1] > NList[2]:
    HighestPerformance = NList[1]
else:
    HighestPerformance = NList[2]
print(HighestPerformance)
#Checking highest competitor-------------------------------
HighestCompetitor = Names[1][0]
print(HighestCompetitor)

strokeRating = (StrokeScores[1][1] + StrokeScores[1][3])/2 #Calculate stroke rating of highest competitor------------


        
   


# Process each competitor
        

# Display championship medal winner
print("The winner is:",HighestCompetitor,"with a performance of:",HighestPerformance, "and a stroke rating of:",strokeRating)
