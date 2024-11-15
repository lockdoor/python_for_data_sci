from time import gmtime, strftime, time

if __name__ == '__main__':
    t = time()
    print ('Seconds since ', end="")
    print (strftime("%B %Y,", gmtime(0)), int(strftime("%d", gmtime(0))), end="")
    print (f': {t:,.4f} or {t:.2e} in scientific notation')
    print (strftime("%b %d %Y", gmtime()))
