#!/usr/bin/env python
"""the entry point of the command interpreter"""

import cmd
from models import storage
from models.base_model import BaseModel
import re
from shlex import split
from datetime import datetime




def parse(arg):
    """parse arg with list or dict"""
    iscurly = re.search(r"\{(.*?)\}", arg)
    isbrace = re.search(r"\[(.*?)\]", arg)
    if isbrace:
        cmdlex = [i.strip(",") for i in split(arg[:isbrace.pos()])]
        cmdlex.append(isbrace.group())
    elif iscurly:
        cmdlex = [i.strip(",") for i in split(arg[:iscurly.pos()])]
        cmdlex.append(isbrace.group())
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
    def  do_create(self, model=None):
        model = parse(model)
        if not model:
            print("** class name missing **")
        elif model[0] in self.__defined_models:
            print(eval(model[0])().id)
            storage.save()
        else:
            print("** class doesn't exist **")
    def help_create(self):
        print("\n".join(["Usage: create <Model>", "On class not found <** class"
                         "name missing **>", "on class name doesn't exit <**"
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
        elif not self.__all_objs[args[0] + "." + args[1]]:
            print("** no instance found **")
        else:
            model = eval(args[0])(self.__all_objs[args[0] + "." + args[1]])
            print(model)
    def help_show(self):
        print("\n".join(["Usage: show <model> <id>", "class name is missing"
                         " <** class name missing **>", "class name doesn't"
                         " exist <** class doesn't exist **", "id is missing"
                         " <** instance id missing **>", "class instance doesn"
                         "'t exit <** no instance found **>"]))
    def do_all(self, args):
        args = parse(args)
        list = []
        if not len(args):
            for key, val in self.__all_objs.copy().items():
                del val["__class__"]
                val["updated_at"] = datetime.fromisoformat(val["updated_at"])
                val["created_at"] = datetime.fromisoformat(val["created_at"])
                list.append(f"[{key.split('.')[0]}] ({key.split('.')[1]})" +
                            f" {val}")
        print(list)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
