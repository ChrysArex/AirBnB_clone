#!/usr/bin/python3
"""commande line interpreter for the AirBnB project
"""


import cmd
import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    """CLI main class"""

    prompt = "(hbnb) "

    def do_create(self, class_name):
        if class_name != "":
            if class_name == "BaseModel":
                new = BaseModel()
            elif class_name == "User":
                new = User()
            elif class_name == "State":
                new = State()
            elif class_name == "City":
                new = City()
            elif class_name == "Amenity":
                new = Amenity()
            elif class_name == "Place":
                new = Place()
            elif class_name == "Review":
                new = Review()
            else:
                new = None
            if new:
                new.save()
                print(new.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, cmd):
        try:
            class_name = cmd.split()[0]
        except IndexError:
            class_name = ""
        try:
            obj_id = cmd.split()[1]
        except IndexError:
            obj_id = ""
        if class_name != "":
            data = storage.all()
            available_classes = [
                    "BaseModel",
                    "User",
                    "State",
                    "City",
                    "Amenity",
                    "Place",
                    "Review"
                    ]
            if class_name in available_classes:
                if obj_id != "":
                    try:
                        print(data[str(class_name) + "." + str(obj_id)])
                    except KeyError:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_destroy(self, cmd):
        available_classes = [
                "BaseModel",
                "User",
                "State",
                "City",
                "Amenity",
                "Place",
                "Review"
                    ]
        try:
            class_name = cmd.split()[0]
        except IndexError:
            class_name = ""
        try:
            obj_id = cmd.split()[1]
        except IndexError:
            obj_id = ""
        if class_name != "":
            if class_name in available_classes:
                if obj_id != "":
                    data = storage.all()
                    try:
                        del data[str(class_name) + "." + str(obj_id)]
                        obj_dict = {}
                        for key, value in data.items():
                            obj_dict[key] = value.to_dict()
                        with open("file.json", "w", encoding="utf-8") as mf:
                            json.dump(obj_dict, mf)
                        storage.reload()
                    except KeyError:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_all(self, line):
        available_classes = [
                "BaseModel",
                "User",
                "State",
                "City",
                "Amenity",
                "Place",
                "Review",
                ""
                    ]
        data = storage.all()
        to_print = []
        if line in available_classes:
            for key, value in data.items():
                if key.split(".")[0] == line:
                    to_print.append(value.__str__())
                elif line == "":
                    to_print.append(value.__str__())
            print(to_print)
        else:
            print("** class doesn't exist **")

    def do_update(self, cmd):
        available_classes = [
                "BaseModel",
                "User",
                "State",
                "City",
                "Amenity",
                "Place",
                "Review"
                    ]
        validated = 0
        try:
            class_name = cmd.split()[0]
            if class_name in available_classes:
                validated += 1
            else:
                print("** class doesn't exist **")
        except IndexError:
            print("** class name missing **")
        if validated == 1:
            try:
                obj_id = cmd.split()[1]
                validated += 1
            except IndexError:
                print("** instance id missing ** ")
        if validated == 2:
            try:
                attr_name = cmd.split()[2]
                validated += 1
            except IndexError:
                print("** attribute name missing **")
        if validated == 3:
            try:
                attr_value = cmd.split()[3].replace('"', "")
                validated += 1
            except IndexError:
                print("** value missing **")
        if validated == 4:
            data = storage.all()
            try:
                to_be_updated = data[str(class_name) + "." + str(obj_id)]
                setattr(to_be_updated, attr_name, attr_value)
                to_be_updated.save()
            except KeyError:
                print("** no instance found **")

    def do_BaseModel(self, cmd):
        """Manage commandes for the BaseModel class
        """
        class_name = "BaseModel"
        if cmd == ".all()":
            self.do_all(class_name)
        elif cmd == ".count()":
            data = storage.all()
            count = 0
            for key, value in data.items():
                if key.split(".")[0] == class_name:
                    count += 1
            print(count)
        elif cmd[:6] == ".show(":
            obj_id = ""
            for i in cmd[7:]:
                if i == '"':
                    break
                obj_id += i
            self.do_show(class_name + " " + obj_id)
        elif cmd[:9] == ".destroy(":
            obj_id = ""
            for i in cmd[10:]:
                if i == '"':
                    break
                obj_id += i
            self.do_destroy(class_name + " " + obj_id)
        elif cmd[:8] == ".update(":
            args = cmd[9:].split(", ")
            obj_id = ""
            attr_name = ""
            attr_value = ""
            idx = 0
            if len(args) == 2:
                obj_id = args[0].replace('"', "")
                data = json.load(args[1].replace(")", ""))
                for attr_name, attr_value in data.items():
                    self.do_update(class_name + " " + obj_id + " " +
                                   attr_name + " " + attr_value)
            else:
                for i in args:
                    if idx == 0:
                        obj_id = i.replace('"', "")
                    elif idx == 1:
                        attr_name = i.replace('"', "")
                    elif idx == 2:
                        attr_value = i.replace(")", "")
                    idx += 1
                self.do_update(class_name + " " + obj_id + " " +
                               attr_name + " " + attr_value)

    def do_User(self, cmd):
        """Manage commandes for the BaseModel class
        """
        class_name = "User"
        if cmd == ".all()":
            self.do_all(class_name)
        elif cmd == ".count()":
            data = storage.all()
            count = 0
            for key, value in data.items():
                if key.split(".")[0] == class_name:
                    count += 1
            print(count)
        elif cmd[:6] == ".show(":
            obj_id = ""
            for i in cmd[7:]:
                if i == '"':
                    break
                obj_id += i
            self.do_show(class_name + " " + obj_id)
        elif cmd[:9] == ".destroy(":
            obj_id = ""
            for i in cmd[10:]:
                if i == '"':
                    break
                obj_id += i
            self.do_destroy(class_name + " " + obj_id)
        elif cmd[:8] == ".update(":
            args = cmd[9:].split(", ")
            obj_id = ""
            attr_name = ""
            attr_value = ""
            idx = 0
            if len(args) == 2:
                obj_id = args[0].replace('"', "")
                data = json.load(args[1].replace(")", ""))
                for attr_name, attr_value in data.items():
                    self.do_update(class_name + " " + obj_id + " " +
                                   attr_name + " " + attr_value)
            else:
                for i in args:
                    if idx == 0:
                        obj_id = i.replace('"', "")
                    elif idx == 1:
                        attr_name = i.replace('"', "")
                    elif idx == 2:
                        attr_value = i.replace(")", "")
                    idx += 1
                self.do_update(class_name + " " + obj_id + " " +
                               attr_name + " " + attr_value)

    def do_State(self, cmd):
        """Manage commandes for the BaseModel class
        """
        class_name = "State"
        if cmd == ".all()":
            self.do_all(class_name)
        elif cmd == ".count()":
            data = storage.all()
            count = 0
            for key, value in data.items():
                if key.split(".")[0] == class_name:
                    count += 1
            print(count)
        elif cmd[:6] == ".show(":
            obj_id = ""
            for i in cmd[7:]:
                if i == '"':
                    break
                obj_id += i
            self.do_show(class_name + " " + obj_id)
        elif cmd[:9] == ".destroy(":
            obj_id = ""
            for i in cmd[10:]:
                if i == '"':
                    break
                obj_id += i
            self.do_destroy(class_name + " " + obj_id)
        elif cmd[:8] == ".update(":
            args = cmd[9:].split(", ")
            obj_id = ""
            attr_name = ""
            attr_value = ""
            idx = 0
            if len(args) == 2:
                obj_id = args[0].replace('"', "")
                data = json.load(args[1].replace(")", ""))
                for attr_name, attr_value in data.items():
                    self.do_update(class_name + " " + obj_id + " " +
                                   attr_name + " " + attr_value)
            else:
                for i in args:
                    if idx == 0:
                        obj_id = i.replace('"', "")
                    elif idx == 1:
                        attr_name = i.replace('"', "")
                    elif idx == 2:
                        attr_value = i.replace(")", "")
                    idx += 1
                self.do_update(class_name + " " + obj_id + " " +
                               attr_name + " " + attr_value)

    def do_City(self, cmd):
        """Manage commandes for the BaseModel class
        """
        class_name = "City"
        if cmd == ".all()":
            self.do_all(class_name)
        elif cmd == ".count()":
            data = storage.all()
            count = 0
            for key, value in data.items():
                if key.split(".")[0] == class_name:
                    count += 1
            print(count)
        elif cmd[:6] == ".show(":
            obj_id = ""
            for i in cmd[7:]:
                if i == '"':
                    break
                obj_id += i
            self.do_show(class_name + " " + obj_id)
        elif cmd[:9] == ".destroy(":
            obj_id = ""
            for i in cmd[10:]:
                if i == '"':
                    break
                obj_id += i
            self.do_destroy(class_name + " " + obj_id)
        elif cmd[:8] == ".update(":
            args = cmd[9:].split(", ")
            obj_id = ""
            attr_name = ""
            attr_value = ""
            idx = 0
            if len(args) == 2:
                obj_id = args[0].replace('"', "")
                data = json.load(args[1].replace(")", ""))
                for attr_name, attr_value in data.items():
                    self.do_update(class_name + " " + obj_id + " " +
                                   attr_name + " " + attr_value)
            else:
                for i in args:
                    if idx == 0:
                        obj_id = i.replace('"', "")
                    elif idx == 1:
                        attr_name = i.replace('"', "")
                    elif idx == 2:
                        attr_value = i.replace(")", "")
                    idx += 1
                self.do_update(class_name + " " + obj_id + " " +
                               attr_name + " " + attr_value)

    def do_Amenity(self, cmd):
        """Manage commandes for the BaseModel class
        """
        class_name = "Amenity"
        if cmd == ".all()":
            self.do_all(class_name)
        elif cmd == ".count()":
            data = storage.all()
            count = 0
            for key, value in data.items():
                if key.split(".")[0] == class_name:
                    count += 1
            print(count)
        elif cmd[:6] == ".show(":
            obj_id = ""
            for i in cmd[7:]:
                if i == '"':
                    break
                obj_id += i
            self.do_show(class_name + " " + obj_id)
        elif cmd[:9] == ".destroy(":
            obj_id = ""
            for i in cmd[10:]:
                if i == '"':
                    break
                obj_id += i
            self.do_destroy(class_name + " " + obj_id)
        elif cmd[:8] == ".update(":
            args = cmd[9:].split(", ")
            obj_id = ""
            attr_name = ""
            attr_value = ""
            idx = 0
            if len(args) == 2:
                obj_id = args[0].replace('"', "")
                data = json.load(args[1].replace(")", ""))
                for attr_name, attr_value in data.items():
                    self.do_update(class_name + " " + obj_id + " " +
                                   attr_name + " " + attr_value)
            else:
                for i in args:
                    if idx == 0:
                        obj_id = i.replace('"', "")
                    elif idx == 1:
                        attr_name = i.replace('"', "")
                    elif idx == 2:
                        attr_value = i.replace(")", "")
                    idx += 1
                self.do_update(class_name + " " + obj_id + " " +
                               attr_name + " " + attr_value)

    def do_Place(self, cmd):
        """Manage commandes for the BaseModel class
        """
        class_name = "Place"
        if cmd == ".all()":
            self.do_all(class_name)
        elif cmd == ".count()":
            data = storage.all()
            count = 0
            for key, value in data.items():
                if key.split(".")[0] == class_name:
                    count += 1
            print(count)
        elif cmd[:6] == ".show(":
            obj_id = ""
            for i in cmd[7:]:
                if i == '"':
                    break
                obj_id += i
            self.do_show(class_name + " " + obj_id)
        elif cmd[:9] == ".destroy(":
            obj_id = ""
            for i in cmd[10:]:
                if i == '"':
                    break
                obj_id += i
            self.do_destroy(class_name + " " + obj_id)
        elif cmd[:8] == ".update(":
            args = cmd[9:].split(", ")
            obj_id = ""
            attr_name = ""
            attr_value = ""
            idx = 0
            if len(args) == 2:
                obj_id = args[0].replace('"', "")
                data = json.load(args[1].replace(")", ""))
                for attr_name, attr_value in data.items():
                    self.do_update(class_name + " " + obj_id + " " +
                                   attr_name + " " + attr_value)
            else:
                for i in args:
                    if idx == 0:
                        obj_id = i.replace('"', "")
                    elif idx == 1:
                        attr_name = i.replace('"', "")
                    elif idx == 2:
                        attr_value = i.replace(")", "")
                    idx += 1
                self.do_update(class_name + " " + obj_id + " " +
                               attr_name + " " + attr_value)

    def do_Review(self, cmd):
        """Manage commandes for the BaseModel class
        """
        class_name = "Review"
        if cmd == ".all()":
            self.do_all(class_name)
        elif cmd == ".count()":
            data = storage.all()
            count = 0
            for key, value in data.items():
                if key.split(".")[0] == class_name:
                    count += 1
            print(count)
        elif cmd[:6] == ".show(":
            obj_id = ""
            for i in cmd[7:]:
                if i == '"':
                    break
                obj_id += i
            self.do_show(class_name + " " + obj_id)
        elif cmd[:9] == ".destroy(":
            obj_id = ""
            for i in cmd[10:]:
                if i == '"':
                    break
                obj_id += i
            self.do_destroy(class_name + " " + obj_id)
        elif cmd[:8] == ".update(":
            args = cmd[9:].split(", ")
            obj_id = ""
            attr_name = ""
            attr_value = ""
            idx = 0
            if len(args) == 2:
                obj_id = args[0].replace('"', "")
                data = json.load(args[1].replace(")", ""))
                for attr_name, attr_value in data.items():
                    self.do_update(class_name + " " + obj_id + " " +
                                   attr_name + " " + attr_value)
            else:
                for i in args:
                    if idx == 0:
                        obj_id = i.replace('"', "")
                    elif idx == 1:
                        attr_name = i.replace('"', "")
                    elif idx == 2:
                        attr_value = i.replace(")", "")
                    idx += 1
                self.do_update(class_name + " " + obj_id + " " +
                               attr_name + " " + attr_value)

    def help_create(self):
        print("Creates a new instance of BaseModel,")
        print("saves it (to the JSON file) and prints the id")

    def help_show(self):
        print("Prints the string representation of an instance")
        print("based on the class name and id")

    def help_destroy(self):
        print("Deletes an instance based on the class name and id")

    def help_all(self):
        print("Prints all string representation of all instances")
        print("based or not on the class name")

    def help_update(self):
        print("Updates an instance based on the class name and id")
        print("by adding or updating attribute")

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """exit the CLI"""
        return True

    def emptyline(self):
        """define the behavious when typing an empty line + enter"""
        print(end="")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
