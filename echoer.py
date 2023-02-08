

# Imports And Measages:


# this is a echoer
# enter
import sys

def init():
    print("Welcome")
    print("Thanks for select me.")
    print("Please type text for echo.")
    print("type 1 for exit.")
init()


# Entry And Exit



def eae():
    text = input("Text For Echo:")
    if text == "1":
        sys.exit()

    print(text)


# Run


eae()


# Thanks for view.
