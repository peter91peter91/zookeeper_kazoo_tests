# zookeeper_kazoo_tests

1.1)стартуем зукипер
```
docker pull zookeeper:3.8.2
docker run --name ZK382 -t -i zookeeper:3.8.2
```
у меня он при такой установке стартовал на айпи 172.17.0.3:2181   (если будет другой,то в скрипте подменить)

1.2)это-только если хотим проверить что подключается клиент к зукиперу.
```sudo docker run -it --rm --link ZK382:zookeeper zookeeper zkCli.sh -server zookeeper```

2)стартуем зунавигатор ,чтобы проще было посмотреть на то как исчезает узел эфимерный(разрегистрируется сервис)
```
docker run \
  -d --network host \
  -e HTTP_PORT=9999 \
  --name zoonavigator \
  --restart unless-stopped \
  elkozmon/zoonavigator:latest
```

3)ставим PIP на python2
```
sudo apt install python2
curl https://bootstrap.pypa.io/pip/2.7/get-pip.py -o get-pip.py
python get-pip.py
pip install zc.zk
```

4)запускаем мой скрипт подключения,создания древа и  регистрации  сервиса, к примеру, портейнера http://127.0.0.1:9000/
+++скрипт с исключениями,проверками
```
python2 kazoo_register_0.py
```

        совсем сухой скрипт 
     ```python2 kazoo_register_0_short.py```

5)смотрим как в зукипере http://localhost:9999/   появляется  
и спустя 5сек удаляется узел со свежевыданным PID "процесса слежения" внутри {"pid":26303}

```.....Error: KeeperErrorCode = NoNode for /service_mois_portainer/local_portainer/172.17.0.3:2181:9000```
