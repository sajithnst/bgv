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
    empid : str
    company_name : str
    designation : str
    aadhaar : int
    pan : str
    status : str = 'pending'

### create a new user and also create a folder with email as filename
@app.post('/user')
async def add_user(user: UserModel):
    filter = {
        'aadhaar': user.aadhaar,
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
    if client.bgv.user.count_documents(filter) == 0:
        
################################################################################################

############### API related to HR ##############################################################

class HrModel(BaseModel):
    name : str
    company_email : str
    company_name : str
    empid : str
    designation : str
    password : str
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
            print('Error inserting hr'+ str(e))
            return False
    else: 
        return False
################################################################################################

############### API related to Notary ##########################################################
class NotaryModel(BaseModel):
    name : str
    email : str
    password : str
    aadhaar : str
    designation : str = 'Notary'

class SslcModel(BaseModel):
    regno :str
    name : str



