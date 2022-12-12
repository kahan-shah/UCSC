########################################################################################################################
# 	Created by:Shah, Kahan                   																					      
#			   kavshah			
#			  16 May, 2022
#
#
# 	Assignment: 	Lab 3: Looping in RISC-V Assembly
#			       CSE 12, Computer Systems and Assembly Language
#			       UC Santa Cruz, Spring 2022
#
#
#
#
# 	Description: This program take input from the user and print a pattern of  dollar signs and askerisk in the shape of a right triangle.
#
# 	Notes: This program is intended to be run from the RARS IDE.
########################################################################################################################

# Register Usage
# a0 - zero
# a7 - ecalls
# t0 - user input
# t1 - counter for the row_loop
# t2 - the number that is to be printed at the end of every row
# t3 -  counter for the pattern_loop
# s1 - constant kept at one

#  macros
.macro exit 			#macro to exit program
		li a7, 10
		ecall
		.end_macro	
		
.macro print_str(%string1) #macro to print any string
    li a7,4 
    la a0, %string1
    ecall
    .end_macro
    
.macro print_int (%x)  	#macro to print any integer or register
    li a7, 1
    add a0, zero, %x
    ecall
    .end_macro

.data					# storing messages and strings that will be printed.
dollar: .asciz  "$"
asterisk: .asciz  "*"
intial_prompt: .asciz  "Enter the height of the pattern (must be greater than 0):"
error_message: .asciz  "Invalid Entry!"
newline: .asciz  "\n"  	

.text
restart: # restart from the top if an error is found

main:
print_str(intial_prompt)    # asks the user the number of rows the pattern will have
    li 		a7 5 				#reads the input
    ecall				# ecall to read input

    addi t0, a0, 0		# intializing a0 to t0 
    blez t0, error 		# checking if t0 is less than or equal to zero if so then brances  to the error label 
    li s1, 1				# Intialize s1 to 1
    li t1, 1				# intialize t1 to 1
    li t2 1				# intialize t2 to 1
    bge t0,s1, row1		# if t0 is 1 then goes to label that makes the first row
    exit
 
 error:				#  If the input is equal to or less than 0 the following prints an error message and redirects them to the start.
     print_str(error_message) # print  error message
     print_str(newline)	# print newline for space	
     blez t0, restart		# redirect to the start

 row1: 				# This section prints the first row and then branches to the main loop
     print_str(dollar)		# print the dollar sign
     print_int (s1)		# print s1 which is set to one at this point
     bgt t0,s1,row_loop	# if the inputer t0 is greater than 1 then branches to row loop
     print_str(newline)
     exit				# exit ecall


 row_loop:			# this is the first loop where a new line created every iteration and the first character is added.
         print_str(newline)	# print newline
         print_str(dollar)	# print dollar sign as the first character of every row
         addi t2,t2,2 		#  increase the t2 by 2 for every row.
         li t3, 0			# intialize t3  to be one for the pattern_loop
         
             pattern_loop:	#  this inner loop creates the pattern of dollars and asterisks for every row
                print_str(asterisk) 	# print asterisk
                print_str(dollar)	# print dollar
                addi t3,t3,1
            	blt t3, t1, pattern_loop # if the row length is still not done re-run until the correct row length is achieved
            	
    	print_int(t2)		# print t2
   	addi t1,t1,1		# increase the counter of the outer loop
         bgt t0,t1, row_loop		# check if the number of rows that user wants has been creater if not then branch to start of the loop
         print_str(newline)		# create a newline
         exit				# ecall exit to end program.
