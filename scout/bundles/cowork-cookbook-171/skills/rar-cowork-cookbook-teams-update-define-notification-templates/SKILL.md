---
name: "rar-cowork-cookbook-teams-update-define-notification-templates"
description: "Summarizes notification-template status from Dynamics 365 F&SCM for a legal entity and returns a Teams-ready markdown channel post plus a saved Adaptive Card JSON file; nothing is posted automatically."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_define_notification_templates", "rar_sha256": "dd9e5622ab0e375f135d258c95696e1994937fbddf6428f6b9528bce6cbcd3ae", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_define_notification_templates`. The original RAPP
agent is preserved byte-for-byte in `teams_update_define_notification_templates_agent.py` and in the RCI capsule.

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

Define notification templates Teams Channel Update — Summarizes notification-template status from Dynamics 365 F&SCM for a legal entity and returns a Teams-ready markdown channel post plus a saved Adaptive Card JSON file; nothing is posted automatically.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-define-notification-templates
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
    "card_filename": {
      "description": "Output filename for the Adaptive Card JSON, e.g. teams-update-define-notification-templates-2026-05-24-card.json.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to summarize, e.g. USMF.",
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
    "quick_actions": {
      "description": "Quick-action buttons to include on the card, e.g. 'View detail', 'Open in D365'.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_define_notification_templates_agent.py` and embedded as the fenced Python below (sha256 dd9e5622ab0e375f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_define_notification_templates_agent.py` first:

```bash
python3 teams_update_define_notification_templates_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_define_notification_templates_agent.py   # or on stdin
python3 teams_update_define_notification_templates_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define notification templates Teams Channel Update — Summarizes notification-template status from Dynamics 365 F&SCM for a legal entity and returns a Teams-ready markdown channel post plus a saved Adaptive Card JSON file; nothing is posted automatically.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-define-notification-templates
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_define_notification_templates',
    "version": '3.0.3',
    "display_name": 'Define notification templates Teams Channel Update',
    "description": 'Summarizes notification-template status from Dynamics 365 F&SCM for a legal entity and returns a Teams-ready markdown channel post plus a saved Adaptive Card JSON file; nothing is posted automatically.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-define-notification-templates',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-define-notification-templates',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1b63f30d3163968a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-notifications-alerts/define-notification-templates'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/teams-update-define-notification-templates', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Output filename for the Adaptive Card JSON, e.g. teams-update-define-notification-templates-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to summarize, e.g. USMF.', 'quick_actions': "Quick-action buttons to include on the card, e.g. 'View detail', 'Open in D365'."}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of define notification templates. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-define-notification-templates-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads define notification templates, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes notification-template status from Dynamics 365 F&SCM for a legal entity and returns a Teams-ready markdown channel post plus a saved Adaptive Card JSON file; nothing is posted automatically.', 'example_request': "Draft a Teams update on define notification templates for USMF with an Adaptive Card, but don't post it.", 'inputs': [{'description': 'D365 legal entity to summarize, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-define-notification-templates-2026-05-24-card.json.', 'name': 'card_filename'}, {'description': "Quick-action buttons to include on the card, e.g. 'View detail', 'Open in D365'.", 'name': 'quick_actions'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a reviewable Teams channel update and Adaptive Card on define-notification-templates status from D365 ERP data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateDefineNotificationTemplates(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateDefineNotificationTemplates'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-define-notification-templates-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to summarize, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'quick_actions': {'description': "Quick-action buttons to include on the card, e.g. 'View detail', 'Open in D365'.", 'type': 'string'}},
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
    print(TeamsUpdateDefineNotificationTemplates().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
