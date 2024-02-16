#!/usr/bin/python3
"""This module defines the State class."""
from models.base_model import BaseModel


class State(BaseModel):
    """This class represents a state.

    Attributes:
        name (str): The name of the state.
    """

    name = ""
