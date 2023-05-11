#!/usr/bin/python3
""" This is a BaseModel class that defines the all common attributes/methods"""
import uuid
from datetime import datetime


class BaseModel:
    """Representing the BaseModel"""
    def __init__(self, *args, **kwargs):
        """
            initializing the BaseModel and
            using *args, and **kwargs arguments as constructor
            of the BaseModel

            Args:
                *args(tuple(args1, args2))= this is a tuple
                **kwargs({"key":value}) = This is a dictionary
        """

        if kwargs:
            kwargs.pop('__class__', None)
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """__str__:should print: [<class name>] (<self.id>) <self.__dict__>"""

        className = self.__class__.__name__
        id_number = self.id
        my_dict = self.__dict__
        return "[{}] ({}) {}".format(className, id_number, my_dict)

    def save(self):
        """
            This is a public instance method that updates the public
            instance attribute updated_at with the current datetime
        """

        self.updated_at = datetime.now()

    def to_dict(self):
        """This methods returns a dictionary containing all keys/values
           of __dict__ the instance
        """
        my_dict = self.__dict__.copy()
        my_dict.update({
                "__class__": self.__class__.__name__,
                "id": self.id,
                "created_at": self.created_at.isoformat(),
                "updated_at": self.updated_at.isoformat()
                })
        return my_dict
