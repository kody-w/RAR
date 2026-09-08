---
name: "rar-cowork-cookbook-scheduled-brief-correct-synchronous-integration-failures"
description: "Builds a morning brief on synchronous integration failures from Dynamics 365 F&SCM for a given legal entity and owner: top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then sav"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_correct_synchronous_integration_failures", "rar_sha256": "7fd6ce90d166aa0389105d909059865f305e1d20662fad1cae2fdf69c6f173a2", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_correct_synchronous_integration_failures`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_correct_synchronous_integration_failures_agent.py` and in the RCI capsule.

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

Correct synchronous integration failures Scheduled Email Brief — Builds a morning brief on synchronous integration failures from Dynamics 365 F&SCM for a given legal entity and owner: top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then sav

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-correct-synchronous-integration-failures
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
    "owner": {
      "description": "Responsible owner who receives the drafted email brief.",
      "type": "string"
    },
    "schedule": {
      "description": "Optional cadence/time for the recurring run, e.g. weekdays at 7am.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_correct_synchronous_integration_failures_agent.py` and embedded as the fenced Python below (sha256 7fd6ce90d166aa03…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_correct_synchronous_integration_failures_agent.py` first:

```bash
python3 scheduled_brief_correct_synchronous_integration_failures_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_correct_synchronous_integration_failures_agent.py   # or on stdin
python3 scheduled_brief_correct_synchronous_integration_failures_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Correct synchronous integration failures Scheduled Email Brief — Builds a morning brief on synchronous integration failures from Dynamics 365 F&SCM for a given legal entity and owner: top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then sav

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-correct-synchronous-integration-failures
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_correct_synchronous_integration_failures',
    "version": '3.0.3',
    "display_name": 'Correct synchronous integration failures Scheduled Email Brief',
    "description": 'Builds a morning brief on synchronous integration failures from Dynamics 365 F&SCM for a given legal entity and owner: top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then sav',
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
        "upstream_slug": 'scheduled-brief-correct-synchronous-integration-failures',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-correct-synchronous-integration-failures',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a4db18d4a544d4db',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/monitor-systems-environments-and-capacity/correct-synchronous-integration-failures'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/scheduled-brief-correct-synchronous-integration-failures', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'Optional cadence/time for the recurring run, e.g. weekdays at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where correct synchronous integration failures stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on correct synchronous integration failures for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads correct synchronous integration failures, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on synchronous integration failures from Dynamics 365 F&SCM for a given legal entity and owner: top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then sav', 'example_request': 'Draft my 7am weekday brief on sync integration failures in USMF and email it to the owner as a draft.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'Optional cadence/time for the recurring run, e.g. weekdays at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when someone wants a daily or weekly D365 ERP integration-failure brief drafted for an owner, or wants it scheduled for weekday mornings.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefCorrectSynchronousIntegrationFailures(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefCorrectSynchronousIntegrationFailures'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'Optional cadence/time for the recurring run, e.g. weekdays at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefCorrectSynchronousIntegrationFailures().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
