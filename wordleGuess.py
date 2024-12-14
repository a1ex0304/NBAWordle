import csv
import random

teams = []
conference= []
lastChip = []
founded = []
colour1 = []
colour2 = []
colour3 = []

correctTeamData = {}

def setupLists(filename):
    with open(filename, 'r', encoding='utf8') as wordleFile:
        fileContent = csv.reader(wordleFile)
        next(fileContent)
        for line in fileContent:
            teams.append(line[0])
            conference.append(line[1])
            lastChip.append(line[2])
            founded.append(line[3])
            colour1.append(line[4])
            colour2.append(line[5])
            colour3.append(line[6])                 


def getRandomTeamData():
    correctTeam = random.choice(teams)
    correctTeamIndex = teams.index(correctTeam)
    correctTeamData = {
        "Team": teams[correctTeamIndex],
        "Conference": conference[correctTeamIndex],
        "Last Championship": int(lastChip[correctTeamIndex]) if lastChip[correctTeamIndex].isdigit() else lastChip[correctTeamIndex],
        "Founded": int(founded[correctTeamIndex]),
        "Colour1": colour1[correctTeamIndex],
        "Colour2": colour2[correctTeamIndex],
        "Colour3": colour3[correctTeamIndex]
    }
    return correctTeamData
       
def getGuessedTeamData(guessedTeam):
    guessedTeamIndex = teams.index(guessedTeam)
    guessedTeamData = {
        "Conference": conference[guessedTeamIndex],
        "Last Championship": int(lastChip[guessedTeamIndex]) if lastChip[guessedTeamIndex].isdigit() else lastChip[guessedTeamIndex],
        "Founded": int(founded[guessedTeamIndex]),
        "Colour1": colour1[guessedTeamIndex],
        "Colour2": colour2[guessedTeamIndex],
        "Colour3": colour3[guessedTeamIndex]
    }
    return guessedTeamData 

def inputTeam():
    setupLists("C:/Users/Alex Vong/PycharmProjects/wordleSideProject/sportwordle.csv")
    while True:
        guessedTeam = str(input("Enter Team: "))
        guessedTeam = " ".join([word.capitalize() for word in guessedTeam.split()])

        if " " not in guessedTeam:
            print("Enter the full team name")

        elif (guessedTeam not in teams):  
            print("This team is not a NBA Team+\n")

        else:
            return guessedTeam          

def wordleGuessing():
    setupLists("C:/Users/Alex Vong/PycharmProjects/wordleSideProject/sportwordle.csv")

    global correctTeamData
    correctTeamData = getRandomTeamData()
    #print(correctTeamData)
    correctGuess = False
    attempts = 5

    while not correctGuess:
        guessedTeam = inputTeam()
        guessedTeamData = getGuessedTeamData(guessedTeam)

        allCorrect = True

        if attempts > 0:
            attempts = attempts - 1
            print("Attempts remaining: "+str(attempts)+"\n")
            for i in correctTeamData:
                if i == "Team":
                    continue
                
                if correctTeamData[i]!=guessedTeamData[i]:
                    allCorrect = False
                    
                    if isinstance(correctTeamData[i], int):  
                        if correctTeamData[i]>guessedTeamData[i]:
                            if guessedTeamData[i] == 0:
                                print(f"Incorrect {i}: Your guess was {guessedTeamData[i]}(never), but the correct value is higher")
                            else:
                                print(f"Incorrect {i}: Your guess was {guessedTeamData[i]}, but the correct value is higher")

                        elif correctTeamData[i]<guessedTeamData[i]:
                            if guessedTeamData[i] == 0:
                                print(f"Incorrect {i}: Your guess was {guessedTeamData[i]}(never), but the correct value is higher")
                            else:
                                print(f"Incorrect {i}: Your guess was {guessedTeamData[i]}, but the correct value is lower")
                          
                    else:
                        print(f"Incorrect {i}: Your guess was {guessedTeamData[i]}")

                else:
                    print(f"Correct {i}: Your guess was {guessedTeamData[i]}") 

            if allCorrect:
                print(f"The team was {correctTeamData['Team']} You guessed it correct in "+str(5-attempts)+" tries")   
                correctGuess = True

        else:
            print("You ran out of attempts, please try again")
            print(f"The correct team was the {correctTeamData['Team']}")
            correctGuess = True
