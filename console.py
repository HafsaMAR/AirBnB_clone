#!/usr/bin/python3

from models.base_model import BaseModel
import cmd 
from models.engine.file_storage import FileStorage
from models import storage


class HBNBCommand(cmd.Cmd):

    
    prompt ="(hbnb) "
    

    
    def  do_emptyline(self, line):
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
  
        if line  in ["user", "city", "amenity", "place", "BaseModel"]:
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
        pass
    def do_destroy(self, line):
        pass
    def do_update(self, line):
        pass
    





if __name__ == '__main__':
    HBNBCommand().cmdloop()