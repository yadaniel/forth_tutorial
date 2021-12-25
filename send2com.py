#!/cygdrive/c/Python39/python

import sys, time, serial

# com port settings
comSettings = {
    "port" : "com23",
    "baudrate" : 115200,
    "parity" : serial.PARITY_NONE,
    "stopbits" : serial.STOPBITS_ONE,
    "bytesize" : serial.EIGHTBITS,
    "timeout" : 0.25
}

try:
    com = serial.Serial(**comSettings)
except Exception as e:
    print(f"com error => {e}")
    sys.exit()

with open(sys.argv[1]) as file:
    for line in file.readlines():
        if line.strip() == "":
            continue
        if line.strip().startswith("\ "):
            continue
        if line.strip().startswith("( "):
            continue
        com.write(bytes(line, "ascii"))
        ans = str(com.read(100), "ascii")
        print(f"send: {line}", end="")
        print(f"recv: {ans}")
        time.sleep(0.1)

com.close()

