#! /usr/bin/env python3

import psycopg2
DBNAME = "news"


def execute_query(query):
    """Connects to the database, runs the query passed to it,
    and returns the results"""
    
    try:
        db = psycopg2.connect(database=DBNAME)
        c = db.cursor()
        c.execute(query)
        rows = c.fetchall()
        db.close()
        return rows
    except:
        print("Connection to database failed!")


def top_articles():
    '''Returns top 3 most read articles'''

    query = """
        select articles.title as article, count(*) as views
        from articles join log
        on log.path ~~ concat('%', articles.slug)
        where log.status = '200 OK'
        group by articles.title
        order by views desc limit 3;
        """

    output = execute_query(query)

    print('\nTop three articles:')
    for i in output:
        print('"' + i[0] + '"' + ' -- ' + str(i[1]) + ' views')
# turned i[1] into str in order to concatenate
# where i[0] is title and i[1] is number of views and so on


def top_authors():
    '''Returns top authors by page views'''

    query = """
        select authors.name as author, count(*) as views
        from authors join articles
        on authors.id = articles.author
        join log
        on log.path ~~ concat('%', articles.slug)
        where log.status = '200 OK'
        group by authors.name
        order by views desc;
    """

    output = execute_query(query)

    print('\nTop authors: ')
    for i in output:
        print('"' + i[0] + '"' + ' -- ' + str(i[1]) + ' views')


def errors():
    '''Returns days with more than 1% requests lead to error'''

    query = """
        select to_char(date, 'Mon DD, YYYY') as date, percent
        from err_prc
        where percent > 1.0;
        """

    output = execute_query(query)

    print('\nDays with errors > 1%')
    for i in output:
        print(i[0] + ' -- ' + str(i[1]) + '%' + ' errors')


if __name__ == "__main__":
    top_articles()
    top_authors()
    errors()
# to make sure that the code is only run when the program is executed directly, not when imported as a module.
