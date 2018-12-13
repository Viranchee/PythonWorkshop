# Python

Hooray, no semicolons, only : and \t

= is Binding operator, not assignment operator
type(someVariable)
help(someVariable) Similar to man pages
id(someVariable)
bin(someVariable)
compile()
import os  
dir(os)
globals(): ___name___ = ___main___ OR fileName, if imported to another file.

## Basic Language

Data Types:
    Basic: Integer, Bool, Float, Character<List[0]>
    Lists, Tuples(immutable, like lists), String, Set{}, Dictionary(get,setdefault,update)
    Class: ___init___ ; ___privateVariable___ ; @classmethod method(class) ; @staticmethod ; @property ( get ) ; @variable.setter ( set ) ; @variable.deleter ( delete )  
    Boo, There are no Structs in Python, they are classes, lists, collections

Functions:
    def function( *manyArguments ):
        return manyArguments

    function(1,2,3) # => 1,2,3

    def function( **keywordArguments ):
        print( keywordArguments )

    function( file="workshop", extension = ".py) # => workshop.py

Access scope

    x = 5
    def changeX(value):
        global x
        x = value
        print(x)

    changeX(10)

Control Flow:
    While(condition):, For i in list/collection/range:

Saving Files:
    workspace.py

Importing Files

Interactive Input:
    x = input("Put in something\n")

## Advanced Python

Exception:
    try:
        < >
        raise Error1("Description")
    except Error1 as e1:
        pass
    except (Error2,Error3):
        pass
    else:
        print("NO ERRORS you are doing good")
    finally:
        print("This gets executed Everytime")

    with open("myfile.txt") as file:
        for line in file:
            print(line)

LAMBDA: Advanced Functions, In Bonus Round, if any. Similar to Closures

Testing:
    Use Functions to evaluate conditions

TODO: CLI, Bash, Web Scraping, Networking, JSON & CSV

webbrowser, requests,

Unusual Control Flow:
    breakpoint(*args, **kws)