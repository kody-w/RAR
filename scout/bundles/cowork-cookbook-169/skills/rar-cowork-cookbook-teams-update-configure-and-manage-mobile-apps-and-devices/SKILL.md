---
name: "rar-cowork-cookbook-teams-update-configure-and-manage-mobile-apps-and-devices"
description: "Summarizes mobile app and device management status from Dynamics 365 F&SCM for a given legal entity and saves two draft artifacts: a markdown Teams channel post and an Adaptive Card JSON; nothing is posted."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_configure_and_manage_mobile_apps_and_devices", "rar_sha256": "e241095f1ceb64adbbbdf4b44746167c9c31570dda6e5557fa733a249be2a2e0", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
