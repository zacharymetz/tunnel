"""
Tunnel 0.1

usage 

tunnel endpoint list

tunnel endpoint add <host> <port> <user> <keyfile> <name>

tunnel endpoint rm <name | id>

tunnel port list

tunnel port add <endpoint> <from> <to> <name>

tunnel port rm <name | id>

tunnel update  //   this will go and see what needs to be restarted and what no 

"""
import argparse
from resources import endpoint, port
import db_utils
def main():


    #   before any parsing happens we should make sure a db 
    #   exists and if not we create it, this function will do that 
    db_utils.check_db_integrety()

    # parse the first arg there to see what you need to do  
    parser = argparse.ArgumentParser(description='Process some integers.')
    # first we can add the resource and action thing to let us know whats up 
    parser.add_argument('resource', help='endpoint | port | update',nargs='?', type=str)
    parser.add_argument('action', help='list | add | rm',nargs='?', type=str)

    # here is where we put all the optional things 
    parser.add_argument('--host', help='the host of the server you want to forward traffic from.')
    parser.add_argument('--port', help='The port used to ssh to host , default is 22')
    parser.add_argument('--user', help='The user that will be used to connect to the host')
    parser.add_argument('--keyfile', help='The ssh key file for the user.')
    parser.add_argument('--name', help='string name for the created resoruce')
    parser.add_argument('--local', help='the port you want to accept traffic from on the host')
    parser.add_argument('--remote', help='the port you want to forward it to')
    parser.add_argument('--target', help='the ip of where you want the traffice forwarded too')
    parser.add_argument('--endpoint', help='the name of the endpoint you want the tunnel traffic from')
    args = parser.parse_args()
    # this is the inial switch for what gets run when we call the function 
    
    if args.resource == 'update':
        #   we dont care about the action or any args here 
        #   so we will just call the function that will preform all of the 
        #   nessisary restarts 
        pass 
    elif args.resource == 'endpoint':
        #   now in endpoint we have list, add and remove
        if args.action == 'list':
            endpoint.list_endpoints()
            pass 
        elif args.action == 'add':
            endpoint.add(args.host,args.port,args.user,args.keyfile,args.name)
            pass
        elif args.action == 'rm':
            endpoint.remove()
            pass
        else:
            print("ERROR, please enter a valid action for resource:endpoint.")
            return -1
        
    elif args.resource == 'port':
        #   now in endpoint we have list, add and remove
        if args.action == 'list':
            port.list_ports()
            pass 
        elif args.action == 'add':
            port.add(args.endpoint,args.local,args.remote,args.target,args.name)
            pass
        elif args.action == 'rm':
            port.remove()
            pass
        else:
            print("ERROR, please enter a valid action for resource:port.")
            return -1
        
    else:
        print("ERROR, please enter a valid resource.")
        return -1
  
    
    
    pass 


if __name__ == "__main__":
    main()