from random import *
class Tank:
  def __init__(self, name):
    self.name = name
    self.hp = 2100
    self.reload = 1
    self.accuracy = 100
    self.wheels = 1
    self.moving = 0
    self.alive = True
  def move(self):
    if self.wheels == 1:
       print('Moving!')
       self.accuracy = 30
       self.moving = 1
    else:
      print('Repairing!')
      self.wheels = 1
  def stop(self):
    if self.moving == 1:
      print('We stopped!')
      self.accuracy = 100
      self.moving = 0
    else:
      print('Not moving!')
  def shoot(self):
    if self.reload == 1:
      print('Boom!')
      self.reload=0
    else:
      print('Reloading!')
      self.reload = 1
  def got_shot(self):
    print('We got Shot!')
    self.hp -= 100
  def broke_wheels(self):
    print('We cannot move anymore!')
    self.wheels = 0
  def is_alive(self):
    if self.hp == 0:
      print('You are Dead!')
      self.alive = False
  def statistics(self):
    print('HP =  ', self.hp, ' Moving = ', self.moving)
  def action(self, move):
    act = 'Step ' + str(move)
    print(act)
    action = randint(1,5)
    if action == 1:
      self.move()
    elif action == 2:
      self.stop()
    elif action == 3:
      self.shoot()
    elif action == 4:
      self.got_shot()
    elif action == 5:
      self.broke_wheels()
    self.statistics()
    self.is_alive()
tank = Tank("Tiger")
for move in range(100):
	if tank.alive == False:
		break
	tank.action(move)
    