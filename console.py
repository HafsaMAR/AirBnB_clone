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



class HBNBCommand(cmd.Cmd):

    
    prompt ="(hbnb) "
    

    
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