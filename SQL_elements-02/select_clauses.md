Select clauses

These are all the select clauses we've seen in the lesson so far.

where

The where clause expresses restrictions — filtering a table for rows that follow a particular rule. where supports equalities, inequalities, and boolean operators (among other things):

where species = 'gorilla' — return only rows that have 'gorilla' as the value of the species column.
where name >= 'George' — return only rows where the name column is alphabetically after 'George'.
where species != 'gorilla' and name != 'George' — return only rows where species isn't 'gorilla' and name isn't 'George'.
limit / offset

The limit clause sets a limit on how many rows to return in the result table. The optional offset clause says how far to skip ahead into the results. So limit 10 offset 100 will return 10 results starting with the 101st.

order by

The order by clause tells the database how to sort the results — usually according to one or more columns. So order by species, name says to sort results first by the species column, then by name within each species.

Ordering happens before limit/offset, so you can use them together to extract pages of alphabetized results. (Think of the pages of a dictionary.)

The optional desc modifier tells the database to order results in descending order — for instance from large numbers to small ones, or from Z to A.

group by

The group by clause is only used with aggregations, such as max or sum. Without a group by clause, a select statement with an aggregation will aggregate over the whole selected table(s), returning only one row. With a group by clause, it will return one row for each distinct value of the column or expression in the group by clause.

###########################################################################
The having clause works like the where clause, but it applies after group by aggregations take place. The syntax is like this:

select columns from tables group by column having condition ;

Usually, at least one of the columns will be an aggregate function such as count, max, or sum on one of the tables' columns. In order to apply having to an aggregated column, you'll want to give it a name using as. For instance, if you had a table of items sold in a store, and you wanted to find all the items that have sold more than five units, you could use:

select name, count(*) as num from sales having num > 5;

You can have a select statement that uses only where, or only group by, or group by and having, or where and group by, or all three of them!

But it doesn't usually make sense to use having without group by.

If you use both where and having, the where condition will filter the rows that are going into the aggregation, and the having condition will filter the rows that come out of it.

You can read more about having here:

http://www.postgresql.org/docs/9.4/static/sql-select.html#SQL-HAVING



