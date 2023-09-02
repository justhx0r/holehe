#!/usr/bin/env python3
import os,requests,argparse
from random import choice

def get_exit_nodes_by_time(min_days_ago,max_days_ago):return rq.get(f'https://onionoo.torproject.org/details?search=first_seen_days:{min_days_ago}-{max_days_ago}%20running:true%20flag:exit%20flag:running%20flag:valid').json()["relays"]
def format_node_list(node_list):
    result=""
    for n in node_list:
        f=n.get('fingerprint')
        result+=f'{f},'
    return result.strip(",").strip()

def fill_node_list():
    exits=[]
    i=0
    while True:
        for node in get_exit_nodes_by_time(0,i):
            if node.get("exit_addresses"):
                for ip in node.get("exit_addresses"):
                    exits.append({"fingerprint":node.get("fingerprint"),"ip":node.get("exit_addresses"),"nickname":node.get("nickname")})
            else:
                pass
        i+=1
        if len(exits) >= argv.n:
            break

    
    return exits

def unique_node_iterator(node_list):
    seen_fingerprints = set()
    while True:
        node = choice(node_list)
        if node['fingerprint'] not in seen_fingerprints:
            seen_fingerprints.add(node['fingerprint'])
            yield node

def update_file_with_exit_nodes(file_path, content):
    if os.path.exists(file_path):
        lines = []
        with open(file_path, 'r') as file:
            lines = file.readlines()

        with open(file_path, 'w') as file:
            updated = False
            for line in lines:
                if line.strip().startswith("ExitNodes"):
                    file.write(f'ExitNodes {content}\n')
                    updated = True
                else:
                    file.write(line)
            if not updated:
                file.write(f'ExitNodes {content}\n')
    else:
        with open(file_path, 'w') as file:
            file.write(f'ExitNodes {content}\n')

if __name__ == "__main__":
    arg = argparse.ArgumentParser()
    arg.add_argument("-n", type=int, help="Number of recently registered tor exits to retrieve", default=3)
    arg.add_argument("-f", type=str, help="File to write the result to")
    argv = arg.parse_args()
    rq = requests.session()
    node_list = fill_node_list()
    
    unique_nodes = []
    node_iterator = unique_node_iterator(node_list)
    for _ in range(argv.n):
        unique_nodes.append(next(node_iterator))
    
    result = format_node_list(unique_nodes)
    
    if argv.f:
        update_file_with_exit_nodes(argv.f, result)
    else:
        print(f'ExitNodes {result}')

