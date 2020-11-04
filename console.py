#!/usr/bin/python3
import cmd
import string
import sys
import string
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

    """Class for command interpreter"""
    prompt = '(hbnb) '
    file = None

    my_class = {"BaseModel": BaseModel, "Amenity": Amenity,
                "City": City, "Place": Place, "Review": Review,
                "User": User, "State": State}

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
        if arg is "":
            print(" class name missing ")
            return
        arg_list = arg.split()
        try:
            args = eval(arg_list[0])()
        except Class.DoesNotExist:
            print("** class doesn't exist")
            return
        if len(arg_list) is 1:
            print("** instance id missing **")
            return
        instance = 0
        for key, value in storage.all().items():
            if arg is "":
                print(" class name missing ")
                return
        arg_list = arg.split()
        try:
            args = eval(arg_list[0])()
        except Class.DoesNotExist:
            print("** class doesn't exist")
            return
        if len(arg_list) is 1:
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
        """Deletes an instance based on the class name and id"""
        list_arg = arg.split(' ')
        strg = FileStorage()
        strg.reload()
        sv = strg.all()
        if arg == "":
            print(" class name missing ")
        elif list_arg[0] not in HBNBCommand.my_class.keys():
            print(" class doesn't exist ")
        elif len(list_arg) < 2:
            print(" instance id missing ")
        else:
            sv.pop(list_arg[0] + '.' + list_arg[1], None)
            strg.save()

    def do_all(self, arg):
        if arg is "":
            for key, value in storage.all().items():
                print(value)
            return
        arg_list = arg.split()
        try:
            args = eval(arg_list[0])()
        except Class.DoesNotExist:
            print("** class doesn't exist")
            return
        if len(arg_list) is 1:
            print("** instance id missing **")
            return
        instance = []
        for key, value in storage.all().items():
            if key == "{}.{}".format(arg_list[0], arg_list[1]):
                print(value)
                instance.append(value)
        if instance == 0:
            print("** no instance found **")

    def do_count(self, arg):
        if arg is "":
            print("** class name missing **")
            return
        arg_list = arg.split()            
        try:
            args = eval(arg_list[0])()
        except Class.DoesNotExist:
            print("** class doesn't exist")
            return
        count = 0
        for key, value in storage.all().items():
            if key == "{}.{}".format(arg_list[0], arg_list[1]):
                count += 1
                print(count)

    def do_quit(self, arg):
        "Quit command to exit the program\n"
        sys.exit(0)

    def do_EOF(self, arg):
        "Quit command to exit the program\n"
        sys.exit(0)

    def emptyline(self):
        """Ignores empty spaces"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
