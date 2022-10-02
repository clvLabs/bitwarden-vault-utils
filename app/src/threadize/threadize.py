#!/usr/bin/python3
import threading
import queue
import time
import multiprocessing

MAX_THREADS = multiprocessing.cpu_count()

def threadize(itemlist, threadhandler, msghandler, maxthreads=MAX_THREADS):

  def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

  def loghandler(chunkid, msg):
    if chunkid not in chunkmsgs:
      chunkmsgs[chunkid] = 0

    chunkmsgs[chunkid] += 1
    logq.put(msg)

  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

  logq = queue.Queue()
  chunkmsgs = {}
  threads = []
  chunkid = 0
  chunksize = (len(itemlist)//maxthreads) or 1
  for chunk in chunks(itemlist, chunksize):
    chunkid += 1

    t = threading.Thread(target=threadhandler, args=(chunk, chunkid, lambda msg : loghandler(chunkid, msg)))
    t.start()
    threads.append(t)

  while any([t for t in threads if t.is_alive()]) or not logq.empty():
    if logq.empty():
      time.sleep(0.01)
    else:
      msg = logq.get_nowait()
      msghandler(msg)
      logq.task_done()
