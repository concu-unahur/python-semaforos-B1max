
import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

comensales = 23
platos = 3
platosDisponibles = platos

class Cocinero(threading.Thread):
  def __init__(self):
    super().__init__()
    self.name = 'Cocinero'

  def run(self):
    global platosDisponibles
    global comensales
    global platos
    while (True):
      # print('while cocinero')
      if(platosDisponibles==0):
        # print('acquire cocinero')
        cocinero.release()
        cocinero.acquire()
        try:
          platosDisponibles = platos
          logging.info('Reponiendo los platos...')
        finally:
          comensal.release()
      else:
        comensal.release()

class Comensal(threading.Thread):
  def __init__(self, numero):
    super().__init__()
    self.name = f'Comensal {numero}'

  def run(self):
    global platosDisponibles
    comensal.acquire()
    if(platosDisponibles>0):
      try:
        platosDisponibles -= 1
        logging.info(f'¡Qué rico! Quedan {platosDisponibles} platos')
      finally:
        comensal.release()

comensal = threading.Semaphore(platos)
cocinero = threading.Semaphore(1)
Cocinero().start()

for i in range(comensales):
  Comensal(i).start()
