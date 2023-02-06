""" Base model Module """

import datetime
from datetime import datetime
from uuid import uuid4
timestamp = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
 """ Creates Base Model, define attributes for project. """
 def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        
        def __str__(self):
            return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

        def save(self):
            """ Updates public instance to current date/time """
        self.updated_at = datetime.datetime.now()
        self.save = models.storage

        def to_dict(self):
            """ Returing a dictionary containing all keys/values of __dict__ """
        dict_cpy = self.__dict__.copy()
        dict_cpy['__class__'] = type(self).__class__.__name__
        dict_cpy['created_at'] = self.created_at.isoformat()
        dict_cpy['updated_at'] = self.updated_at.isoformat()
        return dict_cpy