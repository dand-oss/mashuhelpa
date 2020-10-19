"""
examples/mashuhelpa_demo.py

Mashumaro without
- forced inheritance
- dataclasses to JSON or YAML without forward declartation


"""
import sys
from pprint import pprint

# serialize helper
import mashuhelpa as mh

# example dataclasses
from dc_examples import MainClass


def test_yaml() -> None:

    yaml_str = """
a: 11
member_list:
    - c: 3
    - c: 5
    - c: 2
"""

    print(f"--- from YAML to dataclass{yaml_str}")

    # deserialize
    main_inst = mh.from_yaml(MainClass, yaml_str)
    pprint(main_inst)

    # serialize
    print(
        f"""
--- from dataclass to JSON
{mh.to_json(main_inst)}"""
    )
    print(
        f"""
--- from dataclass to YAML
{mh.to_yaml(main_inst)}"""
    )


def test_json() -> None:

    json_str = """
{
    "a": 11,
    "member_list":
    [
        {"c": 3},
        {"c": 5},
        {"c": 2}
    ]
}
"""

    print(f"--- from JSON to dataclass{json_str}")

    # deserialize
    main_inst = mh.from_json(MainClass, json_str)

    pprint(main_inst)

    # serialize
    print(f"--- from dataclass to JSON\n{mh.to_json(main_inst)}")
    print(f"--- from dataclass to yaml\n{mh.to_yaml(main_inst)}")


def main(argv=None) -> int:
    if not argv:
        argv = sys.argv

    test_yaml()
    test_json()

    return 0


if __name__ == "__main__":
    exit(main())
