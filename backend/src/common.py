from flask import Flask,session,redirect,url_for,request,make_response
from datetime import datetime,timedelta
import json
from pymysql import *

app = Flask(__name__,static_url_path='/statistic')

class Query:
    def conn(self):
        db = connect('127.0.0.1', "root", "123456", "mettuan", chatset='utf-8')
        return db

test
1
2
3
