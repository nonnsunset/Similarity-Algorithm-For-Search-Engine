import pandas as pd 
import numpy as np
from connect_db import search_data

# def data_ml():
#     data = data_model()
#     dataset = pd.DataFrame(data, columns=['RequestPositionID', 'JobFieldID', 'ResultID'])
#     return dataset

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
def data_sim() :
    data = search_data()
    dataset = pd.DataFrame(data, columns=['RequestPosition', 'JobPositionID'])
    JobPosition = dataset.RequestPosition
    JobPositionID = dataset.JobPositionID
    J = JobPosition.to_numpy()
    JID = JobPositionID.to_numpy()
    return J, JID