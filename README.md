# ACES

Play with ACES tone mapping in Python.

- Following is the ACES 1000 nits tone mapping. (Genreated via aces_tonescale_1000nits.py)

<script src="https://www.desmos.com/api/v1.3/calculator.js?apiKey=dcb31709b452b1cf9dc26972add0fda6"></script>
<div id="calculator" style="width: 800px; height: 400px;"></div>
<script>
    var elt = document.getElementById('calculator');
    var calculator = Desmos.GraphingCalculator(elt);
    calculator.setExpression({
        type: 'table',
        columns: [
            {
                latex: 'x',
                values: [-12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
            },
            {
                latex: 'y',
                values: [0.0001, 0.00015685846572065964, 0.00039912254812403164, 0.0011397153083418776, 0.003220443953498406, 0.008821547574794916, 0.023146674657765477, 0.057039114089735804, 0.15369089445472542, 0.4569082861571723, 1.3154293975284082, 3.6906752090985875, 10.0, 25.235506932510315, 59.306497687955535, 127.78788536400916, 247.46275489838948, 422.1791055932963, 608.4176737333613, 772.8219909761671, 894.9502115712964, 967.594741705806, 1000.0, 1014.9784059980663],
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



