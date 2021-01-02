#define our player variables
#player_name = 'Toto'
#player_attack = 10
#player_heal = 16
#health = 100

#create player list
#player = ['Toto',10,16,100] -> list

from random import randint

game_running = True
game_results = []

print('Welcome to Player vs Monsters Game')

def calculate_monster_attack(attack_min,attack_max):
    return randint(attack_min,attack_max)

def game_ends(winner_name):
    #use f-strings
    print(f'{winner_name} won the game')
    

while game_running == True :
    counter = 0
    new_round = True
    print('-'* 21)
    print('Enter Player Name :')
    player_name = input('Your Name : ')
    monster_name = input('Your Monster Name : ')

    print()
    print('-'* 21)

    #create dictionary
    player = {'name' : player_name, 'attack' : 13, 'heal' : 16, 'health' : 100}
    monster = {'name' : monster_name, 'attack_min' : 10, 'attack_max' :20, 'health' : 100}

    print(player['name'] + ' has ' + str(player['health']) + ' health.')
    print(monster['name'] + ' has ' + str(monster['health']) + ' health.')

    while new_round == True :
        counter = counter + 1
        player_won = False
        monsters_won = False

    #print for action for users
        print(' ')
        print('Please select action')
        print('1) Attack')
        print('2) Heal')
        print('3) Exit Game')
        print('4) Show Results')
        #users can choose options, input only can save strings
        player_choice = input()

        if player_choice == '1':
            #print('You attack the monsters for 10 points!')
            monster['health'] = monster['health'] - player['attack']
            if monster['health'] <= 0:
                player_won = True
            else :
                player['health'] = player['health'] - calculate_monster_attack(monster['attack_min'],monster['attack_max'])
                if player['health'] <= 0:
                    monsters_won = True
        elif player_choice == '2':
            #print('Heal for 16 points!')
            player['health'] = player['health'] + player['heal']
            if player['health'] > 100 :
                player['health'] = 100
            player['health'] = player['health'] - calculate_monster_attack(monster['attack_min'],monster['attack_max'])
            if player['health'] <= 0 :
                monsters_won = True

        elif player_choice == '3':
            print('Thank You')
            new_round = False
            game_running = False
        elif player_choice == '4' :
            for item in game_results:
                print(item)
        else:
            print('Invalid action, try again!')

        if player_won == False and monsters_won == False:
            print(str(monster['name']) + ' health : ' + str(monster['health']))
            print(str(player['name']) + ' health : ' + str(player['health']))
        elif player_won == True :
            game_ends(player['name'])
            round_result = {'name' : player['name'], 'health' : player['health'], 'total rounds': counter}
            game_results.append(round_result)
            new_round = False
        elif monsters_won == True :
            game_ends(monster['name'])
            round_result = {'name' : monster['name'], 'health' : monster['health'],'total rounds': counter}
            game_results.append(round_result)
            new_round = False







