#By default, join() blocks indefinitely. It is also possible to pass a timeout argument (a float representing the number of seconds to wait for the thread to become inactive).
# If the thread does not complete within the timeout period, join() returns anyway.
import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )

def daemon():
    logging.debug('Starting')
    time.sleep(2)
    logging.debug('Exiting')

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

def non_daemon():
    logging.debug('Starting')
    logging.debug('Exiting')

t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()

d.join(1)
#Since the timeout passed is less than the amount of time the daemon thread sleeps, the thread is still “alive” after join() returns.
print ('d.isAlive()', d.isAlive())
t.join()

# (daemon    ) Starting
# (non-daemon) Starting
# (non-daemon) Exiting
# d.isAlive() True