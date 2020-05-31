import logging
logaccelerate = logging.basicConfig(filename="textlog.log", level=logging.INFO)
logaccelerate = logaccelerate = logging.info('You accelerated')
logaccelerate = logging.error('no error')
logaccelerate = logging.debug('your text goes here')

logbrake = logging.basicConfig(filename="textlog.log", level=logging.INFO)
logbrake = logaccelerate = logging.info('You braked')
logbrake = logging.error('no error')
logbrake = logging.debug('your text goes here')

logodometer = logging.basicConfig(filename="textlog.log", level=logging.INFO)
logodometer = logaccelerate = logging.info('Odometer')
logodometer = logging.error('no error')
logodometer = logging.debug('your text goes here')

logspeed = logging.basicConfig(filename="textlog.log", level=logging.INFO)
logspeed = logaccelerate = logging.info('You saw your average speed')
logspeed = logging.error('no error')
logspeed = logging.debug('your text goes here')

logerror = logging.basicConfig(filename="textlog.log", level=logging.INFO)
logerror = logaccelerate = logging.info('You intered invalid characters')
logerror = logging.error('ERR_INVALID_CHAR')
logerror = logging.debug('your text goes here')

class Car:

    def __init__(self, speed=0):
        self.speed = speed
        self.odometer = 0
        self.time = 0

    def say_state(self):
        print("I'm going {} kph!".format(self.speed))

    def accelerate(self):
        self.speed += 5
        logaccelerate

    def brake(self):
        self.speed -= 5
        logbrake

    def step(self):
        self.odometer += self.speed
        self.time += 1
        logodometer

    def average_speed(self):
        if self.time != 0:
            return self.odometer / self.time
            logspeed
        else:
            pass

if __name__ == '__main__':

    my_car = Car()
    print("I'm a car!")
    while True:
        action = input("What should I do? [A]ccelerate, [B]rake, "
                 "show [O]dometer, or show average [S]peed?").upper()
        if action not in "ABOS" or len(action) != 1:
            print("I don't know how to do that")
            continue
        if action == 'A':
            my_car.accelerate()
        elif action == 'B':
            my_car.brake()
        elif action == 'O':
            print("The car has driven {} kilometers".format(my_car.odometer))
        elif action == 'S':
            print("The car's average speed was {} kph".format(my_car.average_speed()))
        my_car.step()
        my_car.say_state()
