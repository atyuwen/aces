from aceslib.tonescales import *

def aces_tonescale_1000nits(x):
    y = segmented_spline_c5_fwd(x)
    z = segmented_spline_c9_fwd(y, ODT_1000nits)
    return z

print "   mid-gray:", aces_tonescale_1000nits(0.18)
print "paper-white:", aces_tonescale_1000nits(1.0)
print "      curve:"
for i in range(24):
    x = 0.18 * pow(2, i - 12)
    y = aces_tonescale_1000nits(x)
    print " %10.5f %10.5f" %(x, y)


