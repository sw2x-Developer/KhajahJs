from py_mini_racer import py_mini_racer
import sys
import os

def runJs(code):
  ctx = py_mini_racer.MiniRacer()
  print(ctx.eval(code.replace("document.write", "return ").replace("console.log" , "return ")))


if(len(sys.argv) > 1 ):
    filename = sys.argv[1].replace(".js" , "")
    if(os.path.exists(filename + ".js")):
        str = open(filename + ".js", 'r').read()
        runJs(str)
    else:
        print("File not found")