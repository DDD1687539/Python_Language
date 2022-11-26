import os

def function(*args):
    print(args)

function(10)
function(10, 30)
function(30, 405, 50)

def functionArgs(**args):
    print(args)

functionArgs(a=10, b=20)


os.system('notepad.exe')



