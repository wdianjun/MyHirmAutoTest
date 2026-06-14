import json
import os

import jsonschema
from jsonschema import ValidationError


def validate_json_by_schema(json_file_path: str, schema_file_path: str) -> None:
    """Validate a JSON data file against a JSON Schema file.

    Args:
        json_file_path:  Path to the JSON data file (e.g. data/login.json)
        schema_file_path: Path to the JSON Schema file (e.g. data/login_schema.json)

    Raises:
        jsonschema.ValidationError: If any field fails validation, with full detail
        FileNotFoundError:         If either file does not exist
        json.JSONDecodeError:      If either file contains invalid JSON
    """
    # --- Load schema ---
    if not os.path.exists(schema_file_path):
        raise FileNotFoundError(f"Schema file not found: {schema_file_path}")
    with open(schema_file_path, 'r', encoding='utf-8-sig') as f:
        schema = json.load(f)

    # --- Load data ---
    if not os.path.exists(json_file_path):
        raise FileNotFoundError(f"Data file not found: {json_file_path}")
    with open(json_file_path, 'r', encoding='utf-8-sig') as f:
        data = json.load(f)

    # --- Validate ---
    validator = jsonschema.Draft7Validator(schema)
    errors = sorted(validator.iter_errors(data), key=lambda e: e.path)

    if errors:
        messages = []
        for i, error in enumerate(errors, 1):
            path = " -> ".join(str(p) for p in error.path) if error.path else "(root)"
            messages.append(f"  [{i}] Path: {path}")
            messages.append(f"      Message: {error.message}")
            messages.append(f"      Schema:  {list(error.schema_path)}")
        raise ValidationError(
            f"\n{len(errors)} validation error(s) found in {json_file_path}:\n" +
            "\n".join(messages)
        )
