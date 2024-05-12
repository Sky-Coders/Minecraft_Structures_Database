import pandas as pd
from GenericsFunctions import linkName_textName as linkStructures_textStructures
from GenericsFunctions import dataframe_json

def jsonStructures():
    linkStructures = 'https://minecraft.fandom.com/wiki/Structure'
    
    def linkStructures_dataframeStructures(linkStructures):
      tablesStructures = linkStructures_tablesStructures(linkStructures)
      dataframesStructures = []
      for tableStructures in tablesStructures:
        dataframeTableStructures = tableStructures_dataframeTableStructures(tableStructures)
        dataframesStructures.append(dataframeTableStructures)
      dataframesStructures.append(pd.DataFrame(data=[('ruined_portal','Ruined Portal')],columns=['identifier','name']))
      return pd.concat(dataframesStructures,ignore_index=True)

    def linkStructures_tablesStructures(linkStructures):
        textStructures = linkStructures_textStructures(linkStructures)
        return textStructures.find_all(name='table')[:7]

    def tableStructures_dataframeTableStructures(tableStructures):
      rowsTableStructures = tableStructures_rowsTableStructures(tableStructures)
      dataTableStructures = []
      for rowTableStructure in rowsTableStructures:
        dataRowTableStructure = rowTableStructure_dataRowTableStructure(rowTableStructure)
        if dataRowTableStructure[0] != 'ruined_portal':
          dataTableStructures.append(dataRowTableStructure)
      dataColumnsTableStructures = ['identifier','name']
      return pd.DataFrame(data=dataTableStructures,columns=dataColumnsTableStructures)

    def tableStructures_rowsTableStructures(tableStructures):
      return tableStructures.find_all(name='tr')[1:]

    def rowTableStructure_dataRowTableStructure(rowTableStructure):
      nameStructure = rowTableStructure.find(name='td').text.strip()
      nameStructure = normalize(nameStructure)
      identifierStructure = nameStructure_identifierStructure(nameStructure)
      if 'obsidian_pillar' == identifierStructure:
        identifierStructure = 'end_spike'
      return identifierStructure , nameStructure

    def normalize(nameStructure):
      nameNormalize = ''
      for character in nameStructure:
        if character != '[':
          nameNormalize += character
        else:
          break
      if 'Void' in nameNormalize:
        nameNormalize = 'Void Start Platform'
      return nameNormalize

    def nameStructure_identifierStructure(nameStructure):
      return '_'.join(nameStructure.lower().split())

    dataframeStructures = linkStructures_dataframeStructures(linkStructures)

    dataframe_json([dataframeStructures],['jsonStructures'])

if __name__=='__main__':
    jsonStructures()