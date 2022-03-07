#!/usr/bin/python3
"""
Test Console
"""
import unittest
import uuid
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.place import Place
import os
import json
from datetime import datetime
