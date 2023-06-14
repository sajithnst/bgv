from fastapi import FastAPI,File , UploadFile,Form
from pydantic import BaseModel
from typing import Dict
from random import choice
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pymongo import MongoClient
import datetime
import os
import configparser
from graph import Graph

client = MongoClient('mongodb://localhost:27017/')



##############Graph API interface #############################################################
config = configparser.ConfigParser()
config.read(['config.cfg', 'config.dev.cfg'])
azure_settings = config['azure']
graph: Graph = Graph(azure_settings)
# For testing the working of the  graph api integration
def greet_user(graph: Graph):
    user = graph.get_user()
    print('Hello,', user['displayName'])
    # For Work/school accounts, email is in mail property
    # Personal accounts, email is in userPrincipalName
    print('Email:', user['mail'] or user['userPrincipalName'], '\n')
greet_user(graph)

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
@app.get('/otp')
async def otp(email: str):
    number =['0','1','2','3','4','5','6','7','8','9']
    otp =''
    for i in range(6):
        otp+=choice(number)

    subject = "OTP for New Account Created"
    msg = f" Hi \n The OTP your email verification is {otp} in the verifychain application\n\n "
    graph.send_mail(subject,msg,email)
    return otp

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

@app.post('/userupdate')
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
        }
    }

    try: 
        client.bgv.user.find_one_and_update(filt, update)
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

@app.post('/sslc')
async def sslcinput(sslc : SSLC):
    filter = {
        'regno': sslc.regno,
        'email': sslc.email,
    }
    if client.bgv.sslc.count_documents(filter) == 0:
        try:
            client.bgv.sslc.insert_one(dict(sslc))
            return True
        except Exception as e:
            print (str(e))
    else: return False

@app.get('/sslc')
async def get_sslc(email: str):
    filter = {'email': email}
    project = { '_id':0}
    try:
        return client.bgv.sslc.find_one(filter,project)
    except Exception  as e:
        print(str(e))
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

@app.post('/hse')
async def hseinput(hse : HSE):
    filter = {
        'email': hse.email,
        'regno': hse.regno,
    }
    if client.bgv.hse.count_documents(filter) == 0:
        try:
            client.bgv.hse.insert_one(dict(hse))
            return True
        except Exception as e:
            print (str(e))
    else: 
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

@app.post('/ug')
async def addug(ug: UG):
    filter= {
        'email': ug.email,
        'regno': ug.regno,
    }
    if client.bgv.ug.count_documents(filter) == 0:
        try:
            client.bgv.ug.insert_one(dict(ug))
            return True
        except Exception as e:
            print(str(e))
    else: return False


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

@app.post('/pg')
async def addpg(pg: PG):
    filter= {
        'email': pg.email,
        'regno': pg.regno,
    }
    if client.bgv.pg.count_documents(filter) == 0:
        try:
            client.bgv.pg.insert_one(dict(pg))
            return True
        except Exception as e:
            print(str(e))
    else: return False


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

#### API to add experience  #########################

@app.post('/exp')
async def add_exp(exp :Experience):
    filter = {
        'email': exp.email,
        'empid': exp.empid,
    }
    if client.bgv.exp.count_documents(filter) == 0: 
        try :
             client.bgv.exp.insert_one(dict(exp))
             filter2= {
                'email' : exp.email
             }
             update = {
                '$set' : { 'firstlogin' : False}
             }
             client.bgv.user.find_one_and_update(filter2,update)
             return True
        except Exception as e:
            print(str(e))
    else : return False

@app.get('/exp')
async def get_exp(email:str):
    filter = {
        'email':email
    }
    project ={
        '_id':0
    }
    try:

        if client.bgv.exp.count_documents(filter) == 0:
            return None
        return list(client.bgv.exp.find(filter,project))
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
    empid :str
    company_mail : str
    password : str
    firstlogin: bool

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

class NLogin(BaseModel):
    email : str
    password : str
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
        return {'status': False, 'user' : 'Check login creadentials'}

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
        'firstlogin':{'$ne':True},
    }
    project ={
        '_id':0,
        }
    try:
        return list(client.bgv.user.find(filter,project))
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
        return list(client.bgv.user.find(filter,project))
    except Exception as e:
        print(str(e))
        return False



class Verify(BaseModel):
    user_email : str
    regno: str| None = None
    notary_email: str
    notary_name :str
    status : str = "verified"
@app.post('/verify/personal')
async def verify(verify:Verify):
    sslc = client.bgv.sslc.count_documents({'email':verify.user_email,'status':False})
    hse = client.bgv.hse.count_documents({'email':verify.user_email,'status':False})
    ug = client.bgv.ug.count_documents({'email' : verify.user_email, 'status' : False})
    if sslc+hse+ug == 0:
        try:
        
            filter = {
                'email': verify.user_email,
            }
            update ={
                '$set':{ 'status': verify.status, 'notary_email': verify.notary_email, 'notary_name':verify.notary_name}
            }
            client.bgv.user.update_one(filter=filter,update=update)
            return True
        except Exception as e:
            print(str(e))
    else:
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




   