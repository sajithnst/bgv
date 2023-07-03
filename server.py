from fastapi import FastAPI,File , UploadFile,Form
from pydantic import BaseModel
from typing import Dict, Optional
from random import choice
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pymongo import MongoClient
from datetime import datetime
import os
import configparser
from graph import Graph

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
@app.get('/')
async def get():
    return True
######### API related to users #################################################################

class SubmitModel(BaseModel):
    email: str
    status: str='pending'

@app.post('/user/submit')
async def verify(submit:SubmitModel):
    personal = client.bgv.personal.count_documents({'email' : submit.email})
    sslc = client.bgv.sslc.count_documents({'email':submit.email})
    hse = client.bgv.hse.count_documents({'email':submit.email})
    ug = client.bgv.ug.count_documents({'email' : submit.email})
   
    if personal == 0 and sslc == 0 and hse == 0 and ug == 0:
        return False
    else:
        try:
            filter = {
                'email': submit.email,
            }
            update ={
                '$set':{'status': submit.status}
            }
            client.bgv.user.update_one(filter=filter,update=update)
            return True
        except Exception as e:
            print(str(e))



class UserModel(BaseModel):
    name : str
    email : str
    password : str
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

@app.get('/totalprofile')
async def total_user():
    try:

        counts = client.bgv.user.count_documents({})
        return {'counts': counts}
    except Exception as e:
        print(str(e))
        return False


@app.get('/usereducation')
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

@app.get('userexp')
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


@app.post('/emailverified')
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
    submitted_on : str =  datetime.now()
    edited_on : str =  datetime.now()


@app.get('/personal')
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

@app.post('/personal')
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
        'status': "pending",
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
        'status': "pending",
        'submitted_on': data.submitted_on

        }
    }

    try: 
        client.bgv.personal.insert_one(filt, update)
        return True
    except Exception as e:
        print (str(e))
        return False

@app.post('/personal/update')
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
        'status': "pending",
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
    regno : str
    email : str
    marks : int
    school : str
    passout : str
    name : str
    board : str
    status : bool = False
    submitted_on: str= datetime.now()
    edited_on: str=datetime.now()
@app.post('/sslcupdate')
async def update( sslc : SSLC ):
    filt = {
        'email' : sslc.email
    }
    update={
        '$set':{
        'regno': sslc.regno,
        'marks':sslc.marks,
        'school' : sslc.school,
        'passout': sslc.passout,
        'board': sslc.board,
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
    
@app.post('/sslc')
async def sslcinput(sslc : SSLC):
    filt = {
        'email' : sslc.email,
        'regno': sslc.regno,
        'marks':sslc.marks,
        'school' : sslc.school,
        'passout': sslc.passout,
        'board': sslc.board,
        'status': sslc.status,
        'submitted_on': sslc.submitted_on
    }
    update={
        '$set':{
        'regno': sslc.regno,
        'marks':sslc.marks,
        'school' : sslc.school,
        'passout': sslc.passout,
        'board': sslc.board,
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

@app.get('/sslc')
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


### code to upload pdf file 
@app.post('/uploadsslcpdf')
def upload(email : str = Form(), regno : str = Form(),file: UploadFile = File(...)):
    
    path = os.path.join(email,regno+".pdf")
    try:
        contents = file.file.read()
        with open(path, 'wb') as f:
            f.write(contents)
    except Exception:
        return False
    finally:
        file.file.close()

    return True




@app.get('/getpdf')
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
    regno: str
    email : str
    name : str
    marks : int
    passout : str
    school : str
    board : str
    status : bool = False
    submitted_on: str= datetime.now()
    edited_on: str=datetime.now()

@app.post('/hseupdate')
async def update( hse : HSE ):
    filt = {
        'email' : hse.email
    }
    update={
        '$set':{
        'regno': hse.regno,
        'marks':hse.marks,
        'school' : hse.school,
        'passout': hse.passout,
        'board': hse.board,
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

@app.post('/hse')
async def hseinput(hse : HSE):
    filt = {
        'email' : hse.email,
        'regno': hse.regno,
        'marks':hse.marks,
        'school' : hse.school,
        'passout': hse.passout,
        'board': hse.board,
        'status': hse.status,
        'submitted_on': hse.submitted_on
    }
    update={
        '$set':{
        'regno': hse.regno,
        'marks':hse.marks,
        'school' : hse.school,
        'passout': hse.passout,
        'board': hse.board,
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
@app.get('/hse')
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

@app.post('/uploadhsepdf')
def upload(email : str = Form(), regno : str = Form(),file: UploadFile = File(...)):
    
    path = os.path.join(email,regno+".pdf")
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
    regno : str
    email : str
    name : str
    specialization : str
    college : str
    marks : int
    passout : str
    university : str
    status : bool = False
    submitted_on: str= datetime.now()
    edited_on: str=datetime.now()

@app.post('/ugupdate')
async def update( ug : UG ):
    filt = {
        'email' : ug.email
    }
    update={
        '$set':{
        'regno': ug.regno,
        'marks':ug.marks,
        'specialization' : ug.specialization,
        'college': ug.college,
        'passout': ug.passout,
        'university': ug.university,
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

@app.post('/ug')
async def addug(ug: UG):
    filt = {
        'email' : ug.email,
        'regno': ug.regno,
        'marks':ug.marks,
        'specialization' : ug.specialization,
        'college': ug.college,
        'passout': ug.passout,
        'university': ug.university,
        'status': ug.status,
        'submitted_on': ug.submitted_on
    }
    update={
        '$set':{
        'regno': ug.regno,
        'marks':ug.marks,
        'specialization' : ug.specialization,
        'college': ug.college,
        'passout': ug.passout,
        'university': ug.university,
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


@app.get('/ug')
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

@app.post('/uploadugpdf')
def upload(email : str = Form(), regno : str = Form(),file: UploadFile = File(...)):
    
    path = os.path.join(email,regno+".pdf")
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
class PG(BaseModel):
    regno : str
    email : str
    name : str
    specialization : str
    college : str
    marks : int
    passout : str
    university : str
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
        'regno': pg.regno,
        'marks':pg.marks,
        'specialization' : pg.specialization,
        'college': pg.college,
        'passout': pg.passout,
        'university': pg.university,
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
        'regno': pg.regno,
        'marks':pg.marks,
        'specialization' : pg.specialization,
        'college': pg.college,
        'passout': pg.passout,
        'university': pg.university,
        'status': pg.status,
        'submitted_on': pg.submitted_on
    }
    update={
        '$set':{
        'regno': pg.regno,
        'marks':pg.marks,
        'specialization' : pg.specialization,
        'college': pg.college,
        'passout': pg.passout,
        'university': pg.university,
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
def upload(email : str = Form(), regno : str = Form(),file: UploadFile = File(...)):
    
    path = os.path.join(email,regno+".pdf")
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
    company : str
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
        'company':exp.company,
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
        'company':exp.company,
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
        'company':exp.company,
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
async def get_exp(email:str):
    filter = {'email': email}
    project = {
        '_id':0
    }
    try:
        return dict(client.bgv.exp.find_one(filter,project))
    except Exception as e:
        print(str(e))
        return False



@app.post('/uploadexppdf')
def upload(email : str = Form(), empid : str = Form(),file: UploadFile = File(...)):
    
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


@app.get('/exp')
async def exp(email : str ):
    try:
        filter= {
            "email" : email
        }
        project={
            "_id":0
        }
        if client.bgv.exp.count_documents(filter) == 0:
            return None
        return dict(client.bgv.exp.find(filter,project))
    except Exception as e:
        print(str(e))
        return False
 
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
    password : str| None=None
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
    password :str

@app.post("/hrlogin")
async def hrlogin(login : HRLogin):
    filter = dict(login)
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
    regno: Optional[str] = None
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
            'regno': verify.regno
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
            'regno': verify.regno
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
            'regno': verify.regno
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
    except Exception as e:
        print(str(e))
        return False

@app.post('/verify/pg')
async def verifypg(verify: Verify):
    try :
        filter = {
            'email' : verify.user_email,
            'regno': verify.regno
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
            'regno': verify.regno
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



@app.get('/user/firstlogin')
async def firstlogin(email:str):
    filter ={
        'email': email
        }
    update = {
        '$set': { 'firstlogin': False}
    }
    try:
        client.bgv.user.update_one(filter,update)
        return True
    except Exception as e:
        print(str(e))
        return False

@app.get('/user/qrcode')
async def get_user_qr(email :str):
    filter ={
        'email': email,
        'status' : 'verified'
        }
    if client.bgv.user.count_documents(filter) == 1:
        return True
    else : return False



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
    company_mail:str|None=None
    email:str|None=None
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
class Inprogress(BaseModel):
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
        client.bgv.personal.find_one_and_update(filter,update)
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
        client.bgv.sslc.find_one_and_update(filter,update)
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
        client.bgv.hse.find_one_and_update(filter,update)
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
        client.bgv.ug.find_one_and_update(filter,update)
        return True
    except Exception as e:
        print(str(e))
        return False