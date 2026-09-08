---
name: "rar-cowork-cookbook-teams-update-configure-and-manage-microsoft-teams-integrations"
description: "Drafts a Teams channel post (markdown summary plus 3 bullets) and a saved Adaptive Card JSON with KPIs, status indicators, and quick-action buttons on Teams integration status, using the D365 ERP plugin for a legal entit"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_configure_and_manage_microsoft_teams_integrations", "rar_sha256": "e2e5dc5f82fd832f1385e05c43c5e66cea5460b9e7083daa3880e9e99c644f18", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_configure_and_manage_microsoft_teams_integrations`. The original RAPP
agent is preserved byte-for-byte in `teams_update_configure_and_manage_microsoft_teams_integrations_agent.py` and in the RCI capsule.

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

Configure and manage Microsoft Teams integrations Teams Channel Update — Drafts a Teams channel post (markdown summary plus 3 bullets) and a saved Adaptive Card JSON with KPIs, status indicators, and quick-action buttons on Teams integration status, using the D365 ERP plugin for a legal entit

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-configure-and-manage-microsoft-teams-integrations
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
      "description": "Filename for the Adaptive Card JSON artifact, including date.",
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
      "description": "Buttons to include on the card, e.g. 'View detail', 'Open in D365'.",
      "type": "string"
    },
    "topic": {
      "description": "Subject of the update, e.g. configure and manage Microsoft Teams integrations.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_configure_and_manage_microsoft_teams_integrations_agent.py` and embedded as the fenced Python below (sha256 e2e5dc5f82fd832f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_configure_and_manage_microsoft_teams_integrations_agent.py` first:

```bash
python3 teams_update_configure_and_manage_microsoft_teams_integrations_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_configure_and_manage_microsoft_teams_integrations_agent.py   # or on stdin
python3 teams_update_configure_and_manage_microsoft_teams_integrations_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and manage Microsoft Teams integrations Teams Channel Update — Drafts a Teams channel post (markdown summary plus 3 bullets) and a saved Adaptive Card JSON with KPIs, status indicators, and quick-action buttons on Teams integration status, using the D365 ERP plugin for a legal entit

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-configure-and-manage-microsoft-teams-integrations
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_configure_and_manage_microsoft_teams_integrations',
    "version": '3.0.3',
    "display_name": 'Configure and manage Microsoft Teams integrations Teams Channel Update',
    "description": 'Drafts a Teams channel post (markdown summary plus 3 bullets) and a saved Adaptive Card JSON with KPIs, status indicators, and quick-action buttons on Teams integration status, using the D365 ERP plugin for a legal entit',
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
        "upstream_slug": 'teams-update-configure-and-manage-microsoft-teams-integrations',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-configure-and-manage-microsoft-teams-integrations',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '53e3fcb6294cb5c5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-manage-microsoft-teams-integrations'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/teams-update-configure-and-manage-microsoft-teams-integrations', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Filename for the Adaptive Card JSON artifact, including date.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to summarize, e.g. USMF.', 'quick_actions': "Buttons to include on the card, e.g. 'View detail', 'Open in D365'.", 'topic': 'Subject of the update, e.g. configure and manage Microsoft Teams integrations.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of configure and manage Microsoft Teams integrations. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-configure-and-manage-microsoft-teams-integrations-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads configure and manage Microsoft Teams integrations, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Drafts a Teams channel post (markdown summary plus 3 bullets) and a saved Adaptive Card JSON with KPIs, status indicators, and quick-action buttons on Teams integration status, using the D365 ERP plugin for a legal entit', 'example_request': "Draft a Teams channel post and Adaptive Card on Teams integration status for USMF from D365 — save them, don't post.", 'inputs': [{'description': 'D365 legal entity to summarize, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Subject of the update, e.g. configure and manage Microsoft Teams integrations.', 'name': 'topic'}, {'description': 'Filename for the Adaptive Card JSON artifact, including date.', 'name': 'card_filename'}, {'description': "Buttons to include on the card, e.g. 'View detail', 'Open in D365'.", 'name': 'quick_actions'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a review-ready Teams channel update and Adaptive Card about Microsoft Teams integration status sourced from Dynamics 365 F&SCM.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateConfigureAndManageMicrosoftTeamsIntegrations(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateConfigureAndManageMicrosoftTeamsIntegrations'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Filename for the Adaptive Card JSON artifact, including date.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to summarize, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'quick_actions': {'description': "Buttons to include on the card, e.g. 'View detail', 'Open in D365'.", 'type': 'string'}, 'topic': {'description': 'Subject of the update, e.g. configure and manage Microsoft Teams integrations.', 'type': 'string'}},
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
    print(TeamsUpdateConfigureAndManageMicrosoftTeamsIntegrations().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
