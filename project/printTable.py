def printTable(data):
    header_format = "| {:<35} | {:>15} |"
    separator = "-" * 55  # Length calculated based on header format

    print(separator)
    print(header_format.format("Principal Funds Available", "Value"))
    print(separator)

    for i, (key, value) in enumerate(data.items()):
        print(header_format.format(key, value))
        if i == len(data) - 2:  # Add horizontal line before the second-to-last row
            print(separator)
    
    print(separator)  # Horizontal line after printing all rows
