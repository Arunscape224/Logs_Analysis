#! /usr/bin/env python3

import psycopg2

DBNAME = "news"


def run_query(query):
        db = psycopg2.connect(database=DBNAME)
        c = db.cursor()
        c.execute(query)
        rows = c.fetchall()
        db.close()
        return rows


def top_three_articles():
    ''' Prints out the three most popular articles '''
    query1 = """ SELECT title, COUNT(*)
    AS num FROM articles,log
    WHERE log.path=CONCAT('/article/', articles.slug)
    GROUP BY articles.title
    ORDER BY num DESC LIMIT 3; """

    # Run Query
    results1 = run_query(query1)

    # Print Results
    print('----------------------------------------------')
    print("Three Most Popular Articles:\n")
    for i in results1:

        print('"{0}" | {1} views'.format(i[0], str(i[1])))

    print('')


def top_three_authors():
    ''' Prints out the three most popular authors '''
        query2 = """ SELECT authors.name, COUNT(*)
        AS num FROM authors,articles,log
        WHERE (log.path=CONCAT('/article/', articles.slug)
        AND (articles.author = authors.id))
        GROUP BY authors.name
        ORDER BY num DESC; """

        # Run Query
        results2 = run_query(query2)

        # Print Results
        print('----------------------------------------------')
        print("The Most Popular Authors:\n")
        for i in results2:

            print('"{0}" | {1} views'.format(i[0], str(i[1])))

        print('\n----------------------------------------------')


def percent_error():
        ''' Prints out the days where requests that were errors is greater than 1% '''
        query3 = """ SELECT * FROM
        (SELECT DATE(TIME), round(100.0 * sum(CASE log.status
        WHEN '404 NOT FOUND'
        THEN 1 ELSE 0 END) / count(log.status), 1)
        AS error FROM log
        GROUP BY DATE(TIME)
        ORDER BY error DESC)
        AS subq WHERE error > 1; """

        # Run Query
        results3 = run_query(query3)

        # Print Results
        print("Days where more than 1% of requests lead to a '404' error:\n")
        for i in results3:

            print('"{0}" | {1}% errors'.format(i[0], str(i[1])))

        print('\n----------------------------------------------')

if __name__ == "__main__":
    top_three_articles()
    top_three_authors()
    percent_error()
