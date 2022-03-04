#!/usr/bin/python3
"""The HBNB Console"""
import cmd
import sys
from models import storage
from models.engine.file_storage import FileStorage

dictclass = storage.all_class

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

    def do_create(self, line):
        """Create new instance and prints the id
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        else:
            for i in args:
                if i in dictclass.keys():
                    obj = dictclass[a]()
                    obj.save()
                    print(obj.id)
                else:
                    print("** class doesn't exist **")
                    break

    def do_show(self, line):
        """Prints the string representation
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in dictclass.keys():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in storage.all().keys():
            print("** no instance found **")
        else:
            obj = storage.all()["{}.{}".format(args[0], args[1])]
            print(obj)
            









    
if __name__ == '__main__':
    HBNBCommand().cmdloop()
    
