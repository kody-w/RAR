---
name: "rar-cowork-cookbook-teams-update-report-on-inventory-quality"
description: "Summarizes inventory quality status from Dynamics 365 F&SCM for a legal entity and saves a draft Teams channel post plus an Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_report_on_inventory_quality", "rar_sha256": "aafbc9c16a0dc1427e0dc304b4c0b01ffe9954249287533cdb009dabb0548a28", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
