```python
import numpy as np
import threading
import time

# CPUni maksimal ishlatish uchun kod
def cpu_max():
    while True:
        _ = np.random.rand(1000, 1000)  # CPUga yuklash

# GPUni maksimal ishlatish uchun kod (agar CUDA mavjud bo'lsa)
import tensorflow as tf
def gpu_max():
    while True:
        tf.random.normal([1000, 1000])  # GPUga yuklash

# CPUni maksimal ishlatish uchun 4 ta thread ishga tushurish
for _ in range(4):
    threading.Thread(target=cpu_max, daemon=True).start()

# GPUni maksimal ishlatish (agar GPU mavjud bo'lsa)
gpu_max()

# 10 daqiqa davomida ishlashini kutish
time.sleep(600)
