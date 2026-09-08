---
name: "rar-cowork-cookbook-teams-update-manage-organizational-structure"
description: "Summarizes the current state of manage organizational structure from Dynamics 365 F&SCM for a given legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON file; nothing is posted."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_manage_organizational_structure", "rar_sha256": "7467be3fe16d589acb5b8dc7dd1003cde0f8777ae3318e6cc2735de572697c39", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
