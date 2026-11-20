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
maxPerformanceScores = []    #list to score all the performance scores
strokeRating = []   #list to store all the stroke ratings
certificateCompetitor = []  #list to store all the certificate winners

# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------
# =====> Write your code here

# Process each competitor
for i in range(len(RaceScores)):
    maxPerformanceScores.append(int(min(RaceScores[i])) + max(StrokeScores[i]))   #calculating performance scores of all players




for index in range(len(StrokeScores)):
    strokeRating.append((min(StrokeScores[index])) + (max(StrokeScores[index])/2))   #calculating stroke scores of players




for scores in range(len(RaceScores)):
    if max(RaceScores[scores]) >= 90:
        print("certificate winners:",Names[scores][0]+"- performance score: ",str(maxPerformanceScores[scores])+" stroke rating: ",str(strokeRating[scores]))    #determining the certificate winners

        
   
for medalWinner in range(len(maxPerformanceScores)):
    if maxPerformanceScores[medalWinner] == max(maxPerformanceScores):
        print((Names[medalWinner][0]) + str(min(RaceScores[medalWinner]) )+ str(max(StrokeScores[medalWinner]) )+ str(maxPerformanceScores[medalWinner]))    #printing the certificate winners with other features
                                                
# Display championship medal winner

for medalWinner in range(len(maxPerformanceScores)):
    if maxPerformanceScores[medalWinner] == max(maxPerformanceScores):     #printing the medal winner/s with other features
        print("ChampionShip medal winner:",(Names[medalWinner][0]) + "- lowest race score:",str(min(RaceScores[medalWinner]) )+" highest stroke score:", str(max(StrokeScores[medalWinner]) )+" performance score:"+ str(maxPerformanceScores[medalWinner]))
