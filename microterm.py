import sys
import os

global command
command = {'help': ''}

def cmd(name: str, code: str):
  command[name] = code

def term(cmd: str):
  exec(command[cmd])
