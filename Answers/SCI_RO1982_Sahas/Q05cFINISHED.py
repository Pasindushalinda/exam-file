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
minimum=RaceScores[0][0]
minimum_2=StrokeScores[0][0]
maximum=0
store_rating=0
performance_score=0



# Process each competitor
for i in range(0,len(Names)):
    for a in StrokeScores[i]:
        if a>maximum:
            maximum=a
        elif a<minimum_2:
            minimum_2=a
    for u in RaceScores[i]:
        if u<minimum:
            minimum=u
        if u>=90:
            certificate=True
    performance_score=minimum+maximum
    
    stroke_rating=(maximum+minimum_2)/2
    if certificate==True and (stroke_rating>75 or maximum==100):
        print("surname:",Names[i][1])        
        print("performance score:",performance_score)
        print("stroke rating:",stroke_rating)
    if performance_score>HighestPerformance:
        WinnerIndex=i
        Highest_performance=performance_score
        maximum_3=[i][0]
        minimum_3=[i][0]
        for s in StrokeScores[WinnerIndex]:
            if s>maximum_3:
                maximum_3=s
        
        for t in RaceScores[WinnerIndex]:
            if t<minimum_3:
                minimum_3=t

    
    
        
   

# Display championship medal winner
print("Champoinship medal winner")
print("Surname:",Names[WinnerIndex][1])
print("Lowest race score:",minimum_3)
print("Highest stroke score:",maximum_3)
print("Performance:",Highest_performance)
