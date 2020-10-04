import time
import random


def waste_time(time, symbol):
    for p in range(time):
        p = symbol
        print_pause(p)


def print_pause(message):
    print(message + "\n")
    time.sleep(2.5)


def valid_input(prompt, option1, option2,):
    bad_input = ["Huh??", "Did you not understand the question?",
                 "This input is the opposite of valid.",
                 "hint: enter '1' or '2'",
                 "I wish you were a better listener."]

    while True:
        response = input(prompt).lower()
        if option1 in response:
            break
        elif option2 in response:
            break
        else:
            print_pause(random.choice(bad_input))
    return response


def game_over():
    print_pause("Unfortunately, Murphy's law got the best of you today.")

    again = valid_input("would you like to try your luck again?\n", "y", "n")

    if "y" in again:
        print_pause("So brave.")
        murphys_law_simulator()

    elif "n" in again:
        print_pause("OK seeya!")
        exit()


def intro():
    print_pause("Murphy's law states:"
                " \"Anything that can go wrong will go wrong.\"")
    print_pause("Can you manage to get through a monday"
                " without anything going horribly awry?")
    waste_time(1, "")


def wake_up(inventory):
    morning_outcomes = ["You wake up in a panic. You are late! \n\n"
                        "You throw some clothes on and rush out the door.",
                        "You picked a bad day to sleep in. "
                        "A meteor crashes into your house.",
                        "CRUD! You've overslept!!"]

    print_pause("You wake up to the sound of your alarm"
                " feeling unrested and slightly hungover.")
    print_pause("\"Why did I booze on a work night?\" you wonder.")
    print_pause("\"Ugh I should get ready for work,"
                " but I could really use a snooze.\"")

    choice = valid_input("Do you (1) hit the snooze button or (2)"
                         " suck it up and get ready for work?\n"
                         "Enter '1' or '2'\n", "1", "2",)

    if "1" in choice:
        outcome = random.choice(morning_outcomes)
        print_pause(outcome)

        if "panic" in outcome:
            go_to_work(inventory)

        elif "CRUD" in outcome:
            print_pause
            print_pause("You look at your phone and"
                        " notice a text from your boss;")
            print_pause("YOU'VE BEEN LATE FOR THE LAST TIME!"
                        " YOU'RE FIRED!!")
            print_pause("It seems a bit unprofessional to get"
                        " fired over text, but alas, you are out of a job.")

        else:
            game_over()

    elif "2" in choice:
        print_pause("You take a shower, scarf down some eggs,"
                    " and remember to grab your ID card "
                    "to get in the building.")
        print_pause("On your way to work you can't help but "
                    "feel like something catastrophic "
                    "is going to happen.")
        print_pause("Eh, it's probably nothing.")
        inventory.append("ID card")
        go_to_work(inventory)


def busy_work():
    choice = valid_input("Should we (1) fill out some TPS reports or "
                         "(2) Type some random numbers into a spreadsheet?\n",
                         "1", "2").lower()

    if "1" in choice:
        print_pause("Four of your bosses have asked for a TPS report today "
                    "so you decide to do that.")

    else:
        print_pause("You realize you don't actually know what a TPS report is"
                    ", so you start typing random numbers into a spreadsheet.")
        print_pause("\"Hmm, I wonder if there is some sort of way "
                    "to automate this task,\" "
                    "you think to yourself... \"Maybe by writing some sort "
                    "of code or function?\"")
        print_pause("\"Nah, it's probably impossible.\"")


def go_to_work(inventory):
    if "ID card" in inventory:
        print_pause("You make it to the office, swipe your ID card, "
                    "and take a seat at your cubicle.")
        print_pause("Time to do office stuff.")
        busy_work()
        waste_time(3, ".")

        if "strudel" in inventory:
            print_pause("You are confronted by an angry looking boss man. "
                        "uh oh")
            print_pause("\"Pack your stuff, you've been late for the "
                        "last time\", he says.")
            print_pause("Ah nuts, you got canned.")
            game_over()

    else:
        print_pause("You make it to the office just in time.")
        print_pause("You arrive at the front desk and reach for your "
                    "ID card but it's not there!")
        print_pause("The office has a very strict no ID no entry policy "
                    "so you rush home to grab it.")
        print_pause("While at the house, you realize you didnt eat "
                    "breakfast.") 
        print_pause("You figure, eh I'm already late and "
                    "throw a strudel in the toaster.")
        inventory.append("ID card")
        inventory.append("strudel")
        go_to_work(inventory)

    go_to_lunch(inventory)


def go_to_lunch(inventory):

    cafeteria_events = ["Bummer, while you were enjoying your fish sticks, "
                        "a meteor vaporizes the cafeteria.",
                        "You order the sushi and head back to work. "
                        "Alas, the sushi had turned! You poop your pants "
                        "and everyone laughs.",
                        "You order the sushi, and head back to your cubicle "
                        "to chow down. "
                        "You notice the odd color of the crab meat "
                        "but decide it's probably fine to eat.",
                        "You slurp down some noodles and wonder why nobody "
                        "ever eats in the "
                        "cafeteria. These noodles aren't half bad!"]

    fast_food_events = ["Oh no! You are abducted by aliens and forced to "
                        "assimilate into the lowest caste of their society "
                        "forever.",
                        "As you enjoy your burger, you think to yourself, "
                        "'What a routine day this has been.'",
                        ]

    print_pause("*grrgh")
    print_pause("\"My tummy is rumbling. I better go get something to eat!\"")
    print_pause("There is a cafeteria in the building. you've heard terrible "
                "things about it so you've never eaten there.")
    print_pause("Down the block there are a few fast food joints you usually "
                "go to.")
    choice = valid_input("Should we go to the cafeteria or get some fast "
                         "food?\n"
                         "Enter '1' for cafeteria or '2' for fast food.\n",
                         "1", "2")

    if "1" in choice:
        print_pause("The cafeteria is pretty secluded.")
        outcome = random.choice(cafeteria_events)
        print_pause(outcome)

        if "cubicle" in outcome:
            print_pause("Let's do more office stuff.")
            inventory.append("sushi")
            waste_time(3, ".")
            go_home(inventory)

        elif "noodles" in outcome:
            print_pause("Okay, let's get back to work.")
            waste_time(3, ".")
            go_home(inventory)

        else:
            game_over()

    elif "2" in choice:
        print_pause("You set off towards the burger queen to get their "
                    "world famous quarter ton triple fat burger.")
        outcome = random.choice(fast_food_events)
        print_pause(outcome)

        if "enjoy" in outcome:
            print_pause("I guess I'll head back to work then.")
            waste_time(3, ".")
            go_home(inventory)

        else:
            game_over()


def go_home(inventory):
    print_pause("Ok, time to call it a day!")
    print_pause("As you head home, you reflect on the day and the weird "
                "premonition you had on the way to work.")
    print_pause("See? It was just another boring monday.")
    print_pause("As soon as you get home you plop down on the couch, "
                "turn on the tube and tune in to your programs.")
    print_pause("You drift away to sleep.")

    if "sushi" in inventory:
        waste_time(3, "*")
        print_pause("Ooof, you wake up feeling nauseous and your "
                    "head is pounding. What the heck?")
        print_pause("You start to regret ordering the sushi.")
        print_pause("Within minutes you collapse onto the floor and "
                    "start convulsing.")
        print_pause("Your vision starts to blur and for some reason "
                    "you start to crave flesh.")
        print_pause("*your vision fades to black")
        waste_time(4, "???")
        print_pause("Your eyes open, but only one thought reverberates "
                    "in your head...")
        print_pause("Braaaaains.")
        game_over()

    else:
        outro()


def outro():
    print_pause("Congratulations. Murphy's plans have been foiled. "
                "You managed to have a regular boring ol' day.")
    choice = valid_input("Would you like to try again? 'yes' or "
                         "'no'\n", "y", "n")

    if "y" in choice:
        print_pause("Good luck!")
        murphys_law_simulator()

    elif "n" in choice:
        print_pause("BYEBYE")
        exit()


def murphys_law_simulator():
    inventory = []
    intro()
    wake_up(inventory)


murphys_law_simulator()
