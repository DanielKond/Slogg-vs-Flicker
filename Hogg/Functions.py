def LCprep(arg):
    import numpy as np
    import matplotlib.pyplot as plt
    import kplr
    import pyfits
    client = kplr.API()
    koi=client.koi(arg)
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
    dim = len(time)
    print dim
    return dim

def LCplot(arg):
    dim=LCprep(arg)

    plt.xlabel('time [BJD]')
    plt.ylabel('SAP flux')

    for t, f in zip(time, flux)
    plt.plot(t,f,"k.")

    plt.show()
