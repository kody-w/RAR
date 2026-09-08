---
name: "rar-cowork-cookbook-teams-update-define-notification-templates"
description: "Summarizes notification-template status from Dynamics 365 F&SCM for a legal entity and returns a Teams-ready markdown channel post plus a saved Adaptive Card JSON file; nothing is posted automatically."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_define_notification_templates", "rar_sha256": "dd9e5622ab0e375f135d258c95696e1994937fbddf6428f6b9528bce6cbcd3ae", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
