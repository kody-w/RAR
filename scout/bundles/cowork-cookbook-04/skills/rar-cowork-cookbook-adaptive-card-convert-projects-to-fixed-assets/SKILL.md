---
name: "rar-cowork-cookbook-adaptive-card-convert-projects-to-fixed-assets"
description: "Generates a read-only Adaptive Card JSON file showing convert-projects-to-fixed-assets status from Dynamics 365 F&SCM (legal entity USMF), with KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_convert_projects_to_fixed_assets", "rar_sha256": "ee4a756223f52d0df8b0cb65483d93f07db34abde4cabc0df95d33a1410d3953", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_convert_projects_to_fixed_assets`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_convert_projects_to_fixed_assets_agent.py` and in the RCI capsule.

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

Convert projects to fixed assets Status Adaptive Card — Generates a read-only Adaptive Card JSON file showing convert-projects-to-fixed-assets status from Dynamics 365 F&SCM (legal entity USMF), with KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-convert-projects-to-fixed-assets
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
    "as_of_date": {
      "description": "Snapshot date used in the card timestamp and output filename.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to query, e.g. USMF.",
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
    "output_filename": {
      "description": "Name of the Adaptive Card JSON file to produce.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_convert_projects_to_fixed_assets_agent.py` and embedded as the fenced Python below (sha256 ee4a756223f52d0d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_convert_projects_to_fixed_assets_agent.py` first:

```bash
python3 adaptive_card_convert_projects_to_fixed_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_convert_projects_to_fixed_assets_agent.py   # or on stdin
python3 adaptive_card_convert_projects_to_fixed_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Convert projects to fixed assets Status Adaptive Card — Generates a read-only Adaptive Card JSON file showing convert-projects-to-fixed-assets status from Dynamics 365 F&SCM (legal entity USMF), with KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-convert-projects-to-fixed-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_convert_projects_to_fixed_assets',
    "version": '3.0.2',
    "display_name": 'Convert projects to fixed assets Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file showing convert-projects-to-fixed-assets status from Dynamics 365 F&SCM (legal entity USMF), with KPI tiles, RAG row, and action buttons.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-convert-projects-to-fixed-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-convert-projects-to-fixed-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '46720b175723b1f8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-financials/convert-projects-to-fixed-assets'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/adaptive-card-convert-projects-to-fixed-assets', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'as_of_date': 'Snapshot date used in the card timestamp and output filename.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical convert projects to fixed assets status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-convert-projects-to-fixed-assets-2026-05-24-card.json' that visualizes the current state of convert projects to fixed assets. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current convert projects to fixed assets KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file showing convert-projects-to-fixed-assets status from Dynamics 365 F&SCM (legal entity USMF), with KPI tiles, RAG row, and action buttons.', 'example_request': 'Make an Adaptive Card showing convert projects to fixed assets status in USMF as of 2026-05-24.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Snapshot date used in the card timestamp and output filename.', 'name': 'as_of_date'}, {'description': 'Name of the Adaptive Card JSON file to produce.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable Adaptive Card snapshot of convert projects to fixed assets status for Teams, Outlook, or a dashboard.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardConvertProjectsToFixedAssets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardConvertProjectsToFixedAssets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'as_of_date': {'description': 'Snapshot date used in the card timestamp and output filename.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce.', 'type': 'string'}},
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
    print(AdaptiveCardConvertProjectsToFixedAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
