
from sys import argv
from sys import exit
from random import randint

script, username = argv

# These are the classes for TheDugeon game I am creating.

class Scene(object):
	
	def enter(self):
		exit(1)


class gold_room(Scene): 

	all = 1000000

	def enter(self):
        	print "This room is full of gold. You have won this for all your \ntrouble take as much as you want"

        	next = raw_input("> ")
        	if  "0" in next or "1" in next:
                	how_much = int(next)
        	else:
                	return 'dead'
			
        	if how_much < all:
                	print "Nice, you're not greedy and a true warrior."
                	exit(0)
        	else:
                	return 'dead'
	
class dragon_lair(Scene):

	def enter(self):
        	print "%s, you have entered into the dranon's lair." %(username)
        	print "He is snacking on human remains."
        	print "The scary dragon is in front of another door."
        	print "Could that be the exit?"
        	print "what do you do."
        	print "grab the body, draw sword, or taunt the dragon"
        	dragon_moved = False

        	while True:
                	next = raw_input("> ")

                	if next == "grab body":
                        	return 'dead'
                	elif next == "draw sword" and not dragon_moved:
                        	print "You have cut off the head of the dragon!"
                        	print "A door has been reviled and you may go through."
                        	dragon_moved = True
                	elif next == "taunt the dragon" and dragon_moved:
                        	return 'dead'
                	elif next == "open door" and dragon_moved:
                        	return 'gold_room'
               		else:
                        	return 'dead'

class water_well(Scene):

	def enter(self):
        	print "%s, you are now in a room with the watering well for the dugeon." %(username)
        	print "There seems to be no monsters in this room."
        	print "There is a door to the west and a door to the south."
        	print "Which way will you go."

        	next = raw_input("> ")

        	if next == "west":
                	return 'gold_room'
        	elif next == "south":
                	return 'dragon_lair'
        	else:
                	return 'dead'

class trap_room2(Scene):

	def enter(self):
        	print "%s, you have entered into a trap room." %(username)
        	return 'dead'

class level_2(Scene):

	def enter(self):
        	print "%s, you have walked down a spiral stair case." %(username)
        	print "This has lead you to the lower level of the dugeon."
        	print "As you enter the room you notice two ogres."
        	print "There is one in fornt of each door blocking your passage."
        	print "What do you do?"
        	print "feed them a piece of cake, draw sword, taunt ogre 1, stab ogre 2, taunt ogre 2"
        	ogre1_moved = False
        	ogre2_moved = False

        	while True:
                	next = raw_input("> ")
	
                	if next == "feed them a piece of cake":
                        	return 'dead'
                	elif next == "draw sword" and not ogre1_moved:
                        	print "You have cut off the head of the ogre in front of the west door"
                        	print "But, the ogre in front of the south door dodges the attack."
                        	ogre1_moved = True
                	elif next == "taunt ogre 1" and ogre1_moved:
                        	return 'dead'
                	elif next == "open west door" and ogre1_moved:
                        	return 'water_well'
                	elif next == "stab ogre 2" and not ogre2_moved:
                        	print "You have stabbed the ogre in the heart and he has died."
                        	print "The south door is now open."
                        	ogre2_moved = True
                	elif next == "taunt ogre 2" and ogre2_moved:
                        	return 'dead'
                	elif next == "open south door" and ogre2_moved:
                        	return 'trap_room2'
                	else:
                        	return 'dead'

class torture_chamber(Scene):

	def enter(self):
        	print "%s, it looks as if you have entered into the torture chanmber." %(username)
        	print "As you look around you find a sword and pick it up."
        	print "You also see a door to the south."
        	raw_input("> ")

        	south = level_2()
		return 'level_2'

class prison_cells(Scene):

	def enter(self):
        	print "%s, you have stumbled upon a room in the dugeon that looks to have held prisoners." %(username)
        	print "As you look aroud the room you see a door to the east"
        	raw_input("> ")

        	east = torture_chamber()
		return 'torture_chamber'

class trap_room1(Scene):

	def enter(self):
        	print "%s, you have entered into a trap room." %(username)
        	return "dead"


class dead(Scene):
	
	quips = [
		"You died.  You kinda suck at this.",
		"Your mom would be proud...if she were smarter.",
         	"Such a luser.",
         	"I have a small puppy that's better at this."
	]

	def enter(self):
        	print dead.quips[randint(0, len(self.quips)-1)]
        	exit(1)

	

class the_dungeon_entrance(Scene):
	
	def enter(self):

        	print "Hello %s, you are in a dark room." %(username)
        	print "There is a door to your south and east."
        	print "Which one do you take?"

        	next = raw_input("> ")

        	if next == "south":
                	return 'prison_cells'
        	elif next == "east":
                	return 'tramp_room1'
        	else:
                	return 'dead'

class Map(object):

    scenes = {
        'the_dungeon_entrance' : the_dungeon_entrance(),
        'trap_room1' : trap_room1(),
        'prison_cells' : prison_cells(),
        'torture_chamber' : torture_chamber(),
        'level_2' : level_2(),
        'trap_room2' : trap_room2(),
        'water_well' : water_well(),
        'dragon_lair' : dragon_lair(),
        'gold_room' : gold_room(),
        'dead' : dead()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene
        print "start_scene in __init__", self.start_scene

    def next_scene(self, scene_name):
        print "start_scene in next_scene"
        val = Map.scenes.get(scene_name)
        print "next_scene returns", val
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

class Engine(object):

    def __init__(self, scene_map):
        print "Engine __init__ has scene_map", scene_map
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        print "Play's first scene", current_scene

        while True:
            print "\n--------"
            next_scene_name = current_scene.enter()
            print "next scene", next_scene_name
            current_scene = self.scene_map.next_scene(next_scene_name)
            print "map returns new scene", current_scene

a_map = Map('the_dungeon_entrance')
a_game = Engine(a_map)
a_game.play()

