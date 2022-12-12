
#Note that this file only contains a function xyCoordinatesToAddress
#As such, this function should work independent of any caller funmction which calls it
#When using regisetrs, you HAVE to make sure they follow the register usage convention in RISC-V as discussed in lectures.
#Else, your function can potentially fail when used by the autograder and in such a context, you will receive a 0 score for this part

xyCoordinatesToAddress:
	#(x,y) in (a0,a1) arguments
	#a2 argument contains base address
	#returns pixel address in a0
	
	#make sure to return to calling function after putting correct value in a0!
	#Enter code below!DO NOT MODIFY ANYTHING BEFORE THIS COMMENT LINE!
	# Register Usage
	#a0 - orginal x and also final output
	#a1 - orginal y 
	# s2 - new x
	# s3 - new y
	# s4 - copy of  a2
	# s5 - variable used to store contents of a2 and have operation applied to it
	# t1 -  counter for the x and y loops


    addi     s2, a0, 0 # new x
    addi     s3, a1, 0 # new y
    addi     s4, a2, 0 # new base address
    addi     s5, a2, 0 # base addresss to be changed
    
    bne s3, zero, math1 # checks if the point requested is zero if so then it goes to second to check if  x is zero
    
    second: 			# checks if x is 0
        bne s2, zero, math2 # if x is not zero goes to the loop for x
   	mv     a0, s5		# otherwise it will move contents of s5 to a0
    	ret
   
     math1: 			# just sets up counter for the y loop
        li     t1, 0 			# initialize t1 with 0 as counter
        j y_loop			# go to y loop

    y_loop: 			# loop for t that increments by 128px  for every unit that the user wants to move on the y-axis
        addi    s5, s5, 128	# same as base address = base address * 128 = base address * 2^(7)
        addi     t1, t1, 1 	# progress loop forward
        blt     t1, s3, y_loop # if t1 < s3, restart loop
        j second


    math2: 			# just sets up counter and moves to the x loop
        li     t1, 0 			# initialize t1 with 0 as counter
        j x_loop			# go to the x loop

    x_loop:  			# loop for x that increments by 4px  for every unit that the user wants to move on the x-axis
	addi    s5, s5, 4 	# same as base address = base address * 4 = base address * 2^(2)
        addi     t1, t1, 1 	# progress loop forward
        blt     t1, s2, x_loop # if t1 < s2, restart loop

    mv     a0, s5 		# put the contents of s5 in to a0 for the output.


    ret 