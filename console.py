#!/usr/bin/python3
''' Module that supports the console behavior
'''
import cmd
import string
import sys
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User
from itertools import count


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    my_class = {"BaseModel": BaseModel, "Amenity": Amenity,
                "City": City, "Place": Place, "Review": Review,
                "User": User, "State": State}
    file = None

    def do_quit(self, arg):
        "Quit command to exit the program"
        sys.exit(1)

    def do_EOF(self, arg):
        "Quit command to exit the program"
        sys.exit(1)

    def emptyline(self):
        """Ignores empty spaces"""
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel
        and saves it to JSON file
        """
        if arg == "":
            print("** class name missing **")
            return
        try:
            new_instance = {}
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")
            return

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        if arg == "":
            print("** class name missing **")
            return
        arg_list = arg.split()
        try:
            args = eval(arg_list[0])()
        except Exception:
            print("** class doesn't exist **")
            return
        if len(arg_list) == 1:
            print("** instance id missing **")
            return
        instance = 0
        for key, value in storage.all().items():
            if key == "{}.{}".format(arg_list[0], arg_list[1]):
                print(value)
                instance = 1
        if instance == 0:
            print("** no instance found **")

    def do_destroy(self, arg):
        """ Delete a class instance of a given id."""
        list_arg = arg.split()
        obj_dict = storage.all()
        if len(list_arg) == 0:
            print("** class name missing **")
        elif list_arg[0] not in HBNBCommand.my_class:
            print("** class doesn't exist **")
        elif len(list_arg) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(list_arg[0], list_arg[1]) not in obj_dict.keys():
            print("** no instance found **")
        else:
            del obj_dict["{}.{}".format(list_arg[0], list_arg[1])]
            storage.save()

    def do_all(self, arg):
        """ Prints all string representation of all instances
         based or not on the class name.
         Ex: $ all BaseModel or $ all."""
        list_arg = arg.split()
        if len(list_arg) > 0 and list_arg[0] not in HBNBCommand.my_class:
            print("** class doesn't exist **")
        else:
            obj_list = []
            for obj in storage.all().values():
                if len(list_arg) > 0 and list_arg[0] == obj.__class__.__name__:
                    obj_list.append(obj.__str__())
                elif len(list_arg) == 0:
                    obj_list.append(obj.__str__())
            print(obj_list)

    def do_update(self, arg):
        """Usage: update <class> <id> <attribute_name> <attribute_value> or
       <class>.update(<id>, <attribute_name>, <attribute_value>) or
       <class>.update(<id>, <dictionary>)
        Update a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary."""
        list_arg = arg.split()
        obj_dict = storage.all()

        if len(list_arg) == 0:
            print("** class name missing **")
            return False
        if list_arg[0] not in HBNBCommand.my_class:
            print("** class doesn't exist **")
            return False
        if len(list_arg) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(list_arg[0], list_arg[1]) not in obj_dict.keys():
            print("** no instance found **")
            return False
        if len(list_arg) == 2:
            print("** attribute name missing **")
            return False
        if len(list_arg) == 3:
            try:
                type(eval(list_arg[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(list_arg) == 4:
            obj = obj_dict["{}.{}".format(list_arg[0], list_arg[1])]
            if list_arg[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[list_arg[2]])
                obj.__dict__[list_arg[2]] = valtype(list_arg[3])
            else:
                obj.__dict__[list_arg[2]] = list_arg[3]
        elif type(eval(list_arg[2])) == dict:
            obj = obj_dict["{}.{}".format(list_arg[0], list_arg[1])]
            for k, v in eval(list_arg[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()

    def do_count(self, arg):
        """Usage: count <class> or <class>.count()
        Retrieve the number of instances of a given class."""
        list_arg = arg.split()
        c = 0
        for obj in storage.all().values():
            if (list_arg[0] == obj.__class__.__name__):
                c += 1
        print(c)

    def precmd(self, arg):
        list_arg = arg.split(".")
        if "()" in arg and len(list_arg) == 2:
            string = list_arg[1].split("(")[0] + " " + list_arg[0]
        elif "("and")" in arg and len(list_arg) == 2:
            spc = " "
            string = list_arg[1].split("(\"")[0] + spc + list_arg[0]
            string2 = spc + list_arg[1].split("(\"")[1].split("\")")[0]
            return string + string2
        else:
            return arg


if __name__ == '__main__':
    HBNBCommand().cmdloop()
