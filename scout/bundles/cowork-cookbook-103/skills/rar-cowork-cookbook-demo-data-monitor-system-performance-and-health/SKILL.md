---
name: "rar-cowork-cookbook-demo-data-monitor-system-performance-and-health"
description: "Generates 25 realistic demo records for system performance and health monitoring in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_monitor_system_performance_and_health", "rar_sha256": "ca152312e684fc923ffe43f4a10d268b1b083f8e7e3567f686b1e63c67220186", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
