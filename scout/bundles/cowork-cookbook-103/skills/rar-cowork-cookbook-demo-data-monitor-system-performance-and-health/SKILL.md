---
name: "rar-cowork-cookbook-demo-data-monitor-system-performance-and-health"
description: "Generates 25 realistic demo records for system performance and health monitoring in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_monitor_system_performance_and_health", "rar_sha256": "ca152312e684fc923ffe43f4a10d268b1b083f8e7e3567f686b1e63c67220186", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_monitor_system_performance_and_health`. The original RAPP
agent is preserved byte-for-byte in `demo_data_monitor_system_performance_and_health_agent.py` and in the RCI capsule.

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

Monitor system performance and health Demo Data Generator — Generates 25 realistic demo records for system performance and health monitoring in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-monitor-system-performance-and-health
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
      "description": "Sandbox D365 legal entity to target (default USMF); must not be production.",
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
    "record_count": {
      "description": "How many demo records to generate (default 25).",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, default demo-data-monitor-system-performance-and-health-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_monitor_system_performance_and_health_agent.py` and embedded as the fenced Python below (sha256 ca152312e684fc92…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_monitor_system_performance_and_health_agent.py` first:

```bash
python3 demo_data_monitor_system_performance_and_health_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_monitor_system_performance_and_health_agent.py   # or on stdin
python3 demo_data_monitor_system_performance_and_health_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor system performance and health Demo Data Generator — Generates 25 realistic demo records for system performance and health monitoring in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-monitor-system-performance-and-health
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_monitor_system_performance_and_health',
    "version": '3.0.3',
    "display_name": 'Monitor system performance and health Demo Data Generator',
    "description": "Generates 25 realistic demo records for system performance and health monitoring in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-monitor-system-performance-and-health',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-monitor-system-performance-and-health',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'fc3959800c679869',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/monitor-systems-environments-and-capacity/monitor-system-performance-and-health'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/demo-data-monitor-system-performance-and-health', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'record_count': 'How many demo records to generate (default 25).', 'workbook_name': 'Excel staging file name, default demo-data-monitor-system-performance-and-health-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic monitor system performance and health data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for monitor system performance and health. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-monitor-system-performance-and-health-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic monitor system performance and health records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo records for system performance and health monitoring in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary", 'example_request': 'Generate 25 demo system performance and health records in the USMF sandbox and stage them in Excel first.', 'inputs': [{'description': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'name': 'legal_entity'}, {'description': 'How many demo records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, default demo-data-monitor-system-performance-and-health-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need demo/training data for system performance and health monitoring created in a D365 sandbox legal entity — never against production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataMonitorSystemPerformanceAndHealth(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataMonitorSystemPerformanceAndHealth'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'How many demo records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, default demo-data-monitor-system-performance-and-health-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataMonitorSystemPerformanceAndHealth().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
