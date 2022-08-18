batch_result = df.nsmallest(int(params["number of rows"]), attributes["column"][0]) 

self.bottom = pd.concat([self.bottom, batch_result], axis=0).nsmallest(int(params["number of rows"]), attributes["column"][0]) if self.bottom is not None else batch_result
return self.bottom