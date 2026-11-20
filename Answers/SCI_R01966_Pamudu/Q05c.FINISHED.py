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
for points in StrokeScores:
    points=int(points)
    if points>=100:
        index=StrokeScores.index(points)
        if index>=0 and index<=3:
            print(Names[1][0])
        elif index>3 and index<=7:
            print(Names[3][2])
        elif index>7 and index<=11:
            print(Names[5][4])
        


# Process each competitor

   

# Display championship medal winner

