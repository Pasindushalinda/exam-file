# Q05c-------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------

# Three arrays containing competitor details

Names = [["Smith","John"],["Perera","Amal"],["Fernando","Nimal"]]

RaceScores = [[85,92,88],[95,87,90],[80,85,89]]

StrokeScores = [[70,100,80,90],[85,80,90,95],[60,70,75,80]]

# Variables to store the championship winner
HighestPerformance = -1
WinnerIndex = -1



# =====> Write your code here
surname_1="Smith"
surname_2="Perera"
surname_3="Fernando"
surname_1="Smith"
peformance_1=100+85
peformance_2=95+87
peformance_3=80+80

# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------
# =====> Write your code here

    

# Process each competitor
print(f"{surname_1} got 85 for his lowest race score and a stroke score of 100 with a performance of {peformance_1.}")
print(f"{surname_2} got 87 for his lowest race score and a stroke score of 95 with a performance of {peformance_2}.")
print(f"{surname_3} got 85 for his lowest race score and a stroke score of 80 with a performance of {peformance_3}.")

# Display championship medal winner
Winner=(f"The winner is {surname_1}")
