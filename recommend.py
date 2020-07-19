from analyst_data import JobTypeID, UserExperience
from search import search_ai
from connect_db import recommendBusinessInfo
import pandas as pd
import json

def FindJobType(JobID) :
    dataset = pd.read_pickle('')
    if(dataset.isin([JobID]).any().any()) :
        data = dataset.loc[dataset['JobPositionID'] == JobID]
        output_position = data.JobTypeID
        output_position = output_position.to_numpy()
        output_position = output_position[0]
        return output_position
    else :
        return 0

def Filtering(UserID, i) :
    uData = UserExperience(UserID)
    JobID, LastSalary, ProvinceID = uData.JobPositionID, uData.LastSalary, uData.ProvinceID
    JobID, LastSalary, ProvinceID = JobID.to_numpy(), LastSalary.to_numpy(), ProvinceID.to_numpy()
    JobID, LastSalary, ProvinceID = JobID[0], LastSalary[0], ProvinceID[0]
    JobType = FindJobType(JobID)
    businessData = recommendBusinessInfo(JobType, LastSalary, ProvinceID)
    recommend = businessData[i]
    salary = recommend[2]
    salary = json.dumps(float(salary))
    recommend = {'Position': recommend[0], 'Salary' : salary, 'Decription' : recommend[1], 'Company' : recommend[3], 'BusinessType' : recommend[4], \
        'Phone' : recommend[5], 'Province' : recommend[6], 'Distinct':recommend[7], 'Email':recommend[8]}
    return recommend

# print(Filtering(145759, 2))