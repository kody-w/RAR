# JSON Doctor

Inspect, validate, schema/shape diff or query JSON and JSONL without opening it. Infers shape with per-field coverage and points at the exact line and column of a syntax error.

The `diff` action compares inferred top-level field names, types and coverage, not values, nested structure or record order. Its output labels the comparison `schema/shape`; `identical_shape: true` does **not** mean the documents are identical. Use `query` to retrieve specific values.

Moved here from the RAPP Store (now an alias of RAR); the original page keeps working: https://kody-w.github.io/RAPP_Store/#json_doctor
