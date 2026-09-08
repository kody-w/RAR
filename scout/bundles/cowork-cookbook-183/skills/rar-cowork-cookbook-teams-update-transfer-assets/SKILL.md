---
name: "rar-cowork-cookbook-teams-update-transfer-assets"
description: "Summarizes transfer asset status from the Dynamics 365 ERP plugin for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; does not pos"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_transfer_assets", "rar_sha256": "4bc81aef5963a84d2d689f58545d6450c737431b3822a5b9352f9a4221c02bfd", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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
