#!/usr/bin/python3
"""
    This is  going to  convert the dictionary representaton to a JSON string.
    Also a JSON string into a dictionary representaion which basically 
    deserialization and serializatin.
"""
# file_storage.py

import json
import os
#import models
#from models.base_model import BaseModel

class FileStorage:
    """
        This class serializes instances to a JSON 
        file and deserializes JSON file to instances.

        Arguments:
            __file_path: string-path to the JSON file(ex: file.json)
            __objects: dictionary -empty but will store all objects by 
            <class name>.id (ex: to store a BaseModel object with 
            id=12121212, the key will be BaseModel.12121212)

        Note: This attributes all private class attributes.
    """

    __file_path = "file.json"
    __objects = {}
    def all(self):
        """
            This method returns dictionary __objects 
            i.e this is a getter method

            Return:
                dictionary
        """
        return self.__objects

    def new(self, obj):
        """
            sets in __objects the obj with key <obj class name>.id

            Args:
                obj: class instance which is an object
            Raise:
               TypeError: if instance is not an object
        """
        #if type(obj) is not object:
            #raise TypeError
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
            This method serializes __objects to the 
        """
        import models
        with open(self.__file_path, mode="w", encoding="utf-8") as json_file:
            #obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
            obj_dict = {} 
            for key, value in self.__objects.items():
                obj_dict[key] = value.to_dict()
            json.dump(obj_dict, json_file)
            #print(obj_dict)

    def reload(self):
        from models.base_model import BaseModel
        from models.user import User
        if os.path.exists(self.__file_path):
            with open(self.__file_path, mode="r") as json_file:
                obj_json = json.load(json_file)
                #try:
                    #obj_json  = json.load(json_file)
                    #for keys, obj_values in obj_json.items():
                        #class_name, obj_id = keys.split(".", 1)
                        #import models
                        #class_attribute = getattr(models, class_name)
                        #print(class_attribute)

                #except json.JSONDecodeError:
                    #pass

        else:
            pass
