#!/usr/bin/python3

""" This contains the entry point of the command interpreter:
"""
# console0.0.1.py

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """hbnb command interpreter """

    prompt = '(hbnb) '
    class_list = ["BaseModel"]

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, arg):
        """ A method command to exit the program\n"""
        return True

    def emptyline(self):
        """This method return an empty when nothing is enter"""
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
        if not arg:
            obj = storage.all()
            print(obj)
        elif len(arg) > 0:
            args = arg.split()
            if args[0] in self.class_list and len(args) == 1:
                obj = storage.all()
                my_list = []
                for value in obj.values():
                    str_value = "\"{}\"".format(value)
                    my_list.append(str_value)
                convert_str = ", ".join(my_list)
                print(f"[{convert_str}]")
                """obj_model = {}
                obj_t = (self.class_list)
                for key, value in obj.items():
                    if key.startswith((*obj_t)):
                        obj_model.update({key:value})
                print([str(obj_model)])"""
            if args[0] not  in self.class_list and len(args) == 1:
                print("** class doesn't exist **")
        else:
            print("** class name missing**")
 
if __name__ == '__main__':
    HBNBCommand().cmdloop()


