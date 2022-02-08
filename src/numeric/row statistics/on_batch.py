import numpy as np
from scipy import stats

columns = df[attributes['columns']]
function = lambda x: 0
new_column = params['column name'] if params['column name'] else params['statistic'] 

if params['statistic'] == 'mean':
    function = np.mean
elif params['statistic'] == 'median':
    function = np.median
elif params['statistic'] == 'mode':
    function = lambda x: stats.mode(x)[0][0]
elif params['statistic'] == 'max':
    function = np.amax
elif params['statistic'] == 'min':
    function = np.amin


df[new_column] = columns.apply(function, axis=1)