---
name: "rar-cowork-cookbook-adaptive-card-implement-project-governance-approach"
description: "Generates a read-only Adaptive Card JSON file visualizing project governance approach status from Dynamics 365 F&SCM (legal entity USMF), with KPI tiles, a RAG row, and action buttons for Teams, Outlook, or dashboards."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_implement_project_governance_approach", "rar_sha256": "ff74d1e7884ae4c612ce9a1c2e4744c2596ca5e5c1431368252c97d17c675c08", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_implement_project_governance_approach`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_implement_project_governance_approach_agent.py` and in the RCI capsule.

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

Implement project governance approach Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing project governance approach status from Dynamics 365 F&SCM (legal entity USMF), with KPI tiles, a RAG row, and action buttons for Teams, Outlook, or dashboards.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-implement-project-governance-approach
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
      "description": "Snapshot date used in the card header timestamp and output filename.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "kpi_count": {
      "description": "How many KPI tiles to include (3-5), each with current value and trend arrow.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 F&SCM legal entity to read from, e.g. USMF.",
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
      "description": "Name of the Adaptive Card JSON file to produce in Documents/Cowork/output/.",
      "type": "string"
    },
    "topic": {
      "description": "The initiative or status area to visualize, e.g. implement project governance approach.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_implement_project_governance_approach_agent.py` and embedded as the fenced Python below (sha256 ff74d1e7884ae4c6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_implement_project_governance_approach_agent.py` first:

```bash
python3 adaptive_card_implement_project_governance_approach_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_implement_project_governance_approach_agent.py   # or on stdin
python3 adaptive_card_implement_project_governance_approach_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Implement project governance approach Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing project governance approach status from Dynamics 365 F&SCM (legal entity USMF), with KPI tiles, a RAG row, and action buttons for Teams, Outlook, or dashboards.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-implement-project-governance-approach
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_implement_project_governance_approach',
    "version": '3.0.2',
    "display_name": 'Implement project governance approach Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file visualizing project governance approach status from Dynamics 365 F&SCM (legal entity USMF), with KPI tiles, a RAG row, and action buttons for Teams, Outlook, or dashboards.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'adaptive-card-implement-project-governance-approach',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-implement-project-governance-approach',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '76eb1b866fafae27',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/implement-project-governance-approach'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/adaptive-card-implement-project-governance-approach', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'as_of_date': 'Snapshot date used in the card header timestamp and output filename.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'kpi_count': 'How many KPI tiles to include (3-5), each with current value and trend arrow.', 'legal_entity': 'D365 F&SCM legal entity to read from, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce in Documents/Cowork/output/.', 'topic': 'The initiative or status area to visualize, e.g. implement project governance approach.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical implement project governance approach status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-implement-project-governance-approach-2026-05-24-card.json' that visualizes the current state of implement project governance approach. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-06-01', 'what_it_does': 'Generates an Adaptive Card JSON file with current implement project governance approach KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file visualizing project governance approach status from Dynamics 365 F&SCM (legal entity USMF), with KPI tiles, a RAG row, and action buttons for Teams, Outlook, or dashboards.', 'example_request': 'Make me an Adaptive Card showing project governance approach status from D365 USMF as of 2026-05-24.', 'inputs': [{'description': 'D365 F&SCM legal entity to read from, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'The initiative or status area to visualize, e.g. implement project governance approach.', 'name': 'topic'}, {'description': 'Snapshot date used in the card header timestamp and output filename.', 'name': 'as_of_date'}, {'description': 'Name of the Adaptive Card JSON file to produce in Documents/Cowork/output/.', 'name': 'output_filename'}, {'description': 'How many KPI tiles to include (3-5), each with current value and trend arrow.', 'name': 'kpi_count'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable Adaptive Card snapshot of implement project governance approach status pulled from D365 ERP data, without changing any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardImplementProjectGovernanceApproach(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardImplementProjectGovernanceApproach'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'as_of_date': {'description': 'Snapshot date used in the card header timestamp and output filename.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'kpi_count': {'description': 'How many KPI tiles to include (3-5), each with current value and trend arrow.', 'type': 'string'}, 'legal_entity': {'description': 'D365 F&SCM legal entity to read from, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce in Documents/Cowork/output/.', 'type': 'string'}, 'topic': {'description': 'The initiative or status area to visualize, e.g. implement project governance approach.', 'type': 'string'}},
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
    print(AdaptiveCardImplementProjectGovernanceApproach().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
