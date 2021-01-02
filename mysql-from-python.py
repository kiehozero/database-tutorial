import os
import datetime
import pymysql

# Get username

username = os.getenv('GH_user')

# Connect to database

connection = pymysql.connect(host='localhost',
                             user=username,
                             password='',
                             db='Chinook')

try:
    # Run a query
    with connection.cursor() as cursor:
        list_of_names = ['Fred', 'Tony']
        # Prepare a string with the same number of placeholders as in list_of_names
        format_strings = ",".join(['%s']*len(list_of_names))
        cursor.execute("DELETE FROM Friends WHERE Name IN({});".format(format_strings), list_of_names)
        connection.commit()
        # commit() saves the changes to the table

finally:
    # Close connection whether above was successful or not
    connection.close()