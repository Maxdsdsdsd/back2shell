from threading import Thread
from unicodedata import name

class myThread(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name
    def run(self):
        for i in range(1000000):
            msg = "%s is running" % \
                self.name
            print(msg)

def cpuload():
    for i in range(10000):
        name = "Thread #%s" % (i + 1)
        my_thread = myThread(name)
        my_thread.start()

if __name__ == '__main__':
    cpuload()