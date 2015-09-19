-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

CREATE TABLE players (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT NOT NULL);

-- CREATE TABLE matchup (
-- 	player_1 TEXT,
-- 	player_2 TEXT,
-- 	win INTEGER,
-- 	loss INTEGER,
-- 	FOREIGN KEY(player_1) REFERENCES players(id),
-- 	FOREIGN KEY(player_2) REFERENCES players(id));
