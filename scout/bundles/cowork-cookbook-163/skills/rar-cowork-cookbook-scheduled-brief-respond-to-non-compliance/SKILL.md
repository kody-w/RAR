---
name: "rar-cowork-cookbook-scheduled-brief-respond-to-non-compliance"
description: "Builds a morning brief on responding to non-compliance from Dynamics 365 F&SCM data for a legal entity, with top 5 items by impact, anomalies vs the 7-day average, and next actions; drafts an email to the owner (unsent)"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_respond_to_non_compliance", "rar_sha256": "fdb0f234eafa70db0ef61e3775576a95f54bff2ae1031e4a981f89de9d336933", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
