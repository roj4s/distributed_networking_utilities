import zmq
import random
import sys
import time
from distributed_networking_utilities.zmq_exchange import send_array
import numpy as np

port = "5556"
context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.connect("tcp://localhost:%s" % port)

while True:
    n1 = 1000
    n2 = 512

    print("Creating random array with shape = ({}, {})".format(n1, n2))
    t = time.time()
    r = np.random.random((n1, n2))
    t = time.time() - t
    print("Created in {:.2f} secs.".format(t))
    print("Sending array")
    t = time.time()
    send_array(socket, r, t)
    t = time.time() - t
    print("Sent in {:.2f} secs.".format(t))
    time.sleep(1)
