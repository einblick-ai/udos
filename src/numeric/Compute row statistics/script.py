import numpy as np
from scipy import stats

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


ds = self.from_input(0)

for dfs in ds:
    for df in dfs:
        df[new_column] = df[attributes['columns']].apply(function, axis=1)
        yield df