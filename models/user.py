#!/usr/bin/python3                                                                                                               
"""Class user"""
from models.base_model import BaseModel

class User(BaseModel):
    """Data del usuario"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
