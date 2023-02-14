import sys
import os

global command
global cmdlist
command = {'help': ''}
cmdlist = ['help']

def new_cmd(name: str, code: str):
  command[name] = code
  cmdlist.append(name)

def term(cmd: str):
  exec(command[cmd])

def keep():
  while True:
    pass

def run_sys(cmd: str):
  os.system(cmd)
  
def input_cmd(prompt='> ', check=True, errmsg='No command', msg='Executing'):
  try:
    inp = input(prompt)
    cmdlist.index(name)
    print(msg)
    term(inp)
  except:
    print(errmsg)
