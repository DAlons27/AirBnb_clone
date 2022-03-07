#!/usr/bin/python3
"""The HBNB Console"""
import cmd
import sys
from models import storage
from models.engine.file_storage import FileStorage
import json
import re

dictclass = storage.all_classes

class HBNBCommand(cmd.Cmd):
    """Console HBNB"""
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
                    obj = dictclass[i]()
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
            
    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
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
            del(obj)
            """deletes the instance"""
            del storage.all()["{}.{}".format(args[0], args[1])]
            """deletes the item in the main dictionary"""
            storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances based or
        not on the class name
        """
        args = line.split()
        listobjs = []
        if len(args) == 0:
            for v in storage.all().values():
                listobjs.append(str(v))
            print(listobjs)
        elif args[0] not in dictclass.keys():
            print("** class doesn't exist **")
        else:
            for k, v in storage.all().items():
                clid = k.split('.')
                if clid[0] == args[0]:
                    listobjs.append(str(v))
            print(listobjs)
           
    def do_update(self, line):
        """Updates an instance based on the class name and id by adding
        or updating attribute
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
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            objU = storage.all()["{}.{}".format(args[0], args[1])]
            args[3] = no_quotes(args[3])
            q1 = (args[2] != 'id')
            q2 = (args[2] != 'created_at')
            q3 = (args[2] != 'updated_at')
            if (q1 and q2 and q3):
                if hasattr(objU, args[2]):
                    t = type(getattr(objU, args[2]))
                    setattr(objU, args[2], t(args[3]))
                else:
                    if is_integer(args[3]):
                        setattr(objU, args[2], int(args[3]))
                    elif is_float(args[3]):
                        setattr(objU, args[2], float(args[3]))
                    else:
                        setattr(objU, args[2], args[3])
                objU.save()
            else:
                print("** this attribute can't be updated **")

    def do_count(self, line):
        """Prints the number of instances of a class, or all instances
        """
        args = line.split()
        listobjs = []
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in dictclass.keys():
            if args[0] == "all":
                n = 0
                for key in storage.all().keys():
                    n = n + 1
                print(str(n))
            else:
                print("** class doesn't exist **")
        else:
            n = 0
            for key in storage.all().keys():
                clid = key.split('.')
                if clid[0] == args[0]:
                    n = n + 1
            print(str(n))

    def default(self, line):
        """Checks a new structure of commands: <class>.<command>(<arguments>)
        """
        m = re.search('[^\(\)\.\s]+\.[^\(\)\.\s]+\([^\(\)]*\)', line)
        if m is not None:
            found = re.findall('[^\(\)]*', line)
            clcmd = found[0].split('.')
            argcmd = clcmd[1]
            if hasattr(self, 'do_' + argcmd):
                argclass = clcmd[0]
                linearg = found[2]
                rep = linearg.replace("'", "\"")
                id_dict = re.findall('[^\{\}]*', rep)
                try:
                    dictarg = "{" + id_dict[2] + "}"
                    dictarg = json.loads(dictarg)
                    classid = id_dict[0].replace("\"", "").replace(",", "")
                    argclass += " {}".format(classid)
                    if argcmd == "update":
                        self.dict_update(argclass, **dictarg)
                    else:
                        self.stdout.write('*** Unknown syntax: %s\n'%line)
                except IndexError:
                    itemstr = linearg.split(", ")
                    args = ""
                    for i in range(len(itemstr)):
                        if i != 2:
                            args += itemstr[i].replace("\"", "") + " "
                        else:
                            args += itemstr[i] + " "
                    newl = "{} {} {}".format(argcmd, argclass, args)
                    self.onecmd(newl)
                except json.decoder.JSONDecodeError:
                    print("** Invalid format **")
            else:
                self.stdout.write('*** Unknown syntax: %s\n'%line)
        else:
            self.stdout.write('*** Unknown syntax: %s\n'%line)

    def dict_update(self, line, *args, **kwargs):
        """Same of do_update, but from a dictionary
        """
        lines = ""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in dictclass.keys():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in storage.all().keys():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            for k, w in kwargs.items():
                lines = "update {} {} {}".format(line, str(k), str(w))
                self.onecmd(lines)
            
if __name__ == '__main__':
    HBNBCommand().cmdloop()
