---
name: "rar-cowork-cookbook-teams-update-test-software-releases"
description: "Summarizes the current state of test software releases from the Dynamics 365 ERP plugin for a given legal entity, returning a markdown Teams channel post plus a saved Adaptive Card JSON file; nothing is posted."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_test_software_releases", "rar_sha256": "3e4769ea0d7ec32d0524d932ea93f816c3abf12198d853e76207f84b6b8b170f", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_test_software_releases`. The original RAPP
agent is preserved byte-for-byte in `teams_update_test_software_releases_agent.py` and in the RCI capsule.

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

Test software releases Teams Channel Update — Summarizes the current state of test software releases from the Dynamics 365 ERP plugin for a given legal entity, returning a markdown Teams channel post plus a saved Adaptive Card JSON file; nothing is posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-test-software-releases
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
      "description": "Filename for the saved Adaptive Card JSON, e.g. teams-update-test-software-releases-2026-05-24-card.json.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to query, e.g. USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_test_software_releases_agent.py` and embedded as the fenced Python below (sha256 3e4769ea0d7ec32d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_test_software_releases_agent.py` first:

```bash
python3 teams_update_test_software_releases_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_test_software_releases_agent.py   # or on stdin
python3 teams_update_test_software_releases_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Test software releases Teams Channel Update — Summarizes the current state of test software releases from the Dynamics 365 ERP plugin for a given legal entity, returning a markdown Teams channel post plus a saved Adaptive Card JSON file; nothing is posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-test-software-releases
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_test_software_releases',
    "version": '3.0.3',
    "display_name": 'Test software releases Teams Channel Update',
    "description": 'Summarizes the current state of test software releases from the Dynamics 365 ERP plugin for a given legal entity, returning a markdown Teams channel post plus a saved Adaptive Card JSON file; nothing is posted.',
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
        "upstream_slug": 'teams-update-test-software-releases',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-test-software-releases',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'fbbc2f30a9ea3039',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/uptake-software-releases/test-software-releases'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/teams-update-test-software-releases', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Filename for the saved Adaptive Card JSON, e.g. teams-update-test-software-releases-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'quick_actions': "Quick-action buttons to include on the card, e.g. 'View detail', 'Open in D365'."}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of test software releases. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-test-software-releases-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads test software releases, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes the current state of test software releases from the Dynamics 365 ERP plugin for a given legal entity, returning a markdown Teams channel post plus a saved Adaptive Card JSON file; nothing is posted.', 'example_request': "Draft a Teams update on test software releases from D365 USMF with an Adaptive Card — don't post it, just save it.", 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Filename for the saved Adaptive Card JSON, e.g. teams-update-test-software-releases-2026-05-24-card.json.', 'name': 'card_filename'}, {'description': "Quick-action buttons to include on the card, e.g. 'View detail', 'Open in D365'.", 'name': 'quick_actions'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a review-ready Teams channel update on test software release status from D365 F&SCM, with an Adaptive Card artifact saved for them.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateTestSoftwareReleases(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateTestSoftwareReleases'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Filename for the saved Adaptive Card JSON, e.g. teams-update-test-software-releases-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'quick_actions': {'description': "Quick-action buttons to include on the card, e.g. 'View detail', 'Open in D365'.", 'type': 'string'}},
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
    print(TeamsUpdateTestSoftwareReleases().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
