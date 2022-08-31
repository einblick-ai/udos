defaultValueAsString = params["custom_binning"]["custom_binning"]["default_value"]
formattedDefaultValue = f"{defaultValueAsString}";
dataTypeForBinValues = params["custom_binning"]["custom_binning"]["bin_values_data_type"]

if dataTypeForBinValues == "boolean":
    if defaultValueAsString == "true":
        formattedDefaultValue = "True"
    if defaultValueAsString == "false":
        formattedDefaultValue = "False"
elif dataTypeForBinValues == "decimal":
    formattedDefaultValue = float(defaultValueAsString)
else:
    formattedDefaultValue = f"'{defaultValueAsString}'"

bins = params["custom_binning"]["custom_binning"]["bins"]

expression = formattedDefaultValue

for b in bins:
    name = b["name"]
    if dataTypeForBinValues == "boolean":
        if name == "true":
            name = "True"
        if name == "false":
            name = "False"
    elif dataTypeForBinValues == "decimal":
        name = float(name)
    else:
        name = f"'{name}'"
    
    if b["expression"] != "()":
        expression = f"{name} if {b['expression']} else {expression}"

ds = self.from_input(0)

transformation = ds.transformation(expression=expression, column=f'{params["custom_binning"]["custom_binning"]["new_column"]}')

for dfs in zip(ds.flatten(), transformation.flatten()):
    yield pd.concat([dfs[0], dfs[1]], axis=1)