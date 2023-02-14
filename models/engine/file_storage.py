#!/usr/bin/env python3
"""serialize and deserialize python obj"""

import json
from models.base_model import BaseModel


class FileStorage:
    """File strorage engine"""
    __file_path = "file.json"
    __objects = {}
    iter = 0

    def all(self):
        """Returns the dictionary object"""
        return self.__objects

    def new(self, obj):
        """set __objectS with dictionary value of object

        Args:
            obj: obj to serialize
        """
        if obj and isinstance(obj, BaseModel):
            self.__objects[obj.__class__.__name__ + "." + obj.id
                           ] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        serializes_dict = {key: obj_dict.to_dict() for key, obj_dict in
                           self.__objects.items()}
        print(serializes_dict)
        with open(self.__file_path, "w", encoding="utf8") as f:
            json.dump(serializes_dict, f)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON
        __file_path exits; otherwise, do nothing, if the file doesn't
        exist, no exception should be raised)
        """
        try:
            with open(self.__file_path, "r", encoding="utf8") as f:
                self.__objects = {key: eval(key.split(".")[0])(**{key: val for
                                                                  key, val
                                                                  in val.
                                                                  items()
                                                                  if key
                                                                  !=
                                                                  "__class__"
                                                                  }) for key,
                                  val in json.load(f).items()}
        except FileNotFoundError:
            pass
