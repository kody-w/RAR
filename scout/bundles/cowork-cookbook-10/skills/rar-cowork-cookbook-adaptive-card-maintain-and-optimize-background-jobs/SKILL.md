---
name: "rar-cowork-cookbook-adaptive-card-maintain-and-optimize-background-jobs"
description: "Generates a read-only Adaptive Card JSON file summarizing background job status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_maintain_and_optimize_background_jobs", "rar_sha256": "72f50e3fb971662b82b863e2e326c54a799fef58ad67083c83c892cd3a865925", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
