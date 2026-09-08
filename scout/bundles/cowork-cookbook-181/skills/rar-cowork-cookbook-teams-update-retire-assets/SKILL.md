---
name: "rar-cowork-cookbook-teams-update-retire-assets"
description: "Summarizes retire-assets status from the Dynamics 365 ERP plugin for a given legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_retire_assets", "rar_sha256": "805b85051bfb11e7bfd1015258429b94fd0061256eef013c2e1a8720addee368", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_retire_assets`. The original RAPP
agent is preserved byte-for-byte in `teams_update_retire_assets_agent.py` and in the RCI capsule.

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

Retire assets Teams Channel Update — Summarizes retire-assets status from the Dynamics 365 ERP plugin for a given legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-retire-assets
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
      "description": "Filename for the Adaptive Card JSON, e.g. teams-update-retire-assets-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_retire_assets_agent.py` and embedded as the fenced Python below (sha256 805b85051bfb11e7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_retire_assets_agent.py` first:

```bash
python3 teams_update_retire_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_retire_assets_agent.py   # or on stdin
python3 teams_update_retire_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Retire assets Teams Channel Update — Summarizes retire-assets status from the Dynamics 365 ERP plugin for a given legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-retire-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_retire_assets',
    "version": '3.0.3',
    "display_name": 'Retire assets Teams Channel Update',
    "description": 'Summarizes retire-assets status from the Dynamics 365 ERP plugin for a given legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'teams-update-retire-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-retire-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '348f0c661244a8ba',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/dispose-of-assets/retire-assets'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/teams-update-retire-assets', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Filename for the Adaptive Card JSON, e.g. teams-update-retire-assets-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to summarize, e.g. USMF.', 'quick_actions': "Quick-action buttons to include on the card, e.g. 'View detail', 'Open in D365'."}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of retire assets. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-retire-assets-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-06-01', 'what_it_does': 'Reads retire assets, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes retire-assets status from the Dynamics 365 ERP plugin for a given legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted.', 'example_request': "Draft a Teams post and Adaptive Card on retire assets status for legal entity USMF — save them, don't post.", 'inputs': [{'description': 'D365 legal entity to summarize, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Filename for the Adaptive Card JSON, e.g. teams-update-retire-assets-2026-05-24-card.json.', 'name': 'card_filename'}, {'description': "Quick-action buttons to include on the card, e.g. 'View detail', 'Open in D365'.", 'name': 'quick_actions'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need a review-ready Teams channel update on retire assets status in Dynamics 365 F&SCM, with an Adaptive Card artifact saved for manual posting.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateRetireAssets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateRetireAssets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Filename for the Adaptive Card JSON, e.g. teams-update-retire-assets-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to summarize, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'quick_actions': {'description': "Quick-action buttons to include on the card, e.g. 'View detail', 'Open in D365'.", 'type': 'string'}},
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
    print(TeamsUpdateRetireAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
