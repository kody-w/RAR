---
name: "rar-cowork-cookbook-bulk-update-report-quality-test-results"
description: "Applies a bulk field update across report quality test results records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_report_quality_test_results", "rar_sha256": "727a8bd9a6e192773a59b20341481dcae5159caa5fdeedcc30063e26495c7931", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_report_quality_test_results`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_report_quality_test_results_agent.py` and in the RCI capsule.

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

Report quality test results Bulk Field Update — Applies a bulk field update across report quality test results records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-report-quality-test-results
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_report_quality_test_results_agent.py` and embedded as the fenced Python below (sha256 727a8bd9a6e19277…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_report_quality_test_results_agent.py` first:

```bash
python3 bulk_update_report_quality_test_results_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_report_quality_test_results_agent.py   # or on stdin
python3 bulk_update_report_quality_test_results_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Report quality test results Bulk Field Update — Applies a bulk field update across report quality test results records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-report-quality-test-results
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_report_quality_test_results',
    "version": '2.0.0',
    "display_name": 'Report quality test results Bulk Field Update',
    "description": 'Applies a bulk field update across report quality test results records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-report-quality-test-results',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-report-quality-test-results',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b48eb9a79109a726',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/control-production-quality/report-quality-test-results'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/bulk-update-report-quality-test-results', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdateReportQualityTestResults(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateReportQualityTestResults'
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
    print(BulkUpdateReportQualityTestResults().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6eZPiVrbnV9HL90fZj6wCIQlQdXTEILSCBEIbIJcjreVqQ/uCFo+/+1wBmWW/dvdrT0zEUJVVSDr37Od3zr3KX1+spg6y8uXriwqsFOGsOA4DUCJW6iKbrM3KK/wvu9rwB3GytC5Du6mzsnp5fXFB5ZRhXodZCpev8zwOQYVYiN3EV8QLQewiTe5aNUAsp8yqCilBnpU1UjRWHNY9UoOqhveqJq7HZ05WuhXilVkChSNhmjc1EodV/Yq0YR0gbtl/LpsUyUtwC0GL2MDLSgB1SpKw/gLVAZ2V5DGoXr7+9PPrSwi/v3z99cWJrQreeqGgUvpdG+WuxfGhhAZ1UB4qQBaxlfqQNu+hS1J4nYMSCkngLRd4yPPqhwrE3ivyX/91ba3Sr378+i1Fnp9vL+MfBWpZBwCpM6uqgYs4Vm7Z4SjtC7KOW6sfra2bMh2dVUGPpv6Xx8rvnLIc+fv47IeHkC8+qH/49pJBFazR399efkSyEsqDHoHfv4xc8h9+/BJnLSh/+PE7n6qxI+DUIzOo9Ze35/WTLST8Thp6d6l/h1wfkbXBt5ffGTd+HnqPdsKVL1+iLEx/eDDOy+wGUit1wA8//jO2TgCc6xjSf4vvTw/GAbBcaNNT8R9f707+GZk8Dfrg+c/F5jCsf8USSP4u7hV5Ouqf8b77/7+xjsMU1sG7x/+U3Z8tmPwd+emf2vavFrwi3rcXGsThDWaHHYOvyK9vqsxsfvrkfr/56effIOv/kY2aNaVz5/CWWGnowfJ4e/vpU3W//ennnz41Ocw1YCVvTRn/Gc8/8+tdzh88+KT64Y9roXw9vaZZmyIfmY78muX/Uf72BTFgvbrf71dfkd/Xy/iZIKMR70IfLvhdzVRQ19/58ceX3yBKpNCaxrk/hlX+n/+JSOGIVZlXI6qTQQSCAa7DBIzKa0FYIfDvWNsQhEBZhdCxTzqY/2OER40zD/nlfzl37PzsPLFzOoLi2wMO3x44+PbEwbcRB9+eOPjLF0SD7LMy9MPUihFlLcvfUssHaT2KhuBXgfIGQcXua/AZwtHn8QtES+SXf1PC253Zl7z/5Y7x4QOrlI0w4hSkAF9GW08BSJ+WORCNQQecBsqJMwcq5YUQZl9H6M7iG8S50S/VNYxjxA0hjsP20N95Q999HZn98ssvtlUF39IHsGLIo29UU0jwoQ7y+TO0zotDP6i/pcAJMuTTr799Qv438q9W3ZmPMmQI88/IQA236mGPwEprEkgGgwbDDGHkHplff3v6GLJJYaODcQy9sXGNi2GmXoH77nCVX3+eE4v3VgNbCnQqRGsENhxE8JAPfZ+dbcTzIINNzQU5SF2QOrDJBRY058OTaVYjFUzHyutfkaYCd6m/2KV1VzGBJW/VvyDSRobdI4vhP6OadyK4OEtD6P6PdHjch0zKTxVCvbP4guzH3ERyq7TyoLSeMjzrERfYNd6XQ+YWkoL2Wzo2SzC66l4oD/dAIugZ5xnSz2PM780WBrZ6l32nscYep917XfktrZ5FYJXg3tOhKj3iN6E7toa/PVOqCrIGTgej/6CmI6dnFNxnVO45qPyLcWFs5wh7nzEeXR351sxnKI78/x1DRrXXHKcw3FpjaITZa8rl4c5xdhrd/hi3Rrlw3aN0vs8H7+jyDrLf0jiEuVH2f3tQ3oPwpHkAV1NCnylr5c4fZgB058j3nqBjwpXl3Rnf0nc0f4WeuUMXjBGsZpjtY5K9CxyfvmsawJIdr7939qd3xtqGSYjkjR3DBPEAcG3LuUKtyrHInoGA2QrGgmuD0An+YBUCucOkgPwRqEQIvQ4R/+66fQbNhPV19/4HeXgPWZm5jQO1hcMp+IKcYJ2MuVLBAMChZ6SBXvh0Z4UkAPoYqvjh4Sqw8ocy4zz7VNAaY5ElY2L8LgLPh98z+67LqD7kasE0gr5sR8B1QfeI7Ieez1hBZZOxFu+L/hjup63I79vO376ldx0/MB6WeDx27N85B+ZomVR3TB0RqoIok4BnAsFMuDfnL4/++mjgH7p8/Ych/oe/NuffO6b+x8h9RYK6zquv0+mjy703uS+wCqYwR8IcVPeG9/lReJ8fFff5WXGfx4r7/Ky4P7B/eOsr8tdU/AOLZ25/RdAvsy+z8ZEYOmBM3ucHemTzmbp8xsenI8h8D/UzH0aQjXvYYT86zjsJbDt+CfyR+NGBqrFxtbBX3iEXBuNb+pEOz2KBiJ76Y7usst8V8b31wuA+YvfRGeCjtIay3XFs88G4rYlH9Svw8jVt4vj1JbUS8O9uZ8YWALMWemTcCcEKgqNQHYL71cdYNF78cSd3ry0ICm72dSyxV2QcYV+Rj2n0FXnfH9y3XWkDN0g/jZPwKBKSwv8+aD+2iTZ4gbuyus9H7R+bnnEAew7G/6jEWFlQYweMbT37KNVR4j8wgV98H5T/yORw/2LFT7yoamts0mH9XuUV1NOFI88rAuMHqw8WFMRJ6Mo/EQPllKBoYDd0R3O/+++7WdnDlt/ubqgfO8dfX95x4xmD55QIyWGBfq7GfjiFuQoFwutHVsFn/7fz45MNBDw4uEA+y/nSWtkuaS0ASs6XS8wiSHs+w3AUX6GuYwECJUjHsgjPhTDuONhstsDAfIGThLMkMRTye6To26PDQZZzy3JWzhLFXXJpLRyAzWzMAegcdZcYmBEk5q1WAIde+lh6hWj5tPdh3+jMj1F29MvT7F9f7AUOKXm8EtaPz2ZKGtaCEO06OE/KhbtOlKm6LcuLnWdztQQaebJrEJpzTDxrGmdFF51Rr/km3ggX30BNzA0v8lX1pOv0uKQmFBuL/Xw2iWd4nNonX8APdHheYi1vUGvGnzVGshB0GdV7FBiHWCpOWbyZq9eq5GMvr89haJiFYE/3THwtV5ObdMPDQdYX8+q62YUr9SQbc8LpslPH+iIQS+VYqVd1R1js/BiaGxOLDTVWbafp5oe8F81tuO+TQjuobFOzxa7foXtBVys3rlz66tLSAsjlfAX4cj5phNLx+JAEZ0yfsgvN2ZuFvVX7Xe4k+HbeqblSlrpROV2cs1dtypqhk5/tKqZ6aRaghhSEJH6ym72aF4XrH4PT2bAY1TnH8x7s4iHWqEvB8YA1Nw7LtdvjxU5AEmfhXnAsaVfMZoke7L0LZuRJg2b13hxEMLe8aiU6C6lPnPPu1F7m6tHEz9dTHlWGWqiqutKMmZ+pDA+t19bJwO4bNKrdJdFxx/OhE+psveHqy3zetgmYs+0tGWJ7T0ho02dtqBg0jZ2LmNJWLmq1sWGYCT9HuS6nM3xqMmyYzWnb3K8vaEHEy+jYddqp3FbpxLwegpnILCKr1SPBS0PjsKmFCx5aoeL38yoNz0Xk7a8ZzFg615xW1g6id2tI1WOsxmmSPTqRTrRLCEU17AlZ71KqslCW2dJsl++CSnfntnO2YAhkFouAwZyqC60H5xvPKzlHHGh3hfL7qAzlFWvtz5uQX7Fsnc2FVUwW4Ni2lduqPStfeMmeuuRe8cqqGmqPtkRw4it0NlOWw54JpIWRGlyoGf1OM7pGO8MfNcS20QJr6p2bATtsO61Sb1QnU46ct5OEHui+vuBGZ6XT9bxxtI6YytOr7uMbBa2YCUUrJpyMw9SmusyT1aHJ8szo6015CnuVX/b6cuAdwWzJUE9pKvOrdarY/Wmul6ZkD1pv6Av6lurNsW+GaKttsiYoJe0UXiycNVpzffC5ixGklhLudIxZZozE7GM8ugk7YrMuTKLbn0z8olFzCUurZN82UatOAFDBzCOvaeZRwiLFNbDteWIrHyfcOSOwPLsuAt6ssAWwtk3qBN5pgrVHPnI3MX3osAk9DckNqof4RjVXcrhiF54an9miuQXVhtvUXLtZoNvdUEbOpuf0k051pMWtxfVlSkqDtx+uuVLXqSTRhTNsZtkRLA+hMvg+Y+xEkpVzMgD0DM8ll99tI2667KphwhZVyG8WpBHJ11KfDNl5O0Mj19zTXMSaPYgMKgEoJe1ICCcXkB9NzZ3dmHPUoi1FidIlLeS0NR39Ku6FUzBfiut0hQpTpl+YmSadph6jbxl8xuy8Fev2ey0s+7V7uxlDdJtvVviMEGbnOmOq7d4ElDpYrnQ5XNtE3YoLztrF2nY4FHtO2F23mQ6ypFhC5WcdvWvIrtfdzfWQL6ZimKF25TlTdp0OMbWcaPoqZUGqbkg8qvoqzI8Jlh0qTD+hnr6zjbC2SIJoAapxzdKbHNn1tLlWvKYQ85lwTPOjpqFxUlCNH+G9Qq+74jDZGNTlYkW9ydMgstbGcWams2gZVBCnq6XcAflGaXYwCMS+DfjZdJ+WO+2QNmk+BObkIu6xPXO++Qa+ljY9odk8nXiLfYXy6rpzIhU/MgfV4rZgN6NnkWncdmkV5Z7erQUmD1jW4fT1ueS37kxdp4c5u25zYafQwskUisPiBNF8teNbfCnHHaVSp27Z90f7cKJs3poQZG3G2zxTEuB6HlZNDyJbtJWqXhYol3juVLPy7e6g27Mu2fuOGlXHE3/OTwMxnVhrNnE7jF9eJTaYFqmH8goxFeV0IFc+v/I8cKE7dbXjmiiOT+SO9q8+Czphd0RraIG+87cSjHbBrbklt8LlmXYyCiFAW+F8tEIC+JIRmuzBIPbqcU9NF+pGW5exZZmRsZbXzFFrQ4F3cI0QACs5vrwLGGa1lVWNK9ZnTEl0ZUbsk5RTHHCdps6u1jLKnHoxjouumjI6Whl+s15ZLWZyjVMRtluq6EFpxapC6elZBwnp+JtW7Mm4TC1z1tZ1QHPAHMxNGQbR5hAw3vSw3ZfsNr2SRWMsXRomXsKt5Lng5Jyf57pzY+BcRWItiV54IWptIWQzoSDVlbCRskuz44QmK1hWZNWT2bn9ybW6ScdjlE1pG3PRVY5rpfFusxBY3g9wo2I5yeclZrpwd6xWb0KNa/OQIPTLaUK7qrIT+s5qFjseW8wDapGvMl0L9FojmcMRu+wIim6lOExAaCinkz3MVwHdUDc9Q/s0IxZNr5ZHpSLK6yCpJUf5esRjNBHcpKVbXGvBYK6JQIv4VZRtPqgbToo3vdnP4lbkrbk8SKgoDcm2NHKV7VdkfcIrBWjFAVh5nse7Ez1V4DZAyDm7WbH+escO56a5pHM54Y9CSAqmic/3C5cxZcovghgi+UEXMOPkD2kX+QvdUDLZ8FUHV5aXLbGeWdtTlrXojuIuWtjvYmxzVKMWb62VRhYEKYBE465cQ99Id4gumUzkczQ7UCGBq77E+NXNLkvtbNOFNq9yzZyKRxdbTcEEvVFBIF6L/Mjw4Lr1LFLAt1HZ68Bdwh2QAOIzurBN2jOHOhQz95CvxAtpCRU7T0Rms44u4fSyOyrr3bHVhcX03GCcYedmK5GZK2hCF+/4QTt6UUE4OlFrKH260HvUhpGaNHoxG3qeVYCwQYPIEGOX7d0dHYGztfJzrVTC3lovff6qF2c9J5wGteEg6HMsNOl4S2oiW/GitbGcKA8OirDAt00csWUw0zv+mmwn1i5hKJNUjgQTcM21ow6hasmLK9YzyXlOau51tdyJKgWxMyWVyy0rD9tTU1w4jC7iaaqwwU6ZBblgVuwZP0VsfJU0JlcviRZcNjdLLPJYLLYgbk1RH5i86shFaJ9PA3sz2WrwI7qc0UyHaZeNeVNTVL5S1y5S5s55W+6KhmO3RrHqE60Qe8b0lifNy4c95VnLQs40h5pgRV24nSgbN2wft2UXEVx4FZszh7aorUR91izOoVRf8cXZmBqSIywnhqzU3ATHTTW/DfoGUE5cadI5dEP9kq6r2V6KnO3a15pVHh8XujKYKsfztUhvlB4/Db5WMYubtaotPDoWNVHOJpFCKEVPKtVEV66W6E2YHL8dereb9/sDbaDhdXvCAhXPVZPmCz/FJXe90nw+yIRmxtNHdmLBxgznDInJdKZDNTNnTkO3K4BTueJ0fbJiMT5RitwZ8ZyhC9M6CXyqrucXjHBWydwYms1aUuJzl3JoYQihZg+YgyU1JXETjXQSY5o0ilhUpSjDYcBzzknBMBudhwOo4HiS3IamP4/OXgvWXZqzsnfOSUq/0DZsFv2hWsB20JQDHA9MX+HjqVhv+52Btd6sH2akPiGPNlleDeN6Mb1WPQuzrTfsL0l+ctl5utjbOnM0GmMSn52ruRfiYTZzkqiN+7JcX3I38A8numr1RgtYqTOl82LYBMfBPMi6uanFfMCkPcpTqHrd+xTwa/Q0kVe8OXPtm2hSM6MVr6Hoczld8eKwVI63Y7O7nZ1qSxbHFZAE37InQWJYLCkfFd6lzc1SvBU8joMbbpFi1xK87aSoqx0FPy7U3QSL8jA6sQNal+SiDNHD5EjXVq3VRhM3QTAhT44W4KcpHMusW00qhiNgi5VM9ssjqMEKxWq6Xy52U9AM50w8zGXSvfTWJolzcoIvkpQpylSNrH2ktF7QUnF/KDepazhkvSFJGkVX6ImQp5zRKhyemHrfy+ExirDW1rvFjnPXRBAbJ5vuq81ecVtD4INGnXHUpHROXXvY2mcUv9KqvZh5ymAtDvNt5JHcacUZ1mXCTaShKpdksS5pinRp0Q2x4xlMbxSIxPYmY+cztuRoPLiE+fk0nRbLySG91h5YmBMZ3lD0Opc9hd/d/HOeJTOLSvGm2Tb08uKVfhLRk0DGQzrNpOnVStgTQ6e02bcFuMiZKDDY9sZsO6k3p8SCU26JsVjEnkSz7b4v+u2Q4TJoB2x9Chuz3fHNmV0OUbqTup164Xo2jivW0y/ELdEMj1SppWN42MZJPf+2mPQLCnRySDaM7EPIWpZXcXJojDquzOPaIRZhtJwk8tml/AVni5sLuULZ2YyQFXCIjqubMo2KEpWnJ3mCX3Qi1QbvIsQZk1W+K9/a+jApzWE11InQDBZJZsqlY9ILW3dmZE3ImAA8VRqDVbv4Qd8fKreTpp6MYzZB7SuGPdCpfdNXJyGQu73eMwfhtJ0L6cypJXEudEC69THc7W6OLE+U65WnOUa9Ussb25Kk38qzjO+GTczJgXohj6LVSfLBPzOqF2CJKHNzvGs3BAFH/2MHmGbaZldiWlD4CshKdsjnCxo98gLcadVkVTrY9dhC2N774Exx7NLCt3swZNWk4DeT1NGKgmg8QwwJdMWaA+8a8kZ0ay9z0w7bKna4v5nzKKpyIrlw4UzHdtvmLLYOUwi+cr5Vq7ZcaSel5xZz2tuW7nKBmy5+3QnSssw1b3Nb09R8Fu1PGM7ftHm32BAeBbxKTeerOZFh/DyumB3lzeIMs9gyN2eHpCBRo9FcGawOqH09cZlDTFmHV1F2Eu3xLdOWLZM1O+22d9f20rOZcE3vOhhtOMdGShVte7B2w/M2KxJv5lUHzbI9WgQClbnzyU0SKZqwa69DfSwcylu8WbgoRmbxdIZXEimjg4UOvR8P2srJrNvNs6bi6oCJe3ViN35z3U9WDdXcxCVsW567XLHkxJnLVjx19phklgujso5XWzisBF1ZHwBX3KzDIE/TyzzSzyeBW6OuQ7iTw7nzwnq1144ylW9o1PX4KGpXOyEv0EmzjObiOT3ZhXGY3PaXMjGJsN4sbmzBqJcpsWZcusHwNVVIcbCV9KUUD/UQzARCQr3TfJu76A2giThHsdPNja4gU+K8VKYmTci8vjkMwcqJFUfvZLAFK9xp15UjnFt3x+SS5GDCouzTNBsKkCqJJfW9Q/N9ataz4qBiVW5F+TLms8VAi0RhD6iNH0gQHLcOe3N3DjvxkxvoeutcOjwjOPhtKTpRf1jaPTMzSUfqG2m2O28TkS2ddKoL1HFqHJJDknhz7Co7yzJu+cPaTXetdZix26NlLa+CMD9cRcVbn3ljm15A6HbxlOJEjD872LaWlrlZkFqMzlJ/ulpfGkO47o75er3++8vry3gy/Txf/qsvk8fDvv9nZ46P48H3t073w2VguV/vsr7+Zc1+fn0pnRDq9ThlreLGfx5G/rcz1s//5iuLkUn/eFs7virr6vez+dryx98+eglTt6nqsn+rsri5H/a+QodW429BVG/PQ+2Xu4lJXt+ffZj0PEJ/q7O35xuvl/G3FMb3P8ANHwTjpf88fH59cXsYstCp3rAF8QbKfLT3+RJkPKwd34K8/PZ/ACimBqPnJQAA -->
