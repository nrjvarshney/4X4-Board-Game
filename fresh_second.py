# neeraj varshney 2014A7PS0103P
import turtle
import time
from turtle import *
import sys

class Tree(object):
    def __init__(self):
        self.min= None# 1 is min node else 2
        self.child = []
        self.utility = None
        self.child_no=None

def init():
	global grid,init_root,first_empty_row,count
	global screen
	global my_turtle,erasable_turtle,game_over_turtle	
	global window_width,window_height
	global canvas
	global final_col
	global no_of_nodes_generated
	global no_of_nodes_generated_pruning
	
	global memory_1_node
	global siz_of_stack
	global init_time,fine_time

	no_of_nodes_generated=0
	no_of_nodes_generated_pruning=0

	final_col=0
	canvas = turtle.getcanvas()

	screen = turtle.Screen()
	window_width=screen.window_width()
	window_height=screen.window_height()
	turtle.setup(1.0, 1.0, startx=window_width/2, starty=window_height/2)
	window_width=screen.window_width()
	window_height=screen.window_height()
	my_turtle = turtle.Turtle()
	erasable_turtle=turtle.Turtle()
	erasable_turtle.shape("turtle")
	erasable_turtle.speed(0)
	game_over_turtle=turtle.Turtle()
	game_over_turtle.shape("turtle")
	game_over_turtle.speed(0)
	
	
	my_turtle.shape("turtle")
	my_turtle.speed(0)
	grid = [[0 for i in range(4)] for j in range(4)]
	init_root=Tree()
	first_empty_row=[0,0,0,0]
	count=0

def draw_partition_from_origin():
	my_turtle.penup()
	my_turtle.backward(window_width/6)
	
	my_turtle.right(90)
	my_turtle.forward(window_height/2)
	my_turtle.pendown()
	my_turtle.backward(window_height)
	my_turtle.penup()
	my_turtle.forward(window_height/2)
	my_turtle.left(90)
	my_turtle.forward(window_width/6)
	my_turtle.pendown()

def write_status_minimax(no_of_nodes_generated,memory_1_node,siz_of_stack,time_diff,timer,R6,R7,R8,R9,R10,R11,R12):
	my_turtle.penup()
	my_turtle.backward(window_width/2-50)
	my_turtle.left(90)
	my_turtle.forward(window_height/2-50)
	my_turtle.pendown()
	my_turtle.write("ANALYSIS MODULE", move=False, align="left", font=("Arial", 10, "normal"))
	my_turtle.penup()
	my_turtle.backward(50)
	my_turtle.pendown()
	my_turtle.write("R1 "+str(no_of_nodes_generated)+" nodes", move=False, align="left", font=("Arial", 10, "normal"))
	my_turtle.penup()
	my_turtle.backward(50)
	my_turtle.pendown()
	my_turtle.write("R2 "+str(memory_1_node)+" bytes", move=False, align="left", font=("Arial", 10, "normal"))
	my_turtle.penup()
	my_turtle.backward(50)
	my_turtle.pendown()
	my_turtle.write("R3 "+str(siz_of_stack)+" bytes", move=False, align="left", font=("Arial", 10, "normal"))
	my_turtle.penup()
	my_turtle.backward(50)
	my_turtle.pendown()
	if(time_diff=="Not computed yet"):
		my_turtle.write("R4 "+str(time_diff), move=False, align="left", font=("Arial", 10, "normal"))	
	else:
		my_turtle.write("R4 "+str(time_diff)+" seconds", move=False, align="left", font=("Arial", 10, "normal"))
	my_turtle.penup()
	my_turtle.backward(50)
	my_turtle.pendown()
	my_turtle.write("R5 "+str(timer)+" nodes", move=False, align="left", font=("Arial", 10, "normal"))
	my_turtle.penup()
	my_turtle.backward(50)
	my_turtle.pendown()
	if(R6=="Not computed yet"):
		my_turtle.write("R6 "+str(R6), move=False, align="left", font=("Arial", 10, "normal"))
	else:
		my_turtle.write("R6 "+str(R6)+" nodes", move=False, align="left", font=("Arial", 10, "normal"))
	my_turtle.penup()
	my_turtle.backward(50)
	my_turtle.pendown()
	my_turtle.write("R7 "+str(R7), move=False, align="left", font=("Arial", 10, "normal"))
	my_turtle.penup()
	my_turtle.backward(50)
	my_turtle.pendown()
	if(R8=="Not computed yet"):
		my_turtle.write("R8 "+str(R8), move=False, align="left", font=("Arial", 10, "normal"))
	else:
		my_turtle.write("R8 "+str(R8)+" seconds", move=False, align="left", font=("Arial", 10, "normal"))
	my_turtle.penup()
	my_turtle.backward(50)
	my_turtle.pendown()
	if(R9=="Not computed yet"):
		my_turtle.write("R9 "+str(R9), move=False, align="left", font=("Arial", 10, "normal"))	
	else:
		my_turtle.write("R9 minimax uses "+str(R9)+" bytes more memory", move=False, align="left", font=("Arial", 10, "normal"))
	my_turtle.penup()
	my_turtle.backward(50)
	my_turtle.pendown()
	if(R9=="Not computed yet"):
		my_turtle.write("R10 "+str(R10), move=False, align="left", font=("Arial", 10, "normal"))
	else:
		my_turtle.write("R10 "+str(R10)+" seconds", move=False, align="left", font=("Arial", 10, "normal"))
	my_turtle.penup()
	my_turtle.backward(50)
	my_turtle.pendown()
	my_turtle.write("R11 "+str(R11), move=False, align="left", font=("Arial", 10, "normal"))
	my_turtle.penup()
	my_turtle.backward(50)
	my_turtle.pendown()
	my_turtle.write("R12 "+str(R12), move=False, align="left", font=("Arial", 10, "normal"))
	my_turtle.penup()
	my_turtle.forward(12*50)
	my_turtle.backward(window_height/2-50)
	my_turtle.right(90)
	my_turtle.forward(window_width/2-50)
	my_turtle.pendown()

def write_winner(winner):
	game_over_turtle.penup()
	game_over_turtle.left(90)
	game_over_turtle.forward(window_height/2-100)
	if(winner==1):
		game_over_turtle.write("GAME OVER YOU LOST !!!", move=False, align="left", font=("Arial", 10, "normal"))
	else:
		game_over_turtle.write("CONGRATULATIONS YOU WON !!!", move=False, align="left", font=("Arial", 10, "normal"))
	game_over_turtle.backward(window_height/2-100)
	game_over_turtle.right(90)
	game_over_turtle.hideturtle()
def write_selected_cell(column):
	global first_empty_row_game,final_col
	erasable_turtle.penup()
	erasable_turtle.left(90)
	erasable_turtle.forward(window_height/2-250)
	erasable_turtle.write("You selected row "+ str(first_empty_row_game[column]+1)+" and col "+str(column+1)+"\nIf sure Press Enter in terminal else select the cell again", move=False, align="left", font=("Arial", 10, "normal"))
	
	erasable_turtle.backward(window_height/2-250)
	erasable_turtle.right(90)
	erasable_turtle.hideturtle()

def write_try_again():
	erasable_turtle.clear()
	
	global first_empty_row_game,final_col
	erasable_turtle.penup()
	erasable_turtle.left(90)
	erasable_turtle.forward(window_height/2-250)
	erasable_turtle.write("To play the game again Enter \"y\" in the terminal \nTo exit enter \"n\"", move=False, align="left", font=("Arial", 10, "normal"))
	
	erasable_turtle.backward(window_height/2-250)
	erasable_turtle.right(90)
	erasable_turtle.hideturtle()

def modifyglobalvariables(rawx,rawy):
	global xclick,yclick
	global first_empty_row_game,final_col
	global grid
	erasable_turtle.clear()
	xclick = int(rawx//1)
	yclick = int(rawy//1)
	x_change=xclick-old_x
	y_change=yclick-old_y
	col=0
	if(x_change<=50):
		col=0
	elif(x_change<=100):
		col=1
	elif(x_change<=150):
		col=2
	elif(x_change<=200):
		col=3
	final_col=col
	write_selected_cell(final_col)
	print(x_change,final_col)
	
xclick = 0
yclick = 0

def draw_circle(color):
	my_turtle.color(color)
	my_turtle.pendown()
	my_turtle.begin_fill()
	my_turtle.circle(22)
	my_turtle.end_fill()
	my_turtle.penup()
	
def draw_grid():
	global old_x,old_y

	old_x=my_turtle.position()[0]
	old_y=my_turtle.position()[1]
	
	dot_distance = 50
	width = 4
	height = 4
	for y in range(height):
	    for i in range(width):
	        for i in range(4):
    			
    			my_turtle.forward(dot_distance)
    			my_turtle.right(90)
	        my_turtle.forward(dot_distance)
	    my_turtle.backward(dot_distance * width)
	    my_turtle.right(90)
	    my_turtle.forward(dot_distance)
	    my_turtle.left(90)
	    
	my_turtle.left(90)
	my_turtle.forward(dot_distance*height)
	my_turtle.right(90)
	my_turtle.penup()

def write_indices():
	dot_distance = 50
	
	my_turtle.penup()
	my_turtle.backward(dot_distance/2)
	my_turtle.right(90)
	my_turtle.forward(dot_distance)
	my_turtle.pendown()
	my_turtle.write("1", move=False, align="left", font=("Arial", 20, "normal"))
	my_turtle.penup()
	##
	my_turtle.forward(dot_distance)
	my_turtle.pendown()
	my_turtle.write("2", move=False, align="left", font=("Arial", 20, "normal"))
	my_turtle.penup()
	##
	my_turtle.forward(dot_distance)
	my_turtle.pendown()
	my_turtle.write("3", move=False, align="left", font=("Arial", 20, "normal"))
	my_turtle.penup()
	##
	my_turtle.forward(dot_distance)
	my_turtle.pendown()
	my_turtle.write("4", move=False, align="left", font=("Arial", 20, "normal"))
	my_turtle.penup()
	##
	my_turtle.backward(dot_distance*4)
	my_turtle.left(90)
	
	my_turtle.forward(dot_distance/2)

	##
	my_turtle.left(90)
	my_turtle.forward(dot_distance/4)
	my_turtle.right(90)

	my_turtle.forward(dot_distance/2)
	my_turtle.pendown()
	my_turtle.write("1", move=False, align="left", font=("Arial", 20, "normal"))
	my_turtle.penup()
	##
	my_turtle.forward(dot_distance)
	my_turtle.pendown()
	my_turtle.write("2", move=False, align="left", font=("Arial", 20, "normal"))
	my_turtle.penup()
	##
	my_turtle.forward(dot_distance)
	my_turtle.pendown()
	my_turtle.write("3", move=False, align="left", font=("Arial", 20, "normal"))
	my_turtle.penup()
	##
	my_turtle.forward(dot_distance)
	my_turtle.pendown()
	my_turtle.write("4", move=False, align="left", font=("Arial", 20, "normal"))
	my_turtle.penup()
	##
	my_turtle.backward(dot_distance*(3.5))
	my_turtle.right(90)
	my_turtle.forward(dot_distance/4)
	my_turtle.left(90)

def fill_grid():
	dot_distance = 50
	
	my_turtle.right(90)
	my_turtle.forward(dot_distance)
	my_turtle.left(90)
	my_turtle.forward(dot_distance/2)
	for i in range(4):
		for j in range(4):
			if(grid[i][j]==1):
				draw_circle("green")
			if(grid[i][j]==2):
				draw_circle("blue")
			my_turtle.forward(dot_distance)
		my_turtle.right(90)
		my_turtle.forward(dot_distance)
		my_turtle.right(90)
		my_turtle.forward(dot_distance*4)
		my_turtle.right(90)
		my_turtle.right(90)
		
	my_turtle.left(90)
	my_turtle.forward(dot_distance*5)
	my_turtle.left(90)
	
	my_turtle.forward(dot_distance/2)
	my_turtle.right(90)
	my_turtle.right(90)
def clean_grid():
	dot_distance = 50
	
	my_turtle.right(90)
	my_turtle.forward(dot_distance)
	my_turtle.left(90)
	my_turtle.forward(dot_distance/2)
	for i in range(4):
		for j in range(4):
			if(grid[i][j]==1):
				draw_circle("white")
			if(grid[i][j]==2):
				draw_circle("white")
			my_turtle.forward(dot_distance)
		my_turtle.right(90)
		my_turtle.forward(dot_distance)
		my_turtle.right(90)
		my_turtle.forward(dot_distance*4)
		my_turtle.right(90)
		my_turtle.right(90)
		
	my_turtle.left(90)
	my_turtle.forward(dot_distance*5)
	my_turtle.left(90)
	
	my_turtle.forward(dot_distance/2)
	my_turtle.right(90)
	my_turtle.right(90)
	
def minValue(state):
	mini=sys.maxint
	for i in range(len(state)):
		if(mini>state[i]):
			mini=state[i]
	return mini

def maxValue(state):
	maxi=sys.minint
	for i in range(len(state)):
		if(maxi<state[i]):
			maxi=state[i]
	return maxi
def successor(state,row,col,turn):
	grid[row][col]=turn


def terminalTest(state):
	winner=checkWinningState()
	return winner;

def checkValidity(R,C,checkWith):
	if(R<4 and R>=0 and C<4 and C>=0 and grid[R][C]==checkWith):
		return 1;
	return 0;
def checkWinningState():
	checkWith=2
	for row in range(4):
		for col in range(4):
			if(grid[row][col]==checkWith):
				#down
				if(checkValidity(row+1,col,checkWith)==1 and checkValidity(row+2,col,checkWith)==1):
					return checkWith;

				#right
				if(checkValidity(row,col+1,checkWith)==1 and checkValidity(row,col+2,checkWith)==1):
					return checkWith;
				
				#down left diag
				if(checkValidity(row+1,col-1,checkWith)==1 and checkValidity(row+2,col-2,checkWith)==1):
					return checkWith;
				
				#down right diag
				if(checkValidity(row+1,col+1,checkWith)==1 and checkValidity(row+2,col+2,checkWith)==1):
					return checkWith;
	checkWith=1
	for row in range(4):
		for col in range(4):
			if(grid[row][col]==checkWith):
				#down
				if(checkValidity(row+1,col,checkWith)==1 and checkValidity(row+2,col,checkWith)==1):
					return checkWith;

				#right
				if(checkValidity(row,col+1,checkWith)==1 and checkValidity(row,col+2,checkWith)==1):
					return checkWith;
				
				#down left diag
				if(checkValidity(row+1,col-1,checkWith)==1 and checkValidity(row+2,col-2,checkWith)==1):
					return checkWith;
				
				#down right diag
				if(checkValidity(row+1,col+1,checkWith)==1 and checkValidity(row+2,col+2,checkWith)==1):
					return checkWith;
	
	

	return 0;

def my_func(root,turn,row,col,flag):
	global no_of_nodes_generated,no_of_nodes_generated_pruning
	global siz_of_stack
	siz_of_stack=sys.getsizeof(root)+sys.getsizeof(turn)+sys.getsizeof(row)+sys.getsizeof(col)+sys.getsizeof(flag)

	if(flag==1):
		no_of_nodes_generated+=1
	else:
		no_of_nodes_generated_pruning+=1
	grid[row][col]=turn
	global count
	count+=1
	first_empty_row[col]+=1

	next_turn=1
	if(turn==1):
		next_turn=2
	winner=checkWinningState()
	if(winner==1):
		root.utility=1
		grid[row][col]=0
		first_empty_row[col]-=1
		count-=1
		return;
	if(winner==2):
		root.utility=-1
		grid[row][col]=0
		first_empty_row[col]-=1
		count-=1
		return;
	if(count==16):
		root.utility=0
		grid[row][col]=0
		first_empty_row[col]-=1
		count-=1
		
		return;
	for i in range(4):
		root_child=Tree()
		root.child.append(root_child)	
		if(first_empty_row[i]==4):
			root.child[i].utility=0
	for i in range(4):
		if(first_empty_row[i]==4):
			continue
		my_func(root.child[i],next_turn,first_empty_row[i],i,flag)
		if(flag==0):
			if(root.child[i].utility==1 and turn==2):
				root.utility=1
				root.child_no=i;
				break;
			if(root.child[i].utility==-1 and turn==1):
				root.utility=-1
				root.child_no=i;
				break;
		
	if(root.utility is None):
		min_utility=2
		max_utility=-2
		child_number=0
		for i in range(4):
			if(turn==2):
				#max
				if(max_utility<root.child[i].utility):
					max_utility=root.child[i].utility
					child_number=i
			else:
				#min
				if(min_utility>root.child[i].utility):
					min_utility=root.child[i].utility
					child_number=i
		if(turn==2):
			root.utility=max_utility
			root.child_no=child_number
			# child_number=i
		else:
			root.utility=min_utility
			root.child_no=child_number
			# child_number=i
		
	grid[row][col]=0
	first_empty_row[col]-=1
	count-=1
	# print("assigned to turn" + str(turn)+ " with utility "+str(root.utility)+" count is "+str(count))
def printTree(root):
	print(root.utility)
	for i in range(len(root.child)):
		printTree(root.child[i])
def main(flag):
	init()
	for i in range(4):
		init_child=Tree()
		init_root.child.append(init_child)
		my_func(init_root.child[i],1,first_empty_row[i],i,flag)
		
		if(init_root.child[i].utility==1):
			init_root.utility=1
			init_root.child_no=i
			print("got it for "+str(i))
			break
		# print(len(init_root.child[i]))
	# printTree(init_root)

def play():
	game_over=0
	my_root=init_root
	global first_empty_row_game
	first_empty_row_game=[0,0,0,0]
	while(game_over==0):
		col=my_root.child_no
		my_root=my_root.child[col]
		grid[first_empty_row_game[col]][col]=1
		first_empty_row_game[col]+=1
		
		fill_grid()
		
		winner=checkWinningState()
		if(winner<>0):
			# print(winner)
			write_winner(winner)
			write_try_again()
			return winner

		turtle.onscreenclick(modifyglobalvariables) # Here's the change!
		x = raw_input("Press Enter:")
		colll=final_col
		print(final_col)
		
		grid[first_empty_row_game[colll]][colll]=2
		first_empty_row_game[colll]+=1


		my_root=my_root.child[colll]
		winner=checkWinningState()
		if(winner<>0):
			# print(winner)
			write_winner(winner)
			write_try_again()
			return winner


def final_game(flag):
	global init_time,fine_time
	init_time=time.time()
	main(flag)
	fine_time=time.time()
	
	
	draw_partition_from_origin()
	# write_status(no_of_nodes_generated,sys.getsizeof(Tree))
	draw_grid()
	write_indices()
	winner=play()
	
	playing=1
	while(playing==1):
		x = raw_input("Press y to play again / n to close:")
		if(x=="y" or x=="Y"):
			game_over_turtle.clear()
			erasable_turtle.clear()
			my_turtle.clear()	
			main(flag)
			draw_partition_from_origin()
			# write_status(no_of_nodes_generated,sys.getsizeof(Tree))
			draw_grid()
			write_indices()
			winner=play()
			
		else:
			playing=0
			erasable_turtle.clear()
			my_turtle.clear()	
			game_over_turtle.clear()
	

	return fine_time-init_time;
def give_nodes_pruning():
	return no_of_nodes_generated_pruning;
def give_nodes_minimax():
	return no_of_nodes_generated;


def write_status_from_driver(no_of_nodes_minimax,time_diff,timer,no_of_nodes_generated_pruning,time_2):
	write_status_minimax(no_of_nodes_minimax,sys.getsizeof(Tree),siz_of_stack*no_of_nodes_minimax,time_diff,(no_of_nodes_minimax/timer)*0.000001,no_of_nodes_generated_pruning,(no_of_nodes_minimax-no_of_nodes_generated_pruning)/float(no_of_nodes_minimax) ,time_2,siz_of_stack*(no_of_nodes_minimax-no_of_nodes_generated_pruning),10,10,20)
			
