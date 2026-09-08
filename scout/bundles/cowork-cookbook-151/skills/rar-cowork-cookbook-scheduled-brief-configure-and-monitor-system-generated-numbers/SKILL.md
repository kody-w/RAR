---
name: "rar-cowork-cookbook-scheduled-brief-configure-and-monitor-system-generated-numbers"
description: "Builds a morning brief on system generated number sequences from Dynamics 365 F&SCM (legal entity USMF), covering top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions; drafts an ema"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_configure_and_monitor_system_generated_numbers", "rar_sha256": "8459c69f34b882b03e16446dfb1301d1ae9a4b1672d893575d754bdfd50a10f3", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
