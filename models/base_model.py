#!/usr/bin/python3
"""
Base model for AirBnB Project
"""

from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """Main Class Body"""

    def __init__(self, *args, **kwargs):
        """ Initializer Function """
        self.id = str(uuid4())
        self.updated_at = self.created_at = datetime.now()
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, time_format))
                elif key == "__class__":
                    continue
                else:
                    setattr(self, key, value)

    def __str__(self):
        """
        Prints string representation of the data object
        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """
        Updates date of the object.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary with all object data.
        """
        return dict(self.__dict__,
                    __class__=self.__class__.__name__,
                    updated_at=self.updated_at.isoformat(),
                    created_at=self.created_at.isoformat())