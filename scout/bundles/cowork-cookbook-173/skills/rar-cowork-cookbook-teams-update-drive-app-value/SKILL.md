---
name: "rar-cowork-cookbook-teams-update-drive-app-value"
description: "Drafts a Teams channel post (markdown summary plus 3 bullets) and an Adaptive Card JSON with KPIs, status indicators and quick-action buttons on drive app value status from Dynamics 365 ERP data; saves files without post"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_drive_app_value", "rar_sha256": "04b90dd712c0555198997ce2c1ee8c0bdfb008a27b4edba3da60bc4e3a9ac888", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_drive_app_value`. The original RAPP
agent is preserved byte-for-byte in `teams_update_drive_app_value_agent.py` and in the RCI capsule.

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

Drive app value Teams Channel Update — Drafts a Teams channel post (markdown summary plus 3 bullets) and an Adaptive Card JSON with KPIs, status indicators and quick-action buttons on drive app value status from Dynamics 365 ERP data; saves files without post

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-drive-app-value
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
      "description": "Output filename for the Adaptive Card JSON, e.g. teams-update-drive-app-value-2026-05-24-card.json.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity to summarize, e.g. USMF.",
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
    "topic": {
      "description": "The initiative or area to report on, e.g. drive app value.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_drive_app_value_agent.py` and embedded as the fenced Python below (sha256 04b90dd712c05551…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_drive_app_value_agent.py` first:

```bash
python3 teams_update_drive_app_value_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_drive_app_value_agent.py   # or on stdin
python3 teams_update_drive_app_value_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Drive app value Teams Channel Update — Drafts a Teams channel post (markdown summary plus 3 bullets) and an Adaptive Card JSON with KPIs, status indicators and quick-action buttons on drive app value status from Dynamics 365 ERP data; saves files without post

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-drive-app-value
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_drive_app_value',
    "version": '3.0.3',
    "display_name": 'Drive app value Teams Channel Update',
    "description": 'Drafts a Teams channel post (markdown summary plus 3 bullets) and an Adaptive Card JSON with KPIs, status indicators and quick-action buttons on drive app value status from Dynamics 365 ERP data; saves files without post',
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
        "upstream_slug": 'teams-update-drive-app-value',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-drive-app-value',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e010a6edbeda491f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/drive-app-value'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/teams-update-drive-app-value', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Output filename for the Adaptive Card JSON, e.g. teams-update-drive-app-value-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to summarize, e.g. USMF.', 'topic': 'The initiative or area to report on, e.g. drive app value.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of drive app value. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-drive-app-value-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads drive app value, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Drafts a Teams channel post (markdown summary plus 3 bullets) and an Adaptive Card JSON with KPIs, status indicators and quick-action buttons on drive app value status from Dynamics 365 ERP data; saves files without post', 'example_request': "Draft a Teams channel update and Adaptive Card on drive app value status from D365 USMF — save them, don't post.", 'inputs': [{'description': 'Dynamics 365 legal entity to summarize, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'The initiative or area to report on, e.g. drive app value.', 'name': 'topic'}, {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-drive-app-value-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a review-ready Teams channel update and Adaptive Card on drive app value status pulled from Dynamics 365 F&SCM.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateDriveAppValue(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateDriveAppValue'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-drive-app-value-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to summarize, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'topic': {'description': 'The initiative or area to report on, e.g. drive app value.', 'type': 'string'}},
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
    print(TeamsUpdateDriveAppValue().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
