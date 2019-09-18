from aceslib.tonescales import *

def aces_tonescale_1000nits(x):
    y = segmented_spline_c5_fwd(x)
    z = segmented_spline_c9_fwd(y, ODT_1000nits)
    return z

print "   mid-gray:", aces_tonescale_1000nits(0.18)
print "paper-white:", aces_tonescale_1000nits(1.0)
print "    mapping:"
for i in range(24):
    x = 0.18 * pow(2, i - 12)
    y = aces_tonescale_1000nits(x)
    print " %10.5f %10.5f" %(x, y)

# Plot the mapping via desmos.
html = '''
<script src="https://www.desmos.com/api/v1.3/calculator.js?apiKey=dcb31709b452b1cf9dc26972add0fda6"></script>
<div id="calculator"></div>
<script>
    var elt = document.getElementById('calculator');
    var calculator = Desmos.GraphingCalculator(elt);
    calculator.setExpression({
        type: 'table',
        columns: [
            {
                latex: 'x',
                values: $Xs$
            },
            {
                latex: 'y',
                values: $Ys$,
                columnMode: Desmos.ColumnModes.POINTS_AND_LINES
            }
        ]
    });
    calculator.setMathBounds({
        left: -13,
        right: 13,
        bottom: -100,
        top: 1100
    });
</script>
'''

Xs = [i - 12 for i in range(24)]
Ys = [0.0] * 24
for i in range(24):
    x = 0.18 * pow(2, Xs[i])
    y = aces_tonescale_1000nits(x)
    Ys[i] = y

html = html.replace("$Xs$", str(Xs))
html = html.replace("$Ys$", str(Ys))
f = open("graph.html", 'w')
f.write(html)
f.close()

import os
os.system("explorer graph.html")

