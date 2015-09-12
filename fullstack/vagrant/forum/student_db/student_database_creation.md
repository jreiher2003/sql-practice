https://www.sqlite.org/cli.html

001
-- CREATE DATABASE
002
 
003
sqlite3 studentdb.db
004
 
005
-- There are no ENUMs in SQLite, so we need a separate table for sex
006
 
007
CREATE TABLE sex_type(
008
sex_id TEXT PRIMARY KEY NOT NULL,
009
sex_type INTEGER);
010
 
011
-- Fill the sex_type table
012
 
013
INSERT INTO sex_type(sex_id, sex_type) VALUES ('M',1);
014
INSERT INTO sex_type(sex_id, sex_type) VALUES ('F',2);
015
 
016
--------
017
 
018
CREATE TABLE student(
019
name VARCHAR(23) NOT NULL, -- VARCHAR is treated as TEXT and 23 is ignored
020
sex CHARACTER(1) NOT NULL, -- CHARACTER and the length restriction is ignored
021
id_number INTEGER PRIMARY KEY AUTOINCREMENT,
022
foreign key(sex) references sex_type(sex_id));
023
 
024
--------
025
 
026
-- Creating an ENUM that represents the type of test (Quiz or Test)
027
 
028
CREATE TABLE test_type(
029
test_id TEXT PRIMARY KEY NOT NULL,
030
test_type INTEGER);
031
 
032
-- Fill the test_type table
033
 
034
INSERT INTO test_type(test_id, test_type) VALUES ('Q',1);
035
INSERT INTO test_type(test_id, test_type) VALUES ('T',2);
036
 
037
--------
038
 
039
CREATE TABLE test(
040
  date     DATE NOT NULL, -- DATE is seen as a NUMERIC type
041
  type_test TEXT NOT NULL,
042
  test_id INTEGER PRIMARY KEY AUTOINCREMENT,
043
  FOREIGN KEY (type_test) REFERENCES test_type (test_id));
044
 
045
 
046
CREATE TABLE test_score(
047
student_id INTEGER NOT NULL,
048
test_id INTEGER NOT NULL,
049
score INTEGER NOT NULL,
050
FOREIGN KEY (test_id) REFERENCES test (test_id),
051
FOREIGN KEY (student_id) REFERENCES student (id_number),
052
PRIMARY KEY (test_id, student_id)); -- A Composite Primary Key
053
 
054
--------
055
 
056
CREATE TABLE absence(
057
  student_id INTEGER NOT NULL,
058
  date       DATE NOT NULL,
059
  PRIMARY KEY (student_id, date),
060
  FOREIGN KEY (student_id) REFERENCES student (id_number));
061
   
062
-------
063
 
064
INSERT VALUES
065
 
066
INSERT INTO student (name, sex) VALUES ('Sally','F');
067
INSERT INTO student (name, sex) VALUES ('Mark','M');
068
INSERT INTO student (name, sex) VALUES ('Paul','M');
069
INSERT INTO student (name, sex) VALUES ('Peter','M');
070
INSERT INTO student (name, sex) VALUES ('Michael','M');
071
INSERT INTO student (name, sex) VALUES ('Thomas','M');
072
INSERT INTO student (name, sex) VALUES ('Rebecca','F');
073
INSERT INTO student (name, sex) VALUES ('Willow','F');
074
INSERT INTO student (name, sex) VALUES ('Sarah','F');
075
INSERT INTO student (name, sex) VALUES ('Emily','F');
076
 
077
 
078
-- date, type_test, test_id
079
 
080
INSERT INTO test VALUES (date('now'),'Q',1); -- New Test: NULL for Autoincrement
081
 
082
-- student_id, test_id, score
083
 
084
INSERT INTO test_score VALUES (1,1,24);
085
INSERT INTO test_score VALUES (2,1,22);
086
INSERT INTO test_score VALUES (3,1,-1);
087
INSERT INTO test_score VALUES (4,1,19);
088
INSERT INTO test_score VALUES (5,1,25);
089
INSERT INTO test_score VALUES (6,1,22);
090
INSERT INTO test_score VALUES (7,1,18);
091
INSERT INTO test_score VALUES (8,1,16);
092
INSERT INTO test_score VALUES (9,1,20);
093
INSERT INTO test_score VALUES (10,1,19);
094
 
095
-- student_id, date
096
 
097
INSERT INTO absence VALUES (3,date('now')); -- One student was absent
098
 
099
------- NEW TEST
100
 
101
-- date, type_test, test_id
102
 
103
INSERT INTO test VALUES ('2013-06-10','T',2); -- Put quotes around date
104
 
105
-- student_id, test_id, score
106
 
107
INSERT INTO test_score VALUES (1,2,48);
108
INSERT INTO test_score VALUES (2,2,44);
109
INSERT INTO test_score VALUES (3,2,42);
110
INSERT INTO test_score VALUES (4,2,-1);
111
INSERT INTO test_score VALUES (5,2,40);
112
INSERT INTO test_score VALUES (6,2,45);
113
INSERT INTO test_score VALUES (7,2,50);
114
INSERT INTO test_score VALUES (8,2,39);
115
INSERT INTO test_score VALUES (9,2,-1);
116
INSERT INTO test_score VALUES (10,2,-1);
117
 
118
-- student_id, date
119
 
120
INSERT INTO absence VALUES (4,'2013-06-10');
121
INSERT INTO absence VALUES (9,'2013-06-10');
122
INSERT INTO absence VALUES (10,'2013-06-10');
123
 
124
-- SELECT QUERIES
125
 
126
-- Show test results for all students for the quiz given on 2013-06-08
127
-- We need to pull this information from 2 tables this time
128
 
129
SELECT student_id, score, type_test, date
130
FROM test, test_score
131
WHERE date = '2013-06-08'
132
AND test.test_id = test_score.test_id;
133
 
134
-- Print out the students name with the scores
135
-- You have to match the student ids for tables test_score and student
136
-- That way they will only show the test score that corresponds with each
137
-- individual student
138
 
139
SELECT name, score, type_test, date
140
FROM test, test_score, student
141
WHERE date = '2013-06-08'
142
AND test.test_id = test_score.test_id
143
AND test_score.student_id = student.id_number;
144
 
145
-- List all students along with their number of absences
146
-- Since we are using an aggregate query here to group data we have to define
147
-- how we want the information to be grouped when it is displayed on the screen.
148
-- That is why we define id_number as the way to group information. It is saying
149
-- that we should calculate the number of absences for each id_number.
150
 
151
SELECT name AS NAME,
152
COUNT(absence.date) AS ABSENCES
153
FROM student, absence
154
WHERE absence.student_id = student.id_number
155
GROUP BY id_number;
156
 
157
-- SQLite JOINS
158
 
159
-- Above we defined INNER JOINs by separating tables with a comma. You can also
160
-- define them with the word INNER JOIN
161
 
162
-- An INNER JOIN is the most common join. An INNER JOIN returns only those
163
-- records from tables that match. The JOIN CONDITION defines the results.
164
 
165
SELECT name, score, test_id
166
FROM test_score JOIN student
167
ON student_id = id_number;
168
 
169
 
170
 
171
-- To show all students with the number of ansences even if they have none we
172
-- have to use a LEFT JOIN.
173
 
174
-- The LEFT JOIN says that we need a row for each piece of data listed on the
175
-- left of the join. Don't forget to change WHERE into ON
176
 
177
SELECT name AS NAME,
178
COUNT(absence.date) AS ABSENCES
179
FROM student LEFT JOIN absence
180
ON absence.student_id = student.id_number
181
GROUP BY id_number;
182
 
183
 
184
 
185
-- A NATURAL INNER JOIN is similar to a LEFT JOIN in that it returns all columns
186
-- that match in both tables.
187
 
188
SELECT score, test_id
189
FROM student NATURAL JOIN test_score
190
WHERE student_id = id_number;
191
 
192
 
193
 
194
-- A CROSS INNER JOIN (Cartesian Join) combines all the records from 2 tables.
195
-- This can sometimes make a mess and should normally be avoided
196
 
197
SELECT score, test_id 
198
FROM student CROSS JOIN test_score;
199
 
200
 
201
 
202
-- Applying Functions in SQLite
203
 
204
-- Find the Best and Worst Scores on all quizes and tests
205
 
206
-- test_score : student_id, test_id, score
207
-- test : date, type_test, test_id
208
-- student : name, sex, id_number
209
 
210
SELECT test.date AS DATE,
211
MIN(test_score.score) AS WORST,
212
MAX(test_score.score) AS BEST
213
FROM test_score, test
214
WHERE test_score.test_id = test.test_id
215
GROUP BY test.date;
216
 
217
-- Print the average score on each test
218
 
219
SELECT test.date AS DATE,
220
AVG(test_score.score) 'AVG SCORE'
221
FROM test_score, test
222
WHERE test_score.test_id = test.test_id
223
GROUP BY test.date;
224
 
225
-- List all students that had a test score over 40
226
 
227
SELECT name, test_score.score
228
FROM test_score, student
229
WHERE test_score.score > 40 AND test_score.student_id = student.id_number
230
GROUP BY name;
231
 
232
SELECT COUNT(name) AS 'SCORED OVER 40'
233
FROM student
234
WHERE student.name in
235
(SELECT name
236
FROM test_score, student
237
WHERE test_score.score > 40 AND test_score.student_id = student.id_number
238
GROUP BY name);
239
 
240
-- VIEWS IN SQLite --
241
 
242
-- A view is used to store a queries result. It is not part of the schema
243
 
244
CREATE VIEW ScoreOver40 AS
245
SELECT name, test_score.score
246
FROM test_score, student
247
WHERE test_score.score > 40
248
AND test_score.student_id = student.id_number
249
GROUP BY name;
250
 
251
drop view ScoreOver40; -- Delete the view
252
 
253
-- TRIGGERS in SQLite --
254
 
255
-- Triggers are operations that are automatically performed when a specific
256
-- event occurs
257
 
258
-- test : date, type_test, test_id
259
-- test_score : student_id, test_id, score
260
-- student : name, sex, id_number
261
 
262
-- Will Hold Data When a Student Has a Makeup Test
263
 
264
CREATE TABLE Log(
265
id INTEGER PRIMARY KEY,
266
test_id INTEGER NOT NULL,
267
date     DATE NOT NULL,
268
student_id INTEGER NOT NULL,
269
FOREIGN KEY (test_id) REFERENCES test_score (test_id),
270
FOREIGN KEY (student_id) REFERENCES test_score (student_id));
271
 
272
-- The Trigger that updates the Log when test_score is updated
273
 
274
CREATE TRIGGER test_score_update
275
AFTER UPDATE OF score ON test_score
276
BEGIN
277
INSERT INTO Log(test_id, date, student_id)
278
VALUES(new.test_id, date('now'), new.student_id);
279
-- Don't reference table instead use new
280
END;
281
 
282
select * from absence; -- Show all absences
283
 
284
UPDATE test_score
285
SET score=20
286
WHERE test_id=2 AND student_id=9;
20 Responses to “SQLite3 Tutorial 4”

