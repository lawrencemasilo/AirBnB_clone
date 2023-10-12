#!/usr/bin/python3
"""command interpreter"""
import cmd
import shlex
from shlex import split
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd, BaseModel):
    """
    class to define all command interpreter behaviour
    """
    prompt = "(hbnb) "
    __classes = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review,
            }

    def emptyline(self):
        """handles empty lines"""
        pass

    def postcmd(self, stop, line):
        """handles end of file(Ctrl^D) command"""
        return cmd.Cmd.postcmd(self, stop, line)

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
            return
        args = line.split()
        if line:
            if args[0] not in HBNBCommand.__classes:
                print("** class doesn't exist **")
                return
            if args[0] in HBNBCommand.__classes:
                class_name = args[0]
                instance = self.__classes[class_name]()
                instance.save()
                print(instance.id)

    def help_create(self):
        """(create) command documentation"""
        print("creates an instance")

    def do_show(self, line):
        """prints the string representation of a class instance"""
        if not line:
            print("** class name missing **")
            return
        args = line.split()
        if args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        if key not in storage.all().keys():
            print("** no instance found **")
            return
        else:
            print(storage.all()[key])

    def help_show(self):
        """(show) command documentation"""
        print("prints the string representation of a class instance")

    def do_destroy(self, line):
        """deletes an instance"""
        if not line:
            print("** class name missing **")
            return
        args = line.split()
        if args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        if key not in storage.all().keys():
            print("** no instance found **")
            return
        else:
            class_name = args[0]
            instance = self.__classes[class_name]
            instance_id = args[1]
            del storage.all()["{}.{}".format(args[0], args[1])]
            storage.save()

    def help_destroy(self):
        """(destroy) command documentation"""
        print("deletes an instance")

    def do_all(self, line):
        """prints all string representation of all instances"""
        objectList = []
        args = line.split()
        if not line:
            for obj in storage.all().values():
                objectList.append(str(obj))
            print(objectList)

        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        else:
            for obj in storage.all().values():
                if obj.__class__.__name__ == args[0]:
                    objectList.append(str(obj))
            print(objectList)

    def help_all(self):
        """(all) command documentation"""
        print("prints all string representation of all instances")

    def do_update(self, line):
        """updates an instance"""
        if not line:
            print("** class name missing **")
            return
        args = line.split()
        if args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        if key not in storage.all().keys():
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        obj = storage.all()[key]
        setattr(obj, args[2], args[3])
        obj.save()

    def help_update(self):
        """(update) command documentation"""
        print("updates an instance")

    def stripper(self, s):
        """Strips line"""
        new_str = s[s.find("(")+1:s.rfind(")")]
        new_str = shlex.shlex(new_str, posix=True)
        new_str.whitespace += ','
        new_str.whitespace_split = True
        return list(new_str)

    def default(self, line):
        """Default commands."""
        sub_arg = self.stripper(line)
        args = list(shlex.shlex(line, posix=True))
        if args[0] not in HBNBCommand.__classes:
            print("** Unknown syntax: {}".format(line))
            return
        if args[2] == "all":
            self.do_all(args[0])
        else:
            print("** Unknown syntax: {}".format(line))
            return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
