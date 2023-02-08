
Imports And Measages


```python
# this is a echoer
# enter
import sys

def init():
    print("Welcom")
    print("Thanks for select me.")
    print("Please type text for echo.")
    print("type 1 for exit.")
init()
```

    Welcom
    Thanks for select me.
    Please type text for echo.
    type 1 for exit.
    

Entry And Exit


```python
def eae():
    text = input("Text For Echo:")
    if text == "1":
        sys.exit()

    print(text)
```

Run


```python

eae()
```

    Text For Echo:1
    


    An exception has occurred, use %tb to see the full traceback.
    

    SystemExit
    


Thanks for view.
