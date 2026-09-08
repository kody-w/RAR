---
name: "rar-cowork-cookbook-bulk-update-assess-software-releases"
description: "Applies a bulk field update to assess software releases records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a supplied list of record IDs, producing a dry-run preview workbook for approval before committing a"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_assess_software_releases", "rar_sha256": "8168ecd77d704e19fd82ffd41d3e70160e2f5caa9c889be33f72193420466e95", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

<!-- rci-capsule:v1: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 -->
