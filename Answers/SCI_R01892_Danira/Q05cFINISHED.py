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

#Subprogram to check whether a competitor is suitable for a certificate 
def certificate(maximumRaceScore, maximumStrokeScore, StrokeRating):
    check = False
    if (maximumRaceScore >= 90) and ((maximumStrokeScore == 100) or (StrokeRating > 75)):
        check = True
    return check

# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------
# =====> Write your code here
PerformanceScoreList = []
PerformanceScore = 0
StrokeRating = 0

# Process each competitor

#Traverses the list of names
for name in range(0, len(Names)):

    
    #Find the minimum and maximum race scores of the competitior
    minimumRaceScore = min(RaceScores[name])
    maximumRaceScore = max(RaceScores[name])

    #Find the minimum and maximum stroke scores of the competitior
    maximumStrokeScore = max(StrokeScores[name])
    minimumStrokeScore = min(StrokeScores[name])    

    #Calculate the performance score of the competitor
    PerformanceScore = (minimumRaceScore + maximumStrokeScore)
    PerformanceScoreList.append(PerformanceScore)

    #Calculate the stroke rating of the competitor
    StrokeRating = (maximumStrokeScore + minimumStrokeScore) / 2

    #Calling the subprogram
    certify = certificate(maximumRaceScore, maximumStrokeScore, StrokeRating)
    
    if certify == True:
        #Display competitors awarded certificates
        print(Names[name][0], "with a performance score of", PerformanceScore, "and a stroke rating of", StrokeRating, "is awarded a certificate")

#Find the highest performance score       
HighestPerformance = max(PerformanceScoreList)

for index in range(0, len(PerformanceScoreList)):
    if PerformanceScoreList[index] == HighestPerformance:
        WinnerIndex = index

print()

# Display championship medal winner
print("The champion is", Names[WinnerIndex][0], "with a lowest race score of", min(RaceScores[WinnerIndex]), ", a highest stroke score of", max(StrokeScores[WinnerIndex]), "and a performance score of", HighestPerformance)
