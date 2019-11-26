

import texttable as tt
from db_utils import *
def list_endpoints():
    """
        In this thing we will do an sqlite3 query and get all of the endpoints minus key files 

    """

    endpoints = get_data("""
        select id, name, host,port,user,keyfile from endpoints;
    """,[])

    titles = ['id', 'name', 'host', 'port','user','keyfile']
    tab = tt.Texttable()
    tab.header(titles)
    for row in endpoints:
        tab.add_row(row)

    s = tab.draw()
    print (s)
    pass 



def add(host,port,user,keyfile,name):
    """ 
    
    """
    insert_data("""
        INSERT INTO endpoints (host,port,user,keyfile,name)
        VALUES (?,?,?,?,?) 
    """,[host,port,user,keyfile,name])
    #   make sure we have all of the params to to make proper tunnels 
    #   we can make an sql insert and if error then it isnt unique but 
    #   if it is then we should be all good 
    print("added :", name)
    pass

def remove(name,id):

    #   id take precidence over name so if id then 
    #   see if there is record to delete with that id and if not then 
    #   throw an error
    pass 