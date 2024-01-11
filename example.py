import sqlite3

conn = sqlite3.connect('data/soccer.sqlite')
c = conn.cursor()
c.execute("""
            SELECT
                League.id,
                League.name AS league_name,
                COUNT(matches.id) AS match_count,
                Country.name AS country_name
            FROM "Match" AS matches
            JOIN League ON matches.league_id = League.id
            JOIN Country ON League.country_id = Country.id
            GROUP BY League.id
            ORDER BY
            match_count DESC,
            country_name ASC
          """)
row = c.fetchall()
print(row)