-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.


CREATE TABLE players (
	id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
	name TEXT NOT NULL,
	wins INTEGER DEFAULT 0,
	matches INTEGER DEFAULT 0
	);

CREATE TABLE matchup (
	id INTEGER,
	winner INT REFERENCES players(id),
	loser INT REFERENCES players(id)
	);
