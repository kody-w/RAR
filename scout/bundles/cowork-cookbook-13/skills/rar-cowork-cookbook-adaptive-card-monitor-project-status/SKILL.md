---
name: "rar-cowork-cookbook-adaptive-card-monitor-project-status"
description: "Generates a read-only Adaptive Card JSON file summarizing project status from Dynamics 365 F&SCM (legal entity USMF), with a header, 3-5 KPI tiles, a RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_monitor_project_status", "rar_sha256": "623e2cda693ea1e3bed383c6fdc9a9e118faa8a1a3359c38c5b87684fb957b9d", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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
