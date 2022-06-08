import numpy as np

specified_cols = [x for x in ["year", "month", "day", "hour", "minute", "second", "microsecond", "nanosecond", "day of week"] if x in params["date columns to include"]]

for column in df[attributes['columns']].columns.tolist():
    for feature in specified_cols:
        if feature == "year":
            current_component = df[column].dt.year
        elif feature == "month":
            current_component = df[column].dt.month
        elif feature == "day":
            current_component = df[column].dt.day
        elif feature == "hour":
            current_component = df[column].dt.hour
        elif feature == "minute":
            current_component = df[column].dt.minute
        elif feature == "second":
            current_component = df[column].dt.second
        elif feature == "microsecond":
            current_component = df[column].dt.microsecond
        elif feature == "nanosecond":
            current_component = df[column].dt.nanosecond
        elif feature == "day of week":
            current_component = df[column].dt.dayofweek

        df[column + "_" + feature] = current_component
