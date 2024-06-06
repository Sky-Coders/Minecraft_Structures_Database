def copy_file(backup,file):
    with open(f'../SQLScripts/{file}_Minecraft_Structures_Database.sql',encoding='utf-8') as file_copy:
        for line_copy in file_copy:
            if line_copy[:2] != '--':
                backup.write(line_copy)

if __name__=='__main__':
    with open('../../backup_Minecraft_Structures_Database.sql','w',encoding='utf-8') as backup:
        backup.write('-- Minecraft Structures Database\n')
        backup.write('-- Descripción: Archivo SQL para recuperar la base de datos\n')
        backup.write('-- Autores\n\n\n')

        backup.write('-- DDL: Creación de la base de datos y tablas\n')
        copy_file(backup,'DDL')
        backup.write('\n\n\n')

        backup.write('-- DML: Creación de registros en las tablas\n')
        copy_file(backup,'DML')