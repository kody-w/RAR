---
name: "rar-cowork-cookbook-scheduled-brief-respond-to-non-compliance"
description: "Builds a morning brief on responding to non-compliance from Dynamics 365 F&SCM data for a legal entity, with top 5 items by impact, anomalies vs the 7-day average, and next actions; drafts an email to the owner (unsent)"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_respond_to_non_compliance", "rar_sha256": "fdb0f234eafa70db0ef61e3775576a95f54bff2ae1031e4a981f89de9d336933", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_respond_to_non_compliance`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_respond_to_non_compliance_agent.py` and in the RCI capsule.

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

Respond to non-compliance Scheduled Email Brief — Builds a morning brief on responding to non-compliance from Dynamics 365 F&SCM data for a legal entity, with top 5 items by impact, anomalies vs the 7-day average, and next actions; drafts an email to the owner (unsent)

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-respond-to-non-compliance
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
      "description": "Optional cadence for running it, e.g. weekday mornings at 7am.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_respond_to_non_compliance_agent.py` and embedded as the fenced Python below (sha256 fdb0f234eafa70db…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_respond_to_non_compliance_agent.py` first:

```bash
python3 scheduled_brief_respond_to_non_compliance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_respond_to_non_compliance_agent.py   # or on stdin
python3 scheduled_brief_respond_to_non_compliance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Respond to non-compliance Scheduled Email Brief — Builds a morning brief on responding to non-compliance from Dynamics 365 F&SCM data for a legal entity, with top 5 items by impact, anomalies vs the 7-day average, and next actions; drafts an email to the owner (unsent)

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-respond-to-non-compliance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_respond_to_non_compliance',
    "version": '3.0.3',
    "display_name": 'Respond to non-compliance Scheduled Email Brief',
    "description": 'Builds a morning brief on responding to non-compliance from Dynamics 365 F&SCM data for a legal entity, with top 5 items by impact, anomalies vs the 7-day average, and next actions; drafts an email to the owner (unsent)',
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
        "upstream_slug": 'scheduled-brief-respond-to-non-compliance',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-respond-to-non-compliance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '05b868ffa1d76cb5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-compliance/respond-to-non-compliance'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/scheduled-brief-respond-to-non-compliance', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'Optional cadence for running it, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where respond to non-compliance stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on respond to non-compliance for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads respond to non-compliance, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on responding to non-compliance from Dynamics 365 F&SCM data for a legal entity, with top 5 items by impact, anomalies vs the 7-day average, and next actions; drafts an email to the owner (unsent)', 'example_request': 'Give me the non-compliance morning brief for USMF and draft it to the owner.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'Optional cadence for running it, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when someone wants a daily or weekly non-compliance brief for the responsible owner, drafted as an email and a Teams channel post.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefRespondToNonCompliance(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefRespondToNonCompliance'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'Optional cadence for running it, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefRespondToNonCompliance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
