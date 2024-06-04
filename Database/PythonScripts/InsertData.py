import pandas as pd

def fromJSON_InsertData(DMLfile,jsonName,tableName,columnsTable=None,functionsApply=[]):
    jsonPath = '../../Data/dataJSON/json'+jsonName+'.json'
    dataframe = pd.read_json(jsonPath)

    for function , column in functionsApply:
        dataframe[column] = dataframe[column].map(function)

    if not columnsTable:
        headerInsert = f'INSERT INTO {tableName} VALUES\n\t'
    else:
        headerInsert = f'INSERT INTO {tableName}'+columnsTable_columnsRepr(columnsTable)+'VALUES\n\t'
    DMLfile.write(headerInsert)

    dataRecords = []
    for record in dataframe.values:
        dataRecords.append('('+record_reprData(record)+')')    
    DMLfile.write(',\n\t'.join(dataRecords))
    
    DMLfile.write(';')

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
        DMLfile.write('USE Minecraft_Structures_Database;')
        #Aqui se van los poner las diferentes llamadas a la
        #funcion fromJSON_InsertData de las respectivas tablas