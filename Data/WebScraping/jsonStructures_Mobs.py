import pandas as pd
from GenericsFunctions import linkName_textName as linkStructureMobs_textStructureMobs
from GenericsFunctions import dataframe_json

def jsonStructures_Mobs():
    linksStructuresMobs = ['https://minecraft.wiki/w/Igloo','https://minecraft.wiki/w/Pillager_Outpost',
                           'https://minecraft.wiki/w/Swamp_Hut','https://minecraft.wiki/w/Village',
                           'https://minecraft.wiki/w/Woodland_Mansion','https://minecraft.wiki/w/Ocean_Ruins',
                           'https://minecraft.wiki/w/Ocean_Monument','https://minecraft.wiki/w/Nether_Fortress',
                           'https://minecraft.wiki/w/Bastion_Remnant','https://minecraft.wiki/w/End_City']
    
    dataframePartStructuresMobs = [('ancient_city','warden'),('mineshaft','cave_spider'),('stronghold','silverfish'),('abandoned_village','zombie_villager')]

    def links_dataframePart_StructuresMobs_dataframeStructuresMobs(linksStructuresMobs,dataframePartStructuresMobs):
      dataframeStructuresMobs = linksStructuresMobs_dataframeStructuresMobs(linksStructuresMobs) + dataframePartStructuresMobs
      dataColumnsStructuresMobs = ['structure_identifier','mob_identifier']
      return pd.DataFrame(data=dataframeStructuresMobs,columns=dataColumnsStructuresMobs)

    def linksStructuresMobs_dataframeStructuresMobs(linksStructuresMobs):
      tablesStructuresMobs = linksStructuresMobs_tablesStructuresMobs(linksStructuresMobs)
      dataframeStructuresMobs = []
      for identifierStructure , tableStructureMobs in tablesStructuresMobs:
        for identifierStructureMob in tableStructureMobs_dataStructureMobs(tableStructureMobs):
          if identifierStructure == 'village' and identifierStructureMob == 'zombie_villager':
            continue
          dataframeStructuresMobs.append((identifierStructure,identifierStructureMob))
      return dataframeStructuresMobs

    def linksStructuresMobs_tablesStructuresMobs(linksStructuresMobs):
      tablesStructuresMobs = []
      for linkStructureMobs in linksStructuresMobs:
        identifierStructure , tableStructureMobs = linkStructureMobs_tableStructureMobs(linkStructureMobs)
        tablesStructuresMobs.append((identifierStructure,tableStructureMobs))
      return tablesStructuresMobs

    def linkStructureMobs_tableStructureMobs(linkStructureMobs):
      identifierStructure = linkStructureMobs_identifierStructure(linkStructureMobs)
      textStructureMobs = linkStructureMobs_textStructureMobs(linkStructureMobs)
      tableStructureMobs = textStructureMobs_tableStructureMobs(textStructureMobs)
      return identifierStructure , tableStructureMobs

    def linkStructureMobs_identifierStructure(linkStructureMobs):
      identifierStructure = ''
      for charLinkStructureMobs in linkStructureMobs[::-1]:
        if charLinkStructureMobs != '/':
          identifierStructure += charLinkStructureMobs
        else:
          break
      return identifierStructure[::-1].lower()

    def textStructureMobs_tableStructureMobs(textStructureMobs):
      tableStructureMobs = textStructureMobs.find(name='table').find_all(name='tr')[1].find(name='td')
      return tableStructureMobs

    def tableStructureMobs_dataStructureMobs(tableStructureMobs):
      listStructureMobs = tableStructureMobs.find_all(name='a')
      return [mobStructureMob_identifierMobStructureMob(mobStructureMob) for mobStructureMob in listStructureMobs if mobStructureMob.text and mobStructureMob.text != 'monster spawner']

    def mobStructureMob_identifierMobStructureMob(mobStructureMob):
      dataNameStructureMob = mobStructureMob.text.strip()
      return dataNameStructureMob_identifierMobStructureMob(dataNameStructureMob)

    def dataNameStructureMob_identifierMobStructureMob(dataNameStructureMob):
      identifierMobStructureMob = '_'.join(dataNameStructureMob.lower().split())
      if identifierMobStructureMob == 'black_cat':
        identifierMobStructureMob = 'cat'
      return identifierMobStructureMob
    
    dataframeStructuresMobs = links_dataframePart_StructuresMobs_dataframeStructuresMobs(linksStructuresMobs,dataframePartStructuresMobs)

    dataframe_json([dataframeStructuresMobs],['jsonStructures_Mobs'])

if __name__=='__main__':
    jsonStructures_Mobs()