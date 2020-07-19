from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import string
import numpy as np
from analyst_data import data_search, JobTypeID
import pandas as pd 



def JobTypeObj():
    dataset = JobTypeID()
    dataset.to_pickle('')


def Sim_model() :
    vectorizer = TfidfVectorizer()

    JobPosition, JobID = data_search()

    vector = vectorizer.fit_transform(JobPosition)
    vector = vector.toarray()
    x = []
    def cosine_sim (vec1, vec2) :
        vec1 = vec1.reshape(1, -1)
        vec2 = vec2.reshape(1, -1)
        return cosine_similarity(vec1, vec2)[0][0]

    for i in range(len(JobPosition)):
        for i2 in range(len(JobPosition)):
            sim = cosine_sim(vector[i], vector[i2])
            sim = '%.6f'%sim
            v = []
            if(i == i2):
                pass
            else:
                if(sim == '0.000000'):
                    pass
                else:
                    v.append(JobPosition[i])
                    v.append(JobPosition[i2])
                    v.append(JobID[i2])
                    # sim = sim * 100
                    v.append(sim)
                    print(v)
                    x.append(v)
    dataset = pd.DataFrame(x, columns=['INPUT', 'OUTPUT','ID', 'Similarity(%)']) ### จะถูกเก็บเป็น OBJ ####
    dataset.to_pickle('')

### Uncomment while you want to generate new similarity model ###

#Sim_model()

### Uncomment while you want to generate new JobType Object ###

#JobTypeObj()
