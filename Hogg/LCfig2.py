def RMS(arg):

    import numpy as np
    import matplotlib.pyplot as plt
    import kplr
    import pyfits
    #import pylab
    client = kplr.API()

    koi = client.koi(arg)

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
    F=flux[0]
    G = (F**2)/len(F)
    R=np.nansum(G)**.5
    print R
RMS(500.01)
