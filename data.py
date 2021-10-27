"""
ROOMS
1 - Master Bedroom
2 - Corridor A
3 - Kitchen
4 - Lounge
5 - Master Bathroom
6 - Bowling Alley
7 - Swimming Pool
8 - Corridor B
9 - Games Room
10 - Study
11 - Guest Bedroom A
12 - Guest Bedroom B
13 - Guest Bathroom
14 - Entrance Hall
15 - Garden

MONSTERS
Bowling Balls
Shark
Alien
Cue-wielding maniac

WEAPONS
16 - candlestick
17 - knife
18 - cue
19 - all
"""

master_bedroom = 1
corridor_a = 2
kitchen = 3
lounge = 4
master_bathroom = 5
bowling_alley = 6
swimming_pool = 7
corridor_b = 8
games_room = 9
study = 10
guest_bedroom_a = 11
guest_bedroom_b = 12
guest_bathroom = 13
entrance_hall = 14
garden = 15

candlestick = {
    'name': 'Candlestick'
}
knife = {
    'name': 'Knife'
}
cue = {
    'name': 'Cue'
}
final = 19

bowling_balls = {
    'id': 20,
    'weapon': knife
}
shark = {
    'id': 21,
    'weapon': knife
}
alien = {
    'id': 22,
    'weapon': cue
}
cue_maniac = {
    'id': 23,
    'weapon': candlestick
}

rooms = {
    master_bedroom: {
        'name': 'Master Bedroom',
        'locked': 0,
        'key': False,
        'monster': None,
        'weapon': None,
        'north': corridor_a,
        'east': kitchen,
        'south': lounge,
        'west': master_bathroom,
        'won': False
    },
    corridor_a: {
        'name': 'Corridor (A)',
        'locked': 0,
        'key': False,
        'monster': None,
        'weapon': None,
        'north': bowling_alley,
        'east': swimming_pool,
        'south': master_bedroom,
        'west': corridor_b,
        'won': False
    },
    kitchen: {
        'name': 'Kitchen',
        'locked': 0,
        'key': False,
        'monster': None,
        'weapon': knife,
        'north': None,
        'east': None,
        'south': None,
        'west': master_bedroom,
        'won': False
    },
    lounge: {
        'name': 'Lounge',
        'locked': 0,
        'key': False,
        'monster': None,
        'weapon': None,
        'north': master_bedroom,
        'east': guest_bedroom_b,
        'south': entrance_hall,
        'west': study,
        'won': False
    },
    master_bathroom: {
        'name': 'Master Bathroom',
        'locked': 0,
        'key': True,
        'monster': None,
        'weapon': None,
        'north': None,
        'east': master_bedroom,
        'south': None,
        'west': None,
        'won': False
    },
    bowling_alley: {
        'name': 'Bowling Alley',
        'locked': 0,
        'key': False,
        'monster': bowling_balls,
        'weapon': candlestick,
        'north': None,
        'east': None,
        'south': corridor_a,
        'west': None,
        'won': False
    },
    swimming_pool: {
        'name': 'Swimming Pool',
        'locked': 0,
        'key': False,
        'monster': shark,
        'weapon': None,
        'north': None,
        'east': None,
        'south': guest_bedroom_a,
        'west': corridor_a,
        'won': False
    },
    corridor_b: {
        'name': 'Corridor (B)',
        'locked': 1,
        'key': False,
        'monster': None,
        'weapon': None,
        'north': None,
        'east': corridor_a,
        'south': games_room,
        'west': None,
        'won': False
    },
    games_room: {
        'name': 'Games Room',
        'locked': 0,
        'key': True,
        'monster': cue_maniac,
        'weapon': cue,
        'north': corridor_b,
        'east': study,
        'south': None,
        'west': None,
        'won': False
    },
    study: {
        'name': 'Study',
        'locked': 1,
        'key': False,
        'monster': None,
        'weapon': None,
        'north': None,
        'east': lounge,
        'south': None,
        'west': games_room,
        'won': False
    },
    guest_bedroom_a: {
        'name': 'Guest Bedroom (A)',
        'locked': 0,
        'key': False,
        'monster': None,
        'weapon': None,
        'north': swimming_pool,
        'east': None,
        'south': guest_bedroom_b,
        'west': None,
        'won': False
    },
    guest_bedroom_b: {
        'name': 'Guest Bedroom (B)',
        'locked': 2,
        'key': False,
        'monster': alien,
        'weapon': None,
        'north': guest_bedroom_a,
        'east': guest_bathroom,
        'south': None,
        'west': lounge,
        'won': False
    },
    guest_bathroom: {
        'name': 'Guest Bathroom',
        'locked': 0,
        'key': True,
        'monster': None,
        'weapon': None,
        'north': None,
        'east': None,
        'south': None,
        'west': guest_bedroom_b,
        'won': False
    },
    entrance_hall: {
        'name': 'Entrance Hall',
        'locked': 3,
        'key': False,
        'monster': None,
        'weapon': None,
        'north': lounge,
        'east': None,
        'south': garden,
        'west': None,
        'won': False
    },
    garden: {
        'name': 'Garden',
        'locked': 0,
        'key': False,
        'monster': None,
        'weapon': None,
        'north': None,
        'east': None,
        'south': None,
        'west': None,
        'won': True
    }
}
