---
name: "rar-cowork-cookbook-adaptive-card-maintain-and-optimize-background-jobs"
description: "Generates a read-only Adaptive Card JSON file summarizing background job status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_maintain_and_optimize_background_jobs", "rar_sha256": "72f50e3fb971662b82b863e2e326c54a799fef58ad67083c83c892cd3a865925", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_maintain_and_optimize_background_jobs`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_maintain_and_optimize_background_jobs_agent.py` and in the RCI capsule.

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

Maintain and optimize background jobs Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing background job status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-maintain-and-optimize-background-jobs
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
    "action_buttons": {
      "description": "The 2-3 action buttons to include on the card.",
      "type": "string"
    },
    "as_of_date": {
      "description": "Date/timestamp the snapshot represents.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "kpi_count": {
      "description": "How many KPI tiles to include (3-5).",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to report on, e.g. USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_maintain_and_optimize_background_jobs_agent.py` and embedded as the fenced Python below (sha256 72f50e3fb971662b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_maintain_and_optimize_background_jobs_agent.py` first:

```bash
python3 adaptive_card_maintain_and_optimize_background_jobs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_maintain_and_optimize_background_jobs_agent.py   # or on stdin
python3 adaptive_card_maintain_and_optimize_background_jobs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Maintain and optimize background jobs Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing background job status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-maintain-and-optimize-background-jobs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_maintain_and_optimize_background_jobs',
    "version": '3.0.2',
    "display_name": 'Maintain and optimize background jobs Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file summarizing background job status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.',
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
        "upstream_slug": 'adaptive-card-maintain-and-optimize-background-jobs',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-maintain-and-optimize-background-jobs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '599324ffbf1a3f86',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-background-jobs/maintain-and-optimize-background-jobs'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/adaptive-card-maintain-and-optimize-background-jobs', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'action_buttons': 'The 2-3 action buttons to include on the card.', 'as_of_date': 'Date/timestamp the snapshot represents.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'kpi_count': 'How many KPI tiles to include (3-5).', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical maintain and optimize background jobs status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-maintain-and-optimize-background-jobs-2026-05-24-card.json' that visualizes the current state of maintain and optimize background jobs. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-06-01', 'what_it_does': 'Generates an Adaptive Card JSON file with current maintain and optimize background jobs KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file summarizing background job status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.', 'example_request': 'Make an Adaptive Card JSON showing background job status in USMF as of 2026-05-24.', 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce.', 'name': 'output_filename'}, {'description': 'Date/timestamp the snapshot represents.', 'name': 'as_of_date'}, {'description': 'How many KPI tiles to include (3-5).', 'name': 'kpi_count'}, {'description': 'The 2-3 action buttons to include on the card.', 'name': 'action_buttons'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when a user wants a shareable Adaptive Card snapshot of D365 background job status for Teams, Outlook, or a dashboard, without changing data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardMaintainAndOptimizeBackgroundJobs(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardMaintainAndOptimizeBackgroundJobs'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'action_buttons': {'description': 'The 2-3 action buttons to include on the card.', 'type': 'string'}, 'as_of_date': {'description': 'Date/timestamp the snapshot represents.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'kpi_count': {'description': 'How many KPI tiles to include (3-5).', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce.', 'type': 'string'}},
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
    print(AdaptiveCardMaintainAndOptimizeBackgroundJobs().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
