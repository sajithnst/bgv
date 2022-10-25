from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
import os

client = MongoClient('mongodb://localhost:27017/')

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
    )
######################## Test API #############################################################
@app.get('/')
async def get():
    return True
######### API related to users #################################################################

class UserModel(BaseModel):
    name : str
    email : str
    password : str
    firstlogin : bool
    status : str = 'pending'

### create a new user and also create a folder with email as filename
@app.post('/user')
async def add_user(user: UserModel):
    filter = {
        'email': user.email,
    }
    if client.bgv.user.count_documents(filter) == 0:
        try:
            os.mkdir(user.email)
        except FileExistsError as e:
            print (str(e))
        try:
            client.bgv.user.insert_one(dict(user))
            return True
        except Exception as e:
            print('Error inserting user: %s' % e)
    else : 
        return False

#### getting user information from database

@app.get('/user')
async def get_user(email : str):
    filter = {
        'email': email
    }
    project = {
        '_id': 0,
    }
    if client.bgv.user.count_documents(filter) == 1:
        return dict(client.bgv.user.find_one(filter,project))
    else : 
        return False
        
################################################################################################

############### API related to HR ##############################################################

class HrModel(BaseModel):
    name : str
    empid :str
    company_email : str
    password : str
    firstlogin: bool

@app.post('/hr')
async def add_hr(hr:HrModel):
    filter = {
        'company_email': hr.company_email
    }
    if client.bgv.hr.count_documents(filter) == 0:
        try:
            client.bgv.hr.insert_one(dict(hr))
            return True
        except Exception as e:
            print('Error inserting hr'+ st(e))
            return False
    else: 
        return False
################################################################################################

############### API related to Notary ##########################################################
class NotaryModel(BaseModel):
    name : str
    email : str
    aadhaar :str
    password : str
    firstlogin : bool

@app.post('/notary')
async def add_notary(notary:NotaryModel):
    filter = {
        'email': notary.email,
    }
    if client.bgv.notary.count_documents(filter) == 0:
        try:
            client.bgv.notary.insert_one(dict(notary))
            return True
        except Exception as e:
            print ('Error inserting notary'+ str(e))
    else :
        return False

#################################################################################################

##################################### Login API #################################################
class Login(BaseModel):
    email :str
    password : str

@app.post("/login")
async def login(login : Login):
    filter = dict(login)

    if client.bgv.user.count_documents(filter) ==1:
        return {'status': True,'user': 'user'}
    else:
        if client.bgv.notary.count_documents(filter) ==1:
                return {'status':True, 'user' : 'notary'}
        else:
            filter = {
                'company_email' : login.email,
                'password' : login.password
            }
            if client.bgv.hr.count_documents(filter) ==1:
                return {'status' : True, 'user': 'hr'}
            else :
                return {'status': False, 'user' : 'Check login creadentials'}
            