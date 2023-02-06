#!/usr/bin/python3
"""
Base model for AirBnB Project
"""

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Main Class Body"""

    def __init__(self, name="Test"):
        """ Initializer Function """
        self.name = name
        self.id = str(uuid4())
        self.updated_at = self.created_at = datetime.now()

    def __str__(self):
        """
        Prints string representation of the data object
        """
        return "[{self.name}] ({self.id}) {self.__dict__}"

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