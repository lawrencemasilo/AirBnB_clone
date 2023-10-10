#!/usr/bin/python3
"""command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    class to define all command interpreter behaviour
    """
    prompt = "(hbnb) "

    def emptyline(self):
        print

    def do_quit(self, line):
        return True

    def help_quit(self):
        print("Quit command to exit the program")

    def do_EOF(self, line):
        return True

    def help_EOF(self):
        print("EOF command to exit the program")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
