---
name: "rar-cowork-cookbook-scheduled-brief-correct-synchronous-integration-failures"
description: "Builds a morning brief on synchronous integration failures from Dynamics 365 F&SCM for a given legal entity and owner: top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then sav"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_correct_synchronous_integration_failures", "rar_sha256": "7fd6ce90d166aa0389105d909059865f305e1d20662fad1cae2fdf69c6f173a2", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
