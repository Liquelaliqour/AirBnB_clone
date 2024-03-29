#!/usr/bin/python3

"""
A class BaseModel that defines all common attributes/methods for other classes:
"""

from uuid import uuid
from datetime import datetime

class BaseModel:
    """
    A  Public Instance Attributes:
    """
    
    def __init__(self, name):
        # Public instance attribute
        self.name = name

        # Assigning a unique id using uuid.uuid4() and converting it to a string
        self.id = str(uuid.uuid4())

        # Assigning created_at and updated_at with the current datetime
        current_datetime = datetime.utcnow()
        self.created_at = current_datetime
        self.updated_at = current_datetime

    def update_timestamp(self):
        # Updating the updated_at timestamp whenever the object is modified
        self.updated_at = datetime.utcnow()

    def __str__(self) -> str:
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"
    
    """
     A documentation of Public instance methods:
    """

    def __init__(self, name):
        # Public instance method
        self.name = name

    def save(self):
        # Public instance method to update the public instance attribute updated_at with the current datetime
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        # A pubic instance method to return a dictionary containing all keys/values of __dict__ of the instance
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict