---
name: "rar-cowork-cookbook-scheduled-brief-monitor-system-usage"
description: "Builds a morning brief on monitor system usage from Dynamics 365 ERP (legal entity USMF): top 5 items by impact today, anomalies vs the 7-day rolling average, and recommended next actions, then saves a draft email to the"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_monitor_system_usage", "rar_sha256": "1368eb47e02d321fd17feb1e3e97b76a582cb55b9877ffe287c7bd7551208c10", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
