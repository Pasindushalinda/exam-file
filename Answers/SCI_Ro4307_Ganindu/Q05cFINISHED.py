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
jhonPS=85+100
pereraPS=87+95
fernandoPS=80+80
# Process each competitor
print( "Smith","performance score",jhonPS,"stroke rating",round(340/4),"%")
print( "perera","performance score",pereraPS,"stroke rating",round(350/4),"%","awarded a certificate")
print( "fernando","performance score",fernandoPS,"stroke rating",round(265/4),"%")

# Display championship medal winner

print("smith","lowest race score",85,"highest stroke score",100,"performance score",jhonPS,"CHAMPIONSHIP MEDAL WINNER")
print
