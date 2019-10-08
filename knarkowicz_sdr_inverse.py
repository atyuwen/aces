# Fit a curve to invert Knarkowicz ACES tone mapping (SDR).

def ACES_Knarkowicz(x):
	a = 2.51
	b = 0.03
	c = 2.43
	d = 0.59
	s = 0.14
	return (x * ( a * x + b)) / (x * (c * x + d) + s)

def ACES_Knarkowicz_inverse(x):
	"find the inverse by a simple binary search."
	a = 0.0
	b = 20.0
	while b - a > 0.0001:
		m = (a + b) / 2
		v = ACES_Knarkowicz(m)
		if v < x:
			a = m
		else:
			b = m
	return a

t0 = ACES_Knarkowicz(20)
t1 = ACES_Knarkowicz_inverse(t0)
t2 = ACES_Knarkowicz_inverse(1.0)
print t0, t1, t2

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
        left: -0.1,
        right: 1.2,
        bottom: -1,
        top: 12
    });
</script>
'''

N = 256
Xs = [i / float(N - 1) for i in range(N)]

Ys = [0.0] * len(Xs)
for i in range(len(Xs)):
    x = Xs[i]
    y = ACES_Knarkowicz_inverse(x) / max(x, 0.0001)
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
print "(%f * x^2 + %f * x + %f) * x / (%f * x^2 + %f * x + %f)" % (ret[5], ret[6], ret[7], ret[2], ret[3], ret[4])

def fitted_curve(x):
	return float(ret[5] * x * x + ret[6] * x + ret[7]) / (ret[2] * x * x + ret[3] * x + ret[4])

max_error = 0.0
for i in range(260):
    x = i / 255.0
    y0 = ACES_Knarkowicz_inverse(x)
    y1 = fitted_curve(x) * x
    error = abs(y0 - y1)
    print "x %f y0 %f y1 %f err: %f" % (x, y0, y1, error)
    max_error = max(max_error, abs(y0 - y1))

print "max error: ", max_error

