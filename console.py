#!/usr/bin/python3

import ast
from models.base_model import BaseModel
import cmd 
from models.engine.file_storage import FileStorage
from models import storage
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
import re

class HBNBCommand(cmd.Cmd):

    
    prompt ="(hbnb) "
    

    def do_count(self, line):
        """Methode that retrives the number of instances of a class"""
        saved_objects = storage.all()
        count = 0
        args = line.split()
        
        if not args:
            print("** class name missing **")
        else:
            if args[0] not in  ['BaseModel', 'User', 'State', 'Amenity', 'Place', 'Review']:
                print("** class doesn't exist **")
            for key in saved_objects.keys():
                k = key.split(".")
                if k[0] == args[0]:
                    count += 1
        print(count)



    def default(self, line):
        """Handle <class.method> format commands."""
        pattern = re.compile(r'^(\w+)\.(\w+)\(([^)]*)\)$')
        match = pattern.match(line)
        if match:
            class_name, method, args = match.groups()
            class_name = class_name.strip()
            method = method.strip()
            args = args.strip()
            if class_name in ["User", "City", "Amenity", "Place", "BaseModel", "State", "Review"]:
                if method == "all" and not args:  # Handle <class name>.all()
                    self.do_all(class_name)
                elif method == "count" and not args:  # Handle <class name>.count()
                    self.do_count(class_name)
                elif method == "show":
                    casted_arg = args[1:-1]
                    self.do_show(f"{class_name} {casted_arg}")
                elif method == "destroy":
                    casted_arg = args[1:-1]
                    self.do_destroy(f"{class_name} {casted_arg}")
                elif method == "update":
                    # Parse the arguments for update
                    update_args = args.split(', ')
                    if len(update_args) == 3:
                        casted_arg = update_args[0][1,-1]
                        print(casted_arg)
                        # self.do_update(f"{class_name} {casted_arg_prime} {update_args[1]} {update_args[2]}")
                    else:
                        print("** Invalid update format. Use <class name>.update(<id>, <attribute name>, <attribute value>) **")
                else:
                    print("** Unknown method: {}.{} **".format(class_name, method))
            else:
                print("** class doesn't exist **")
        else:
            print("** Unknown syntax: {} **".format(line))

    def do_emptyline(self, line):
        """"an empty line + ENTER shouldn’t execute anything """
        pass

    def do_EOF(self, line):
        """ This Method exit in the END OF FILE """
        return True


    def do_quit(self, line):
        """quit method"""
        return True

    def do_create(self, line):
        if line is None:
            print('** class name missing **')
  
        if line  in ["User", "City", "Amenity", "Place", "BaseModel", "State", "Review"]:
            instance_of_basemodel = eval(line)()
            instance_of_basemodel.save()
            print(instance_of_basemodel.id)
        else:
            print("** class doesn't exist **")

        
    def do_show(self, line):
        """Prints the string representation of an instance based on the class name and id"""
        saved_objects = storage.all()
        args = line.split()
        
        if not args:
            print("** class name missing **")
        
        else:
            class_name = args[0]

            if class_name not in  ['BaseModel', 'User', 'State', 'Amenity', 'Place', 'Review']:
                print("** class doesn't exist **")
                
            elif len(args) < 2:
                print("** instance id missing **")
            
            else:
                obj_id = args[1]   
                key = "{}.{}".format(class_name, obj_id)
                if key in saved_objects:
                    obj= saved_objects[key]
                    print(obj)
                else:
                    print("** no instance found **")


    def do_all(self, line):
        """"Methode that Prints all string representation of 
            all instances based or not on the class name."""
        list_of_instance = []
        output = []

        saved_objects = storage.all()
        check = 0 #check the number of items found
        if not line:
            for key in saved_objects.keys():
                list_of_instance.append(saved_objects[key])
            for i in range(len(list_of_instance)):
                output.append(str(list_of_instance[i]))
            print(output)
        else:
            for key in saved_objects.keys():
                args = key.split('.')
                if line == args[0]:
                    list_of_instance.append(saved_objects[key])
                    check += 1
            if check == 0:
                print("** class doesn't exist **")
            else:
                for i in range(len(list_of_instance)):
                    output.append(str(list_of_instance[i]))
                print(output)

    def do_destroy(self, line):
        """Prints the string representation of an instance based on the class name and id"""
        saved_objects = storage.all()
        args = line.split()
        
        if not args:
            print("** class name missing **")
        
        else:
            class_name = args[0]

            if class_name not in  ['BaseModel', 'User', 'State', 'Amenity', 'Place', 'Review']:
                print("** class doesn't exist **")
                
            elif len(args) < 2:
                print("** instance id missing **")
                       

            else:
                obj_id = args[1]   
                key = "{}.{}".format(class_name, obj_id)
                if key in saved_objects:
                    del saved_objects[key]
                    storage.save()       
                else:    
                    print("** no instance found **")
   
    def do_update(self, line):
        saved_objects = storage.all()
        args = line.split()
        
        if not args:
            print("** class name missing **")
        
        elif args[0] not in  ['BaseModel', 'User', 'State', 'Amenity', 'Place', 'Review']:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
                check = 0
                for key in saved_objects:
                    obj_data = saved_objects[key].__dict__['id']
                    if args[1] == obj_data:
                        check +=1
                        id = key
                          
                if check == 0:
                    print("** no instance found **") 
                elif len(args) < 4:
                        print("** value missing **")
                elif len(args) < 3:
                        print("** attribute name missing **")
                else:
                    saved_objects[id].__dict__[args[2]] = ast.literal_eval(args[3])
                    storage.save()
                
                
    
      


if __name__ == '__main__':
    HBNBCommand().cmdloop()