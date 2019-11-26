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
def main():
    # parse the first arg there to see what you need to do  
    parser = argparse.ArgumentParser(description='Process some integers.')
    # first we can add the resource and action thing to let us know whats up 
    parser.add_argument('resource', help='foo help',nargs='?', type=str)
    parser.add_argument('action', help='foo help',nargs='?', type=str)

    # here is where we put all the optional things 
    parser.add_argument('--host', help='the host of the server you want to forward traffic from.')
    parser.add_argument('--port', help='The port used to ssh to host , default is 22')
    parser.add_argument('--user', help='The user that will be used to connect to the host')
    parser.add_argument('--keyfile', help='The ssh key file for the user.')
    parser.add_argument('--name', help='string name for the created resoruce')
    parser.add_argument('--to', help='the port you want to accept traffic from on the host')
    parser.add_argument('--from', help='the port you want to forward it to')
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
            endpoint.add()
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
            port.add()
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