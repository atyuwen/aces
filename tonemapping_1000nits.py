from aceslib.tonescales import *

def input_transform(x):
    if x < 1:
        return x
    return math.exp(x - 3) + 0.8646 * x

print "Engine IDT:"
for i in range(17):
    x = i / 2.0
    y = input_transform(x)
    print " %10.5f %10.5f" %(x, y)

def tonemapping_1000nits(x):
    x = input_transform(x)
    y = segmented_spline_c5_fwd(x)
    z = segmented_spline_c9_fwd(y, ODT_1000nits)
    return z

print "   mid-gray:", tonemapping_1000nits(0.18)
print "paper-white:", tonemapping_1000nits(1.0)

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
        left: -1,
        right: 10,
        bottom: -100,
        top: 1100
    });
</script>
'''


Xs = [0.0, 0.01, 0.02, 0.04, 0.06, 0.1, 0.14, 0.18, 0.24, 0.3, 0.36, 0.42, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.25, 1.5, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 10.0]
Ys = [0.0] * len(Xs)
for i in range(len(Xs)):
    x = Xs[i]
    y = tonemapping_1000nits(x)
    Ys[i] = y

html = html.replace("$Xs$", str(Xs))
html = html.replace("$Ys$", str(Ys))
f = open("graph.html", 'w')
f.write(html)
f.close()

#import os
#os.system("explorer graph.html")

# fit this curve using a rational polynomial
import utils.rationalfit
ret = utils.rationalfit.ratfit(Xs, Ys, 2, 2)

print ret
print "(%f * x^2 + %f * x + %f) / (%f * x^2 + %f * x + %f)" % (ret[5], ret[6], ret[7], ret[2], ret[3], ret[4])


