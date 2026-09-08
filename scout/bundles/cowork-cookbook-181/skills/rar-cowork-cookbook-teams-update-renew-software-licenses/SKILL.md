---
name: "rar-cowork-cookbook-teams-update-renew-software-licenses"
description: "Summarizes renew software licenses status from Dynamics 365 ERP for a legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_renew_software_licenses", "rar_sha256": "12bb09a37d5b202e6ce47b9d437b482ba32c23847d360a4bb60333f89142f19f", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_renew_software_licenses`. The original RAPP
agent is preserved byte-for-byte in `teams_update_renew_software_licenses_agent.py` and in the RCI capsule.

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

Renew software licenses Teams Channel Update — Summarizes renew software licenses status from Dynamics 365 ERP for a legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-renew-software-licenses
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
      "description": "Filename for the Adaptive Card JSON artifact, e.g. teams-update-renew-software-licenses-2026-05-24-card.json.",
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
    "topic": {
      "description": "Subject of the status update, e.g. renew software licenses.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_renew_software_licenses_agent.py` and embedded as the fenced Python below (sha256 12bb09a37d5b202e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_renew_software_licenses_agent.py` first:

```bash
python3 teams_update_renew_software_licenses_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_renew_software_licenses_agent.py   # or on stdin
python3 teams_update_renew_software_licenses_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Renew software licenses Teams Channel Update — Summarizes renew software licenses status from Dynamics 365 ERP for a legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-renew-software-licenses
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_renew_software_licenses',
    "version": '3.0.3',
    "display_name": 'Renew software licenses Teams Channel Update',
    "description": 'Summarizes renew software licenses status from Dynamics 365 ERP for a legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted.',
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
        "upstream_slug": 'teams-update-renew-software-licenses',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-renew-software-licenses',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6045e6878f955f73',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-licensing-and-entitlements/renew-software-licenses'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/teams-update-renew-software-licenses', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Filename for the Adaptive Card JSON artifact, e.g. teams-update-renew-software-licenses-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'topic': 'Subject of the status update, e.g. renew software licenses.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of renew software licenses. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-renew-software-licenses-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads renew software licenses, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes renew software licenses status from Dynamics 365 ERP for a legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted.', 'example_request': 'Draft a Teams update on renew software licenses from D365 USMF, with an Adaptive Card I can review before posting.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Subject of the status update, e.g. renew software licenses.', 'name': 'topic'}, {'description': 'Filename for the Adaptive Card JSON artifact, e.g. teams-update-renew-software-licenses-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a review-ready Teams channel update and Adaptive Card on renew software licenses status pulled from Dynamics 365 F&SCM.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateRenewSoftwareLicenses(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateRenewSoftwareLicenses'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Filename for the Adaptive Card JSON artifact, e.g. teams-update-renew-software-licenses-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'topic': {'description': 'Subject of the status update, e.g. renew software licenses.', 'type': 'string'}},
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
    print(TeamsUpdateRenewSoftwareLicenses().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
