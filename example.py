# Imports
import time
from motor import Motor

# Global settings
SLAVE_ID_1 = <REPLACE>
SLAVE_ID_2 = <REPLACE>

rightMotor = Motor(SLAVE_ID_1)
leftMotor = Motor(SLAVE_ID_2)


def main():

    rightMotor.haltMotor()
    leftMotor.haltMotor()

    print("RMCS 2303 Motor Driver")
    time.sleep(2)

    rightMotor.setSpeed(25)
    leftMotor.setSpeed(25)
    time.sleep(5)

    print("Right Motor Speed :", rightMotor.getSpeed())
    print("Right Motor Direction :", rightMotor.getDirection())
    print("Left Motor Speed :", leftMotor.getSpeed())
    print("Left Motor Direction :", leftMotor.getDirection())
    time.sleep(5)

    rightMotor.haltMotor()
    leftMotor.haltMotor()
    time.sleep(2)

    rightMotor.setSpeed(-25)
    leftMotor.setSpeed(-25)
    time.sleep(5)

    print("Right Motor Speed :", rightMotor.getSpeed())
    print("Right Motor Direction :", rightMotor.getDirection())
    print("Left Motor Speed :", leftMotor.getSpeed())
    print("Left Motor Direction :", leftMotor.getDirection())
    time.sleep(5)

    rightMotor.haltMotor()
    leftMotor.haltMotor()


if __name__ == "__main__":
    main()
