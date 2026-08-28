---
name: "rar-cowork-cookbook-configure-measure-warehouse-performance"
description: "Applies a bulk configuration change to measure warehouse performance from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_measure_warehouse_performance", "rar_sha256": "2a314dc6a1b98ffb6975000261b7f26970825750159d4287de69c486417a859a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_measure_warehouse_performance`. The original RAPP
agent is preserved byte-for-byte in `configure_measure_warehouse_performance_agent.py` and in the RCI capsule.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the linked
agent SHA-256 before importing it. If preflight reports a host dependency that
Scout cannot satisfy, use the `brainstem_chat` MCP tool to run the canonical
agent in the user's Brainstem. Never paraphrase the factory or agent into a new
implementation. The generic direct-file commands in the generated Toaster
section are recovery guidance; Scout should prefer the verified runner.

Measure warehouse performance Configuration Bulk Setup — Applies a bulk configuration change to measure warehouse performance from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-measure-warehouse-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "operation": {
      "description": "What to do: run, plan, checklist, describe.",
      "enum": [
        "run",
        "plan",
        "checklist",
        "describe"
      ],
      "type": "string"
    },
    "subject": {
      "description": "The process to automate.",
      "type": "string"
    },
    "trigger": {
      "description": "Optional. What starts it \u2014 schedule, event or manual.",
      "type": "string"
    }
  },
  "required": [
    "operation"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_measure_warehouse_performance_agent.py` and embedded as the fenced Python below (sha256 2a314dc6a1b98ffb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_measure_warehouse_performance_agent.py` first:

```bash
python3 configure_measure_warehouse_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_measure_warehouse_performance_agent.py   # or on stdin
python3 configure_measure_warehouse_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Measure warehouse performance Configuration Bulk Setup — Applies a bulk configuration change to measure warehouse performance from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-measure-warehouse-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_measure_warehouse_performance',
    "version": '2.0.0',
    "display_name": 'Measure warehouse performance Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to measure warehouse performance from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'community',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'configure-measure-warehouse-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-measure-warehouse-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1d62c60ec1432b1f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/analyze-warehouse-operations/measure-warehouse-performance'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/configure-measure-warehouse-performance', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Microsoft 365 Copilot Cowork'],
}


try:
    from agents.basic_agent import BasicAgent
except ModuleNotFoundError:
    class BasicAgent:
        def __init__(self, name, metadata):
            self.name = name
            self.metadata = metadata


# The toasted capability. The upstream entry supplies the WHAT; this procedure
# is RAR's own method for that shape of work, generated by
# @kody-w/skill_toaster_agent from the metadata we hold. No upstream text is
# reproduced here — see the module docstring.
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ConfigureMeasureWarehousePerformance(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureMeasureWarehousePerformance'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'The process to automate.', 'type': 'string'}, 'trigger': {'description': 'Optional. What starts it — schedule, event or manual.', 'type': 'string'}},
                "required": ["operation"],
            },
        }
        super().__init__(self.name, self.metadata)

    # ── helpers ─────────────────────────────────────────────────────────

    def _subject(self, kwargs):
        for key in ("subject", "input", "target", "topic"):
            value = str(kwargs.get(key) or "").strip()
            if value:
                return value
        return ""

    def _header(self, subject):
        label = subject or f"<no {_SPEC['subject_label']} supplied>"
        return f"{_SPEC['verb']}: {label}"

    def _context(self, kwargs):
        extras = []
        for key in _SPEC["params"]:
            if key == "subject":
                continue
            value = str(kwargs.get(key) or "").strip()
            if value:
                extras.append(f"{key}: {value}")
        return extras

    def _plan(self, subject, kwargs):
        lines = [self._header(subject)]
        extras = self._context(kwargs)
        if extras:
            lines += ["", "Context:"] + [f"  {e}" for e in extras]
        lines += ["", "Procedure:"]
        lines += [f"  {i}. {step}" for i, step in enumerate(_SPEC["steps"], 1)]
        if not subject:
            lines += [
                "",
                f"Pass subject=\u0022...\u0022 to bind this procedure to a "
                f"specific {_SPEC['subject_label']}.",
            ]
        return lines

    def _checklist(self):
        return ["Acceptance checks:"] + [f"  [ ] {c}" for c in _SPEC["checks"]]

    def _provenance(self):
        src = __manifest__["source"]
        lines = [
            f"{__manifest__['display_name']} (v{__manifest__['version']})",
            "",
            __manifest__["description"],
            "",
            f"Capability shape: {_SPEC['archetype']} "
            f"(confidence {_SPEC['confidence']})",
        ]
        platforms = __manifest__.get("platforms") or []
        if platforms:
            lines.append("Runs on:          " + ", ".join(platforms))
        lines += [
            "",
            f"Indexed from:     {src['source_name']}",
            f"Upstream entry:   {src['upstream_url']}",
            f"Upstream author:  {__manifest__['author']}",
            "",
            "RAR indexes this capability and implements its method; the "
            "upstream library remains the authority for its own instructions. "
            "Open the link above to get those from the source.",
        ]
        return lines

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

        if op == "describe":
            return "\n".join(self._provenance())

        if op == "checklist":
            return "\n".join([self._header(subject), ""] + self._checklist())

        if op == "plan":
            return "\n".join(self._plan(subject, kwargs))

        if op == "run":
            lines = self._plan(subject, kwargs)
            lines += [""] + self._checklist()
            lines += ["", f"Deliverable: {_SPEC['deliverable']}"]
            lines += ["", f"Source: {__manifest__['source']['upstream_url']}"]
            return "\n".join(lines)

        return (
            f"Unknown operation {op!r}. Valid operations: "
            + ", ".join(_SPEC["operations"])
        )


if __name__ == "__main__":
    print(ConfigureMeasureWarehousePerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816abObyJL2X2HOfHD3YB8EYpNvdMQghDYkkJBYRLvDzVIgdsQO/fZ/fwtJ59g9fe+d2xPzYWQ7LKAqM+vJzCezCv32YtXVNStePr+cgJUiKyuOgysoECt1ET5rsyKC/2WRDf8hTpZWRWDXVVaULx9fXFA6RZBXQZbC6VyexwEoEQux6/g+1gv8urDGx4hztVIfIFWGJMAq6wIgrVWAa1aXAMlB4WVFYqUOQLwiS6BqJEjzukKEzgEx4gUx+Ii0QXVFGisO3IfE0b4ii2PbciKkrPM8K6pXaBTorCSPQfny+edfPr4E8PvL599enNgq4a0X/mkV2D/M0N+sOHwzAgqJobVwdN5DaFJ4/TQR3nKB92bwDyWIvY/If/xHBNfilz9+/pIiz8+Xl/GPUqdIdR1XbZUVcBHHyi07iIOqf0W4uLX6EilAVRfpCFoJkU3918fMb5KyHPlpfPbDQ8mrD6ofvrxk0IQ7DF9efkSyAuor6vH76ygl/+HH1zhrQfHDj9/klLUdAqcahUGrX78+r59i4cBvQwPvrvUnKPXhYRt8eflucePnYfe4Tjjz5TXMgvSHh+C8yBqQjjj+8OM/EutcgRPFQVn9S3J/fgi+AsuFa3oa/uPHO8i/IOhzQe8y/7HaHLr1r6wEDn9T9xF5AvWPZN/x/y+i4yCF+fCG+N8V9/cmoD8hP//Dtf2zCR8R78vLAsRBA6PDjsFn5Levp4PA//zB/Xbzwy+/Q9H/rZhTVhfOXcJXmBSBB8rq69efP5T32x9++flDncNYA1bytS7ivyfz7+F61/MHBJ+jfvjjXKhfTaM0a1PkPdKR37L834rfXxFt5IBv98vPyPf5Mn5QZFzEm9IHBN/lTAlt/Q7HH19+hzyRwtXUzv0xzPJ//3dkHzhFVmZehZycDHIRdHAVJGA0/nwNSgT+HXO7ABDXMoDAPsfB+B89PFqceciv/+ncOfST8+RQ7I0XwdcnE359Z8Kv3zHhr6/IGYrPisAPUitGFO5w+JJaPkirUXVegBIUDSQVu6/AJzjr0/gF8iby67+o4etd2Gve/3rn0uDBVQq/GXmqrGPwOq5Vv4L0uTIH8jLogFNDPXHmWA9mLj9CDMosbiDPjbiUURDHiBsUEISs6B88XaefR2G//vqrbZXXL+mDWKfIo36UGBzwbg7y6RNcnRcH/rX6kgLnmiEffvv9A/L/kH826y581HGARP/0DLRwe5IlBGZancBh0GnQzZBG7p757fcnxlBMCgse9GPgjQVsnAwjNQLuG+CnNfeJoGjEBhA8CHIyFhvI1khQvSIbD3m3FyodH418fs3KCnFBDlIXpE4PpVpwOe9IplmFlDAcS6//iIxVcNT6q11YdxMTmPJW9Suy5w+wemTxWDiLZzWBk7M0gPC/h8PjPhRSfCiR+ZuIV0QaYxPJrcLKr4X11OFZD7/AqvE2HQq3kBS0X9KxXIIRqnuiPOCBgyAyztOln0afw+KewBhyyzfd9zHWWOPO91pXfEnLZxLA0IOoOLAoQKV+Dcs3jL2/PUOqhFEZu3f8oKWjpKcX3KdX7jG4/6ctA/+HRmM+9h4nyCo58qUmJjiJ/F/oS8ZVcKuVIqy4s7BABOmsXB7oji3V6IVHFwZbAwTqfGTSt3bhjWzeOPdLGgcwVIr+b4+Rd588xzx4DK7EhZyh3OXDgIDojnLv8TrGX1HcIfmSvpH7R4jPncngEmByw+AfQXlTOD59s/QKM3i8/lbo7/4t3HHpMCaRvLZjGC8eAO4dhOpajDn3dAcMXjDmX3sNnOsfVoVA6TBGoHwEGhHALIIF4A6dlMFlwnS7e+F9eDC2T9AKt3agtbBnBa+IDtNmDJ0S5irsgcYxEIUPd1HQxRBjaOI7wuXVyh/GjG3u00Br9EWWwGj+3gPPh98C/W7LaD6UakHfQyzbkX9d0D08+27n01fQ2GRMzfukP7r7uVbk+yr0ty/p3cZ3yocZH48F/DtwEJhpSXkPuZGwSkg6CXgGEIyEe61+fZTbRz1/t+Xzn3r7H/5a+38voOofPfcZuVZVXn7GsEfRe6t5r5AuMBgjQQ7Kb/Xv0zPjPr1n3KfvMu4P4h9ofUb+mol/EPGM7c8I/jp5nYyPdoEDxuB9fiAi/Kf55RM5Pv2SKuCbq5/xMHJu3MOC+16A3obAKuQXwB8HPwpSOdaxFpbOOwNDZ3xJ38PhmSwP5oHVs8y+S+J7JYbOffjuvVDAR2kFdbtjF+eDcZ8Tj+aX4OVzWsfxx5fUSsC/vr8ZawKMW4jJuDmCOQSRrwJwv3rvk8aLP27x7tkFacHNPo9J9hEZe9qPyHt7+hF52zDcd2JpDXdMP4+t8agSDoX/vY993z/a4AVu1Ko+H+1/7ILGjuzZKf/ZiDG3oMUOGOt89p6so8Y/CYFffB8UfxYi379Y8ZMxysoaq3ZQveV5Ce1065HfoQdh/sGUgtjVcMKf1UA9BbjVsDy643K/4fdtWdljLb/fYageW8nfXt6Y4+mDZ9sIh8MU/VSOBRKD0QoVwutHXMFn/9OG8ikGUh7sZKAcwpripOvQFm7PWM+z6RlDTSYTgsZtxiPg1YQlKHgLp2YuSbCMC+iZQ7I0iTMWS80sKO8RpF/HZiCo7iIth3UYKHbGWLQDphN76gCcwF1mCibUbOqxLCAhSu9TI8iXz/U+1jeC+d7bjrg8l/3bi02TcOSaLDfc48NjM82iCcZWrjZa0OBiGtjGDtTbyW6Wxyoq6SKXpYg/z1OTCNiNRvACFd2sROb7dSXurXmTHT1ng/YGkw4HLjilQh20OuFrzS7dRoPJMrE8Y03RD/jJsYxtbXJzTtKuOlu4Zm2PlCuqKypKT3lveWJsuKeosI1d55q4GxwrDb8YJMl4XqfGirnMzY2q7Tk2laerY8VS6ilWVjaYupc4uYQmT02M6qTJ6/p8E9rStS4JGZmGNRWqPTWhg/P2oOhJv9va29ie46oZ9HwEwojwDkOJgtRuUXRiOY3RzbBonxk3VhM1OW/mYl9UVoJLmn4RXKWwVS04dVGxkOhrwd7OIrnTKU20I8sMo8q0rygTWMpq36pn+nbm99q289KdTN4MWXNgk6PoItWpQtwb9oU8hbSl9/jxRNRwV7b11CHCu6t0HE62AMLQpArL9SYuvrIsSh9M9aYlCzG+kFjbbMghvQSxGiReg+eLY5nXvUDU12UiJowm42GTCubcsaOE8DmRbm+oveZNxjJ41JO1cjphVie1XmLunvahHs3Kj94O1eNTWEw3+cUE1oqqF+SluwgdKxK05ePFcrprkzjog0o/m7vZoJr6LZnhqzjKVxx2UGlHsI54J9xoPeuqy0HFtBXqbbUQa9Z8QPkgcfWp7dITdIM7lLvfVbPDaudSm1s5SMxhf00XpYkvFdEQQ2CQfaqgpmNY9vZ0WE5DgK/04LJQr7vmGt5Y36Gd5fpwNhKxNDGyvvIb8+RdjqWEMmuBVJQeiHGYiPqkoxZUgePe4Oj0zc+YlJ2cjDwkXX0ZSKEkXHlaTc+6md8uaEWblR3hTO3qBuO3+LJDk8sS5UNUpsDcR/n5zKeWtStu8jPWYrq8xVHMOUz4tpeH2Egvc5ZPgh5bekudEM+qomvpYCqbIrZivVpHwQGPWkLcOftLKwVqGkqZzwrpdbLXZHKLwyqy7XrRk01jjqd5JercEC9tU5acU0XuM65eADELzF02gdNsJ5QjxY8GgxepYJdtleVe13AzvHb79Tqs3TYLNzTm1LQpNUzuzbdUOjlVZ1oEZ9YEYeEkgZELs6QH+SzTE7dbDWfSm7NoJcEYYQyP9tpFqYSqEYln7UpqUcnQJ5FstJiQOOUy9QnB1s2FUckUvXG0zs52Mi54XNnqM/qaoXZ22x4KC8sW1GTh8EtqhavJKdZWRyACoe8zjd/XCTMzhtiemMxtGUyVIGNRDFvVUZ+ILLvJ4mSH8vICdpITokB5FN/OT3vxNiVRISzP5jQ8neWrtsPUOj4SahPhqbFQ5EI6+nuV9Y9NDjxOuwK/jONLuktY/oCpZ9bKqg29JnsXXERJ2yQAttVcLe+yEibjVD9A1g6HdBoJMSA4q49WGSPZ61K4tsxZdDcJehQzmNPpvifxOBY321oHWUQztrgTuoNYE93gu1xyoGhsl5Q47dgOJgTpEHPM6uyBdOZEw2mOLsq+7Mk2mWYyjqm65J1EGz/VaZ+Wc1YQTGbG0ByxRkmenHnr9NJ2AMTzJWRZkM+LzSHc7veNe1pjWzHQ9geF2kPfd9Xxxl6OwGGsij2uSmNLiwWDHnXufK4ZIZ938x20a5HHO8nTHQtjVEqKibDyF+Sw3XAFZ6eL3bmhxaPEneadE4rH40Y+WastWE34SWHiDax+4S2aaJys5ldtmax07kJGeRWdtqlMLNs234jKegPMLF/hu5NEgOWCdWZrmvTzDWO6nelXzfYihY3Lgkk5RC2bMQe5SXEUNHZPZp3gpxvz1sXYIcpuvRVGK0q2B5MWOGa5vFIkzrKyt3MWZVF7F8MKfVpIMG+rsKjKxQsGI7HlmnXkaNGdWFFvznGss7eFH/lL0G3EI16lZbEX/e2+0YZbvic59yDN3P0kolPu7MxXkySrDXKnXgj3qMlnNRgcBxX8ddILilTimZ/6kAVauB+ts+3MOpyS/U02TKMVF2g17JQ5qmqNCKmyYmmn17qEwDGG132RuixnbjojdlW4XS41Re2KFTsRJLY+aFXNqXSQawmLLgvJlm0fTACB+r7A7dRZVqS6NiGqquNq1BzMcBfOw4WxEGwfJnk5mYX0vrFLXREH1Vrv+50aKcryVm9vyq3wGAowgetDUnJyQeV0v9gRF2WXGfM1G22knjL0SGQMiueWuqb07IXPlF5oZqqWX4A1CdDmVFfHulwXJXkerjA1m7YIpoddrfdWtesEgkJbTi2EpDzMDF2bb8ulrpgHV08K67JxnHi63zHqrWoVVmDnqcoa4aqc5Oh6KZMrW5tK2oBJ7XGzskWnXauXaLJdqGtinrYluVoeLW/pmLudHDG6cW1HFl0th5LvdnRG46q9X9UZIXTO9rLQL6jIqO5MmFrUQVlWm/7gnU7JrjxSAKXpONzC3d6NjK9tfcgGFQf6cc0yttotyFzEt11QNaZvNRU3wU9twXn1tA4zLbAwN1QvIb+dDnrpFobXKCSu8DYZTIMblk+O0Wx1iiIFX22XaKDuSQ2gt3genP3ihCnGbh9RWVy2NibgmloqipKXO/ImF/ub7sw5sqdPlcJ6rnHI1+pEtPyjtfTqyaHKjPLkOlg4udSAzxbqxtjVM5OZLAUm6jYDxVjc4XCeHSYzgKLlQSkvqsVtuzmWo9OeC+W1TWNR0lQXFBJbocVqMp1QpQmGZS/nBqjSetZMFk3Y+fN8OphTc78Rg+7IOZvVslPYWOc1J9xd1v0G503rGmcgpOWdRpxS3E0k079xBCsVzsngiuNu0DiPNSfXnX5bKvNupud+fXDXyvZ0u4KZqzKhFlCakjtKrJY45buH9nLLHLLQ9JgqVIGweMsJ81i6ZXFIXzm1nmpHQQZmmkeU2XJxf1nu/ZUdhftpckNNifapblKruLEST4PjN5t0UokeKuzbmbTtlCpPHDo0nCDjNVbp6JuT6Sd5HZ3J/ur0w3q/zYDF7w5HH5uXmr10XXo9jyplf0oG2bXCnLb36iwlhgO/l5vJstrTu/lZuqlY3vv7XpL1IaD29lKjBlMsjduql7Nmo8VYhbIu44pmgGum717RiYNyBTuzupUzrAalmLa2UHSZWlKOqR3wZn2g6yir9x0RFjnO7ad7Z8Og2kGpZJRMTMtsumwBto4mqKQRuIF6SbkA8kd+yWYyQ/Hi/JaxK1g0kyOvJvsg7qqUWx83pbmgMgk2Clv30u8HUB6oVBvO9DqlazBNyEER9auS4yWI5UAMNnEEXbcA7LZcNFtOCv2aOToHrjGLaJgTrnS65Ec51TgQKTbs+Qql7ycNezAzAYWdK9xBbCV2F0v9JLps9WVedq2FkVzEpPsDEM58cs4lRl3ZAjpt6mWzFPmjRKYmVZveYRIaR5KQQbzgVbqWOHGlZitRm3RxNzP9lBMTw4P9xZUJV0Z63M7202y1zM65yehuHzHVUEnW6jRfHPiGqE3NWpEkXyfubdW4dSbVm3i5yFdLw7ilsFUV2C2IEy1VFtYpCIj5mscGKUiUVNqe551ycw88I8VOZp9W4pq88BJHSMt1SXGYooeSVXF7dU8MUY+W6dnCQHuStN6dHOcXbpsPlFKW6ZIw6rbyT5FACudDYOLlehvS1SZUPLGRBTe/Xi4sWFwyS6eukWYunVlClRV1wrgmYTeMVctDR+Fb1zaGE7dZxUkdC5i1qa6OPjWMxWVPrw4i7AuF29RqROySsd6VjTtanuKwiKZ6AaZ8T6wmHXFtHcPHpnbPNm7raC3lkDG5ml9toifDdHnanI1qyDRJnjBxzFPi4lwyiTwcfKlWZFNnCqaouHVTJqVCWGQ2v8YHQSGKZLlnz1nBkF7bhMJsxckbp4MNVtISPHbzaHm94HwX47GcpWeUPvfU2LnOAmUGc4ospbXLKQ1DsKJqt4rNt6hLaBWFt1oUgnjdoUu52DUXop3qJLVM6RRjsWuFHneTvtid0WHAluceHRrXmWEwAW5M3zfHNtXTckkJcujOz2QNriFXME3uozUDtgeaD06X/cKsL64ASilXJhQZyPFaWMd7xid4klqwutK6TD+cT4zbN7UbtCvKpRJqIq0DksPjYqvtSXw73Vkz6hxWq8tyvQ/zfduji0pkg+lA7cu5zWN1UpI+pjrtdO2Y0qaEvZs75dcdcCvX6CV22zjT04ov5mqObnpWvdIMRIQbzMtC8GDvkRyMKNCvWKWTDIFPkworPNRxnI2prg12AtqFcFIORkgbBsdWW8KeDvvzxQU13pKXYOrPCTIbSkzHZ9g2mNLX2qj3/I7AVJmk7dooQcVWKcFbPreY4TfUmx/TNtnlYC7sHBiv9XZaLWnh0ig6ZWGQBzf8wm+vqJHX+MIRCq+Hm2WhHLrNnL0MxRD2mbPYL2dcsm4ucrg9tPpApYHtuGbHkrAJK02PF+uNY8zAeY2Wq4VCYvx+ffRuHCMkQdw0A4z6gOc5SD3cmdxOGlufc+VaDvpV5uzoWSffbjq10OtdarSXlHdxid2UND4rCG/t5Mt6Q7CGKYMgTWD53ilnNiMGdwO6U3aez0E9DHwzu5rMxissyUmqoSm6dBocs+vgLogLKc3Ci9yRF7G/cjPUI7hW32WHM1OUW2/rdPYw1adKxdU63zLitUiqctmcKVpDDVmSCHd6I7XVxaQl3N8rlMP4Limv/XCYZzzvYDd6XhAZM6H3kKnZxZol5HB2uyqtF85oRTzUCYjIxjr3rhs2zuZKHolqYsvzjrVnaV11Q8LYcIPOLBl8MDyj4xfoenGYUY4sHbHsrMjYBYi7oiIazlvN+EJvV0wxI2fumsmYYn92mHpKHrCybPKNsgAuNrftXm/SNjBh9G0m3VyS+by0bszWkzzlHF00r95M3A3usrjRHoCGSoejdIBMV3nL84C5InnNcKpgwsneSE+eGbqdZXf2bnHWPD4WDZz02+5MHuj1Muta73hZn9TNftgvjHWyzlzCFG951RKULefVYVrlde9Kh84qOFg1VhJxqJ3Zecvw65Z11p2t4qQ27Rfhft1yW4MXWIPwtwNYwJpVo7lEyRZnTigR7oc88VpK/WUmyklVyIavA+Yq7xs/QWlQtgcUq9W0XWld0Z6njb2ghG3l1BlpoAM/rSWU3+1mqThgV4sLZFTTZFraroqdj3faTBTEHJtQblvXLnEoeccL03Yt8vaab2kwWW0jy7YFbkugOaligr7G15EKLK+bTQJ5WtcoFV7LsihcBm5FC/SgeO0ctonRNeQzjuN++unl48t4jv08jf6rb6LHg8H/tfPJx1Hi2zuq+0E0sNzPd12f/7Jlv3x8KZwA2vU4kS3j2n8eXP6X89hP/+ILjlFI/3jVO75Y66q3k/zK8scfL70EqVuXVdF/LbO4vh8Mf3yx63L8CUX59XkA/nJfYpKPp+nvel/GnzOMp9YZnFxlX58//rjfHl8YATewKvC89J9n1R9f3B56LXDKr1Oa+gqKfFzy863J6I7xtcnL7/8fks1kUi8mAAA= -->
