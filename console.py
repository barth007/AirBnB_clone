#!/usr/bin/python3
"""  a program called console.py that contains the entry point of the command interpreter
"""
import cmd
class HBNBCommand(cmd.Cmd):
    """hbnb command interpreter"""
    prompt = '(hbnb) '

    def do_quit(self, arg): 
        """Quit command to exit the program"""
        return True
    def do_EOF(seif, arg):
        """A method that will exit the program"""
        return True
    def emptyline(self):
        """This method does nothing when an empty line is entered"""
        pass
    def help(self):
        """This methods provide help messages for the corresponding commands."""
        prints("")

if __name__ == '__main__':
    HBNBCommand().cmdloop()

