---
name: "rar-cowork-cookbook-bulk-update-follow-up-on-a-case"
description: "Applies a bulk field update to follow-up-on-a-case records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook, then a confirmation workbook after appro"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_follow_up_on_a_case", "rar_sha256": "b9e22aea0b5e12eccac74303d98b9633cc6a3a7962465f630a96558fc60a4a66", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_follow_up_on_a_case`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_follow_up_on_a_case_agent.py` and in the RCI capsule.

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

Follow up on a case Bulk Field Update — Applies a bulk field update to follow-up-on-a-case records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook, then a confirmation workbook after appro

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-follow-up-on-a-case
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
      "description": "Explicit approval after reviewing the dry-run preview, before changes are written.",
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
      "description": "The new field value(s) to apply to those records.",
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
      "description": "List of follow-up-on-a-case record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_follow_up_on_a_case_agent.py` and embedded as the fenced Python below (sha256 b9e22aea0b5e12ec…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_follow_up_on_a_case_agent.py` first:

```bash
python3 bulk_update_follow_up_on_a_case_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_follow_up_on_a_case_agent.py   # or on stdin
python3 bulk_update_follow_up_on_a_case_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Follow up on a case Bulk Field Update — Applies a bulk field update to follow-up-on-a-case records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook, then a confirmation workbook after appro

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-follow-up-on-a-case
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_follow_up_on_a_case',
    "version": '3.0.3',
    "display_name": 'Follow up on a case Bulk Field Update',
    "description": 'Applies a bulk field update to follow-up-on-a-case records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook, then a confirmation workbook after appro',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-follow-up-on-a-case',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-follow-up-on-a-case',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8853817adc4f2f13',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/follow-up-on-a-case'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/bulk-update-follow-up-on-a-case', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview, before changes are written.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against; defaults to USMF sandbox.', 'new_values': 'The new field value(s) to apply to those records.', 'record_ids': 'List of follow-up-on-a-case record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when follow up on a case records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to follow up on a case records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to follow-up-on-a-case records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook, then a confirmation workbook after appro', 'example_request': 'Bulk update these follow-up case records in USMF sandbox with the new owner — show me a dry-run first.', 'inputs': [{'description': 'List of follow-up-on-a-case record IDs to update.', 'name': 'record_ids'}, {'description': 'The new field value(s) to apply to those records.', 'name': 'new_values'}, {'description': 'D365 legal entity to run against; defaults to USMF sandbox.', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview, before changes are written.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you have a list of follow-up-on-a-case record IDs and new field values to update in bulk in a D365 sandbox, and want a reviewable dry-run before committing.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateFollowUpOnACase(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateFollowUpOnACase'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview, before changes are written.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against; defaults to USMF sandbox.', 'type': 'string'}, 'new_values': {'description': 'The new field value(s) to apply to those records.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of follow-up-on-a-case record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateFollowUpOnACase().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916adPaWJbmX2Hejph0tmxrF+CKihgJLYAQaAMhpSuc2vcFrUjZ+d/nCrCdWeXq6oqYT/NmZADSveee9XnOsfTbm921UVm/fXrTfLtYCHaWxZFfL+zCW2zKoaxT8FGmDvh/4ZZFW8dO15Z18/b+zfMbt46rNi4LsJ2uqiz2m4W9cLosXQSxn3mLrvLs1l+05SIos6wcPnTVh7L4YH9w7cZf1L5b1l6ziIsFOxZ2HrvNAqfIBf+/tY20eJf5oZ0t/KKN23Fx1iT+/aIBajnl/edFH9uLNvK/qsjO2zhVXlRZF8bFeyC67eoiLkKgj1ePH+quWFS138f+sJh3zPa8nyUUYAGwK4jr3J4t+XZ3YQft7IeqqktgrH+38yrzm7dPv/zt/VsMvr99+u3NzewGXHpjgMnnh638w85zdSroDbAR7MzsIgRLqhH4uQC/K78OyjoHlzw/WLx+vWv8LHi/+M//TAe7DpufP30uFq+/z2/zfyowYDa4Le2m9b2Fa1e2E2fANR8XdDbYY/OyeY5AA8JUhB+fO79LKqvFX+d7756HfAz99t3ntxKo8DD989vPi7IG5wFnge8fZynVu58/Anv8+t3P3+U0nZP4bjsLA1p//PL6/RILFn5fGgeLL5rMbV5ngYjHlQ+E/8G++e+p+kvcyyVfnovfldX7xY8lz/b8Fej7TEQHyP2xWOADsPPtY1LGxbvXGXXZ+4VduP67n/+ZWDfy3TSLm/Z/JPeXp+DItz3grZdLfn7/CN/fFtDLtm8y//mxFUiYf8cSsPzrcd8c9c9kPyL7d6KzuABl+zWWPxT3ow3QXxe//FPb/rsN7xfB5zfWz+Ie5J2T+Z8Wvz1S5JefvO8Xf/rb70D0vxSjlV3tPiR8ye0iDvym/fLll5+ax+Wf/vbLT10Fsti38y9dnf1I5o/8+jjnTx58rXr3573g/HORFuVQLL7V0OK3svpf9e8fFxc7i73v15tPiz9W4vwHLWYjvh76dMEfqrEBuv7Bjz+//Q5gpwDWdO7jNsCP//iPhRS7ddmUQbvQ3LJrFyDAbZz7s/J6FANobR6oAZDPr5sYOPa1DuT/HOFZ4zJY/Pp/3AeOfnBfUA/PGP7lid5fntANfn0piy/2lxm6f/240IHYso4B2gKQVmlZ/lzYIQDr+UiAtI1f9wCmnLH1P4Bq/jB/mYH+138h+ctDyMdq/PVBQfET9dTNbka8psv8j7NtxgzcT0tcwFr+3Xc7ID8rXaBMEAOcnimgKbMeIObshyaNs2zhxQBTAHuND9nAV59mYb/++qtjN9Hn4gnR+OJJaw0MFnxTZ/HhA7AqyOIwaj8XvhuVi59++/2nxX8t/rtdD+HzGTLgiVckgIZ77XRcgMrqcrBs5j8A6bb3iMRvv798C8QUgH9A3OJg5tV5M8jM1Pe+Olrb0h8wklo4PnAwcG5elXU7U17cflzsgsU3fcGh862ZGaKyaReeX/mF5xfuCKTawJxvnizKFnBsGzfB+H7RNf7j1F+d2n6omIMSt9tfF9JGBjxUZjOv1y9eApvLIgbu/5YGz+tASP1Ts2C+ivi4OM65uKjs2q6i2n6dEdjPuAD++bodCLcXhT98Lma29WdXPQrj6R6wCHjGfYX0wxxzwOM5QIFnQ9F+XWPPbKk/WLP+XDSvpLfrZ/sBVBkXYRd7MxX85ZVSTVR2oHmZ/Qc0nSW9ouC9ovLIwSfTgxZnUT6aiNmUuQ9Y8I/W59kOLD53GIISi/+fu6PZGbQgqJxA6xy74I66aj6DNDeMczCfPeasKMjUZ0F+71++YtRXqP5cZDHIuHr8y3PlI7SvNU/462oQCZVWH/JBXgFFZrmPtJ/TuK4frv5cfOWE98CMBwACCwBGgBqanf71wPdPIx+aRgAI5t/f+4NXHGbEAKm9qDonA2kX+L7n2G4KtKrn0n2FGdSAP5fxEMVu9Cer5kiBVAPy53SJQTEC3vj4Daefd7+q/qeNzzZo3vJoETtQufVDANDDnxWcsWyIWwBgdvvsz4Gdnx5CgBl51c62OyB++fvXRb/2b13cxO2Mk0+/+hWA6A/z59PS+ap/r0C5AGeBoqg64N1HGc1pk4MmB+gAkARkQR4XgPSBU15OeAi08xkTAOa+utKnxMfll0H+o/Zmtvq6cTZk3jM3AIsAqA6ujH+EDv1HaQLk5fOKx7l/n2nfTptlz/DZAAgEJ369++wUPj7J/tlNLL7K/fQPA9C7f29GetD3+c8J8GkRtW3VfILhJ+V+ZdyPALzgp67Ng30/PNHhww+g4U9inxZ/Wvx7qv1JxKs0Pi3Qj8hHZL51eKXW6w94YvOBMT8Q893Phep/R1ZwfDljwxy3EdD9Nxr8ugRwYVgDrAKLn7TYzGw6AGx58AAIwufij7k+1xqgmSKcc7Mp/4ABj34A5P0zZt/oCtwqWnC2N/eOof9xHrlm9cHw9anosuz9GwBP/18MaTMd5XMyN/NYB8oGtGFt7D9+PUCutx8D359nXu4OUN0FdfB1yQsWn1A6F8qcY3+HsO+/EvbLygcXDSBnAQDNyrdjNWv7nOHmru+BTff2H48/Pb7Y2ccF6wMczJo/JvyLxGYS/0NdPh0MHOsCC98vZmc0M+kCB8/GzzVtN6BIgII/1OXBOl+erPOPCj2I5k/E9OoQ7PBRw38BgBHYXQaCCG7MpPWVs354GCD/L8Cp3TMMfz5qhgJw/8Wkj1Xvmp9nsSAW2eNgUBffafSHB3xrtv9RvgE6nVmIV36aLXj/glLwCQak94tvsw7w4Wv6nE/wiw4M9r/Mc9acVI8t8xewB3x82/TtH08c/+1vP9DrqfOX2PuB4Qewf6aYf94yLHZs8+S3Obw/MPxxAiAAQKOzst+98F2X8jEAzroA3dvnv1f89gYqxAYy7VeNvCYIsBzg5Ydm7p1gACHgQPD7Wezg3r87W7y2N5ENmluw31n7GGb7NuKQPor5rmu7SwJHcG+9ctYUjrsuZeP2ck1hBEUGFI7Ya4okV4FLITZhUxSQ90SML3N/GM8qzfoAT3wAoON/vw0ueS9bnrrPjvo2yjyQ4GnSb28ORYCVW6LZ0c+/DQyhDoUtHW3vQDXll4RC16J2VAOr8G0tdlS9O3H3pLye6BTBIoIRLS6LR0y0Dsddh+yikifjbbHxrcN6uqW3+KaUGJLh04DWwoHhLhVCedoy6C66tVpOzGq875u8VUltf4hULUK5clVb+8NKvxuapvskyTVZkCyv8CpP+t0qtq5CuTHWV3i7HOuhl5Z8rLTSrcCc6sJR1lncbupdjMS8fHf2vair99squMDBePLhdeAQpBdnYnjIlfiSFQLJ+3DQFwPEXW45oh+WJ8a6NqqeGWWRLNmyPjTnKS+scZ06qXY9q9X9pBxuTZx40mHFSBcMy9RK2/UobzR1eD0agmORplKuRGr0mPNVQAsBE9WlCGm3y85Q/AuZhqutGt+9Yj9CJ7xCVtzo93iFr6ldixsMomswXVi80TXEwbwKZ/4mmXba1JmULkvBIdQbanQjcthP2mafEeemLeHjwBuuyLocTZVKIra7gsE86ZpaFbTZjJKdHRDywG0IMeuP4W59JKqrQg6q3V1EYQ+NyuEwcQ5dBAfdHYTchVBU6KkkRr3bRctL78SE/LD1eaJNp/AsUkZcKUM/qFKpipN/5LrLyDuxH2Fbam1BGifzWR7riatkcDYWcM4OSWEVeJL7xvo0uNVQ57eNhp7Vs20rYhESBn/ghKJR0atIbJt4PPh8rvqdJdHwvV9VO6w3de0Yycszc72RY20A1kTuUqWTnpx5aQX7Zo+ct7h0uUQbjc8uZGRwUEzpXazqmBvvIEZQw87EXbVOXDdeWth+pAn8sD9shUoJ0POyuTCmjdHhYCUjC9nO3VUaqW52Q2HAAhJyNYNItnk+ujdFaFkaT/Z1hl/E+7bac0TfXqLCkLA1eskuEX0beWjXBnftRLV3ckx4KV+hyzXv7C+HgQ5gwV4yw7lD5J3DJ4Nhb7elnEN1IJDG3svqzp8MN9SVqZfZpXyc2M3NGhThPEgscickm9+hHYkddOzUaC5PDZf7irrCUUBwOI62epNAIDpbhDJhXYYOGcHdPVGOjT0v00hUkDKV1SJpOaUrxVParF1E2vhXXqV3q0FgoHsA4YUxhew1P6pcT4W2l6TnjgdzrpfGOkAStmojYnJvdI2ltmWBIvMrzTCSXFQ6ghZlk+13dOwmg8/4m33H1MpeJ7wa24U4jxKMty/H0yQ32L4z1wijRU7ALom7XaVEX+96mtrshq7Z4DuuYQWL7qLChjJNVCGmGuFjuU4w0dvjO+ckl3Ic4qglXDg7LOA94h5a7JJMS93Rl8fyuITO/P02TYR3FzJjqA0sbAhVddlQHTAj49QbwtZMHB9gZDptYv/S1XlNafROGjdDfdkzQhFtpVvcISVUkKomu1ST7U47kaT5IBtMNT1IARGLSxtpAZznvRCISM4cxii5e812m483noNdWrKqFSOW612FdWJ83PPujsbSHUKxBV54KeGcMnTLl7hETQq+6vFWuU+MGzg7+lBGoX/BKVp2t2hcD7QHtyqDOkjOI9ckj/fOeXMwETPZMe4ykGgRGfPVoR44W02LqLPHOBcQaSeWMe9nDonpsFpLAuaiUcYkDEnB4liimINMBCERUrm/nfz7EJDT1JvL9Xo3gn5aEfBwq07nDLhbELT1ZuXjm6UHLdfaRAxir2rOitYGvJ040ZWwNBF210n2qZ1KYy213m1MnSizu4J79mYzCeE+n5BJ8S7pGQSQMNhpfTZoVfL2taFGZkby3DndWTEWpQfhpDOYogrr6wHBfWj00Ua7KSkSp0l2E7DYxdJ81SrwTbT02CNvl1PYG5cW23CIerXYnbl01YG1Wg5JLeFwDZT7Qb8duVw908hwW14x91xxN7K+4Ns1Qe/1RFXWziaiwq65xqh1VyvTw4TIKRxXKreW1OSGhFS91ULBtoJWgEQ3En8qZUmCQs0PVPJSZvI+yXLbkZVyvQ9jJ50kHO/XexpqOwF3FDXajTcBgmHfqZ0lvEqJaSNTFGQUeDXcBI88XsOJleAsvzM0e9hloIhwdrzGF5urYP7Gm96FjkbQOhx7Orle1mUeJqzQp1s5mWzzJp3N7V0uFCGmhiKXrufrjpCVy0kf8kLXtLBk6LMQKES1YTZBcm4bEDBmM9j0WJhbJtwmtjEUcd6Yq5pgWCg7X2uDXJaHS1xYF5+N74fNcb+SvXgrOinhonQWtMs6bVBYu0Xkeokox3TgqfAASWl5wT2Wk0vx2Egnz97tTG0kJcwP6PvF7PTwvs0giVSimPC4DcltNxtLNZndYYBZD6khL2YR7dhl8a5nKWgMG0U4ls5mmyJMTXOrVlxB4eZmmhPmrSfWFJqaU/bNkV+D3KrS8yq+ni/GpYtGoTmcElGGryJvl16Vht3hxLj7jLlooij5G63W7Jzc7HCoQw+cEWul6/MTZ8lKUtmUgmzrtSDF7UnVxPrI3x2/ZkeW527J/Zh2BnwQy3KSrrI1IeOKNQGgMxf94pU3aHvz9spdyfuDiPL7GBbF1Efdy4E8NyfznDKClWETqsuqtgkmFAVFOgKYFCi+8gseWydCVoLGlMxxbSVEZkU6qcfSZnjqfLIqh4k508lB3YIGChLPyZipSIBYIhMaYbgFnUyptVpdb0efNlSAk7sLm0lj3EbH/OiavJhfNrR4LlYJpVImUdU0zKk9J7JisTKIBvZopUDsUBVpGBphT6Xvw3bJVeY0dHI32Hx0uovEXdkUKJ6frw4VGBKjjiZhXq02hk7RDtlxbkxKfeLnNXQybvLaZvKiZLRVcD2OwYmyCG8ZS5beCDswSCLkrSYE+tRpGE2gtkVybQzgJpYokk63tyu3CeSyOty1e2tsVvGYioNapbB+3R5Z3SKDFeOejwia0cYoD55xzCrdSJGqNLfHI4HtZH9VnwV1dxL6+HgMsMumDBXKECuCZbglgqUBeWMuTVERaAkLnc6ItEFrHnXN4dM6DW5tyIxMudMM3tqstetxC6X3lvZlzM9tLlsd1whuwdNqNa72N4WwOgLCpYoZJxbWMc+++bwNvI9Ho3ZWydMq3Y5qyndrVFMoioZ7weU8thjbc15t1FSGkHFzjhW0rCRayNw1vqm6RIsOe5/H96E5RLdlWt3DYnvnAJ4L1ZWWHYUv49Qe9+vKr0jbpQ/C4EIXmyb2A7W87TRMcSeRPO6MmEHR4TaulOuE3HMsn+Ad29U3fmncOvKUO6VgXKCdfF5xkdoSKifENArZWFZpV+ymyRuYJx3xaNeKb6B5HYXWwEHwGIIOKBlyY7/fXXUNKvvCyY7W8YBez7QI6sy869GmWppNRQUK1SCcvxdzVnc9PtChycwGwTsr6RT7Y8z2sjXskY0rt6ccOefOWiu6U+ulznWLOoHu3+q1VV+v6CRNaph6V8GycsO0lKV2RdkgZVs+4vm1bgkkx/C1AO0lJ+aPtUYw+7y/Y45fHC7IHRSy2Z7Pqniidpfedavcce+0zqbueh0eNgcmiUGTkFoBYZ6QrbkEcGQZI4thZI6EsXcE7SIzxQUUEYdG0Ta4KxhbZ6vWWxbqKwk6DFsJcDKKeOoaJZYHDGvRKgInw41nWcqaKfQIH5UzjHbygccCw8Vva7cJtoLNlZpeCwrJUx477lcKc92IpVmgYenwJ7SJYFz0yYuE78VbaeHUECBGOLhM2rVKKl+j0DGVxEbLaYMpk3nZn8oY2duHZBP5uc7ohRIui4Hg5aXKZkzDuGQqnkbvLBPIekWtVmdZxfxez6B1I+X5XQ85e3Pj2xPLWX6tqBlLFBOrtg4I1Flebqy1we2jKXXBfBL1GnW/+7aLb7LTVhr26K0aB6RbRjte9jD70Dv15qZoQnaTlwzaU5x7O12MjLEgiYdXeqAz5AHTsou6sZOpnjYxV3XIajo696qAB44qzyFEK0ftJMRFcisRT06uN6k4ZHpugMmuYyybriEz9WFz0CFwv4G1Mzpx9dm6BLtCStEIN7zhirZtEeAFf6BoNiszJlNk9KSt9ttDbFsMHHJm2Z02iC0K/oTebaj1dusBOQtgC7rC0NY6H8mQkrggYxzK2Iob5YD6ap5bZGUHAXvqrwwo6DN+uLK+EwX4yOY24zv9nmNMzR3j+OhD6y4eQseuvQPioaFEsL2yv0r8JUXQG5g3QprdXA3WMs0lvgT141ztTGq88bqmSBF0XFfjMNmoxzUM6u0CzBrPRlKYiQrlCXxupt2hFcXl9mZAPq6puLcqDM1PmxN7B6xnw/j5QG72g0h7RQXrJ98uJIleMuO4D2F9L/BXdUyPa0tEG6XVVNbwTfeSn+W7jYQChetIkDm3truD4RZR5NONRhuRTTaQzh9v28Jgt8E+UAzpnrRwspK2dMh2WQ1F7AAmIl0zSr86TTeQRiZxYIrVWc/U3UrFDjYju8t7AUaPALSmeomdzLuRXKclc9w08DS18RYQoXa8943tJGZh3hEsM6EChzEvlWzcXOckdiRSsYgInp6Any5iwW2r6XrRghYl4XHy9WiJFxRJSWSzvZLYPnF8z/fuq3N+5a56rYgZpN+R/SkMTsYe9q3tiquu+U2UUBIAJAcrQZTmnZ1viMMJ3nRjiyeE43d+0RGUqm963DIpPr9ftB4+xUJnkQa19gR8pOGzMJwycd/r19hehmMA+pij2iJSPiQXVt9i1qXqZcfWkeYYg94B8mQQwTHHZH2d6CQRybnQ3D0L66XgiDEjfYkAUwVhp7C8jQzGedUIeN3DcFvD4cUmwfC/Z3NqCfPOcIQcdzNMfnKw1wrdhVuWZ80OtcwYBiOgiQpb3xpSJPT0o0wXFxmKUCwLG5JjE5CLqbbtTDjc7aUgnfYEvk7zADISN4/sHmAwWZTVsctxn01K2cD5LLFKYZNcl0014PlJojVztI7E0OA9lOZOeGdB+Pc87qYlr+Dqdl2vPc+DDFJT7zq/dAffIjEM03dmJ0Waf7yElh7GehSsuSJoG/Q4rffOdOjjMuflooxsFe60Er4mLS/C9XUpHYuBztNbwmkKC2hU3hbLOnG6UYIkx4xFwja6VkXDvRdEu0s3Wq1NtVkULJXkmhR02fRnPjlhVupP6zzT16FgriT4mEhF0Rx4ySlEBNoJ0LjLXK1qNsJdYEYTLu2TSZ1u5w2rSIRTgS4R6sRtirbicVLOTBVSNFneR4vDGBdj6ByOx8bYNtEG8oRz6mINAbmymQqbvmc1g8taTe9RNQjk7eWyXPb5sOKmpjMF1LxfMWLwoWO4rwffLC7OqtqwkIr4fIbqZkA5bHfenBMPb0+y3NsnBdA7Id0GcsKKcpkNzZ1DSxJMwFdplNaMfaiyrXEEwAtGqTja5uhqIpdnI747FMW26b0z+pMwnTWdEzwEVbNwuSpC3AmTWiQ2W5LaebHd9SfZWxsmZFb9VWgbLzM5sp6Obcs21S12EbaE7cNpzTVTHzppp5p2dC+kdvCOxLiWqywh0yUt7sRII/rp3iyj0FBkuIStK0fdyly6E8flVrgEF9GrKnZp543fuPRxGQpF7xRqROC9jlVeS8IGQuZYfYJ8klpqsXmHcyhYng+d618vJzG/5muP8j190EravW7p65igKlChs1e9iONQSF07GdKaJQIf4hitmn7wtk7hQdldPq8nSqGQlOuJrcGJR806Os2EWv5R8MT1ZakdhcImUL3eJ6csaU8uyF6RCryRkrarMcEPmKkP8HgIj3fFrTKLRZlbFBjdfXtlzb2an+HjTe6V5LQPDiM00ImFjtqW5EslXioNSDnGLbadsMm3q/A8RuWKDDKWPefa0etA9XFkmt5uUYIEmi+fwMh5kJpjTpoBbzVd2qYo1EgO7oVgzj63nd+zlUzqeHMBeU45A+j4hbi7rpa8bAqKH4oKruBE6Vg1u3LAFCVNY0ZGZcAmGA65+RE6tDd8Vw+lyKKOjXbUCDPHth7oClrbO3cbbExbJdx1h9TaVFyPpG17vXAV8SlbK7fKMAY0QRoXU8Es3Vo2Crp4yUn60lBDvF1XDUpSWQc1aZ37IHeaTHf5k7+kMemshpi15e6wsMz6E8y1bKyte0O8V+xapreXm38OxaLDjXPaeafUumNnpL0qtTzqLat3Utnv0pWXz4MtOsE5scZNaZygJGipGJZXPu4Xxa6/thnNOpCxqqXWVE6xNCj2qGs+wEQ551OETehuC8MitNqe2i68Rrxn1wOTBbLBuYnfVu3Bc5f2MiM7UsWtMwympZN88Ouiiz3M00B1tIpbriu1KzbufrvC9MLYRlHFRXYDmjSovbnwUlsedm3B+HfI5PctRDIj1gc5ngPidFMwIUg0cd0XO6xz4T4PdedqIevhtpLM9W5DKwZFJgidGidI2ezrgijcA00vPaGezD2ISz4FOSfk59WS07Z3FIWYWmYNz2uhhl9zx726lPmz7JZyiJ6XaBFloJn37sfAd9fYkbSwixFMXcetobz1wjqRM3jdHJDgjDmrOyFbfNwSPAsdcmVgdT0iUXvZI9LtGt8E0o7JpoFRhMED1NqDLsIfCNiGXGoyamNTDDjG982lI7C6QXnsPk1az/fIcoNBVnS8M8QaS3t2KWYpdu3hXFsyV7drvR4uREoZ7kO2Ek/ZjqMZVCRhwTbFKqRjn4oPO325r08JSrj89no/tIbRxHtiGeKkI6ntHlOO2UEd3BO7Krm0iXLPX6XeWPYYJZ9xq212LdQHaw02UuLsE1W7vFdo52rwcUC2GZuWW3s5+b0ydZsqlRUn4QtVv+1upkefEfLITw06neV4CcNCHyK7bRCKHCBoBV0jmpMc6bhB+iSQU3+7HGMpMF15re7lRPRPDLza4sU+7gJ1Q9P0X9/ev80Pk1+PhP+nL6PND4n+nz2Pej5W+vp+yeNxoW97nx5nffofa/S392+1GwN9nk/cmqwLXw+v/u5524d/8TbBvHl8vt319UHz87F5a4fz685vceF1TVuPX5oye7xbAnY4XTO/JdnML9K64POPTzv/YML80HPWui2/PF7H+7o9Lub3RnxAgI8188/w9Qzy/Zv3etvpC06RX/y6mk19vaIALMQ/Ih/xt9//L0S1ik+5LgAA -->
