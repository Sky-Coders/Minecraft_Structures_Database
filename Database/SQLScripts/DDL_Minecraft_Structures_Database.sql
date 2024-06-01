-- Minecraft Structures Database 
-- Descripción: Archivo SQL para la creación de la base de datos y DDL 
-- Autores:

-- DDL: Creación de la base de datos
DROP DATABASE IF EXISTS Minecraft_Structures_Database;
CREATE DATABASE Minecraft_Structures_Database;
USE Minecraft_Structures_Database;


CREATE TABLE structure (
	identifier VARCHAR(30) PRIMARY KEY,
	name VARCHAR(30) UNIQUE
	);

CREATE TABLE dimension (
	identifier VARCHAR(30) PRIMARY KEY,
	name VARCHAR(30) NOT NULL,
	numeric_id TINYINT DEFAULT 0
	);

CREATE TABLE block (
	identifier VARCHAR(30) PRIMARY KEY,
	name VARCHAR(30),
	blast_resistance VARCHAR(5),
	hardness VARCHAR(5),
	luminosity ENUM("yes", "no"),
	transparency ENUM("yes", "no","partial")
	);

CREATE TABLE drops (
	identifier VARCHAR(30) PRIMARY KEY,
    	name VARCHAR(30) NOT NULL
    	);
    
CREATE TABLE mob (
	identifier VARCHAR(30) PRIMARY KEY,
    	name VARCHAR(30) UNIQUE,
    	aggressiveness ENUM("passive", "neutral", "hostile")
    	);
    
CREATE TABLE loot (
	identifier VARCHAR(30) PRIMARY KEY,
    	name VARCHAR(30) NOT NULL,
    	rarity VARCHAR(30),
    	renewable ENUM("yes", "no"),
    	stackable TINYINT UNSIGNED
    	);

