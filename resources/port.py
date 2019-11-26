from db_utils import *
import texttable as tt
import os
def list_ports():
    """
        In this thing we will do an sqlite3 query and get all of the endpoints minus key files 

    """

    endpoints = get_data("""
        select ports.id, ports.name, target,local,remote, endpoints.name
        from ports
        inner join endpoints 
        on endpoints.id = ports.endpoint
        
        ;
    """,[])

    titles = ['id', 'name', 'target', 'local','remote','enpoint']
    tab = tt.Texttable()
    tab.header(titles)
    for row in endpoints:
        tab.add_row(row)

    s = tab.draw()
    print (s)
    pass 



def add(endpoint_name,local,remote,target,port_name):
    #   this is going to be the heaviest file since we have to do a few things 
    endpoint = get_data("""
        select id,host,port,user,keyfile from endpoints where name = ?;
    """,[endpoint_name])
    #   1. get the endpoint if it is there if not throw error
    if len(endpoint) == 0:
        print("please give an existing endpoint as an agument")
        return -1
    #   2. tempalte file with all the settings from above and get
    file_string  = ""
    file_string += "TARGET=" + endpoint[0][1] + " \n"
    file_string += "USER="+endpoint[0][1]+" \n"
    file_string += "KEYFILE="+endpoint[0][1]+"  \n"
    file_string += "FORWARD_TARGET="+target+"  \n"
    file_string += "LOCAL_PORT="+local+"  \n"
    file_string += "REMOTE_PORT="+remote+"  "
    #   3. save the file to the proper direcoty and create enable link
    file_name = "/etc/default/secure-tunnel@" + port_name
    tunnel_file = open(file_name,'w')
    tunnel_file.write(file_string)
    tunnel_file.close()
    os.system("systemctl enable secure-tunnel@" + port_name)
    #   4. create a records in the db to flag the update thing to say 
    insert_data("""
        INSERT INTO endpoints (endpoint,name,local,remote,target)
        VALUES (?,?,?,?,?) 
    """,[endpoint[0][0],port_name,local,remote,target])
    return 0

def remove(name,id):
    #   calling remove will instantly remove the file assosiated with the port
    #   as well as stop the service without the need to call the update function
    #   then it will make sure to remove the entry from the sqlite db
    pass 