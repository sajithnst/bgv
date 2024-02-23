from fastapi import FastAPI,File , UploadFile,Form
from pydantic import BaseModel
from typing import Dict, Optional
from random import choice
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pymongo import MongoClient
from datetime import datetime
from typing import Dict , Optional
from io import StringIO
import pandas as pd
import os


client = MongoClient('mongodb://localhost:27017/')





##############################################################################################

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
    )
######################## Test API #############################################################
@app.get('/' ,tags=['Test'])
async def get():
    return True
######### API related to users #################################################################

class SubmitModel(BaseModel):
    email: str
    status: str='pending'
    submit_button: bool = False 

@app.post('/user/submit',tags=["User"])
async def verify(submit:SubmitModel):
    personal = client.bgv.personal.count_documents({'email' : submit.email})
    sslc = client.bgv.sslc.count_documents({'email':submit.email})
    hse = client.bgv.hse.count_documents({'email':submit.email})
    ug = client.bgv.ug.count_documents({'email' : submit.email})
   
    if personal == 0 or sslc == 0 or hse == 0 or ug == 0:
        return False
    else:
        try:
            filter = {
                'email': submit.email,
            }
            update ={
                '$set':{'status': submit.status, 'submit_button': submit.submit_button}
            }
            client.bgv.user.update_one(filter=filter,update=update)
            return True
        except Exception as e:
            print(str(e))



class UserModel(BaseModel):
    name : str
    email : str
    password : str
    submit_button: bool = True 

### create a new user and also create a folder with email as filename
@app.post('/user',tags=["User"])
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

@app.get('/user',tags=["User"])
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

@app.get('/totalprofile',tags=["User "])
async def total_user():
    try:
        counts = client.bgv.user.count_documents({'status': "verified"})
        count1 = client.bgv.user.count_documents({'status':"pending"})
        count2 = client.bgv.user.count_documents({'status':"InProgress"})
        return {'counts': counts + count1 + count2}
    except Exception as e:
        print(str(e))
        return False


@app.get('/usereducation',tags=["User"])
async def get_usercertificates(email:str):
    filter = {
        'email': email
        }
    project={
        '_id': 0,
    }
    data ={
        'sslc' : dict(client.bgv.sslc.find_one(filter,project)),
        'hse' : dict(client.bgv.hse.find_one(filter,project)),
        'ug': dict(client.bgv.ug.find_one(filter,project)),
    }
    return data

@app.get('userexp',tags=["User"])
async def user_exp(email: str):
    filter ={
        'email': email
    }
    project = {
        '_id': 0,
        }
    if client.bgv.exp.count_documents(filter) == 0:
        return False
    else :
        return list(client.bgv.exp.find(filter,project))

#### generating otp for email verification


####  comparing OTP with existing user account


@app.post('/emailverified',tags=["User"])
async def checkotp(email : str ):

    filter = { 'email' : email}
    update = {
        '$set': {'emailverified' : True}
    }
    try:
        client.bgv.user.find_one_and_update(filter,update)
        return True
    except Exception as e:
        print ("Error in updating email verification status"+str(e))
        return False

## the personal data input api for the user     

class PersonalData(BaseModel):

    empid : str
    doj : str
    email : str
    company_name:str
    designation: str
    company_mail : str
    mob : str
    aadhaar: str
    pan : str
    passport : str
    personal : bool = True
    status : bool = False
    submitted_on : str =  datetime.now()
    edited_on : str =  datetime.now()
    


@app.get('/personal', tags=["Personal"])
async def get_personal(email : str):
    filter = {
        'email': email
    }
    project = {
        '_id': 0,
    }
    if client.bgv.personal.count_documents(filter) == 1:
        return dict(client.bgv.personal.find_one(filter,project))
    else : 
        return False

@app.post('/personal',tags=["Personal"])
async def add_personal( data : PersonalData ):
    filt = {
        'email' : data.email,
        'empid': data.empid,
        'doj': data.doj,
        'company_name':data.company_name,
        'designation' : data.designation,
        'company_mail': data.company_mail,
        'mob': data.mob,
        'aadhaar': data.aadhaar,
        'pan': data.pan,
        'passport': data.passport,
        'personal': data.personal,
        'status': data.status,
        'submitted_on': data.submitted_on
    }
    update={
        '$set':{
        'empid': data.empid,
        'doj': data.doj,
        'company_name':data.company_name,
        'designation' : data.designation,
        'company_mail': data.company_mail,
        'mob': data.mob,
        'aadhaar': data.aadhaar,
        'pan': data.pan,
        'passport': data.passport,
        'personal': data.personal,
        'status': data.status,
        'submitted_on': data.submitted_on

        }
    }

    try: 
        client.bgv.personal.insert_one(filt, update)
        return True
    except Exception as e:
        print (str(e))
        return False
class PersonalAddress(BaseModel):
    email:str
    houseNo:str
    street:str
    region:str
    state:str
    country:str
    zipcode:str
    address:bool=True

@app.post('/personal/address',tags=["Personal"])
async def update_address(data : PersonalAddress):
    filt ={
        'email':data.email
    }
    update={
        '$set':{
        'houseNo':data.houseNo,
        'street':data.street,
        'region' : data.region,
        'state':data.state,
        'country':data.country,
        'zipcode':data.zipcode,
        'address':data.address,
        }
    }
    try:
        client.bgv.personal.find_one_and_update(filt,update)
        return True
    except Exception as e:
        print(str(e))
        return False

@app.post('/personal/update',tags=["Personal"])
async def update( data : PersonalData ):
    filt = {
        'email' : data.email
    }
    update={
        '$set':{
        'empid': data.empid,
        'doj': data.doj,
        'company_name':data.company_name,
        'designation' : data.designation,
        'company_mail': data.company_mail,
        'mob': data.mob,
        'aadhaar': data.aadhaar,
        'pan': data.pan,
        'passport': data.passport,
        'personal': data.personal,
        'status': data.status,
        'edited_on': data.edited_on,
        }
    }

    try: 
        client.bgv.personal.find_one_and_update(filt, update)
        return True
    except Exception as e:
        print (str(e))
        return False



## sslc certificate input

class SSLC(BaseModel):
    sslc_regno : str
    email : str
    sslc_marks : int
    sslc_school : str
    sslc_passout : str
    name : str
    sslc_board : str
    status : bool = False
    submitted_on: str= datetime.now()
    edited_on: str=datetime.now()
@app.post('/sslcupdate',tags=["SSLC"])
async def update( sslc : SSLC ):
    filt = {
        'email' : sslc.email
    }
    update={
        '$set':{
        'sslc_regno': sslc.sslc_regno,
        'sslc_marks':sslc.sslc_marks,
        'sslc_school' : sslc.sslc_school,
        'sslc_passout': sslc.sslc_passout,
        'sslc_board': sslc.sslc_board,
        'status': sslc.status,
        'edited_on': sslc.edited_on
        }
    }

    try: 
        client.bgv.sslc.find_one_and_update(filt, update)
        return True
    except Exception as e:
        print (str(e))
        return False
    
@app.post('/sslc',tags=["SSLC"])
async def sslcinput(sslc : SSLC):
    filt = {
        'email' : sslc.email,
        'sslc_regno': sslc.sslc_regno,
        'sslc_marks':sslc.sslc_marks,
        'sslc_school' : sslc.sslc_school,
        'sslc_passout': sslc.sslc_passout,
        'sslc_board': sslc.sslc_board,
        'status': sslc.status,
        'submitted_on': sslc.submitted_on
    }
    update={
        '$set':{
        'sslc_regno': sslc.sslc_regno,
        'sslc_marks':sslc.sslc_marks,
        'sslc_school' : sslc.sslc_school,
        'sslc_passout': sslc.sslc_passout,
        'sslc_board': sslc.sslc_board,
        'status': sslc.status,
        'submitted_on': sslc.submitted_on

        }
    }

    try: 
        client.bgv.sslc.insert_one(filt, update)
        return True
    except Exception as e:
        print (str(e))
        return False

@app.get('/sslc',tags=["SSLC"])
async def get_sslc(email : str):
    filter = {
        'email': email
    }
    project = {
        '_id': 0,
    }
    if client.bgv.sslc.count_documents(filter) == 1:
        return dict(client.bgv.sslc.find_one(filter,project))
    else : 
        return False



@app.get('/checkpdf',tags=["SSLC"])
async def checkpdf(email: str, regno: Optional[str] = None):
    filter = {
        'email': email
    }
    if(os.path.isfile(f"./{email}/{regno}.pdf")):
        return 'True'
    else:
        return 'False'


### code to upload pdf file 
@app.post('/uploadsslcpdf', tags=["SSLC"])
def upload(email : str = Form(), sslc_regno : str = Form(),file: UploadFile = File(...)):
    if(not os.path.isdir(email)):
         os.mkdir(email)
    path = os.path.join(email,sslc_regno+".pdf")
    try:
        contents = file.file.read()
        with open(path, 'wb') as f:
            f.write(contents)
    except Exception:
        return False
    finally:
        file.file.close()
    return True




@app.get('/getpdf',tags=['READ PDF'])
async def getpdf(email: str, regno: str):
    path = os.path.join(email,regno+".pdf")
    if os.path.exists(path):
        try:
            return FileResponse(path, media_type="application/pdf", filename=regno+".pdf")
        except Exception as e:
            print(str(e))
    else:
        return False



## hser certificate input

class HSE (BaseModel):
    hse_regno: str
    email : str
    hse_marks : int
    hse_passout : str
    hse_school : str
    hse_board : str
    status : bool = False
    submitted_on: str= datetime.now()
    edited_on: str=datetime.now()

@app.post('/hseupdate', tags=["HSE"])
async def update( hse : HSE ):
    filt = {
        'email' : hse.email
    }
    update={
        '$set':{
        'hse_regno': hse.hse_regno,
        'hse_marks':hse.hse_marks,
        'hse_school' : hse.hse_school,
        'hse_passout': hse.hse_passout,
        'hse_board': hse.hse_board,
        'status': hse.status,
        'edited_on': hse.edited_on
        }
    }

    try: 
        client.bgv.hse.find_one_and_update(filt, update)
        return True
    except Exception as e:
        print (str(e))
        return False

@app.post('/hse', tags=["HSE"])
async def hseinput(hse : HSE):
    filt = {
        'email' : hse.email,
        'hse_regno': hse.hse_regno,
        'hse_marks':hse.hse_marks,
        'hse_school' : hse.hse_school,
        'hse_passout': hse.hse_passout,
        'hse_board': hse.hse_board,
        'status': hse.status,
        'submitted_on': hse.submitted_on
    }
    update={
        '$set':{
        'hse_regno': hse.hse_regno,
        'hse_marks':hse.hse_marks,
        'hse_school' : hse.hse_school,
        'hse_passout': hse.hse_passout,
        'hse_board': hse.hse_board,
        'status': hse.status,
        'submitted_on': hse.submitted_on
        }
    }
    try: 
        client.bgv.hse.insert_one(filt, update)
        return True
    except Exception as e:
        print (str(e))
        return False
@app.get('/hse', tags=["HSE"])
async def get_hse(email:str):
    filter = {
        'email': email,
    }
    project={
        '_id':0
    }
    try:
        return dict(client.bgv.hse.find_one(filter,project))
    except Exception as e:
        print (str(e))
        return False

@app.post('/uploadhsepdf', tags=["HSE"])
def upload(email : str = Form(), hse_regno : str = Form(),file: UploadFile = File(...)):
    if(not os.path.isdir(email)):
         os.mkdir(email)
    path = os.path.join(email,hse_regno+".pdf")
    try:
        contents = file.file.read()
        with open(path, 'wb') as f:
            f.write(contents)
    except Exception:
        return False
    finally:
        file.file.close()
    return True

# --------------- API for uploading UG data --------------------------------

class UG(BaseModel):
    ug_regno : str
    email : str
    name : str
    ug_specialization : str
    ug_college : str
    ug_marks : int
    ug_passout : str
    ug_university : str
    status : bool = False
    submitted_on: str= datetime.now()
    edited_on: str=datetime.now()

@app.post('/ugupdate', tags=["UG"])
async def update( ug : UG ):
    filt = {
        'email' : ug.email
    }
    update={
        '$set':{
        'ug_regno': ug.ug_regno,
        'ug_marks':ug.ug_marks,
        'ug_specialization' : ug.ug_specialization,
        'ug_college': ug.ug_college,
        'ug_passout': ug.ug_passout,
        'university': ug.ug_university,
        'status': ug.status,
        'edited_on': ug.edited_on
        }
    }

    try: 
        client.bgv.ug.find_one_and_update(filt, update)
        return True
    except Exception as e:
        print (str(e))
        return False

@app.post('/ug', tags=["UG"])
async def addug(ug: UG):
    filt = {
        'email' : ug.email,
        'ug_regno': ug.ug_regno,
        'ug_marks':ug.ug_marks,
        'ug_specialization' : ug.ug_specialization,
        'ug_college': ug.ug_college,
        'ug_passout': ug.ug_passout,
        'ug_university': ug.ug_university,
        'status': ug.status,
        'submitted_on': ug.submitted_on
    }
    update={
        '$set':{
        'ug_regno': ug.ug_regno,
        'ug_marks':ug.ug_marks,
        'ug_specialization' : ug.ug_specialization,
        'ug_college': ug.ug_college,
        'ug_passout': ug.ug_passout,
        'ug_university': ug.ug_university,
        'status': ug.status,
        'submitted_on': ug.submitted_on
        }
    }
    try: 
        client.bgv.ug.insert_one(filt, update)
        return True
    except Exception as e:
        print (str(e))
        return False


@app.get('/ug', tags=["UG"])
async def get_ug(email:str):
    filter = {'email': email}
    project = {
        '_id':0
    }
    try:
        return dict(client.bgv.ug.find_one(filter,project))
    except Exception as e:
        print(str(e))
        return False

@app.post('/uploadugpdf', tags=["UG"])
def upload(email : str = Form(), ug_regno : str = Form(),file: UploadFile = File(...)):
    if(not os.path.isdir(email)):
         os.mkdir(email)
    path = os.path.join(email,ug_regno+".pdf")
    try:
        contents = file.file.read()
        with open(path, 'wb') as f:
            f.write(contents)
    except Exception:
        return False
    finally:
        file.file.close()
    return True
######### PG DETAILS ##################
class updation(BaseModel):
    email: str 
    status: bool = False
    submit_button: bool = True 


@app.post('/user/pgupdation')
async def add_pgupdation(pg: updation):
    filter={
        'email': pg.email,
    }
    update={
        '$set':{
            'status': pg.status, 'submit_button': pg.submit_button
        }
    }
    try:
        client.bgv.user.find_one_and_update(filter, update)
        return True
    except Exception as e:
        print(str(e))
        return False

@app.post('/user/expupdation')
async def add_expupdation(exp: updation):
    filter={
        'email': exp.email,
    }
    update={
        '$set':{
            'status': exp.status, 'submit_button': exp.submit_button
        }
    }
    try:
        client.bgv.user.find_one_and_update(filter, update)
        return True
    except Exception as e:
        print(str(e))
        return False

class PG(BaseModel):
    pg_regno : str
    email : str
    name : str
    pg_specialization : str
    pg_college : str
    pg_marks : int
    pg_passout : str
    pg_university : str
    status : bool = False
    submitted_on: str= datetime.now()
    edited_on: str=datetime.now()

@app.post('/pgupdate')
async def update( pg : PG ):
    filt = {
        'email' : pg.email
    }
    update={
        '$set':{
        'pg_regno': pg.pg_regno,
        'pg_marks':pg.pg_marks,
        'pg_specialization' : pg.pg_specialization,
        'pg_college': pg.pg_college,
        'pg_passout': pg.pg_passout,
        'pg_university': pg.pg_university,
        'status': pg.status,
        'edited_on': pg.edited_on
        }
    }

    try: 
        client.bgv.pg.find_one_and_update(filt, update)
        return True
    except Exception as e:
        print (str(e))
        return False

@app.post('/pg')
async def addpg(pg: PG):
    filt = {
        'email' : pg.email,
        'pg_regno': pg.pg_regno,
        'pg_marks':pg.pg_marks,
        'pg_specialization' : pg.pg_specialization,
        'pg_college': pg.pg_college,
        'pg_passout': pg.pg_passout,
        'pg_university': pg.pg_university,
        'status': pg.status,
        'submitted_on': pg.submitted_on
    }
    update={
        '$set':{
        'pg_regno': pg.pg_regno,
        'pg_marks':pg.pg_marks,
        'pg_specialization' : pg.pg_specialization,
        'pg_college': pg.pg_college,
        'pg_passout': pg.pg_passout,
        'pg_university': pg.pg_university,
        'status': pg.status,
        'submitted_on': pg.submitted_on
        }
    }
    try: 
        client.bgv.pg.insert_one(filt, update)
        return True
    except Exception as e:
        print (str(e))
        return False


@app.get('/pg')
async def get_pg(email:str):
    filter = {'email': email}
    project = {
        '_id':0
    }
    try:
        return dict(client.bgv.pg.find_one(filter,project))
    except Exception as e:
        print(str(e))
        return False

@app.post('/uploadpgpdf')
def upload(email : str = Form(), pg_regno : str = Form(),file: UploadFile = File(...)):
    if(not os.path.isdir(email)):
         os.mkdir(email)
    path = os.path.join(email,pg_regno+".pdf")
    try:
        contents = file.file.read()
        with open(path, 'wb') as f:
            f.write(contents)
    except Exception:
        return False
    finally:
        file.file.close()
    return True
######### Experience models and API ################################

class Experience(BaseModel):
    empid : str
    name : str
    email : str
    company_name : str
    hr_mail : str
    start_date : str
    end_date : str
    designation : str
    lpa : str
    reporting_manager : str
    status : bool = False
    submitted_on: str= datetime.now()
    edited_on: str=datetime.now()

#### API to add experience  #########################
@app.post('/expupdate')
async def update( exp : Experience ):
    filt = {
        'email' : exp.email
    }
    update={
        '$set':{
        'empid': exp.empid,
        'company_name':exp.company_name,
        'hr_mail': exp.hr_mail,
        'start_date': exp.start_date,
        'end_date': exp.end_date,
        'designation': exp.designation,
        'lpa': exp.lpa,
        'reporting_manager': exp.reporting_manager,
        'status': exp.status,
        'edited_on': exp.edited_on
        }
    }

    try: 
        client.bgv.exp.find_one_and_update(filt, update)
        return True
    except Exception as e:
        print (str(e))
        return False
    
@app.post('/exp')
async def add_exp(exp :Experience):
    filt = {
        'email' : exp.email,
        'empid': exp.empid,
        'company_name':exp.company_name,
        'hr_mail': exp.hr_mail,
        'start_date': exp.start_date,
        'end_date': exp.end_date,
        'designation': exp.designation,
        'lpa': exp.lpa,
        'reporting_manager': exp.reporting_manager,
        'status': exp.status,
        'submitted_on': exp.submitted_on
    }
    update={
        '$set':{
        'empid': exp.empid,
        'company_name':exp.company_name,
        'hr_mail': exp.hr_mail,
        'start_date': exp.start_date,
        'end_date': exp.end_date,
        'designation': exp.designation,
        'lpa': exp.lpa,
        'reporting_manager': exp.reporting_manager,
        'status': exp.status,
        'submitted_on': exp.submitted_on
        }
    }
    try: 
        client.bgv.exp.insert_one(filt, update)
        return True
    except Exception as e:
        print (str(e))
        return False

@app.get('/exp')
async def get_experience(email: str):
    filter ={
        'email' : email,
    }
    project ={
        '_id':0,
        }
    
    try:
        
        return list(client.bgv.exp.find(filter,project))
        
    except Exception as e:
        print(str(e))
        return False

"""@app.get('/exp')
async def get_exp(email:str):
    filter = {'email': email}
    project = {
        '_id':0
    }
    try:
        return dict(client.bgv.exp.find_one(filter,project))
    except Exception as e:
        print(str(e))
        return False"""



@app.post('/uploadexppdf')
def upload(email : str = Form(), empid : str = Form(),file: UploadFile = File(...)):
    if(not os.path.isdir(email)):
         os.mkdir(email)
    path = os.path.join(email,empid+".pdf")
    try:
        contents = file.file.read()
        with open(path, 'wb') as f:
            f.write(contents)
    except Exception:
        return False
    finally:
        file.file.close()
    return True

 
class Expupdate(BaseModel):
    empid : str
    reason : str
    rehire : str
    dues: str
    relieved: str
    remarks: str
@app.post('/expdataadd')
async def dataadd(data : Expupdate):
    filter = {
        'empid' : data.empid
    }
    update = {
        '$set': {
            'reason': data.reason,
            'dues': data.dues,
            'relieved': data.relieved,
            'remarks': data.remarks,
            'rehire': data.rehire
        }
    }
    try:
        client.bgv.exp.find_one_and_update(filter, update)
        return True
    except Exception as e:
        print(str(e))
        return False
    
        
################################################################################################

############### API related to HR ##############################################################

class HrModel(BaseModel):
    name : str
    company_reg:str
    company_mail : str
    password : str
    mob:str
    gst:str
    status:str='pending'
    
@app.post('/hr')
async def add_hr(hr:HrModel):
    filter = {
        'company_email': hr.company_mail
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
@app.get('/hr')
async def get_hr(company_mail: str):
    try :
        filter = {
            'company_mail':company_mail
            }
        project ={
            '_id':0,
        }
        return dict(client.bgv.hr.find_one(filter,project))
    except Exception as e:
        print('Error getting hr'+ str(e))
        return False
class Hrprofile(BaseModel):
    company_mail : str
@app.post('/hrprofile')
async def gethr(hr:Hrprofile):
    try:
        filter = dict(hr)
        project={
            '_id':0,
            'name': 1,
            'company_mail': 1
        }
        return dict(client.bgv.hr.find_one(filter,project))
    except Exception as e:
        print('Error getting hr'+ str(e))
        return False
    
@app.post('/uploadgstn')
async def uploadgstn(company_mail : str = Form(), file: UploadFile = File(...)):
      if(not os.path.isdir(company_mail)):
         os.mkdir(company_mail)
      path = os.path.join(company_mail, file.filename)
      try:
         contents = file.file.read()
         with open(path, 'wb') as f:
          f.write(contents)
      except Exception:
       return False
      finally:
         file.file.close()

      return True
################################################################################################

############### API related to Notary ##########################################################

@app.get('/notary')
async def get_notary(email: str):
    try :
        filter = {
            'email':email
            }
        project ={
            '_id':0,
        }
        return dict(client.bgv.notary.find_one(filter,project))
    except Exception as e:
        print('Error getting notary'+ str(e))
        return False

class NotaryModel(BaseModel):
    name : str
    email : str
    aadhaar :str
    password : str
    mob:str
    pan:str
    status:str='pending'

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

class NLogin(BaseModel):
    email : str
    password : Optional[str] = None
    login_date: str = datetime.now()
    last_login: str = datetime.now()
    notary_last_visited: str = datetime.now()

@app.post('/notary/user_lastvisited')
async def user_lastvisited(data: NLogin):
    filter={
        'email': data.email
    }
    update={
        '$set':{
            'notary_last_visited': data.notary_last_visited
        }
    }
    try:
        client.bgv.user.update_one(filter, update)
        return True
    except Exception as e:
        print(str(e))
        return False

@app.get("/notary/login")
async def login(email : str, password : str):
    filter = {
        'email': email,
        'password': password
    }

    if client.bgv.notary.count_documents(filter) ==1:
        return True 
    else:
        return False
    
@app.post('/notarylogin')
async def notary_login(login:NLogin):
    try:
        if(client.bgv.notary.count_documents(dict(login))) ==1:
            return True
        else:
            return False
    except Exception as e:
        print(str(e))
        return False

@app.post('/notary/logindate')
async def notary_logindate(login:NLogin):
    filter={
        'email': login.email
    }
    update={
        '$set':{
            'login_date':login.login_date,
        }
    }
    try:
        client.bgv.notary.update_one(filter, update)
        return True
    except Exception as e:
        print(str(e))
        return False

@app.post('/notary/last_login')
async def notary_lastlogin(login:NLogin):
    filter={
        'email': login.email
    }
    update={
        '$set':{
                  'last_login': login.last_login
        }
  
    }
    try:
        client.bgv.notary.update_one(filter, update)
        return True
    except Exception as e:
        print(str(e))
        return False



#################################################################################################

##################################### Login API #################################################


@app.get("/login")
async def login(email : str, password : str):
    filter = {
        'email': email,
        'password': password
    }

    if client.bgv.user.count_documents(filter) ==1:
        return True 
    else:
        return False

class HRLogin(BaseModel):
    company_mail :str
    password : Optional[str] = None
    login_date: str = datetime.now()
    last_login: str = datetime.now()

@app.post('/hr/login_date')
async def hr_logindate(login:HRLogin):
    filter={
        'company_mail': login.company_mail
    }
    update={
        '$set':{
            'login_date':login.login_date,
        }
    }
    try:
        client.bgv.hr.update_one(filter, update)
        return True
    except Exception as e:
        print(str(e))
        return False

@app.post('/hr/last_login')
async def hr_lastlogin(login:HRLogin):
    filter={
        'company_mail': login.company_mail
        }
    update={
        '$set':{
            'last_login':login.last_login,
        }
    }
    try:
        client.bgv.hr.update_one(filter, update)
        return True
    except Exception as e:
        print(str(e))
        return False

@app.get("/hr/login")
async def hr_login(company_mail : str, password : str):
    filter = {
        'company_mail': company_mail,
        'password': password
    }

    if client.bgv.hr.count_documents(filter) ==1:
        return True 
    else:
        return False


@app.get('/pendinguser')
async def pendinguser():
    filter ={
        'status' : 'pending',
    }
    project ={
        '_id':0,
        }
    
    try:
        count = client.bgv.user.count_documents(filter)
        return {"count":count, "list": list(client.bgv.user.find(filter,project))}
        
    except Exception as e:
        print(str(e))
        return False

@app.get('/verifiedusers')
async def apprpvedusers():
    try:
        filter ={
            'status' : 'verified'
            }
        project ={
            '_id':0
            }
        count1 = client.bgv.user.count_documents(filter)
        return {"count1": count1, "list":list(client.bgv.user.find(filter,project))}
    except Exception as e:
        print(str(e))
        return False





class Verify(BaseModel):
    user_email : str
    empid: Optional[str] = None 
    sslc_regno: Optional[str] = None
    hse_regno: Optional[str] = None
    ug_regno: Optional[str] = None
    pg_regno: Optional[str] = None
    notary_email: str
    notary_name :str
    status : str = "verified"
    approved_on: str= datetime.now()

@app.post('/verify/user')
async def verify(verify:Verify):
    personal = client.bgv.personal.count_documents({'email' : verify.user_email, 'status' : False})

    sslc = client.bgv.sslc.count_documents({'email':verify.user_email,'status':False})
    hse = client.bgv.hse.count_documents({'email':verify.user_email,'status':False})
    ug = client.bgv.ug.count_documents({'email' : verify.user_email, 'status' : False})
    pg = client.bgv.pg.count_documents({'email' : verify.user_email, 'status' : False})
    exp = client.bgv.exp.count_documents({'email' : verify.user_email, 'status' : False})


    if sslc+hse+ug+pg+exp+personal == 0:
        try:
        
            filter = {
                'email': verify.user_email,
            }
            update ={
                '$set':{ 'approved_on':verify.approved_on,'status': verify.status, 'notary_email': verify.notary_email, 'notary_name':verify.notary_name}
            }
            client.bgv.user.update_one(filter=filter,update=update)
            return True
        except Exception as e:
            print(str(e))
    else:
        return False

@app.post('/verify/personaldetails')
async def verify(verify : Verify):
    try:
        filter = {
            'email': verify.user_email,
        }
        update = {
            '$set' : {
                'approved_on':verify.approved_on,
                'status' : verify.status,
                'notary_email' : verify.notary_email,
                'notary_name' : verify.notary_name
            }
        }
        client.bgv.personal.find_one_and_update(filter=filter,update=update)
        return True
    except Exception as e:
        print(str(e))
        return False


@app.post('/verify/sslc')
async def verifysslc(verify : Verify):
    try:
        filter = {
            'email': verify.user_email,
            'sslc_regno': verify.sslc_regno
        }
        update = {
            '$set' : {
                'approved_on':verify.approved_on,
                'status' : verify.status,
                'notary_email' : verify.notary_email,
                'notary_name' : verify.notary_name
            }
        }
        client.bgv.sslc.find_one_and_update(filter=filter,update=update)
        return True
    except Exception as e:
        print(str(e))
        return False

@app.post('/verify/hse')
async def verifyhse(verify: Verify):
    try:
        filter = {
            'email' : verify.user_email,
            'hse_regno': verify.hse_regno
        }
        update = {
            '$set' : {
                'approved_on':verify.approved_on,
                'status' : verify.status,
                'notary_email' : verify.notary_email,
                'notary_name' : verify.notary_name
            }
        }
        client.bgv.hse.find_one_and_update(filter=filter,update=update)
        return True
    except Exception as e:
        print(str(e))
        return False

@app.post('/verify/ug')
async def verifyug(verify: Verify):
    try:
        filter = {
            'email' : verify.user_email,
            'ug_regno': verify.ug_regno
        }
        update = {
            '$set' : {
                'approved_on':verify.approved_on,
                'status' : verify.status,
                'notary_email' : verify.notary_email,
                'notary_name' : verify.notary_name
            }
        }
        client.bgv.ug.find_one_and_update(filter=filter,update=update)
        return True
    except Exception as e:
        print(str(e))
        return False

@app.post('/verify/pg')
async def verifypg(verify: Verify):
    try :
        filter = {
            'email' : verify.user_email,
            'pg_regno': verify.pg_regno
        }
        update = {
            '$set' : {
                'approved_on':verify.approved_on,
                'status' : verify.status,
                'notary_email' : verify.notary_email,
                'notary_name' : verify.notary_name
            }
        }
        client.bgv.pg.find_one_and_update(filter=filter,update=update)
        return True
    except Exception as e:
        print(str(e))
        return False

@app.post('/verify/exp')
async def verifyexp(verify: Verify):
    try:
        filter = {
            'email' : verify.user_email,
            'empid' : verify.empid
        }
        update = {
            '$set' : {
                'approved_on':verify.approved_on,
                'status' : verify.status,
                'notary_email' : verify.notary_email,
                'notary_name' : verify.notary_name
            }
        }
        client.bgv.exp.find_one_and_update(filter=filter,update=update)
        return True
    except Exception as e:
        print(str(e))
        return False
## API to create view request

class Request(BaseModel):
    user_email : str
    hr_email :str
    hr_name:str
    status: str = 'pending'
@app.post('/requestdata')
async def request(request:Request):
    try:
        client.bgv.request.insert_one(dict(request))
        return True
    except Exception as e:
        print(str(e))
        return False
## API to update request status
@app.get('/user/pendingrequest')
async def get_request(email:str):
    try:
        filter = {
            'user_email': email,
            'status' :'pending'
            }
        project ={
            '_id':0
        }
        return list(client.bgv.request.find(filter,project))
    except Exception as e:
        print(str(e))
        return False

@app.get('/user/approved')
async def get_approved(email:str):
    try:
        filter = {
            'user_email': email,
            'status':'approved'
        }
        project ={
            '_id':0
            }
        return list(client.bgv.request.find(filter,project))
    except Exception as e:
        print(str(e))
        return False



@app.get('/hr/pendingrequest')
async def pendingrequest(hr_email: str):
    try:
        pipeline = [
            {
                '$match': {
                    'hr_email': hr_email, 
                    'status': 'pending'
                }
            }, {
                '$lookup': {
                    'from': 'user', 
                    'localField': 'user_email', 
                    'foreignField': 'email', 
                    'as': 'user_name'
                }
            }, {
                '$addFields': {
                    'user_name': {
                        '$arrayElemAt': [
                            '$user_name', 0
                        ]
                    }
                }
            }, {
                '$addFields': {
                    'user_name': '$user_name.name', 
                    'user_designation': '$user_name.designation'
                }
            }, {
                '$project': {
                    '_id': 0
                }
            }
]
        return list(client.bgv.request.aggregate(pipeline))
    except Exception as e:
        print(str(e))
        return False

@app.get('/hr/approved')
async def approvedhr(email: str):
    try:
        filter ={
            'hr_email':email,
            'status':'approved'
            }
        project={
            '_id':0
        }
        return list(client.bgv.request.find(filter,project))
    except Exception as e:
        print(str(e))
        return False


class UpdateRequest(BaseModel):
    user_email : str
    hr_email : str
    status : str
@app.post('/request/update')
async def update_user(update : UpdateRequest ):
    try:
        filter = {
            'user_email': update.user_email,
            'hr_email' : update.hr_email,
            'status': 'pending'
            }
        update= {
            '$set' : {
                'status' : update.status
            }
        }
        client.bgv.request.update_one(filter, update)
        return True
    except Exception as e:
        print(str(e))
        return False




@app.post('/user/filter')
async def user_filter(query : Dict):
    try:
        filter = query
        project = {
            "_id":0
        }
        return list(client.bgv.user.find(filter,project))
    except Exception as e:
        print(str(e))
        return False



#############Super Admin ###########

class Admin(BaseModel):
      name: str
      admin_email: str
      password: str

@app.post("/admin")
async def add_admin(admin: Admin):
      try:
        client.bgv.admin.insert_one(dict(admin))
        return True
      except Exception as e:
        print(str(e))
      return False

@app.get('/admin')
async def get_user(admin_email:str):
    filter={
        'admin_email':admin_email
    }
    project ={
        '_id':0,
    }
    if client.bgv.admin.count_documents(filter)==1:
        return dict(client.bgv.admin.find_one(filter,project))
    else:
        return False

class Adminlogin(BaseModel):
      admin_email : str
      password : str
@app.post('/adminlogin')
async def admin_login(login:Adminlogin):
      try:
        if(client.bgv.admin.count_documents(dict(login)) ==1):
          return True
        else:
          return False
      except Exception as e:
        print(str(e))
        return False
      
      
@app.post('/hr/uploadcsv')
async def uploadcsv(company_mail: str= Form(),file: UploadFile = File(...) ):
   if(not os.path.isdir(company_mail)):
       os.mkdir(company_mail)
   path = os.path.join(company_mail,file.filename)
   try:
        contents = file.file.read()
        with open(path, 'wb') as f:
            f.write(contents)
   except Exception:
        return False
   finally:
        file.file.close()
   return True
    
############### CompanyRegistration ################################
@app.get('/company/pending')
async def company_pending():
    filter={
        'status':"pending"
    }
    project={
        '_id':0
    }
    try:
        Ccount=client.bgv.hr.count_documents(filter)
        return {'Ccount':Ccount,'list':list(client.bgv.hr.find(filter,project))}
    except Exception as e:
        print(str(e))
        return False
    
@app.get('/company/verified')
async def company_verified():
    filter={
        'status':"verified"
    }
    project={
        '_id':0
    }
    try:
        Gcount=client.bgv.hr.count_documents(filter)
        return {'Gcount':Gcount,'list':list(client.bgv.hr.find(filter,project))}
    except Exception as e:
        print(str(e))
        return False
#####################NotayRegistration################

@app.get('/notary/pending')
async def notary_pending():
    filter={
        'status':"pending"
    }
    project={
        '_id':0
    }
    try:
        Ecount=client.bgv.notary.count_documents(filter)
        return{'Ecount':Ecount,'list':list(client.bgv.notary.find(filter,project))}
    except Exception as e:
        print(str(e))
        return False
    
@app.get('/notary/verified')
async def notary_verified():
    filter={
        'status':"verified"
    }
    project={
        '_id':0
    }
    try:
        Fcount=client.bgv.notary.count_documents(filter)
        return{'Fcount':Fcount,'list':list(client.bgv.notary.find(filter,project))}
    
    except Exception as e:
        print(str(e))
        return False
    
class SuperAdminVerify(BaseModel):
    company_mail:Optional[str] = None
    email:Optional[str] = None
    admin_email:str
    name:str
    status:str="verified"

@app.post('/company/verification')
async def verify_company(data:SuperAdminVerify):
    filter={
        'company_mail':data.company_mail
    }
    update={
        '$set':{
            'admin_email':data.admin_email,
            'name':data.name,
            'status':data.status
        }
    }
    try:
        client.bgv.hr.find_one_and_update(filter,update)
        return True
    except Exception as e:
        print(str(e))
        return False
    
@app.post('/notary/verification')
async def verify_notary(data:SuperAdminVerify):
    filter={
        'email':data.email
    }
    update={
        '$set':{
            'admin_email':data.admin_email,
            'name':data.name,
            'status':data.status
        }
    }
    try:
        client.bgv.notary.find_one_and_update(filter,update)
        return True
    except Exception as e:
        print(str(e))
        return False
    

#####################InProgress###################
class InProgress(BaseModel):
    email:str
    status:str="InProgress"

@app.post('/personal/inprogress')
async def inprogress_personal(data:InProgress):
    filter={
        'email':data.email
    }
    update={
        '$set':{
            'status':data.status
      }
    }
    try:
        client.bgv.user.find_one_and_update(filter,update)
        return True
    except Exception as e:
        print(str(e))
        return False
    
@app.post('/sslc/inprogress')
async def inprogress_sslc(data:InProgress):
    filter={
        'email':data.email
    }
    update={
        '$set':{
            'status':data.status
      }
    }
    try:
        client.bgv.user.find_one_and_update(filter,update)
        return True
    except Exception as e:
        print(str(e))
        return False
    
@app.post('/hse/inprogress')
async def inprogress_hse(data:InProgress):
    filter={
        'email':data.email
    }
    update={
        '$set':{
            'status':data.status
      }
    }
    try:
        client.bgv.user.find_one_and_update(filter,update)
        return True
    except Exception as e:
        print(str(e))
        return False
    

@app.post('/ug/inprogress')
async def inprogress_ug(data:InProgress):
    filter={
        'email':data.email
    }
    update={
        '$set':{
            'status':data.status
      }
    }
    try:
        client.bgv.user.find_one_and_update(filter,update)
        return True
    except Exception as e:
        print(str(e))
        return False
    

@app.post('/pg/inprogress')
async def inprogress_pg(data:InProgress):
    filter={
        'email':data.email
    }
    update={
        '$set':{
            'status':data.status
      }
    }
    try:
        client.bgv.user.find_one_and_update(filter,update)
        return True
    except Exception as e:
        print(str(e))
        return False
    

   
@app.post('/exp/inprogress')
async def inprogress_exp(data:InProgress):
    filter={
        'email':data.email
    }
    update={
        '$set':{
            'status':data.status
      }
    }
    try:
        client.bgv.user.find_one_and_update(filter,update)
        return True
    except Exception as e:
        print(str(e))
        return False
    

class UserVerified(BaseModel):
    email: str
    status: str="verified"

@app.post('/inprogress_verified')
async def inprogress_verified(user: UserVerified):
    filter={
        'email': user.email, 
        'status': "verified"
    }
    user_filter={
        'email': user.email,
        'status': "InProgress"
    }
    
    project={
        '_id':0
    }
    update={
        '$set':{
            'status':user.status
        }
    }
    
    personal = client.bgv.personal.count_documents(filter)
    sslc = client.bgv.sslc.count_documents(filter)
    hse = client.bgv.hse.count_documents(filter)
    ug = client.bgv.ug.count_documents(filter)

    count_filter={
        'email': user.email
    }
    if client.bgv.pg.count_documents(count_filter) >0 and client.bgv.exp.count_documents(count_filter) >0:
        pg = client.bgv.pg.count_documents(filter)
        exp = client.bgv.exp.count_documents(filter)
        exp_count = client.bgv.exp.count_documents(count_filter)
        if personal > 0 and sslc > 0 and hse > 0 and ug > 0 and pg > 0 and exp == exp_count:
            try:
                client.bgv.user.find_one_and_update(user_filter, update)
                return True
            except Exception as e:
                print(str(e))
                return False

    elif client.bgv.pg.count_documents(count_filter) == 0 and client.bgv.exp.count_documents(count_filter) >0: 
        exp = client.bgv.exp.count_documents(filter)
        exp_count = client.bgv.exp.count_documents(count_filter)

        if personal > 0 and sslc > 0 and hse > 0 and ug > 0 and exp == exp_count:
            try:
                client.bgv.user.find_one_and_update(user_filter, update)
                return True
            except Exception as e:
                print(str(e))
                return False
    elif client.bgv.pg.count_documents(count_filter) > 0 and client.bgv.exp.count_documents(count_filter) == 0:
        pg = client.bgv.pg.count_documents(filter)
        if personal > 0 and sslc > 0 and hse > 0 and ug > 0 and pg > 0:
            try:
                client.bgv.user.find_one_and_update(user_filter, update)
                return True
            except Exception as e:
                print(str(e))
                return False
    elif client.bgv.pg.count_documents(count_filter) == 0  and client.bgv.exp.count_documents(count_filter) == 0:
        if personal > 0 and sslc > 0 and hse > 0 and ug > 0:
            try:
                client.bgv.user.find_one_and_update(user_filter, update)
                return True
            except Exception as e:
                print(str(e))
                return False
    else:
        return False


@app.get('/inprogressuser')
async def inprogressuser():
    filter ={
        'status' : 'InProgress',
    }
    project ={
        '_id':0,
        }
    
    try:
        count = client.bgv.user.count_documents(filter)
        return {"count":count, "list": list(client.bgv.user.find(filter,project))}
        
    except Exception as e:
        print(str(e))
        return False
    
#################################################### Upload CSV File ####################################################################################
@app.post("/hr/uploadpersonal")
async def upload_csv(csv_file: UploadFile = None):
    if csv_file is None:
        return {"message": "No file uploaded"}
    contents = await csv_file.read()
    csv_string = contents.decode("utf-8")
    df = pd.read_csv(StringIO(csv_string))
    df['aadhaar'] = df['aadhaar'].astype(str)
    df['passport'] = df['passport'].astype(str)
    df['mob'] = df['mob'].astype(str)
    insert=df[~df.isnull().any(1)]

    insert['status'] = False
    insert['submitted_on'] = datetime.now()

    user = insert[['email','name']].copy()
    user['submit_button'] = False
    user['status'] = "pending"
    user["password"]="sajith@123"
    try:
        client.bgv.user.insert_many(user.to_dict('records'))
        client.bgv.personal.insert_many(insert.to_dict('records'))

    except Exception as e:
        print(str(e))
    
    delete=df[df.isnull().any(1)]
    delete.fillna(0,inplace=True)
    returndata  = {
        'total_count':len(df.index),
        'insert_count': len(insert.index),
        'delete_count': len(delete.index),
        'insert_list': insert.to_dict('records'),
        'delete_list': delete.to_dict('records'),
    }
    return returndata  
################################################################################################
@app.post("/hr/uploadsslc")
async def upload_csv(csv_file: UploadFile = None):
    if csv_file is None:
        return {"message": "No file uploaded"}
    contents = await csv_file.read()
    csv_string = contents.decode("utf-8")
    df = pd.read_csv(StringIO(csv_string))
    df['sslc_regno'] = df['sslc_regno'].astype(str)
    df['sslc_passout'] = df['sslc_passout'].astype(str)
    df['sslc_marks'] = df['sslc_marks'].astype(str)
    insert=df[~df.isnull().any(1)]
    insert['status'] = False
    insert['submitted_on'] = datetime.now()
    try:
        client.bgv.sslc.insert_many(insert.to_dict('records'))

    except Exception as e:
        print(str(e))
    
    delete=df[df.isnull().any(1)]
    delete.fillna(0,inplace=True)
    returndata  = {
        'total_count':len(df.index),
        'insert_count': len(insert.index),
        'delete_count': len(delete.index),
        'insert_list': insert.to_dict('records'),
        'delete_list': delete.to_dict('records'),
    }
    return returndata
#######################################################################################################
@app.post("/hr/uploadhse")
async def upload_csv(csv_file: UploadFile = None):
    if csv_file is None:
        return {"message": "No file uploaded"}
    contents = await csv_file.read()
    csv_string = contents.decode("utf-8")
    df = pd.read_csv(StringIO(csv_string))
    df['hse_passout'] = df['hse_passout'].astype(str)
    df['hse_marks'] = df['hse_marks'].astype(str)
    df['hse_regno'] = df['hse_regno'].astype(str)
    insert=df[~df.isnull().any(1)]
    insert['status'] = False
    insert['submitted_on'] = datetime.now()
    try:
        client.bgv.hse.insert_many(insert.to_dict('records'))

    except Exception as e:
        print(str(e))
    
    delete=df[df.isnull().any(1)]
    delete.fillna(0,inplace=True)   
    returndata  = {
        'total_count':len(df.index),
        'insert_count': len(insert.index),
        'delete_count': len(delete.index),
        'insert_list': insert.to_dict('records'),
        'delete_list': delete.to_dict('records'),
    }
    return returndata
######################################################################################################
@app.post("/hr/uploadug")
async def upload_csv(csv_file: UploadFile = None):
    if csv_file is None:
        return {"message": "No file uploaded"}
    contents = await csv_file.read()
    csv_string = contents.decode("utf-8")
    df = pd.read_csv(StringIO(csv_string))
    df['ug_regno'] = df['ug_regno'].astype(str)
    df['ug_passout'] = df['ug_passout'].astype(str)
    df['ug_marks'] = df['ug_marks'].astype(str)
    insert=df[~df.isnull().any(1)]
    insert['status'] = False
    insert['submitted_on'] = datetime.now()
    try:
        client.bgv.ug.insert_many(insert.to_dict('records'))

    except Exception as e:
        print(str(e))
    
    delete=df[df.isnull().any(1)]
    delete.fillna(0,inplace=True) 
    returndata  = {
        'total_count':len(df.index),
        'insert_count': len(insert.index),
        'delete_count': len(delete.index),
        'insert_list': insert.to_dict('records'),
        'delete_list': delete.to_dict('records'),
    }
    return returndata    

##########################################################################################################
@app.post("/hr/uploadpg")
async def upload_csv(csv_file: UploadFile = None):
    if csv_file is None:
        return {"message": "No file uploaded"}
    contents = await csv_file.read()
    csv_string = contents.decode("utf-8")
    df = pd.read_csv(StringIO(csv_string))
    df['pg_regno'] = df['pg_regno'].astype(str)
    df['pg_passout'] = df['pg_passout'].astype(str)
    df['pg_marks'] = df['pg_marks'].astype(str)
    insert=df[~df.isnull().any(1)]
    insert['status'] = False
    insert['submitted_on'] = datetime.now()
    try:
        client.bgv.pg.insert_many(insert.to_dict('records'))

    except Exception as e:
        print(str(e))
    
    delete=df[df.isnull().any(1)]
    delete.fillna(0,inplace=True)  
    returndata  = {
        'total_count':len(df.index),
        'insert_count': len(insert.index),
        'delete_count': len(delete.index),
        'insert_list': insert.to_dict('records'),
        'delete_list': delete.to_dict('records'),
    }
    return returndata  

#####################################################################################################
@app.post("/hr/uploadexp")
async def upload_csv(csv_file: UploadFile = None):
    if csv_file is None:
        return {"message": "No file uploaded"}
    contents = await csv_file.read()
    csv_string = contents.decode("utf-8")
    df = pd.read_csv(StringIO(csv_string))
    df['empid'] = df['empid'].astype(str)
    df['lpa'] = df['lpa'].astype(str)
    insert=df[~df.isnull().any(1)]
    insert['status'] = False
    insert['submitted_on'] = datetime.now()
    try:
        client.bgv.exp.insert_many(insert.to_dict('records'))

    except Exception as e:
        print(str(e))
    
    delete=df[df.isnull().any(1)]
    delete.fillna(0,inplace=True)    
    returndata  = {
        'total_count':len(df.index),
        'insert_count': len(insert.index),
        'delete_count': len(delete.index),
        'insert_list': insert.to_dict('records'),
        'delete_list': delete.to_dict('records'),
    }
    return returndata
#######################################################################################################
class SubscriptionType(BaseModel):
    name: str
    price: float

subscription_types = [
    SubscriptionType(name="Basic", price=9.99),
    SubscriptionType(name="Standard", price=19.99),
    SubscriptionType(name="Premium", price=29.99)
]

class UserSubscription(BaseModel):
    email: str
    subscription_type: str

subscriptions = []

@app.get("/subscription_types")
def get_subscription_types():
    return {"subscription_types": subscription_types}

@app.post("/subscribe")
def subscribe(user_subscription: UserSubscription):
    matching_subscription_type = next(
        (st for st in subscription_types if st.name == user_subscription.subscription_type),
        None
    )
    if matching_subscription_type:
        subscriptions.append(user_subscription)
        return {"message": "Subscription added successfully"}
    else:
        return {"message": "Invalid subscription type"}

@app.get("/subscriptions")
def get_subscriptions():
    return {"subscriptions": subscriptions}

@app.get("/subscriptions/{email}")
def get_subscription_by_email(email: str):
    matching_subscriptions = [subscription for subscription in subscriptions if subscription.email == email]
    if matching_subscriptions:
        return {"subscriptions": matching_subscriptions}
    else:
        return {"message": "No subscriptions found for the provided email"}
    
