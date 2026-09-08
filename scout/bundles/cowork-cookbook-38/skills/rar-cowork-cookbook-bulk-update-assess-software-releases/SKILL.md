---
name: "rar-cowork-cookbook-bulk-update-assess-software-releases"
description: "Applies a bulk field update to assess software releases records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a supplied list of record IDs, producing a dry-run preview workbook for approval before committing a"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_assess_software_releases", "rar_sha256": "8168ecd77d704e19fd82ffd41d3e70160e2f5caa9c889be33f72193420466e95", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_assess_software_releases`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_assess_software_releases_agent.py` and in the RCI capsule.

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

Assess software releases Bulk Field Update — Applies a bulk field update to assess software releases records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a supplied list of record IDs, producing a dry-run preview workbook for approval before committing a

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-assess-software-releases
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
      "description": "Explicit approval after reviewing the dry-run preview workbook, before changes are applied.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against; USMF sandbox by default.",
      "type": "string"
    },
    "new_values": {
      "description": "The field(s) and new value(s) to apply to each record.",
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
      "description": "List of assess software releases record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_assess_software_releases_agent.py` and embedded as the fenced Python below (sha256 8168ecd77d704e19…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_assess_software_releases_agent.py` first:

```bash
python3 bulk_update_assess_software_releases_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_assess_software_releases_agent.py   # or on stdin
python3 bulk_update_assess_software_releases_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Assess software releases Bulk Field Update — Applies a bulk field update to assess software releases records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a supplied list of record IDs, producing a dry-run preview workbook for approval before committing a

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-assess-software-releases
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_assess_software_releases',
    "version": '3.0.3',
    "display_name": 'Assess software releases Bulk Field Update',
    "description": 'Applies a bulk field update to assess software releases records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a supplied list of record IDs, producing a dry-run preview workbook for approval before committing a',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-assess-software-releases',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-assess-software-releases',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6e64baded46899b3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/uptake-software-releases/assess-software-releases'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/bulk-update-assess-software-releases', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook, before changes are applied.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against; USMF sandbox by default.', 'new_values': 'The field(s) and new value(s) to apply to each record.', 'record_ids': 'List of assess software releases record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when assess software releases records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to assess software releases records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to assess software releases records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a supplied list of record IDs, producing a dry-run preview workbook for approval before committing a', 'example_request': 'Bulk update these assess software releases records in USMF sandbox to the new value — show me the dry-run first.', 'inputs': [{'description': 'List of assess software releases record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to each record.', 'name': 'new_values'}, {'description': 'D365 legal entity to run against; USMF sandbox by default.', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change the same field(s) across many assess software releases records in D365 ERP and want a reviewable dry-run before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateAssessSoftwareReleases(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateAssessSoftwareReleases'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are applied.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against; USMF sandbox by default.', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to each record.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of assess software releases record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateAssessSoftwareReleases().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916abObWLblX1HfF9GZ+bDNIBDCFRXRYhAamCQhCUhXOJnneSY7/3sfJF1nZpXrvaqO/tTXceNKcM6e91r7GH59M9smyKu3z28X18wWvJkkYeBWCzNzFkze51UM/uSxBX4Xdp41VWi1TV7Vbx/eHLe2q7BowjwD2zdFkYRuvTAXVpvECy90E2fRFo7ZuIsmX5h17db1os69pjcrd1G5iWuCS+CDnVdOvQizBTtmZhra9WK5Ihbb/3lhxMWPieubycLNmrAZF9eLuP2wqIFtVj78tPCqPAX66vah2lkkYd0scu8lcrFn6w+Losqd1g4zHyx0qvFj1WbgmtuFbr+YvXs45uXA4QIs7YAuywVfXeBsmoZN89gJnHUHMy0St377/PPfPryF4PPb51/f7AT4BZyngcvXh6+bh5+Xl5vnl5dAQGJmPlhZjCDcGfheuBXQk4JLjustXt9+rN3E+7D4z/+MwW6//unzl2zx+vnyNv87A/ObYI6oWTfAZdssTCtMQHA+LTZJb45zQJu2yuZE1CBbmf/pufN3SXmx+Ot878enkk++2/z45S0HJphzLr+8/bQA8fjyBkIFPn+apRQ//vQpyXu3+vGn3+XUrRW5djMLA1Z/+vr6/hILFv6+NPQWXy8Kx7x0gQSFhQuE/8G/+edp+kvcKyRfn4t/zIsPi+9Lnv35K7D3WY8WkPt9sSAGYOfbpygPsx9fOkDK3czMbPfHn/6ZWDtw7XgurX9J7s9PwYFrOiBar5D89OGRvr8toJdv32T+c7UFKJh/xxOw/F3dt0D9M9mPzP6d6CTMQDe+5/K74r63Afrr4ud/6tt/teHDwvvyxrpJ2IG6sxL38+LXR4n8/IPz+8Uf/vYbEP3firnkbWU/JHxNzSz03Lr5+vXnH+rH5R/+9vMPbQGq2DXTr22VfE/m9+L60POnCL5W/fjnvUD/NYuzvM8W33po8Wte/I/qt0+Lm5mEzu/X68+LP3bi/AMtZifelT5D8IdurIGtf4jjT2+/AfTJgDet/bgN8OM//mMhhnaVz9i6uNh52yxAgpswdWfj1SAE4Fo/UAPgnlvVIQjsax2o/znDs8UAN3/5X/YD8T/aL8SHZyj/+gTxr08E//qO4F/fEfyXTwsVyM6r0A8zgJ/njaJ8yUwfYPasF4Bt7VYdwCprbNyPoKU/zh9mvP/lXxH/9SHpUzH+8uCk8Il/Z2Y/Y1/dJu6n2ct74GYvn2xAY+7g2i1QkuQ2sMgLAXB/AN7XedIB7JwjUsdhkiycEKALoLPxIRtE7fMs7JdffrHMOviSPcF6uXjyXA2DBd/MWXz8CFzzktAPmi+Zawf54odff/th8b8X/9Wuh/BZhwL8feUEWHi4yNIC9FibgmUzFwJwN51HTn797RVgICYDxAwyGHoz0c6bQY3GrvMe7ctu8xEjVu8MBkgqrx4EFjafFntv8c1eoHS+NXNEkAPOdNzCzRw3s0cg1QTufItkljeAb5uw9sYPi7Z2H1p/sSrzYWIKmt1sflmIjAIYKU9moq9eDAU251kIwv+tFp7XgZDqh3pBv4v4tJDmqlwUZmUWQWW+dHjmMy8zM7+2z1PEInP7L9lMv+4cqkeLPMMDFoHI2K+Ufpxz/uBwkNj6XfdjjTnzpvrgz+pLVr/K/zmT2IAOgFK/DZ2ZFP7yKqk6yFswzczxA5bOkl5ZcF5ZedTg5p+NOPN0sNg+BqLnkLD40mIIii/+f56ZHhHh+TPHb1SOXXCSetafmZrHyDmjz8lztnGW9ejK38eZd8h6R+4vWRKCsqvGvzxXPvL7WvNEw7YC7pw354d8UFwgU7PcR+3PtVxVj1B/yd4p4gNw74GHIP0AKEAjzUF/Vzjffbc0AGgwf/99XHiPFwgrqO9F0VoJqD3PdR3LtGNgVTX37yvNoBHcOcZ9ENrBn7yakwTqDchfACNC0JGARj59g+3n3XfT/7TxORXNWx4TYwvat3oIAHa4s4EzoPVhA1DMbJ5TO/Dz80MIcCMtmtl3CzQQ8PR50a3csg3rsJnB8hlXtwBg/XH++/R0vuoOBegZECzQGUULovvopTnnKZh5gA0ATkBrpWEGSgsE5RWEh0AznYEBAO9rSH1KfFx+OeQ+GnAmr/eNsyPznnkeeJVvNv4RP9TvlQmQl84rHnr/vtK+aZtlzxhaAxwEGt/vPgeHT0/ufw4Xi3e5n//hWPTjv3dyerD59c8F8HkRNE1Rf4bhJwO/E/An0FHw09b6QcYfn+jw8QkNH9+h4eM7NPxJ9tPtz4t/z74/iXj1x+cF+gn5hMy3hFd9vX5AOJiPtP4Rn+9+yc7u7xgL1OcpKLA5eSNg/2+E+L4EsKJfAawCi58EWc+82gMqfzACyMSX7I8FPzccIJzMnwu0zv8ABI/JoKlfiftGXOBW1gDdzjxP+u6n+Rg2m1+7b5+zNkk+vAHwdP+189vMT+lc2PV88AMtBCa0JnQf395xcP7851MxNwCYtUFPfINK0wMyFk80nZtmrrd/BrIfvgHr0+sHS5lP5J6dacZitv55zpsnwwdgDc0/2iE/PpjJpwXrAnBM6j92wYveZnr/Q7M+Aw4CbQNXPyzm4NQzHYOAz1GYG92sQecAA79ry4OFvj5Z6B8NYme++hNRvWYH03809l8exPXOW3P1gGOy2SbNd3WBqeArCG77TMefNc3w8GDWH+ufHoUCFi8ei+cLM82CgD7UuyaA56fb39XybSj/RyV3MAfNIpz88+zFhxfGgr/gIPVh8e1MBOL4OqXOGtysTd8+/zyfx+YKe2yZP4A94M+3Td/+r8Vy3/72HbueJn8Nne94L7z4/b+ZJWbif7LfnOfveP9QA+gBkOxs8e+h+N2g/HFanA0CDjTP/9z49Q30jAlkmq+ueR03wHKAph/rebyCAbYAheD7EwXAvf+rg8hLRh2YYAgGQtboau3aDkk6JIK7KOU5a8zzHBx1li6JoCvExTzCNk3KXq8py10uPRJDqSWOIfhq5VIEkPfEk6/PuQaInI0C4fgIIMn9/Ta45LwcejowR+vbuecBEE+/fn2zVjhYucPr/eb5w8AQasF33BpIDc6Q9bA8HbWCq1tk1CWrzapwHY7WJtjvOGnk/VNZ38iWrdNDUnXiVBLJKWBPAeSrVJytZMxJqbwRLpp5WVYmfjrRB3mSsqkYlSWc6rXrEP4gN4VjMMaqCw/1mIz8NTwt+8u07uJ7NVzFPNs6ZI0LRxWHUBg+xATWIudAos8Cn8CDy2d8iIzcsIoSsa7G+6a9hYFHStJYXvad0sFj5CqJl6w8L9xyIYpxobEtcz2EoBaeUuKq5uIe0zDdHe6yZmy7rogrVz6bB2RvHW+HSyZrUHjA5JuhcXqp3aUwk6HMNcDYvxw7Yo/hoydUhmHS2KXX8BOhLjG5K+yLd41Vwynbo5/YMh26nZZgdqcWhAsbTCagkAvzrEARrckRps9ez0l9TUc8YfPkXCe0cW43rXYstx107DbE7piF6MhjCB8mWaqTBGSGl/Z2Ye0tty7z4062CVeI/TrdHYsrEaP3rbDGBU4kpqSTfH5llAftOvTOzh3RsRLo22GboJF0UtumlM4DZKco3a1SBC+RiZGKg3g7s9WGWh6NkgvrYj9qunaSsngTGN09vV+KQxPZ1vaOmsS4S4hdGwo2szl2bHTorjufdBA5UlKXx5t+TZQHLKXVra5eTXOYdjFxP7Acn/kXaVXprHgMR+k+Cjt2IzviBqYa56Q7bpBrDGeju9RuvUt5u+09jRsTBXBwRyU7cuTcNIIFRr2euMC434fjuLs2aJrfbdgSGQM6M72Q3qkbk8mMJEeIykz2qZWCOKenFRPdfKisFD3nTsuaDvJhxylrREEHpl8bd4RE8SyWE50PKvUYVFuTQYtTujYcty0LbO8chYs5IhivGVM+5dUaCRgqPtjrEmauBiYg+CTu1PWow3J0GdIUDzT8OtT7LAywgmCNWmYmbU/Ra7LFhtYJr8OJVAxY2ie4jmlXSOOdlJeu0yaXC1/ni15nih6ffzepqSlx6/k4WeTXiunEwYWpCZ4UUTmizcUjd8h5kLMl1MMngd3gLbGtmP56HGlsdKz7VikEmbrLq22UHdEjrIrqKWMoNd/tUm708uupEWCrH8U+4tDDBpdTx5C8s1H3miESq3IKyOxk19klEobgAE60W4QOjgzWO0eCtk742tV3/okWybOPbNYcabNyfsnyHhEHoxaE3hlVI3X4K1mrdo/H23PoKOENsZfXo27fuCDc0pwe+Ddpj9OnseEu9XGfycTApgREkJVyahnPpTFIHXLzGO73aC94GkzIbBClfZ0iJGlbVoMGXnBPFRS9MYl9iisMkTpGV0KbOfIjuo+uMWPojMqocJHq0lG8xWWmrEE1HDrRH/dCHaCW1GN5cqCVoawGaihZp1D0MQo30UY2SFwXRrTlIID9S0op+LQul9m6PPXl9mRy8QVn4+vKwvFQ7+3WudDTgVJxx77tzDHufdE8qVUuw+4NU9sau+e3+3mNCJLqjZ172+6kLUTV46YJac+uljUf43uPEHxnGSy5PZPBR88fu0a8YDlo04Lmw/WQ17UoIUzgilXMrW77NGgv/Y0EOCKK5K3smKYgj6q/zKLW1u/HkKUp0iGOFw9ND7FXSv6+bO9Uv5aIybfJQ3Oa6nWvppmvmKytyV7MyWGmNTI+XCRCwOUtpYyGTvHkecMUPOzqsRq6SGxwLFwQQ15yG4VFgJvE5hjqN7ZB642g25sM6VSOxvizWRPK+aooFK3T4oAEDXNcCr24WZ3r7QbbD5UxSVHMbDOR6DQJunUesUMwzdgH1xCJ0hWPXWwoTiHnZJWyAXQPpXOMfAxtJOaQn12DjfW1fTmxTsMhY1+rLTScsMw2DxJbb+rxJnfrOHcCLeiyfbjsxZUsbTfLtcx3jad3t3HMovvGwtDBWlpmnSuGWKd3ESkoI4G8jFhRXdRHvZglQi0S/mX0zsUt38r8ThAxjB7OK5Jm+O2atD2F2rHOhTSpgOZRZZ8Lq6u2XA1nSdc9eJd4MFyoSK3tZSSskEOpdWmgb2qm4HiMUDqfSO+6yWX7MtGrrXE9cLstxIjiAd2qhtEzLdHu0XXGi5ZYM/byvMk2UIOfBBy3jkcjue+V0y1U+3RQb6HP0LuY9054sQ8uAy4V8RV1lK2PEInQyyqB3trVcb3NXbnt6pK2u7vQxAAihV0tYuNmqnj7Bp3X5J3hwxsBwYweSyys9RSb0Bs2WrOeiV0CjiBkfPSbtCcJbhMHBavGPgVTIX8JDV6IYfZGqowos6tLc+S3mwOXsvEk6+cQ1sbtkltuN31pZCp3MtgWiuoNI+Uqr4Sy1G5ku77U2LRe0jeZ6SDBsO2LhBwNJrGWN4/fXrhRHS/YKBWjdu2j9EAOsEEdt6xzHePhxJB53l6GaSyQa3G9G0kmqgK8g6eLXp+ZvUCPQXXW8M2py/mjDu96JCAHK9n30VGSCt1lWYplpLaglaw3bjv+GIhTMiylgb9y5ka5poxw3dbIMh2HYNofSd2XhPDCS0gnr8IteazlzTVGGJCWpaLSiU0rJIruU37krha/3lSutsMoHQtLdROq0cmpcGM75l5L5yIdigRRXeNRNbPTuE05rF2NHc0qK0c8eOdkn9J6OLDOXqYVQg4b16hZp56GnWBfrhEjlLQnHpP0SHAxt8ERhxLZIyrJV44jt1uMOUx840wrFTLxRhS3tILgS/Yk2CeOGmvZ0KddoI+rbuLOzind5m1arcbJVTEqFWR2o4qwVGvosE/HU8jt5JuNKI0flidWX7HHTUmbmr+ul8bKuGVF1goFyoz6cjQLM8yxrPYHf0VcEH6SkqReYa5+2AiYmu99SS19daCSkr/cm7LXuLt9vh9lJCtMXPNDq2MpXygDhsd14hqLu3tkbnrkSmjTqYdKHRChQzXXWufclYmIWLM55n0sEJezobL4PnFTPELjwOFwaAojldn7pqwiax2B0VbdrlievjgrLVjKTSKXgi9cmP3+ct+CaruEzQ6Kh2bjKqV2k+4Wz0Mrq4YhyjW2PHG4ysu9FqR1wRryUFFSce3shh15dQrisNle1OWBhmNzsKhVOW61i0KtJz/K5fvQ49fD8RQLV6GUNzSfJhcm19tLFF4zo8Cxux6gtXpCB+kCRj4I34QiegACfCY5bQ9FocfuSoh2l3o4oDfDtPKDX0nHK2mPy8mk8gMGEUa+UnfT0KeXZrL0s1i5Fyatm3K1upfa6sRddRzmzqflflsRzHkez4rd2SpNBCnxI4YXghVEnhHZWHfDrnQvA7YjIlK7rlak5iTSZsOvmWKXi8LtuvQvp3MYE7eAh2w5VjJNEHuL9XWv2Hgnxk5Vp0/BYEhhmOtvqbM48Q4g6wJGWMvnizUypskVrq+hgU11t8K1yL0jx0q/O9tbZy/XiIln5KTUE3KUchBoM5pGgaIr3oQKSQ3DE3Q7aoO0POaaCaJQm9bJS2Fh6q/G7hgmzhllWW0EJ8TJ4femXtcqPoX5CIfjEjsVZpqpt4BMiDrnaaxSl0sAVXqV4/voAK93cBmF5MT1FTokJIZcz+aARPj5doY3yPUuMUwEd40iu7eWlBzDUIbNrruE14DSi1txLuG7vq49iwqvSK8RY0bL67gWGD2ExSDh6Hyz8reTrUC39NqrqjeVOnJJqDOkUOS4yfHePIAREY9P441KwotUaZMo2JEUIAkf7s4CZnN8jRHIhG0GRakcD8z0PEQorGIWY9OfD34q7nfgmKGch6jrIoiQ50NJo0kBj9Z7z1eNu7otpqvK1H3enP0+Pi1xrV6JXO/jeq1ssrI1rXRlpN3K8T24EYygzIwU35LOFTfNynEPxFE/7TTXS6zYV/RDI3XcMqEh1Ns3lyHzUna5trpJJGw7OB7DDaplt2DLCYIZuZNhUYUEj3umNjdyrEo1v40GQ8wmHF1Fh5E4G1k7XBG5G/iULTK9lS67Q7dSD1DP0JpmMs25JYntLQakXg4l10JSTclgbPZqet2IuIjQ8P4qMZcQR1PfIuSeOdyihKWDFGZOiNqQbotB8TZfaQ3fykplXVHshCFsY5zBwaA72HZNSIdE2HJxklWrAeNQ9eAjEn1boUbvwrW9LPqs6yGkzV0cNqMxkmTSakcxdOpgl1n720pv6+iC2faZ7vdy0oK5KMowaDVZtGfpVRn5OCSaZzXMucuwsgIh1vy4aqfe9LJdumLPIak2652iHtT6UC6REoMsbcpUZzdcRxdx/BO3uYUmlcU3g3WQYaMYBXy4tCpYszkzprExLvWOj9p41VA24NRTft9Il2gpToGArp1geZqsHpYdkm1RxRS3bm9EEl1G1mQYHW7LsoES6RqcAHYdjClMbIT+CN2VkR7Zw3Yw7YlGL66HYbF5PFxtJtlGV9HaNazNyO3FRiQcoGcTg183ajsqSIfSJVCsZ6GdWvCFjIkNdr1BkyMVttJANZUZCt9gF6N0Yoimu37ND7u6aMq1ElqgNfFCwWzZaRstI13qCuj0rDUtcZX72tIpFNUE5RL3ntOWF1AS6fl09iT+3mnpMMn5ZjgR+Z3IsebWdVTt7Q7SlgJnQAtqQ0hkjYxs9CrdgTMGBW/aXWjg4NSqYcIQYW5llljoUPISVWBVO4WWSGR357LE7AAlVvuyvI6cuQr0vDo30gCZkZwG69s9hzbaxB5Xd2qJuvuUwnGS2FXt5ebYDj92nRn7haghCJU0e8NhIlb1It9FYRhGO2+twXooq7tbmkKe4uHdmheadqNXnYlS7PYeeX1qC8fGGVSCpggnXAGQBKOOUm1vdLS+k4YaA1gIDu2aomOqHWoDj1ZphNCjuiUb9y57lBBb0a0TULGsMxrKMbYXwaTMTrVz76XU3+wPzGTFNdEvU3m/ueiYye1ti8ymk9qsLHWpp0hItuW1C7yK7LoxkwVZ1lsSdH4nj+1obLbjXb4MCSMnMm+02wq5ODC2RJYTgnZiCx1D04bc8FrsAuIYwbebOSaUpkC6rkS0VHTcPva5IvYdpYMVXnNSAzohA+eaSOPoUbU/mf54qqh6OKKoJYSIHKRZItOG5eY7zhZJidpVikCSjHTuDchMLKU73cvVsb0d1qdGrc/HuDyFJ3AikQVhzTrLaUiv7cmkM7aRVIdc4YWrakiipevTVqWRYhqidCzqDSGWtAQLxKAfRm5Jxsbl3JNTuO2p8mQfobV00Mc7KshwcqAoKrdhSCA6D9zXwqq1wgQCRwl56Laiyy65MrZS8eRN8tTXbWkxMGs7Y3xPrORQEChFHIadAylcpO3EAZVYJ7mFe2wdHeV7iaeHrBDOhpSvJlc5I3G9i7k1VmR+pxNIK5y0jdOkzoihPmaVFzuY2oAy8APl4/JgXx1dO10hJdIaYTsQBXyfzGpVpahtlhBs94dJu6tmWRFjSeuoVbKW0NyjMoWP2JZOeb7zGJZzNOEqd3TWicsNd0ouJGLuKldmudpXpjM8bdWV6YdigCu7jLmeUN4pyN1a39dBvRYbcsOnmrW2+jWnJNXVg+xVZdjLTFPc1h4p/Gzb0KR4bHFbyoqWM4UREJ7H3LN2fSq33XbbR+tQsmxcJRNawBoKKqh0F+G2daOaEc+HlbGDdqfDaucVtgVQDsqa5hRqa7ZjtnIR+oWJVWRvCeSWrNz8JJoFUmlcUrUh37Q25kkHnGoIotzhSLTcK5aKQyM4FA6ba5EQO5Q+JqCVKF5j7cM5vUEmYjkDpl/hZUH453t/vK7kUbWzLZ/CN9bncG86iuhpj+NUzAQoCpcjB/hjECDUuRB+LJZUiHgXWpEPe0gQa6kgSm97qNuYiiWiFvPpphO+eSOte9NjKoQ45FapT5DMgfAfygwEDhyEmJjw6djpG6hkdpZP8jvcjsARlwqOyoRTAVVPNMVhqBUnU7qlx6Yxl55BhlIj9DYA5oK7b6Edz2TuMro1R6oZhBRqGh6NqsYiLlh5Q6KDvhpWd9nad9EaqyUzKcRWGgDl73sLgRBIX1PG0euJI6GUDCbQ9yV0u1GDPjElw6s5lHR72GkOJEnE5mUJjuR36mgfci5vIiSjawoFlQBqB/FvS0e9FB5jd6wSSwyppOsgckgTQrXYQI5Y5qJsSnvYJN4rfIK3WqMu42WGxhu6g6W7lkLxYXfmzb10Fgp/7dPZtBlNaciV3QQlnk1pmnGq8MA9UytmTLRKbVUfA+cJOXAmCoOW65isEysHNJSusJIgO83rklY/kgF/VExPI7mMoeAgNqgQ1++XPd8WpblFmylbI3cMEQjkVoNp6EJq3XXdVIp1xjOIRQ+636knnhuNlVIpINGFuESxs2KvIp9XLgc/3tbuPtgc0KhO/VZPoA5hfE5eHsI1qCmrAWRGGHTVQFJ5qAh95e2XWVDJLQZfGaji4xyMjuUuv+56t2ShqV+PVQnhadfRHsqv3NUqBWy+HDbeCtG4HibWBdxc8LyEJptf7ggUsbrg6gxrlmfNwZRay3DcAj3Ztyta2UbXeAUAIzB/cYOmLaFtRt7G7G6jpu+4ane9UzbpDNaNrMmKaTlljbH31oqohCPFVPUnVdQS+96doGLlZLZqRRrZrDWkF09dTPrgmLDzfSa/wzFiBZJIX9X+Rt9orxAcRF7SOd6uDs0KReKDvBNd6mhA4IyAcc2BP7IB7iX7dRzby3zJde19SyCnIwSLDhj1hAJGScpQB2MV8XDLa+5qsBAk6t2bO/pO5W1X03TEBewE0S13p9BjHhYBRrNqguzo4S7Za6EjIRNiVV8a6XyKqBM25WG/KpCQ6S+tBGtssVpvliy2s/uru0QmNqpdZaOsz3pyzAJ2s9n89e3D2/w4+fVQ+N96O21+GvT/7MHT8/nR+7smjyeErul8fuj6/O+Z9bcPb5UdAqOeD9nqpPVfj6r+7hHbx3/l9YJZwvh88ev9SfPzOXpj+vOr0W9h5rR1U43ApOTxxgnYYbX1/CplPb9ta4O/f3zU+QdnwDfTeb414lZfm/zr8xnjfD3M5hdKXCf8/av/evz44c15vQH1dbkivrpVMbv8em0BeLr8hHxavv32fwB43o1u6C4AAA== -->
