from sklearn.cluster import MiniBatchKMeans
from sklearn.preprocessing import normalize
import numpy as np

kmeans = MiniBatchKMeans(n_clusters=params["Number of clusters"])

for dfs in self.from_input(0):
    for df in dfs:
        processed = normalize(df[attributes["Features"]])
        kmeans.partial_fit(processed)
        df.insert(0, params['Output column name'], kmeans.predict(processed) + 1)
        yield df