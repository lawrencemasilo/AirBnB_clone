#!/usr/bin/python3
"""command interpreter"""
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd, BaseModel):
    """
    class to define all command interpreter behaviour
    """
    prompt = "(hbnb) "

    def emptyline(self):
        """handles empty lines"""
        pass

    """ def postcmd(self):
        handles end of file(Ctrl^D) command
        if line == "EOF":
            return True"""

    def do_quit(self, line):
        """handles (quit) command"""
        return True

    def help_quit(self):
        """(quit) command documentation"""
        print("Quit command to exit the program")

    def do_EOF(self, line):
        """handles end of file command"""
        return True

    def help_EOF(self):
        """(EOF) command documentation"""
        print("EOF command to exit the program")

    def do_create(self, line):
        """
        handles (create) command
        On success, a instance is created, and
        a the id is printed
        """
        if not line:
            print("** class name missing **")
        if line:
            if line != "BaseModel":
                print("** class doesn't exist **")
            if line == "BaseModel":
                instance = BaseModel()
                instance.save()
                print(instance.id)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
