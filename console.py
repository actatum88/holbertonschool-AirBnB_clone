#!/usr/bin/python3
"""Entry point for the command interpreter"""
import cmd
import sys
import models
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

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

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it and prints the id."""
        # Usage: create <class name>
        if not arg:
            print("** class name missing **")
        else:
            class_name = arg.strip()
            if class_name in ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]:
                new_instance = eval(class_name + "()")
                new_instance.save()
                print(new_instance.id)
            else:
                print("** class doesn't exist **")
                
    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id."""
        # Usage: show <class name> <id>
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            class_name, instance_id = args[0], args[1]
            if class_name in ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]:
                all_instances = models.storage.all()
                instance_key = class_name + "." + instance_id
                if instance_key in all_instances:
                    print(all_instances[instance_key])
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")
# code will not be executed when imported
if __name__ == '__main__':
    HBNBCommand().cmdloop()