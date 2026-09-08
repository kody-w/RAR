---
name: "rar-cowork-cookbook-teams-update-conduct-training"
description: "Summarizes conduct training status from Dynamics 365 ERP for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_conduct_training", "rar_sha256": "adde43dcbc43087f9ca1b19de5a11a52a5a59b97e673230e87b5adeb1b71b5f9", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_conduct_training`. The original RAPP
agent is preserved byte-for-byte in `teams_update_conduct_training_agent.py` and in the RCI capsule.

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

Conduct training Teams Channel Update — Summarizes conduct training status from Dynamics 365 ERP for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-conduct-training
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
      "description": "Filename for the saved Adaptive Card JSON, e.g. teams-update-conduct-training-2026-05-24-card.json.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to report on, e.g. USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_conduct_training_agent.py` and embedded as the fenced Python below (sha256 adde43dcbc43087f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_conduct_training_agent.py` first:

```bash
python3 teams_update_conduct_training_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_conduct_training_agent.py   # or on stdin
python3 teams_update_conduct_training_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Conduct training Teams Channel Update — Summarizes conduct training status from Dynamics 365 ERP for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-conduct-training
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_conduct_training',
    "version": '3.0.3',
    "display_name": 'Conduct training Teams Channel Update',
    "description": 'Summarizes conduct training status from Dynamics 365 ERP for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted.',
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
        "upstream_slug": 'teams-update-conduct-training',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-conduct-training',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6335e806faf195a5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/train-users-and-increase-adoption/conduct-training'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/teams-update-conduct-training', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Filename for the saved Adaptive Card JSON, e.g. teams-update-conduct-training-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of conduct training. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-conduct-training-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads conduct training, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes conduct training status from Dynamics 365 ERP for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted.', 'example_request': "Draft a Teams post and Adaptive Card on conduct training status for USMF — save them, don't post.", 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Filename for the saved Adaptive Card JSON, e.g. teams-update-conduct-training-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a review-ready Teams channel update on conduct training status from D365 F&SCM, with an Adaptive Card saved for them to check first.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateConductTraining(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateConductTraining'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Filename for the saved Adaptive Card JSON, e.g. teams-update-conduct-training-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateConductTraining().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
