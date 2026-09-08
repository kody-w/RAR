---
name: "rar-cowork-cookbook-teams-update-correct-data-synchronization-failures"
description: "Summarizes the current state of data synchronization failures from the Dynamics 365 ERP plugin for a given legal entity and saves two draft artifacts: a markdown Teams channel post and an Adaptive Card JSON; nothing is p"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_correct_data_synchronization_failures", "rar_sha256": "26f1cce504fcf609b2fed303074fd64a4aef3e8869f231380fe63f99422cf405", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
