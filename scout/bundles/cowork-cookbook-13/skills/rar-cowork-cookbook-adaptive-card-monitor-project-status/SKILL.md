---
name: "rar-cowork-cookbook-adaptive-card-monitor-project-status"
description: "Generates a read-only Adaptive Card JSON file summarizing project status from Dynamics 365 F&SCM (legal entity USMF), with a header, 3-5 KPI tiles, a RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_monitor_project_status", "rar_sha256": "623e2cda693ea1e3bed383c6fdc9a9e118faa8a1a3359c38c5b87684fb957b9d", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_monitor_project_status`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_monitor_project_status_agent.py` and in the RCI capsule.

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

Monitor project status Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing project status from Dynamics 365 F&SCM (legal entity USMF), with a header, 3-5 KPI tiles, a RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-monitor-project-status
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
      "description": "Date used for the card timestamp and file name.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to read from, e.g. USMF.",
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
    },
    "status_topic": {
      "description": "What the card should visualize, e.g. monitor project status.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_monitor_project_status_agent.py` and embedded as the fenced Python below (sha256 623e2cda693ea1e3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_monitor_project_status_agent.py` first:

```bash
python3 adaptive_card_monitor_project_status_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_monitor_project_status_agent.py   # or on stdin
python3 adaptive_card_monitor_project_status_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor project status Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing project status from Dynamics 365 F&SCM (legal entity USMF), with a header, 3-5 KPI tiles, a RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-monitor-project-status
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_monitor_project_status',
    "version": '3.0.2',
    "display_name": 'Monitor project status Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file summarizing project status from Dynamics 365 F&SCM (legal entity USMF), with a header, 3-5 KPI tiles, a RAG row, and action buttons.',
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
        "upstream_slug": 'adaptive-card-monitor-project-status',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-monitor-project-status',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9ad122063c38253e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/analyze-project-performance/monitor-project-status'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/adaptive-card-monitor-project-status', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'as_of_date': 'Date used for the card timestamp and file name.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to read from, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce.', 'status_topic': 'What the card should visualize, e.g. monitor project status.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical monitor project status status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-monitor-project-status-2026-05-24-card.json' that visualizes the current state of monitor project status. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current monitor project status KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file summarizing project status from Dynamics 365 F&SCM (legal entity USMF), with a header, 3-5 KPI tiles, a RAG row, and action buttons.', 'example_request': 'Make me an Adaptive Card JSON showing project status for USMF as of 2026-05-24, read-only.', 'inputs': [{'description': 'D365 legal entity to read from, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'What the card should visualize, e.g. monitor project status.', 'name': 'status_topic'}, {'description': 'Name of the Adaptive Card JSON file to produce.', 'name': 'output_filename'}, {'description': 'Date used for the card timestamp and file name.', 'name': 'as_of_date'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable Adaptive Card snapshot of D365 project status for Teams, Outlook, or a dashboard, without changing any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardMonitorProjectStatus(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardMonitorProjectStatus'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'as_of_date': {'description': 'Date used for the card timestamp and file name.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to read from, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce.', 'type': 'string'}, 'status_topic': {'description': 'What the card should visualize, e.g. monitor project status.', 'type': 'string'}},
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
    print(AdaptiveCardMonitorProjectStatus().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
