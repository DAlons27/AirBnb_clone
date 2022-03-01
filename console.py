#!/usr/bin/python3
"""The HBNB Console"""
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'

    def do_EOF(self, line):
        """EOF command to exit the program
        """
        sys.exit(0)

    def do_quit(self, line):
        """Quit command to exit the program
        """
        sys.exit(0)

    def do_help(self, line):
        """Help command
        """
        cmd.Cmd.do_help(self, line)

    def emptyline(self):
        """Does nothing
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
    
