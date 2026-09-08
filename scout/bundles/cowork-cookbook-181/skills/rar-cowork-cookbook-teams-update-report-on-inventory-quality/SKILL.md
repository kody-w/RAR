---
name: "rar-cowork-cookbook-teams-update-report-on-inventory-quality"
description: "Summarizes inventory quality status from Dynamics 365 F&SCM for a legal entity and saves a draft Teams channel post plus an Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_report_on_inventory_quality", "rar_sha256": "aafbc9c16a0dc1427e0dc304b4c0b01ffe9954249287533cdb009dabb0548a28", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_report_on_inventory_quality`. The original RAPP
agent is preserved byte-for-byte in `teams_update_report_on_inventory_quality_agent.py` and in the RCI capsule.

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

Report on inventory quality Teams Channel Update — Summarizes inventory quality status from Dynamics 365 F&SCM for a legal entity and saves a draft Teams channel post plus an Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-report-on-inventory-quality
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
    "card_filename": {
      "description": "Output filename for the Adaptive Card JSON artifact.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to report on (e.g., USMF).",
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
    "report_date": {
      "description": "Date used for the report and card filename (e.g., 2026-05-24).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_report_on_inventory_quality_agent.py` and embedded as the fenced Python below (sha256 aafbc9c16a0dc142…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_report_on_inventory_quality_agent.py` first:

```bash
python3 teams_update_report_on_inventory_quality_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_report_on_inventory_quality_agent.py   # or on stdin
python3 teams_update_report_on_inventory_quality_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Report on inventory quality Teams Channel Update — Summarizes inventory quality status from Dynamics 365 F&SCM for a legal entity and saves a draft Teams channel post plus an Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-report-on-inventory-quality
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_report_on_inventory_quality',
    "version": '3.0.3',
    "display_name": 'Report on inventory quality Teams Channel Update',
    "description": 'Summarizes inventory quality status from Dynamics 365 F&SCM for a legal entity and saves a draft Teams channel post plus an Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-report-on-inventory-quality',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-report-on-inventory-quality',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd06251826a5449bd',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/analyze-warehouse-operations/report-on-inventory-quality'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/teams-update-report-on-inventory-quality', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Output filename for the Adaptive Card JSON artifact.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on (e.g., USMF).', 'report_date': 'Date used for the report and card filename (e.g., 2026-05-24).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of report on inventory quality. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-report-on-inventory-quality-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads report on inventory quality, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes inventory quality status from Dynamics 365 F&SCM for a legal entity and saves a draft Teams channel post plus an Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted.', 'example_request': "Draft a Teams update on inventory quality for USMF as of 2026-05-24 with an Adaptive Card — don't post it.", 'inputs': [{'description': 'D365 legal entity to report on (e.g., USMF).', 'name': 'legal_entity'}, {'description': 'Date used for the report and card filename (e.g., 2026-05-24).', 'name': 'report_date'}, {'description': 'Output filename for the Adaptive Card JSON artifact.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a reviewable Teams channel update on inventory quality status from D365 ERP data, with an Adaptive Card artifact saved for manual posting.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateReportOnInventoryQuality(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateReportOnInventoryQuality'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Output filename for the Adaptive Card JSON artifact.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on (e.g., USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'report_date': {'description': 'Date used for the report and card filename (e.g., 2026-05-24).', 'type': 'string'}},
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
    print(TeamsUpdateReportOnInventoryQuality().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
