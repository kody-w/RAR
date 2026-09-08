---
name: "rar-cowork-cookbook-bulk-update-manage-opportunity-process"
description: "Applies a bulk field update to Dynamics 365 manage opportunity process records in legal entity USMF via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing changes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_manage_opportunity_process", "rar_sha256": "5f41daa4cc1a03eade6504344636922ce2e36cf932b41f82ab6ad11e8b97546a", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_manage_opportunity_process`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_manage_opportunity_process_agent.py` and in the RCI capsule.

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

Manage opportunity process Bulk Field Update — Applies a bulk field update to Dynamics 365 manage opportunity process records in legal entity USMF via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing changes.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-manage-opportunity-process
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
      "description": "List of manage opportunity process record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_manage_opportunity_process_agent.py` and embedded as the fenced Python below (sha256 5f41daa4cc1a03ea…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_manage_opportunity_process_agent.py` first:

```bash
python3 bulk_update_manage_opportunity_process_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_manage_opportunity_process_agent.py   # or on stdin
python3 bulk_update_manage_opportunity_process_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage opportunity process Bulk Field Update — Applies a bulk field update to Dynamics 365 manage opportunity process records in legal entity USMF via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing changes.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-manage-opportunity-process
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_manage_opportunity_process',
    "version": '3.0.3',
    "display_name": 'Manage opportunity process Bulk Field Update',
    "description": 'Applies a bulk field update to Dynamics 365 manage opportunity process records in legal entity USMF via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing changes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-manage-opportunity-process',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-manage-opportunity-process',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '14b5eaf285e0b5a0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/pursue-opportunities/manage-opportunity-process'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/bulk-update-manage-opportunity-process', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to run against; USMF sandbox by default.', 'new_values': 'The field(s) and new value(s) to apply to those records.', 'record_ids': 'List of manage opportunity process record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when manage opportunity process records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to manage opportunity process records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to Dynamics 365 manage opportunity process records in legal entity USMF via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing changes.', 'example_request': 'Bulk update these opportunity process records in USMF sandbox to the new value — show me a dry-run first.', 'inputs': [{'description': 'List of manage opportunity process record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to those records.', 'name': 'new_values'}, {'description': 'Dynamics 365 legal entity to run against; USMF sandbox by default.', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change a field on many manage opportunity process records at once and want a before/after preview and approval step first (sandbox only).'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateManageOpportunityProcess(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateManageOpportunityProcess'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to run against; USMF sandbox by default.', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to those records.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of manage opportunity process record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateManageOpportunityProcess().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916adObSLbmX9G890NVXWwLIRCSOzpixCIJxL5KlCtc7PsOQlC3/vskkuxydbvu7Z6YTyOHQwIyT571eU6+yW9vdt9FZfP28U317WJxtLMsjvxmYRfegiyHsknBV5k64P/CLYuuiZ2+K5v27d2b57duE1ddXBZg+r6qsthvF/bC6bN0EcR+5i36yrM7f9GVC2os7Dx228V6gy1yu7BDf1FWVdl0fRF346JqStdv20Xju2XjtYu4WGR+aGcLv+jm57rKHxa32F50kf9FMWqWRSvSosr6MC7ezUK83o2LEGjhNeP7pi/APf8W+8NinvGwIiiBdRUYegPSHR9c+sCyPI+7bp7pRnYR+u0HYKB/t/Mq89u3jz//8u4tBr/fPv725mZ2C269EcBM/WEf/zBH/MMa6WkMEJEBYWBsNQInF+C68huwYA5ueX6weF392PpZ8G7xn/+ZDnYTtj99/FQsXp9Pb/M/Bdgx292Vdtv53sK1K9uJM7DSh8U+G+xx9lvXN8Xs/hbEqAg/PGf+IamsFn+fn/34XORD6Hc/fnorgQr2HMFPbz8tgGM+vQGfgd8fZinVjz99yMrBb3786Q85be8kvtvNwoDWHz6/rl9iwcA/hsbB4rMq0eRrLRDauPKB8G/smz9P1V/iXi75/Bz8Y1m9W3xf8mzP34G+zyx0gNzviwU+ADPfPiRlXPz4WgPE3i/swvV//OmvxLqR76ZZ3Hb/ktyfn4Ij3/aAt14u+endI3y/LKCXbV9l/vWyFUiYf8cSMPzLcl8d9VeyH5H9B9FZXICa/RLL74r73gTo74uf/9K2/27Cu0Xw6Y3ys/gG8s7J/I+L3x4p8vMP3h83f/jldyD6fxSjln3jPiR8BoASB37bff788w/t4/YPv/z8Q1+BLPbt/HPfZN+T+T2/Ptb5kwdfo37881ywvl6kRTkUi681tPitrP5X8/uHhWFnsffH/fbj4ttKnD/QYjbiy6JPF3xTjS3Q9Rs//vT2O8CfAljTu4/HAD/+4z8WfOw2ZVsG3UJ1y75bgAB3ce7PymtRDDC0faAGAEC/aWPg2Nc4kP9zhGeNy2Dx6/92H3D63n3h/HIG8M9P6P78hOrP30D15xdU//phoQHpZRMD7AVQquwl6dM8uOjmlQHutn5zA2jljJ3/HhT1+/nHDOy//msLfH7I+lCNvz7YKH5ioEIyM/61feZ/mC01I7942eUCAvPvvtuDZbLSBToFMYDvd8ADbZndAH7OXmnTOMsWXgwQBhDZ+JANPPdxFvbrr786dht9Kp6AvV48Ga5dggFf1Vm8fw+MC7I4jLpPhe9G5eKH337/YfFfi/9u1kP4vIYE6OMVF6Ahq4rCAtRZn4NhM+0BgLe9R1x++/3lYiCmAJQMohgHM8XOk0Gepr73xd/qaf8ewTZf6AxQFXDmzGZx92HBBIuv+oJF50czT0Rl2y08v/ILzy/cEUi1gTlfPVmU3aIFydgG47tF3/qPVX91GvuhYg4K3u5+XfCkBFipzGaKb14sBSaXRQzc/zUbnveBkOaHdkF8EfFhIcyZuajsxq6ixn6tEdjPuMw0/ZoOhNuLwh8+FTMJ+7OrHmXydA8YBDzjvkL6fo75g9BBYNsvaz/G2DN3ag8ObT4V7asE7MZ/dB1AlXER9rE3E8PfXinVRmUP+pjZf0DTWdIrCt4rKo8c5P+6n5m7hMXh0Qw9m4XFpx6BV+ji/7d+afbD/nhU6ONeo6kFLWjK9RmfuW2c4/jsNGflZpGPWvyjkfkCVl8w+1ORxSDZmvFvz5GPqL7GPHGwb0AQlL3ykA9SCsRnlvvI+DmDm+bh3k/FF3J4B6x8ICEIOoAHUD6zo78sOD/9omkEMGC+/qNRePl5BguQ1YuqdzKQcYHve47tpkCrZq7aV2hB+vtzBQ9R7EZ/smqODsgyIH8BlIhBHQIC+fAVsJ9Pv6j+p4nPfmie8ugVe1C0zUMA0MOfFZxhbIg7gF129+zSgZ0fH0KAGXnVzbY7oGyApc+bfuPXfdzG3QyRT7/6FQDp9/P309L5rn+vQKUAZ4F6qHrg3UcFzaHPQbcDdAAgAgoqjwvA/sApLyc8BNr5DAcAbl/t6VPi4/bLIP9RdjNtfZk4GzLPmTuBRQBUB3fGb1FD+16aAHn5POKx7j9m2tfVZtkzcrYA/cCKX54+W4YPT9Z/thWLL3I//tM26Md/b6f04HH9zwnwcRF1XdV+XC6f3PuFej+Awlo+dW0fNPz+iQjvnwjw/hsEeP9CgD9Jfxr+cfHvafgnEa8K+bhYfYA/wPMj7pVhrw9wCPmeuL5H56efCsX/A1vB8mUOUmwO3wh4/ysRfhkC2DBsAEyBwU9ibGc+HQCFP5gAxOJT8W3KzyX3Aph3IErfQMGjIwDp/wzdV8ICj4oOrO3NvWToz7u4R4G0/tvHos+yd28AVv1/dfc2M1M+J3c7b/yAw0F/1sX+4+oLJM6//7wTpu8A2V1QF19R0w6AjMUTWOfCmXPur/D23VeMfdr94KcX3vrebFA3VrMFz33e3Bk+YOve/bMm4uOHnX1YUD6AyKz9thZe1DZT+zcl+3Q6cLYLjH23mB3UzlQMnD77YS53uwX1A1T8ri4PEvr8JKF/VuhPrPYnvnr1D3b4KPO/PfmrBVF2yvucSWC7bPdZ9901QWfwGbi5fwbmzyvOYPHg1h/bnx5JAwYvHoPnG3NjAXj4sTyonPaL/e131/nanv/zMibohmYhXvlxtuPdC3PBN9hSvVt83R0Bj772q48/MBR9/vbx53lnNmfbY8r8A8wBX18nff1bi+O//fIdvZ46f46979jPgfkzF/2PLcSCodonH84x/479j4UAYQDanXX+wxl/qFQ+do6zSsCE7vmHjt/eQAXZQKb9qqHX1gMMB/j6vp3brCXAGrAguH6iAnj2f7kpeUlpIxu0w0AMFqArz7ZR113Z8Hrenm8wGF2j6Ga92SGI6yP+euMGuzXioKtgi9jOxvZWK3/r7HAM3dhA3hNhPj9LcBa5wwN4t0OAZAT2QF4iqOdtN9uNi+EIbO8cG3Owne38MTWNC+9l7tO82Zdf90cPMHla/dubs0HByBPaMvvnh1xCK3ATd0TWgfBNENoMuSqcU6ZJXtpe9kgMo3Vmk/spNI0dJdvC1aJUXO24LFPjFVMr9XHvXyNsKHJ16aJRbd2yOq03/NROCEns61QbtxLh3go+QteFj7IGj9E2K/A39UbGWi3EHEdvqcoxUKO1L2hqpmhGbVPGHHWRuwVLxPHZKnNtFU6P7AFFWp/brtD02hQQrPVlSnLOcjmlXuix2KZh+BXF2Sx9P5bJdXNUw9Za+lJQR0F4VY1Dm2kR2+y4rZ4MhVkHhQPrZoa1Za6QSrsfY2vP90MxLCe3pdc77aQeYNZsDmd9TZpYyua5VCqrg3u+jaVScZ1nECrMd8nZOouwdA+3QVCMS0nL4KVfTNtLtVkGhbQs4qVl52xooHTDtF2eiQ1xIq5RV9FuxDf1+Xrr6fW10XiPpZteudGwWl+gYHPPnVi89mZ+pRnrcDR7uThBO3ZixzFSREsUyAxyDyrpYuPk7FX50lh6zyZJpGCX5syYLtzv1Xo8pN0dEcRks9bzZeVN9aDmsnomu4SxhCEUl9m5RMnWuNYXvgjpZCTkNqw1j6HVrOZqBNadw61g7HXqb5huoAkdZaGGIFlc27jTFcWLVcK1p6N5PtQRKimHjK5rN0P5g2KPBLumjYPXExxTbs1KP1BJVBx7YpndDXjD6i0TTUpwUDGoNnnvIJeScxoNIYM7a6ne1ncaqkPIUsuSOaswxzGqXCCB2q7rdZvLEHGMzpkKxRjDFAMPSYqoiUjk3hMajVBUlewYQmq+5Dn5cgUpuA8O0hbSz8dsQ1mXyYoRFzP29dFrbbrProSZ9PZw6BAccHOsJyf9cq7umnNwckyvEN0/85Efn4JtuSZ0bItJWk4hjlQnHlzmaHxBY/wqS4dTq8XH6eoei17ZUFi46xJ3eejicJSspbDP0Cty0iHpGOVHQZ/2JVm5AQL+G9WwM4tVZzp3HokwiJugY6e2PDoc1kv4tCwlPjjvOjXBiS2D5hqO20FZUHtcXOkOcVcVi+As0cP3JdwBAJUskljn+uHS5FU8ZVbFU3GytySY4ZF2iWz3KX9dSepgE9UaUqxDyuc6jVOon6KW2B2vE6mxdMqV2lE/COEmoYl+D682obAk3D5zAyfVta22Cvd4tDH3nL485UPbEldDyC30qvl3fqLKu3EkVpCFy5PnV1GmjoJaWUfW7Y/g22R1gbuDVDufYM694M2t9JUpP2MXvOqk2GMMStVph8yW0NYUuuGe6BeN1JZS1a03co7CRrbly1Fur8Yar3QsiVopUvb3S6XbPMxVZkGEdkipSeZwXUg6qHl3qm3ljoICJZFEiJF1bIPdcr8W4WNpXXC6Ye06GRwuvgd737rBxV1ikb6tgwSqLFnfs96hkhKYJVkzs257n4Wbm6GxytSEZXPmNJJ22f2xDR0MX2NHdlpZqoKe7uJ2Jy6dFWpu9fGyHofQRC2lIpZbmc4J+pKaMt5TNS8lonyHRnQLK5wTKs4pSa1wyvv9sMe1szf0/V6pjq55xOqav559JjBpv5FvgR+7uFCF63XetOWekYITFGRIpSZYgY1jCId5heESMRQ3cZPcCngipyknHX/fXQRFRyF1WC3L02U9QDufLoLb8pQRYJ+pEclwRxK3cNVzlFiDi0o+T6MwcwVocjBlsjpaKrqjBK2NmpBrCjZS8fW+Nt2CiYsbnLZMet3Ya55yG04nWaPU7kdBOl9bNxXhihBw4WL5u10aUJaiRyybVSdRFzrY2nGCS8YNrI9FumP12DsRXXI909YQY5sjo2zRdH/i7Cpyx+7WQlEGF1d74qmWqCJPuOloZUXe/ZL0Ci7vw+KYR1tEoFCi6S/nnQ0TN6LjRFzQMgA6h9thY1ZH1V22EC5q8C64aWEGu5WZiWQgY25f0uWKDFIAiSdvX7quer1UI9Y7uIS04RpeU1RXo0PrINVOT1gvCJaCm+wu1Eqlahzw9JasMwyzfZKT44HoAFeionOYODPu9iuzhpKSGYn4JlBnZhNVbQllEFFzGZrQ24Bp4mFQRojdbujVRQTFNh1j7EDgZKf6dF46O9I7mf212lFxGotcPDgKU41XnyOa6SxRsIZ1mWXjXFXdSOforyFxQ3p6fewuSnTdxccMoXflLiqw41ngDw7mjzbXKOvaPSkBvafvlFNU4xiLm4t2GQayVguPolIiJoW8hQSyKAbGOK5TtDYwl0Iue9eiU4pPb7R5Iis9HSihX5+hQ86EGIMcVD7WybO3OlxD3pFzWttvL1c2Gu/nyRGmXgWNTrDxyWFIbVlXM3bdn3flOVYHTVXHsV0NF3igcus27bL7OaMIvadXCsQlda+WhKaeUkM1loJmTfR603ccSzQHGaOF6GRJYVKdNzJ2CrfJXTEKprIyOh86SYnwuCMNRTuM67V3OOp2lXM5b4P6IK77aWDaSjQRNuAM4bq9Vj0ZIi0rX+9xaDTwLc8s5lBhDH0/31sfsc7rkBuajScKtNwjQrO/uDnHb7ALra+E1aAXxRW7DCOXyZpPDTJBY/hkrk5xzh2T9BxzdqrkZ2upVecLbJ3Z0CxbpsHY+u5XsMmt2BA3c7+EsEhNr8ruymKEbkZmecvoRq/s8qjU1lAdsJg56YyReyJapN3SZiqJX+1RmIJOIYKCJigMXDVKJBLjVwLCx3bCsYrCrFdIjl6wjWDyBLcFmU1MzgGGDpQ8RCOX2pC7OcqEuVVKj+Dham8HRY/7oOxNP/fR20nn2CRgy7xmcdsfyZ5q0kJ2RMQ248aywjQsQOfBUvaxI4sEYzVeb/EVMBAeyFbXLUldTUUIWunTtL8YDCxY140O00eT8qpBd1GNuoyQI2u97/SiH9ABDmM+qWQD5jInrD0HcdinjaFhGEWgZefmcAaBUkvSjjwJASKMe0+dUFqT6q1kYWlh8AN5pitt3+bnWsyLncpAkXQBPZl5A4B3cQXktFwu91vKLb2jUwr9JGq+O0CwGDsKtZZktyu2jMI1sXDG0hQaBbrEOsOhnLSGWm9SUjI4G/6QsmeZ4AyOHQlCj9ORqJU778rZZtscVavgimsaNdGYbrE7JEewo9CGxwxnY6/neUIqeNnzXj2ihaEb1ZiG0QYqVdZN5JhVVbJrGsoIJP7mHFxMbISuo0fBO5/r46puKpCwGHGKkhAiBCKVAzG1eH2wz/muCvQMq3XQ79wJE6ZO4vrCd5jpy3BbQRJDBf76VHWjCTrceilrsmzK6sgJV7tm+6wiufoS17TBDFsd6vibQmxFMoJSakOfRd7c7pe7S08J9fooC5DSremM25yyNvZwaBBjTiqQQmFVmYHu5qXo67vQdLFwcZTayyzcuNBTgms3GN1W4nFPECtqx2q6B8le2cvDekVcXdg9jephqwYrmjyY5UDiwTWBYQUUh6jUTGld3TvKueXVb9dKfM45zoXaoeaXaOt5lXiB+IN9gJz+rji1lQWOC/sqIVZ1bF/u+XJHLdeqkh9iVJA302qyzszKcQ4b0Oc68aYmaJL19xKSZJONB0exbwXpipTpRRQE2/Bv905qWD2wL7jnKAgk0i2zpbO0rWKuHU+6LIXUFqQ4wlXHYbnxRk3zJts/qlmkQssVuhx6dEiI/NihqcJFmXVtExuhJ3LdTleF1csYZmM8bFc9jBzr8chiS4vbNizoAM6MejL6pCfPoP2OZOzc3Tcibyy3kKRtd17RZNN11Wkk49L4Kr3bLpYOjX5m06vL0t2SSU5KdKQl6UDA9NLALfeK87ubW4Tl7rrRxLVICWMduJUFb+Hc6Aa/7KUentgTUpuVtT0cl9V1rCprrSscNgRTjG8ZiU17sznLpN4LBgaDnc8ZbEgOt22+cagJUB7FR9RqP7hCcd36EsXXfMDkWu+NgFOwYO9e1VqLrys9uCSxtE72WkbI02a15wJX8TUL23CAl5pwPeXO7ZbxREtrx2N9PW55yGA5DZCTUKWn7T4Tw9La7cPt5EbXnkNWhT7dVArkphUkhx2y6ixdWMobm/Y9osHMEy/KF8uNjKufFQlqG61Iq6mgVSuv2/jHpWX0tn7A+zYLO1JTDV1R1hsPudPUqZdovRkIrzrCJdiJkK4sOB7KFsSUeIIVxY2QGIC5iODE61ULk8J1KQzZ3Rsmb22hnZ+ejhtOiTit2xq3jCysyagwU9ghl2ldeexdB4AroDI5GK6501KDpQx42kuHaskovZYUyl62bW1vjS15oMx6dxbltb3e+oLOQdlKRe4V3aE+qlqi4+KMK0b0kAUExwur2/FSttR1YFRRSOPM0Yp9awp+NvCmfE92y2TbnvYp12fTThM8rjXuVjuRmdq7JDLY3EF2qdUBhL+hd9SGlHtVhg9odbMjAbXHe2hw3sE5L6ktfp92sbfNM3lHrm8J11dOBuPrEQq4lbfJ1Vpk4XwMKXGZO0mIrrIRcxrDX0tGq1xw9dRjbjPZt5Bc2iF668fOzuzci66bEU/KzvJveWjinrnSopUoxoho6oKPSdTRkpm6GYZsbXfpLQySld2fEN4WxcnzPGM78PilAQTWi6m+yrZVICnt+lzvgp20RzjBWplShUDdyW7PhF4l4kZXNahmuE3g0cYJucQXwjtgIs6Kl16dWkRSR0QM46Wt4uraH/M7ErSHS8KsdqPRcY2IGBGmDwIf+3nSejuSK/nMCfYWhYzOUtwtofEGxTVy5nFW3UL98i5sj1rXylfsFmQrv2QKmWrGQr6cyx1rh8m0xQ6s791vabrMuTMVwDXoA/cb6iJqN20TdeswkXfTaUccmKQtKMlctum0mWAnXnGH2skCnjpYt8s1t2BYKq5kSjgGbcg1lV8wZyJOjKdf25HnhTu6xJAU7Ur4TvV3b32giPRsqMtweSmCoPNd01UUH3T/o+9lQjrSoKty08SmXdWVNdc5lSmOdTDW+rXjX72tcYAxdEtbpkjFxgmCPbZ2Nn3QDvdAJG21ZRR2L6jsHvKDXhR6nJm29y5mOqWyN6uTSR1WoJJNnM2NpkbMA+qRQiCCbcS4k30etXLQrx/ti4TsnWQAU8+j7w+9voq8RkOjBmxZjIqODlGrxO5RxqpJiXK1lTdsQe3OjHNZ3TUxnyqlt7x9xp+0ghfF5pwPh3Qq6fW2vRzCglGDW5SxJ+omMhcKYUmiwUckS1lHT3FIp+47aIuubxB0Pe17z7iTyE0lbkPVCHeNEHwKP9a3dcEPwSBSaN/XGrXUrt7o2rljCQ122OFaSKJHyDT7XtvVGxEjOV5ZXUXdFQ4TP0myGW8sxWihmIo4W2IIrAsEElpVlWvGfYhbfJPdmqhd0RlBFDuOngYNlwYvRpnN2O97KKhPV7NpEJDT8OoCFcIZXRvGWginvm2PO32t70zynhtGDhm2IJkHP+vPFC0KG0Q8lmhvloYPcsrp90x0Pl4qVjIh90hY+2WfLAvaYWuSGU/hsndZhdItOCuDKo1HcRqmS7u3LU8ab6AvhszOWEJT3WWT4/ndBpuSdXW4T4CMtmJ2cdGdH8EGH0gblKF3l3Eli+jtdghAMJ0C8NPE+tnttvL4uxv4nL3srxeD9DV1OW1sXMZ3XEKFZFfJgSXXeOihcrUSSvisMZeyXBeIszK9a3g1nMbsqVzakOc1tmO3cBFyYJO9CxJVcuvdXUqWTD9MNKHmlzTQabAHuuKw5QIkP1oXrAZ9D25F2jI45cTB2VcairPC6Oq2tivFvRYteWYy9kmSIPL5dLlAdalGYzRWhShzR6I4AdiJ4UAVJZFlII5vhQyDg8Oh7dNVauxavZyMKxbaBn5B+gGErMIRLrCFnctY/Z5Sb1IfxElKMInMMXjUbHVORAiElwbsaFnWktel5I4HyzgXILar10yzZs7UyrFXPa7ilNBxg1uJSEWboIU7kpm/npTuvIXRDOAq0lzvBnTbss7hbCt568lL7iTklzvimHknw3lwRB1EStHDBvRBog+VWDBWZ2xdHxGBOF0g3dht0YmsyaMGdrw3Zul1LI5jqa2ujXE0d6zLgo13l8AF0S4BIzSYBo1h3dd5pkI05psBY3tjJWCnE57fd/VSCMtDJ+02FO8u66V1kg2e926rwJb9ZdDtzWlrbxveu9pizA+yPWoqgdGUlB9SmEuaXrptbWh36kM7ukRgT9wMx+x6Mx0XrG91jmfivdPtelxDVjvoroQudFldHA/Cd043KRcv8GScSHces0tu3VCIW+lIqQK1YsI+6hwDu925dpcj7gGnsdDN1w52Aom5o3oPCjtIY0/XgVLk3J3szZT3vr+r3GJaE80VS2AKBkhSZIx8Vq7cKmHyxG+ELYhxBNtLLk6Pk+Z0G9veeMo98pRAKHTUbLcCdl+tbfQCM9vs5MKmvDMTiLrLN1M8XVaesoaxLbDnVky4YZjB5Pu8B+XtrsQTLlvu2mLl6YizvaOSpSUCKiQQlwcypXERtrLxW8rXp7g+VnYMtTC0gsV1sLLu2eEaoH7QXUTPSoyGMDBpFzmrqVsfu0txzZGDxwRYduyuyAkXWYThTwSSX28O2vrdzoGRfnPGiwuebD1yLHhP5kDbV6oETXlj7d1zZF8zzLmow2REl+rZAVhy8eTV1t4Yh4KLRRETIHOgHdVPE0OBXQkKA1JlHdopLgV32tYM5d8QAdEcchUg+LJdbdqOSIKTJPUC3+GgiKVz4sp9Viaeh2ftoWMCHiI5H8101rhzclKS+Skqb1TfW9A28IM9tj1ie9S9+8XSSoXA48PSVDcdfAOYV+L91q4inOrDWrI21+yOSFIUnHRUgVCD2u/3f3979zYfPL+Oj//NN9jms6D/Z0dSz9OjL2+mPM4PgZSPj7U+/ruK/fLurXFjoNbzCK7N+vB1VPUPB3Dv/7XXEWYZ4/MFsS+n0s9z984O5xep3+LC69uuGT+3ZfZ4RwXMcPp2fu2y/eYU7+th6DcGPW+38+son7vyc92Xj3txMb9+4nux/fUyfB1NvnvzXifOn9cb7LPfVLPBr1ccgJ3rD/CH9dvv/wdd3/VQBi8AAA== -->
