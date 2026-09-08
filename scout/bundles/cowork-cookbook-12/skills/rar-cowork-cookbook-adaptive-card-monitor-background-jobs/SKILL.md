---
name: "rar-cowork-cookbook-adaptive-card-monitor-background-jobs"
description: "Generates a read-only Adaptive Card JSON file snapshotting background job status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_monitor_background_jobs", "rar_sha256": "64af739fe503292c11094bb049efecf6787254941ab4d24ebbcdf8c99bb35ef2", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_monitor_background_jobs`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_monitor_background_jobs_agent.py` and in the RCI capsule.

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

Monitor background jobs Status Adaptive Card — Generates a read-only Adaptive Card JSON file snapshotting background job status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-monitor-background-jobs
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-monitor-background-jobs-2026-05-24-card.json.",
      "type": "string"
    },
    "snapshot_date": {
      "description": "Date/timestamp the card header should reflect.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_monitor_background_jobs_agent.py` and embedded as the fenced Python below (sha256 64af739fe503292c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_monitor_background_jobs_agent.py` first:

```bash
python3 adaptive_card_monitor_background_jobs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_monitor_background_jobs_agent.py   # or on stdin
python3 adaptive_card_monitor_background_jobs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor background jobs Status Adaptive Card — Generates a read-only Adaptive Card JSON file snapshotting background job status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-monitor-background-jobs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_monitor_background_jobs',
    "version": '3.0.2',
    "display_name": 'Monitor background jobs Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file snapshotting background job status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, RAG row, and action buttons.',
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
        "upstream_slug": 'adaptive-card-monitor-background-jobs',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-monitor-background-jobs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'caea781e46161724',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-background-jobs/monitor-background-jobs'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/adaptive-card-monitor-background-jobs', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-monitor-background-jobs-2026-05-24-card.json.', 'snapshot_date': 'Date/timestamp the card header should reflect.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical monitor background jobs status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-monitor-background-jobs-2026-05-24-card.json' that visualizes the current state of monitor background jobs. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-06-01', 'what_it_does': 'Generates an Adaptive Card JSON file with current monitor background jobs KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file snapshotting background job status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, RAG row, and action buttons.', 'example_request': 'Make an Adaptive Card JSON of background job status in USMF for today, with KPI tiles and a RAG row.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-monitor-background-jobs-2026-05-24-card.json.', 'name': 'output_filename'}, {'description': 'Date/timestamp the card header should reflect.', 'name': 'snapshot_date'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a Teams/Outlook/designer-ready Adaptive Card showing current D365 background job status, without changing any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardMonitorBackgroundJobs(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardMonitorBackgroundJobs'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-monitor-background-jobs-2026-05-24-card.json.', 'type': 'string'}, 'snapshot_date': {'description': 'Date/timestamp the card header should reflect.', 'type': 'string'}},
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
    print(AdaptiveCardMonitorBackgroundJobs().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
