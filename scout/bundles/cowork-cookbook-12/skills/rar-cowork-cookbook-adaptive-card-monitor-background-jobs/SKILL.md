---
name: "rar-cowork-cookbook-adaptive-card-monitor-background-jobs"
description: "Generates a read-only Adaptive Card JSON file snapshotting background job status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_monitor_background_jobs", "rar_sha256": "64af739fe503292c11094bb049efecf6787254941ab4d24ebbcdf8c99bb35ef2", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
