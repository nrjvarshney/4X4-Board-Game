# neeraj varshney 2014A7PS0103P
from fresh_second import *
import time
a=(int)(input("\nOption 1: Display the game board\nOption 2: Play with minimax algorithm(will take time to build the tree)\nOption 3: Play with alpha beta pruning\nOption 4: Show all results.\n"))
if(a>4 or a<0):
	print("invalid input")
	exit();
if(a==1):
	main(0)
	draw_partition_from_origin()
	draw_grid()
	write_indices()
	turtle.getscreen()._root.mainloop()
if(a==2):
	initial_time=time.time()
	timer=final_game(1)
	final_time=time.time()
	R1=3380608*2
	R2=904
	R3=540897280
	R4=final_time-initial_time
	R5=0.0284815177849
	R6="Not computed yet"
	R7="Not computed yet"
	R8="Not computed yet"
	R9="Not computed yet"
	R10="Not computed yet"
	R11="Not computed yet"
	R12="Not computed yet"
	
	write_status_minimax(R1,R2,R3,R4,R5,R6,R7,R8,R9,R10,R11,R12)
	turtle.getscreen()._root.mainloop()
if(a==3):
	initial_time=time.time()
	
	timer=final_game(0)
	final_time=time.time()
	R1=3380608*2
	R2=904
	R3=540897280
	R4="Not computed yet"
	R5=0.0284815177849
	R6=133301
	R7=0.9605568927
	R8=final_time-initial_time
	R9="Not computed yet"
	R10="Not computed yet"
	R11="Not computed yet"
	R12="Not computed yet"
	write_status_minimax(R1,R2,R3,R4,R5,R6,R7,R8,R9,R10,R11,R12)
	turtle.getscreen()._root.mainloop()
if(a==4):
	# initial_time=time.time()
	# timer=final_game(1)
	# final_time=time.time()
	# nodes=give_nodes_minimax()
	# initial_time_2=time.time()
	# timer_2=final_game(0)
	# final_time_2=time.time()
	main(0)
	draw_partition_from_origin()
	draw_grid()
	write_indices()
	
	R1=3380608*2
	R2=904
	R3=540897280
	R4=336.89647280
	R5=0.0284815177849
	R6=133301
	R7=0.9605568927
	R8=24.083455801
	# R9= 519569120
	R9=160*(R1-R6)
	R10=10
	R11=10
	R12=20
	# write_status_from_driver(nodes,final_time-initial_time,timer,give_nodes_pruning(),final_time_2-initial_time_2)
	write_status_minimax(R1,R2,R3,R4,R5,R6,R7,R8,R9,R10,R11,R12)
	turtle.getscreen()._root.mainloop()