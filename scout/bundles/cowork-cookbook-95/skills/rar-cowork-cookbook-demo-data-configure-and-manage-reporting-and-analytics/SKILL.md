---
name: "rar-cowork-cookbook-demo-data-configure-and-manage-reporting-and-analytics"
description: "Generates 25 realistic demo records for configure and manage reporting and analytics in a Dynamics 365 F&SCM sandbox legal entity, stages them in an Excel workbook, creates them, and returns each record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_configure_and_manage_reporting_and_analytics", "rar_sha256": "b8a8bf9e4af4508b19660e99412519039657507700ede06aec0983acc08c8379", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
