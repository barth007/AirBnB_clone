#!/usr/bin/python3
"""  This program contains the entry point of the command interpreter
"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User


class HBNBCommand(cmd.Cmd):

    """hbnb command interpreter"""
    prompt = '(hbnb) '
    class_list = ["BaseModel"]

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(seif, arg):
        """A method that will exit the program\n"""
        return True

    def emptyline(self):
        """This method does nothing when an empty line is entered\n"""
        pass

    def do_create(self, arg):
        """
            Creates a new instance of BaseModel, saves it (to the JSON file)
            and prints the id. Ex: $ create BaseModel
        """
        if not arg:
            print("** class name missing **")
        elif len(arg) > 0:
            args = arg.split()
            if args[0] in self.class_list and len(args) == 1:
                obj = BaseModel()
                obj.save()
                print(obj.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing**")

    def do_show(self, arg):
        """This method shows the class name of a given
           instance of BaseModel
        """
        if not arg:
            print("** class name missing **")
        elif len(arg) > 0:
            args = arg.split()
            if len(args) == 1 and args[0] not in self.class_list:
                print("**class name doesn't exist **")
            elif len(args) == 1 and args[0] in self.class_list:
                print("** instance id missing **")
            elif len(args) == 2 and args[0] in self.class_list:
                key = "{}.{}".format(args[0], args[1])
                obj = storage.all()
                if key in obj:
                    print(obj[key])
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id (
           save the change into the JSON file).
           Ex: $ destroy BaseModel 1234-1234-1234.
        """
        if not arg:
            print("** class name missing **")
        elif len(arg) > 0:
            args = arg.split()
            if len(args) == 1 and args[0] not in self.class_list:
                print("**class name doesn't exist **")
            elif len(args) == 1 and args[0] in self.class_list:
                print("** instance id missing **")
            elif len(args) == 2 and args[0] in self.class_list:
                key = "{}.{}".format(args[0], args[1])
                obj = storage.all()
                if key in obj:
                    del obj[key]
                    storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def do_all(self, arg):
        """
            Creates a new instance of BaseModel, saves it (to the JSON file)
            and prints the id. Ex: $ create BaseModel
        """
        if arg or not arg:
            args = arg.split()
            if args == [] or (args[0] in self.class_list and len(args) == 1):
                obj = storage.all()
                my_list = []
                for value in obj.values():
                    str_value = "\"{}\"".format(value)
                    my_list.append(str_value)
                convert_str = ", ".join(my_list)
                print(f"[{convert_str}]")
            else:
                print("** class doesn't exist **")

    
if __name__ == '__main__':
    HBNBCommand().cmdloop()
