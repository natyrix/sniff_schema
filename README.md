# Sniffer

The `Sniffer` class provides functionality for sniffing JSON data and generating corresponding schemas.

## Usage

```python
from scripts.sniffer import Sniffer

# Instantiate the Sniffer class
sniffer = Sniffer()

# Sniff the schema from a JSON input
json_input = {
    "message": {
        "key_one": "value_one",
        "key_two": 123,
        "key_three": ["value_one", "value_two"]
    }
}
schema = sniffer.sniff_schema(json_input)

# Create a schema file
output_path = "./output"
file_name = "schema.json"
sniffer.create_schema_file(schema, output_path, file_name)

# Run the sniffer on a directory of JSON files
data_path = "./data"
sniffer.run(data_path)
```

## Methods

### sniff_schema(json_input: dict) -> dict
Sniffs the schema from a JSON input and returns the corresponding schema dictionary.

- `json_input` (dict): The JSON input for which to sniff the schema.

Returns:
- `schema` (dict): The generated schema dictionary.

### create_schema_file(schema: dict, output_path: str, file_name: str) -> None
Creates a schema file from a given schema dictionary.

- `schema` (dict): The schema dictionary to be saved as a file.
- `output_path` (str): The path to the output directory where the schema file will be created.
- `file_name` (str): The name of the schema file.

### run(data_path: str) -> None
Runs the sniffer on a directory of JSON files, generating schemas for each file and saving them in the output directory.

- `data_path` (str): The path to the directory containing the JSON files.

## Dependencies

The `Sniffer` class has the following dependencies:
- Python 3.x
- The `json` module
