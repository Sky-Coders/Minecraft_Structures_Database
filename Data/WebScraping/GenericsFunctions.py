from bs4 import BeautifulSoup
import requests

def linkName_textName(linkName):
    htmlName = requests.get(linkName).text
    return BeautifulSoup(htmlName,'html.parser')

def dataframe_json(daframesPandas,dataframeNames):
    for daframePandas , dataframeName in zip(daframesPandas,dataframeNames):
        daframePandas.to_json('../dataJSON/'+dataframeName+'.json')