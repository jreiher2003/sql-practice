#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

# import psycopg2
import sqlite3


def connect():
    """Connect to the sqlite database.  Returns a database connection."""
    conn = sqlite3.connect("tournament.db")
    c = conn.cursor()
    return conn, c

def close():
    """ close db connection """
    conn.commit()
    return conn.close()

# def deleteMatches():
    # """Remove all the match records from the database."""


def deletePlayers():
    """Remove all the player records from the database."""
    delP = c.execute('DELETE from players')
    print "All player records were successfully deleted."
    return delP
    


def countPlayers():
    """Returns the number of players currently registered."""
    c.execute("SELECT count(*) from players")
    num = c.fetchall()[0][0]
    try:
        return c.fetchall()[0][0]
    except IndexError:
        if num == 1:
            print "There is only %d player registered" % (num)
        else:
            print "There are %d players registered" % (num)

    


def registerPlayer(name):
    """Adds a player to the tournament database.
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
    Args:
      name: the player's full name (need not be unique).
    """
    regP = c.execute("INSERT INTO players (name) VALUES(?)", (name,)) # remember to make it a tuple
    print "Successfully added player %s" % name
    return regP



# def playerStandings():
#     """Returns a list of the players and their win records, sorted by wins.

#     The first entry in the list should be the player in first place, or a player
#     tied for first place if there is currently a tie.

#     Returns:
#       A list of tuples, each of which contains (id, name, wins, matches):
#         id: the player's unique id (assigned by the database)
#         name: the player's full name (as registered)
#         wins: the number of matches the player has won
#         matches: the number of matches the player has played
#     """


# def reportMatch(winner, loser):
#     """Records the outcome of a single match between two players.

#     Args:
#       winner:  the id number of the player who won
#       loser:  the id number of the player who lost
#     """
 
 
# def swissPairings():
#     """Returns a list of pairs of players for the next round of a match.
  
#     Assuming that there are an even number of players registered, each player
#     appears exactly once in the pairings.  Each player is paired with another
#     player with an equal or nearly-equal win record, that is, a player adjacent
#     to him or her in the standings.
  
#     Returns:
#       A list of tuples, each of which contains (id1, name1, id2, name2)
#         id1: the first player's unique id
#         name1: the first player's name
#         id2: the second player's unique id
#         name2: the second player's name
#     """


if __name__ == '__main__':
    conn, c = connect()
    registerPlayer('May Flowers')
    countPlayers()
    # deletePlayers()
    close()
