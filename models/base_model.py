#!/usr/bin/env python3

"""BaseModel defines all the common attributes/methods"""
import uuid
import datetime
from models import storage


class BaseModel:
    def __init__(self, *args, **kargs):
        """initialize the basemodel from a dict"""
        if kargs:
            for key, val in kargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.datetime.fromisoformat(val))
                elif "__class__" != key:
                    setattr(self, key, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self.to_dict())
    def __str__(self):
        """Returns a string representation of the basemodel"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
    def save(self):
        """Save changes to storage"""
        self.updated_at = datetime.datetime.now()
        storage.new(self.to_dict())
        storage.save()
    def to_dict(self):
        """Returns a dictionary representation of the obj"""
        dict = self.__dict__.copy()
        dict["__class__"] = self.__class__.__name__
        dict["created_at"] = self.created_at.isoformat()
        dict["updated_at"] = self.updated_at.isoformat()
        return dict
