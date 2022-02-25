# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 07:05:03 2022

@author: zhao
"""
class Person:
    #argument first name and last name
    def __init__(self, first, last):
        self.first = first
        self.last = last
    def fullname(self):
        return self.first + ' ' + self.last

class Student(Person):
    #argument add subject inherit others from Person
    def __init__(self, first, last, subject):
        super().__init__(first, last)
        self.subject = subject
    def printNameSubject(self):
        print(self.fullname() + ','+ ' ' +self.subject)
        
class Teacher(Person):
    #argument add teaching course inherit others from Person
    def __init__(self, first, last, Teachingcourse):
        super().__init__(first, last)
        self.Teachingcourse = Teachingcourse
    def printTeachCourse(self):
        print(self.fullname() + ','+ ' ' +self.Teachingcourse)
    
