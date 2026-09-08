---
name: "rar-cowork-cookbook-scheduled-brief-configure-and-monitor-system-generated-numbers"
description: "Builds a morning brief on system generated number sequences from Dynamics 365 F&SCM (legal entity USMF), covering top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions; drafts an ema"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_configure_and_monitor_system_generated_numbers", "rar_sha256": "8459c69f34b882b03e16446dfb1301d1ae9a4b1672d893575d754bdfd50a10f3", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_configure_and_monitor_system_generated_numbers`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_configure_and_monitor_system_generated_numbers_agent.py` and in the RCI capsule.

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

Configure and monitor system generated numbers Scheduled Email Brief — Builds a morning brief on system generated number sequences from Dynamics 365 F&SCM (legal entity USMF), covering top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions; drafts an ema

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-configure-and-monitor-system-generated-numbers
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
      "description": "D365 legal entity to run against; defaults to USMF.",
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
      "description": "The responsible owner who receives the drafted email brief.",
      "type": "string"
    },
    "schedule": {
      "description": "When the brief should run, e.g. weekday mornings at 7am.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_configure_and_monitor_system_generated_numbers_agent.py` and embedded as the fenced Python below (sha256 8459c69f34b882b0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_configure_and_monitor_system_generated_numbers_agent.py` first:

```bash
python3 scheduled_brief_configure_and_monitor_system_generated_numbers_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_configure_and_monitor_system_generated_numbers_agent.py   # or on stdin
python3 scheduled_brief_configure_and_monitor_system_generated_numbers_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and monitor system generated numbers Scheduled Email Brief — Builds a morning brief on system generated number sequences from Dynamics 365 F&SCM (legal entity USMF), covering top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions; drafts an ema

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-configure-and-monitor-system-generated-numbers
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_configure_and_monitor_system_generated_numbers',
    "version": '3.0.3',
    "display_name": 'Configure and monitor system generated numbers Scheduled Email Brief',
    "description": 'Builds a morning brief on system generated number sequences from Dynamics 365 F&SCM (legal entity USMF), covering top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions; drafts an ema',
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
        "upstream_slug": 'scheduled-brief-configure-and-monitor-system-generated-numbers',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-configure-and-monitor-system-generated-numbers',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '712782eef1db495b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-monitor-system-generated-numbers'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/scheduled-brief-configure-and-monitor-system-generated-numbers', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against; defaults to USMF.', 'owner': 'The responsible owner who receives the drafted email brief.', 'schedule': 'When the brief should run, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where configure and monitor system generated numbers stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on configure and monitor system generated numbers for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads configure and monitor system generated numbers, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on system generated number sequences from Dynamics 365 F&SCM (legal entity USMF), covering top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions; drafts an ema', 'example_request': 'Give me the morning brief on system generated numbers in USMF and draft it to the owner.', 'inputs': [{'description': 'D365 legal entity to run against; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'The responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'When the brief should run, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a daily or weekly brief on configure and monitor system generated numbers in D365, as an email draft and Teams post summary.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefConfigureAndMonitorSystemGeneratedNumbers(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefConfigureAndMonitorSystemGeneratedNumbers'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'The responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'When the brief should run, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefConfigureAndMonitorSystemGeneratedNumbers().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
