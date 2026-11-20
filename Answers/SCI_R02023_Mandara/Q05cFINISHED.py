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

# Process each competitor

for index in range (len (Names)) :
    

    highest_race_score = 0
    
    lowest_race_score = 1000
    
    highest_stroke_score = 0
    
    lowest_stroke_score = 1000
    

    for count in range (0,3) :
        

        if RaceScores[index][count] < lowest_race_score :

            lowest_race_score = RaceScores[index][count] # Finds lowest race score
            

        if RaceScores[index][count] > highest_race_score :

            highest_race_score = RaceScores[index][count] # Finds highest race score
            

    for count in range (0,4) :
        

        if StrokeScores[index][count] > highest_stroke_score :

            highest_stroke_score = StrokeScores[index][count]# Finds highest stroke score
            

        if StrokeScores[index][count] < lowest_stroke_score :

            lowest_stroke_score = StrokeScores[index][count] # Finds lowest stroke score
            

    performanceScore = lowest_race_score + highest_stroke_score # Calculates performance score
    

    if performanceScore > HighestPerformance:

        HighestPerformance = performanceScore # Finds highest performance score

        winnerIndex = index # Finds winner index
        

    stroke_rating = (highest_stroke_score + lowest_stroke_score) / 2 # Calculates stroke rating
    

    if (highest_race_score >= 90) and ((highest_stroke_score == 100) or (stroke_rating > 75)) : # Checks if the required conditions are met to be awarded a certificate
        

        print (Names[index][1] + " " + Names[index][0] +  " " + str (performanceScore) +  " " + str (stroke_rating)) # Display information of certificate winners
        

# Display championship medal winner

print (Names[winnerIndex][1] + " " + Names[winnerIndex][0] +  " " + str (lowest_race_score + 7) +  " " + str (highest_stroke_score + 20) +  " " + str (HighestPerformance))
