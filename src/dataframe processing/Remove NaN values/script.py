import numpy as np

axis = 1 if params["axis"][0] == "drop columns" else 0
relative_threshold = float(params["min % valid values"]) / 100
drop_nan = params["drop NaN"]
drop_infinity = params["drop infinity"]

def get_absolute_threshold(batch):
    """
    Transform the relative threshold in an absolute threshold

    Args:
        batch (pd.DataFrame): batch from input stream
    """
    dimension = len(batch) if axis == 1 else len(batch.columns)
    return int(dimension * relative_threshold)

def drop(batch: pd.DataFrame, abs_threshold: int):
    """
    Drop columns or rows based on mode and absolute-threshold

    Args:
        batch (pd.DataFrame): batch from input stream

    Returns:
        preprocessed_batch (pd.DataFrame): preprocessed batch
    """
    if drop_infinity and drop_nan:
        with pd.option_context("mode.use_inf_as_null", True):
            return batch.dropna(axis=axis, thresh=abs_threshold)
    elif drop_nan:
        return batch.dropna(axis=axis, thresh=abs_threshold)
    elif drop_infinity:
        mask = (batch == np.infty) | (batch == -np.infty)
        keep = (mask.sum(axis=axis) <= abs_threshold).values
        return batch[keep] if axis == 1 else batch.loc[keep, :]
    else:
        return batch

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
first_batch = True
columns_to_keep = None
absolute_threshold = None

for dfs in self.from_input(0):
    for batch in dfs:
        if first_batch:
            absolute_threshold = get_absolute_threshold(batch)
            preprocessed_batch = drop(batch, absolute_threshold)

            # for columns, save dropped columns and apply the same rule on future batches
            if axis == 1:
                columns_to_keep = preprocessed_batch.columns
            first_batch = False
            yield preprocessed_batch
        else:
            yield batch[columns_to_keep] if axis == 1 else drop(batch, absolute_threshold)
