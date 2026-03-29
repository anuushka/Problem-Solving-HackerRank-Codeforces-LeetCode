'''
str.isalnum()
str.isalpha()
str.isdigit()
str.islower()
str.isupper()

Decoupling:
By putting the lambda inside the list without calling it yet, you've created a "menu" of tests.
The "Menu" (Definition): 
You define a list of functions. At this stage, nothing has been checked yet.
The "Processor" (Execution): 
You loop through that list and apply each function to your data (s).
'''

if __name__ == '__main__':
    s = input()
    menu = [lambda x: x.isalnum(), 
            lambda x: x.isalpha(), 
            lambda x: x.isdigit(), 
            lambda x: x.islower(), 
            lambda x: x.isupper()]
    for processor in menu:
        print(any(processor(ch) for ch in s)) 
