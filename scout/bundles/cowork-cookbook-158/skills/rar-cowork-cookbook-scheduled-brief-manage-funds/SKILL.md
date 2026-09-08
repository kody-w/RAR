---
name: "rar-cowork-cookbook-scheduled-brief-manage-funds"
description: "Builds a manage-funds morning brief from Dynamics 365 ERP data for a legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, saved as an email draft plus a Teams-ready summary."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_manage_funds", "rar_sha256": "897cab31d7fd61627d3f420d3368567c6237baaff42c3b30d409d89fd83b0cd7", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_manage_funds`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_manage_funds_agent.py` and in the RCI capsule.

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

Manage funds Scheduled Email Brief — Builds a manage-funds morning brief from Dynamics 365 ERP data for a legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, saved as an email draft plus a Teams-ready summary.

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-manage-funds
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_manage_funds_agent.py` and embedded as the fenced Python below (sha256 897cab31d7fd6162…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_manage_funds_agent.py` first:

```bash
python3 scheduled_brief_manage_funds_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_manage_funds_agent.py   # or on stdin
python3 scheduled_brief_manage_funds_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage funds Scheduled Email Brief — Builds a manage-funds morning brief from Dynamics 365 ERP data for a legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, saved as an email draft plus a Teams-ready summary.

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-manage-funds
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_manage_funds',
    "version": '3.0.3',
    "display_name": 'Manage funds Scheduled Email Brief',
    "description": 'Builds a manage-funds morning brief from Dynamics 365 ERP data for a legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, saved as an email draft plus a Teams-ready summary.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-manage-funds',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-manage-funds',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f94fc69ca76c7b29',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/manage-cash/manage-funds'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/scheduled-brief-manage-funds', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'When to run the brief, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where manage funds stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on manage funds for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads manage funds, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a manage-funds morning brief from Dynamics 365 ERP data for a legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, saved as an email draft plus a Teams-ready summary.', 'example_request': 'Draft my manage funds morning brief for USMF and send the email to drafts for the owner.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'When to run the brief, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a responsible owner wants a daily or weekly manage-funds brief drafted from D365 F&SCM, including an unsent email draft and a Teams channel post summary.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefManageFunds(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefManageFunds'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'When to run the brief, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefManageFunds().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
