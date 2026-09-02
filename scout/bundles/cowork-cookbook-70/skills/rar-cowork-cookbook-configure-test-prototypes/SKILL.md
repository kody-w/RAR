---
name: "rar-cowork-cookbook-configure-test-prototypes"
description: "Applies a bulk configuration change to test prototypes from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_test_prototypes", "rar_sha256": "0a7e9b457301b167b8c011c6a5f42d9baeaf61e5480f54e3af69880336791b18", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_test_prototypes_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-test-prototypes:3ecb9b54f7f3ccf216293b2b1c51fb666c614630e032619771812c4cc5987605", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_test_prototypes`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_test_prototypes_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

Test prototypes Configuration Bulk Setup — Applies a bulk configuration change to test prototypes from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-test-prototypes
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_test_prototypes_agent.py` and embedded as the fenced Python below (sha256 0a7e9b457301b167…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_test_prototypes_agent.py` first:

```bash
python3 configure_test_prototypes_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_test_prototypes_agent.py   # or on stdin
python3 configure_test_prototypes_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Test prototypes Configuration Bulk Setup — Applies a bulk configuration change to test prototypes from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-test-prototypes
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_test_prototypes',
    "version": '2.0.0',
    "display_name": 'Test prototypes Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to test prototypes from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-test-prototypes',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-test-prototypes',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1d0cad7720372edb',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/research-and-develop-offerings/test-prototypes'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/configure-test-prototypes', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ConfigureTestPrototypes(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureTestPrototypes'
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
    print(ConfigureTestPrototypes().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6eZPbRrLnV8H2+8P2Q0vEDbAnJmLBCyRIgiBu0nK0cBQO4r4IAl5/9y2Q3S1pPJ43E7ERS4csHFV55y8zC/r9yW6bMK+eXp5UYGeIYCdJFIIKsTMPmeddXsXwrzx24B/EzbOmipy2yav66fnJA7VbRUUT5RnczhdFEoEasRGnTe5r/ShoK3t8jbihnQUAaXKkAXWDFFXe5E1fwOV+laeQGRJlRdsgy5sLEsSPEvCMdFETIlc7ibwHjVGiKk8Sx3ZjpG6LIq+az1AMcLPTIgH108uvvz0/RfD66eX3Jzexa/joaf4mB9AgY/mDL9yXQJHggqKH+mfwvgCVn1cpfOQBH3m7+7kGif+M/Pd/x51dBfUvL18y5O335Wn8T2kzpAlH1ey6AR7i2oXtREnU9J8RPunsvkYq0LRVNlqmhubLgs+Pnd8o5QXy9/Hdzw8mnwPQ/PzlKYci3DX/8vQLkleQX9WO159HKsXPv3xO8g5UP//yjU7dOhfgNiMxKPXn17f7N7Jw4belkX/n+ndI9eFGB3x5+k658feQe9QT7nz6fMmj7OcHYei/K8jszAU///JXZN0QuHES1c2/RffXB+EQ2B7U6U3wX57vRv4NQd8U+qD512wL6Nb/RBO4/J3dM/JmqL+ifbf/P5BOogxG8bvF/ym5f7YB/Tvy61/q9q82PCP+l6cFSKIrjA4nAS/I76+qvJz/+pP37eFPv/0BSf+PZNS8rdw7hdfUziIfZsjr668/1ffHP/32609tAWMN2OlrWyX/jOY/s+udzw8WfFv18497IX89i7O8y5CPSEd+z4v/Vf3xGTHGtP/2vH5Bvs+X8YcioxLvTB8m+C5naijrd3b85ekPCA0Z1KZ1769hlv/XfyH7yK3yOvcbRHVzCD/QwU2UglF4LYxqRHtL6q/qdrPbfU69rwh8OqY7hAi7TRpEqOwoGfFs9PioQe4jX/+3ewfOT+4bcE7ewRC8jvD3+g3+vn5GtBDyy6soiDI7QRRelhE7AFkzcrrHRN2mn64jMyhI9AAbZb4ZgaZuE/A35OtfUn+9E/pc9KPYXzLoBxs6x4MYnELwtKso6RH7jth9Az5BHIXY8YGw4//a4vNoCzME2ZuFXAjV4AbctgFIkrv2A6zrZ+jkOk+uEAdHu9VxlCSIF1XQKHnVP6C7zV5GYl+/fnXsOvySPYCXRB5FpJ7ABR8CI58+FRXwkygImy8ZcMMc+en3P35C/g/yr3bdiY88ZIj9d0PB4E0QUT1ICMzENoXLamQMAwgzd0/9/sfDA6N0Gax6MH8if6xizeiV79w+avBwy7tPoM6jiKB64/Sj3ZAuhHZBogZaC+Z0/fwlG0nkcGnVRTV4N+Jj88P0705+8Bl9Ur/ZEPrpXifHtfeIG53p5pX3Gdn4yIeloLpjURw9GuawzHqgAJkHMreHO+3mmwuzvEFqmCe13z8jbQ1VHSl/dSDp0TgpBCO7+Yrs5zKsa3ky1u3qrc7B3XkWjY5/i9LHY0ik+gnG2OydxGdEAtCaSGFXdhFWdg3u63z7ERGwnr3vh8RtJAMdMpZuMPronsH3yNP+oVuY/9BVzMZGQ4XoUiBfWgLDKeT/TxMySsoLgrIUeG25QJaSppweYTV2TKOWjyYLNgUIbCoeOfKtUXjHlHe0/ZIlEXRF1f/tsdK/R9JjzQPBYK57ECqUO/0xp6s73aiB8TA6uKruRviSvcP6M7QI9EY9qgDTNh5BIP9gOL59lzSEuTnefyvxyCPURtVhECNF6ySRi/gAeHcjNGE1ZtObA2BwgDGzYPi74Q9aIZA6dDykj0AhIhilEPrvppNgVsC26OGFj+XR2DhBKbzWhdLCtAGfEXOMYhiJNeIA2P2Ma6AVfrqTQlIAbQxF/LBwHdrFQ5ixi30T0B59kad2A773wNtLGJFj/YD8PtINUrWh76EtO+gEmE23h2c/5HzzFRQ2HUP/vulHd7/pinxff/42phyU8RvUw8Z7LN3fGQeGaZXW95CDRTWuYVKn4C2AYCTcq/TnR6F9VPIPWV7+1Lr//J919/fSqf/ouRckbJqifplMHuXtvbp9dvN0AmMkgpn0rdJ9GnPs07cc+4Hgwz4vyH8m1A8k3qL5BcE/Y5+x8dUucsEYrm8/aIP5p9npEzW+/ZIp4Jtz3yJgRDGIrE7/UUzel8CKElQgGBc/iks91qQOlsE7pt2Lw0cAvKXHA11gVajz79J21Gl058NbH9gLX2UjqntjxxaAcYxJRvFr8PSStUny/JTZKfiX48sIrDA4oRnGcQcaGrY+TQTudx9t0Hjz45h2TyGY+17+MmYSLGKwZX1GPrrPZ+R9HrjPVlkLB6Jfx853ZAmXwr8+1n7MgA54gqPXKBnk8BhyxobrrRH+sxBjAkGJXTCW6fwjI0eOfyICL4IAVH8mcrhf2MkbLNSNPZY+WHHfkrmGcnrtCOLQaTDJYN5AOGzhhj+zgXwqULaw2Hqjut/s902t/KHLH3czNI9J8fend3gYrx+V/xEwcMP/3JaNtnwvp68jRXvcd2+e7qa9t5ivUK1oLJvfvQrGHuD1EXhPLxBUwPPTaMAqgpVquI/CTw8xoPzfmlNIAcLDp3psAyYwbyAlWJyLUfYYQtt3DMbHkXdfP168/HVH+495/kIC15k6NOWzPum6PoEzxJR0CAd3adx3GIZxGZxiSAxgJMHgU5bFOZxwKdelpxzLYDTkPnoutd+4T/DR5lDuD8P+++3102MjLAQEzcCdmM2CqUPRLInhDs6wDudiOO4yNu1ThDd1bGD7DA5oisN8mgIkvJtyHEaSDDuFG7iR3lvxf0jz+t5Tv3vhkeevEBLTaJSVsG2Xc1mc8qaszbiAxBzSBTiBeywJMHpK+hwHKLj/Y+ubJ0ZHPRQegxO2eLDBuo58fn/z7BhwDAVXrql6wz9+88nUsB1z4ijhDq0S9HYjmSOpF3ra0B4PjL487Jn2OJOEJqK3XWGdRD9Wm9KmKtHFcvawl3gfMyYni9zJw5z2lX1ySGs5xPbz5gzYmj30nHyR9CWvXhquMPMolM520eR2R0l+olZooRpNFVNJ6lmneGd45go9EJbFGaJuHm1ltVs24qLG5mcY7ahebvp8dumtwos36bH1VqSeDA2VbENpBxFQbKW1YSbDTtuCQ8jdNP2c1xFh9KJ581Zbu+6adU7vzR3H7i2RmMjX8JxVUxT4N3TbEM3qhrtlRal1yeqF5+iGih+2dkk0qnAMTzSp7Cc3I3CC1lnpZaskySGik9Yio/ky3YfBcekZO6PQqxXqxnRNu4zRmwNu6LmVnANLtOvAWwl0VooRxgQXszHMcDPZc7HhxfvVYAkYUUOC2Vnysf2A96UFbHFZKqJWZFqzPLOWa5+02jiWtN9YNjnbmL5A92e9U0lhwOuEoQdqnu3rhlNOx+PKp7yztDjbnMQW4JodaOfU9JixCCaVIm9aODTPa4O08VSsa6aJVkbq5IGA37hhw64UTMAYOzQqnBW7uLj0UWxqxRod4rNV2jRuGkG17SayPtdXakATyxJY+SypZH1iHUxnawy3en1MmQC26Kbly4xAbMn9zdedAt2bC5veRMQwdaT97TKri9uaOu/SG7tCz0OJ1ib0JHel5j3dMtpMxcQaakN0q1TdB+i2zG7JsEKXnGupEcUFEKDs5YS+BPHmdLAO+dlWs3qfXSdu4xlutW3LWpbPu4MgRR5nielpCDAvv+37OlIxvDAj22vWOo16+v4GJhpzRGcoSruTFY3OQy4Ujau33W32E2xCylMMbQeWOaO3w6KwMj2dYppVgOgaVc5MLE/X7RCWqrqlzcLIFddVzdoUbuFRuggnoBIxaAgLO7X8LRLZ2Xo3VMUhVVbn/niSuKkkqr3JBcW6uFW1cZmBQOiIqNyku1LayDOT3LDF8iTu8fW8PEXMXFe0VeKaNuVqsxvDZu522x+u5EZItZPJ2N0xVsxoCIrLdSpXl+E0EQOMGHCpibBbm1POEDLO2aumPXpVucmAis1tLbRKJnI+rJxe4vdna8XW9e1YMULvAEUyEommqOwUDtYqyUyzEdugmWCLGUcquumbwZWSb6JhrFbJ6eD06kVYDVFKGHYFG3nS3zKujV5krwtOTO0tLX+C74p9EV3lmSraMz+1xN0UrRrbttD2bOt9KW63LMXmmaTR5EVdilpJ46XVx6fyyjjVzqicFUyHnT4N9lYO/KUBJKpNcIgloTvX/GgHmp0erBYT5hgKiZCsjpNjqHU2nej6liHVXcqjJzG8HebdIDvBDERnBnSJQe6pXCtWonC0NgKOi9lF8FxG7ROtKA2QNxETHFanYMK3gdhZjSzsaWKyM2OCkXTXZ7xjYUdgc7s2mGYc99nB5c8GnipyyHft7Wpfjxph38DBWLe9vVlDdJ/UspfSlMQBLIs4nFFP2+2eK3GcSIOePa1wqhQstFi0+lTRBRFCr8nksbo2hPkgmx5lBi7va/FkVaPcatGuc00fttZ1V9JeezzqUw3sYkrDCOAAv9th/IXH3PViHpPzTTHZTDgyOQ/nfl+t5DktsgHwHXE4NIFJ7dz8oF/UEy9Fl7NuiL06U0TbOS2z840IT61wmu3mpi9h2HCO+S3bqm0ttfTZOeqp5w5mXYfmlkbrcwnrWjGs0lOSeZJ/lvqpPOC0n81Wu9NcukiAYSZa1N62B5WF8SlltbvIAs2yKhPbuBNTVeuWpkNvup8BbMJsxXWR4BzqX2ESUOhsWREXdInPUpymabbdWsfdeb4u43qjYwNhpCvVWF2NoSz2zHE4OKygqVq5NqUOg4UmogFPzaKzIVlnSd2IsymrYSqhVEqRp6XGKproxZWIt0avto1i67fkhh8Ff1b6EDVLbBJFCuYb1IU/d8Fku6NlfLWkSO20vOwTaT9YG1H3D0Z2xC+uu0xFBd2m6XGSBdNtlKDZwtHM1ZkiQNCcK58gAi2Qz/y6bqZz7eqJZ6UC9Fp1u4uX7lud2eyto8L1Jr3dXVkJL7nrDN/NKrvWzYA5RquNburlLnZjxpW2V7rdyMoZj5VNfuodW/Uv4Xoz1yR6NTNONbEtuYtlZ5IyzLsy3cmzPbPhF2R5oXfzPq0NzPZJ1sCD6TSgXXe7kp1dR3p576mpZShSlZH8jq8Uc2k0bLlrS3HGp/z2RlVxfTrEAt+u2AjmrGFyRblENaEIhrVkQByTbHdfQIDGwZGzpAWh0tq1iC6pUG6Ny7yXsJnGq9yCzEtrU0h4VnZTmVKz4wmrPd6BXdHaKLVzhAfza+qEm3hxWESAk3x1ytbD6bxWl00wXOXIXa47f942FGFUs9DqQ3G63KXVdZBxJcjiZioJkntsTatdYodyF3hYpdlKah6z/EpbRqRHPENQmJCvi0yGNf1Q2EFI5cusWJSrPZdjbjYV1JhM1svI8HNjOKwuV5s++tRki10xeT+Igr1z9gKqnZnS3OQ5Rq1yfW2kxs5cBsGGFk2iPxzwilH6Y6jbsyJfTdiIIAzQFHhtHxSXZrcbAWbmClvIh7DK9FyEfPZi10ynFKo1JLXpzvFVUahZ28leQ0w1SulY0gcxTizWJiy1TF3GBJpJly12OpyTbTVtp4ukD3gKyPxMRdnyZARlLij8fOjOES+QZZUc5Nk0nBeqw0up5rqK4l2HmCnIW6GB5CxJKZby1ODNrYi5rRmh3hyJbWIdPcssT+uA7PXVZur05JBmHmxntvZcObbG4kJdOTfm3W0waVva0QUjUrbCDEOzUz73Y9IVuVvH6JeQ3i5kTcT64CYvu+2Z368367Mv6lzv44vLujgVtTBX1cENr5ssrrc+utQ79BhTOYFd9mA2HaTysnKX+bzMtmJ6iZQ5WuemS1cJdIDHC8HGLYSy3qdFxFjbuFGkKB0k066Ker3XvZQYrvO9ecVmtz2zEzWjNCdFH+xjSTBhVO+dlUFD1KytVu/dW6lUzmB7JCf3y2FVJjPJwbQ0II8t6pacZHZCYwnkzcKranVbxYzltociYyZBlhgKBkOLuFyueLUhZG6ZoUasETsNTPbX/WIbadc62mCM1ikhvZG1QOH5WbfmIagvyiTPt9EQl9sTnJPEY0ThWuC3y5g/c5iQqRsur0X73JprWrWJAxreiCor+paTg+R0FM2tS4p2Hh0DUSnxisyiGSneYlWq+do5gs2xOlY6ucCadWAV+j5bLd345ra6fVX6/gapNBV/OKhDrl3E6a1LJIbI8pm/Op0GsL0xC0YZyqzgy/N5p6dDflH3XnalRUtN5uqUW5+VyJbPW3XXqaf0ql5nsFkXOpzPdVnYlmA4CdlMPcJCv75awf7MKDML63w4pYQufWkVf6WBy4GExtrGyXGD9mySxEYU1ABlj47vGBpLzaSdsN1Ih2F+wDB5lvO+aZ5TxZJ4BUinWXflrKXa75VqQ617yQkZi46rRNOLKECF+eW4uiiKcwgOtXEmajOwesETu/NpdWBYi8YipUyHNJht+YXX+DtviTJtP8UkfWsG8mwF22CU2BUZnLqqo2lne2rqhacN5i3ynG40TS7nc5Zpkn0eqlIpMdhStvOSKVGDP88w4Ubi1lXFKzwdGlWa83ayQ7WQ3K/n5Py6nEDnXmPQciBCy6xndfbgpAa7c9ktK88uxykAQsK2uwhdHzJv7Z4E6eo4kVwzqzkvlV6rl6zWgMvSNsK4szX/mJ9Wk5XSOmvVOQMTNpWyTXGpSspqOAPxOabBoRf4aIKSvZVHaaJJsL88XSfJtHeIgjtSc1eqmvjagwPPpRMLP1gKeaIm6s0Da/5ouWvv0K9BFMtskksLijwTZAYHhqPElfLF3YNpBibNob3e+oN8I0l2OtM43pwlhHmdZGt0m624ATAhnVhTIjDY7TSfOx3ILS7MnHwrzzFmdZpncabNpp7LqT620OPueHDcrbrlTs7xchu6JaqsTutCogOUp8R1bSpw5iYmmsqeh2uqXMRGpYdmyG1ZGkQ9rRP9dtFJt9mR4eHg9pRIJ+dNKliddNOAiTmLhJLj6y6suPWEmRIzir2IuZQJqdUMM87KHMvgAnlq09pUOm3z1Sqjqt1NXTdtJ7lCtZudLrS+opdTXy1sAcWrS83C2Y9Em8n5hndhcjRkbEMEQrUMfG1NWWt+itNoyNrlzm3MFue5MmJqlKHqsHYA0Vyl0CpLqdIOC/piVZZ7VtkpKWT+5nzhs12nsx67joblGRV7ONreolt7i0E4LQVwEyRimOikJlK7Ga9UaYFO565eb/qrbCypSdLNMDpr1ovYcle3yts4YDeQuXFbkgycwRToM4tYomAWVPqeDBdzbtuDScJPwFWjXCUS2EA2AiMY6gNJdqsOKOs5n6oExOK1xAZE584Xi1MblLs1N8nFqpTiY5Rdqf6wTHK+Xl+ZBFsQrOwVRrQhOK06gHSVbvf7Vd6iOnu6guv5qNEZf7XOt3A9mdRNSOJTodVSmpzmJNtt9H5o1niwn0+iemFz+ux87CT0sOPPzqoTiilJ8usw2ptcg8fYerPqOmLt6I3rNGHCkNd50xd00boVqBSdXly12CgYebfWveuqQylwPvBBJjN2oE437bRd8GgA+Ntkf8kndhG7a2oClv2FhaAosnjMBdkpI/cbn5IqLxpE1xcmDntxt3RLEJOyrWcTFydv3ZGfTLthAshFpMNhWleuvRa5ntMaBE2BeCsx+Tn15U7ol0SfZbNdTVxJajfhuNilaNlthv2ZZU41ONb25sDlBcefOMk44/WwmDQndAHbbH9vlBSdn+mZefMjjdtrvMyLcx/3/LWmTdzt5lJiZzit2+KNjhtyU/lGWXsdwaGRLFStEKoZ4eq8fBxqLuDtSwDL1Tml4Ozsdg0vaZqDN51gaM7kqqicO3X88mbyGK9Scu7X4TRblMJVu3G+OPPMmwxuKNe58cym+CqkdNE58ZSvJIuER41UXxz4fefRcb6RE4ALxdGlyVNjLxo24U/9sNixbVEkHtWi8kFcuatg2rvSZJYG0yHurhZnbiaDigE8Wgwsmm2Xt06KCQlNDImwNdwkxSrSep3HnUkeDTs4ytQ+Ld7Qg8/DLmV/WBUEutkrG6ybL5eXZnrsMiKPr6W8KTnMv1Tr2Cc10zx0vX0kugNoC55ZX7H1FHbgtssVPM///en56f7d9ukFx1iMfH4aPwK8HeX/W+fBwRAVr28kSJYmnp/+3x1ePg4S3z/r3Y/1ge293Lm//BvS/fb8VLkRlORxdFwnbfB2UPkPB7Kf/vJ0eNzWP74wj98bb837547GDu6n1lHmtXVT9a91nrT3M2to0bYe/01J/fr2yeDprkZajN8fPjg9rl1QNK9N/praVQzG91E2fkQDXmQ34O02eDvaf37yeuiayK1fSYZ+BVUxavj2XWk8uh0/LD398X8B1YQ9TiInAAA= -->
