# CS3310-Assignment1
Files for assignment 1 of CS 3310 - Data & File Structures. Due 9/20/24

1. Develop a doubly linked list and use it to implement a queue and a stack.

2. Develop a program that when given a string of left and right parentheses determines if the parentheses match.

3. Both the queue and the stack must be used to determine if the parentheses match.

# Problem Specification
Write a program to read random strings from a user, consisting of any number of “(“ and “)” in any combination, and determine whether they contain balanced parentheses until the user wishes to end the program. A string with balanced parentheses is one where each “(“ is paired with a “)”. For instance, the string “()((()()))” has balanced parentheses, but the strings “(“, “)”, “(()”, “))((” and “()(()))()()” do not have balanced parentheses. Given the data structures from the course material, there are two ways you can implement a technique for checking balanced parentheses.

1.	Implement a class that uses a stack to determine if a string has balanced parentheses
2.	Implement a class that uses queues to determine if a string has balanced parentheses (Hint: two queues can be used to simulate a stack’s behavior).

Instead of using arrays for the underlying structures of stacks and queues, use linked list representations that do not use built-in list classes. The program may be implemented either in Python, Java, or C++. The program implemented in either language MUST be well-commented, i.e. use block comments for describing each method in a class and give some lines of comments to explain statements. Programs with very few comments (as in just commenting on one of two methods only) or no comments at all will receive a small penalty. 

If you implement the program in Python, you must write a Class Queue, a Class Stack, a Class Node, a Class LinkedList, and a Class StackParenthesesChecker.
Problem Specification
Write a program to read random strings from a user, consisting of any number of “(“ and “)” in any combination, and determine whether they contain balanced parentheses until the user wishes to end the program. A string with balanced parentheses is one where each “(“ is paired with a “)”. For instance, the string “()((()()))” has balanced parentheses, but the strings “(“, “)”, “(()”, “))((” and “()(()))()()” do not have balanced parentheses. Given the data structures from the course material, there are two ways you can implement a technique for checking balanced parentheses.

1.	Implement a class that uses a stack to determine if a string has balanced parentheses
2.	Implement a class that uses queues to determine if a string has balanced parentheses (Hint: two queues can be used to simulate a stack’s behavior).

Instead of using arrays for the underlying structures of stacks and queues, use linked list representations that do not use built-in list classes. The program may be implemented either in Python, Java, or C++. The program implemented in either language MUST be well-commented, i.e. use block comments for describing each method in a class and give some lines of comments to explain statements. Programs with very few comments (as in just commenting on one of two methods only) or no comments at all will receive a small penalty. 

If you implement the program in Python, you must write a Class Queue, a Class Stack, a Class Node, a Class LinkedList, and a Class StackParenthesesChecker.
