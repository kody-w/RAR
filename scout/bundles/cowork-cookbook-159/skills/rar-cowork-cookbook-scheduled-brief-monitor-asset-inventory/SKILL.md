---
name: "rar-cowork-cookbook-scheduled-brief-monitor-asset-inventory"
description: "Builds a morning brief on monitor asset inventory from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs 7-day rolling average, and next actions, then saves a draft email to the owner plus a Teams"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_monitor_asset_inventory", "rar_sha256": "f5f02dd1155bf73fc224b8e92cc3fb971f847b1e30ea35b5dd3f329312f7385a", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_monitor_asset_inventory`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_monitor_asset_inventory_agent.py` and in the RCI capsule.

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

Monitor asset inventory Scheduled Email Brief — Builds a morning brief on monitor asset inventory from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs 7-day rolling average, and next actions, then saves a draft email to the owner plus a Teams

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-monitor-asset-inventory
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
      "description": "Dynamics 365 F&SCM legal entity to query; recipe defaults to USMF.",
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
    "owner": {
      "description": "Responsible owner who receives the drafted email brief.",
      "type": "string"
    },
    "schedule": {
      "description": "When to run it, e.g. weekday mornings at 7am, daily or weekly.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_monitor_asset_inventory_agent.py` and embedded as the fenced Python below (sha256 f5f02dd1155bf73f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_monitor_asset_inventory_agent.py` first:

```bash
python3 scheduled_brief_monitor_asset_inventory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_monitor_asset_inventory_agent.py   # or on stdin
python3 scheduled_brief_monitor_asset_inventory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor asset inventory Scheduled Email Brief — Builds a morning brief on monitor asset inventory from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs 7-day rolling average, and next actions, then saves a draft email to the owner plus a Teams

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-monitor-asset-inventory
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_monitor_asset_inventory',
    "version": '3.0.3',
    "display_name": 'Monitor asset inventory Scheduled Email Brief',
    "description": 'Builds a morning brief on monitor asset inventory from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs 7-day rolling average, and next actions, then saves a draft email to the owner plus a Teams',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-monitor-asset-inventory',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-monitor-asset-inventory',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd221e78b1b399a85',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/analyze-assets/monitor-asset-inventory'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/scheduled-brief-monitor-asset-inventory', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 F&SCM legal entity to query; recipe defaults to USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'When to run it, e.g. weekday mornings at 7am, daily or weekly.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where monitor asset inventory stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on monitor asset inventory for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-06-01', 'what_it_does': 'Reads monitor asset inventory, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on monitor asset inventory from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs 7-day rolling average, and next actions, then saves a draft email to the owner plus a Teams', 'example_request': 'Draft my monitor asset inventory morning brief from USMF for the owner and set it for 7am weekdays.', 'inputs': [{'description': 'Dynamics 365 F&SCM legal entity to query; recipe defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'When to run it, e.g. weekday mornings at 7am, daily or weekly.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when someone wants a daily or weekly monitor asset inventory brief for the responsible owner, drafted as an email (not sent) with a Teams channel summary.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefMonitorAssetInventory(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefMonitorAssetInventory'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 F&SCM legal entity to query; recipe defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'When to run it, e.g. weekday mornings at 7am, daily or weekly.', 'type': 'string'}},
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
    print(ScheduledBriefMonitorAssetInventory().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
