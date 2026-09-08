---
name: "rar-cowork-cookbook-scheduled-brief-perform-corrective-and-preventative-actions"
description: "Builds a morning brief on corrective and preventative actions from Dynamics 365 F&SCM (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then drafts an e"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_perform_corrective_and_preventative_actions", "rar_sha256": "ca13d1ee78ecb230ee8aa3b6614b17b49fff8868957606c2388ebacbdcfd2a67", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
