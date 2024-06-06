import pandas as pd
from genericFunctions import *

def fromJSON_InsertData(DMLfile,jsonName,tableName,columnsTable=None,functionsApply=[]):
    jsonPath = '../../Data/dataJSON/json'+jsonName+'.json'
    dataframe = pd.read_json(jsonPath)

    for function , column in functionsApply:
        if column:
            dataframe[column] = dataframe[column].map(function)
        else:
            function(dataframe)

    if not columnsTable:
        headerInsert = f'INSERT INTO {tableName} VALUES\n\t'
    else:
        headerInsert = f'INSERT INTO {tableName}'+columnsTable_columnsRepr(columnsTable)+' VALUES\n\t'
    DMLfile.write(headerInsert)

    dataRecords = []
    for record in dataframe.values:
        dataRecords.append('('+record_reprData(record)+')')    
    DMLfile.write(',\n\t'.join(dataRecords))
    
    DMLfile.write(';\n\n')

def columnsTable_columnsRepr(columnsTable):
    return '('+','.join(columnsTable)+')'

def record_reprData(record):
    return ' , '.join([value_normalize(value) for value in record])

def value_normalize(value):
    dataType = type(value)
    if dataType==str:
        return f"'{value.lower()}'"
    else:
        return str(value)
    
if __name__=='__main__':
    with open('../SQLScripts/DML_Minecraft_Structures_Database.sql','w',encoding='utf-8') as DMLfile:
        DMLfile.write('-- Minecraft Structures Database\n')
        DMLfile.write('-- Descripción: Archivo SQL para insertar los registros a base de datos\n')
        DMLfile.write('-- Autores:\n\n')
        
        fromJSON_InsertData(DMLfile,'Dimensions','dimension',['identifier', 'numeric_id', 'name'])
        
        fromJSON_InsertData(DMLfile,'Biomes','biome',['identifier', 'numeric_id', 'name', 'temperature', 'precipitation', 'grass_color', 'foliage_color', 'water_color', 'dimension_identifier'])
        
        fromJSON_InsertData(DMLfile,'Structures','structure',['identifier', 'name'])
        
        functionsApply_Structures_Biomes = [(str_search_replace('mushroom_field_shore','mushroom_fields'),'biome_identifier'),
                                            (str_search_replace('desert_hills','desert'),'biome_identifier'),
                                            (str_search_replace('jungle_hills','jungle'),'biome_identifier'),
                                            (str_search_replace('deep_warm_ocean','warm_ocean'),'biome_identifier'),
                                            (str_search_replace('taiga_hills','taiga'),'biome_identifier'),
                                            (str_search_replace('snowy_taiga_hills','taiga'),'biome_identifier'),
                                            (str_search_replace('dark_forest_hills','dark_forest'),'biome_identifier')]
        fromJSON_InsertData(DMLfile,'Structures_Biomes','structure_biome',functionsApply=functionsApply_Structures_Biomes)
        
        functionsApply_Blocks = [(str_cast_numeric(float),'blast_resistance'),
                                 (str_cast_numeric(float),'hardness')]
        fromJSON_InsertData(DMLfile,'Blocks','block',functionsApply=functionsApply_Blocks)

        functionsApply_Structures_Blocks = [(str_search_replace('village#abandoned_villages','abandoned_village'),'structure_identifier'),
                                            (str_search_replace('iceberg_\(','iceberg'),'structure_identifier'),
                                            (str_search_replace('jungle_pyramid','jungle_temple'),'structure_identifier'),
                                            (str_search_replace('monster_room','dungeon'),'structure_identifier'),
                                            (str_search_replace('java_edition','stairs'),'block_identifier')]
        fromJSON_InsertData(DMLfile,'Structures_Blocks','structure_block',functionsApply=functionsApply_Structures_Blocks)

        functionsApply_Loots = [(str_search_replace('flower charge, field masoned, bordure indented, globe, snoutcommoncreeper charge, skull chargeuncommonthingepic','Common'),'rarity'),
                                (str_search_replace("bottle_o'_enchanting",'bottle_o_enchanting'),'identifier'),
                                (str_search_replace("bottle o' enchanting",'Bottle O Enchanting'),'name'),
                                (drop_duplicates,None)]
        fromJSON_InsertData(DMLfile,'Loots','loot',functionsApply=functionsApply_Loots)

        functionsApply_Structures_Loots = [(str_search_replace("bottle_o'_enchanting",'bottle_o_enchanting'),'loot_identifier'),
                                           (str_search_replace('jungle_pyramid','jungle_temple'),'structure_identifier')]
        fromJSON_InsertData(DMLfile,'Structures_Loots','structure_loot',functionsApply=functionsApply_Structures_Loots)

        fromJSON_InsertData(DMLfile,'Mobs','mob')

        fromJSON_InsertData(DMLfile,'Structures_Mobs','structure_mob')