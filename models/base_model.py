#!/usr/bin/python3
""" This is a BaseModel class that defines the all common attributes/methods"""
import uuid
from datetime import datetime


class BaseModel:
    """Representing the BaseModel"""
    def __init__(self):
        """
            Public instance attributes:
            id: string - assign with an uuid when an instance is created:
            you can use uuid.uuid4() to generate unique id but don’t forget
            to convert to a string
            the goal is to have unique id for each BaseModel
            created_at: datetime - assign with the current datetime when an
            instance is created
            updated_at: datetime - assign with the current datetime when an
            instance is created and it will be updated every time
            you change your object
        """

        id = str(uuid.uuid4())
        created_at = datetime.now()
        updated_at = datetime.now()
        self.id = id
        self.created_at = created_at
        self.updated_at = updated_at

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
                "updated_at": self.updated_at.isoformat(),
                })
        return my_dict
