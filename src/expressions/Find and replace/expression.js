const columnToSearch = inner_inputs["find_replace"]?.find_replace?.["find_in_column"] ?? '""';
const processedColumn = columnToSearch ? `[${columnToSearch}]` : "";
const findReplaceChain = inner_inputs["find_replace"]?.find_replace?.[
        "find_replace_pairs"
    ]
    .filter((pair) => pair["find_keyword"]?.length > 0)
    .map((pair) => `replace('${pair["find_keyword"]}', '${pair["replace_keyword"] ?? ""}')`)
    .join(".") ?? "";
return (!!findReplaceChain && !!processedColumn) ? `[${columnToSearch}].${findReplaceChain}` : '""';