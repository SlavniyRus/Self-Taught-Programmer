import csv

list_film = [["Zvezd voin", "Terminator", "AI"],
             ["Fool", 'Matild', "Lefiafan"],
             ["People in black", "I'm - ROBOT", "Evolution"]]

with open("list_film.csv", "w") as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=",")
    for list in list_film:
        spamwriter.writerow(list)
