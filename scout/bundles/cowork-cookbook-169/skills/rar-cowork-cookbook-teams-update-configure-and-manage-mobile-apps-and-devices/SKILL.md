---
name: "rar-cowork-cookbook-teams-update-configure-and-manage-mobile-apps-and-devices"
description: "Summarizes mobile app and device management status from Dynamics 365 F&SCM for a given legal entity and saves two draft artifacts: a markdown Teams channel post and an Adaptive Card JSON; nothing is posted."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_configure_and_manage_mobile_apps_and_devices", "rar_sha256": "e241095f1ceb64adbbbdf4b44746167c9c31570dda6e5557fa733a249be2a2e0", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_configure_and_manage_mobile_apps_and_devices`. The original RAPP
agent is preserved byte-for-byte in `teams_update_configure_and_manage_mobile_apps_and_devices_agent.py` and in the RCI capsule.

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

Configure and manage mobile apps and devices Teams Channel Update — Summarizes mobile app and device management status from Dynamics 365 F&SCM for a given legal entity and saves two draft artifacts: a markdown Teams channel post and an Adaptive Card JSON; nothing is posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-configure-and-manage-mobile-apps-and-devices
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
    "as_of_date": {
      "description": "Date used in the update and in the card filename.",
      "type": "string"
    },
    "card_filename": {
      "description": "Output filename for the Adaptive Card JSON artifact.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 F&SCM legal entity to report on (e.g. USMF).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_configure_and_manage_mobile_apps_and_devices_agent.py` and embedded as the fenced Python below (sha256 e241095f1ceb64ad…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_configure_and_manage_mobile_apps_and_devices_agent.py` first:

```bash
python3 teams_update_configure_and_manage_mobile_apps_and_devices_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_configure_and_manage_mobile_apps_and_devices_agent.py   # or on stdin
python3 teams_update_configure_and_manage_mobile_apps_and_devices_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and manage mobile apps and devices Teams Channel Update — Summarizes mobile app and device management status from Dynamics 365 F&SCM for a given legal entity and saves two draft artifacts: a markdown Teams channel post and an Adaptive Card JSON; nothing is posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-configure-and-manage-mobile-apps-and-devices
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_configure_and_manage_mobile_apps_and_devices',
    "version": '3.0.3',
    "display_name": 'Configure and manage mobile apps and devices Teams Channel Update',
    "description": 'Summarizes mobile app and device management status from Dynamics 365 F&SCM for a given legal entity and saves two draft artifacts: a markdown Teams channel post and an Adaptive Card JSON; nothing is posted.',
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
        "upstream_slug": 'teams-update-configure-and-manage-mobile-apps-and-devices',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-configure-and-manage-mobile-apps-and-devices',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c6a5d364b7d9ca5f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-manage-mobile-apps-and-devices'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/teams-update-configure-and-manage-mobile-apps-and-devices', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'as_of_date': 'Date used in the update and in the card filename.', 'card_filename': 'Output filename for the Adaptive Card JSON artifact.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 F&SCM legal entity to report on (e.g. USMF).', 'quick_actions': "Quick-action buttons to include on the card, e.g. 'View detail', 'Open in D365'."}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of configure and manage mobile apps and devices. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-configure-and-manage-mobile-apps-and-devices-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads configure and manage mobile apps and devices, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes mobile app and device management status from Dynamics 365 F&SCM for a given legal entity and saves two draft artifacts: a markdown Teams channel post and an Adaptive Card JSON; nothing is posted.', 'example_request': "Draft a Teams update on mobile app and device management for USMF as of 2026-05-24, with an Adaptive Card — don't post it.", 'inputs': [{'description': 'D365 F&SCM legal entity to report on (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Date used in the update and in the card filename.', 'name': 'as_of_date'}, {'description': 'Output filename for the Adaptive Card JSON artifact.', 'name': 'card_filename'}, {'description': "Quick-action buttons to include on the card, e.g. 'View detail', 'Open in D365'.", 'name': 'quick_actions'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a reviewable Teams channel update plus Adaptive Card on configure-and-manage-mobile-apps-and-devices status from D365 ERP data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateConfigureAndManageMobileAppsAndDevices(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateConfigureAndManageMobileAppsAndDevices'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'as_of_date': {'description': 'Date used in the update and in the card filename.', 'type': 'string'}, 'card_filename': {'description': 'Output filename for the Adaptive Card JSON artifact.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 F&SCM legal entity to report on (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'quick_actions': {'description': "Quick-action buttons to include on the card, e.g. 'View detail', 'Open in D365'.", 'type': 'string'}},
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
    print(TeamsUpdateConfigureAndManageMobileAppsAndDevices().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
