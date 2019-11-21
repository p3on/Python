from Queue import Queue
from threading import Thread

def function2Call(inputQueue, outputQueue):
  print('threadwork')


def main():
  ### define queues for threadsave processing (atomic)
  q_in = Queue(maxsize = 0)
	q_out = Queue(maxsize = 0)

	### block for threading (progressbar + 98 threads that do the work)
	threads = []

	for i in range(99):
		if i == 1:
			runThread = Thread(target=progress, args=(q_in,))
			threads += [runThread]
			runThread.setDaemon(True)
			runThread.start()
		runThread = Thread(target=function2Call, args=(q_in, q_out,))
		threads += [runThread]
		runThread.setDaemon(True)
		try:
			runThread.start()
		except (KeyboardInterrupt, SystemExit):
			cleanup_stop_thread()

  ### locks until all items from the queue have been processed
  q_in.join() 
