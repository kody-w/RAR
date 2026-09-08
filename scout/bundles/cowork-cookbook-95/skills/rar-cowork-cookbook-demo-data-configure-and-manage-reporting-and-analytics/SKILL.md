---
name: "rar-cowork-cookbook-demo-data-configure-and-manage-reporting-and-analytics"
description: "Generates 25 realistic demo records for configure and manage reporting and analytics in a Dynamics 365 F&SCM sandbox legal entity, stages them in an Excel workbook, creates them, and returns each record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_configure_and_manage_reporting_and_analytics", "rar_sha256": "b8a8bf9e4af4508b19660e99412519039657507700ede06aec0983acc08c8379", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_configure_and_manage_reporting_and_analytics`. The original RAPP
agent is preserved byte-for-byte in `demo_data_configure_and_manage_reporting_and_analytics_agent.py` and in the RCI capsule.

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

Configure and manage reporting and analytics Demo Data Generator — Generates 25 realistic demo records for configure and manage reporting and analytics in a Dynamics 365 F&SCM sandbox legal entity, stages them in an Excel workbook, creates them, and returns each record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-configure-and-manage-reporting-and-analytics
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
      "description": "Sandbox D365 legal entity to generate records in (default USMF).",
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
      "description": "Excel staging file name, e.g. demo-data-configure-and-manage-reporting-and-analytics-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_configure_and_manage_reporting_and_analytics_agent.py` and embedded as the fenced Python below (sha256 b8a8bf9e4af4508b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_configure_and_manage_reporting_and_analytics_agent.py` first:

```bash
python3 demo_data_configure_and_manage_reporting_and_analytics_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_configure_and_manage_reporting_and_analytics_agent.py   # or on stdin
python3 demo_data_configure_and_manage_reporting_and_analytics_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and manage reporting and analytics Demo Data Generator — Generates 25 realistic demo records for configure and manage reporting and analytics in a Dynamics 365 F&SCM sandbox legal entity, stages them in an Excel workbook, creates them, and returns each record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-configure-and-manage-reporting-and-analytics
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_configure_and_manage_reporting_and_analytics',
    "version": '3.0.3',
    "display_name": 'Configure and manage reporting and analytics Demo Data Generator',
    "description": "Generates 25 realistic demo records for configure and manage reporting and analytics in a Dynamics 365 F&SCM sandbox legal entity, stages them in an Excel workbook, creates them, and returns each record's primary key.",
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
        "upstream_slug": 'demo-data-configure-and-manage-reporting-and-analytics',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-configure-and-manage-reporting-and-analytics',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c61c1b927bc3331f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-manage-reporting-and-analytics'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/demo-data-configure-and-manage-reporting-and-analytics', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to generate records in (default USMF).', 'record_count': 'How many demo records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-configure-and-manage-reporting-and-analytics-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic configure and manage reporting and analytics data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for configure and manage reporting and analytics. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-configure-and-manage-reporting-and-analytics-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic configure and manage reporting and analytics records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo records for configure and manage reporting and analytics in a Dynamics 365 F&SCM sandbox legal entity, stages them in an Excel workbook, creates them, and returns each record's primary key.", 'example_request': 'Generate 25 demo reporting and analytics records in USMF sandbox and stage them in Excel first.', 'inputs': [{'description': 'Sandbox D365 legal entity to generate records in (default USMF).', 'name': 'legal_entity'}, {'description': 'How many demo records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-configure-and-manage-reporting-and-analytics-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need demo or training data for reporting and analytics setup in a D365 sandbox tenant; never run against production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataConfigureAndManageReportingAndAnalytics(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataConfigureAndManageReportingAndAnalytics'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to generate records in (default USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'How many demo records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-configure-and-manage-reporting-and-analytics-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataConfigureAndManageReportingAndAnalytics().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
