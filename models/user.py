#!/usr/bin/python3
""" Class User, inherits from BaseModel """
from models.base_model import BaseModel


class User(BaseModel):
    """ A class User that inherits from BaseModel """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *agrs, **kwargs):
        """ User init """
        super().__init__(*args, **kwargs)
