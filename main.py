from dataLogic import Stack, LinkedList

def main():
	stack = Stack()
	userString = None

    # Take input, then parse it for validity.
	while True:
		stack.clear()
		errorFlag = False

        # Take an input string of parentheses and parse them into a linked list
		# of nodes that are each one character. After, push open parentheses to
		# a stack, popping them each time a closed parentheses is encountered.
		# If the input is valid, the stack will balance to being empty. Otherwise,
		# it will have leftover data or be called to pop when empty (EmptyStackError).
		

        # Turn user input into linked list of parentheses
		inputList = LinkedList()
		userString = input('Please enter a string of parentheses: ')
		index = 0
		for letter in userString:
			if letter != '(' and letter != ')':
				print("Invalid input. Please enter only parentheses")
				errorFlag = True
				break
			inputList.add(letter, index)
			index += 1
			
        # Iterate through linked list using stack to determine validity of input
		current = inputList.head
		while current != None:
			if current.data == '(':
				stack.push(current)
			elif current.data == ')':
				# Can't peek if the stack is empty. This will trip if input is invalid
				if stack.isEmpty():
					print("Parentheses are not balanced.")
					errorFlag = True
					break
				if stack.peek().data == '(':
					stack.pop()
			current = current.next

		# Output result of parsing
		if not errorFlag:	
			if stack.isEmpty():
				print("Parentheses are balanced.")
			else:
				print("Parentheses are not balanced.")

		# Determine if the user wants to continue
		endFlag = False
		while True:
			continueCheck = input("Continue? (y/n): ")
			if continueCheck.lower() == 'y':
				break
			elif not continueCheck.lower() == 'n':
				print("Invalid input, expected y or n")
			else:
				endFlag = True
				break	
		if endFlag:
			break

if __name__ == '__main__':	
	main()
