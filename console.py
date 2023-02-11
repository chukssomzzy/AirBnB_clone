#!/usr/bin/env python
"""the entry point of the command interpreter"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Airbnb command line interpreter"""
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



if __name__ == "__main__":
    HBNBCommand().cmdloop()
