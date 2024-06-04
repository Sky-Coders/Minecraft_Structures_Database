-- Minecraft Structures Database 
-- Descripción: Archivo SQL para la creación de la base de datos y DDL 
-- Autores:

-- DDL: Creación de la base de datos
DROP DATABASE IF EXISTS Minecraft_Structures_Database;
CREATE DATABASE Minecraft_Structures_Database;
USE Minecraft_Structures_Database;

-- DDL: Creación de las tablas
CREATE TABLE dimension (
	identifier VARCHAR(30) PRIMARY KEY,
	name VARCHAR(30) NOT NULL,
	numeric_id TINYINT NOT NULL
	);

CREATE TABLE biome (
	identifier VARCHAR(30) PRIMARY KEY,
	dimension_identifier VARCHAR(30) NOT NULL,
	name VARCHAR(30) NOT NULL,
	numeric_id TINYINT UNSIGNED UNIQUE,
	precipitation ENUM("yes","no") NOT NULL,
	grass_color CHAR(7) NOT NULL,
	foliage_color CHAR(7) NOT NULL,
	temperature DECIMAL(4,2) NOT NULL,
	water_color CHAR(7) NOT NULL,

	CONSTRAINT reference_between_biome_dimension FOREIGN KEY (dimension_identifier) REFERENCES dimension (identifier)
	);

CREATE TABLE structure (
	identifier VARCHAR(30) PRIMARY KEY,
	name VARCHAR(30) UNIQUE
	);

CREATE TABLE structure_biome (
	structure_identifier VARCHAR(30) NOT NULL,
	biome_identifier VARCHAR(30) NOT NULL,

	CONSTRAINT reference_between_strucbiom_structure FOREIGN KEY (structure_identifier) REFERENCES structure (identifier),
	CONSTRAINT reference_between_strucbiom_biome FOREIGN KEY (biome_identifier) REFERENCES biome (identifier)
	);

CREATE TABLE block (
	identifier VARCHAR(30) PRIMARY KEY,
	name VARCHAR(30) NOT NULL,
	blast_resistance DECIMAL(11,2) NOT NULL,
	hardness DECIMAL(4,2) NOT NULL,
	luminosity ENUM("yes", "no") NOT NULL,
	transparency ENUM("yes", "no","partial") NOT NULL
	);

CREATE TABLE structure_block (
	structure_identifier VARCHAR(30) NOT NULL,
	block_identifier VARCHAR(30) NOT NULL,
	CONSTRAINT reference_between_strucblock_structure FOREIGN KEY (structure_identifier) REFERENCES structure (identifier),
	CONSTRAINT reference_between_strucblock_block FOREIGN KEY (block_identifier) REFERENCES block (identifier)
	);

CREATE TABLE loot (
	identifier VARCHAR(30) PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    rarity VARCHAR(30) NOT NULL,
    renewable ENUM("yes", "no") NOT NULL,
    stackable TINYINT UNSIGNED NOT NULL
    );

CREATE TABLE structure_loot (
	structure_identifier VARCHAR(30) NOT NULL,
	loot_identifier VARCHAR(30) NOT NULL,
	stack_size_lower TINYINT NOT NULL,
	stack_size_upper TINYINT NOT NULL, 
	chance DECIMAL(5,2) NOT NULL,

	CONSTRAINT reference_between_strucloot_structure FOREIGN KEY (structure_identifier) REFERENCES structure (identifier),
	CONSTRAINT reference_between_strucloot_loot FOREIGN KEY (loot_identifier) REFERENCES loot (identifier)
	);

CREATE TABLE mob (
	identifier VARCHAR(30) PRIMARY KEY,
    name VARCHAR(30) UNIQUE,
    aggressiveness ENUM("passive", "neutral", "hostile") NOT NULL
    );

CREATE TABLE structure_mob (
	structure_identifier VARCHAR(30) NOT NULL,
	mob_identifier VARCHAR(30) NOT NULL,

	CONSTRAINT reference_between_strucmob_structure FOREIGN KEY (structure_identifier) REFERENCES structure (identifier),
	CONSTRAINT reference_between_strucmob_mob FOREIGN KEY (mob_identifier) REFERENCES mob (identifier)
	);

CREATE TABLE drops (
	identifier VARCHAR(30) PRIMARY KEY,
    name VARCHAR(30) NOT NULL
    );
    
CREATE TABLE drops_mob (
	drops_identifier VARCHAR(30) NOT NULL,
	mob_identifier VARCHAR(30) NOT NULL,

	CONSTRAINT reference_between_dropsmob_drops FOREIGN KEY (drops_identifier) REFERENCES drops (identifier),
	CONSTRAINT reference_between_dropsmob_mob FOREIGN KEY (mob_identifier) REFERENCES mob (identifier)
	);