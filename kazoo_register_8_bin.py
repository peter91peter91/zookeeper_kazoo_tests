import logging
from datetime import datetime

logging.basicConfig()

from time import sleep
from kazoo.exceptions import NodeExistsError
from kazoo.client import KazooClient
import zc.zk

# COMMENTS ONLY IN ENGLISH!!!

# connecting to zookeeper
zk = KazooClient(hosts='172.17.0.3:2181')
zk.start()

# Ensure a path, create if necessary
zk.ensure_path("/service_mois_portainer3")

########################################################################################
def register(client):
    while True:
        if client.state == 'CONNECTED':
            try:
                client.create('/service_mois_portainer3/portainer3', ephemeral=False, makepath=True)
            except NodeExistsError:
                pass
            try:

                client.register_server('/service_mois_portainer3/portainer3', ('172.17.0.3:2181', 9000))
                break
            except NodeExistsError:
                print('waiting for registration...')
                sleep(0.5)
        else:
            print('zookeeper host is down, reconnecting...')
            sleep(0.5)

# register service
portainer_registration = zc.zk.ZooKeeper('172.17.0.3:2181', session_timeout=5, wait=True)
register(portainer_registration)

#show state in console
current_datetime = datetime.now()
ttt = str(current_datetime)
print(ttt +"portainer3"+  portainer_registration.state)


###########
zk.stop()
