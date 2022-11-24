import time as t

print("Printed immediately")
t.sleep(5)
print("Printed after 5 seconds")


while True:
    localtime =t.localtime()
    result =t.strftime("%I:%M:%S %p", localtime)
    # print(result)
    print(result, end="", flush=True)
    print("\r", end="", flush=True)
    t.sleep(1)