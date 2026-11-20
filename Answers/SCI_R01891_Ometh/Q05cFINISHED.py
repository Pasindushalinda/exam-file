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
def winner():
    flag = False
    if RaceScores >= 90 and (maxstroke == 100 or meanstroke > 75):
        flag = True
    return flag

# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------
# =====> Write your code here
perform = []

for name in Names:
    #getting the minimum and maximum scores of the race
    for i in RaceScores:
        minimumscore = min(i)
        maximumscore = max(i)
    break
    for x in StrokeScores:
        #getting the minimum and maximum of the stroke scores
        maxstroke = max(x)
        minstroke = min(x)
        #gettign stroke rate
        meanstroke = maxstroke + minstroke/len(StrokeScores)
    break 
    
    performancescore = minimumscore + maxstroke
    perform.append(performancescore)   
# Process each competitor

   

# Display championship medal winner

