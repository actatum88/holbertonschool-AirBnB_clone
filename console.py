#!/usr/bin/python3
"""Entry point for the command interpreter"""
import cmd
import sys

class HBNBCommand(cmd.Cmd):
    
    prompt = '(hbnb) '
    
    def emptyline(self):
        """Will not execute anything on a emptyline"""
        pass
    
    def can_exit(self):
        """Helper for do_quit and do_EOF"""
        return True
    
    def do_quit(self, arg):
        """Quit the command interpreter."""
        exit()

    def do_EOF(self, arg):
        """Quit the command interpreter on EOF."""        
        exit()


# code will not be executed when imported
if __name__ == '__main__':
    HBNBCommand().cmdloop()