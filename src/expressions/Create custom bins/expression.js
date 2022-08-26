const defaultValueAsString = inner_inputs["custom_binning"]?.custom_binning?.default_value;
let formattedDefaultValue = `"${defaultValueAsString}"`;
const dataTypeForBinValues = inner_inputs["custom_binning"]?.custom_binning?.bin_values_data_type;

if (dataTypeForBinValues === "boolean") {
    if (defaultValueAsString === "true") {
        formattedDefaultValue = "True";
    }
    if (defaultValueAsString === "false") {
        formattedDefaultValue = "False";
    }
}

if (dataTypeForBinValues === "decimal") {
    formattedDefaultValue = parseFloat(defaultValueAsString);
}

return inner_inputs["custom_binning"]?.custom_binning?.bins?.reduce(
    (prev, binDesc) => {
        let name = binDesc["name"];
        if (dataTypeForBinValues === "boolean") {
            if (name === "true") {
                name = "True";
            }
            if (name === "false") {
                name = "False";
            }
        } else if (dataTypeForBinValues === "decimal") {
            name = parseFloat(name);
        } else {
            name = `"${name}"`;
        }
        return `${name} if ${binDesc["expression"]} else ${prev}`
    },
    formattedDefaultValue
)
