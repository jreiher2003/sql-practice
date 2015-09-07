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