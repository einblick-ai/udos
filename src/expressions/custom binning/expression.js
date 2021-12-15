return inner_inputs["custom_binning"]?.custom_binning?.bins?.reduce(
    (prev, binDesc) => `"${binDesc["name"]}" if ${binDesc["expression"]} else ${prev}`,
    `"${inner_inputs["custom_binning"]?.custom_binning?.default_value}"`
)