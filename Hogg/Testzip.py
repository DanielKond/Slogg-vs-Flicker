def LCfig(arg):
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
    if len(time)<5:
        dim = len(time)
    else:
        dim = 5
    print len(time)
    plt.xlabel('time [BJD]')
    plt.ylabel('SAP flux')


    plt.figure(1)

    for i in range(0,dim):
        plt.subplot(dim,1,i+1)
        plt.plot(time[i],flux[i],"k.")

    plt.show()

LCfig(100.01)
