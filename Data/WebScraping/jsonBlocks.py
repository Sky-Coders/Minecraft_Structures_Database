import pandas as pd
from GenericsFunctions import linkName_textName
from GenericsFunctions import dataframe_json

def jsonBlocks():
    linksAsideStructuresBlocks = ['https://minecraft.wiki/w/Mineshaft','https://minecraft.wiki/w/Buried_Treasure',
                                  'https://minecraft.wiki/w/Trail_Ruins','https://minecraft.wiki/w/Desert_Pyramid',
                                  'https://minecraft.wiki/w/Igloo','https://minecraft.wiki/w/Jungle_Pyramid',
                                  'https://minecraft.wiki/w/Pillager_Outpost','https://minecraft.wiki/w/Swamp_Hut',
                                  'https://minecraft.wiki/w/Village','https://minecraft.wiki/w/Village#Abandoned_villages',
                                  'https://minecraft.wiki/w/Woodland_Mansion','https://minecraft.wiki/w/Ocean_Ruins',
                                  'https://minecraft.wiki/w/Shipwreck','https://minecraft.wiki/w/Ocean_Monument',
                                  'https://minecraft.wiki/w/Nether_Fossil','https://minecraft.wiki/w/End_City',
                                  'https://minecraft.wiki/w/Monster_Room','https://minecraft.wiki/w/Desert_Well',
                                  'https://minecraft.wiki/w/Bonus_Chest','https://minecraft.wiki/w/Pile',
                                  'https://minecraft.wiki/w/Coral_Reef','https://minecraft.wiki/w/Forest_rock',
                                  'https://minecraft.wiki/w/Disk','https://minecraft.wiki/w/Geode',
                                  'https://minecraft.wiki/w/Fossil','https://minecraft.wiki/w/Ice_spike',
                                  'https://minecraft.wiki/w/Ice_Patch','https://minecraft.wiki/w/Iceberg_(feature)',
                                  'https://minecraft.wiki/w/Exit_portal','https://minecraft.wiki/w/End_gateway',
                                  'https://minecraft.wiki/w/End_spike','https://minecraft.wiki/w/Obsidian_platform',
                                  'https://minecraft.wiki/w/Void_start_platform']
    mobsAsideStructuresBlocks = [0,0,0,0,2,0,3,0,1,1,3,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    linksSectionStructuresBlocks = ['https://minecraft.wiki/w/Ancient_City','https://minecraft.wiki/w/Stronghold',
                                    'https://minecraft.wiki/w/Ruined_Portal','https://minecraft.wiki/w/Nether_Fortress']
    tableSectionStructuresBlocks = [6,1,2,1]

    linksSectionDivStructuresBlocks = ('https://minecraft.wiki/w/Bastion_Remnant',36)

    def linksStructuresBlocks_dataframeStructuresBlocks(linksAsideStructuresBlocks,mobsAsideStructuresBlocks,linksSectionStructuresBlocks,tableSectionStructuresBlocks,linksSectionDivStructuresBlocks):
      dataframeBlocks = dict()
      dataframeAsideStructuresBlocks = linksAside_dataframeAsideStructuresBlocks(linksAsideStructuresBlocks,mobsAsideStructuresBlocks,dataframeBlocks)
      dataframeSectionStructuresBlocks = linksSection_dataframeSectionStructuresBlocks(linksSectionStructuresBlocks,tableSectionStructuresBlocks,dataframeBlocks)
      dataframeSectionDivStructuresBlocks = linksSectionDiv_dataframeSectionDivStructuresBlocks(linksSectionDivStructuresBlocks,dataframeBlocks)
      dataframeStructuresBlocks = dataframeAsideStructuresBlocks+dataframeSectionStructuresBlocks+dataframeSectionDivStructuresBlocks
      dataBlocks = dataframeBlocks_dataBlocks(dataframeBlocks)
      dataColumnsStructuresBlocks = ['structure_identifier','block_identifier']
      dataColumnsBlocks = ['identifier','name','blast_resistance','hardness','luminosity','transparency']
      return pd.DataFrame(data=dataframeStructuresBlocks,columns=dataColumnsStructuresBlocks) , pd.DataFrame(data=dataBlocks,columns=dataColumnsBlocks)

    def linksAside_dataframeAsideStructuresBlocks(linksAsideStructuresBlocks,mobsAsideStructuresBlocks,dataframeBlocks):
      dataframeAsideStructuresBlocks = []
      for linkStructureBlocks , mobsAsideIndex in zip(linksAsideStructuresBlocks,mobsAsideStructuresBlocks):
        tableStructureBlocks = linkStructureBlocks_tableStructureBlocks_Aside(linkStructureBlocks,mobsAsideIndex)
        identifierStructure = linkStructureBlocks_identifierStructure(linkStructureBlocks)
        dataAsideStructureBlocks = tableStructureBlocks_dataStructureBlocks(tableStructureBlocks,identifierStructure,dataframeBlocks)
        dataframeAsideStructuresBlocks.extend(dataAsideStructureBlocks)
      return dataframeAsideStructuresBlocks

    def linksSection_dataframeSectionStructuresBlocks(linksSectionStructuresBlocks,tableSectionStructuresBlocks,dataframeBlocks):
      dataframeSectionStructuresBlocks = []
      for linkStructureBlocks , tableSectionIndex in zip(linksSectionStructuresBlocks,tableSectionStructuresBlocks):
        tableStructureBlocks = linkStructureBlocks_tableStructureBlocks_Section(linkStructureBlocks,tableSectionIndex)
        identifierStructure = linkStructureBlocks_identifierStructure(linkStructureBlocks)
        dataSectionStructureBlocks = tableStructureBlocks_dataStructureBlocks(tableStructureBlocks,identifierStructure,dataframeBlocks,True)
        dataframeSectionStructuresBlocks.extend(dataSectionStructureBlocks)
      return dataframeSectionStructuresBlocks

    def linksSectionDiv_dataframeSectionDivStructuresBlocks(linksSectionDivStructuresBlocks,dataframeBlocks):
      linkStructureBlocks , tableDivIndex = linksSectionDivStructuresBlocks
      tableStructureBlocks = linkStructureBlocks_tableStructureBlocks_Div(linkStructureBlocks,tableDivIndex)
      identifierStructure = linkStructureBlocks_identifierStructure(linkStructureBlocks)
      dataframeDivStructureBlocks = tableStructureBlocks_dataStructureBlocks(tableStructureBlocks,identifierStructure,dataframeBlocks)
      return dataframeDivStructureBlocks

    def dataframeBlocks_dataBlocks(dataframeBlocks):
      dataBlocks = []
      for identifierBlock , linkBlock in dataframeBlocks.items():
        if linkBlock in ['https://minecraft.wiki/w/Slab','https://minecraft.wiki/w/Button','https://minecraft.wiki/w/Stairs','https://minecraft.wiki/w/Java_Edition','https://minecraft.wiki/w/Wall','https://minecraft.wiki/w/Block','https://minecraft.wiki/w/Fence']: continue
        tableBlock =  linkBlock_tableBlock(linkBlock)
        dataNameBlock = identifierBlock_dataNameBlock(identifierBlock)
        dataBlastResistanceBlokc , dataHardnessBlokc , dataLuminousBlokc , dataTransparentBlokc = tableBlock_dataBlock(tableBlock)
        dataBlocks.append((identifierBlock,dataNameBlock,dataBlastResistanceBlokc,dataHardnessBlokc,dataLuminousBlokc,dataTransparentBlokc))
      return dataBlocks

    def linkStructureBlocks_tableStructureBlocks_Aside(linkStructureBlocks,mobsAsideIndex):
      textStructureBlocks = linkName_textName(linkStructureBlocks)
      tableStructureBlocks = textStructureBlocks_tableStructureBlocks(textStructureBlocks)
      itemsStructureBlocks = tableStructureBlocks.find_all(name='li')
      return itemsStructureBlocks if mobsAsideIndex == 0 else itemsStructureBlocks[:-mobsAsideIndex]

    def linkStructureBlocks_tableStructureBlocks_Section(linkStructureBlocks,tableSectionIndex):
      textStructureBlocks = linkName_textName(linkStructureBlocks)
      tableStructureBlocks = textStructureBlocks.find_all(name='table')[tableSectionIndex]
      return tableStructureBlocks.find_all(name='a')[1::2]

    def linkStructureBlocks_tableStructureBlocks_Div(linkStructureBlocks,tableDivIndex):
      textStructureBlocks = linkName_textName(linkStructureBlocks)
      tableStructureBlocks = textStructureBlocks.find_all(name='div')[tableDivIndex]
      return tableStructureBlocks.find_all(name='li')

    def linkBlock_tableBlock(linkBlock):
      textBlock = linkName_textName(linkBlock)
      return textBlock.find(name='table').find_all(name='tr')

    def textStructureBlocks_tableStructureBlocks(textStructureBlocks):
      tableStructureBlocks = textStructureBlocks.find(name='table')
      for rowStructureBlocks in tableStructureBlocks.find_all(name='tr'):
        if rowStructureBlocks.find(name='th').text.strip() == 'Consists of':
          return rowStructureBlocks

    def linkStructureBlocks_identifierStructure(linkStructureBlocks):
      identifierStructure = ''
      acceptFlag = True
      for charLinkStructureBlocks in linkStructureBlocks[::-1]:
        if charLinkStructureBlocks != '/':
          if charLinkStructureBlocks == ')' or charLinkStructureBlocks == '(':
            acceptFlag = not acceptFlag
          if acceptFlag:
            identifierStructure += charLinkStructureBlocks
        else:
          break
      return identifierStructure[::-1].lower()

    def identifierBlock_dataNameBlock(identifierBlock):
      wordsNameBlock = identifierBlock.capitalize().split('_')
      return ' '.join(wordsNameBlock)

    def tableStructureBlocks_dataStructureBlocks(tableStructureBlocks,identifierStructure,dataframeBlocks,flagIsATag=False):
      dataStructureBlocks = []
      for itemStructureBlock in tableStructureBlocks:
        if ('For more information' in itemStructureBlock.text) or ('Terrain-generated' in itemStructureBlock.text): continue
        if flagIsATag:
          linkStructureBlock = itemStructureBlock['href']
        else:
          if len(anchorStructureBlock:=itemStructureBlock.find_all(name='a'))>1:
            linkStructureBlock =  anchorStructureBlock[1]['href']
          else:
            linkStructureBlock =  anchorStructureBlock[0]['href']
        identifierStructureBlock = linkStructureBlock_identifierStructureBlock(linkStructureBlock)
        dataStructureBlocks.append((identifierStructure,identifierStructureBlock))
        dataframeBlocks.update({identifierStructureBlock:'https://minecraft.wiki'+linkStructureBlock})
      return dataStructureBlocks

    def tableBlock_dataBlock(tableBlock):
      dataBlastResistanceBlokc , dataHardnessBlokc , dataLuminousBlokc , dataTransparentBlokc = [None]*4
      for tableRow in tableBlock:
        tableData , tableValue = tableRow.find(name='th').text.strip() , tableRow.find(name='td').text.strip()
        if tableData == 'Blast resistance' or tableData == 'Blast Resistance':
          dataBlastResistanceBlokc = tableValue
        elif tableData == 'Hardness' or tableData == 'hardness':
          dataHardnessBlokc = tableValue
        elif tableData == 'Luminous' or tableData == 'luminous':
          dataLuminousBlokc = 'Yes' if tableValue[0] == 'Y' or tableValue[0] == 'y' else 'No'
        elif tableData == 'Transparent' or tableData == 'transparent':
          if tableValue[0] == 'Y' or tableValue[0] == 'y':
            dataTransparentBlokc = 'Yes'
          elif tableValue[0] == 'N' or tableValue[0] == 'n':
            dataTransparentBlokc = 'No'
          else:
            dataTransparentBlokc = 'Partial'
        if all([dataBlastResistanceBlokc,dataHardnessBlokc,dataLuminousBlokc,dataTransparentBlokc]):
          break
      if dataBlastResistanceBlokc == None: dataBlastResistanceBlokc = '0'
      if dataHardnessBlokc == None: dataHardnessBlokc ='0'
      if dataLuminousBlokc == None: dataLuminousBlokc = 'No'
      if dataTransparentBlokc == None: dataTransparentBlokc = 'No'
      return dataBlastResistanceBlokc , dataHardnessBlokc , dataLuminousBlokc , dataTransparentBlokc

    def linkStructureBlock_identifierStructureBlock(linkStructureBlock):
      identifierStructureBlock = ''
      for charStructureBlock in linkStructureBlock[::-1]:
        if charStructureBlock != '/':
          identifierStructureBlock += charStructureBlock
        else:
          break
      if '%' in identifierStructureBlock:
         indexChar = identifierStructureBlock.find('%')
         identifierStructureBlock = identifierStructureBlock[:indexChar-2] + '_' + identifierStructureBlock[indexChar+1:]
      return identifierStructureBlock[::-1].lower()

    dataframesStructuresBlocks , dataframeBlocks = linksStructuresBlocks_dataframeStructuresBlocks(linksAsideStructuresBlocks,mobsAsideStructuresBlocks,linksSectionStructuresBlocks,tableSectionStructuresBlocks,linksSectionDivStructuresBlocks)

    dataframe_json([dataframesStructuresBlocks,dataframeBlocks],['jsonStructures_Blocks','jsonBlocks'])

if __name__=='__main__':
    jsonBlocks()