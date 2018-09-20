## json save to file

A trivial python example, listening to the json stream, and saving a given variable to a logfile.

## Requirements
You need 'paho-mqtt'.

  $ python3 -m venv .env3
  $ . .env3/bin/activate
  $ pip install paho-mqtt


## example output

```
$ python simple-json-log.py -H 192.168.1.163 --file blah -d E643E5EE2391 -p 'volt/1'
Found matching parameter: 2018-09-20 15:27:49.545000 235.959000
Found matching parameter: 2018-09-20 15:27:51.560000 235.726000
Found matching parameter: 2018-09-20 15:27:53.593000 235.853000
Found matching parameter: 2018-09-20 15:27:55.623000 235.957000
Found matching parameter: 2018-09-20 15:27:57.624000 236.129000
^CTraceback (most recent call last):
  File "simple-json-log.py", line 47, in <module>
    domain()
  File "simple-json-log.py", line 44, in domain
    client.loop_forever()
  File "/home/karlp/src/integration-examples/python-json-file/.env3/lib64/python3.6/site-packages/paho/mqtt/client.py", line 1578, in loop_forever
    rc = self.loop(timeout, max_packets)
  File "/home/karlp/src/integration-examples/python-json-file/.env3/lib64/python3.6/site-packages/paho/mqtt/client.py", line 1057, in loop
    socklist = select.select(rlist, wlist, [], timeout)
KeyboardInterrupt
$ cat blah
2018-09-20 15:27:49.545000;235.959000
2018-09-20 15:27:51.560000;235.726000
2018-09-20 15:27:53.593000;235.853000
2018-09-20 15:27:55.623000;235.957000
2018-09-20 15:27:57.624000;236.129000
```
