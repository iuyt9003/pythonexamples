# Synchronizing Threads

#In addition to using Events, another way of synchronizing threads is through using a Condition object.
# Because the Condition uses a Lock, it can be tied to a shared resource.
# This allows threads to wait for the resource to be updated.
# In this example, the consumer() threads wait() for the Condition to be set before continuing.
# The producer() thread is responsible for setting the condition and notifying the other threads that they can continue.

import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s (%(threadName)-2s) %(message)s',
                    )

def consumer(cond):
    """wait for the condition and use the resource"""
    logging.debug('Starting consumer thread')
    t = threading.currentThread()
    with cond:
        cond.wait()
        logging.debug('Resource is available to consumer')

def producer(cond):
    """set up the resource to be used by the consumer"""
    logging.debug('Starting producer thread')
    with cond:
        logging.debug('Making resource available')
        cond.notifyAll()

condition = threading.Condition()
c1 = threading.Thread(name='c1', target=consumer, args=(condition,))
c2 = threading.Thread(name='c2', target=consumer, args=(condition,))
p = threading.Thread(name='p', target=producer, args=(condition,))

c1.start()
time.sleep(2)
c2.start()
time.sleep(2)
p.start()

# #The threads use with to acquire the lock associated with the Condition. Using the acquire() and release() methods explicitly also works.
#
# 2013-02-21 06:37:49,549 (c1) Starting consumer thread
# 2013-02-21 06:37:51,550 (c2) Starting consumer thread
# 2013-02-21 06:37:53,551 (p ) Starting producer thread
# 2013-02-21 06:37:53,552 (p ) Making resource available
# 2013-02-21 06:37:53,552 (c2) Resource is available to consumer
# 2013-02-21 06:37:53,553 (c1) Resource is available to consumer

