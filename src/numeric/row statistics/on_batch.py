import numpy as np
from scipy import stats

columns = df[attributes['columns']]
function = lambda x: 0
stat = params['statistic'][0]
new_column = params['output column name'] if params['output column name'] else stat

if stat == 'mean':
    function = np.mean
elif stat == 'median':
    function = np.median
elif stat == 'mode':
    function = lambda x: stats.mode(x)[0][0]
elif stat == 'max':
    function = np.amax
elif stat == 'min':
    function = np.amin


df[new_column] = columns.apply(function, axis=1)