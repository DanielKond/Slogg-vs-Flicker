import kplr
client = kplr.API()

kois = client.kois(where="teff>200")
print len(kois)
