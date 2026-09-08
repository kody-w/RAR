---
name: "rar-cowork-cookbook-teams-update-test-software-releases"
description: "Summarizes the current state of test software releases from the Dynamics 365 ERP plugin for a given legal entity, returning a markdown Teams channel post plus a saved Adaptive Card JSON file; nothing is posted."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_test_software_releases", "rar_sha256": "3e4769ea0d7ec32d0524d932ea93f816c3abf12198d853e76207f84b6b8b170f", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
