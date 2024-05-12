import pandas as pd
from GenericsFunctions import linkName_textName , dataframe_json

def jsonMobs():
    aggressivenessMobs =  [('passive',3),('neutral',2),('hostile',4)]
    linkMobs = 'https://minecraft.wiki/w/Mob'

    def linkMobs_dataframeMobs(linkMobs,aggressivenessMobs):
      tablesMobs = linkMobs_tablesMobs(linkMobs,aggressivenessMobs)
      dataframeMobs = []
      linksMob = []
      for tableMobs , aggressivenesTableMobs in tablesMobs:
        dataMobs , linksTableMob = tableMobs_dataMobs(tableMobs,aggressivenesTableMobs)
        dataframeMobs.extend(dataMobs)
        linksMob.extend(linksTableMob)
      dataColumnsMobs = ['identifier','name','aggressiveness']
      return pd.DataFrame(data=dataframeMobs,columns=dataColumnsMobs) , linksMob

    def linkMobs_tablesMobs(linkMobs,aggressivenessMobs):
      textMobs = linkName_textName(linkMobs)
      tablesMobs = textMobs.find_all(name='table')[:9]
      aggressivenessTablesMob = sum([[aggressivenesTableMobs]*amountTablesMob for aggressivenesTableMobs , amountTablesMob in aggressivenessMobs],[])
      tablesMobs = zip(tablesMobs,aggressivenessTablesMob )
      return tablesMobs

    def tableMobs_dataMobs(tableMobs,aggressivenesTableMobs):
      linksTableMob = []
      dataMobs = []
      for dataMob in tableMobs_columnsDataMobs(tableMobs):
        nameMob = dataMob_nameMob(dataMob)
        identifierMob = nameMob_identifierMob(nameMob)
        linkMob = dataMob_linkMob(dataMob)
        dataMobs.append((identifierMob,nameMob,aggressivenesTableMobs))
        linksTableMob.append((identifierMob,linkMob))
      return dataMobs , linksTableMob

    def tableMobs_columnsDataMobs(tableMobs):
      rowTableMobs = tableMobs.find_all(name='tr')[-1]
      return rowTableMobs.find_all(name='td')

    def dataMob_nameMob(dataMob):
      nameMob = dataMob.text.strip()
      if '(' in nameMob:
        index = nameMob.index('(')
        nameMob = nameMob[:index]
      return nameMob

    def nameMob_identifierMob(nameMob):
      wordsNameMob = nameMob.lower().split()
      return '_'.join(wordsNameMob)

    def dataMob_linkMob(dataMob):
      return 'https://minecraft.wiki'+dataMob.find(name='a')['href']

    dataframeMobs , linksMob = linkMobs_dataframeMobs(linkMobs,aggressivenessMobs)

    dataframe_json([dataframeMobs],['jsonMobs'])

    return linksMob

def jsonDrops(linksMob):
    def linksMob_dataframeMobsDrops(linksMob):
      dataframeMobsDrops = []
      dataframeDrops = {}
      for identifierMob , linkMob in linksMob:
        tableDropMob = linkMob_tableDropMob(linkMob)
        if tableDropMob:
          for itemDropMob in tableDropMob:
            identifierDrop , nameDrop = itemDropMob_dataDropMob(itemDropMob)
            if identifierDrop:
              dataframeMobsDrops.append((identifierMob,identifierDrop))
              dataframeDrops.update({identifierDrop:nameDrop})
      dataColumnsMobsDrops = ['mob_indetifier','drop_identifier']
      dataColumnsDrops = ['identifier','name']
      return pd.DataFrame(data=dataframeMobsDrops,columns=dataColumnsMobsDrops) , pd.DataFrame(data=dataframeDrops.items(),columns=dataColumnsDrops)

    def linkMob_tableDropMob(linkMob):
      textMob = linkName_textName(linkMob)
      tablesMob = textMob_tablesMob(textMob)
      for tableMob in tablesMob:
          if (tableCell:=tableMob.find(name='tr').find(name='th')):
            if tableCell.text == 'Item' or tableCell.text == 'Drop':
              return tableMob.find_all(name='tr')[2:]
      return []

    def textMob_tablesMob(textMob):
      return textMob.find_all(name='table')

    def itemDropMob_dataDropMob(itemDropMob):
      nameDrop = itemDropMob.find_all(name='td')
      if len(nameDrop)>3:
        nameDrop = nameDrop[1].find(name='a').text
      else:
        nameDrop = nameDrop[0].find(name='a').text
      return nameDrop_identifierDrop(nameDrop) , nameDrop

    def nameDrop_identifierDrop(nameDrop):
      return '_'.join(nameDrop.lower().split())
    
    dataframeMobsDrops , dataframeDrops = linksMob_dataframeMobsDrops(linksMob)

    dataframe_json([dataframeMobsDrops,dataframeDrops],['jsonMobs_Drops','jsonDrops'])

if __name__=='__main__':
    linksMob = jsonMobs()
    jsonDrops(linksMob)