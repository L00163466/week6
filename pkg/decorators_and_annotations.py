"""
#
# File        : decortors_and_annotations
# Created     : 01/11/21 11:08 AM
# Author      : R. Aravind
# Version     : v1.0.0
# Licencing   : (C) 2021 Aravind Rajesh Kanna, LYIT
                Available under GNU Public License (GPL)
# Credits    :
# Maintainer  :
# Description : Using Overload decorators with getter and setters
#
"""


from typing import overload


class PERSON:
    def __init__(self, name, lnum):
        self._name = name
        self._lnum = lnum

    @property
    def name(self):
        return self._name  # getter

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def display_person_name(self):
        print("Name: {}".format(self._name))

    @staticmethod
    @overload
    def display_person_lnum(lnum: int):
        print("L Num Old Format: {}".format(lnum))

    @staticmethod
    def display_person_lnum(lnum: str):
        print("L Num New Format: {}".format(lnum))


if __name__ == '__main__':
    '''

       Main method of application 

       Calls the person instance with overloading

       Parameters:

        none

       Returns:

        none

    '''

    Joe = PERSON("Joe Bloggs", "L0012345")
    Joe.display_person_name
    Joe.display_person_lnum(123456)
    Joe.display_person_lnum("L00123456")

    Jane = PERSON("Jane", "L0012346")
    Jane.name = "Jane Doe"
    Jane.display_person_name
    Jane.display_person_lnum(1234567)
    Jane.display_person_lnum("L001234567")
