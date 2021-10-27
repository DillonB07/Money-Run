import datetime
import os
import time
from utils import clear, write
from data import *


class Game:
    """
    Game holds all the logic for the game.
    """

    def __init__(self):
        """
        Reset variables and map.
        """
        self.NORTH_ANSWERS = ['north', 'up', 'n', 'u']
        self.EAST_ANSWERS = ['east', 'right', 'e', 'r']
        self.SOUTH_ANSWERS = ['south', 'down', 's', 'd']
        self.WEST_ANSWERS = ['west', 'left', 'w', 'l']
        self.INVENTORY_MESSAGES = ['inventory', 'pockets', 'i', 'p']
        self.CLEAR_MESSAGES = ['clear', 'c']

        self.keys_collected = 0
        self.cue_collected = False
        self.knife_collected = False
        self.candlestick_collected = False

        self.previous_room = {}
        self.current_room = rooms[master_bedroom]

        self.inventory = []

        self.exiting = False

        try:
            self.name = os.environ['REPL_OWNER']
        except:
            write('What is your name?')
            self.name = input()

        self.menu()

    def menu(self):
        """
        Selection menu
        """
        clear()
        write(f'-----MONEY RUN-----\n\nWelcome to Money Run.\nWhat would you like to do?\n\n1. Get started\n2. View controls\n3. Extra info\n|\nV')
        try:
            choice = int(input())
            if choice == 1:
                self.intro()
            elif choice == 2:
                self.controls()
            elif choice == 3:
                self.info()
            else:
                write(
                    'Sorry, that is not a valid option.\nPlease press enter to continue.')
                input()
                self.menu()
        except Exception as e:
            # with open('debug.txt', 'a') as d:
            # d.write(f'Error: {e} at {datetime.datetime.now()}\n')

            write('Sorry, that is not a valid option.\nPress enter to continue.')
            input()
            self.menu()

    def controls(self):
        """
        Writes all of the games controls
        """
        clear()
        write(
            '-----CONTROLS-----\n\nMovement:\n\nTo move around, you can use any of these phrases:\nNorth: {NORTH_ANSWERS}\nEast: {EAST_ANSWERS}\nSouth: {SOUTH_ANSWERS}\nWest: {WEST_ANSWERS}\n\nInventory:\nTo view the items that you\'ve picked up, you can use one of these phrases: {INVENTORY_MESSAGES}.\n\nYou can also clear the screen with one of these: {CLEAR_MESSAGES}.\n\n\n')
        time.sleep(1)
        write('Press enter to continue')
        input()
        self.menu()

    def info(self):
        """
        Writes the contents of README.md
        """
        clear()
        write('This may look a little strange in the console. Open README.md for a better view')
        with open('README.md', 'r') as r:
            write(r.read())
        time.sleep(1)
        write('Press enter to continue')
        input()
        self.menu()

    def intro(self):
        """
        Start the game
        """
        clear()
        write(f'Welcome to Money Run!\n\nPress enter to start!')
        input()
        clear()
        write(f'You wake up and find yourself inside a mysterious mansion after being unconscious for a few hours.')
        time.sleep(2)
        write(f'You notice a note on the floor, so you pick it up and start to read...')
        time.sleep(1)
        write(f'"Welcome {self.name} to our mansion!\nHere, your goal is to get out of the house and into the garden. There are many ways to get there, so have fun!\nOh also, there\'s a prize if you manage to escape\n\nYour mysterious benefactors"\n\n\n\n')

        self.game()

    def game(self):
        """
        Main game code
        """
        start_time = time.time()
        while not self.current_room['won']:
            # If the current room is locked and you have less keys collected than you need to enter tell the user that and then go to the previous room
            if self.current_room['locked'] > self.keys_collected:
                write(
                    f'You need more keys before you can go to the {self.current_room["name"]}')
                self.current_room = self.previous_room
            else:
                write(f'You are now in the {self.current_room["name"]}')
                if self.current_room['monster']:
                    if self.current_room['monster'] == shark:
                        write('There is a shark in the pool!')
                        if self.knife_collected:
                            self.current_room['monster'] = None
                            write(
                                'You use your knife and manage to fend off the shark!')
                        else:
                            write(
                                f'You get scared by the shark and head back to the {self.previous_room["name"]}')
                            self.current_room = self.previous_room

                    elif self.current_room['monster'] == alien:
                        write('There is an alien on the bed!')
                        if self.cue_collected:
                            self.current_room['monster'] = None
                            write(
                                'You whack the alien on the head with your cue and manage to knock it out!')
                        else:
                            write(
                                f'You get scared from the alien and head back to the {self.previous_room["name"]}')
                            self.current_room = self.previous_room

                    elif self.current_room['monster'] == bowling_balls:
                        write(
                            'The bowling balls have come to life and are attacking you! ')
                        if self.knife_collected:
                            self.current_room['monster'] = None
                            write('You slice up the bowling balls and get to live!')
                        else:
                            write(
                                f'You get frightened by the bowling balls and head back to the {self.previous_room["name"]}')
                            self.current_room = self.previous_room

                    elif self.current_room['monster'] == cue_maniac:
                        write(
                            'An angry guest is destroying the walls with a snooker cue!')
                        if self.candlestick_collected:
                            self.current_room['monster'] = None
                            write(
                                'You burn the guest with your candlestick and stay alive.')
                        else:
                            write(
                                f'The guest wards you off and you escape to the {self.previous_room["name"]}')

                    else:
                        write('Sorry, something weird seems to have happened')
                        exit()

                if self.current_room['key']:
                    self.keys_collected += 1
                    self.inventory.append('Key')
                    self.current_room['key'] = False
                    write(
                        f'You\'ve found a key! You now have {self.keys_collected} keys.')

                if self.current_room['weapon']:
                    self.inventory.append(self.current_room['weapon']['name'])
                    write(
                        f'You\'ve collected a {self.current_room["weapon"]["name"]}')
                    if self.current_room['weapon'] == cue:
                        self.cue_collected = True
                    elif self.current_room['weapon'] == knife:
                        self.knife_collected = True
                    elif self.current_room['weapon'] == candlestick:
                        self.candlestick_collected = True
                    else:
                        write('Sorry, something weird seems to have happened')
                        exit()

                self.previous_room = self.current_room

                self.exiting = True

            while self.exiting:
                write('Exits:\n')
                if self.current_room['north'] != None:
                    north = self.current_room['north']
                    name = rooms[north]['name']
                    write(f'North - {name}')
                if self.current_room['east'] != None:
                    east = self.current_room['east']
                    name = rooms[east]['name']
                    write(f'East - {name}')
                if self.current_room['south'] != None:
                    south = self.current_room['south']
                    name = rooms[south]['name']
                    write(f'South - {name}')
                if self.current_room['west'] != None:
                    west = self.current_room['west']
                    name = rooms[west]['name']
                    write(f'West - {name}')

                try:
                    write('Which direction would you like to go in?')
                    direction = input().lower()
                    if direction in self.NORTH_ANSWERS:
                        self.current_room = rooms[self.current_room['north']]
                        self.exiting = False
                    elif direction in self.EAST_ANSWERS:
                        self.current_room = rooms[self.current_room['east']]
                        self.exiting = False
                    elif direction in self.SOUTH_ANSWERS:
                        self.current_room = rooms[self.current_room['south']]
                        self.exiting = False
                    elif direction in self.WEST_ANSWERS:
                        self.current_room = rooms[self.current_room['west']]
                        self.exiting = False
                    elif direction in self.INVENTORY_MESSAGES:
                        msg = f'You have: {self.inventory}'
                        write(msg)
                    elif direction in self.CLEAR_MESSAGES:
                        clear()
                    else:
                        write('That is not a valid direction. Try again.')
                except KeyError:
                    write('Sorry, you can\'t go through walls!')

        end_time = time.time()
        self.end(start_time, end_time)

    def end(self, start_time, end_time):
        """
        End of the game code!
        """
        write(
            'Congratulations {self.name}! You\'ve managed to get to the garden and have won £10,000,000! Have fun spending it.')

        total_time = round(end_time - start_time)
        write(f'You took {total_time} seconds to complete the game!')

        time.sleep(1)

        write(
            f'\nThank you for playing {self.name}!\nI hope that you enjoyed the game that I made for Replit\'s 2021 KAJAM competition.\n\nPress enter to continue.')
        input()
        self.menu()
