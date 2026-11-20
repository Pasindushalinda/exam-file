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
performance_score1=int(Names[0:0:1],RaceScores[0,0])+100
performance_score2=int(Names[1:0:1],RaceScores[1,1])+95
performance_score3=int(Names[2:0:1],RaceScores[2,0])+80

# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------
# =====> Write your code here
stroke_rating1=Names[0:0:1],StrokeScores[0,1]+StrokeScores[0,0]/2
stroke_rating2=Names[1:0:1],StrokeScores[1,3]+StrokeScores[1,1]/2
stroke_rating3=Names[2:0:1],StrokeScores[2,3]+StrokeScores[2,0]/2


# Process each competitor
for RaceScore in RaceScores:
    if RaceScore >=90:
        for StrokeScore in StrokeScores:
            if StrokeScore==100 and stroke_rating1>75:
                print(Names[0:0:1],performance_score1,stroke_rating1,",earned a certificate")
                print(Names[1:0:1],performance_score2,stroke_rating2,",earned a certificate")
                print(Names[2:0:1],performance_score3,stroke_rating3,",earned a certificate")
if (performance_score1>performance_score2) and (performance_score1>performance_score3):
    print(Names[0:0:1],RaceScores[0,0],StrokeScores[0,1],performance_score1,"is the championship medal winner")
else:
    (performance_score2>performance_score1) and (performance_score2>performance_score3);
    print(Names[1:0:1],RaceScores[1,1],StrokeScores[1,3], performance_score2,"is the championship medal winner")
if (performance_score3>performance_score1) and (performance_score3>performance_score2):
     print(Names[2:0:1], RaceScores[2,0], StrokeScores[2,3], performance_score3,"is the championship medal winner")
                
        
    

# Display championship medal winner

