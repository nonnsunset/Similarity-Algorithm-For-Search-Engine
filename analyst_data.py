import pandas as pd 
import numpy as np
from connect_db import search_data, JobType, recommend
import json

def data_search() :
    data = search_data()
    dataset = pd.DataFrame(data, columns=['RequestPosition', 'JobPositionID'])
    # dataset = dataset[:2500]
    ## Pre data 2500 data to train model ####

    JobPosition = dataset.RequestPosition
    JobPositionID = dataset.JobPositionID
    J = JobPosition.to_numpy()
    JID = JobPositionID.to_numpy()
    return J, JID

    ##### Function นี้คือ เตรียมข้อมูลเมื่อ ไม่มี ชุด Data Frame ใน Model ####

def JobTypeID() :
    data = JobType()
    dataset = pd.DataFrame(data, columns=['JobPositionID', 'JobTypeID'])
    return dataset

def UserExperience(UserID) :
    data = recommend(UserID)
    dataset = pd.DataFrame(data, columns=['JobPositionID', 'LastSalary','ProvinceID'])
    return dataset