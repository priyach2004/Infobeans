'''
7. A cricket academy wants to analyze player performance. Each player's information is stored as a tuple.

Tuple Format:

(player_id, player_name, runs_scored)

Requirements:

Read N player records from the user and store them as tuples in a list.
Display all player records.
Find and display the player who scored the highest runs.
Find and display the player who scored the lowest runs.
Calculate and display the total runs scored by all players.
Calculate and display the average runs scored.
Display players who scored more than 50 runs.

Test Case:

Input:

Enter number of players: 5

101 Virat 82
102 Rohit 45
103 Gill 120
104 Hardik 38
105 SKY 76

Expected Output:

All Players:
(101, 'Virat', 82)
(102, 'Rohit', 45)
(103, 'Gill', 120)
(104, 'Hardik', 38)
(105, 'SKY', 76)

Highest Scorer:
(103, 'Gill', 120)

Lowest Scorer:
(104, 'Hardik', 38)

Total Runs:
361

Average Runs:
72.2

Players Scoring More Than 50 Runs:
(101, 'Virat', 82)
(103, 'Gill', 120)
(105, 'SKY', 76)

'''

n=int(input("Enter number of players: "))
player=[]
for i in range(n):
	id = int(input("Enter ID of a Player: "))
	name=input("Enter name of a player: ")
	age=int(input("Enter age of a player: "))
	t=(id,name,age)
	player.append(t)
print("All Players: ")
print(*player)
highest=0
lowest=1000000
sum=0
for i in player:
	if i[2]>highest:
		highest=i[2]
	if i[2]<lowest:
		lowest=i[2]
	sum+=i[2]
for i in player:
	if i[2]==highest:
		print("Highest Score: ")
		print(i)
	if i[2]==lowest:
		print("Lowest Score: ")
		print(i)
print("Total Runs: ",sum)
print("Average Run: ",(sum/n))
for i in player:
	if i[2]>=50:
		print(i)