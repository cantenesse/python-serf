import subprocess

def event(name, payload, coalese='true', rpcaddr='127.0.0.1'):
    print name, payload, coalese, rpcaddr
    subprocess.call(['serf', 'event', '-coalese=', coalese,
                     '-rpc-addr=', rpcaddr, name, payload])
