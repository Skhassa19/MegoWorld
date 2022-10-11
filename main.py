play_again = 'yes'
while play_again == 'yes':

    def tutorial():
        print('Ok since you are freezing to death I\'ll make this quick')
        print('You fell asleep at home and I kidnapped you and brought you to my world Mego')
        print('Before you ask why, it\'s because I was bored and I have all powerful magical powers')
        print('Now I am not merciless so if you ever need any help just type help')
        userVoice = input('Here try it, type help')
        if userVoice == 'help':
            print(helpMe())
            print('See that nice little menu, yeah that\'s me!\nI\'ll be your tour guide of Mego while your here')
    def helpMe():
        print('Looks like you need some help!')
        userVoice = input('What do you need?\n'
                          'Somethings you can ask me include:\nWhat are my options? (options)\n'
                          'What do letters do and how many have I collected already?(letters)\n'
                          'What commands are available to me?(commands)\n'
                          'Summon inventory(inventory)')
        if userVoice == 'options':
            print(Options)
        if userVoice == 'letters':
            print("Yeah, I may have kidnapped you, but I did leave you an escape route!\n"
                  "You have to collect all the letters of my name to escape my world!\n"
                  "It\'s kind of like rumplestilskin, except I don\'t want your first born I always thought that was weird\n"
                  "I am more than happy just to settle for you being my captive! Letters collected =", Letters)
        if userVoice == 'commands':
            print('Somethings you can do include stat command and help command!\nJust type help or stat!')
        if userVoice =='inventory':
            Inventory = ['Magic Statue?', 'Cellphone', 999]
            print(Inventory)
    def stats(stat):
        health = 100*stat
        agility = 20*stat
        speed = 20*stat
        attack = 20*stat
        print('Your current Overall health is:', health)
        print('Your current Overall agility is:', agility)
        print('Your current Overall speed is:', speed)
        print('Your current Overall attack is:', attack)

    def fightSequence(currentState, states, specialstats, monsterName):
        Sequencestart = 'YES'
        while Sequencestart == 'YES':
            health = 100 * currentState
            enemyhealth = 100 * states
            playerDamage = 0
            buff = 1
            while enemyhealth > 0:
                options = ['attack', 'dodge', 'rest', 'run away']
                agility = 20 * currentState
                speed = 20 * currentState
                attack = 20 * currentState * buff
                enemyagility = 20 * specialstats
                enemyspeed = 20 * specialstats
                enemyattack = 20 * states
                print('You have started a battle with,', monsterName)
                print('Your current Overall health is:', health)
                print('Your current Overall agility is:', agility)
                print('Your current Overall speed is:', speed)
                print('Your current Overall attack is:', attack)
                print(options)
                userVoice = input('What would you like to do?')
                damage = 0
                if userVoice == 'attack':
                    if attack >= enemyattack:
                        print('You exchange blows!\nYour attack stat is higher you win the exchange!')
                        damage = 20 * buff
                    if attack < enemyattack:
                        print('You exchange blows!\nYour attack stat is lower you lose the exchange!')
                        playerDamage = 30
                if userVoice == 'dodge':
                    if agility > enemyagility:
                        print('You try to dodge! It\'s succesful!')
                        print('Your successful dodge grants you a slight attack buff! ')
                        buff = 2
                    if agility <= enemyagility:
                        print('You try to dodge! It\'s unsuccesful!')
                        playerDamage = 30
                if userVoice == 'rest':
                    if enemyhealth*2 > health:
                        print('You have rested and recovered some health succesfully!')
                        currentState = 1
                        playerDamage= -10
                    if enemyhealth*2 <= health:
                        print('You cannot rest at this time you must fight! It is almost over!')
                if userVoice == 'run away':
                    if speed > enemyspeed:
                        print('You have succesfully ran away!')
                        print('You exit the fight feeling dispirted, but suddenly a burst of energy runs through you')
                        print('You faint from the sudden onslaught of energy!')
                        break
                    if speed < enemyspeed:
                        print('You can\'t run from this enemy they are too quick!')
                if health <= 10:
                    print('You have taken too much damage! You are feeling light headed')
                    print('You have Fainted!')
                    break
                newPlayerHealth = health - playerDamage
                health = newPlayerHealth
                currentHealth = enemyhealth - damage
                enemyhealth = currentHealth
                print(monsterName, '\'s health is:', enemyhealth)
            if enemyhealth > health*6:
                break
            else:
                print('You have triumphed against', monsterName, '!')
                break

    def special_selection_event():
        print('You passed the test!')
        stock = {"Letter": 1000}
        quantity = 1
        print(stock)
        print('You may only buy one item!')
        item = input("which item do you want?")
        cost = int(input('How much does it cost?'))
        money = Inventory[0]
        how_many = float(input('How much of the item do you want?'))
        if cost in stock.values():
            if how_many > quantity:
                print('Sorry we don\'t have enough of that item')
            if money < (cost * how_many):
                print('You don\'t have enough cash!')
            elif money >= cost and (how_many <= quantity):
                money = money - (cost * how_many)
                print('You now have', money, "dollars left")
                print('Reciept:', item, 'bought \nmost expensive item bought:', item)
                print('Cheapest item bought:', item)
                stock.pop(item)
                print('Remaining items:', stock)

    def inventory():
        Inventory = ['Magic Statue?', 'Cellphone', 999]

    counter = []
    currentState = 1
    print("Good Morning!")
    print('user:........')
    print("WELCOME TO THE AMAZING WORLD OF MEGO!")
    print('user:........')
    print("You are currently in a dark, cold, forest freezing to death!")
    print('user:........')
    print("Hello?")
    print('user:........')
    print("Wow you seem awfully calm about this?\nLike you do know that you are dying right?")
    print('user:........')
    print('SPEAK!!!!! WHAT THE HECK MAN')
    print('oh, wait my bad I forgot to enable it')
    userVoice = input('Ok try it now, try saying hello!')
    if userVoice == ('hello' or "Hello"):
        print('Wow hi! so that\'s how you sound huh?\nDarn should have picked up one that sounds a little less weird'
            '\nLive and Learn I guess')
        userName = input('Now I\'m sorry what was your name again?')
        print("Nice to meet you", userName)
        userVoice = input('I guess you must be wondering what the heck your doing here?')
        Options = {'a': 'Insult the kidnapper', 'b': 'Ask for more help from the kidnapper',
                   'c': 'run away as far and as fast as you can'}
        Letters = []
        if userVoice == 'yes':
            print(tutorial())
        if userVoice == 'no':
            print('Wow you are cold-blooded!')
            userVoice = input('Are you sure you don\'t wanna know\nit\'s kind of like a game tutorial so I would kind of reccomend it')
            if userVoice == ('yes' or 'ok'):
                print(tutorial())
            elif userVoice == 'no':
                print('You should really learn to accept random acts of kindess you won\'t find much of it here but whatever\n'
                      'Good luck I guess...')
    print(Options)
    userVoice = input('Now what do you want to do next')
    if userVoice in Options.keys():
        counter.append(1)
        print('Menu Message: Health is critically low', userName, 'is wounded!')
        print(stats(0.5))
        print('You are quite the rude one you know!\nI offered you my help and yet you insult me?')
        print("How dare you")
        print('I have already given you more than most people in this world can dream of!')
        print('But if you want to test your limits so early on so be it\n'
              'I just gave you a small critical injury')
        print('This is but a small punishment, I\'ll give you one more piece of advice before I leave you alone\n'
              'in Mego no injury is permanent...\n'
              'with enough rest you can heal from pretty much anything')
        userVoice = input('Here go ahead try it, just say rest')
        if userVoice == 'rest':
            print('You have healed after a period of brief rest!')
            print(stats(1))
    while len(Letters) < 4:
        print('The weirdo who kidnapped you is gone\n you are now stuck in a forest in the dark\n the weather is freezing')
        print('If you dont act soon things might not look too good')
        print(stats(.95))
        Options = ['Go north', 'Go South', 'Wait', 'Go West']
        print(Options)
        userVoice = input('What would you like to do now?')
        if userVoice in Options[0]:
            counter.append(1)
            print('You head north\n in the distance you see a very large tree')
            print('The tree is so large that it takes up almost the entire skyline')
            print('If you wanna see anything past the tree you are gonna have to climb it...')
            Options = ['Climb to the top of the tree', 'Climb halfway up the tree', 'Walk up to the base of the tree']
            print(Options)
            userVoice = input('What would you like to do?')
            if userVoice in (Options[1] or Options[2]):
                counter.append(1)
                print('You hear a screeching sound overhead!')
                print('Huge gusts of wind billow around and all of a sudden you are snatched right up!')
                print('You look up to see what has you gripped tightly in it\'s talons\n'
                      'to your shock it\'s actually a giant bird!')
                print('The bird carries you to it\'s nest where a dozen of it\'s giant babies look very hungry')
                print('It looks like the only way out of this is to fight!')
                print(fightSequence(.95, 1, 3, 'GigaBird'))
                print('For you victory you have been awarded a letter!')
                Letters.append('D')
                continue
            if userVoice in Options[0]:
                counter.append(1)
                print('You climb to the top of the tree and see a giant sleeping bird\n'
                      'it\'s yellow beak glistening with the color red')
                print( 'You begin to sneak up on the bird ever so quietly\n as you get closer the smell of rotting meat permeates\n'
                    'your nostrils and when you look closer you can see a dozen baby birds sleeping in the larger birds bosom')
                print('CRACK! Oh no! While getting a good look at the murderous birds you awaken the mama bird!')
                print('It looks like the only way out of this is to fight!')
                print('It\'s a good thing your feeling swole from climbing this huge tree')
                print(fightSequence(1.1, 1, 1, 'GigaBird'))
                print('For you victory you have been awarded a letter!')
                Letters.append('D')
                continue
        if userVoice in Options[1]:
            counter.append(1)
            print('You head south\n while heading south you come across an uncrossable mountain range')
            print('There seems to be only one way through\n it looks like an abandoned mine shaft...')
            print('You enter the mineshaft and after a couple of steps the path forks\nyou must choose a path')
            Options = ['Left', 'Right']
            print(Options)
            userVoice = input()
            if userVoice in Options[0]:
                counter.append(1)
                print('You have chosen to go left, the further you step down the path the hotter and drier the air becomes')
                print('You finally arrive in the center of the mountain it is a huge cavern with a large mass of gemstones in the corner')
                print('The gemstones look valuable so you approach them')
                print('As you get closer you hair is suddenly flung back by the hot wind')
                print('The pile of Gemstones is actually a rock golem!')
                print('It grabs your leg and crushes it!')
                print('With no way to run things look to be shaping up for another fight!')
                fightSequence(.65, 1.5, .5, 'GEMini')
                print('For your victory you have been awarded a letter!')
                Letters.append("M")
                continue
            if userVoice in Options[1]:
                counter.append(1)
                print('You decide to go right...')
                print('The path gets darker and damper')
                print('The path gets so dark that you cannot even see in front of you\nyou trip and fall down a pit')
                print('In the pit it is pitch black and theres is water dripping down on your head')
                print('It smells really bad')
                print('Suddenly a huge mass swipes across your face')
                print('An ear splitting screech pierces the darkness')
                print('It sounds like a battle cry!')
                fightSequence(.98, 1, 3, 'PitPatThePitBat')
                print('Since you annihilated PitPat you have been awarded a Letter! ')
                Letters.append('M')
                continue
        if userVoice in Options[2]:
            counter.append(1)
            print('You decide to wait and formulate a plan of action')
            print(stats(.9))
            print('You are losing vitality pretty quickly you must choose a path soon!')
            reset = input('Will you chose an earlier path?')
            if reset == 'yes':
                print('You go into a brief period of rest')
                continue
            if reset == 'no':
                counter.append(1)
                print(stats(.8))
                print('While you are freezing slowly to death an animal approaches from the darkness')
                print('It looks like a scavenger...\nthe stench of you slowly dying must have brought it here')
                print('The scavenger nips at your toes it looks like you might need to fight it off!')
                fightSequence(.8, .5, .5, 'Lone Scavenger')
                print('You have defeated the Lone Scavenger you don it\'s fur as a cloak!')
                stats(1.2)
                print('Options = [Choose an earlier path, Try to find a clearing, Climb a tree ')
                userVoice = input('What would you like to do?')
                print('Just as you are about to embark low growls echo from the trees around you')
                print('From the trees a Pack of Scavengers emerge')
                print('They are avenging their fallen comrade')
                fightSequence(1.2, 1, 2, 'Scavenger Pack')
                print('You have defeated the Scavenger Pack!')
                print('You have been awarded a letter!')
                Letters.append('O')
                continue
        if userVoice in Options[3]:
            counter.append(1)
            print('You decide to head West!')
            print('As you continue to walk West you stumble out of the forest into the bright warm sunshine')
            print('Further ahead is something that looks like a town')
            print('You walk into town and directly to the left of the town square is a weird looking shop')
            print('As if compelled you walk into the shop')
            print('When you walk in the shop is empty except for a single counter with a shopkeeper behind it')
            print('You walk up to the shopkeeper and he begins his introduction...')
            print('NOTICE: YOU ARE NOW STUCK IN A TIMELOOP!')
            Timeloop = 'yes'
            while Timeloop == 'yes':
                counter.append(1)
                print('         Welcome to MEGALOMANIA!')
                print('The store that makes sure you don\'t SPACE out :)')
                Inventory = ['Magic Statue?', 'Cellphone', 999]
                print('Your Inventory:', Inventory)
                Inventory = {999: 'Dollars'}
                selling = input("Unfortunately, I have just opened shop\n"
                                "and sadly I have no items to sell yet!\n"
                                "would you be willing to sell me some of yours?\n"
                                "Just a couple of items from your inventory would be more than sufficient!")
                if selling == 'no':
                    print('Well then what are you still doing here if you\'re not gonna help me?\nGET OUTTA HERE!')
                    Timeloop = 'yes'
                elif selling == 'yes' or ('ok'):
                    max_length = 2
                    stock = {}
                    quantities = {}
                    while len(stock) < max_length:
                        item = input('What item will you like to sell to me today?')
                        amount = float(input("How many are you selling?"))
                        price = float(input('How much are you hoping to get for it?'))
                        if item not in stock:
                            stock[item] = price
                        if amount not in quantities:
                            quantities[item] = amount
                        if len(stock) == max_length:
                            customer = input('Ok I may have lied a bit by saying I have no items,\n'
                                             'but I wasn\'t sure if I could trust you...\n'
                                             'However, now that you have unloaded your wares\n'
                                             'would you like to shop my special selection?')
                            if customer == 'yes':
                                print("The store owner cackles....")
                                print(
                                    'IF YOU PART WITH YOUR WARES SO EASILY \nYour not good enough to shop the special selection!')
                                print('You must buy your own wares back to prove you are not fickle!')
                                print('NOTICE: You have reached a checkpoint!')
                                print('Your Inventory:', Inventory)
                                while (len(quantities) and len(stock)) > 0:
                                    print("The items you sold to me and their prices, Item:Price", stock)
                                    print('The items you sold to me and their quantities, Item:Quantity', quantities)
                                    item = input("which item do you want?")
                                    cost = float(input('How much does it cost?'))
                                    how_many = float(input('How much of the item do you want?'))
                                    money = float(input("How much money do you have?"))
                                    if cost in stock.values():
                                        if how_many > quantities[item]:
                                            print('Sorry we don\'t have enough of that item')
                                            Timeloop = 'yes'
                                        if money < (cost * how_many):
                                            print('You don\'t have enough money')
                                        elif money >= cost and (how_many == quantities[item]):
                                            money = money - (cost * how_many)
                                            print('You now have', money, "dollars left")
                                            if how_many < quantities[item]:
                                                print('YOU HAVE TO BUY EVERYTHING BACK!')
                                                Timeloop = 'yes'
                                            if how_many == quantities[item]:
                                                stock.pop(item)
                                                quantities.pop(item)
                                        print('Remaining items:', stock)
                                        if len(quantities) == 0:
                                            print('Reciept:', money,
                                                  'dollars remaining.\nMost expensive item: who cares you had to buy all of them back anyway.'
                                                  '\nCheapest item: again you had to buy it this time! why do you care? and finally you bought'
                                                  '\nEVERYTHING!')
                                    if (len(quantities) and len(stock)) == 0:
                                        print('HAHAHAHAHAHA, I can\'t believe you actually bought your own items back\nyou sucker')
                                        print('If only everyone were as dumb as you')
                                        print('But alas I am a man of my word, here take a gander at our special selection')
                                        Inventory = [money]
                                        special_selection_event()
                                        print('You have failed and start to feel woozy...')

                            elif customer == 'no':
                                print(stock)
                                answer = input('Well then after looking through these items I\'m prepared to offer....'
                                               '\nehhhh I think 5 dollars is more than fair')
                                if answer == 'no':
                                    print('If you don\'t like the offer then SCRAM!')
                                    Timeloop = 'yes'
                                elif answer == 'yes' or 'ok':
                                    Inventory = [1004]
                                    special_selection_event()
                                    Timeloop = 'Escaped'
            print('You have gotten a Letter')
            Letters.append('O')
            continue
        if userVoice == 'help':
            print(helpMe())
        else:
            print(helpMe())
    name = 'False'
    while name == 'False':
        counter.append(1)
        print('Suddenly the world swirls around you...')
        print('An annoying voice that you definitely recognize springs into your ears')
        print('Hahahaha you did it you collected all the letters to my name!')
        print(Letters)
        realName = 'OMOD'
        userVoice = input('NOW WHAT IS MY NAME!')
        if userVoice == realName:
            print('YES YES! That\'s right!')
            print('This will make your fight out of here so much easier!')
            fightSequence(3, 2, 2, realName)
            name = 'True'
        if userVoice not in realName:
            print('NOPE!')
            print('This is really going to suck for you!')
            fightSequence(1, 6, 6, userVoice)
            name = "False"
    print('You suddenly wake up in your bed in a cold sweat\n'
          'Was it all a dream?')
    print('Your forearm is burning...')
    print('You look down and see some words\n'
          'number of turns taken to escape:', sum(counter))
    play_again = input('Do you wanna try to get a better score?')
    if play_again != 'yes':
        print('Well I guess Mego will miss you my weird friend-')





