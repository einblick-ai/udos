import numpy as np
def get_absolute_threshold(batch):
    """
    Transform the relative threshold in an absolute threshold

    Args:
        batch (pd.DataFrame): batch from input stream
    """
    if self._axis == 1:
        dimension = len(batch)  # columns threshold
    else:
        dimension = len(batch.columns)  # rows threshold
    self._absolute_threshold = int(dimension * self._relative_threshold)

def drop(batch: pd.DataFrame):
    """
    Drop columns or rows based on mode and absolute-threshold

    Args:
        batch (pd.DataFrame): batch from input stream

    Returns:
        preprocessed_batch (pd.DataFrame): preprocessed batch
    """
    # drop infinity and nan
    if self._drop_infinity and self._drop_nan:
        with pd.option_context("mode.use_inf_as_null", True):
            preprocessed_batch = batch.dropna(axis=self._axis,
                                                how=self._how,
                                                thresh=self._absolute_threshold)
    # drop just nans
    elif self._drop_nan:
        preprocessed_batch = batch.dropna(axis=self._axis,
                                            how=self._how,
                                            thresh=self._absolute_threshold)
    # drop just infinity
    elif self._drop_infinity:
        mask = (batch == np.infty) | (batch == -np.infty)
        keep = (mask.sum(axis=self._axis) <= self._absolute_threshold).values
        if self._axis == 1:
            preprocessed_batch = batch[keep]
        else:
            preprocessed_batch = batch.loc[keep, :]
    # dummy drop (no effect)
    else:
        preprocessed_batch = batch
    return preprocessed_batch

"""
Drop columns/rows for the input stream based on the first batch
results. For large datasets, the nan/infinity values counts
approximation provided by a first batch of 100k rows has an error
<= 0.01 with a high confidence (0.99).

Args:
    batch (pd.DataFrame): batch from the input dataframe

Returns:
    pd.DataFrame: preprocessed batch
"""

batch = df
if self._first_batch:
    get_absolute_threshold(batch)
    preprocessed_batch = drop(batch)

    # for columns save dropped columns and apply same rule on next batches
    if self._axis == 1:
        self._columns_to_keep = preprocessed_batch.columns
    self._first_batch = False
    return preprocessed_batch

# drop columns based on first batch
if self._axis == 1:
    preprocessed_batch = batch[self._columns_to_keep]
# drop rows
else:
    preprocessed_batch = drop(batch)

return preprocessed_batch
