---
name: "rar-cowork-cookbook-adaptive-card-implement-project-governance-approach"
description: "Generates a read-only Adaptive Card JSON file visualizing project governance approach status from Dynamics 365 F&SCM (legal entity USMF), with KPI tiles, a RAG row, and action buttons for Teams, Outlook, or dashboards."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_implement_project_governance_approach", "rar_sha256": "ff74d1e7884ae4c612ce9a1c2e4744c2596ca5e5c1431368252c97d17c675c08", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
