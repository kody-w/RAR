---
name: "rar-cowork-cookbook-scheduled-brief-manage-funds"
description: "Builds a manage-funds morning brief from Dynamics 365 ERP data for a legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, saved as an email draft plus a Teams-ready summary."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_manage_funds", "rar_sha256": "897cab31d7fd61627d3f420d3368567c6237baaff42c3b30d409d89fd83b0cd7", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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
