#!/usr/bin/python3
"""Module generic BaseModel class"""
import uuid
from datetime import datetime
import models

"""ftm = format of current time"""
ftm = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """Defines all common attributes/methods for other classes"""
    
    def __init__(self, *args, **kwargs):
        """Initializes a BaseModel object

        Atributes:
                  id: an unique id
                  created_at: creation time
                  update_at: last change time
        """
        
        if kwargs:
            for i, j in kwargs.items():
                if i != "__class__":
                   if i == "created_at" or j == "updated_at":
                      setattr(self, i, datetime.strptime(j, ftm))
                   else:
                      setattr(self, i, j)
                      
        else:
           self.id = str(uuid.uuid4())
           self.created_at = datetime.now()
           self.updated_at = datetime.now()
           models.storage.new(self)
           
    def __str__(self):
       """Returns a string representation of all atributes"""
       return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
       """Records the last changes made to the object"""
       self.updated_at = datetime.now()
       models.storage.save()

    def to_dict(self):
       """Returns a dictionary"""
       dct = self.__dict__.copy()
       if "created_at" in dct:
          dct["created_at"] = dct["created_at"].strftime(ftm)
       if "update_at" in dct:
          dct["updated_at"] = dct["update_at"].strftime(ftm)
       dct["__class__"] = "{}".format(self.__class__.__name__)
       return dct



       
       






                      
                      
                
    
    
