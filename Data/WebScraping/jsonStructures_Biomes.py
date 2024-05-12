import pandas as pd
from GenericsFunctions import linkName_textName as linkStructures_textStructuresBiomes
from GenericsFunctions import dataframe_json

def jsonStructures_Biomes():
    linkStructuresBiomes = 'https://minecraft.fandom.com/wiki/Structure'
    
    dataframeOverworldBiomes = pd.read_json('../dataJSON/_jsonBiomesOverworld.json')
    dataframeNetherBiomes = pd.read_json('../dataJSON/_jsonBiomesNether.json')
    dataframeEndBiomes = pd.read_json('../dataJSON/_jsonBiomesEnd.json')

    def linkStructures_dataframeStructuresBiomes(linkStructuresBiomes):
      tablesStructuresBiomes = linkStructures_tablesStructuresBiomes(linkStructuresBiomes)
      dataframeStructuresBiomes = []
      for tableStructuresBiomes in tablesStructuresBiomes:
        dataStructuresBiomes = tableStructuresBiomes_dataStructuresBiomes(tableStructuresBiomes)
        dataframeStructuresBiomes.extend(dataStructuresBiomes)
      dataColumnsStructuresBiomes = ['structure_identifier','biome_identifier']
      return pd.DataFrame(data=dataframeStructuresBiomes,columns=dataColumnsStructuresBiomes)
    
    def linkStructures_tablesStructuresBiomes(linkStructuresBiomes):
      textStructuresBiomes = linkStructures_textStructuresBiomes(linkStructuresBiomes)
      return textStructuresBiomes.find_all(name='table')[:7]

    def tableStructuresBiomes_dataStructuresBiomes(tableStructuresBiomes):
      rowsStructuresBiomes = tableStructuresBiomes_rowsStructuresBiomes(tableStructuresBiomes)
      dataStructuresBiomes = []
      for rowStructureBiomes in rowsStructuresBiomes:
        dataStructureBiomes = rowStructureBiomes_dataStructureBiomes(rowStructureBiomes)
        dataStructuresBiomes.extend(dataStructureBiomes)
      return dataStructuresBiomes

    def tableStructuresBiomes_rowsStructuresBiomes(tableStructuresBiomes):
      return tableStructuresBiomes.find_all(name='tr')[1:]

    def rowStructureBiomes_dataStructureBiomes(rowStructureBiomes):
      fieldNameStructure , fieldBiomesStructure = rowStructureBiomes_fieldsStructureBiomes(rowStructureBiomes)
      identifierStructure = fieldNameStructure_identifierStructure(fieldNameStructure)
      listBiomesStructure = fieldBiomesStructure_listBiomesStructure(fieldBiomesStructure)
      dataStructureBiomes = [(identifierStructure,BiomeStructure) for BiomeStructure in listBiomesStructure]
      return dataStructureBiomes

    def rowStructureBiomes_fieldsStructureBiomes(rowStructureBiomes):
      return rowStructureBiomes.find_all(name='td')[:2]

    def fieldNameStructure_identifierStructure(fieldNameStructure):
      nameStructure = fieldNameStructure.find(name='a')['title'].lower()
      wordsNameStructure = nameStructure.split()
      if 'Abandoned' in fieldNameStructure.find(name='a')['href']:
        wordsNameStructure = ['abandoned'] + wordsNameStructure
      return '_'.join(wordsNameStructure)

    def fieldBiomesStructure_listBiomesStructure(fieldBiomesStructure):
      listBiomesStructure = []
      listNamesBiomeStructure = fieldBiomesStructure.find_all(name='li')
      if listNamesBiomeStructure:
        for nameBiomeStructure in listNamesBiomeStructure:
          nameBiome = nameBiomeStructure.find(name='a')['title'].lower()
          wordsNameBiome = nameBiome.split()
          if '(' in wordsNameBiome[-1]:
            listBiomesStructure.append('_'.join(wordsNameBiome[:-1]))
          else:
            listBiomesStructure.append('_'.join(wordsNameBiome))
      else:
        contentFieldBiomesStructure = fieldBiomesStructure.text
        if 'Overworld' in contentFieldBiomesStructure or 'Anywhere' in contentFieldBiomesStructure:
          listBiomesStructure.extend(dataframeOverworldBiomes['identifier'])
        if 'Nether' in contentFieldBiomesStructure:
          listBiomesStructure.extend(dataframeNetherBiomes['identifier'])
        if 'End' in contentFieldBiomesStructure:
          listBiomesStructure.extend(dataframeEndBiomes['identifier'])
      return listBiomesStructure

    dataframeStructuresBiomes = linkStructures_dataframeStructuresBiomes(linkStructuresBiomes)

    dataframe_json([dataframeStructuresBiomes],['jsonStructures_Biomes'])
    

if __name__=='__main__':
    jsonStructures_Biomes()