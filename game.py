"""
This is a script is made to remove the boredom from the life of mine and for all beginners to know how to use classes and definitions.
This script is made in india at Hyderabad, Telangana.
This script has the most nominal and commonly used libraries by the beginner's to make the stuff alot easy.

"""
import sys
from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint 
from pyfiglet import figlet_format
import random
from textwrap import dedent
from sys import exit
import time



def the_font(z = ' '): # this function  is for  the animation 
		text = z
		from PIL import Image, ImageDraw, ImageFont
		import numpy as np
		myfont = ImageFont.truetype("verdanab.ttf", 12)
		size = myfont.getsize(text)
		img = Image.new("1",size,"black")	
		draw = ImageDraw.Draw(img)
		draw.text((0, 0), text, "white", font=myfont)
		pixels = np.array(img, dtype=np.uint8)
		chars = np.array([' ','#'], dtype="U1")[pixels]
		strings = chars.view('U' + str(chars.shape[1])).flatten()
		print( "\n".join(strings))

def letter_range(start, stop="{", step=1):# this def is for  the animation
    """Yield a range of lowercase letters.""" 
    for ord_ in range(ord(start.lower()), ord(stop.lower()), step):
        yield chr(ord_)

def time_convert(sec): # this function converts the time to the real world and makes it understandable
  mins = sec // 60
  sec = sec % 60
  hours = mins // 60
  mins = mins % 60
  print("the round is been completed in  = {0}hrs:{1}mins:{2}sec".format(int(hours),int(mins),sec))


def start():# this function start's the thing
	the_font("Welcome to the")
	the_font("tic tac toe")

	pk_pwn()



def the_rpsn_brd(): # this function is the representative board for the player to understand the variable on the board
	print("this is the representation of the position to the board")

	print(dedent(f"""
		
	                    |       |       
	                a   |   b   |   c   
	              ______|_______|_________
	                    |       |       
	                d   |   e   |   f   
	              ______|_______|_________
	                    |       |       
	                g   |   h   |   i   
	                    |       |       """))

	

def brd():# this  is the function which assigns the symbol on the board
	global a
	global b
	global c
	global d
	global e
	global f
	global g
	global h
	global i





	print(f"""
			\t\t        |       |
			\t\t        |       |
			\t\t    {a}   |   {z}   |   {c}   
			\t\t________|_______|________
			\t\t        |       |       
			\t\t    {d}   |   {e}   |   {f}   
			\t\t________|_______|________
			\t\t        |       |       
			\t\t    {g}   |   {h}   |   {i}   
			\t\t        |       |
			\t\t        |       |        """)

a = " "
z = " "
c = " "
d = " "
e = " "
f = " "
g = " "
h = " "
i = " "

def pk_pwn(): # this function ask's the player which symbol they wanna use
	global ply_pwn

	global sys_pwn

	global start_time
	print("What would you like to use 'X' or 'O'")
	ply_pwn = input(">")
	start_time = time.time()

	if ply_pwn == "O" or ply_pwn == "o":
		sys_pwn = "X"
		ply_pwn = "O"

	elif ply_pwn == "X" or ply_pwn == "x":
		sys_pwn = "O"
		ply_pwn = "X"

	else:
		print(f"{ply_pwn} is an unidentified input")
		pk_pwn()

	the_rpsn_brd()
	lvl()
	placing_ply()



def placing_ply(): # This function places the player's pawn or symbol on the board

	global a
	global z
	global c
	global d
	global e
	global f
	global g
	global h
	global i

	global ply_pwn

	global sys_pwn

	


	print(f"where would you like to place the {ply_pwn}")

	pos = input('>')

	if pos == "a" and a !=sys_pwn and a != ply_pwn:
		a = ply_pwn
		brd()

	elif pos == "b" and z !=sys_pwn and z != ply_pwn:
		z = ply_pwn
		brd()

	elif pos ==  "c" and c!=sys_pwn and c != ply_pwn:
		c = ply_pwn
		brd()

	elif pos == "d" and d!=sys_pwn and d != ply_pwn:
		d = ply_pwn
		brd()

	elif pos == "e" and e!=sys_pwn and e != ply_pwn:
		e = ply_pwn
		brd()

	elif pos == "f" and f!=sys_pwn and f!= ply_pwn:
		f = ply_pwn
		brd()

	elif pos == "g" and g!=sys_pwn and g != ply_pwn:
		g = ply_pwn
		brd()

	elif pos == "h" and h!=sys_pwn and h!= ply_pwn:
		h =ply_pwn
		brd()

	elif pos == "i" and i!=sys_pwn and i!= ply_pwn:
		i = ply_pwn
		brd()

	else:
		print("The place is been occupied or the input is unidentified")
		placing_ply()

	Evaluation.win_sit()
	Evaluation.lose_sit()
	draw_sit.r1()
	placing_sys()


def placing_sys(): # this function places the system's pawn that is symbol on the board

	global a
	global z
	global c
	global d
	global e
	global f
	global g
	global h
	global i

	global ply_pwn

	global sys_pwn
	

	place = ["a" ,"b" ,"c" ,"d" ,"e" ,"f" ,"g" ,"h" ,"i"]

	b = random.randint(0,8)

	pos = place[b]

	print(f"system placing {sys_pwn}........")

	

	if pos == "a" and a != sys_pwn and a != ply_pwn:
		a = sys_pwn
		brd()
		print("marked at 'a")

	elif pos == "b" and z != sys_pwn and z != ply_pwn:
		z = sys_pwn
		brd()
		print("marked at 'b")

	elif pos ==  "c" and c != sys_pwn and c != ply_pwn:
		c = sys_pwn
		brd()
		print("marked at 'c")

	elif pos == "d" and d != sys_pwn and d != ply_pwn:
		d = sys_pwn
		brd()
		print("marked at 'd")

	elif pos == "e" and e != sys_pwn and e != ply_pwn:
		e = sys_pwn
		brd()
		print("marked at 'e")

	elif pos == "f" and f != sys_pwn and f != ply_pwn:
		f = sys_pwn
		brd()
		print("marked at 'f")

	elif pos == "g" and g != sys_pwn and g != ply_pwn:
		g = sys_pwn
		brd()
		print("marked at 'g")

	elif pos == "h" and h != sys_pwn and h != ply_pwn:
		h =sys_pwn
		brd()
		print("marked at 'h")

	elif pos == "i" and i!= sys_pwn and i != ply_pwn:
		i = sys_pwn
		brd()
		print("marked at 'i")

	else:
		placing_sys()

	Evaluation.win_sit()
	Evaluation.lose_sit()
	draw_sit.r1()
	placing_ply()


class Evaluation(): # it has different evaluations like win and lose

	def win_sit():# this function see's that the player has won or not

		global a
		global z
		global c
		global d
		global e
		global f
		global g
		global h
		global i

		global ply_pwn


		if a == z == c == ply_pwn:
			win()

		elif d == e == f == ply_pwn:
			win()

		elif g == h == i == ply_pwn:
			win()

		elif a == d == g == ply_pwn:
			win()

		elif z == e == h == ply_pwn:
			win()

		elif c == f == i == ply_pwn:
			win()

		elif a == e == i == ply_pwn:
			win()

		elif h == e == c == ply_pwn:
			win()

		else:
			pass





	def lose_sit():# this function see's that the player has lost or not


		global a
		global z
		global c
		global d
		global e
		global f
		global g
		global h
		global i

		global sys_pwn

		if a == z == c == sys_pwn:
			loss()

		elif d == e == f == sys_pwn:
			loss()

		elif g == h == i == sys_pwn:
			loss()

		elif a == d == g == sys_pwn:
			loss()

		elif z == e == h == sys_pwn:
			loss()

		elif c == f == i == sys_pwn:
			loss()

		elif a == e == i == sys_pwn:
			loss()

		elif h == e == c == sys_pwn:
			loss()

		else:
			pass


class draw_sit(): # this function see's that the game is draw or not
	def r1():
		if (a== sys_pwn or a == ply_pwn ) and (z == sys_pwn or z == ply_pwn) and (c == sys_pwn or c == ply_pwn):

			draw_sit.r2()
		else:
			pass

	def r2():
		if (c== sys_pwn or c == ply_pwn ) and (d == sys_pwn or d == ply_pwn) and (e == sys_pwn or e == ply_pwn):

			draw_sit.r3()

		else:
			pass

	def r3():
		if (g== sys_pwn or g == ply_pwn ) and (h == sys_pwn or h == ply_pwn) and (i == sys_pwn or i == ply_pwn):

			draw()

		else:
			pass



def lvl(): # this function takes the level in which the playere want to play

	global range

	print("Enter the level in which you want to play ( easy, medium and hard)")
	lvl = input('>')

	if lvl == "easy":

		range = [0,0]

	elif lvl == "medium":

		range = [0,1]

	elif lvl == "hard":

		range = [1,1]

	else:
		print("since the given input is not recognized you are been set to easy as default")
		range = [0,0]

def lvl_stng(): # this function sets the level of the gameplay

	global range 

	b= random.randint(0,1)

	lvl = range[b]

	if lvl == 0:
		placing_sys()

	else:

		player.r1()

class player():

	def r1():# this funtion decides that the player is winning on the rows to make the things easy i categorized them into r1, r2, and r3

		global a
		global z
		global c
		global d
		global e
		global f
		global g
		global h
		global i

		if a == z == ply_pwn:

			c = sys_pwn

			brd()

		elif d == e == ply_pwn:
			f = sys_pwn
			brd()

		elif g == h == ply_pwn:

			i = sys_pwn
			brd()

		else:
			player.r2()

	def r2():

		global a
		global z
		global c
		global d
		global e
		global f
		global g
		global h
		global i

		if  z == c == ply_pwn:
			a = sys_pwn
			brd()

		elif e == f == ply_pwn:
			d = sys_pwn
			brd()

		elif h == i == ply_pwn:
			g = sys_pwn
			brd()

		else:
			player.r3()


	def r3():

		global a
		global z
		global c
		global d
		global e
		global f
		global g
		global h
		global i

		if a == c == ply_pwn:
			z = ply_pwn
			brd()

		elif d == f == ply_pwn:
			e = ply_pwn
			brd()

		elif g == i == ply_pwn:
			h = ply_pwn
			brd()

		else:
			player.c1()

	def c1():# this function decides that the player is winning on the columns to make the thing easy I categorized them as c1, c2, c3

		global a
		global z
		global c
		global d
		global e
		global f
		global g
		global h
		global i

		if a == d ==ply_pwn:
			g = ply_pwn
			brd()

		elif z == e == ply_pwn:
			h = ply_pwn
			brd()

		elif c == f == ply_pwn:
			i = ply_pwn
			brd()

		else:
			player.c2()

	def c2():

		global a
		global z
		global c
		global d
		global e
		global f
		global g
		global h
		global i

		if g == d == ply_pwn:
			a = sys_pwn
			brd()

		elif h == e == ply_pwn:
			z = sys_pwn
			brd()

		elif f == i == ply_pwn:
			c = sys_pwn
			brd()

		else:
			player.c3()

	def c3():

		global a
		global z
		global c
		global d
		global e
		global f
		global g
		global h
		global i

		if a == g == ply_pwn:
			d = sys_pwn
			brd()

		elif z == h == ply_pwn:
			e = sys_pwn
			brd()

		elif c == i ==ply_pwn:
			f = sys_pwn
			brd()

		else:
			player.d1()

	def d1(): # this def decides that if the player is winning on the diagonal the cross line

		global a
		global z
		global c
		global d
		global e
		global f
		global g
		global h
		global i

		if a == e == ply_pwn:
			i = sys_pwn
			brd()

		elif i == e == ply_pwn:
			a = sys_pwn
			brd()

		elif g == e == ply_pwn:
			c = sys_pwn
			brd()

		elif e == c == ply_pwn:
			g = sys_pwn
			brd()

		else:
			placing_sys()


def loss():# this the function that is what will happen if you lose
	global end_time
	global time_lapsed
	
	the_font("sorry you lost :(")
	end_time = time.time()
	time_lapsed = end_time - start_time
	time_convert(time_lapsed)
	exit(1)

def win():# this is function that will decide what will happen if the player wins
	global end_time
	global time_lapsed

	the_font("You Won!")
	end_time = time.time()
	time_lapsed = end_time - start_time
	time_convert(time_lapsed)
	exit(1)

def draw():#this is the function for the draw animation 

	global end_time
	global time_lapsed

	the_font("Draw!")
	end_time = time.time()
	time_lapsed = end_time - start_time
	time_convert(time_lapsed)
	exit(1)

start()#the game starts here
