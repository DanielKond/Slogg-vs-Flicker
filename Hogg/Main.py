import numpy as np
import matplotlib.pyplot as plt
import kplr
client = kplr.API()

koi = client.koi(954.01)
print koi.koi_period
