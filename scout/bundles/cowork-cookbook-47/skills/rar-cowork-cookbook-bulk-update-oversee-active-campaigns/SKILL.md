---
name: "rar-cowork-cookbook-bulk-update-oversee-active-campaigns"
description: "Applies a bulk field update to oversee active campaigns records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook, pausing for approval, then a confir"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_oversee_active_campaigns", "rar_sha256": "8b97a0e3bcf5b2bbd07b7c2d56f1c86d81807de6e6419e5dd253c3b777c76a4a", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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
