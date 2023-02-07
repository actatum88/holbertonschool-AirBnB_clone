#!/usr/bin/python3
"""
Base model for AirBnB Project
"""

from uuid import uuid4
from datetime import datetime
from .__init__ import storage


class BaseModel:
    """Main Class Body"""
    def __init__(self, *args, **kwargs):
        """Initializer function for Base Model"""
        # if kwargs is not empty
        # *args won’t be used
        if kwargs:
            # each key of this dictionary is an attribute name
            # each value of this dictionary is the value of this attribute name
            for key, value in kwargs.items():
                # __class__ from kwargs is the only one that
                # should not be added as an attribute
                if key != '__class__':
                    setattr(self, key, value)
                else:
                    self.id = str (uuid4())
                    self.updated_at = self.created_at = datetime.now()
                    storage.new(self)
            

    def save(self):
        """
        Updates date of the object.
        """
        self.updated_at = datetime.now()
        
    def to_dict(self):
        """Returns a dictionary with all object data."""
        return dict(self.__dict__,
                    __class__=self.__class__.__name__,
                    updated_at=self.updated_at.isoformat(),
                    created_at=self.created_at.isoformat())