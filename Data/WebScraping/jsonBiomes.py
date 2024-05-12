import pandas as pd
from bs4 import BeautifulSoup
from GenericsFunctions import linkName_textName as linkBiome_textBiome
from GenericsFunctions import dataframe_json

def jsonBiomes():
    linksOverworld = [
        (9, 'https://minecraft.fandom.com/wiki/Ocean'),
        (1, 'https://minecraft.fandom.com/wiki/Mushroom_Fields'),
        (1, 'https://minecraft.fandom.com/wiki/Meadow'),
        (1, 'https://minecraft.fandom.com/wiki/Cherry_Grove'),
        (5, 'https://minecraft.fandom.com/wiki/Mountains'),
        (3, 'https://minecraft.fandom.com/wiki/Windswept_Hills'),
        (2, 'https://minecraft.fandom.com/wiki/Forest'),
        (1, 'https://minecraft.fandom.com/wiki/Taiga'),
        (2, 'https://minecraft.fandom.com/wiki/Old_Growth_Taiga'),
        (1, 'https://minecraft.fandom.com/wiki/Snowy_Taiga'),
        (2, 'https://minecraft.fandom.com/wiki/Birch_Forest'),
        (1, 'https://minecraft.fandom.com/wiki/Dark_Forest'),
        (3, 'https://minecraft.fandom.com/wiki/Jungle'),
        (2, 'https://minecraft.fandom.com/wiki/River'),
        (2, 'https://minecraft.fandom.com/wiki/Swamp'),
        (3, 'https://minecraft.fandom.com/wiki/Beach'),
        (2, 'https://minecraft.fandom.com/wiki/Plains'),
        (2, 'https://minecraft.fandom.com/wiki/Snowy_Plains'),
        (1, 'https://minecraft.fandom.com/wiki/Desert'),
        (3, 'https://minecraft.fandom.com/wiki/Savanna'),
        (3, 'https://minecraft.fandom.com/wiki/Badlands'),
        (1, 'https://minecraft.fandom.com/wiki/Deep_Dark'),
        (1, 'https://minecraft.fandom.com/wiki/Dripstone_Caves'),
        (1, 'https://minecraft.fandom.com/wiki/Lush_Caves'),
        (1, 'https://minecraft.fandom.com/wiki/The_Void')
        ]

    linksNether = [
        (1, 'https://minecraft.fandom.com/wiki/Nether_Wastes'),
        (1, 'https://minecraft.fandom.com/wiki/Soul_Sand_Valley'),
        (1, 'https://minecraft.fandom.com/wiki/Crimson_Forest'),
        (1, 'https://minecraft.fandom.com/wiki/Warped_Forest'),
        (1, 'https://minecraft.fandom.com/wiki/Basalt_Deltas')
        ]

    linksTheEnd = [
        (5, 'https://minecraft.fandom.com/wiki/The_End_(biome)')
        ]

    linkBiomeIDs = 'https://minecraft.wiki/w/Biome'

    def linksBiomeDimension_dataframeBiomesDimensions(linksDimension,Dimension):
      dataframeBiomeDimensionIDs = linksBiomeDimension_dataframeBiomeDimensionIDs(linksDimension)
      lenRecords = len(dataframeBiomeDimensionIDs)
      dataframeBiomeDimensionIDs['dimension.identifier'] = pd.DataFrame(data=[(Dimension)]*lenRecords,columns=['dimension.identifier'])
      return dataframeBiomeDimensionIDs

    def linksBiomeDimension_dataframeBiomeDimensionIDs(linksDimension):
      dataframeBiomesIDs = linkBiomeIDs_dataframeBiomesIDs(linkBiomeIDs)
      dataframeBiomeDimension = linksBiomeDimension_dataframeBiomeDimension(linksDimension)
      return dataframeBiomesIDs.merge(right=dataframeBiomeDimension,how='right',on='name')

    def linksBiomeDimension_dataframeBiomeDimension(linksDimension):
      dataframesBiomes = []
      for amountBiome , linkBiome in linksDimension:
        dataframeBiomes = linkBiome_dataframeBiome(amountBiome,linkBiome)
        dataframesBiomes.append(dataframeBiomes)
      return pd.concat(dataframesBiomes,ignore_index=True)

    def linkBiome_dataframeBiome(amountBiome,linkBiome):
      tablesBiome = linkBiome_tablesBiome(amountBiome,linkBiome)
      dataframesBiome = []
      for tableBiome in tablesBiome:
        dataColumnsBiomesDimension = ['name', 'temperature', 'precipitation', 'grass color', 'foliage color', 'water color']
        dataBiome = tableBiome_dataBiome(tableBiome)
        dataframeBiome = pd.DataFrame(data=[dataBiome],columns=dataColumnsBiomesDimension)
        dataframesBiome.append(dataframeBiome)
      dataframeBiomes = pd.concat(dataframesBiome,ignore_index=True)
      return dataframeBiomes

    def linkBiome_tablesBiome(amountBiome,linkBiome):
      textBiome = linkBiome_textBiome(linkBiome)
      return textBiome.find_all(name='aside')[:amountBiome]

    def tableBiome_dataBiome(tableBiome):
      nameBiome = tableBiome_nameBiome(tableBiome)
      temperatureBiome = tableBiome_temperatureBiome(tableBiome)
      precipitationBiome = tableBiome_precipitationBiome(tableBiome)
      grassBiome , foliageBiome , waterBiome = tableBiome_colorsBiome(tableBiome)
      return nameBiome , temperatureBiome , precipitationBiome , grassBiome , foliageBiome , waterBiome

    def tableBiome_nameBiome(tableBiome):
      nameBiome = tableBiome.find(name='h2').text.strip().title()
      if 'Waste' in nameBiome:
        return 'Nether Wastes'
      elif 'Void' in nameBiome:
        return 'The Void'
      else:
        return nameBiome

    def tableBiome_temperatureBiome(tableBiome):
      sectionClimateBiome = tableBiome.find_all(name='section')[0]
      return temperatureBiome_temperatureBiome(sectionClimateBiome.find_all(name='div')[1].text)

    def temperatureBiome_temperatureBiome(temperature):
      tmp = ''
      for char in temperature:
        if char in '-0123456789.':
          tmp += char
        else:
          break
      return tmp

    def tableBiome_precipitationBiome(tableBiome):
      sectionClimateBiome = tableBiome.find_all(name='section')[0]
      return sectionClimateBiome.find_all(name='div')[5].text

    def tableBiome_colorsBiome(tableBiome):
      sectionColorsBiome = tableBiome.find_all(name='section')[1]
      divColorsBiome = sectionColorsBiome.find_all(name='div',class_='pi-item pi-data pi-item-spacing pi-border-color')
      for divColor in divColorsBiome:
        nameColor = divColor.find(name='h3').text
        if nameColor=='Grass color':
          grassBiome = divColor.find(name='span').text.split()[0]
        elif nameColor=='Foliage color':
          foliageBiome = divColor.find(name='span').text.split()[0]
        elif nameColor=='Water color':
          waterBiome = divColor.find(name='span').text.split()[0]
      return grassBiome , foliageBiome , waterBiome

    def linkBiomeIDs_dataframeBiomesIDs(linkBiomeIDs):
      tableBiomeIDs = linkBiomeIDs_tableBiomeIDS(linkBiomeIDs)
      rowsBiomesIDs = tableBiomeIDs_rowsBiomesIDs(tableBiomeIDs)
      dataBiomesIDs = []
      for rowBiomeID in rowsBiomesIDs:
        dataBiomeID = rowBiomeID_dataBiomeID(rowBiomeID)
        dataBiomesIDs.append(dataBiomeID)
      dataColumnsBiomeIDs = ['identifier','numeric id','name']
      return pd.DataFrame(data=dataBiomesIDs,columns=dataColumnsBiomeIDs)

    def linkBiomeIDs_tableBiomeIDS(linkBiomeIDs):
      textBiomeIDs = linkBiome_textBiome(linkBiomeIDs)
      return textBiomeIDs.find_all(name='table')[-19]

    def tableBiomeIDs_rowsBiomesIDs(tableBiomeIDs):
      return tableBiomeIDs.find_all(name='tr')[1:]

    def rowBiomeID_dataBiomeID(rowBiomeID):
      _ , rowIdentifierBiome , rowNumericIDBiome = rowBiomeID.find_all(name='td')
      return rowIdentifierBiome_dataIdentifierBiome(rowIdentifierBiome) , rowNumericIDBiome_dataNumericIDBiome(rowNumericIDBiome) , rowNameBiome_dataNamebiome(rowIdentifierBiome)

    def rowNameBiome_dataNamebiome(rowIdentifierBiome):
      nameWords = rowIdentifierBiome_dataIdentifierBiome(rowIdentifierBiome).split('_')
      nameWords = [nameWord.capitalize() for nameWord in nameWords]
      return ' '.join(nameWords)

    def rowIdentifierBiome_dataIdentifierBiome(rowIdentifierBiome):
      return rowIdentifierBiome.find(name='code').text.split()[0]

    def rowNumericIDBiome_dataNumericIDBiome(rowNumericIDBiome):
      return rowNumericIDBiome.text.split()[0]

    dataframeOverworldBiomes = linksBiomeDimension_dataframeBiomesDimensions(linksOverworld,'overworld')
    dataframeNetherBiomes = linksBiomeDimension_dataframeBiomesDimensions(linksNether,'the_nether')
    dataframeEndBiomes = linksBiomeDimension_dataframeBiomesDimensions(linksTheEnd,'the_end')
    dataframeBiomes = pd.concat([dataframeOverworldBiomes,dataframeNetherBiomes,dataframeEndBiomes],ignore_index=True)

    dataframe_json([dataframeBiomes],['jsonBiomes'])

if __name__=='__main__':
    jsonBiomes()