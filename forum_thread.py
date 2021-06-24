#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 16:14:25 2021

@author: haihem
"""
# fils de discussion thread:forum
import crypt
import datetime

class User:
    def __init__(self,id,name,password):
        self.id = id
        self.name = name
        self._salt = crypt.mksalt()
        self._password = self._crypt_pwd(password)
        
    def _crypt_pwd(self,password):
                return crypt.crypt(password, self._salt)

    def check_pwd(self, password):
        return self._password == self._crypt_pwd(password)
#objet THread
    def new_thread(self, title, message):
        return Thread(title, self, message)
# methode du Threa
    def answer_thread(self, thread, message):
        thread.answer(self, message)
        
class Post:
    def __init__(self, author, message):
        self.author = author
        self.message = message
        self.date = datetime.datetime.now()
    def format(self):
        date = self.date.strftime('le %d/%m/%Y à %H:%M:%S')
        return '<div><span>Par {} {}</span><p>{}</p></div>'.format(self.author.name, date, self.message)



if __name__ == '__main__':
    john = User(1, 'john', '12345')
    peter = User(2, 'peter', 'toto')
    thread = john.new_thread('Bienvenue', 'Bienvenue à tous')
    peter.answer_thread(thread, 'Merci')
    print(thread.format())