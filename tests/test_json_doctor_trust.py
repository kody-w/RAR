"""The diff action is explicitly an inferred schema/shape comparison."""

import importlib.util
import json
from pathlib import Path

import pytest


SOURCE = Path(__file__).resolve().parents[1] / "stacks/json-doctor/json_doctor_agent.py"


@pytest.fixture
def doctor():
    spec = importlib.util.spec_from_file_location("json_doctor_trust", SOURCE)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.JsonDoctorAgent()


def compare(doctor, tmp_path, a, b):
    first, second = tmp_path / "a.json", tmp_path / "b.json"
    first.write_text(json.dumps(a))
    second.write_text(json.dumps(b))
    return json.loads(doctor.perform(action="diff", path=str(first), other=str(second)))


def test_changed_values_are_not_sold_as_value_diff(doctor, tmp_path):
    result = compare(doctor, tmp_path, {"count": 1}, {"count": 99})
    assert result.get("comparison") == "schema/shape"
    assert result["identical_shape"] is True
    assert "ignores values" in result["note"].lower()
    assert "top-level" in result["note"]
    assert "schema/shape" in doctor.metadata["description"]


def test_nested_changes_are_disclosed_as_outside_scope(doctor, tmp_path):
    result = compare(doctor, tmp_path, {"nested": {"a": 1}}, {"nested": {"b": "new"}})
    assert result["identical_shape"] is True
    assert "nested structure" in result.get("note", "")


def test_shape_changes_still_report_types_keys_and_coverage(doctor, tmp_path):
    result = compare(doctor, tmp_path,
                     [{"typed": 1, "optional": True, "old": 1}, {"typed": 2, "old": 2}],
                     [{"typed": "one", "optional": True, "new": 1},
                      {"typed": "two", "optional": False, "new": 2}])
    assert result["identical_shape"] is False
    assert result["fields_added"] == ["new"]
    assert result["fields_removed"] == ["old"]
    assert result["fields_changed"] == [
        {"field": "optional", "coverage": "50% -> 100%"},
        {"field": "typed", "from": ["int"], "to": ["string"]},
    ]
