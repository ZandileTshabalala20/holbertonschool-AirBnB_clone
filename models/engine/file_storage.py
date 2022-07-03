#!/usr/bin/python3
"""
    class FileStorage that serializes instances to a JSON file and deserializes
    JSON file to instances
"""
import json
from os.path import exists


class FileStorage():
    """ class FileStorage """
    __file_path = "file.json"
    __object = {}
    def all(self):
        """ Method all returns the dictionary __objects """
        return self.__object

    def new(self, obj):
        """ Method new sets in __objects the obj with
            key <obj class name>.id
        """
        if obj is None:
            key = obj.__class__.__name__ + "." + obj.id
            setattr(self.__object, key, obj)

    def save(self):
        """ Method save serializes __objects
            to the JSON file (path: __file_path)
        """
        json_obj = {}
        for key in self.__objects:
            json_obj[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w', encoding='UTF-8') as file:
            json.dump(json_obj, file)

    def reload(self):
        """ Method reload deserializes the JSON file to
            __objects (only if the JSON file (__file_path) exists ;
            otherwise, do nothing. If the file doesn’t exist,
            no exception should be raised)
        """
        if(exists(self.__file_path)):
            with open(self.__file_path, 'r', encoding='UTF-8') as f:
                ld = json.load(f)
            for key in ld:
                self.__objects[key] = classes[ld[key]["__class__"]](**ld[key])
