---
name: "rar-cowork-cookbook-bulk-update-oversee-active-campaigns"
description: "Applies a bulk field update to oversee active campaigns records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook, pausing for approval, then a confir"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_oversee_active_campaigns", "rar_sha256": "8b97a0e3bcf5b2bbd07b7c2d56f1c86d81807de6e6419e5dd253c3b777c76a4a", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_oversee_active_campaigns`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_oversee_active_campaigns_agent.py` and in the RCI capsule.

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

Oversee active campaigns Bulk Field Update — Applies a bulk field update to oversee active campaigns records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook, pausing for approval, then a confir

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-oversee-active-campaigns
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
      "description": "Explicit approval after reviewing the dry-run preview workbook before changes are committed.",
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
      "description": "List of oversee active campaigns record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_oversee_active_campaigns_agent.py` and embedded as the fenced Python below (sha256 8b97a0e3bcf5b2bb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_oversee_active_campaigns_agent.py` first:

```bash
python3 bulk_update_oversee_active_campaigns_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_oversee_active_campaigns_agent.py   # or on stdin
python3 bulk_update_oversee_active_campaigns_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Oversee active campaigns Bulk Field Update — Applies a bulk field update to oversee active campaigns records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook, pausing for approval, then a confir

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-oversee-active-campaigns
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_oversee_active_campaigns',
    "version": '3.0.3',
    "display_name": 'Oversee active campaigns Bulk Field Update',
    "description": 'Applies a bulk field update to oversee active campaigns records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook, pausing for approval, then a confir',
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
        "upstream_slug": 'bulk-update-oversee-active-campaigns',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-oversee-active-campaigns',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '91850507ab6a1a70',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/manage-marketing-campaigns/oversee-active-campaigns'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/bulk-update-oversee-active-campaigns', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook before changes are committed.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against; USMF sandbox by default.', 'new_values': 'The field(s) and new value(s) to apply to those records.', 'record_ids': 'List of oversee active campaigns record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when oversee active campaigns records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to oversee active campaigns records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to oversee active campaigns records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook, pausing for approval, then a confir', 'example_request': 'Bulk update these campaign record IDs in USMF sandbox with the new owner value - show me the dry-run first.', 'inputs': [{'description': 'List of oversee active campaigns record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to those records.', 'name': 'new_values'}, {'description': 'D365 legal entity to run against; USMF sandbox by default.', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook before changes are committed.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you have a list of record IDs and new values and want a previewed, approval-gated bulk field update on oversee active campaigns records in a D365 sandbox.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateOverseeActiveCampaigns(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateOverseeActiveCampaigns'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook before changes are committed.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against; USMF sandbox by default.', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to those records.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of oversee active campaigns record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateOverseeActiveCampaigns().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
