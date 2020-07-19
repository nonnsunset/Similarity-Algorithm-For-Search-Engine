FROM continuumio/miniconda3

RUN mkdir -p /src/app

WORKDIR /src/app

COPY ./ /src/app

RUN apt-get update && apt-get install -y \
  freetds-dev \
  python-dev 

RUN conda install python
RUN conda install Cython
RUN conda install ipython
RUN conda install pandas
RUN conda install scikit-learn
RUN conda install numpy
RUN conda install flask
RUN conda install pymssql

EXPOSE 8000

# ADD main.py /
# ADD search.py /
# ADD generate_model.py /
# ADD connect_db.py /
# ADD analyst_data.py /
# ADD config_db.py /
# RUN python3 main.py


CMD ["python3", "main.py"]