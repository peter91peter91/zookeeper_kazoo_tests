import zc.zk
from kazoo.client import KazooClient
ip_var='172.17.0.3:2181'
zk = KazooClient(hosts=ip_var)
zk.start()
zk.ensure_path("/service_mois_portainer")
zk.create("/service_mois_portainer/local_portainer", b"a value")
registration = zc.zk.ZooKeeper(ip_var)
registration.register_server('/service_mois_portainer/local_portainer', (ip_var, 9000))
zk.stop()