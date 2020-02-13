import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

class Cocinero(threading.Thread):
  def __init__(self):
    super().__init__()
    self.name = 'Cocinero'

  def run(self):
    global platosDisponibles
    while (True):
      semaforo.acquire()
      platosDisponibles = 3
      logging.info('Reponiendo los platos...')
      semaforoComensal.release()#libero un plato

class Comensal(threading.Thread):
  def __init__(self, numero):
    super().__init__()
    self.name = f'Comensal {numero}'

  def run(self):
    global platosDisponibles
    semaforoComensal.acquire()
    platosDisponibles -= 1
    logging.info(f'¡Qué rico! Quedan {platosDisponibles} platos')
    semaforo.release()

semaforoComensal = threading.Semaphore(4)
semaforo = threading.Semaphore(0)
platosDisponibles = 3


Cocinero().start()

for i in range(15):
  Comensal(i).start()