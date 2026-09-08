---
name: "rar-cowork-cookbook-teams-update-make-payments-on-asset-leases"
description: "Summarizes the current state of make-payments-on-asset-leases from Dynamics 365 F&SCM (legal entity USMF) and returns a markdown Teams channel post plus a saved Adaptive Card JSON file; nothing is posted."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_make_payments_on_asset_leases", "rar_sha256": "3a5b5e7a8e0bb2959f974143441580b8c7ee306173713607d391f70afeb050b0", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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
