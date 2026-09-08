---
name: "rar-cowork-cookbook-bulk-update-conduct-competitive-analysis"
description: "Applies a bulk field update to conduct competitive analysis records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook, approval p"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_conduct_competitive_analysis", "rar_sha256": "0a596ddd0703bf624894cc5798c9aa067ab02cdd9da1eddde466ad26070b7cd0", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_conduct_competitive_analysis`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_conduct_competitive_analysis_agent.py` and in the RCI capsule.

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

Conduct competitive analysis Bulk Field Update — Applies a bulk field update to conduct competitive analysis records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook, approval p

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

This entry carries the upstream recipe itself, under its licence and with
attribution: the prompt verbatim, the prerequisites, the step-by-step and
the expected output. Toasting made it deterministic — the same call returns
the same recipe every time — and callable from any Brainstem. The upstream
library remains the authority for the recipe and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-conduct-competitive-analysis
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
    "approval": {
      "description": "Explicit approval after reviewing the dry-run preview workbook, before changes are committed.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against; defaults to USMF sandbox.",
      "type": "string"
    },
    "new_values": {
      "description": "The field(s) and new value(s) to apply to those records.",
      "type": "string"
    },
    "operation": {
      "description": "What to do: run, prompt, plan, checklist, describe.",
      "enum": [
        "run",
        "prompt",
        "plan",
        "checklist",
        "describe"
      ],
      "type": "string"
    },
    "record_ids": {
      "description": "List of conduct competitive analysis record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_conduct_competitive_analysis_agent.py` and embedded as the fenced Python below (sha256 0a596ddd0703bf62…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_conduct_competitive_analysis_agent.py` first:

```bash
python3 bulk_update_conduct_competitive_analysis_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_conduct_competitive_analysis_agent.py   # or on stdin
python3 bulk_update_conduct_competitive_analysis_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Conduct competitive analysis Bulk Field Update — Applies a bulk field update to conduct competitive analysis records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook, approval p

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

This entry carries the upstream recipe itself, under its licence and with
attribution: the prompt verbatim, the prerequisites, the step-by-step and
the expected output. Toasting made it deterministic — the same call returns
the same recipe every time — and callable from any Brainstem. The upstream
library remains the authority for the recipe and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-conduct-competitive-analysis
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_conduct_competitive_analysis',
    "version": '3.0.3',
    "display_name": 'Conduct competitive analysis Bulk Field Update',
    "description": 'Applies a bulk field update to conduct competitive analysis records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook, approval p',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-conduct-competitive-analysis',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-conduct-competitive-analysis',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '126af7804d6023f3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/analyze-marketing-operations/conduct-competitive-analysis'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/bulk-update-conduct-competitive-analysis', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


# The toasted capability, generated by @kody-w/skill_toaster_agent. A licensed
# recipe entry carries the upstream recipe verbatim (with attribution) in
# _SPEC["recipe"]; a metadata-only entry carries RAR's own method for that shape
# of work. See the module docstring for which this is.
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against; defaults to USMF sandbox.', 'new_values': 'The field(s) and new value(s) to apply to those records.', 'record_ids': 'List of conduct competitive analysis record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when conduct competitive analysis records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to conduct competitive analysis records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to conduct competitive analysis records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook, approval p', 'example_request': 'Bulk update these conduct competitive analysis records in USMF sandbox - here are the IDs and new values; show me a dry run first.', 'inputs': [{'description': 'List of conduct competitive analysis record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to those records.', 'name': 'new_values'}, {'description': 'D365 legal entity to run against; defaults to USMF sandbox.', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change the same field(s) across many conduct competitive analysis records in D365 ERP and want a reviewable dry-run before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateConductCompetitiveAnalysis(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateConductCompetitiveAnalysis'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against; defaults to USMF sandbox.', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to those records.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of conduct competitive analysis record IDs to update.', 'type': 'string'}},
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

    # ── recipe entries: the upstream recipe, verbatim, deterministic ─────

    def _recipe_context(self, kwargs):
        extras = []
        subject = self._subject(kwargs)
        if subject:
            extras.append(f"subject: {subject}")
        for key in _SPEC["params"]:
            value = str(kwargs.get(key) or "").strip()
            if value:
                extras.append(f"{key}: {value}")
        return extras

    def _recipe_prompt(self, kwargs):
        r = _SPEC["recipe"]
        lines = [r["prompt"]]
        extras = self._recipe_context(kwargs)
        if extras:
            lines += ["", "Context supplied by the caller:"] + [f"- {e}" for e in extras]
        return lines

    def _recipe_attribution(self):
        src = __manifest__["source"]
        r = _SPEC["recipe"]
        who = ", ".join(r.get("authors") or []) or __manifest__["author"]
        return [
            f"Recipe: {__manifest__['display_name']} — by {who}, {src['source_name']} "
            f"({src['license']}). Source: {src['upstream_url']}",
        ]

    def _perform_recipe(self, op, kwargs):
        r = _SPEC["recipe"]
        ref = _SPEC.get("refinement") or {}
        if op == "prompt":
            return "\n".join(self._recipe_prompt(kwargs) + [""] + self._recipe_attribution())
        if op == "plan":
            lines = [f"Steps for {__manifest__['display_name']} on {r['platform']}:"]
            lines += [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "checklist":
            lines = ["Before you run it:"] + [f"  [ ] {p}" for p in r["prerequisites"]]
            if r.get("expected_output"):
                lines += ["", "Done when:", f"  [ ] {r['expected_output']}"]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "describe":
            lines = self._provenance()
            if ref.get("when_to_use"):
                lines += ["", f"When to use: {ref['when_to_use']}"]
            if ref.get("example_request"):
                lines += [f"Ask for it like: {ref['example_request']}"]
            if ref.get("inputs"):
                lines += ["", "It will ask you for:"] + [f"  - {i['name']}: {i['description']}" for i in ref["inputs"]]
            if r.get("business_value"):
                lines += ["", f"Why it matters: {r['business_value']}"]
            return "\n".join(lines)
        if op == "run":
            lines = [f"{__manifest__['display_name']} — run on {r['platform']}", ""]
            if r.get("what_it_does"):
                lines += [r["what_it_does"], ""]
            lines += [f"Prompt (paste into {r['platform']}):", ""] + self._recipe_prompt(kwargs) + [""]
            lines += ["Procedure:"] + [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)] + [""]
            lines += ["Acceptance checks:"] + [f"  [ ] {c}" for c in _SPEC["checks"]] + [""]
            lines += [f"Deliverable: {_SPEC['deliverable']}", ""]
            if r.get("tenant_caveat"):
                lines += [f"Verified upstream: {r['tenant_caveat']}", ""]
            return "\n".join(lines + self._recipe_attribution())
        return (
            f"Unknown operation {op!r}. Valid operations: "
            + ", ".join(_SPEC["operations"])
        )

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

        if _SPEC.get("recipe"):
            return self._perform_recipe(op, kwargs)

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
    print(BulkUpdateConductCompetitiveAnalysis().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916adPaWJbmX2HejpjMbNnWjsAdFTHakZAEWhBLusKpXUIr2kV2/fe5Al6ns8vVUzUxnwbbAUj3nv08z7kWv785XRuX9dvnNzNwioXoZFkSB/XCKfwFWw5lnYK3MnXBv4VXFm2duF1b1s3bhzc/aLw6qdqkLMB2uqqyJGgWzsLtsnQRJkHmL7rKd9pg0ZbzXr/zWvCeV0GbtEkfAB1ONjVJs6gDr6z9ZpEUC24qnDzxmgW+JBfC/zRZdfFzFkROtggKsG1aHExV+LBogH1uOf6yCOsyBzo9YHdQf2y6hxX+IkuadlGGL8kLiWseHhXBsOidrAuaD4shaWOw06+nj3VXLKo66BNwe3Z59vbDwqmqugSrFxVwNhidvMqC5u3zr3/98JaAz2+ff3/zMqcBl94Y4PLh4Sv79JP9w0365SUQkjlFBFZXEwh5Ab5XQR2WdQ4u+UG4eH37uQmy8MPi3/89HZw6an75/KVYvF5f3uY/BrC2jeeoOk0LfPWcynGTDATn04LOBmeaA9p2dTEnowEZK6JPz51/SCqrxV/mez8/lXyKgvbnL28lMMGZ8/nl7ZdFWQN9IDLg86dZSvXzL5+ycgjqn3/5Q07TudcApBUIA1Z/+vr6/hILFv6xNAkXX809z750gcwkVQCEf+ff/Hqa/hL3CsnX5+Kfy+rD4seSZ3/+Aux91qQL5P5YLIgB2Pn26Vomxc8vHSDJQeEUXvDzL/9IrBcHXjrX1D8l99en4DhwfBCtV0h++fBI318X0Mu3bzL/sdoKFMy/4glY/q7uW6D+kexHZv+L6CwpQAe/5/KH4n60AfrL4td/6Nt/t+HDIvzyxgUZ6JLacbPg8+L3R4n8+pP/x8Wf/vo3IPr/KMYsu9p7SPiaO0USBk379euvPzWPyz/99defugpUceDkX7s6+5HMH8X1oedPEXyt+vnPe4H+Q5EW5VAsvvXQ4vey+h/13z4tbCdL/D+uN58X33fi/IIWsxPvSp8h+K4bG2Drd3H85e1vAIEK4A0Amvk2wI9/+7eFmnh12ZRhuzC9smsXIMFtkgez8VYMQBb8nVEDwFxQNwkI7GsdqP85w7PFADB/+1/eA/U/ei/Uh2c4//oE8q8vFP/6HYp/fUfx3z4tLCC/rJMoAZcWBr3ffymcCOD2rBvgaxPUPcArd2qDj6CtP84fZsz/7Z9V8fUh7VM1/fZA8+SJgwYrzRjYdFnwafb2GAfFyzcPUFowBl4HFGUlIAnAS9kM/sCYMgMU1M6RadIkyxZ+AlAGUNv0kA2i93kW9ttvv7lOE38pnqCNL56c18BgwTdzFh8/AvfCLIni9ksReHG5+On3v/20+M/Ff7frIXzWsQck8soNsFA2d9oC9FqXg2UzJwKQd/xHbn7/2yvIQEwBSBpkMgln0p03g1pNA/894uaG/oiRy4UbgEiDKOdVWbeACRZJ+2khhYtv9gKl862ZK+ISkKYfVEHhB4U3AakOcOdbJIuyBbzbJk04fVh0TfDQ+ptbOw8Tc9D0TvvbQmX3gJnKbCb9+sVUYHNZJCD83+rheR0IqX9qFsy7iE8Lba7OReXUThXXzktH6DzzAhjpfTsQ7sxs/qWYqTiYQ/VolWd4wCIQGe+V0o9zzufBA+DCc8ho39c4M39aDx6tvxTNqw2cOngMDsCUaRF1iT+Tw3+8SqqJyw5MNnP8gKWzpFcW/FdWHjXI/nfjzjwtLITHgPQcGhZfOgxBicX/zzPUHBVaFA1epC2eW/CaZZyf2ZrHyjmrz0l0tg+U7LMz/xht3uHrHcW/FFkCSq+e/uO58pHj15onMnY18MGgjYd8UGAgW7PcR/3P9VzXj1B/Kd7pAli7eGAjKAEAFqCZ5qC/K5zvvlsaA0SYv/8xOrwHCQQI1Pii6twM1F8YBL7reCmwqp57+JVm0AzBHNghTrz4T17NCQI1B+QvgBEJ6EpAKZ++Qfjz7rvpf9r4nJDmLY/psQMtXD8EADuC2cA5dXO6gHntc4oHfn5+CAFu5FU7++6CJgKePi8GdXDrkiZp50w/4xpUALQ/zu9PT+erwViBvgHBAt1RdSC6j36aoSYH8w+wAUAKaK88KUA9gaC8gvAQ6OTBo+zeB9anxMfll0PBowlnInvfODsy75lng1fpFtP3GGL9qEyAvHxe8dD7Xyvtm7ZZ9oyjDcBCoPH97nOI+PScA56DxuJd7ue/Oyb9/K+dpB7MfvhzAXxexG1bNZ9h+MnG72T8CbQ+/LS1eRDzxyc6fHxBw8fvoOHjOzT8Sf7T9c+Lf83GP4l49cjnBfoJ+YTMt5RXjb1eICTsR+b8kZjvfimM4A+sBerLHBTZnMAJTALfiPF9CWDHqAZYBRY/ibKZ+XUAlP5gBpCNL8X3RT83HSCeIpqLtCm/A4PHhAAa4Jm8bwQGbhUt0O3P82UUfJqPZbP5TfD2ueiy7MMbAM/gnz/TzVyVzwXezAdC0EpgamuT4PHtHf3mz38+LfMjwFgP9MY3gHRCIGPxBNC5eea6+8e4+qL1l+cPxpoJLmlB3GaX2qmafXie/uZ58QFdY/v3luweH5zs04ILAExmzff98CK7mey/a9tn2EG4PeDsh8UcomYmZxD2OQ5zyzsN6CFg4g9teXDR1ycX/b1B3Mxaf6Kr1yThRI8W/w+AJ6HTZSC14MZMZe9M9kNlgK6+Punq71XNSPEg2Z+bX/7MbfOFecYAVPjQD5qmeXe8+aGeb9P636s5gsFoFuKXn2dHPrwAF7yDE9aHxbfDEgjl6/g6awiKLn/7/Ot8UJvL7LFl/gD2gLdvm779R4wbvP31B3Y9bf6a+D/wX3kx/D8xWDzo/0GHc7p/EIGHKsAXgHVnq/8Ixx9GlY+j5GwUcKJ9/s/H72+geRwg03m1z+ssApYDeP3YzDMXDIAGKATfn5AA7v1fn1JecprYAdMxEIQ45Hrp+z5CIbgbLjFitSY8j6TWK2/tOMiSclwE83x/7TtoANYFxHLp+NgSrHcpz5/tegLM12f/AZGzYSAkHwFGBX/cBpf8l1NPJ+aIfTsUPdDi6dvvb+6SACs3RCPRzxcLQyi4SLmTfILqZVCqKrP1EmubH7JcgOWlGqAYhsURxW0AIAzi5iDmk7CtqyQ3h0nx7bjUSHYzxZvchL1ltW1J3vf6a34czFoUaD7L0GVrkuHON9ELVXAHypLZmtNLq9KqnbBt9c32LKXJxnecUGyuW1hgp9PV3Ewn48DHow/D0NUf0/w4plnJn9NTj8ITpO0gRZCtrrxcFVVFroqtJ0UHmedtyyoutVqWcDKeoNX+hGRGLa7YXIp55O4mARz0RTnyViWV2Wnpmfdj4NZCnvP6eN+GwAMy4c3GZzdm6xyaewVxjambiTsYG2JLZJsSnHDNcfCGEkfwuxoLF+W6KnuFlFdQa+cZuTdkJgvOtSHFjWplS6jnYioIlY5SUiKA8Y6I/LDXWgnLdKZNDV2oGkSGqKNjLrecez4wWT4crvx6WK7YaNWqApWqbamd61CK8Dsy0mvvluWExKSMeDkT2kkePXWf0bIlF82tHkYr5cWdTk54PnDGFs3qkq6gLXdX7C0/igVh2bkOMd3uVNeQNvBBuoMdezWxF1nfRQKzo9WVggYj29jOlEd2rIURa+iJnUOmXEl8UGsG4TjoBpXVPtk7dDSVdLzCE2t17rd7Pz8FO3J9RurtMJmGlvbyUlLLLL23eyZKrKMpimnFC7qgZE6mH7Cd6DnEBnIF16psmy5djV9lSrG62YYjOEYgIdDFsgNqe8InoctjWL7KjcTqSK1IZnRFT0ZdAutO57jlRwmSLuzmXh+qSCdpkbosZcbuZT9yd6Wj8dzyVvhJY3I7hBc5KdDDuwWJtMAZDWWd3OSoL+3oJraqI3b2mTtmkTukGUbdsnOC1KDw69O5Eq5a79tVfvbMJg4T5bSyr13lFdtLioWxhLl3YblFVL7nTXibagy/OnTIXnKF6+A41KbcZ/4R0u6NmW8tdV00JF3EhRNwIxSKBxe9qkzk5ODfVYiwhqVv3o6Wi/xOuQWh0UtX2A7UXT31sBdCZ+pOju3tAOv+WPDLELa4NY0SO6Uz7VhWhQujnXctzlZp3O+ojcMaeL5NeuROoxcm80+7kJYimLejloFAjZ0I7nCUTUTN48uuj+0u6sytJWwL7hIU1IVFRRJnDrKUKmdLvC0tGolFPkXXTDZSUaAw3i73Q6WxLc/qIusULXGVOfdKMXg5Z2dafjl7YTAqwyZNb6vNiWzXnIay+TZTJNTMsnM1ERczS4lKR3opqbQy1HMm7PLAQKrCcxm3Kw+QchwP9lY3mgyP8XuudyzissvQD6ub1sGZ4G0PI4RvS4kezxi2rBAyYrxrZAzoseKtI3LKlQsvw8idZ/PAbqoCX7Ihm9zPWZ42ymZ17KVzZtDslF4vemhRbHfpBSJpXDnQKVvJsRMTQ3o5wkmt+ZR5H6tpS5HwNuIB7WWs6Q+rzG0a3loPtNEz3vJmq/uWFgXyqF0YiZGiLBZDy4PISg1rgFj0TdvgFbYUYSGfbkso2K65E66YKi8ksDfIcAyw7RS511Wge9oek8M4v7hnodaJ/Gqwvk1wTOacrU4UQW9LzFRimhBkUYMkYuqQxziA1vYF8zmm77XwrOuHPNgTnQId0zAPRQW1U0Y7TcRuA3VauTlCrqVSinoeK4LDI1y+F6Sysb1TK67Oo7jOVlfOwdc3Yhf7VSScN7ToRPdkjfCXoxJdkZ71HLbjrHIsUmZp3A7dSb/qF2KaRB1SJd6R/XGwq521Ot43g37kzd2aPW05mOcPksSPkyAUGraz1KVu5Ou8XuEBNOlaCyU6VwmkuE+1Nl0ysgZB8Un1I5sNjZu/zfqj3V5YmTDMC3+40J4ZcWrLI8uoTTpoMLHiYI4a29DtZGM9klbX+MTUhZTjg7bdaQJNrnbi/QYNQZ0lp2NH4+RJ6NusmsZLfrvH/t2M7LxA72FRY1CHXOjDqmtGi2JUZbXfVnw5RFCV5kvc2etnohn6nMvHvoGdGxeePHWHtVd27F3BXm2WexiuVwaU1CMJr4KTwxxKanJ6Pc99SNESlhYxXTnydLdJjVEozeFWo8fSzjjR9KiVNnKcba/rlLfx/Sj2KYnnd4XO90h6jcJjowqQqqHCGbulm2ZLyoTpVb2uC0KSO6FOkGySlIiMTFsfq5LBkaYroamwq152kOFX4SDfKizNXX0640EvsOtzl/tXk7kIsYhN4vocJxkp3rWz7JBhdjmIk+itNxwGizRdSI7aWqdtSVYVFXK8WCktou5MUZJ2DnqmRS/Ux9TFrEg+rYldRHJXmU9dALQJkRpKioOy69anSUN5ShaHm1FatEGvDJFnxFS7bpKNEkZFofC1VsJadLKiGk6wk8RfYzbT9eMaPaHxgWkyOu28q+dFGDOEpkrB60PZJjGSOyzWMsKEHi+H9Tbd0u22vUxuJxWwRnaghflms2W8bShxvCbh5qZZhSUCQHFSdmxieeK+GkLGihVZHb1Ew8dLVgnS6I2FaSmDRh8xWsx2ByxRlpdqL16FbLCnMdpaYnpwqkBYH2rRML1LLJUNpbTFLffYRoSLa23wSjacB42UTXg3CEQlVjcAbQSycSDR8G4KFTkcfb7uAoeU1RS/IGrsx1qVO/ZSusBWGcuESvLedIL529Wrzn26VIQpG9bTfX8wvFF2dlLQbFfRzZbqxp6SoLRbDyCv5hxEgIZCLip3MfOuSxvWVLPgzahZinu4unQSHRC1lh/VkTiqXbsa+dOBjHUFgFWDYCnaX5J7VBl5kGM4RaTWWWJEpth2yQYbLrYkNC2zpm1d3k6U399Tot9be+94n5g0xq/I3WB83w7ou4BNAqKItS1LaLsfJoDxnCpHrUVEHLnOtqZ59G/TKTUPcc5qQeQhY2iLACrW9EljUL8cJplPdi070ZfRdFely11MyNGtMbDhli9NvjcviId1tBPd0sbWbdJiiLL18nONpzufJzo8unKiHC0hE+HPOIx2unDbhExyIU85tW8z51ZHnMmWtHkUbM02e20TRPd2OGq3k61h9U6E2LCHIcivjiIlIyIiFVXaXPZOgBdLd9p5pLNP1aLg5NZR0qIzuVDCkxOFH9Jtl4b3sWD2hr0SpUwyhVuGynR0M0xZOG5PzDju3M6UE4IPXBpVPcOOXDNsCKhUUs1GtwdQ+bl+4atNk4QO3olglj/EdJcuWUKir3wJ5itGPt+apXllyvoIkU1EJqf7gAfH7p6eLa92rOnYdLc7drpJO5OX3DPMGwZJMANpGnzj5DedCSsnHWViay5v7pm9rv1rdKwOmCpPGG+PIwk1smSbNMq7Frus2ZOx2ZECc1EQNLM8XTqDCNLKEWOx9TLap/pZHephI6JnlKK0rKD90dCtHcCEVRQiFhxtq7V7UwyyQLbTCq2OMhP2Y2I4pNXWPXuD8kPrQIHBsTF5bhMRCVPEN0OCZS6hIYQH1aBM9LTLaiKjM4LZeJLiqT6mWdeRsteHKCUD4hyhq9vZV3Eh2eaK0kD5cNNWRNOiUdetvKMjNG430s7ycoVdz9uZ8e62TW72mPdrjsSNOBcSQhuS+3S/3GTB9e6EdWYQBj14Kuc0m77d71M0v2mBf85Ggbyy9TFZ6YXE4MXJXZ0tB8pDxDjdx1PGBvyaZYkbuWPWLK/r8CBQ+t7nKql3XKvzrXCw6+nUOqdIr6/iNpcQMok32hG9JpN2de43zrPk6yrDwCzP26Hk0edJPgd6wzRBKC5Dk/WMddJsYsHC3CiPGdqzsSTyk/tVDPeb9eSd6tXa693j5XYwOKMAdaNYVyW3yhVf6TUQXsoJC3q34ENOZid1LShV6LrCJrz0jOWMUH4VPZFqD3Dl3CvUPjSd3fLYGssu52VjonsqavAVZ9qqEkLJZr9dQ4HQl7CXmzp5NvVjOtZqd+Xl8tihtzZaR1C0gsubPor02lBx64zsNyVi7QAfaMUh2fnH9T1dMWjMVjuZs4F7OwkOGqM7CLRSp/S4HoRKAwe/hq223ea0izsoOMBL2FAlp9JdTMEMOlFz1FirUQgOd4hZFRhLbzwWPXeU0wUQIpTHS3RcFUTjHjG57gx0xVPT1RraQNLjzlxeWeOGovIevifNKVY77oDLp+LYxDCMbY49C4usO55kmWdvGlInF4pyJIgV93h+uBPq3ua5c0ZO69Tsu9U+50uATh22O6yieGNoGFphiorZJ38jkyuDSlJZN9DUw48nvWB8PCtSj5KsFtGvOJS5RLG7b912u0UK0Ob+6Y5EvowenJD3Sjowbc+BlYNfcfG4lRjYgjKaDHbGgdWrSo3Ru8LI1k1SLkemDfutiJl4uIHIFXvhSILbtQGOQZ51Uny8W6tbfsBoZ3MQ0vqyI7bRVEMNn0xLNYFXoUoTPCdgXZgat+48cZl1kA8rDbnXZCsK2ZjzDGP0iI0NAyNXuWWcml1glzWsWrcANXBLHNxxv1ux+LnYy9WB0kfqxMI3mqx259W98NZFEKbdtV8rTa1Pe+K4InaaQXZHHL3494tbn+hqjy29u+LuOQhylbXniwFm5SrFj33f9TsCuR0VnqrQUTiuK/i82djHohbtvrlCLJKaFwFy+Bo9AFDfG9PVrq1NsNm7Q3cLwzPk2grFkN0uAwP7iOBBdmmEwIEd9tocQSv2e7NdWxhKpnRldgFSHbK1IDlNyG5vbjPynbBUtzZmeX17h+7RWlFch6XWA9wKPnWjNqdgNALP2hCX46oDJ7B8k53OSCcTzm7ECamlJ63FmXTv7vsVhcPUFiauR6K5qxl3X6FwEg4ASM/maIWbWiT1UxdtjoIYdOSZNKOLUIxLhV/dr0rFQvmmE3rHubD1WpMuWLM5pFolIXtvhGnDlCi5s9CeklWoWYuEdsDau3cni7LWAJff/ZYhMamERNJQDtvrJYOOq8EYN7aoqD04769CgjK9Y+tcDFzv4MSq44QooBVVV/UdwRNJmYgIwu+t0uT6eK45JHVqXEl5HhZIR95D9WXt4rcCz5VAMDwtgKuDzdVONk5tPU9Mdb1U/X6IjsOUHByd4xNjv7kShRV2U7NUXSKRvW3QtgYZj76xk4V8vKDOEoz3AUX39nWj3pq9Ll4D7JwG+DoXbCjGDisV4JmK951iM/fTklhLx+UooY4pM4cLX/ZMFGT9chsR20KV6St6zeXlcrU6tBdvd6yvMi6Q0TKVKwuReZQ5LB36iCdrAtHOk7+6eKREtAy2LsW7DPvnAFuVEWWmRb8kw/2dSKb1Cr/7ISuPp6Ro46Rb+7mCjjajBRwl3tanQhpAgjmi624WB1tnf0qd3D379ZitQVDoQAy34algG9TfeJXQSVi7kXbiROZGARjVV8sb1FrBOmvAMWGFJXnc+0cEA8cV3W7ydomSA3bemWV0h1r6ct7CA6FhhLScOrqE9wersdA1WYWHzr3CdZ557k26NwOJH/NrUFo3rGKJka3vJ6nN+1vUm6gQ3zZiYykccjwpyLY77Y9uR0vXm6jcuP0RbkTmQsPdFc63VWoz/OU6ePudeoNu6tIyN0skuwgXwnAxWtt1NbmOCby3sCIQyfURIUtsCKCAnFZsch7hHAqpg9J5Ae4w5l25g6KvwfBOHTBIujLUcu8QS7rA2QBvL5Tvoup+M54wdMkJpHFDSBTapXukg02CPjD3pXnDWcEddivpsCxyR5bzGlFdgcqWNZYG6jZD62Ib1buOa3eHKdREyvCh5Xqzmq44h/nWAE9KpI26V2UXDmVucXjsxs2JO8tGfoS126ZtjH6zz0b/TF8alrwwKw/ZGuv0uAkNbqfcUS62OEjfuvoh8AtZH20yjU97OE7jurdsc3L2FbPZ0DGcNSfROkOhcOk7fl1ocnNyxWS8R6saazQ/VgsIsSkB78IQQ2iMJnO3PHGDzm6zDa0VfhTDNwS+RNSGINTbvrGNcrunqDVEwGSEXd2kH6YKZqLqiIN2RSAkvEypIvdX/VoPo3od/Y6qciwTg3BC09rVusutsFaFnaRtRJ268yW9QrByvgs3Lk/O903vtVfm7i3vWnvP9uEqR8EZ0tug8jknrg5c01B2MCL0spEG+IinfYfz2h3S13tnO14UKNC35aFpuUMPBhzSc6i1wRzSA96e9GoPhnGOyzUCPuerNrFrcECkYhlZQmmQbbJdSNhiNTB3eHs7xuuJQkc5Iigovwtjv5Q4iVMEUaqR0y6gLSNytDOx3KwpGOtvnsXvShsJTtsjypIugx0oEaM62yrEHQyRvhskFkbbwyE4oaHi6yuOQsFxUqP90o/vXTSEI36/WbgjxkYrxrckVsrwiAbg1LLOuuM96s+9yqUY5Ueke+pvxr3YMbgspa1F74TpMml1sbdJJHGXlFp0mh1zXJmcZcalElVn/TMlS0qehv2aLhmuHc79ugHSAkfbnQ7O5TTsxqOvbVxK9FbaBYXQJR2iOtIKjWrr6yRdcajuHyFl2kIFlTjQmgzN7lZfby46EiEiwHXY2FzfD0UAQcnULzXaDXtnr3cBQ+PXQVB3eHGoA8xcEua2XFaVcqQsivNIfx8UknAxYGOE0IZE8/bYCKdojQn9YYt7Lgq5rEtcyDhMTo59dUN1yM/lKqAcO15307RUsI1lhK1bbn2/gDqFluNrvCeW2taQaO5mX5caMhgWbfAr+3DUN0sP9zfV4Aub06i0x2OTyAQV4aSrGq2M6VqmGEMoMNCBNrHzfdcH+o482NR6X7oNhvE3uMXhc49etuIG2jmB5/guzvd3T2DJeK0wAIlxhdhTenceWSUgMkS2R0W/lmy+ict+3XUOAe37fXRYcV4U7Ihex3GfPrm2lE1L2xZ7SFt2SWkO6BVHBKH1K4ugrOsQrsDhagfhqzVH0/Rf3j68zc+fX0+R/+Wfts1PjP6fPZx6PmN6/5HK42li4PifH7o+/+um/fXDW+0lwLDnA7km66LXI63/8jju4z/724RZyvT89dj7A+rnQ/jWiebfWr8lYG/T1tPXpsweP1kBO9yumX+X2cw/3fXA+/ePR79z6u3x1NsLqvZrW37NnToN5hWAo4M6D/zkuWT+Gr0eVX54818/nfqKL8mvQV3NLr9+7wA8xT8hn/C3v/1v30VE/DUvAAA= -->
