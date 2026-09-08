---
name: "rar-cowork-cookbook-teams-update-dispute-invoices"
description: "Summarizes the current state of dispute invoices from the Dynamics 365 ERP plugin for a given legal entity and returns a Teams channel post in markdown plus an Adaptive Card JSON file saved for review, never posted."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_dispute_invoices", "rar_sha256": "a6c0f0a4cbba5846d1ad8839148c6abd46aea545116d5247f19c70bbd48a01b7", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_dispute_invoices`. The original RAPP
agent is preserved byte-for-byte in `teams_update_dispute_invoices_agent.py` and in the RCI capsule.

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

Dispute invoices Teams Channel Update — Summarizes the current state of dispute invoices from the Dynamics 365 ERP plugin for a given legal entity and returns a Teams channel post in markdown plus an Adaptive Card JSON file saved for review, never posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-dispute-invoices
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
      "description": "Filename for the generated Adaptive Card JSON, e.g. teams-update-dispute-invoices-2026-05-24-card.json.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 F&SCM legal entity to query, e.g. USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_dispute_invoices_agent.py` and embedded as the fenced Python below (sha256 a6c0f0a4cbba5846…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_dispute_invoices_agent.py` first:

```bash
python3 teams_update_dispute_invoices_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_dispute_invoices_agent.py   # or on stdin
python3 teams_update_dispute_invoices_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Dispute invoices Teams Channel Update — Summarizes the current state of dispute invoices from the Dynamics 365 ERP plugin for a given legal entity and returns a Teams channel post in markdown plus an Adaptive Card JSON file saved for review, never posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-dispute-invoices
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_dispute_invoices',
    "version": '3.0.3',
    "display_name": 'Dispute invoices Teams Channel Update',
    "description": 'Summarizes the current state of dispute invoices from the Dynamics 365 ERP plugin for a given legal entity and returns a Teams channel post in markdown plus an Adaptive Card JSON file saved for review, never posted.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-dispute-invoices',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-dispute-invoices',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5d82f1843ff5615e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-accounts-payable/dispute-invoices'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/teams-update-dispute-invoices', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Filename for the generated Adaptive Card JSON, e.g. teams-update-dispute-invoices-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 F&SCM legal entity to query, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of dispute invoices. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-dispute-invoices-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads dispute invoices, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes the current state of dispute invoices from the Dynamics 365 ERP plugin for a given legal entity and returns a Teams channel post in markdown plus an Adaptive Card JSON file saved for review, never posted.', 'example_request': "Draft a Teams post and Adaptive Card on dispute invoices in USMF — save them, don't post.", 'inputs': [{'description': 'Dynamics 365 F&SCM legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Filename for the generated Adaptive Card JSON, e.g. teams-update-dispute-invoices-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a draft Teams update on dispute invoice status with an interactive Adaptive Card for triage, saved as artifacts rather than posted.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateDisputeInvoices(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateDisputeInvoices'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Filename for the generated Adaptive Card JSON, e.g. teams-update-dispute-invoices-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 F&SCM legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateDisputeInvoices().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
