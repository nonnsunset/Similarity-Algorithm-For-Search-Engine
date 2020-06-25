from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import string
import numpy as np
from analyst_data import data_search, data_sim
import pandas as pd 

vectorizer = TfidfVectorizer()
def search(input_data) : ### Function For similarity while model doesn't have Input_data ####
    RequestPosition, JobPositionID = data_sim()
    info = RequestPosition
    similar = [input_data]
    for i in info:
        similar.append(i)
    vector = vectorizer.fit_transform(similar)
    vector = vector.toarray()
    v = []
    def cosine_sim (vec1, vec2) :
        vec1 = vec1.reshape(1, -1)
        vec2 = vec2.reshape(1, -1)
        return cosine_similarity(vec1, vec2)[0][0]
    for i in range(len(similar)):
        x = cosine_sim(vector[0], vector[i])
        v.append(x)
    r = v[1:]
    percentage = max(r)
    index = np.argmax(r)
    JobPosition = RequestPosition[index]
    JobPositionID = JobPositionID[index]
    dataset = pd.read_pickle('Path')
    search_input = [[input_data, JobPosition, JobPositionID, percentage]]
    search_df = pd.DataFrame(search_input, columns=['INPUT', 'OUTPUT','ID', 'Similarity(%)'])
    data = dataset.append(search_df, ignore_index=True)
    print(data)
    data.to_pickle('Path')
    return JobPosition, JobPositionID, percentage

def search_ai(input_data): #### Function Of Model, It use to get PositionID and Similarity Precentage #### 
    dataset = pd.read_pickle('Path')
    print(dataset)
    if(dataset.isin([input_data]).any().any()):
        data = dataset.loc[dataset['INPUT'] == input_data]
        output_position = data.OUTPUT
        output_ID = data.ID
        output_sim = data['Similarity(%)']
        output_position = output_position.to_numpy()
        output_ID = output_ID.to_numpy()
        output_sim = output_sim.to_numpy()
        percent = max(output_sim)
        index = np.argmax(output_sim)
        output = output_position[index]
        ID = output_ID[index]
        return output ,ID ,percent
    else:
        return search(input_data)
