a= 3-1
print(id(a),a)
import time

t0 = time.time()
for i in range (100001):
    print(i, "starts")
    t1 = time.time()
    print(t1-t0, "ends ")