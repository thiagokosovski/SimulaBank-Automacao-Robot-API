import json
from pathlib import Path

from jsonschema import validate
from robot.api.deco import keyword


@keyword("Validar Schema")
def validar_schema(response_json, schema_name):
    """
    Valida um JSON utilizando um arquivo Schema.
    """

    project_root = Path(__file__).parent.parent

    schema_path = (
        project_root
        / "resources"
        / "schemas"
        / schema_name
    )

    with open(schema_path, encoding="utf-8") as schema_file:
        schema = json.load(schema_file)

    validate(
        instance=response_json,
        schema=schema
    )

    return True