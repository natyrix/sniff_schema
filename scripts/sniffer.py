import json
import os


class Sniffer:

    def __init__(self) -> None:
        self.output_dir = "./schema"
        self.data_dir = "./data"

    def sniff_schema(self, json_input: dict) -> dict:
        schema = {}
        message = json_input.get("message", None)

        if not message:
            return schema

        for key, value in message.items():
            if isinstance(value, dict):
                pass
            elif isinstance(value, list):
                if len(value) > 0:
                    schema_type = "enum" if isinstance(value[0], str) else "array"
                    schema[key] = {
                        "type": schema_type,
                        "tag": "",
                        "description": "",
                        "required": False
                    }
            elif isinstance(value, str):
                schema[key] = {
                    "type": "string",
                    "tag": "",
                    "description": "",
                    "required": False
                }
            elif isinstance(value, int):
                schema[key] = {
                    "type": "integer",
                    "tag": "",
                    "description": "",
                    "required": False
                }
        return schema

    def create_schema_file(self, input_json: dict, out_put_path: str, file_name: str) -> None:
        with open(f"{out_put_path}/{file_name}", "w") as f:
            json.dump(input_json, f, indent=4)



    def run(self):
        try:
            for i, filename in enumerate(os.listdir(self.data_dir)):
                if filename.endswith(".json"):
                    file_path = os.path.join("./data", filename)
                    with open(file_path, "r") as file:
                        json_data = json.load(file)
                        schema_json = self.sniff_schema(json_data)
                        self.create_schema_file(schema_json, self.output_dir, f"schema_{i+1}.json")
        except Exception as e:
            print(str(e))
