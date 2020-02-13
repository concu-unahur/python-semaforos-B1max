
import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

comensales = 23
platos = 6

class Cocinero(threading.Thread):
  def __init__(self):
    super().__init__()
    self.name = 'Cocinero'

  def run(self):
    global platosDisponibles
    global comensales
    global platos
    while (True):
      for i in range(platos):
        comensal.release()
      time.sleep(0.25)
      cocinero.acquire()
      platosDisponibles = platos
      logging.info('Reponiendo los platos...')


class Comensal(threading.Thread):
  def __init__(self, numero):
    super().__init__()
    self.name = f'Comensal {numero}'

  def run(self):
    global platosDisponibles
    comensal.acquire()
    platosDisponibles -= 1
    logging.info(f'¡Qué rico! Quedan {platosDisponibles} platos')

platosDisponibles = platos
comensal = threading.Semaphore(0)
cocinero = threading.Semaphore(round((comensales/platosDisponibles))-1)
Cocinero().start()

for i in range(comensales):
  Comensal(i).start()
