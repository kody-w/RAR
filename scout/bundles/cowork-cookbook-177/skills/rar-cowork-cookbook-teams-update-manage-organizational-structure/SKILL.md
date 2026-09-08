---
name: "rar-cowork-cookbook-teams-update-manage-organizational-structure"
description: "Summarizes the current state of manage organizational structure from Dynamics 365 F&SCM for a given legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON file; nothing is posted."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_manage_organizational_structure", "rar_sha256": "7467be3fe16d589acb5b8dc7dd1003cde0f8777ae3318e6cc2735de572697c39", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_manage_organizational_structure`. The original RAPP
agent is preserved byte-for-byte in `teams_update_manage_organizational_structure_agent.py` and in the RCI capsule.

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

Manage organizational structure Teams Channel Update — Summarizes the current state of manage organizational structure from Dynamics 365 F&SCM for a given legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON file; nothing is posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-manage-organizational-structure
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
      "description": "Filename for the Adaptive Card JSON artifact, e.g. teams-update-manage-organizational-structure-2026-05-24-card.json.",
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
    "scope_notes": {
      "description": "Optional adjustments to the scope or emphasis of the summary and highlights.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_manage_organizational_structure_agent.py` and embedded as the fenced Python below (sha256 7467be3fe16d589a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_manage_organizational_structure_agent.py` first:

```bash
python3 teams_update_manage_organizational_structure_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_manage_organizational_structure_agent.py   # or on stdin
python3 teams_update_manage_organizational_structure_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage organizational structure Teams Channel Update — Summarizes the current state of manage organizational structure from Dynamics 365 F&SCM for a given legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON file; nothing is posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-manage-organizational-structure
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_manage_organizational_structure',
    "version": '3.0.3',
    "display_name": 'Manage organizational structure Teams Channel Update',
    "description": 'Summarizes the current state of manage organizational structure from Dynamics 365 F&SCM for a given legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON file; nothing is posted.',
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
        "upstream_slug": 'teams-update-manage-organizational-structure',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-manage-organizational-structure',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8babd80176f36718',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/manage-organizational-structure'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/teams-update-manage-organizational-structure', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Filename for the Adaptive Card JSON artifact, e.g. teams-update-manage-organizational-structure-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to summarize, e.g. USMF.', 'scope_notes': 'Optional adjustments to the scope or emphasis of the summary and highlights.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of manage organizational structure. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-manage-organizational-structure-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads manage organizational structure, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes the current state of manage organizational structure from Dynamics 365 F&SCM for a given legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON file; nothing is posted.', 'example_request': "Draft a Teams update on org structure status for USMF with an Adaptive Card — don't post it.", 'inputs': [{'description': 'D365 legal entity to summarize, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Filename for the Adaptive Card JSON artifact, e.g. teams-update-manage-organizational-structure-2026-05-24-card.json.', 'name': 'card_filename'}, {'description': 'Optional adjustments to the scope or emphasis of the summary and highlights.', 'name': 'scope_notes'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a review-ready Teams channel update and Adaptive Card on organizational structure status from D365 ERP data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateManageOrganizationalStructure(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateManageOrganizationalStructure'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Filename for the Adaptive Card JSON artifact, e.g. teams-update-manage-organizational-structure-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to summarize, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'scope_notes': {'description': 'Optional adjustments to the scope or emphasis of the summary and highlights.', 'type': 'string'}},
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
    print(TeamsUpdateManageOrganizationalStructure().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
