'''
Question:
Define a class which has at least two methods:

getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

Hints:
Use init method to construct some parameters
'''
class Exercise5(object):
    def getString(self):
        self.worlds=input('input some world: ')
    def printString(self):
        print('print the worlds',self.worlds.upper())
e=Exercise5()
e.getString()
e.printString()

