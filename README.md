# Flink/Docker/Python example

## (Optional) Choose Flink docker image
```
export FLICK_DOCKER_IMAGE_NAME=flink-alpine
```

## Start Flink cluster
Execute
```
docker-compose up
```
and check Flink Dashboard at http://localhost:8081 (or whatever ip is assigned - see `docker-machine ip`).

- Two nodes are started - JobManager & TaskManager.
- Project folder is mapped as */app/* to both nodes.


## Trigger hello_world.py Flink job
Running
```
./trigger_helloworld.sh
```
will start a Flink job that outputs "Hello World" into a timestamped file in *out* folder.

```
$ ./trigger_helloworld.sh
Starting execution of program
Program execution finished
Job with JobID af08dc721ea929cdb45cdd2f3cee949d has finished.
Job Runtime: 4542 ms

$ ls out
helloworld_1539091504.366000

$ cat out/helloworld_1539091504.366000
Hello World
```

For simplicity `pyflink-stream.sh` is triggered from within job manager node without an additional "detached launcher" node.