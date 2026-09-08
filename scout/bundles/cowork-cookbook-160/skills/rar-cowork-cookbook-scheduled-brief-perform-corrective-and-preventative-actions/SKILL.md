---
name: "rar-cowork-cookbook-scheduled-brief-perform-corrective-and-preventative-actions"
description: "Builds a morning brief on corrective and preventative actions from Dynamics 365 F&SCM (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then drafts an e"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_perform_corrective_and_preventative_actions", "rar_sha256": "ca13d1ee78ecb230ee8aa3b6614b17b49fff8868957606c2388ebacbdcfd2a67", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_perform_corrective_and_preventative_actions`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_perform_corrective_and_preventative_actions_agent.py` and in the RCI capsule.

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

Perform corrective and preventative actions Scheduled Email Brief — Builds a morning brief on corrective and preventative actions from Dynamics 365 F&SCM (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then drafts an e

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-perform-corrective-and-preventative-actions
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
      "description": "Dynamics 365 F&SCM legal entity to query; defaults to USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_perform_corrective_and_preventative_actions_agent.py` and embedded as the fenced Python below (sha256 ca13d1ee78ecb230…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_perform_corrective_and_preventative_actions_agent.py` first:

```bash
python3 scheduled_brief_perform_corrective_and_preventative_actions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_perform_corrective_and_preventative_actions_agent.py   # or on stdin
python3 scheduled_brief_perform_corrective_and_preventative_actions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Perform corrective and preventative actions Scheduled Email Brief — Builds a morning brief on corrective and preventative actions from Dynamics 365 F&SCM (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then drafts an e

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-perform-corrective-and-preventative-actions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_perform_corrective_and_preventative_actions',
    "version": '3.0.3',
    "display_name": 'Perform corrective and preventative actions Scheduled Email Brief',
    "description": 'Builds a morning brief on corrective and preventative actions from Dynamics 365 F&SCM (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then drafts an e',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-perform-corrective-and-preventative-actions',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-perform-corrective-and-preventative-actions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f8f39dcdfbf9d1ed',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-inventory-quality/perform-corrective-and-preventative-actions'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/scheduled-brief-perform-corrective-and-preventative-actions', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 F&SCM legal entity to query; defaults to USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'When the brief should run, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where perform corrective and preventative actions stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on perform corrective and preventative actions for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads perform corrective and preventative actions, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on corrective and preventative actions from Dynamics 365 F&SCM (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then drafts an e', 'example_request': 'Give me the CAPA morning brief for USMF and draft the email to the owner.', 'inputs': [{'description': 'Dynamics 365 F&SCM legal entity to query; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'When the brief should run, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a daily or weekly CAPA morning brief for the responsible owner, as an email draft and Teams channel post, from D365 ERP data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefPerformCorrectiveAndPreventativeActions(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefPerformCorrectiveAndPreventativeActions'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 F&SCM legal entity to query; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'When the brief should run, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefPerformCorrectiveAndPreventativeActions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
