import time

start = time.time()
for i in range(100):
    pass
end = time.time()
print("ONE LOOP ",end-start)

start = time.time()
for i in range(100):
    for j in range(100):
        pass
end = time.time()
print("TWO LOOP ",end-start)

start = time.time()
for i in range(100):
    for j in range(100):
        for k in range(100):
            pass
end = time.time()
print("THREE LOOP ",end-start)