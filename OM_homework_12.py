import random
import csv

''' 
1. Write a program that generate 26 text files named A.txt, B.txt, and so on up to Z.txt
To each file append a random number between 1 and 100.
Create a summary file (summary.txt) that contains name of the file and number in that file: A.txt: 67, B.txt: 12 ...
'''
summary_file = open('summary.txt', 'w')
for letter in [chr(i) for i in range(ord('A'), ord('Z')+1)]:
    with open(f'{letter}.txt', 'w') as files:
        random_number = random.randint(1, 100)
        files.write(f'{random_number}')  # to each file append a random number between 1 and 100
        summary_file.write(f'{letter}.txt: {random_number}\n')

'''
2. Create file with some content. 
Create second file and copy content of the first file to the second file in upper case.
'''
some_text = [
    'Тому що ніколи тебе не вирвеш,\n',
    'ніколи не забереш,\n',
    'тому що вся твоя свобода\n',
    'складається з меж,\n',
    'тому що в тебе немає\n',
    'жодного вантажу,\n',
    'тому що ти ніколи не слухаєш,\n',
    'оскільки знаєш і так,\n',
    'що я скажу,\n',
]
with open('file.txt', 'w') as file:
    file.writelines(some_text)
with open('file.txt', 'r') as file, open('file_with_upper_case.txt', 'w') as file_with_upper_case:
    some_text_upper = file.read().upper()
    file_with_upper_case.write(some_text_upper)

'''
3. Write a program that will simulate user score in a game. 
Create a list with 5 player's names. After that simulate 100 games for each player. 
As a result of the game create a list with player's name and his score (0-1000 range). And save it to a CSV file. 
'''
players = ['Josh', 'Luke', 'Kate', 'Mark', 'Mary']
with open('scores.csv', mode='w') as file:
    writer = csv.writer(file)
    writer.writerow(['Player name', 'Score'])
    for _ in range(100):  # 100 games simulation for each player
        for player in players:
            score = random.randint(0, 1000)
            writer.writerow([player, score])

'''
4. Write a script that reads the data from previous CSV file and creates a new file called high_scores.csv where \
each row contains the player name and their highest score. Final score should sorted by descending of highest score
'''
high_scores = {}
with open('scores.csv', mode='r') as file:  # reads the data from previous CSV file
    reader = csv.DictReader(file)
    for row in reader:
        player = row['Player name']
        score = int(row['Score'])
        if player in high_scores:  # upgrades the highest score for player in high_scores dictionary
            high_scores[player] = max(high_scores[player], score)
        else:
            high_scores[player] = score
sorted_scores = sorted(high_scores.items(), key=lambda x: x[1], reverse=True)  # sort high scores by descending order
with open('high_scores.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Player name', 'Highest score'])
    for player, score in sorted_scores:
        writer.writerow([player, score])
