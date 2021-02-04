"""
Wirbank User Operations
~~~~~~~~~~~~~~~~~~~

Conector Para la base de datos del Wirbank

:copyright: (c) 2020 Eduardo Ceja
:license: MIT, see LICENSE for more details.

"""
__title__ = 'user_operations'
__author__ = 'Eduardo Ceja'
__license__ = 'MIT'
__copyright__ = 'Copyright 2020 Eduardo Ceja'
__version__ = '0.0.1'

import os
import random
import datetime
import json
import mysql.connector as db
from mysql.connector import errorcode

config = {'user':'emacc', 'password': '12345', 'host': '127.0.0.1', 'database':'Wirbank', 'raise_on_warnings': True} #test

# with open('wircredentials.txt', 'r') as wircredentials: #production
#     config = json.load(wircredentials)


def error(err):
    """
    Handler de Errores de la base de datos, regresa puros `str` con los errores
    """
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        return "Something is wrong with your user name or password"
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        return "Database does not exist"
    else:
        return str(err)

def register_user(member, init_balance = 10):
    ''' Registra los usuarios a una base de datos. Regresa una tupla con mensage de exito error y un boleano que indica si la operacion fue exitosa '''
    try:
        cnx = db.connect(**config)
        cursor = cnx.cursor()
        query = 'INSERT INTO WirUsuarios (Usuario, Balance) VALUES(%s, %d)'
        cursor.execute(query, tuple((member, init_balance)))
        cnx.commit()
        return 'usuario registrado', True
    except db.Error as err:
        return error(err), False

def balance(member):
    ''' Revisa el balance de los usuarios del wirbanco. Regresa el balance en float,  si no esta registrado regresa un error'''
    try:
        items = []
        cnx =  db.connect(**config)
        cursor = cnx.cursor()
        query = f"SELECT Balance FROM WirUsuarios WHERE Usuario = '{member}'"
        cursor.execute(query)
        for row in cursor:
            items.append(row[0])
        cnx.commit()
        print(items)
        return float(items[0])
    except db.Error as err:
        return error(err)

def update_balance(member, new_balance: float):
    '''Actualiza el balance de los usuarios del wirbanco, regresa error si el usuario no esta en el banco'''
    try:
        cnx = db.connect(**config)
        cursor = cnx.cursor()
        query = f"UPDATE WirUsuarios SET Balance = {new_balance} WHERE Usuairo = '{member}'"
        cursor.execute(query)
        cnx.commit()
        return True, None
    except db.Error as err:
        return False, error(err)
    
def transfer_coins(member_origin, member_target, amount):
    raise NotImplementedError