import pandas as pd

dfs = []
for df in self.from_input(0).flatten():
    dfs.append(df)

df = pd.concat(dfs, axis=0)

from sklearn.preprocessing import OneHotEncoder

# Enable commented code once upgrading to sklearn 1.1 where it is supported

if params['Drop method'] == "None":
    drop_method = None
if params['Drop method'] == "Drop first category":
    drop_method = "first"
# if params['Drop method'] == "Drop only for binary columns":
#     drop_method = "if_binary"

if params['Handle unknown method'] == "Ignore":
    handle_unknown = "ignore"
elif params['Handle unknown method'] == "Error":
    handle_unknown = "error"
# elif params['Handle unknown method'] == "Mark as infrequent":
#     handle_unknown = "infrequent_if_exist"

# min_frequency = params['Minimum frequency'] if params['Minimum frequency'] > 0 else None
# max_categories = params['Maximum categories'] if params['Maximum categories'] > 0 else None

encoder = OneHotEncoder(categories='auto',
                        sparse=False,
                        drop=drop_method,
                        handle_unknown=handle_unknown,
                        # min_frequency=min_frequency,
                        # max_categories=max_categories
                        )

encoder.fit(df[attributes['Columns']])

self.save_state(encoder)

result = pd.DataFrame(encoder.transform(df[attributes['Columns']]), columns=encoder.get_feature_names(attributes['Columns']))
if not params['Keep original columns']:
    df = df.drop(attributes['Columns'], axis=1)
yield pd.concat([df.reset_index(drop=True), result], axis=1)
