from src.model import Model

from mongoengine import *
import datetime
import json


connect("schemer")


class Schema(Document):
    pass


"""

name
description
schema
timestamp

"""
