# writing an sql query

QUERY = """
	select name, birthdate from animals where sqecies = 'gorilla';
"""

QUERY = """
	select name from animals where species != 'gorilla' and name != 'Max';
"""

#
# Find all the llamas born between January 1, 1995 and December 31, 1998.
# Fill in the 'where' clause in this query.

QUERY = '''
select name from animals where species = 'llama' and birthdate <= '1998-12-31' and birthdate >= '1995-01-01' ; 
'''


#
# Find the one food that is eaten by only one animal.
#
# The animals table has columns (name, species, birthdate) for each individual.
# The diet table has columns (species, food) for each food that a species eats.
#

QUERY = '''
select food, count(*) as num from diet 
    join animals on animals.species = diet.species group by food order by num asc limit 1;
'''

#
# List all the taxonomic orders, using their common names, sorted by the number of
# animals of that order that the zoo has.
#
# The animals table has (name, species, birthdate) for each individual.
# The taxonomy table has (name, species, genus, family, t_order) for each species.
# The ordernames table has (t_order, name) for each order.
#
# Be careful:  Each of these tables has a column "name", but they don't have the
# same meaning!  animals.name is an animal's individual name.  taxonomy.name is
# a species' common name (like 'brown bear').  And ordernames.name is the common
# name of an order (like 'Carnivores').

QUERY = '''
select ordernames.name, count(*) as num from animals, taxonomy, ordernames where
    animals.species = taxonomy.name and taxonomy.t_order = ordernames.t_order
    group by ordernames.name order by num desc;
'''