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
low_time=0
highscore=0
# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------
# =====> Write your code here



# Process each competitor

#Calculating perfomance score

for index in RaceScores:
   low_time=min(int(RaceScores[index]))
for index in StrokeScores:
    highscore=max(StrokeScores[index])

# Display championship medal winner


