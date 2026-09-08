---
name: "rar-cowork-cookbook-teams-update-dispute-invoices"
description: "Summarizes the current state of dispute invoices from the Dynamics 365 ERP plugin for a given legal entity and returns a Teams channel post in markdown plus an Adaptive Card JSON file saved for review, never posted."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_dispute_invoices", "rar_sha256": "a6c0f0a4cbba5846d1ad8839148c6abd46aea545116d5247f19c70bbd48a01b7", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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
