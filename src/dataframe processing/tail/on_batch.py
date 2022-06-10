if self.result is None:
    self.result = df.tail(params['number of rows'])
return self.result