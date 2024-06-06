-- ¿Cuáles son las 10 estructuras con la mayor diversidad de bloques?
/*
    Se solicita el nombre de cada estructura junto con la 
    cantidad de bloques diferentes que la componen, ordenados 
    de forma descendente según éste último criterio y solo
    limitados a los primeros 10 resultados
*/
SELECT struc.name AS 'Nombre de la estructura', COUNT(*) AS 'Cantidad de bloques diferentes'
FROM structure AS struc
LEFT JOIN structure_block AS strucblock ON struc.identifier = strucblock.structure_identifier
GROUP BY struc.identifier
ORDER BY `Cantidad de bloques diferentes` DESC
LIMIT 10;
-- Funciona


-- ¿Cuántas estructuras hay en cada bioma?
/*
    Se solicita el nombre de cada bioma junto con la cantidad de 
    estructuras que se pueden encontrar en ellas
*/
SELECT bio.name AS 'Nombre del bioma' , COUNT(*) AS 'Cantidad de estructuras'
FROM biome AS bio
LEFT JOIN structure_biome AS strucbio ON bio.identifier = strucbio.biome_identifier
GROUP BY bio.identifier;
-- Funciona


-- ¿Cuáles son los loots con la menor probabilidad de aparición en cada estructura?
/*
    Se solicita el nombre de las estructuras que tengan loot y el menor valor de 
    chance asociado a la estructura junto con de todos los loots pertenecientes
    a esa estructura que tengan el menor de chance
*/
SELECT struc.name AS 'Nombre de la estructura', strucloot.chance AS 'Mínima probabilidad' , loot.name AS 'Nombre del loot' 
FROM structure AS struc
RIGHT JOIN structure_loot AS strucloot ON struc.identifier = strucloot.structure_identifier
INNER JOIN loot AS loot ON strucloot.loot_identifier = loot.identifier
WHERE (struc.identifier,strucloot.chance) IN (SELECT structure_identifier , MIN(strucloot.chance)
                                              FROM structure_loot AS strucloot
                                              GROUP BY strucloot.structure_identifier)
ORDER BY struc.name , loot.name;
-- Funciona


-- ¿Cuáles son los drops que se pueden conseguir en las distintas estructuras?
/*
    Se solicita los nombres de las diferentes estructuras con las que cuentan 
    con mobs que tienen drops y mostrar estos últimos para cada estructura 
*/
SELECT struc.name AS 'Nombre de la estructura' , drops.name AS 'Nombre del drop'
FROM structure AS struc
INNER JOIN structure_mob AS strucmob ON struc.identifier = strucmob.structure_identifier
INNER JOIN mob AS mob ON strucmob.mob_identifier = mob.identifier
INNER JOIN drops_mob AS dropmob ON mob.identifier = dropmob.mob_identifier
LEFT JOIN drops AS drops ON dropmob.drops_identifier = drops.identifier
ORDER BY struc.name;
-- Funciona


-- ¿Cuál es el bloque más resistente a las explosiones de cada estructura?
/*
    Se solicita el nombre de cada estructura junto con el nombre del bloque 
    con el valor de resistencia a explosiones más alto 
*/
SELECT struc.name AS 'Nombre de la estructura' , block.name AS 'Nombre del bloque con mayor resistencia a explosiones'
FROM structure AS struc
LEFT JOIN structure_block AS strucblock ON struc.identifier = strucblock.structure_identifier
INNER JOIN block AS block ON strucblock.block_identifier = block.identifier
WHERE (struc.identifier,block.blast_resistance) IN (SELECT struc.identifier , MAX(block.blast_resistance)
                                                    FROM structure AS struc 
                                                    LEFT JOIN structure_block AS strucblock ON struc.identifier = strucblock.structure_identifier
                                                    INNER JOIN block AS block ON strucblock.block_identifier = block.identifier
                                                    GROUP BY struc.identifier)
GROUP BY struc.identifier
ORDER BY struc.identifier;
-- Finalizada


-- Según los bloques que componen las estructuras ¿En qué biomas se pueden encontrar bloques que su transparencia sea parcial?
/*
    Se solicita de los nombres de lo biomas con los que cuenten con una estructura 
    cuáles tienen un bloque de transparencia parcial en sus respectivas estructuras
*/
SELECT biome.name AS 'Nombre del bioma con bloques transparentes'
FROM biome AS biome
INNER JOIN structure_biome AS strucbio ON biome.identifier = strucbio.biome_identifier
INNER JOIN structure AS struc ON strucbio.structure_identifier = struc.identifier
INNER JOIN structure_block AS strucblock ON struc.identifier = strucblock.structure_identifier
LEFT JOIN block AS block ON strucblock.block_identifier = block.identifier
WHERE block.transparency = 'partial'
GROUP BY biome.identifier
ORDER BY biome.name;
-- Finalizado