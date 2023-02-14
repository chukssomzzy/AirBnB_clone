#!/usr/bin/env python3
"""the entry point of the command interpreter"""

import cmd
import copy
import re
from datetime import datetime
from shlex import split

from models import storage
from models.base_model import BaseModel


def parse(arg):
    """parse arg with list or dict"""
    iscurly = re.search(r"\{(.*?)\}", arg)
    isbrace = re.search(r"\[(.*?)\]", arg)
    if isbrace:
        cmdlex = [i.strip(",") for i in split(arg[:isbrace.pos])]
        cmdlex.append(isbrace.group())
    elif iscurly:
        cmdlex = [i.strip(",") for i in split(arg[:iscurly.pos])]
        cmdlex.append(iscurly.group())
    else:
        cmdlex = [i.strip(",") for i in split(arg)]
    return cmdlex


class HBNBCommand(cmd.Cmd):
    """Airbnb command line interpreter"""
    __defined_models = {
        "BaseModel",
    }
    __all_objs = storage.all()
    prompt = "(hbnb) "

    def do_EOF(self, arg):
        """Control the EOF signal to the command interpreter"""
        return True

    def help_EOF(self):
        print("quit the console")

    def emptyline(self):
        pass

    def do_quit(self, arg):
        """quit terminate the command interpreter"""
        return True

    def help_quit(self):
        print("\n".join(["Quit command to exit the program", ""]))

    def do_create(self, model=None):
        model = parse(model)
        if not model:
            print("** class name missing **")
        elif model[0] in self.__defined_models:
            print(eval(model[0])().id)
            storage.save()
        else:
            print("** class doesn't exist **")

    def help_create(self):
        print("\n".join(["Usage: create <Model>", "On class not found <**"
                         "class name missing **>",
                         "on class name doesn't exit <**"
                         "class doesn't exit **>"]))

    def complete_create(self, text, line, begidx, endidx):
        """Complete create command"""
        return [i for i in self.__defined_models if i.startswith(text)]

    def do_show(self, args):
        """Prints the string representation of an instance based on the class
        name and id
        """
        args = parse(args)
        if not len(args):
            print("** class name missing **")
        elif args[0] not in self.__defined_models:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in self.__all_objs.keys():
            print("** no instance found **")
        else:
            print(self.__all_objs[args[0] + "." + args[1]])

    def help_show(self):
        print("\n".join(["Usage: show <model> <id>", "class name is missing"
                         " <** class name missing **>", "class name doesn't"
                         " exist <** class doesn't exist **", "id is missing"
                         " <** instance id missing **>", "class instance doesn"
                         "'t exit <** no instance found **>"]))

    def do_all(self, args):
        """Prints all string representation of all instances based or
        not on the class

        Ex all BaseModel
        $ all
        """
        args = parse(args)
        list = []
        if not len(args):
            for val in self.__all_objs.values():
                list.append(str(val))
        elif args[0] in self.__defined_models:
            for val in self.__all_objs.values():
                list.append(str(val))
        else:
            print("** class doesn't exist **")
        if len(list):
            print(list)

    def help_all(self):
        print("\n".join(["Usage: all or all <Model>", "Error: ** class doesn't"
                         "exit **"]))

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id

        Ex:
            $ destroy BaseModel 1234-1234-1234
        """
        args = parse(args)
        if not len(args):
            print("** class name missing **")
        elif args[0] not in self.__defined_models:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in self.__all_objs.keys():
            print("** no instance found **")
        else:
            del self.__all_objs[args[0] + "." + args[1]]
            storage.save()

    def do_update(self, args):
        """Updates an instance based on the class name and id by
        adding or updating attribute (save the change into the JSON file)

        Ex:
            $ update BaseModel 1234-1233-1234 email
        Usage:
            update <class name> <id> <attribute name>
            "<attribute value>"
        """

        args = parse(args)
        if not len(args):
            print("** class name missing **")
        elif args[0] not in self.__defined_models:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("instance id missing")
        elif f"{args[0]}.{args[1]}" not in self.__all_objs.keys():
            print("** no instance found **")
        elif len(args) <= 3:
            print("** value missing **")
        else:
            key = args[0] + "." + args[1]
            val_class = getattr(self.__all_objs[key],
                                args[2], None)
            if val_class:
                val_class = eval(val_class.__class__.__name__)
                self.__all_objs[key].__dict__[args[2]] = val_class(args[3])
            else:
                self.__all_objs[key].__dict__[args[2]] = args[3]
            storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
