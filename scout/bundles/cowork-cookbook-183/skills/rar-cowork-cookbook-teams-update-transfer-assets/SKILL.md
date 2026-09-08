---
name: "rar-cowork-cookbook-teams-update-transfer-assets"
description: "Summarizes transfer asset status from the Dynamics 365 ERP plugin for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; does not pos"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_transfer_assets", "rar_sha256": "4bc81aef5963a84d2d689f58545d6450c737431b3822a5b9352f9a4221c02bfd", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_transfer_assets`. The original RAPP
agent is preserved byte-for-byte in `teams_update_transfer_assets_agent.py` and in the RCI capsule.

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

Transfer assets Teams Channel Update — Summarizes transfer asset status from the Dynamics 365 ERP plugin for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; does not pos

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-transfer-assets
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
      "description": "Output filename for the Adaptive Card JSON, e.g. teams-update-transfer-assets-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_transfer_assets_agent.py` and embedded as the fenced Python below (sha256 4bc81aef5963a84d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_transfer_assets_agent.py` first:

```bash
python3 teams_update_transfer_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_transfer_assets_agent.py   # or on stdin
python3 teams_update_transfer_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Transfer assets Teams Channel Update — Summarizes transfer asset status from the Dynamics 365 ERP plugin for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; does not pos

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-transfer-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_transfer_assets',
    "version": '3.0.3',
    "display_name": 'Transfer assets Teams Channel Update',
    "description": 'Summarizes transfer asset status from the Dynamics 365 ERP plugin for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; does not pos',
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
        "upstream_slug": 'teams-update-transfer-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-transfer-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2a044444add64106',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/manage-active-assets/transfer-assets'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/teams-update-transfer-assets', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Output filename for the Adaptive Card JSON, e.g. teams-update-transfer-assets-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of transfer assets. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-transfer-assets-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-06-01', 'what_it_does': 'Reads transfer assets, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes transfer asset status from the Dynamics 365 ERP plugin for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; does not pos', 'example_request': "Draft a Teams update on transfer assets for USMF with an Adaptive Card — save it, don't post.", 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-transfer-assets-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a reviewable Teams channel update on transfer assets status from D365 F&SCM, with an Adaptive Card for triage, saved rather than posted.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateTransferAssets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateTransferAssets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-transfer-assets-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateTransferAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
