#!/usr/bin/python3                                                                                                               
"""Clase usuario"""
from models.base_model import BaseModel

class Usser(BaseModel):
    """Data del usuario"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
