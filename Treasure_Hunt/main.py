import art
import random

print(art.start)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.\n")

guide1 = 0
guide2 = 0
vial_of_poison = 0
gold = 0
circle = 0
no_dice = 0

print(art.tree)
touch = input(
    "You come to a dark forest with trees seemingly rising up to the sky. You reach out to touch the closest tree and it feels hot. \n Do you 'press' the tree or pull your hand 'away'? \n"
)
if touch.lower() == "press":
    guidepoint1 = "The trees suddenly part and a path opens up."
    guide1 += 1
else:
    print(art.snake)
    snake = input("As you pull your hand away, a serpent appears and looks ready to strike.\n Do you 'jump' away or 'grab' the snake?\n ")

    if snake.lower() == "jump":
        print(
            "You jump back but fall into a hidden trap with spikes! You are trapped and bleeding, Game Over."
        )
        print(art.hole)
        quit()
    elif snake.lower() == "grab":
        guidepoint2 = "The snake trembles and asks for mercy, it shows you the way to part the trees and gives you a 'vial of poison'."
        vial_of_poison += 1
        guide2 += 1
    else:
        print("You did something else entirely or check spelling? Game Over!")
        quit()

print(art.forest)
if guide1 > 0:
    print(guidepoint1 + "\n")
if guide2 > 0:
    print(guidepoint2 + "\n")
    # the vial picture is nice, but it distracts from the cabin
    # print(art.venom)

print(
    "You continue along the path!\n After a few minutes of walking, you see a cabin nestled in the trees.\n"
)

knock = input(
    "Do you 'knock' on the door or 'continue' along the path?\n ").lower()

if knock == "knock":
    print(art.man)
    print(
        "You enter the cabin and see a man tossing two dice.\n The rules are simple. You toss the dice and the highest sum wins but you can do it twice if you don't like the first result.\n If you lose... you will find out later what happens, mWahahaha.\n"
    )
    dice = input("Would you like to play he asks? Y or N \n").lower()
    if dice == "y":
        if vial_of_poison == 1:
            print(
                "If you lose, I'll take your 'vial of poison' and if you win, I'll give you gold coins in the amount of the difference in our scores.\n"
            )
        else:  #no poison
            print(
                "If you lose, I'll feed you to my pet and if you win, I'll give you gold coins in the amount of the difference in our scores.\n You suddenly feel uneasy about being fed to a pet so you try to get up and leave but your legs feel heavy, so you will have to stay!\n"
            )
        print(art.dice)
        random_toss = random.randint(1, 6) + random.randint(1, 6)
        print(f"You toss the dice and the result is {random_toss}.")
        toss_again = input(
            "Do you want to 'keep' this result or toss 'again'? \n").lower()
        if toss_again == "keep":
            keeper_toss = random.randint(1, 6) + random.randint(1, 6)
            if random_toss >= keeper_toss:
                print(f"Lucky, I got {keeper_toss}.")
                winnings = random_toss - keeper_toss
                print(
                    f"You receive {winnings} gold and are able to walk away in one piece!\n"
                )
                gold += winnings
                if gold > 0:
                    donation = input(
                        "Would you like to donate some gold? Y or N \n").lower(
                        )
                    if donation == "y":
                        answer = "Keep your money :).\n"
                    else:
                        answer = "Well, I've written too much code already so letting you get away without a donation this time! \n"
            elif vial_of_poison == 1:  #keeper toss better but you have the vial of poison
                print(f"The keeper tosses {keeper_toss}!\n")
                question = input("Do you want to run? Y or N \n").lower()
                if question == "y":
                    vial_lost = "Run or not, you see a huge dire wolf jump in front of you and as much as you want to get away you hand over the 'vial of poison'.\n"
                else:
                    vial_lost = "You see a huge dire wolf jump in front of you and as much as you want to get away you hand over the 'vial of poison'.\n"
                print(art.dog)
                vial_of_poison -= 1
                print(vial_lost)
            else:  #keeper toss better and you die!
                print(
                    f"The keeper tosses {keeper_toss}!\n You desperately try to get away but feel a powerful bite on your neck and pass out. Game Over!\n"
                )
                quit()

        else:  #second toss
            print("You toss the dice again!")
            print(art.dice)

            random_toss2 = random.randint(1, 6) + random.randint(1, 6)
            print(f"This time, your total is {random_toss2}.")
            if random_toss2 < random_toss:
                print(
                    "You idiot, the second toss is even worse, now you are in trouble!\n"
                )

            keeper_toss = random.randint(1, 6) + random.randint(1, 6)
            if random_toss2 >= keeper_toss:
                print(f"Lucky, I got {keeper_toss}.")
                winnings = random_toss2 - keeper_toss
                print(
                    f"You receive {winnings} gold and are able to walk away in one piece!\n"
                )
                gold += winnings
                if gold > 0:
                    donation = input(
                        "Would you like to donate some gold? Y or N \n").lower(
                        )
                    if donation == "y":
                        answer = "Keep your money :).\n"
                    else:
                        answer = "Well, I've written too much code already so letting you get away without a donation this time! \n"
            elif vial_of_poison == 1:  #keeper toss better but you have the vial of poison
                print(f"The keeper tosses {keeper_toss}!\n")
                question = input("Do you want to run? Y or N \n").lower()
                if question == "y":
                    vial_lost = "Run or not, you see a huge dire wolf jump in front of you and as much as you want to get away you hand over the 'vial of poison'.\n"
                else:
                    vial_lost = "You see a huge dire wolf jump in front of you and as much as you want to get away you hand over the 'vial of poison'.\n"
                print(art.dog)
                vial_of_poison -= 1
                print(vial_lost)
            else:  #keeper toss better and you die!
                print(
                    f"The keeper tosses {keeper_toss}!\n You desperately try to get away but feel a powerful bite on your neck and pass out. Game Over!\n"
                )
                quit()

    else:  #no dice
        print("You decide to not play the dice!\n")
        no_dice += 1
        print(
            "Hmm, says the strange old man. Suit yourself.\n You turn around to leave but hear an angry bark.\n"
        )
        run = input("Do you make a 'run' for it or 'walk' out slowly?").lower()
        if run == "run":
            print(art.dog)
            print(
                "You start running but the beast quickly gains on you and mauls you on the ground! Game Over!"
            )
            quit()

        else:  #walk
            print(
                "You walk out slowly and although the angry bark continues no one comes after you.\n Phew, that was a close one!\n"
            )

else:  #continue without knocking
    print(art.knight)

    print(
        "You continue along the path and come to a black knight guarding a fork in the road!\n As you have no gold, the knight won't let you pass.\n"
    )

    come_back = input(
        "Do you want to 'circle' back to the cabin or try to 'sneak' past the guard?\n"
    ).lower()
    if come_back == "circle":
        circle += 1
        print(art.man)
        print(
            "You come back to the cabin and enter the dwelling. An old man is sitting on the floor and tossing two dice.\n The rules are simple. You toss the dice and the highest sum wins but you can do it twice if you don't like the first result.\n If you lose... you will find out later what happens, mWahahaha.\n"
        )
        dice = input("Would you like to play he asks? Y or N \n").lower()
        if dice == "y":
            if vial_of_poison == 1:
                print(
                    "If you lose, I'll take your 'vial of poison' and if you win, I'll give you gold coins in the amount of the difference in our scores.\n"
                )
            else:  #no poison
                print(
                    "If you lose, I'll feed you to my pet and if you win, I'll give you gold coins in the amount of the difference in our scores.\n You suddenly feel uneasy about being fed to a pet so you try to get up and leave but your legs feel heavy, so you will have to stay!\n"
                )
            print(art.man)
            random_toss = random.randint(1, 6) + random.randint(1, 6)
            print(f"You toss the dice and the result is {random_toss}.")

            toss_again = input(
                "Do you want to 'keep' this result or toss 'again'? \n").lower(
                )
            if toss_again == "keep":
                keeper_toss = random.randint(1, 6) + random.randint(1, 6)
                if random_toss >= keeper_toss:
                    print(f"Lucky, I got {keeper_toss}.")
                    winnings = random_toss - keeper_toss
                    print(
                        f"You receive {winnings} gold and are able to walk away in one piece!\n"
                    )
                    gold += winnings
                    if gold > 0:
                        donation = input(
                            "Would you like to donate some gold? Y or N \n"
                        ).lower()
                        if donation == "y":
                            answer = "Keep your money :).\n"
                        else:
                            answer = "Well, I've written too much code already so letting you go without a donation this time! \n"
                elif vial_of_poison == 1:  #keeper toss better but you have the vial of poison
                    print(f"The keeper tosses {keeper_toss}!\n")
                    question = input("Do you want to run? Y or N \n").lower()
                    if question == "y":
                        print(
                            "Run or not, you see a huge dire wolf jump in front of you and as much as you want to get away you hand over the 'vial of poison'.\n"
                        )
                    else:
                        print(
                            "You see a huge dire wolf jump in front of you and as much as you want to get away you hand over the 'vial of poison'.\n"
                        )
                    print(art.dog)
                    vial_of_poison -= 1
                else:  #keeper toss better and you die!
                    print(
                        f"The keeper tosses {keeper_toss}!\n You desperately try to get away but feel a powerful bite on your neck and pass out. Game Over!\n"
                    )
                    quit()

            else:  #second toss
                print("You toss the dice again!")
                print(art.dice)
                random_toss2 = random.randint(1, 6) + random.randint(1, 6)
                print(f"This time, your total is {random_toss2}.")
                if random_toss2 < random_toss:
                    print(
                        "You idiot, the second toss is even worse, now you are in trouble!\n"
                    )
                keeper_toss = random.randint(1, 6) + random.randint(1, 6)
                if random_toss2 >= keeper_toss:
                    print(f"Lucky, I got {keeper_toss}.")
                    winnings = random_toss2 - keeper_toss
                    print(
                        f"You receive {winnings} gold and are able to walk away in one piece!\n"
                    )
                    gold += winnings
                    if gold > 0:
                        donation = input(
                            "Would you like to donate some gold? Y or N \n"
                        ).lower()
                        if donation == "y":
                            answer = "Keep your money :).\n"
                        else:
                            answer = "Well, I've written too much code already so letting you get away without a donation this time! \n"
                elif vial_of_poison == 1:  #keeper toss better but you have the vial of poison
                    print(
                        f"The keeper tosses {keeper_toss}!\n You see a huge dire wolf jump in front of you and as much as you want to get away you hand over the 'vial of poison'.\n"
                    )
                    print(art.dog)
                    vial_of_poison -= 1
                else:  #keeper toss better and you die!
                    print(
                        f"The keeper tosses {keeper_toss}!\n You desperately try to get away but feel a powerful bite on your neck and pass out. Game Over!\n"
                    )
                    quit()

        else:  #no dice
            print(
                "You decide to not play the dice!\n Hmm, says the strange old man. Suit yourself.\n You turn around to leave but hear an angry bark.\n"
            )
            run = input(
                "Do you make a 'run' for it or 'walk' out slowly?").lower()
            if run == "run":
                print(art.dog)
                print(
                    "You start running but the beast quickly gains on you and mauls you on the ground! Game Over!"
                )
                quit()

            else:  #walk
                print(
                    "You walk out slowly and although the angry bark continues no one comes after you.\n Phew, that was a close one!"
                )

    else:  #sneak
        print(art.sword)
        print(
            "You try to sneak around the knight when you think he is not looking but alas, \n the knight was a magical creature and didn't need the eyesight.\n He swings his huge sword and you are gone! Game Over!\n"
        )
        quit()

if circle == 1:
    if gold > 0:
        print(art.knight)
        print(answer)
        print(
            "You continue along the path again and come to a black knight guarding a fork in the road! But this time you have some gold!\n The knight takes 1 gold and you need to decide whether to go left or right."
        )
        gold -= 1
        direction = input("Do you run 'left' or 'right'?\n ").lower()

        if direction == "left" and vial_of_poison == 1:
            print(art.dragon)
            print(
                "You turn left and see a huge dragon guarding a tresure chest!\n"
            )
            poison_toss = input(
                "Do you want to toss your vial of poison at the dragon? Y or N\n"
            ).lower()
            if poison_toss == "y":
                print(
                    "You toss the poison on the dragon and while the dragon spins away and flies off for a bath you grab the chest!\n"
                )
                print(art.treasure)
                print("Congrats you've won the game!")
            else:  #no poison toss
                print(
                    "The dragon stares at you menacingly and unleashes the flames. Game Over!  \n"
                )
                quit()

        elif direction == "left" and gold > 0:
            print(
                "You turn left and see a huge dragon guarding a tresure chest!\n Thankfully you still have some gold left and can toss the coins to distract the dragon.\n"
            )
            poison_toss = input(
                "Do you want to toss your coins behind the dragon? Y or N\n"
            ).lower()
            if poison_toss == "y":
                print(
                    "While the dragon runs after the spinning coins, you grab the chest and sneak away!\n"
                )
                print(art.treasure)
                print("Congrats you've won the game!")
            else:  #no coin toss
                print(
                    "The dragon stares at you menacingly and unleashes the flames. Game Over!  \n"
                )
                quit()

        elif direction == "left":  #but no poison or gold

            print(art.dragon)
            print("You see a huge dragon guarding the chest.\n")
            distract = input(
                "Do you distract the dragon by barking while hiding behind a tree? Y or N? \n"
            ).lower()
            if distract == "y":  #distract
                print(
                    "You bark but the dragon is not fooled! He flies up and unleashes his flames and it's not a pretty sight! Game Over!\n"
                )
                quit()

            else:  #don't distract
                print(
                    "You think drawing the dragon's attenion is a stupid idea and that's true but you wait and wait and have no choice but to turn back.\n You didn't exactly win but at least you returned in one piece!"
                )
                quit()

        else:  #right direction
            print(art.dog)

            print(
                "You turn right and come face to face with a pet of the man in the cabin!\n It's a huge direwolf, so you probably can't esacpe."
            )

            pretend = input(
                "Do you 'crouch' in fetal position and play dead or make a 'run' for it?\n "
            )
            if pretend == "crouch":  #fetal
                print(
                    "The beast sniffs all around you and grabs you by the scruff of your neck.\n He carries you outside the forest and there is no way back, at least not today.\n"
                )
                if gold > 0:
                    print(
                        f"You didn't exactly win but at least you returned in one piece and with {gold} gold!"
                    )
                else:
                    print(
                        "You didn't exactly win but at least you returned in one piece!"
                    )
                quit()
            else:  #run
                print(
                    "You try to run but I said you probably couldn't escape, the beast swipes at your back and gnaws at your neck.\n Game Over!"
                )
                quit()

    else:  #went to the hut but didn't gamble
        # no_gamble = input("I didn't gamble? Is that really me? Y or N \n")
        print(art.knight)
        print(
            "You continue along the path again and see the black knight but still have no gold and the knight won't let you pass.\n But you see a strange light in the distance.\n"
        )
        light = input("Do you want to call to the light? Y or N? \n").lower()
        if light == "y":
            print(art.sword)
            print(
                "You call out to the light, but it zooms to the black knight instead who starts to swing his sword at it and frees up the path.\n"
            )
            direction = input("Do you run 'left' or 'right'?\n ").lower()
            if direction == "left" and vial_of_poison == 1:
                print(art.dragon)
                print(
                    "You turn left and see a huge dragon guarding a tresure chest!\n"
                )
                poison_toss = input(
                    "Do you want to toss your vial of poison at the dragon? Y or N \n"
                ).lower()
                if poison_toss == "y":
                    print(
                        "You toss the poison on the dragon and while the dragon spins away and flies off for a bath you grab the chest!\n"
                    )
                    print(art.treasure)
                    print("Congrats you've won the game!")
                else:  #no poison toss
                    print(
                        "The dragon stares at you menacingly and unleashes the flames. Game Over!  \n"
                    )
                    quit()

            elif direction == "left":  #but no poison or gold
                print(art.dragon)
                print("You see a huge dragon guarding the chest.\n")
                distract = input(
                    "Do you distract the dragon by barking while hiding behind a tree? Y or N? \n"
                ).lower()
                if distract == "y":  #distract
                    print(
                        "You bark but the dragon is not fooled! He flies up and unleashes his flames and it's not a pretty sight! Game Over!\n"
                    )
                    quit()

                else:  #don't distract
                    print(
                        "You think drawing the dragon's attenion is a stupid idea and that's true but you wait and wait and have no choice but to turn back.\n You didn't exactly win but at least you returned in one piece!"
                    )
                    quit()

            else:  #right direction
                print(art.dog)

                print(
                    "You turn right and come face to face with a pet of the man in the cabin!\n It's a huge direwolf, so you probably can't esacpe."
                )
                pretend = input(
                    "Do you 'crouch' in fetal position and play dead or make a 'run' for it? \n"
                )
                if pretend == "crouch":  #fetal
                    print(
                        "The beast sniffs all around you and grabs you by the scruff of your neck.\n He carries you outside the forest and there is no way back, at least not today.\n"
                    )
                    if gold > 0:
                        print(
                            f"You didn't exactly win but at least you returned in one piece and with {gold} gold!"
                        )
                    else:
                        print(
                            "You didn't exactly win but at least you returned in one piece!"
                        )
                    quit()
                else:  #run
                    print(
                        "You try to run but I said you probably couldn't escape, the beast swipes at your back and gnaws at your neck.\n Game Over!"
                    )
                    quit()

        else:  #don't call to the light
            print(
                "You stare at the knight and the light suddenly zooms through you and carries you back outside the forest.\n There doesn't seem to be a way to enter the forest again, at least not today.\n You didn't exactly win but at least you returned in one piece!"
            )
            quit()

else:  #entered the hut on first try
    if gold > 0:
        print(art.knight)
        print(answer)
        print(
            "You exit the cabin and continue along the path. You come to a black knight guarding a fork in the road.\n The knight asks for 1 gold and let's you pass. Now you need to decide whether to go left or right.\n"
        )
        gold -= 1
        direction = input("Do you run 'left' or 'right'?\n ").lower()
        if direction == "left" and vial_of_poison == 1:
            print(art.dragon)
            print(
                "You turn left and see a huge dragon guarding a tresure chest!\n"
            )
            poison_toss = input(
                "Do you want to toss your vial of poison at the dragon? Y or N\n"
            ).lower()
            if poison_toss == "y":
                print(
                    "You toss the poison on the dragon and while the dragon spins away and flies off for a bath you grab the chest!\n"
                )
                print(art.treasure)
                print("Congrats you've won the game!")
            else:  #no poison toss
                print(
                    "The dragon stares at you menacingly and unleashes the flames. Game Over!\n"
                )
                quit()

        elif direction == "left" and gold > 0:
            print(art.dragon)
            print(
                "You turn left and see a huge dragon guarding a tresure chest!\n Thankfully you still have some gold left and can toss the coins to distract the dragon.\n"
            )
            poison_toss = input(
                "Do you want to toss your coins behind the dragon? Y or N\n"
            ).lower()
            if poison_toss == "y":
                print(
                    "While the dragon runs after the spinning coins, you grab the chest and sneak away!\n"
                )
                print(art.treasure)
                print("Congrats you've won the game!")
            else:  #no coin toss
                print(
                    "The dragon stares at you menacingly and unleashes the flames. Game Over!  \n"
                )
                quit()

        elif direction == "left":  #but no poison or gold

            print(art.dragon)
            print("You see a huge dragon guarding the chest.\n")
            distract = input(
                "Do you distract the dragon by barking while hiding behind a tree? Y or N? \n"
            ).lower()
            if distract == "y":  #distract
                print(
                    "You bark but the dragon is not fooled! He flies up and unleashes his flames and it's not a pretty sight! Game Over!\n"
                )
                quit()

            else:  #don't distract
                print(
                    "You think drawing the dragon's attenion is a stupid idea and that's true but you wait and wait and have no choice but to turn back.\n You didn't exactly win but at least you returned in one piece!"
                )
                quit()

        else:  #right direction
            print(art.dog)

            print(
                "You turn right and come face to face with a pet of the man in the cabin!\n It's a huge direwolf, so you probably can't esacpe.\n"
            )
            pretend = input(
                "Do you 'crouch' in a fetal position and play dead or make a 'run' for it? \n"
            )
            if pretend == "crouch":  #fetal
                print(
                    "The beast sniffs all around you and grabs you by the scruff of your neck.\n He carries you outside the forest and there is no way back, at least not today.\n You didn't exactly win but at least you returned in one piece!"
                )
                quit()
            else:  #run
                print(
                    "You try to run but I said you probably couldn't escape, the beast swipes at your back and gnaws at your neck.\n Game Over!"
                )
                quit()

    else:  #went to the hut but didn't get any gold
        if no_dice == 0:
            no_gold = input(
                "Well, I gambled and now have no gold. Do you want to cry? Y or N \n"
            ).lower()
            if no_gold == "y":
                crying = "Crying won't do me much good. I think I see something shiny up ahead.\n"
            else:
                crying = "Right, let's continue walking, I think there is something shiny up ahead.\n"
        else:
            no_gold = input(
                "Well, I didn't even play the dice. Is that really me? Y or N \n"
            ).lower()
            if no_gold == "y":
                crying = "Me or not me, I see 'shiny' up ahead!\n"
            else:
                crying = "Next time, let's gamble all the money! I think there is something shiny up ahead.\n"

        print(art.knight)
        print(crying)
        print(
            "You continue along the path and see a black knight but have no gold and the knight won't let you pass.\n But you see a strange light in the distance.\n"
        )
        light = input("Do you want to call to the light? Y or N? \n").lower()
        if light == "y":
            print(art.sword)

            print(
                "You call out to the light, but it zooms to the black knight instead who starts to swing his sword at it and frees up the path.\n"
            )
            direction = input("Do you run 'left' or 'right'?\n ").lower()
            if direction == "left" and vial_of_poison == 1:
                print(art.dragon)
                print(
                    "You turn left and see a huge dragon guarding a tresure chest!\n"
                )
                poison_toss = input(
                    "Do you want to toss your vial of poison at the dragon? Y or N\n"
                ).lower()
                if poison_toss == "y":
                    print(
                        "You toss the poison on the dragon and while the dragon spins away and flies off for a bath you grab the chest!\n"
                    )
                    print(art.treasure)
                    print("Congrats you've won the game!")
                else:  #no poison toss
                    print(
                        "The dragon stares at you menacingly and unleashes the flames. Game Over!  \n"
                    )
                    quit()

            elif direction == "left":  #but no poison or gold

                print(art.dragon)
                print("You see a huge dragon guarding the chest.\n")
                distract = input(
                    "Do you distract the dragon by barking while hiding behind a tree? Y or N? \n"
                ).lower()
                if distract == "y":  #distract
                    print(
                        "You bark but the dragon is not fooled! He flies up and unleashes his flames and it's not a pretty sight! Game Over!\n"
                    )
                    quit()

                else:  #don't distract
                    print(
                        "You think drawing the dragon's attenion is a stupid idea and that's true but you wait and wait and have no choice but to turn back.\n You didn't exactly win but at least you returned in one piece!"
                    )
                    print("")
                    quit()

            else:  #right direction
                print(art.dog)
                print(
                    "You turn right and come face to face with a pet of the man in the cabin!\n It's a huge direwolf, so you probably can't esacpe.\n"
                )
                pretend = input(
                    "Do you 'crouch' in a fetal position and play dead or make a 'run' for it? \n"
                )
                if pretend == "crouch":  #fetal
                    print(
                        "The beast sniffs all around you and grabs you by the scruff of your neck.\n He carries you outside the forest and there is no way back, at least not today.\n You didn't exactly win but at least you returned in one piece!"
                    )
                    quit()
                else:  #run
                    print(
                        "You try to run but I said you probably couldn't escape, the beast swipes at your back and gnaws at your neck.\n Game Over!"
                    )
                    quit()

        else:  #don't call to the light
            print(
                "You stare at the knight and the light suddenly zooms through you and carries you back outside the forest.\n There doesn't seem to be a way to enter the forest again, at least not today.\n You didn't exactly win but at least you returned in one piece!"
            )
            quit()