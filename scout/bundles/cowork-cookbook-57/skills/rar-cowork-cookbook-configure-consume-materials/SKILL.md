---
name: "rar-cowork-cookbook-configure-consume-materials"
description: "Applies a bulk configuration change to consume materials from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_consume_materials", "rar_sha256": "837fd8f6422b4ecbf9542adb595b5d024c5c1fcfda64c4a4525829b9d7ad82c0", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_consume_materials`. The original RAPP
agent is preserved byte-for-byte in `configure_consume_materials_agent.py` and in the RCI capsule.

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

Consume materials Configuration Bulk Setup — Applies a bulk configuration change to consume materials from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-consume-materials
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_consume_materials_agent.py` and embedded as the fenced Python below (sha256 837fd8f6422b4ecb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_consume_materials_agent.py` first:

```bash
python3 configure_consume_materials_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_consume_materials_agent.py   # or on stdin
python3 configure_consume_materials_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Consume materials Configuration Bulk Setup — Applies a bulk configuration change to consume materials from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-consume-materials
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_consume_materials',
    "version": '2.0.1',
    "display_name": 'Consume materials Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to consume materials from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-consume-materials',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-consume-materials',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '970c7057531209b8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/run-production-operations/consume-materials'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/configure-consume-materials', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureConsumeMaterials(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureConsumeMaterials'
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
    print(ConfigureConsumeMaterials().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8VaeZObWJL/KmztH3av7OIQ4vDERCySAIHEIUAI1O5wc4NA3AhBb3/3fUiqcnt7ZnYmYiNWdkUJeC/v/GXmo357cbo2LuqXLy964OQQ72RZEgc15OQ+tCr6ok7BryJ1wQ/kFXlbJ27XFnXz8unFDxqvTso2KXKwnSnLLAkayIHcLruvDZOoq53pMeTFTh4FUFtM95vuEkAXpw3qxMkaKKyLC2AHJXnZtRB784IMCpMs+AT1SRtDVydL/AeVSaa6yDLX8VKo6cqyqNtXIEhwcy5lFjQvX37+5dNLAr6/fPntxcucBtx6WT0lCVYP1tIbZ7AzA2KBJeUAbJCD6zKow6K+gFt+EELPq49NkIWfoP/4j7R36qj56cvXHHp+vr5M/7Quh9p4Us9p2sCHPKd03CRL2uEVYrLeGRqoDtquzifrNMCEefT62PmdUlFCf52efXwweY2C9uPXlwKIcNf968tPUFEDfnU3fX+dqJQff3rNij6oP/70nU7TuefAaydiQOrXb8/rJ1mw8PvSJLxz/Sug+nClG3x9+YNy0+ch96Qn2Pnyei6S/OODcFkX1yB3ci/4+NPfI+vFgZdmSdP+U3R/fhCOA8cHOj0F/+nT3ci/QLOnQu80/z7bErj1X9EELH9j9wl6Gurv0b7b/3+QzpIcBP6bxf8mub+1YfZX6Oe/q9s/2vAJCr++rIMsuYLocLPgC/TbN11lVz9/8L/f/PDL74D0/0pGL7rau1P4dnHyJAya9tu3nz8099sffvn5Q1eCWAucy7euzv4Wzb9l1zufHyz4XPXxx72A/yFP86LPofdIh34ryn+rf3+FzCnxv99vvkB/zJfpM4MmJd6YPkzwh5xpgKx/sONPL78DcMiBNp13fwyy/N//HZISry6aImwh3SsAAAEHt8klmIQ34qSBwP8pt+sA2LVJgGGf60D8Tx6eJC5C6Nf/9O5g+dl7giX8BoDBtyfkfXuHvF9fIQOQLOokSnIngzRGVb/mThTk7cSurIMmqK8ASNyhDT4DCPo8fQEACf36D6h+uxN4LYdf70CZPDBJWwkTHjVdFrxOOh3jIH9q4AHQDW6B1wHaWeE5D9htPgFdmyK7Ajyb9G/SJMsgP6mBskU9PEC4y79MxH799VfXaeKv+QNA59CjIDQwWPAuDvT5M9AozJIobr/mgRcX0Ifffv8A/Rf0j3bdiU88VIDiTw8ACUVdkSGQUUDzvAXOAe4EcHH3wG+/P+0KyOSgggF/JeFUkabNICLTwH8zsr5hPmMLAnIDYFxg2MtUSQAqQ0n7Cgkh9C4vYDo9mnA7LpoW8oMyyP0g9wZA1QHqvFsyL1qoAWHXhMMnqGuCO9df3dq5i3gBqe20v0LSSgVVosimSlg/qwbYXOQJMP97CDzuAyL1hwZavpF4heQpBqHSqZ0yrp0nj9B5+AVUh7ftgLgD5UH/NZ9qYTCZ6p4QD/OARcAy3tOlnyefg6p8AdnvN2+872ucqZYZ95pWf82bZ7A79eQKD4A/YBp1oDaDEvCXZ0g1cdFl/t1+QNKJ0tML/tMr9xhc/akHWP3QLSynBkIHiFFCXzsMQXHo/6u5mKRleF5jecZg1xArG5r9sOLUC03WfrRPoNRDIJQeGfO9/L+BxxuGfs2zBIREPfzlsfJu++eaBy6BzPYBHmh3+sDxwIoT3XtcTnFW13czfM3fwPoTsMkdmYAKIIlBkE+GeGM4PX2TNAaZOl1/L9x3P9b+pDqIPajs3AzERRgE/t0IbVxPufV0AQjSYMqzPk68+AetIEAdxAKgDwEhEpAtANDvppMLoCZIq7sX3pcnUzsEpPA7D0gLms3gFTqC9JhCpAE5CXqaaQ2wwoc7KegSABsDEd8t3MRO+RBm6k+fAjqTL4rJ9X/0wPPh94C+yzKJD6g6wPfAlv2ErX5we3j2Xc6nr4CwlykF75t+dPdTV+iPVeUvX/O7jO9wDjI7mwryH4wDgfC8NPeQm4CpAeACovahHoiEe+19fZTPR31+l+XLn5ryj/9a334viIcfPfcFitu2bL7A8KOIvdWwVwALMIiRpAya7/Xs8zPLPr9n2Q8kHxb6Av1rYv1A4hnPXyD0FXlFpke7xAumgH1+gBVWn5f2Z3x6+jXXgu/ufcbAhKfZAAroe3F5WwIqTFQH0bT4UWyaqUb1oCze0RU44Gv+HgLPBHkgDKiMTfGHxL1XWeDQh7/eiwB4lLeAtz91YlEwDSjZJH4TvHzJuyz79JI7l+B/GUwmkAcBCgwxjTIgWUBT0ybB/eq9wZkufhzC7mkE8t8vvkzZ9AmamtFP0Htf+Ql66/Tvc1PegVHn56mnnViCpeDX+9r3Cc8NXsBY1Q7lJPRjfJlaqWeL+2chpiQCEnvBVLiL96ycOP6JCPgSRUH9ZyLK/YuTPaGhaZ2pDCftW0I3QE6/m4AcuA0kGsgdAIkd2PBnNoBPHVQdqHf+pO53+31Xq3jo8vvdDO1jBvzt5Q0inj549ntgOcjFz81U8WAQooAhuH4EE3j2r3SCz60Az0A7AvZSczL0qZDAMczFA88N6QWOOb67oBfuwkcw3Ft4aOiFvkPgHu7gC2xBYbRL+6TjU5g3ifKIxm9TRU8mcQIkDOY0inn+nMAWC5xGScyhfQcnHcdHKIpEAEsA+d+3pgAMnzo+dJoM+N6UTrZ4qvrbi0vgYOUGbwTm8VnBtOkQGOlqsTuricA+WbDg5qaIdChWYf3RN/ucJ5ZiNOikFrBbUmQ83ZSNjXhaYy3rLK/FPvSE2WCR+agyFeamDVc0vJug46khvBmcK4UtRLyIOSN3ckXXGUzheKw0E2/aXV2Vq0wuM9zaHiy8PlQVOlJw117xxFAPBNakq20Su8lcpknB3aKsE5wXkVJVEtfEEsGP11XNYX5rl8dtdhgPmknWXsJ2J6LRtNRMk1WpXFK7v8bb+TBfGpm73hNBWCOonxvp6OdzPBk5jA5ggzHc0dnuktI0o/KUaa1BbITcrOz94nByWa/1tHOVneCkvil21WLHeLFxDkSV7G8BEWNI3KBc1xd2vauylRhsrCFpsh3AjtUQlINYEqbA9YdaUDXzciLKY7+IDLwzj7wI+wbLjZEs+oaFHGt5gbjOOsR8bnbST8Z2l+nxwRUq9rYk40A7Zkps16W2PV7pgdk322pEhkvMXcQKxxR5RBfLVWQphND2AtNRQVNFVBnwUmLVp3l3obB9y61wlcgSapdp8akSyTEYOPZoHjW+RLlR2xQRfErFpCLW7kneF+hlkZLn6HbbH0cxzeG4GH3UqNp6eTzEs0C08S2+PKfigbpqnKsHYlC1DWas89FTLvJtRXt4E4YysbI2zmXfVm1Pb0ax9dKFe5pd0kq4JRhqJ8wOw9sZGlRN39RyZHdEo68WB9S8MaXDzgQ0xHr7qDPpUdYMe8ATeBUoVtLhVCZ7hcPC5fns7SP76jM6yqm2LavwqaXNlSsVQ4tfF6rirBuDmicUiq0LeN+5u1Gp6wMqhUYrXPJdesxzwcKlrUNwu/G6awwac+cn1blRFSZz1y6H93slRygPNtSZdPPZGtVq84JiRpt7CRalLjcWV9IdA7ap0S5b1lg8DG7QN3OK5xr7ttND/ny7MjOW64+NJtvlUglFhjwhwOCLBhkOfbUrnZFF7ZTvDEvihlV+9rb9uel7ToBZ2k7YFT9Q0aHhVjf2IDWzfJRwj408o12QYu3tqhnf5ukla1PaVgrXX2NyHJMSTaz93W1Jr2M4LBfFBQuGDLWROQn7crs/sESeX2t4228sch3nAoLPRnleUYTpHRf9bDOoyPYWzzi0MszcuAarHX84HjXXQeT0RCfw9pTPdmdZh+sDJrBhOQo7/aYSBuuoPmtrdSzIRdDBKIKjNB8M0c1EXElVYVjkKqGkruqeuvkJLDdHpVQqz7HOs/K0PSCSqG8Xtie5VSudh1K+GVWGFNZQ2FU3GHFWzFuvOEgZdez5NaJeE1e9IKFOtAm3n63mYSIGcmzGYk4OC12U5NU2hpkLH2XY7sos57C5u0QzO45v+9VtqbpRbCcVFwbJ+dR5nowkl0TYIUuHaA3tvKp8sdxfU2R7PWxEH9msqMhKLU3CN5fyzFOjz5W6217aJiSafVnFvoDDKO2aI2IpITNWpeAEku+4MlnJIKxkuSLNZCGfvEBVw46g8bN+m6VzNjUB6JIXdLft6FNZSgS+pB0xzshyD5fqgUPjw3pndzIhG9ucF9TLVjkS/WozJjS3p+B0E7EFGWIro9l6s/B6Sm/wNttJYlhWXq7P98JsWS5TXOkZUToco5C7ogJPlGfpdHSrIl6s0+i63mFXrjnglUt1I6PZiBKxgnMo9eOaE01XFfxCS3J3ttEZJzp4ctTop6N/sNZW04gdjpM+mix17dhfk/mA0l1WhW01Lsbb1jD2+TEIQ/XcAODdEGc2WonapRaCa4cTkX42tzP5lJ/IjMVxlkrp3Rio8PUEUtT3mdE1+jwVTJoOdHhGtbhlzcnbLEQ2NEls4a7wbxq1vUTGTqRnR3K5E3SZOcc6gQd7wTJPe5s+Vhk+lNw+uzYnmjsUxXhcx8Gqwk2c0ZNtdkTNNOPWeD426onVPdI6tttW7Dgpna/SzBJDeevym9jgs40pxQW7n+08DDE6YzcmRMUVHjbanAkf/aEhcjHz4BMFI5G1E9rByldKq6gcLld4G+4sj9CQ1vHEy208Hhe4463FPOBV6mZvm9gjjMNlT8xZ6bI4txehY3lWElnvuqH9RLSq6xXeFM3RKI+iufeKqEi3azZDh11C84t2jozspkgro09MSWMP5X52ZrYJtXY21U4eqpop0cq1w723qtIM0dmVxBJVNEuipt6hppDTC9QvcsOeBbRktYKj8EgWWH5sDqZ/WtJ9hgg11+hHqyt6vciElb2vN0myQlvFRnTeGfxZZeq3Yr7H9ua2cebLQ3FoWEdCihNATU8+2CoaHBbZLtuOaVU5dr/UOXKpMya13vW1FV0OWZZRnmvs0d7hpNgr+9WsppoKObiSQ/UoR9BnUWojvG3Xc2oRuIfb1kTOu05aGHanLZXdrXUHKdN7x2xSptYUsjo5LrZlXNjPqjpuzhzfUyqfI7cy7zrHaU/Zfke48xjdLXdOF19kLVkR+E5S0l0VFIIixDKu40tdJXxWVLW0XLJ+kHSe0HF6XFlokqpnNYlEeY3KQ3yJ1J1YNWAkNVesJNdLh9dQJ9veIiHhVd0U8zOAPboYkBEr+C6yyHY3uhlhbtxBWPBjnm0jdC+mpEdT2xXqAzvrEmLnyYjABq3MrxGo9wG9FFN2weAIvlsYsaUi/HUpllSg+OczQdum6LdKrZjNzV/3plX7pOHGDNvjIaOLFLLHm6V42DXMMomQdEnD2nF7CNakzursTLK3V63hdotZYJ22a9+3uWJl+YbTxr0i4fsM7crbLK5XrJxWZkpGxMFYUfzMjsp1HRyxI+J25rY0QARwWOH5JsxU/Tr2OFqGRZ0ZzroRR75aIgLK6Bf1wq+2pGcaBUlXTqqL+WrFy+fLij11OTIcHZVI54lwsY6jsRM43OxwBrNkDtdhh2qkxkrznb28RSphKQE7FypL36ZxSqwUfocVo6GKnuxEqLCnVktTOJl6hjSrg+8oAz/wtpJ2zZw3QdoOhxO/3RDyeFmu+nRxysyFkmotU8RzcZfeUtPaiMCJwWkUUb5k5StdzMM87A3pWG1dsVHzpUVjvGybSnE2m9bNirNF3TLBDbpZm1azLOdEO99g/kkrcQelY342HFoOI8nzmAWXMHW4BYcdlivFF2eiTjW8eBDDVGGi/Q0OpCRytkrSlOfdOeDos1B6btkz6TLasXYr5EjCiHV2KupFCR+I3IGjcr5bt3An5UlWHFmRCPVqz5msvlpWZqAG7MzoFNZaLQuAjchSTTanzCuIYNklia8kNl4keCCe9meTbGfC2tJukh3Pb5iYEoN6CEVDkUCTpt14T8XSxI+VQiFEQtvyXmi2aSEO8MYfZ0eOLY00tBgs9dKRD8DcKixEEil6L8qlnuCYm94lTSr32yW3J+1TrlqJdMK05QYZQ2YDem7z3GoW63dRO0dxbcu2oJhhi/TYkKyzIEmZ8enWlK/RAWnsIkJISSD1Pc5HIu2Ul5NcIEuORdPNCr4J2k64Oc05CgUkPfflWLgCIbqbpcAv255NtNiUmKCxTpcsjfKB9cvh5B4XIqaSJbs0lbxlmEMkn5yZa4tN1yVhv6o4cZ8LDYkTHp6xN/oomMCgVk0p0dA0nrwEA8xxFqfmifNoYuQPVKxUi/EoqMe6rpLZca+tD0tupPOzbtY3fGg1ZbUPeZeyxs7m8y5TxI7XyHBoM9zn2uzakSZpVT2Krnxa9DYSWXeUuqKuZOTl3SgvInujYNe1t+g1ztP7q8dtG4Tg0plziBvEMdTTvJdWQurv5MwhXXR9wwxzMcrmxWUHjxIMdke1vRiZI3VFcptF+dyZn+y9em3jwcK7Bid5aVW2yBwJZqN3Cc/zrXtEbQHWb7TDM7fQ38irWz4rMnWX1fK6R05dmBpBt+dA7dkAM6y7BVXPZs1tUNTBgmHSDCmG1zOFz+l8PgPRjOMB0ZLlBr3FFin6zdZhlJ7z4ptTVCpDItaGvS6Fyxn0SUUDF1YgRD1LLDBcw/fYeWPkiYT1MNNkZ+lC7TcSLOTXXPOCmW3VFwNAqSFQ3FELTkcNVzZXY0APxna5P6FefpUUb3GbJwY/3zdDE9Uz0ATjo3DGQ1E5Z4aPrMUNpcbXoIvALHyaXbO1NoRnGkX4UBhzv0HOzmEVqLqmcFSA1ATZbw8xP/TWfm5pbRqoGq+cQ2+uwUZVoyp8VFNCuni38rzB2dFmDoStzOe9sdnT2ALWEPQQkNVxhjFNFC2bLY5LcesGQ3OlF1ZFt4cLBShurI031jhFlq7qsSizzsnKSGarMoylfEutBAePWa0TraIl2Oaq7Tw/RGskWS1Hu4cNZDzcPBavB1+1WHzM9hq+yJebTWrZ7A1Ua7eTKY0Xd70+OnniX1nsMPOWfX3c5rG4lRQjuGpnP4CDqA9GzLvRxbrYO3tnPjcIMLpJwjpejcqJOePypWUM26V2jNdF9TjvsaKrC7mxz2F4I7zbWudwLsTqIm8xZeHtJBMl1YPnIzuJ3A/HgVgY8oUm6Hypsp5Cz87n1RVfnsj6WlfbmUHQxMLTAvwg2YsuvjWUQsXNxqYOsruPFEp1GXtjUlw5mx+YPCsavuhQthd6rh+UjWu1nqVEyLiZg97MRBDyOsvqVJb1k2mxhNKBhqOW8V6a18ulThUXWkA218G8iDgjWWeSD84NofCDurkRS2zZVLPqBOv67SgXPiWhMMN3cxcvo9mSvMFluOMi5EaW1waMtOacpvfMSPXjPFTHOlW3zFwLBz5hfQc+wgHF6NylPbRjmOO0PXNP53naVqcrPVvBMEMKLnu+KotEHundXLV1id0Eh8OMkQO+apzOj2EwoyxJtFIxCfEkRKY3O/saazAvRnzEZgrRXZNyAXfcwUAc9Zji9FKgBp1Oz9caPW4XfuDeNqSJyfuLQc4UZl2csIBhZC1qxFN1WQjN6PU+oxiyhbaRY/nuvNUS2qeJc3cbQKlf9WhxbW7UfFOtQKtDqdzSS1E5WAZ0T0VLx2bByOjtDJtdhMtsmYVhekE2MgNm3ZJNt2qmY87iEJSbfe2c02K4IfbpZlIIgiMYZYQbS0o6fbyWymqW1Ad7kYBU79QsLEt3XqHLsoW1zKd7mR0U7GDymGPdjhuupc6UyXAGXHSw2EpwCwb0sessxsaXmEcuG3p/uGhlyQuiYRNgKmiWnli5Uk+z7pmcNx6I75NyIk0whXiUF3FouClUepgjVeht9wzz8ullOox+Hin/M6+Hp4O+/7PzxsfR4NsLpfthcuD4X+68vvxT0vzy6aX2EiDL4yS1ybroefj4P85RP/+DNxDTxuHxnnV623Vr347aWyea/izoJcn9rmnr4VtTZN39EPfTi9s1098pNN+eh9Uvd1Uu5XTy/c7reTD+rS2+PV9ZvUx/RTC9wAn8BPB/XkbPI+VPL/4AnJF4zbc5sfgW1OWk4fONBlAMe0Ve0Zff/xuw90d7eCUAAA== -->
