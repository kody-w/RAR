---
name: "rar-cowork-cookbook-teams-update-update-access-to-systems"
description: "Summarizes update-access-to-systems status from the Dynamics 365 ERP plugin for a given legal entity and returns a markdown Teams channel post plus an Adaptive Card JSON file saved for review, not posted."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_update_access_to_systems", "rar_sha256": "c0727a7f0481b89a8d8ae569e8a1ad6bcaa1cc9342f9ef587e321606de24a517", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_update_access_to_systems`. The original RAPP
agent is preserved byte-for-byte in `teams_update_update_access_to_systems_agent.py` and in the RCI capsule.

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

Update access to systems Teams Channel Update — Summarizes update-access-to-systems status from the Dynamics 365 ERP plugin for a given legal entity and returns a markdown Teams channel post plus an Adaptive Card JSON file saved for review, not posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-update-access-to-systems
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
      "description": "Filename for the Adaptive Card JSON, e.g. teams-update-update-access-to-systems-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_update_access_to_systems_agent.py` and embedded as the fenced Python below (sha256 c0727a7f0481b89a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_update_access_to_systems_agent.py` first:

```bash
python3 teams_update_update_access_to_systems_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_update_access_to_systems_agent.py   # or on stdin
python3 teams_update_update_access_to_systems_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Update access to systems Teams Channel Update — Summarizes update-access-to-systems status from the Dynamics 365 ERP plugin for a given legal entity and returns a markdown Teams channel post plus an Adaptive Card JSON file saved for review, not posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-update-access-to-systems
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_update_access_to_systems',
    "version": '3.0.3',
    "display_name": 'Update access to systems Teams Channel Update',
    "description": 'Summarizes update-access-to-systems status from the Dynamics 365 ERP plugin for a given legal entity and returns a markdown Teams channel post plus an Adaptive Card JSON file saved for review, not posted.',
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
        "upstream_slug": 'teams-update-update-access-to-systems',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-update-access-to-systems',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '52037b978e7a59a6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-access-and-security/update-access-to-systems'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/teams-update-update-access-to-systems', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Filename for the Adaptive Card JSON, e.g. teams-update-update-access-to-systems-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to summarize, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of update access to systems. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-update-access-to-systems-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads update access to systems, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes update-access-to-systems status from the Dynamics 365 ERP plugin for a given legal entity and returns a markdown Teams channel post plus an Adaptive Card JSON file saved for review, not posted.', 'example_request': "Draft a Teams post and Adaptive Card on update access to systems status for USMF from D365 — don't post it.", 'inputs': [{'description': 'D365 legal entity to summarize, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Filename for the Adaptive Card JSON, e.g. teams-update-update-access-to-systems-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a draft Teams channel update on update-access-to-systems status from D365 F&SCM, with an Adaptive Card for triage.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateUpdateAccessToSystems(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateUpdateAccessToSystems'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Filename for the Adaptive Card JSON, e.g. teams-update-update-access-to-systems-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to summarize, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateUpdateAccessToSystems().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
