import threading
import random
import math
import time

N = int(input("Nhập số phần tử của mảng (N): "))
K = int(input("Nhập số luồng xử lý (K): "))

A = [random.randint(0, 1000) for _ in range(N)]
partial_counts = [0] * K

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def count_primes(thread_id, start, end):
    count = 0
    for i in range(start, end):
        if is_prime(A[i]):
            count += 1
    partial_counts[thread_id] = count
    print(f"T{thread_id + 1}: Kết quả trung gian -> {count} số nguyên tố - Thời gian: {time.strftime('%H:%M:%S')}")

threads = []
segment = N // K
for i in range(K):
    start = i * segment
    end = (i + 1) * segment if i < K - 1 else N  
    t = threading.Thread(target=count_primes, args=(i, start, end))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

total = sum(partial_counts)
print(f"\n== KẾT QUẢ CUỐI CÙNG: Tổng số nguyên tố trong mảng = {total}")
