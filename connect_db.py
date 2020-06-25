import pymssql
import config_db as cf

def search_data() :
    connect = pymssql.connect(host = cf.HOST, port=cf.PORT, database = cf.DBNAME, user = cf.USER, password = cf.PASSWORD)
    cursor = connect.cursor()
    cursor.execute("""...""")
    results = cursor.fetchall()
    data = []
    for row in results:
        data.append(row)
    return data
    
# def data_model () :
#     connect = pymssql.connect(host = cf.HOST, port=cf.PORT, database = cf.DBNAME, user = cf.USER, password = cf.PASSWORD)
#     cursor = connect.cursor()
#     cursor.execute("""...ID""")
#     results = cursor.fetchall()
#     data = []
#     for row in results:
#         data.append(row)
#     return data