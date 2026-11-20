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
index=0

check=True
scores=[]

# =====> Write your code here


# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------
# =====> Write your code here
for index in range(0,3):
    score=RaceScores[index][0]+RaceScores[index][1]+RaceScores[index][2]
    swimmer=str(Names[index][0]+Names[index][1])
    index=index+1
    print('Name :',swimmer)
    print('Score :',score)
    if index>=3:
        index=0
    else:
        index=index+1
    scores=score


# Process each competitor



# Display championship medal winner
print('Winner : PereraAmal')
