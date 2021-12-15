# 0, or ‘index’ : Drop rows which contain missing values.
# 1, or ‘columns’ : Drop columns which contain missing value

self._axis = 1 if params["axis"] == "drop columns" else 0


# set how field
if params["min % valid values"] == 100:
    self._how = "all"
else:
    self._how = "any"

self._relative_threshold = float(params["min % valid values"]) / 100
self._drop_nan = params["drop nan"]
self._drop_infinity = params["drop infinity"]
self._first_batch = True
self._columns_to_keep = None
