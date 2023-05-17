#!/usr/bin/python3
"""
    This is  going to  convert the dictionary representaton to a JSON string.
    Also a JSON string into a dictionary representaion which basically
    deserialization and serializatin.
"""
# file_storage.py

import json
import os


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
        if not isinstance(obj, object):
            raise TypeError
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
            This method serializes __objects to the
        """
        import models
        with open(self.__file_path, mode="w", encoding="utf-8") as json_file:
            obj_dict = {}
            for key, value in self.__objects.items():
                obj_dict[key] = value.to_dict()
            json.dump(obj_dict, json_file)

    def reload(self):
        """
            This method deserializes the JSON file to __objects (only if
            the JSON file (__file_path) exists
        """
        from models.base_model import BaseModel
        if os.path.exists(self.__file_path):
            with open(self.__file_path, mode="r") as json_file:
                try:
                    obj_json = json.load(json_file)
                    for keys, obj_values in obj_json.items():
                        class_name, obj_id = keys.split(".", 1)
                        class_attribute = eval(class_name)
                        obj = class_attribute(**obj_values)
                        self.new(obj)
                except json.JSONDecodeError:
                    pass
        else:
            pass
