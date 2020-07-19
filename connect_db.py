import pymssql
import pandas as pd
import config_db as cf

def search_data() :
    connect = pymssql.connect(host = cf.HOST, port=cf.PORT, database = cf.DBNAME, user = cf.USER, password = cf.PASSWORD)
    cursor = connect.cursor()
    cursor.execute("""SELECT DISTINCT ejf.RequestPosition, ejf.JobPositionID
    FROM dbo.EmployeeJobField ejf
    WHERE ejf.RequestPosition IS NOT NULL""")
    results = cursor.fetchall()
    data = []
    for row in results:
        data.append(row)
    return data

def JobType() :
    connect = pymssql.connect(host = cf.HOST, port=cf.PORT, database = cf.DBNAME, user = cf.USER, password = cf.PASSWORD)
    cursor = connect.cursor()
    cursor.execute("""SELECT DISTINCT jp.JobPositionID, jp.JobFieldID 
    FROM dbo.JobPosition jp""")
    results = cursor.fetchall()
    data = []
    for row in results:
        data.append(row)
    return data

def recommend(UserID) : 
    connect = pymssql.connect(host = cf.HOST, port=cf.PORT, database = cf.DBNAME, user = cf.USER, password = cf.PASSWORD)
    cursor = connect.cursor()
    cursor.execute("""SELECT DISTINCT  ee.JobPositionID , ee.LastSalary , ee.ProvinceID
    FROM dbo.EmployeeExperience ee 
    WHERE ee.EmployeeID = %s"""%UserID)
    results = cursor.fetchall()
    data = []
    for row in results:
        data.append(row)
    return data

def recommendBusinessInfo(JobType, LastSalary, ProvinceID) :
    connect = pymssql.connect(host = cf.HOST, port=cf.PORT, database = cf.DBNAME, user = cf.USER, password = cf.PASSWORD)
    cursor = connect.cursor()
    cursor.execute("""SELECT TOP 3 ja.JobPosition , ja.JobDescription , ja.Wage_Min , e.EmployerName , bt.BusinessTypeName , e.Telephone , p.ProvinceName , d.DistrictName ,e.Email 
    FROM dbo.JobAnnounce ja
    INNER JOIN dbo.Employer e ON e.EmployerID = ja.EmployerID 
    INNER JOIN dbo.BusinessType bt ON bt.BusinessTypeID = e.BusinessTypeID 
    JOIN dbo.Province p ON p.ProvinceID = e.ProvinceID 
    JOIN dbo.District d ON d.DistrictID = e.DistrictID 
    WHERE ja.Wage_Min > %s AND ja.JobFieldID = %s AND e.ProvinceID = %s
    ORDER BY NEWID()"""%(LastSalary, JobType, ProvinceID))
    results = cursor.fetchall()
    data = []
    for row in results:
        data.append(row)
    return data