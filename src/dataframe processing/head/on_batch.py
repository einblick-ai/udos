if self.result is None:
    self.result = df.head(params['number of rows'])
return self.result