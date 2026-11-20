# Q05c-------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------
maxi = 0
StrokeRating = 0

# Three arrays containing competitor details

Names = [["Smith", "John"], ["Perera", "Amal"], ["Fernando", "Nimal"]]

RaceScores = [[85, 92, 88], [95, 87, 90], [80, 85, 89]]

StrokeScores = [[70, 100, 80, 90],  [85, 80, 90, 95],   [60, 70, 75, 80]]

# Variables to store the championship winner
HighestPerformance = -1
WinnerIndex = -1


# =====> Write your code here
for i in RaceScores:
    for j in range(len(RaceScores)-1):
        if i[j] > i[j+1]:
            i[j+1],i[j] = i[j],i[j+1]
            print(RaceScores)

for h in StrokeScores:
    for s in range(len(StrokeScores)):
        if h[s] > h[s+1]:
            h[s+1],h[s] = h[s],h[s+1]
print(StrokeScores)        
    


# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------

# =====> Write your code here



# Process each competitor
for t in range(len(RaceScores)):
    performanceScore = RaceScores[t][0] + RaceScores[t][2]
    print('performance score for ' , Names[t][1],'is',performanceScore)


for k in range(len(StrokeScores)):
    StrokeRating = (StrokeScores[k][0] + StrokeScores[k][3])//2
    print('StrokeRating  for ' , Names[k][1],'is',StrokeRating )


# Display championship medal winner

for t in range(len(RaceScores)):
    performanceScore = RaceScores[t][0] + RaceScores[t][2]
    if performanceScore > maxi:
        maxi = performanceScore
print('the highest performace is :',maxi)

   





























