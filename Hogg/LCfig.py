import numpy as np
import matplotlib.pyplot as plt
import kplr
import pyfits
client = kplr.API()

def LCfig(arg):
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

def LC(arg):
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
    return time, flux

def boxcar(arg):
    time, flux = LC(arg)
    from astropy.convolution import convolve, Box1DKernel
    num=0
    Smooth = convolve(flux[num],Box1DKernel(17))
    #plt.figure(1)
    #plt.subplot(211)
    #plt.plot(time[num],flux[num])
    #plt.subplot(212)
    #plt.plot(time[num], Smooth)
    plt.plot(time[num],flux[num])
    plt.plot(time[num],Smooth)
    return Smooth
F=[]
T=[]
time, flux=LC(500.01)

for f in flux:
    F=np.concatenate((F,f))

for t in time:
    T=np.concatenate((T,t))
from astropy.convolution import convolve, Box1DKernel
Smooth = convolve(F,Box1DKernel(16))

Fluc=F-Smooth

print Fluc[0]**2
