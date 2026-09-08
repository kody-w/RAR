---
name: "rar-cowork-cookbook-teams-update-conduct-training"
description: "Summarizes conduct training status from Dynamics 365 ERP for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_conduct_training", "rar_sha256": "adde43dcbc43087f9ca1b19de5a11a52a5a59b97e673230e87b5adeb1b71b5f9", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
