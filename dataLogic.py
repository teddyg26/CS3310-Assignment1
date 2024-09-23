# NOTE
# There is a lot of unused/unpruned code here from the provided template.
# I understand it is "messy", but I'm leaving it for if we revisit
# any of this code for future assignments and implementation. (You never know)

class Node(object):
	data = None
	__prev = None
	next = None
	
# constructor for Node class
	def __init__(self, data, prev, next):
		self.data = data
		self.__prev = prev
		self.next = next

class LinkedList(object):
	head = None
	def __init__(self):
		self.head = None

	# add item x to list at index i
	def add(self, x, i):
		if self.head == None:
			self.head = Node(x, None, None)
			return
		current = self.head
		pointer = 0
		while(current != None and pointer != i):
			pointer += 1
			if current.next == None:
				node = Node(x, current, None)
				current.next = node
				return
			current = current.next			

	# remove item at index i from the list
	# def remove(self, i):
		# code goes here (should return item from list or None if item is not in the list)

class Stack(object):
	top = None
	def __init__(self):
		top = None

    # push item onto stack
	def push(self, x):
		if self.top == None:
			self.top = Node(x, None, None)
		else:
			newTop = Node(x, None, self.top)
			self.top = newTop

    # pops item from top of stack
	def pop(self):
		if self.isEmpty():
			return None
		else:
			popped = self.top
			self.top = self.top.next
			return popped.data

    # returns Boolean of whether stack is currently empty
	def isEmpty(self) -> bool:
		value = True if self.top == None else False
		return value

    # returns Boolean of whether stack is currently full
	# def isFull(self) -> bool:
        # code goes here

    # clears the stack
	def clear(self):
		self.top = None

    # looks at the top item of the stack without removing it
	# To prevent EmptyStackErrors, will return a value of False
	# if stack is empty
	def peek(self):
		if self.isEmpty(): return False
		return self.top.data

# class Queue(object):
# 	__linkedList = 
# 	__front = 
# 	__rear = 

#     # constructor for Queue class
# 	def __init__(self):
# 		# code goes her

#     # adds item to front of queue
# 	def enqueue(self, x):
# 		# code goes here

# 	# removes item from rear of queue
# 	def dequeue(self):
# 		# code goes here (should return item from end of queue
#         # or None if queue is empty)

# 	# returns Boolean of whether queue is currently empty
#     def isEmpty(self):
#         # code goes here

#     # returns Boolean of whether queue is currently full
#     def isFull(self):
#         # code goes here

# 	# clears the queue
#     def clear(self):
#         # code goes here

# 	# looks at the item at the end of the queue without removing it
#     def poll(self):
#         # code goes here

# class StackParenthesesChecker(object):
# 	__stack = 

# 	# constructor for StackParenthesesChecker class
# 	def __init__(self):
# 		# code goes here

# 	# Check if string s has balanced parenthesis
# 	def isBalanced(self, s):
# 		# code goes here

# class QueueParenthesesChecker(object):
# 	__queue1 = …
# 	__queue2 = …

# # constructor for QueueParenthesesChecker class
# 	def __init__(self):
# 		# code goes here

# 	# Check if string s has balanced parenthesis
# 	def isBalanced(self, s):
# 		# code goes here
