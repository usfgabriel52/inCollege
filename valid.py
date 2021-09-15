# Password validation in Python
#this code is for password validation from the requirements presented by the USER

# Function to validate the password
def password_check(passwd):
	
    #declaring the special characters to be used to enter by user 

	SpecialSym =['$', '@', '#', '%']

    #variable used to determine the valid characters within the loop 
	val = True
	
    # beginning of the loop 

    # checks the minimum length validation 
	if len(passwd) < 8:
		print('length should be at least 8')
		val = False
		

     #checks the max length validation    
	if len(passwd) > 12:
		print('length should be not be greater than 12')
		val = False
		


    #checks for 1 digit input 
	if not any(char.isdigit() for char in passwd):
		print('Password should have at least one digit')
		val = False
		
    #checks for Upper case input 
	if not any(char.isupper() for char in passwd):
		print('Password should have at least one uppercase letter')
		val = False
		


    #checks for special synbol inout 
	if not any(char in SpecialSym for char in passwd):
		print('Password should have at least one of the symbols $@#' )
		val = False

    #checks if inputs are valid 
	if val:
		return val

# Main method
def main():

    
    passwd = 'H@1ahshs'

    #passwd = input("Enter password:")
   
    #passwd = word

	
    if (password_check(passwd)):
		print("Password is valid")
    else:
		print("Invalid Password !!")
		
# Driver Code		
if __name__ == '__main__':
	main()

