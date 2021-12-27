#!/cygdrive/c/Python39/python

import sys, time, serial
import re

comment1 = re.compile(r"\\\s.*?$")
comment2 = re.compile(r"[(]\s.*?[)]")

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

cnt = 1
with open(sys.argv[1]) as file:
    for line in file.readlines():

        if comment1.search(line):
            line = comment1.sub("", line)
            # print("COMMENT1 MATCHED: ", line)

        if comment2.search(line):
            line = comment2.sub("", line)
            # print("COMMENT2 MATCHED: ", line)

        if line.strip() == "":
            continue

        # debug
        # print(line)
        # continue

        # if line.strip().startswith("\ "):
        #     continue
        # if line.strip().startswith("( "):
        #     continue

        com.write(bytes(line, "ascii"))
        ans = str(com.read(100), "ascii")
        print(f"[{cnt:4}] send: {line}", end="")
        print(f"[{cnt:4}] recv: {ans}")
        time.sleep(0.1)
        cnt += 1

com.close()

