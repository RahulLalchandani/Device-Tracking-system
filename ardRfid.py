import serial

ser = serial.Serial('COM3', 9600)


def run():
    return ser.readline()


if __name__ == "__main__":
    while True:
        print(run())

# b'Tap card key: DD:99:50:43\r\n' is id1 in lab1
# b'Tap card key: 31:9D:AC:C3\r\n' is id2 in lab2
