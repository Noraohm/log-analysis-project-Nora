#!/usr/bin/env python

import psycopg2

# 1- What are the most popular three articles of all time?
first_query = '''select title, author, count (*) as view
from articles, log
where log.path LIKE CONCAT ('%', articles.slug)
group by title, author
order by view desc limit 3;'''

# 2- Who are the most popular article authors of all time?
second_query = '''select authors.name, author, count (*) as view
from articles, authors, log
where log.path LIKE CONCAT ('%',articles.slug) and authors.id = articles.author
group by author, authors.name
order by view desc limit 1;'''

# 3- On which days did more than 1% of requests lead to errors?
third_query = '''select *
from (
SELECT total_status.status_time ,
error_per_day,
status_per_day,
((error_per_day::float*100)/status_per_day::float) AS ratio
FROM total_status
INNER JOIN Not_found_error ON
total_status.status_time = Not_found_error.error_time
GROUP BY total_status.status_time, error_per_day, status_per_day
ORDER BY ratio ) as result
where ratio > 1.0;'''


# to get the query
def get_query_result(query):
    ''' The function is to connect the database with psql
    and to give the instruction to a cursor to fetch all the required result
    and close the database once done'''
    db = psycopg2.connect(dbname="news")
    c = db.cursor()
    c.execute(query)
    results = c.fetchall()
    db.close()
    return results


# To print the query result
def print_queries_results(query_result):
    ''' the function to print the first & second queries with loop method '''
    for result in query_result:
        print("\t{} by {} views".format(result[0], result[2]))


def print_third_query_results(query_result):
    '''  the function to print the 3rd query which has different resutl
     not the like the above 2 as it a ratio percentage '''
    for result in query_result:
        print("\t{} with error ratio {} %".format(result[0], result[3]))


# welcome page 1st appear in the python and give instruction to the user.
if __name__ == '__main__':
    Welcome_page = raw_input(''' \n Hi there ! .. \n
WELCOME TO  THE NEWS PAPER DATABASE ,\n
below there are multiple queries , and you can select the required \n
by typing the No. which next to the required Question:

1)What are the most popular three articles of all time? " The most browsed".

2)Who are the most popular article authors of all time? " popular author".

3)On which days did more than 1% of requests lead to errors?

4) All of the above.
'''.title())
    if Welcome_page == '1':
        print "What are the most popular three articles of all time?"
        print_queries_results(get_query_result(first_query))
    elif Welcome_page == '2':
        print "Who are the most popular article authors of all time?"
        print_queries_results(get_query_result(second_query))
    elif Welcome_page == '3':
        print "On which days did more than 1% of requests lead to errors?"
        print_third_query_results(get_query_result(third_query))
    elif Welcome_page == '4':
        print "What are the most popular three articles of all time?"
        print_queries_results(get_query_result(first_query))
        print "\n Who are the most popular article authors of all time?"
        print_queries_results(get_query_result(second_query))
        print "\nOn which days did more than 1% of requests lead to errors?"
        print_third_query_results(get_query_result(third_query))
    else:
        print ("Thanks for visiting the DataBase")
        close()
