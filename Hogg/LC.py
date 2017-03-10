

import numpy as np
import matplotlib.pyplot as plt
import kplr
import pyfits
client = kplr.API()

koi = client.koi(952.01)
lcs = koi.get_light_curves(short_cadence=False)
time, flux, ferr, quality = [], [], [], []
for lc in lcs:
    with lc.open() as f:
        # The lightcurve data are in the first FITS HDU.
        hdu_data = f[1].data
        time.append(hdu_data["time"])
        flux.append(hdu_data["sap_flux"])
        ferr.append(hdu_data["sap_flux_err"])
        quality.append(hdu_data["sap_quality"])

plt.plot(time[0], flux[0])
plt.show()
