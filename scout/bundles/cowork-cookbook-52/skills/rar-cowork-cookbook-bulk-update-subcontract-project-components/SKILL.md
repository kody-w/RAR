---
name: "rar-cowork-cookbook-bulk-update-subcontract-project-components"
description: "Applies a bulk field update to subcontract project components records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, producing a dry-run preview workbook for"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_subcontract_project_components", "rar_sha256": "75fb92e5d3175db1a1326119ac75915745ca2f897b368743ea47474a7296d403", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_subcontract_project_components`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_subcontract_project_components_agent.py` and in the RCI capsule.

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

Subcontract project components Bulk Field Update — Applies a bulk field update to subcontract project components records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, producing a dry-run preview workbook for

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-subcontract-project-components
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
      "description": "Dynamics 365 legal entity to run against; USMF sandbox by default.",
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
      "description": "List of subcontract project components record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_subcontract_project_components_agent.py` and embedded as the fenced Python below (sha256 75fb92e5d3175db1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_subcontract_project_components_agent.py` first:

```bash
python3 bulk_update_subcontract_project_components_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_subcontract_project_components_agent.py   # or on stdin
python3 bulk_update_subcontract_project_components_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Subcontract project components Bulk Field Update — Applies a bulk field update to subcontract project components records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, producing a dry-run preview workbook for

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-subcontract-project-components
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_subcontract_project_components',
    "version": '3.0.3',
    "display_name": 'Subcontract project components Bulk Field Update',
    "description": 'Applies a bulk field update to subcontract project components records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, producing a dry-run preview workbook for',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-subcontract-project-components',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-subcontract-project-components',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '49fabe5eef5a48cd',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-delivery/subcontract-project-components'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/bulk-update-subcontract-project-components', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to run against; USMF sandbox by default.', 'new_values': 'The field(s) and new value(s) to apply to each record.', 'record_ids': 'List of subcontract project components record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when subcontract project components records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to subcontract project components records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to subcontract project components records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, producing a dry-run preview workbook for', 'example_request': 'Bulk update these subcontract project components in USMF sandbox to the new value — show me the dry-run preview first.', 'inputs': [{'description': 'List of subcontract project components record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to each record.', 'name': 'new_values'}, {'description': 'Dynamics 365 legal entity to run against; USMF sandbox by default.', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change one or more fields on many subcontract project components records at once and want a before/after preview and approval gate first.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateSubcontractProjectComponents(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateSubcontractProjectComponents'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to run against; USMF sandbox by default.', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to each record.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of subcontract project components record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateSubcontractProjectComponents().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916adOiWrbmX7HfG9HnnEtmyiiQFRXRyCSKCoKInKzIwzzIPMhwbv333qg5nKqs6qrb/anNyFBh7zXttZ5nrRd/f7O7Nirqt49vmm/nC9FO0zjy64Wdewu26Iv6Bt6KmwP+L9wib+vY6dqibt7evXl+49Zx2cZFDrYzZZnGfrOwF06X3hZB7Kfeois9u/UXbbFoOuex3XbbRVkXiQ/e3SIri9zP22ZR+25Re80izhfcmNtZ7DYLbEUshP+psfvFz6kf2ukCrIzbcXHW9sK7RQMsdIrhl0VQFxnQ6gLL/fp90z3s8BZp3LSLInhJXkhc8/Ap9/vF3U47v3k32+F1bpyHYLtXj+/rLgfX/HsM1syeP5wOQHDevfmDnZWp37x9/PUv795i8Pnt4+9vbmo34NLbGnh8friqfXNTeXrJfnUSiEntPATryxHEPAffS78G8jNwyfODxevbz42fBu8W//mft96uw+aXj5/yxev16W3+dwJ2ttEcVrtpgauuXdpOnILYfFgwaW+Pczzbrs7n02jAkeXhh+fOb5KKcvHn+d7PTyUfQr/9+dNbAUyw5wP99PbLoqiBPhAT8PnDLKX8+ZcPadH79c+/fJMDzvVxlkAYsPrD59f3l1iw8NvSOFh81hSefekCBxOXPhD+nX/z62n6S9wrJJ+fi38uyneLH0ue/fkzsPeZlA6Q+2OxIAZg59uHpIjzn1866uLu53bu+j//8o/EupHv3uaU+pfk/voUHPm2B6L1Cskv7x7H95cF9PLtq8x/rLYECfPveAKWf1H3NVD/SPbjZP9GdBrnoIS/nOUPxf1oA/Tnxa//0Ld/tuHdIvj0xvlpfAd556T+x8XvjxT59Sfv28Wf/vJXIPr/KEYrutp9SPic2Xkc+E37+fOvPzWPyz/95defuhJksW9nn7s6/ZHMH8X1oecPEXyt+vmPe4H+c37Liz5ffK2hxe9F+T/qv35YGHYae9+uNx8X31fi/IIWsxNflD5D8F01NsDW7+L4y9tfAQblwJvOfdwG+PEf/7HYx25dNEXQLjS36NoFOOA2zvzZeD2KAbY2D9QAAOfXTQwC+1r3guPZYoCXv/0v9wH7790X7C9nPP/8RPLP38H459e+z99g/LcPCx1oKOo4jHMA2CdGUT7ldgjuzdoBtjZ+fQeI5Yyt/x4U9vv5wwz6v/3rSj4/5H0ox98egB4/sfDESjMONl3qf5g9vkR+/vLPBbzmD77bAVVpAXgCkFM64z8wp0jvAEfn6DS3OE0XXgyQBvDb+JANIvhxFvbbb785dhN9yp/AjS2exNcswYKv5izevwcOBmkcRu2n3HejYvHT73/9afFfi3+26yF81qEAKnmdD7Bwqx0PC1BvXfagx/mwAZg8zuf3v77CDMTkgKnBacbBzLzzZpCvN9/7EnNtw7xHidXC8UGsQZxBCOt25ru4/bCQgsVXe4HS+dbMF1EBeNPzSz/3/NwdgVQbuPM1knnRAupt4yYY3y26xn9o/c2p7YeJGSh8u/1tsWcVwE5FOjN//WIrsLnIYxD+rxnxvA6E1D81i/UXER8WhzlDF6Vd22VU2y8dgf08F8BKX7YD4fZM6J/ymZD9OVSPcnmGBywCkXFfR/p+PvO54wDY8Owz2i9r7JlD9QeX1p/y5lUKdu0/egdgyrgIu9ibCeJPr5RqoqID7c0cP2DpLOl1Ct7rVB45qP3znmfuGhbCo096Ng+LTx0KI/ji/+NWag4LI4onXmR0nlvwB/10fR7X7NJ8rM9+dDYOLH+W5rf+5guGfYHyT3kag9yrxz89Vz4O+bXmCY9dDRw4MaeHfJBh4LhmuY8CmBO6rh+R/pR/4Yx3wIMHQIIcAGgBqmmO+ReF890vlkYAEubv3/qHLxEC0QFJvig7JwUJGPi+59juDVhVz0X8OmVQDf4c1T6K3egPXs2nA5IOyF8AI2JwpoBXPnzF8efdL6b/YeOzTZq3PFrIDtRw/RAA7PBnA+dz6+MWQJndPnt54OfHhxDgRla2s+8OqCLg6fOiX/tVFzdxOx/zM65+CXD7/fz+9HS+6g8lyEMQLFAeZQei+yioOSEy0AQBGwCmgPrK4hwkEwjKKwgPgXbmP3LuS9f6lPi4/HLIf1ThzGZfNs6OzHvmBuGVt/n4PYjoP0oTIC+bVzz0/m2mfdU2y56BtAFgCDR+ufvsJD48m4Fnt7H4Ivfj3w1LP/9789SD3s9/TICPi6hty+bjcvmk5C+M/AFU+/Jpa/Ng5/dPcHj/HTK8fyHD+2/I8AcNT+c/Lv49K/8g4lUlHxfIB/gDPN+SX1n2eoGgsO/X1/f4fPdTfvK/wS1QX2QgzeYjHEE78JUbvywBBBnWAKrA4idXNjPF9oDVH+QAzuNT/n3az2UHuCcP5zRtiu/g4NEkgBJ4Ht9XDgO38hbo9uY2M/Q/zNPZbH7jv33MuzR99waw0/93hruZsLI5yZt5NgTxB+1bG/uPb3Y5o4T9mBr/ODfzAwBZF9THlyULOwAyFk/wnAtozr1/hKnvvnD7y/cHbc0sF7cgcrNT7VjOXjzHwLlxfMDX0P69JcfHBzv9sOB8AJVp831NvBhvZvzvSvcZeBBwFzj7bjEHqZkZGgR+jsNc9nYD6giY+ENbHmT0+UlGf2/QH+jrD7z1aivs8FHuf3rw2Bcam7MJTNN2l7Y/1Alo6/OTtv5e4wwaD7r9ufnljxw3X5j7DUCJD/W+DUD76f4PtXzt3f9eyQW0SLMIr/g4e/HuhbzgHcxb7xZfRycQz9cwO2vw8y57+/jrPLbNufbYMn8Ae8Db101f/y7j+G9/+YFdT5M/x94PvJdfPP8vNRiPNuDBjPOp/yAGD2WAOgABz3Z/C8g3s4rHaDmbBdxon38J+f0N1JANZNqvKnrNJmA5QNr3zdx/LQHiAIXg+xMbwL3/i6nlJamJbNArA1EkETg06hMehpCE5yA2gqErBKFtlyRohCBxwrXRgKJJB1tRJI75Nk6CfzaJ0isPhzEg74k1n5+FCEQSNBnANI0GOILCHshOFPc8akWtXIJEYZt2bMIhaNv5tvUW597L5aeLczy/DlAPSHl6/vubs8LByg3eSMzzxS4hxFleSOdUO0sTpoaxv3TlbuA9J2gHA0uJanckVVXMWq2HR3hXr9Yqwceg2LYWl6WbPTM1KtTrZKk0JDFaxTneNSUKo9rS7SU+dTtnnwXKcByoiU7Gu4fcuj5RSypmmtPWzhU4p7j2cEjj67hzTvjFdUy8vGiupkHTahfejtt7sMzq474aL/ytZWoxpOEWMokaO2k13E+nSbQtopSM3bC/oax+rZCjLC+XhH1XqvsI7bFrxMnGiZETQReMfFhCvmNoxzCMT04ZrYQr0d3ECrfWm31L1fw9k4bdABeGlBL2eOSatQ3fbnx+q51ih6ebkg/4U1ptJaO8BYRXjiZrkVsRPw8tmkL3c6Q7rH7wSTRBVtRdT6ngrjc0b3t3DMGoldRi9pgWKrTersXLoOeHmLsehMa42pior9XGhLkDteNYfDJ9dUSVU9y6MRcod5cTxuoiF5EosOLJyjgI7xJ2vAYVr2e6cDXuScxNkkRZ0wY73EQwpEqmhK2XEnZs4ZvO22Z8QC0Wu+Ckf0xIMzRI3YMm8hRba/5W5JtznEVQkEqpHV34wpKvci8mI7BJt3WbyW+d014Ksx5yQtots4vNNH2x42SacwafRLCWu0/TfeNmkm0YmlWGxWhKCJ/d3IE4prE6rMtyhVyNFUKogpzaKXNGj+LZxjeQLjh6eTKYwjnwVCrnVGecbME+ORIMWckpcPYBlsneloM0kSPPAtCQ3rZXfSWHCKye7Z7V5PgEa+NNScWtzoSadEAnSmOTi5owUACWbEnEOJKCmoltKO3Fqxsus5RqJFZMLD67LPkxgus1vLev50NTqWLLMViybVMEJNamvLCmeakGvT46/qrW92qfg0huthv8khwjc7MzbnBQmWLN+Ob+lvD2ks2RiKHOl165mlTa2z6xKeSMhtGDTl1WO06i8/PA5lFi+zrp+pl0RU4KG9bCOjT5A9NcL+A/ye7C+5W7QsJpubkSKOtd4xKSsWUUUAKWD3Xt1lAIs8dhpJebDSSkJCx31rZvcLZhbl0uIqFhX/BaSLuoR4Y0sla4FBzC1i3WpyHeJ5RG5CgWCVh8OJ1vyt2pDjfMF1bj2roZm6o9OnC7RkdvtUcyvtJKyVT97fl84UpNkn32kMChm1GQB+FQjjcmXhGbbLmGO8kmfEGJiLN4SazMY02nSdyBZHY5jy5x7HQ7JOW4vYz0WFgGoYP3ynIIXaMhrQlBBqY0WwrQiiA22uU0NAS6KhMc9oQTUq5FzIQY6LjNyM3QRJYV0SmRERBv97CVLhHjtDP2ctKaO3co0NNyq1TyOT7ANg9XXCA6eZS7B5Gql15j1goIqC/Iw+VwBplSSOh5AweuoeyZjhfy9RRvrp07TstmGoWLTO0aFGtlxc6l+g6ylMG7HXXebjGORNoxPCkYw4qUMVXdeehs6TiNN3WMtfgUccze7whaRa7Li3qyI/dqKPodINmOYnMR8sVlgk2DRu3lWLH7LVlGeadtHVt100pxiW46uvAgO+Ha3qRCRU25fw1PpnjFothnMC28FofpfCmvsiTFhtilhXHfWBa9cXtnPVno+chv83opa1Nu33UlIcZiDLMCd016mW8UNr2ncMJOU8ZcofDIIdoZh9wBNXcAZz0huW8VBV9FVKBMhVlV/GWNyytpj0/tVjTj/uyReCYydwK2GX/LVJmDHFKswDdRE9LMPWFPaGX4zTZJrsvNeMIFYeDZe0j3fMgyu9s+VbP4UAHWVLcMXQ47ByW60XOGLZvBwZbhsuvNWAcoOhQIv2J2x9sgHcydv6so+0Jb4oqRrhavnXXmVg4Ss8/QKRlZdDWtNoHmneQ9vAvF1RazaZ3NPKHZwe549xmBx2F4Uy3L+9kwYsqsRfjACIO13DbuYTVETZHow/U0Fk2GWZSfOyOtsOYwZrZ53SJcBq9CLdFk/MY6pVXQbDSZ7FLabUVouSwlkaGnM2kfJVn0TmaA9CK7zJB0393D1RLa4mNjeunWLMyrohy4/nTlfenQsGrATHYTIuVWNWIQ/3hIiuMB3hDbpNplIzghPCsqjGJsCrVUYehCwvVWWBR2brRsKjG9RDTYomgOfEhFRmrOlL7abJTb+UKghnCsreFqXJ1TLxb+kMCpu0Z3MXSw+AnQhjPGzF25yMbNxPbmKSgP7TG/nwClJdzYCu25aimIvWZI0J4SUuT6tarCp1XWGAOpnzoMl2r74iiNe4Ov/lWopyXcQ1EiIUUusXfyXoQVIiUOG0VJxejTGTtejWh5WS8xiRQ2fWw1OqPi1DoWAGrAiXnhNxIggz0aI1y/4ghb2ENy4MYZe9gRjF/LJ9M3PF5jzJNdyRiLmfx630xkAk2jCWuxeWS5S8wSsbyv/Jtm8GwqFsTB5nWFDOpizQ7yevTrtUYwalJeUBXa1LQoxdPxtB7PmhOjtMhhO3trldn2Nm49Acy/Z10YtcNaNCWLOWjicXdG2j22IvWM5WWsKASZNcQDX189ykTU8CpsiYof7aHpULeqYLmvKe944NXOPLRXs8nkG8lgcWFnIy7puuvXV0vQiiWYino/PhNEfbsNunLQNWElhMHmFpntLpGwWrtNTLuWQkxjkQTSr61ZXRjM21MnEIZU6mMvOmaCVgpunGcuog3VOhTLxs5okbkdisi2eJLDjGR1gg+UWGzGMCfbO6bqe3dNDzt7Tzmx1Pgtmey1ruIli3YRRMywTTvsL9Sh308UigYmf3OkUVL3hAHjEMpVBX5oYyUfi3UZ5Cnk50N68UWfVPKzvE2CbZ9VsmjbI8fTdUqqtnKxL3ptl+ENz8+ZajG2dGDzhNqe97fGQYpOgiO2OfulckZGJeIxn5x405AVJBwGqyj2rUguo6LsV2Ks0jVl9rYRtHyh8nfNGl28CUPcjW4rwLlSsOZJOOP9Jt3CekIft6641xmkSUtpqJf5+SaflQvLT2h7yAJHFgyMMW68es16myenNVZIpCskXl1layHngpOCLpdubhtRNx7W7Xq7um5FfcxbAkqpWN/IJ2p9g3BC2J6C23JUnVLELxBmbCm5NCnK6nU4M1WEY29byGCnLJS07fYcV4Z8g4pQRosz7GobKcTRrWT3AyKNcE7vlYolOENNsDPDGsw5y+z4RBYd7O1iaxOyK0mVQU8QM0yBljvB0AxaQqSdA4WtQyZoUkmBKcRwa63UPisv8E1oS8u4U91ZvYVbFR2WWzYZey4db/H2ihzUgl1qyDY2+3M6nNF+vVlNl32LCANDteWREndHdKN06hZb69F6bTG1unc4QxDCCUbXuq5ubSc0mCOMrsDUw8iVeqV6uVur1mW5bqeCVXY77TrVPprltCbiohz4q+IWDlTcTEffyAJzf3VGNDxT1YRX4ZDLWd4WRHM2ZVZSx2SZRdV5yQgrudob7YnZtLLhri73+KwZ4fl6iI57C7XZWt+S1yV/uxHKgQwzuL6u8bGMOUGuqQ5Xiz17LfZGiLZUw9liY3RD1MoW7jhur+nrrtvGTj3lORSncoTrbE+L16XjXSqMr+4tX29g3ry4ZM6vD5CMoHKLXGvdUaBCv64QNrJq9Qi6SlBxAXdzTMSk1ZCiDEtt18o17HaVntTqcOFP0jo6c6RK76QDssaUEiVkQwDzTM4lbJ9wISgdgj1JICEMRV016RluGH7Fa8Zl693YYpAvI3EnrLVl95s1QVklLW0HBZWv/tZg1nd21/PDENi7LWgJ9hZFucpp8LqpXdHtLSvW/FX04rhoj0feMpZr3naPUmyvOJEueo7dZP0g7Zh06txuczjcDW+dQoiQSTs/c0JV7UKSM7z6Im/vmmKTybV1x1OYRYXlHJM85RpEkSZtDIIsJqEtVrbU8cKkAqj5iSx6thLKI+pPG3Wjx0G4Ra7o2sdjuwfd2u0SKGZUIyKXTvGkWHHbuKBl3Sf6btzbjXxeDvlEhyc2qyXBThqnXA83IkCrZcX7UNpAHU6k6nYidgSgCm6phjafpaOIMNjo4Yxem5LI5bu1qfsXML+TRN6ux3V+vSc7yNmN7WheVS9ilThEKFmPbcmlOmlKjw2yU+4QYdZ9ZkGVhdd0bS6DJUwnl3VQc9trcsu5rSFa9HT1ppZntqLinHaO3euQlMEsO7pxtK6lIWkSQT1GzgSGC3HbVt3qIuXEqdwFFENc1MmzvGXDGv6ls3SY3mPMDjntvDo0qDIjdzJoh5C6O0M+KldH0CfgZsuyO7ZLuLuXeJJ/LAlG3nHYgKnHcXVT4cPmdrRYjtMsytjCXJ8fa4FbWVi0vineZjgruxQ5CbDKBpR3c3Wpt7Grax22o1DhepeApuxkFwaMEtf9RrhkHSGvi/Ce4HdqkzD7NUPX8XV1wy9CPO2Pxn41JW5U8kLU52erPVVgzD2FW4mwqt7TCNy5n2jTBg0MGvvoFtoSWGiSwnp1qNqVqLh7s+uPjlEGe2Kl2FNnybWXag6pwzllRXfML3hTMe3DEWdouoqNzeT5Xd/mqyI4GCDH7gpogpU2di5YbeYu6PfpMYVxmq3929LjuWqpp7mOZdFyvbvs9vFynxlQEijkpiCcGrOijMPuRN3I/hXyJoPuPUzWdtSeOp+S4uK0enlHtzgpxNWqseA6ULnWb5ktXOXtdnkic3W/AmO1sUbtm8nRoqEI287MzlhDbrQe7UJ06d9IzbyzUI/eG9GseQLSjOFQdxerJe748co3+41KQmuztw7ZnZnIQ5ZB7RKCwCAYy5f9ntzq1NIM8MoXkcS5ooJD0BqYdwyEc9SCQLCtbPt3pkEPJ9LMXJ+WNmei7svppBeeV9VE59Kh6VGn5oonK5GD16PGkZ1/Pgb09naICqS0szTT797ZEVdR5vg00hxEUagSt9iyk4M3xGRmRznUrtD1wOAkdodvFXmbyPv6IljLgDVO5pIgTfAqO74JElRHm3wVeMiQjbdNKsF5bEgEgoPRMTO9HaabmH4OjAwmbdw+xDJAeA12yJu9QY1UkadV4zV974+jptoqJ4WnQA7xIPAbFib3YCDZ3nZ+2V5X0drQPUK4DRZhrbyy8p3r3eCUY+Vy2oq+oFf4itLo4QKd0AvlJkxCYU2lexxkoggtaXiPE1fN2p4tPtn7oQ9oSiFcQ8/4UF0NCUN7PiQf4WovG0gqJ2rvXRjEWu05u69cpVfs4UjXImUdIa4CpaRFpN9zFuzumrt+3FkZXAok1QVTHE9Lqg88msI3jG+LuGw7+L5wLBF2Edw8qwDLwmiY9s6S722i2VEIje3WvoNWWbYxl+nmasDJPsSCBinPMIIZqJSRN6kmSDBAZfbtQNyNxNmtDPJiIt01mnadJXp1rdcH2oVgxDJlMzv493K144/S0UHCNVn3wT2Kkag9mTgtaMjB3JQbf9m5yh6MgLqGHvGQowaivoAS0dPLwRZA82TcfM23sUAgz3ixV0mTswo7qXA7MkaKnA79ml+fYYPx5mIWQc+whBIo3UXp+SQ5HBYfj00MVc2oaRt03FqCjYcTxrSbAINrbrhfcjC+m7qd1nTRxhxFD8LVE0dueaAA4jsuDnWGlmZmR3vY0U3YYzk554lj78tDH6wnvfUdv1p2uZRvHEx2tOWOBTPjijpTeYytnM3dZW2W8Oi1s2ZyYpPxcqvTnEbfSoL0SqxEzFaCbaNuzSN6OnsQQMbmSlceNDgtJClEuumWoLTXWGaGThgSgKOSmDNY/97Gx0bs7WRfYvU5uJQiZUOmAAKdDXJ62wyTWm4y+urR/H51V/ijsFcIpmzBgDLSO3FX729quVMqPTrkZzCy2gqx5jd9SaeN6Sxx4hDD8D7uEDT35YYb6TFsEoz0rGR/J6oa5e++j7XFGl5PpqlWmzDjEbZiyCPJcKTRHqc1qgyjdQ5slrueA2xJgI77dGpFhA/KVPdlTmtz27QiuvSnVEIdT4zkdhJYReiW3cqxzxaxlC9a2aBEVnnK6F12KgqwkIgyTSGpNtmLhVJtk73rxeh+c5jqfYYdz+OSiGPUWo2HShsOQ4osW72KTiLIIzfh6Nq/QJOrYgrBwV5RC7c7DjOGVhIaX/qyo2sYgtsxWxYlYneR5t8wX8wPteUPCEHu60uLFCZL14jHBLtc4JK8x4XyHl1kFSJaiCr6/XVZUoPrQTEzMuNwiXe0MOUhD1/F1jgqw9Jf0ptVyAybSvBEY5xatbtUbgYNbUcS5xWc3HH/csFKno4RV9iktDmSZ2Ud0S4cTY5yFgcLO3FKQRJMyFniye7EUxZHdV1dEN+hSm/Vo1h2l5IDB48rT6Vt864cp3bP30dj64iMvePHzNlobTbRSivfOh/fOhvXDre9unebll6z8tovPP7M0XSAhIx7TET8cINQp/bybcNV/EY8IVuKPIDmZQqRXDa9OlJUbjx79MniEFvBj8KatiQjMFJ+qW+mMvfHTjui1XQv05EPYISMKsoK70sq9Xs7HgNUYSa/sXO18Yc9mjM721PExPSaFFEb44Q46sVDczQbxhWE7NUKTbDNhrxMG7NC7N6AxFV/oLsWEwk3Q++M6F8NvIWy6wWb9lYnKWaHprhjqdQYU9gVxZyK5BzHXuriBDp/Qu+YSed9ltlFHuSdjjzcCydlfRbOApQfSG3linpMFissMTX1BoZAAi5zHA2nqwanRY3m0erMjdqJ9hNX8wnVrE+bmmwGFNZwM4A6nxSPsqKqGN1PTn6Rj+jN5+JCOXPlFcfMrgw8ddz0u76B/VJgjL0LS/a+ipbZuKzz1F4qmNnvXL9TDxs3KEkHiuVDlWmQ11dJQONewPFQj3AYLgith8s4CbCvpdaNpsm0suYYhvnz27u3+dH06wHzf+Onb/Nzov9nj6ueT5a+/Ibl8YzRt72PD10f/zvG/eXdW+3GwLTnY7om7cLXo6y/eUj3/l//8cIsZ3z+wuzL8+vnU/rWDudfZb/Fudc1bT1+bor08asWsMPpmvn3m81srQvev39w+p1jz8sPd9piXhvE84o4n3+w4nvxc8n8NXw9wnz35r2eTX/GVsRnvy5np18/iAC+Yh/gDyCw/xvwIiOhXi8AAA== -->
