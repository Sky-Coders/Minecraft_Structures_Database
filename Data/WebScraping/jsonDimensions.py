import pandas as pd
from GenericsFunctions import dataframe_json

def jsonDimensions():
    dataDimensions = [('overworld',0,'Overworld'),('the_nether',-1,'Nether'),('the_end',1,'The End')]
    dataColumnsDimension = ['identifier','numeric_id','name']
    dataframeDimensions = pd.DataFrame(data=dataDimensions, columns=dataColumnsDimension)
    dataframe_json([dataframeDimensions],['jsonDimensions'])

if __name__=='__main__':
    jsonDimensions()