teamA_points = 0
teamA_matches = 0
teamB_points = 0
teamB_matches = 0
teamC_points = 0
teamC_matches = 0
teamD_points = 0
teamD_matches = 0
teamE_points = 0
teamE_matches = 0
teamF_points = 0
teamF_matches = 0
teamG_points = 0
teamG_matches = 0
teamH_points = 0
teamH_matches = 0

pre_final_1 = None
pre_final_2 = None
pre_final_3 = None
pre_final_4 = None

final_1 = None
final_2 = None

champion = None

print("="*50)
print("SuperOver Leagues".center(50))
print("="*50)
while True:
    print("\n1. Start League")
    print("2. View Points Table")
    print("3. Exit")

    choice = int(input("Select one from above: "))
    match choice:
        case 1:
            print("League Started Successfully!")
            print("Name of teams are: ")
            print("1. Team A")
            print("2. Team B")
            print("3. Team C")
            print("4. Team D")
            print("5. Team E")
            print("6. Team F")
            print("7. Team G")
            print("8. Team H")
            print("Total Teams: 8\nTotal Matches: 28\nLet's Begin the League!")

            print("-"*25)
            print("Match 1")
            print("Team A vs Team B")
            print("-"*25)
            print("Who won ?")
            print()
            print("1. Team A")
            print("2. Team B")
            print()
            cho1 = int(input("Enter your choice: "))
            
            match cho1:
                case 1:
                    print("Team A won the match !")
                    teamA_points += 2
                    teamA_matches += 1
                    teamB_matches += 1
                    pre_final_1 = 1
                    print("Result Save Successfully")
                case 2:
                    print("Team B won the match !")
                    teamB_points += 2
                    teamB_matches += 1
                    teamA_matches += 1
                    pre_final_1 = 2
                    print("Result Save Successfully")
                case _ :
                    print("Invalid Choice..!")

            print("-"*25)
            print("Match 2")
            print("Team C vs Team D")
            print("-"*25)
            print("Who won ?")
            print()
            print("1. Team C")
            print("2. Team D")
            print()
            cho2 = int(input("Enter your choice: "))
            
            match cho2:
                case 1:
                    print("Team C won the match !")
                    teamC_points += 2
                    teamC_matches += 1
                    teamD_matches += 1
                    pre_final_2 = 3
                    print("Result Save Successfully")
                case 2:
                    print("Team D won the match !")
                    teamD_points += 2
                    teamD_matches += 1
                    teamC_matches += 1
                    pre_final_2 = 4
                    print("Result Save Successfully")
                case _ :
                    print("Invalid Choice..!")
            
            print("-"*25)
            print("Match 3")
            print("Team E vs Team F")
            print("-"*25)
            print("Who won ?")
            print()
            print("1. Team E")
            print("2. Team F")
            print()
            cho3 = int(input("Enter your choice: "))

            match cho3:
                case 1:
                    print("Team E won the match !")
                    teamE_points += 2
                    teamE_matches += 1
                    teamF_matches += 1
                    pre_final_3 = 5
                    print("Result Save Successfully")
                case 2:
                    print("Team F won the match !")
                    teamF_points += 2
                    teamF_matches += 1
                    teamE_matches += 1
                    pre_final_3 = 6
                    print("Result Save Successfully")
                case _:
                    print("Invalid Choice..!")

            print("-"*25)
            print("Match 4")
            print("Team G vs Team H")
            print("-"*25)
            print("Who won ?")
            print()
            print("1. Team G")
            print("2. Team H")
            print()
            cho4 = int(input("Enter your choice: "))

            match cho4:
                case 1:
                    print("Team G won the match !")
                    teamG_points += 2
                    teamG_matches += 1
                    teamH_matches += 1
                    pre_final_4 = 7
                    print("Result Save Successfully")
                case 2:
                    print("Team H won the match !")
                    teamH_points += 2
                    teamH_matches += 1
                    teamG_matches += 1
                    pre_final_4 = 8
                    print("Result Save Successfully")
                case _:
                    print("Invalid Choice..!")
            
            print("="*50)
            print("League Completed!".center(50))
            print("="*50)

            print()
            print("1. Back")
            print("2. View Points table")
            print("3. Continue Upcoming Matches")
            cho = int(input("Enter your choice: "))
            match cho:
                case 1:
                    continue
                case 2:
                    print("="*55)
                    print("Points Table".center(55))
                    print("="*55)
                    print("Team\t \tMatches Played\t \tPoints")
                    print("-"*55)
                    print(f"\nTeam A \t\t\t{teamA_matches}\t \t  {teamA_points}")
                    print(f"\nTeam B \t\t\t{teamB_matches}\t \t  {teamB_points}")
                    print(f"\nTeam C \t\t\t{teamC_matches}\t \t  {teamC_points}")
                    print(f"\nTeam D \t\t\t{teamD_matches}\t \t  {teamD_points}")
                    print(f"\nTeam E \t\t\t{teamE_matches}\t \t  {teamE_points}")
                    print(f"\nTeam F \t\t\t{teamF_matches}\t \t  {teamF_points}")
                    print(f"\nTeam G \t\t\t{teamG_matches}\t \t  {teamG_points}")
                    print(f"\nTeam H \t\t\t{teamH_matches}\t \t  {teamH_points}")
                case 3:
                    team1_name =""
                    team2_name =""
                    match pre_final_1:
                        case 1:
                            team1_name = "Team A"
                        case 2:
                            team1_name = "Team B"
                    match pre_final_2:
                        case 3:
                            team2_name = "Team C"
                        case 4:
                            team2_name = "Team D"
                    print("-"*25)
                    print("Match 1")
                    print(f"{team1_name} vs {team2_name}")
                    print("-"*25)
                    print("Who won ?")
                    print()
                    print(f"1. Team {team1_name}")
                    print(f"2. Team {team2_name}")
                    print()
                    cho1 = int(input("Enter your choice: "))
                    
                    match cho1:
                        case 1:
                            print(f"{team1_name} won the match !")
                            final_1 = pre_final_1
                            match final_1:
                                case 1:
                                    teamA_points += 2                                    
                                    teamA_matches += 1                                    
                                    teamB_matches += 1                                    
                                    
                                case 2:
                                    teamB_points += 2
                                    teamB_matches += 1
                                    teamB_matches += 1
                            print("Result Saved Successfully")
                    
                        case 2:
                            print(f"{team2_name} won the match !")
                            final_1=pre_final_2
                            match final_1:
                                case 1:
                                    teamC_points += 2                                    
                                    teamC_matches += 1                                    
                                    teamD_matches += 1                                    
                                    
                                case 2:
                                    teamD_points += 2
                                    teamD_matches += 1
                                    teamC_matches += 1
                            print("Result Save Successfully")
                        case _ :
                            print("Invalid Choice..!")
                    
                    team3_name =""
                    team4_name =""

                    match pre_final_3:
                        case 5:
                            team3_name = "Team E"
                        case 6:
                            team3_name = "Team F"
                    match pre_final_4:
                        case 7:
                            team4_name = "Team G"
                        case 8:
                            team4_name = "Team H"

                    print("-"*25)
                    print("Match 2")
                    print(f"{team3_name} vs {team4_name}")
                    print("-"*25)
                    print("Who won ?")
                    print()
                    print(f"1. Team {team3_name}")
                    print(f"2. Team {team4_name}")
                    print()
                    cho = int(input("Enter your choice: "))
                    
                    match cho:
                        case 1:
                            print(f"{team3_name} won the match !")
                            final_2 = pre_final_3
                            match final_2:
                                case 1:
                                    teamE_points += 2                                    
                                    teamE_matches += 1                                    
                                    teamF_matches += 1                                    
                                    
                                case 2:
                                    teamF_points += 2
                                    teamF_matches += 1
                                    teamE_matches += 1
                            print("Result Saved Successfully")
                    
                        case 2:
                            print(f"{team4_name} won the match !")
                            final_2=pre_final_4
                            match final_2:
                                case 1:
                                    teamG_points += 2                                    
                                    teamG_matches += 1                                    
                                    teamH_matches += 1                                    
                                    
                                case 2:
                                    teamH_points += 2
                                    teamH_matches += 1
                                    teamG_matches += 1
                            print("Result Save Successfully")

                    print("="*25)
                    print("Semi Finals Completed".center(25))
                    print("="*25)
                    print("1. View Points table")
                    print("2. Continue to Grand Finale")
                    print("3. Exit") 

                    final_choice = int(input("Select any one from above: "))
                    match final_choice:
                        case 1:
                            print("="*55)
                            print("Points Table".center(55))
                            print("="*55)
                            print("Team\t \tMatches Played\t \tPoints")
                            print("-"*55)
                            print(f"\nTeam A \t\t\t{teamA_matches}\t \t  {teamA_points}")
                            print(f"\nTeam B \t\t\t{teamB_matches}\t \t  {teamB_points}")
                            print(f"\nTeam C \t\t\t{teamC_matches}\t \t  {teamC_points}")
                            print(f"\nTeam D \t\t\t{teamD_matches}\t \t  {teamD_points}")
                            print(f"\nTeam E \t\t\t{teamE_matches}\t \t  {teamE_points}")
                            print(f"\nTeam F \t\t\t{teamF_matches}\t \t  {teamF_points}")
                            print(f"\nTeam G \t\t\t{teamG_matches}\t \t  {teamG_points}")
                            print(f"\nTeam H \t\t\t{teamH_matches}\t \t  {teamH_points}")

                            print("1. Continue to Grand Finale")
                            print("2. Exit")
                            next_choice = int(input("Enter any one from above: "))  
                            match next_choice:
                                case 1: 
                                    champion1_name = ""
                                    champion2_name = ""
                                    match final_1:
                                        case 1:
                                            champion1_name ="Team A"
                                        case 2:
                                            champion1_name ="Team B"
                                        case 3:
                                            champion1_name ="Team C"
                                        case 4:
                                            champion1_name ="Team D"
                                    
                                    match final_2:
                                        case 5:
                                            champion2_name ="Team E"
                                        case 6:
                                            champion2_name ="Team F"
                                        case 7:
                                            champion2_name ="Team G"
                                        case 8:
                                            champion2_name ="Team H"
                            
                            print("="*25)
                            print("Grand finale".center(25))
                            print("="*25)
                            print(f"\n{champion1_name} vs {champion2_name}")
                            print("\nWho won ?\n")
                            print(f"1. {champion1_name}")
                            print(f"1. {champion2_name}")
                            g_choice = int(input("Enter winner: "))
                            match g_choice:
                                case 1:
                                    print(f"{champion1_name} won")
                                    champion = final_1
                                case 2:
                                    print(f"{champion2_name} won")
                                    champion = final_2
                            match champion:
                                case 1:
                                    teamA_points += 2
                                    teamA_matches += 1
                                    teamB_matches += 1
                                case 2:
                                    teamB_points += 2
                                    teamB_matches += 1
                                    teamA_matches += 1
                                case 3:
                                    teamC_points += 2
                                    teamC_matches += 1
                                    teamD_matches += 1
                                case 4:
                                    teamD_points += 2
                                    teamD_matches += 1
                                    teamC_matches += 1
                                case 5:
                                    teamE_points += 2
                                    teamE_matches += 1
                                    teamF_matches += 1
                                case 6:
                                    teamF_points += 2
                                    teamF_matches += 1
                                    teamE_matches += 1
                                case 7:
                                    teamG_points += 2
                                    teamG_matches += 1
                                    teamH_matches += 1
                                case 8:
                                    teamH_points += 2
                                    teamH_matches += 1
                                    teamG_matches += 1

                            print("="*25)
                            print("GRAND FINALE COMPLETED".center(25))
                            print("="*25)
                            print("🏆 TOURNAMENT CHAMPION🏆")
                            print("Congratulations...")

                            match champion:
                                case 1:
                                    print("Team A")
                                case 2:
                                    print("Team B")
                                case 3:
                                    print("Team C")
                                case 4:
                                    print("Team D")
                                case 5:
                                    print("Team E")
                                case 6:
                                    print("Team F")
                                case 7:
                                    print("Team G")
                                case 8:
                                    print("Team H")
                        case 2:
                            next_choice = int(input("Enter any one from above: "))  
                            match next_choice:
                                case 1: 
                                    champion1_name = ""
                                    champion2_name = ""
                                    match final_1:
                                        case 1:
                                            champion1_name ="Team A"
                                        case 2:
                                            champion1_name ="Team B"
                                        case 3:
                                            champion1_name ="Team C"
                                        case 4:
                                            champion1_name ="Team D"
                                    
                                    match final_2:
                                        case 5:
                                            champion2_name ="Team E"
                                        case 6:
                                            champion2_name ="Team F"
                                        case 7:
                                            champion2_name ="Team G"
                                        case 8:
                                            champion2_name ="Team H"
                            
                            print("="*25)
                            print("Grand finale".center(25))
                            print("="*25)
                            print(f"\n{champion1_name} vs {champion2_name}")
                            print("\nWho won ?\n")
                            print(f"1. {champion1_name}")
                            print(f"1. {champion2_name}")
                            g_choice = int(input("Enter winner: "))
                            match g_choice:
                                case 1:
                                    print(f"{champion1_name} won")
                                    champion = final_1
                                case 2:
                                    print(f"{champion2_name} won")
                                    champion = final_2
                            match champion:
                                case 1:
                                    teamA_points += 2
                                    teamA_matches += 1
                                    teamB_matches += 1
                                case 2:
                                    teamB_points += 2
                                    teamB_matches += 1
                                    teamA_matches += 1
                                case 3:
                                    teamC_points += 2
                                    teamC_matches += 1
                                    teamD_matches += 1
                                case 4:
                                    teamD_points += 2
                                    teamD_matches += 1
                                    teamC_matches += 1
                                case 5:
                                    teamE_points += 2
                                    teamE_matches += 1
                                    teamF_matches += 1
                                case 6:
                                    teamF_points += 2
                                    teamF_matches += 1
                                    teamE_matches += 1
                                case 7:
                                    teamG_points += 2
                                    teamG_matches += 1
                                    teamH_matches += 1
                                case 8:
                                    teamH_points += 2
                                    teamH_matches += 1
                                    teamG_matches += 1

                            print("="*25)
                            print("GRAND FINALE COMPLETED".center(25))
                            print("="*25)
                            print("🏆 TOURNAMENT CHAMPION🏆")
                            print("Congratulations...")

                            match champion:
                                case 1:
                                    print("Team A")
                                case 2:
                                    print("Team B")
                                case 3:
                                    print("Team C")
                                case 4:
                                    print("Team D")
                                case 5:
                                    print("Team E")
                                case 6:
                                    print("Team F")
                                case 7:
                                    print("Team G")
                                case 8:
                                    print("Team H")
                        case 3:
                            continue
                                
                    
            
        case 2:
            print("="*55)
            print("Points Table".center(55))
            print("="*55)
            print("Team\t \tMatches Played\t \tPoints")
            print("-"*55)
            print(f"\nTeam A \t\t\t{teamA_matches}\t \t  {teamA_points}")
            print(f"\nTeam B \t\t\t{teamB_matches}\t \t  {teamB_points}")
            print(f"\nTeam C \t\t\t{teamC_matches}\t \t  {teamC_points}")
            print(f"\nTeam D \t\t\t{teamD_matches}\t \t  {teamD_points}")
            print(f"\nTeam E \t\t\t{teamE_matches}\t \t  {teamE_points}")
            print(f"\nTeam F \t\t\t{teamF_matches}\t \t  {teamF_points}")
            print(f"\nTeam G \t\t\t{teamG_matches}\t \t  {teamG_points}")
            print(f"\nTeam H \t\t\t{teamH_matches}\t \t  {teamH_points}")
        case 3:
            print("Thank You...\nFor being a part of League Management System.")
            continue
        case _ :
            print("Invalid Choice")