---
name: "rar-cowork-cookbook-teams-update-correct-synchronous-integration-failures"
description: "Summarizes the current state of synchronous integration failures from Dynamics 365 F&SCM for a given legal entity and saves a Teams channel post (markdown) plus an Adaptive Card JSON for review; does not post anything."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_correct_synchronous_integration_failures", "rar_sha256": "022fe9796363150ae888799fe1a9cde19a9008572f48d3efd09f03323008e8ca", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_correct_synchronous_integration_failures`. The original RAPP
agent is preserved byte-for-byte in `teams_update_correct_synchronous_integration_failures_agent.py` and in the RCI capsule.

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

Correct synchronous integration failures Teams Channel Update — Summarizes the current state of synchronous integration failures from Dynamics 365 F&SCM for a given legal entity and saves a Teams channel post (markdown) plus an Adaptive Card JSON for review; does not post anything.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-correct-synchronous-integration-failures
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
      "description": "Date the status snapshot represents, used in the card filename and post.",
      "type": "string"
    },
    "card_filename": {
      "description": "Filename for the saved Adaptive Card JSON, e.g. teams-update-correct-synchronous-integration-failures-2026-05-24-card.json.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 F&SCM legal entity to scope the summary, e.g. USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_correct_synchronous_integration_failures_agent.py` and embedded as the fenced Python below (sha256 022fe9796363150a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_correct_synchronous_integration_failures_agent.py` first:

```bash
python3 teams_update_correct_synchronous_integration_failures_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_correct_synchronous_integration_failures_agent.py   # or on stdin
python3 teams_update_correct_synchronous_integration_failures_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Correct synchronous integration failures Teams Channel Update — Summarizes the current state of synchronous integration failures from Dynamics 365 F&SCM for a given legal entity and saves a Teams channel post (markdown) plus an Adaptive Card JSON for review; does not post anything.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-correct-synchronous-integration-failures
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_correct_synchronous_integration_failures',
    "version": '3.0.3',
    "display_name": 'Correct synchronous integration failures Teams Channel Update',
    "description": 'Summarizes the current state of synchronous integration failures from Dynamics 365 F&SCM for a given legal entity and saves a Teams channel post (markdown) plus an Adaptive Card JSON for review; does not post anything.',
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
        "upstream_slug": 'teams-update-correct-synchronous-integration-failures',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-correct-synchronous-integration-failures',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a33014bca7e36e82',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/monitor-systems-environments-and-capacity/correct-synchronous-integration-failures'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/teams-update-correct-synchronous-integration-failures', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'as_of_date': 'Date the status snapshot represents, used in the card filename and post.', 'card_filename': 'Filename for the saved Adaptive Card JSON, e.g. teams-update-correct-synchronous-integration-failures-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 F&SCM legal entity to scope the summary, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of correct synchronous integration failures. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-correct-synchronous-integration-failures-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads correct synchronous integration failures, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes the current state of synchronous integration failures from Dynamics 365 F&SCM for a given legal entity and saves a Teams channel post (markdown) plus an Adaptive Card JSON for review; does not post anything.', 'example_request': 'Draft a Teams update on synchronous integration failures in USMF and save the Adaptive Card for me to review.', 'inputs': [{'description': 'D365 F&SCM legal entity to scope the summary, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Filename for the saved Adaptive Card JSON, e.g. teams-update-correct-synchronous-integration-failures-2026-05-24-card.json.', 'name': 'card_filename'}, {'description': 'Date the status snapshot represents, used in the card filename and post.', 'name': 'as_of_date'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a ready-to-review Teams update and Adaptive Card on D365 synchronous integration failure status for triage.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateCorrectSynchronousIntegrationFailures(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateCorrectSynchronousIntegrationFailures'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'as_of_date': {'description': 'Date the status snapshot represents, used in the card filename and post.', 'type': 'string'}, 'card_filename': {'description': 'Filename for the saved Adaptive Card JSON, e.g. teams-update-correct-synchronous-integration-failures-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 F&SCM legal entity to scope the summary, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateCorrectSynchronousIntegrationFailures().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
