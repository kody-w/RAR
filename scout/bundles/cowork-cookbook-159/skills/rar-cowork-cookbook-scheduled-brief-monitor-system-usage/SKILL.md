---
name: "rar-cowork-cookbook-scheduled-brief-monitor-system-usage"
description: "Builds a morning brief on monitor system usage from Dynamics 365 ERP (legal entity USMF): top 5 items by impact today, anomalies vs the 7-day rolling average, and recommended next actions, then saves a draft email to the"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_monitor_system_usage", "rar_sha256": "1368eb47e02d321fd17feb1e3e97b76a582cb55b9877ffe287c7bd7551208c10", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_monitor_system_usage`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_monitor_system_usage_agent.py` and in the RCI capsule.

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

Monitor system usage Scheduled Email Brief — Builds a morning brief on monitor system usage from Dynamics 365 ERP (legal entity USMF): top 5 items by impact today, anomalies vs the 7-day rolling average, and recommended next actions, then saves a draft email to the

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-monitor-system-usage
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
      "description": "Dynamics 365 F&SCM legal entity to query (default USMF).",
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
      "description": "Responsible owner who receives the drafted email.",
      "type": "string"
    },
    "schedule": {
      "description": "When to run the brief, e.g. weekday mornings at 7am.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_monitor_system_usage_agent.py` and embedded as the fenced Python below (sha256 1368eb47e02d321f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_monitor_system_usage_agent.py` first:

```bash
python3 scheduled_brief_monitor_system_usage_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_monitor_system_usage_agent.py   # or on stdin
python3 scheduled_brief_monitor_system_usage_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor system usage Scheduled Email Brief — Builds a morning brief on monitor system usage from Dynamics 365 ERP (legal entity USMF): top 5 items by impact today, anomalies vs the 7-day rolling average, and recommended next actions, then saves a draft email to the

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-monitor-system-usage
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_monitor_system_usage',
    "version": '3.0.3',
    "display_name": 'Monitor system usage Scheduled Email Brief',
    "description": 'Builds a morning brief on monitor system usage from Dynamics 365 ERP (legal entity USMF): top 5 items by impact today, anomalies vs the 7-day rolling average, and recommended next actions, then saves a draft email to the',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-monitor-system-usage',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-monitor-system-usage',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '06a79291d8fa7c1a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/monitor-systems-environments-and-capacity/monitor-system-usage'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/scheduled-brief-monitor-system-usage', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 F&SCM legal entity to query (default USMF).', 'owner': 'Responsible owner who receives the drafted email.', 'schedule': 'When to run the brief, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where monitor system usage stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on monitor system usage for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads monitor system usage, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on monitor system usage from Dynamics 365 ERP (legal entity USMF): top 5 items by impact today, anomalies vs the 7-day rolling average, and recommended next actions, then saves a draft email to the', 'example_request': 'Draft my 7am weekday monitor system usage brief from USMF and save the email to drafts.', 'inputs': [{'description': 'Dynamics 365 F&SCM legal entity to query (default USMF).', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email.', 'name': 'owner'}, {'description': 'When to run the brief, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a responsible owner wants a recurring (daily/weekly, e.g. weekday 7am) usage brief drafted as an unsent email and a Teams channel post.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefMonitorSystemUsage(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefMonitorSystemUsage'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 F&SCM legal entity to query (default USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email.', 'type': 'string'}, 'schedule': {'description': 'When to run the brief, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefMonitorSystemUsage().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
