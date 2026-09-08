---
name: "rar-cowork-cookbook-teams-update-correct-synchronous-integration-failures"
description: "Summarizes the current state of synchronous integration failures from Dynamics 365 F&SCM for a given legal entity and saves a Teams channel post (markdown) plus an Adaptive Card JSON for review; does not post anything."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_correct_synchronous_integration_failures", "rar_sha256": "022fe9796363150ae888799fe1a9cde19a9008572f48d3efd09f03323008e8ca", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
