---
name: "rar-cowork-cookbook-teams-update-correct-data-synchronization-failures"
description: "Summarizes the current state of data synchronization failures from the Dynamics 365 ERP plugin for a given legal entity and saves two draft artifacts: a markdown Teams channel post and an Adaptive Card JSON; nothing is p"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_correct_data_synchronization_failures", "rar_sha256": "26f1cce504fcf609b2fed303074fd64a4aef3e8869f231380fe63f99422cf405", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_correct_data_synchronization_failures`. The original RAPP
agent is preserved byte-for-byte in `teams_update_correct_data_synchronization_failures_agent.py` and in the RCI capsule.

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

Correct data synchronization failures Teams Channel Update — Summarizes the current state of data synchronization failures from the Dynamics 365 ERP plugin for a given legal entity and saves two draft artifacts: a markdown Teams channel post and an Adaptive Card JSON; nothing is p

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-correct-data-synchronization-failures
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
      "description": "Output filename for the Adaptive Card JSON, e.g. teams-update-correct-data-synchronization-failures-2026-05-24-card.json.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to scope the summary to, e.g. USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_correct_data_synchronization_failures_agent.py` and embedded as the fenced Python below (sha256 26f1cce504fcf609…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_correct_data_synchronization_failures_agent.py` first:

```bash
python3 teams_update_correct_data_synchronization_failures_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_correct_data_synchronization_failures_agent.py   # or on stdin
python3 teams_update_correct_data_synchronization_failures_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Correct data synchronization failures Teams Channel Update — Summarizes the current state of data synchronization failures from the Dynamics 365 ERP plugin for a given legal entity and saves two draft artifacts: a markdown Teams channel post and an Adaptive Card JSON; nothing is p

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-correct-data-synchronization-failures
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_correct_data_synchronization_failures',
    "version": '3.0.3',
    "display_name": 'Correct data synchronization failures Teams Channel Update',
    "description": 'Summarizes the current state of data synchronization failures from the Dynamics 365 ERP plugin for a given legal entity and saves two draft artifacts: a markdown Teams channel post and an Adaptive Card JSON; nothing is p',
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
        "upstream_slug": 'teams-update-correct-data-synchronization-failures',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-correct-data-synchronization-failures',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3ff1cf8838267a5b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-data/correct-data-synchronization-failures'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/teams-update-correct-data-synchronization-failures', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Output filename for the Adaptive Card JSON, e.g. teams-update-correct-data-synchronization-failures-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to scope the summary to, e.g. USMF.', 'quick_actions': "Quick-action buttons to include on the card, e.g. 'View detail', 'Open in D365'."}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of correct data synchronization failures. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-correct-data-synchronization-failures-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads correct data synchronization failures, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes the current state of data synchronization failures from the Dynamics 365 ERP plugin for a given legal entity and saves two draft artifacts: a markdown Teams channel post and an Adaptive Card JSON; nothing is p', 'example_request': "Draft a Teams update on data sync failures in USMF with an Adaptive Card — don't post it, just save the files.", 'inputs': [{'description': 'D365 legal entity to scope the summary to, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-correct-data-synchronization-failures-2026-05-24-card.json.', 'name': 'card_filename'}, {'description': "Quick-action buttons to include on the card, e.g. 'View detail', 'Open in D365'.", 'name': 'quick_actions'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a review-ready Teams channel update plus Adaptive Card on D365 data sync failure status, without auto-posting it.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateCorrectDataSynchronizationFailures(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateCorrectDataSynchronizationFailures'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-correct-data-synchronization-failures-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to scope the summary to, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'quick_actions': {'description': "Quick-action buttons to include on the card, e.g. 'View detail', 'Open in D365'.", 'type': 'string'}},
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
    print(TeamsUpdateCorrectDataSynchronizationFailures().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
