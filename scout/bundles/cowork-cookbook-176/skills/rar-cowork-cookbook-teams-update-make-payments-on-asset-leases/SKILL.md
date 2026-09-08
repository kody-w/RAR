---
name: "rar-cowork-cookbook-teams-update-make-payments-on-asset-leases"
description: "Summarizes the current state of make-payments-on-asset-leases from Dynamics 365 F&SCM (legal entity USMF) and returns a markdown Teams channel post plus a saved Adaptive Card JSON file; nothing is posted."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_make_payments_on_asset_leases", "rar_sha256": "3a5b5e7a8e0bb2959f974143441580b8c7ee306173713607d391f70afeb050b0", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_make_payments_on_asset_leases`. The original RAPP
agent is preserved byte-for-byte in `teams_update_make_payments_on_asset_leases_agent.py` and in the RCI capsule.

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

Make payments on asset leases Teams Channel Update — Summarizes the current state of make-payments-on-asset-leases from Dynamics 365 F&SCM (legal entity USMF) and returns a markdown Teams channel post plus a saved Adaptive Card JSON file; nothing is posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-make-payments-on-asset-leases
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
      "description": "Output name for the Adaptive Card JSON, e.g. teams-update-make-payments-on-asset-leases-2026-05-24-card.json.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to query; the recipe uses USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_make_payments_on_asset_leases_agent.py` and embedded as the fenced Python below (sha256 3a5b5e7a8e0bb295…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_make_payments_on_asset_leases_agent.py` first:

```bash
python3 teams_update_make_payments_on_asset_leases_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_make_payments_on_asset_leases_agent.py   # or on stdin
python3 teams_update_make_payments_on_asset_leases_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Make payments on asset leases Teams Channel Update — Summarizes the current state of make-payments-on-asset-leases from Dynamics 365 F&SCM (legal entity USMF) and returns a markdown Teams channel post plus a saved Adaptive Card JSON file; nothing is posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-make-payments-on-asset-leases
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_make_payments_on_asset_leases',
    "version": '3.0.3',
    "display_name": 'Make payments on asset leases Teams Channel Update',
    "description": 'Summarizes the current state of make-payments-on-asset-leases from Dynamics 365 F&SCM (legal entity USMF) and returns a markdown Teams channel post plus a saved Adaptive Card JSON file; nothing is posted.',
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
        "upstream_slug": 'teams-update-make-payments-on-asset-leases',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-make-payments-on-asset-leases',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b265f01e0d001e02',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/manage-active-assets/make-payments-on-asset-leases'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/teams-update-make-payments-on-asset-leases', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Output name for the Adaptive Card JSON, e.g. teams-update-make-payments-on-asset-leases-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query; the recipe uses USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of make payments on asset leases. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-make-payments-on-asset-leases-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-06-01', 'what_it_does': 'Reads make payments on asset leases, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes the current state of make-payments-on-asset-leases from Dynamics 365 F&SCM (legal entity USMF) and returns a markdown Teams channel post plus a saved Adaptive Card JSON file; nothing is posted.', 'example_request': "Draft a Teams update on asset lease payments in USMF with an Adaptive Card — don't post it, just save it.", 'inputs': [{'description': 'D365 legal entity to query; the recipe uses USMF.', 'name': 'legal_entity'}, {'description': 'Output name for the Adaptive Card JSON, e.g. teams-update-make-payments-on-asset-leases-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a review-ready Teams channel update on asset lease payment status, with KPIs and quick-action buttons, saved as draft artifacts.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateMakePaymentsOnAssetLeases(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateMakePaymentsOnAssetLeases'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Output name for the Adaptive Card JSON, e.g. teams-update-make-payments-on-asset-leases-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query; the recipe uses USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateMakePaymentsOnAssetLeases().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
