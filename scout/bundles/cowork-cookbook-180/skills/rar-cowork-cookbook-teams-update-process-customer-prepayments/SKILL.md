---
name: "rar-cowork-cookbook-teams-update-process-customer-prepayments"
description: "Summarizes the current state of customer prepayments from Dynamics 365 F&SCM for a given legal entity and saves a draft Teams channel post plus an Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_process_customer_prepayments", "rar_sha256": "8265de005a08607e817b14a29f4d0744a1c563ed3d62d501d9182e9cc6408bcf", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_process_customer_prepayments`. The original RAPP
agent is preserved byte-for-byte in `teams_update_process_customer_prepayments_agent.py` and in the RCI capsule.

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

Process customer prepayments Teams Channel Update — Summarizes the current state of customer prepayments from Dynamics 365 F&SCM for a given legal entity and saves a draft Teams channel post plus an Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-process-customer-prepayments
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
    "as_of_date": {
      "description": "Date used for the status snapshot and the card filename.",
      "type": "string"
    },
    "card_filename": {
      "description": "Output filename for the Adaptive Card JSON artifact.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to report on (e.g., USMF).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_process_customer_prepayments_agent.py` and embedded as the fenced Python below (sha256 8265de005a08607e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_process_customer_prepayments_agent.py` first:

```bash
python3 teams_update_process_customer_prepayments_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_process_customer_prepayments_agent.py   # or on stdin
python3 teams_update_process_customer_prepayments_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Process customer prepayments Teams Channel Update — Summarizes the current state of customer prepayments from Dynamics 365 F&SCM for a given legal entity and saves a draft Teams channel post plus an Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-process-customer-prepayments
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_process_customer_prepayments',
    "version": '3.0.3',
    "display_name": 'Process customer prepayments Teams Channel Update',
    "description": 'Summarizes the current state of customer prepayments from Dynamics 365 F&SCM for a given legal entity and saves a draft Teams channel post plus an Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-process-customer-prepayments',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-process-customer-prepayments',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b94ad658e40eeccd',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-accounts-receivable/process-customer-prepayments'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/teams-update-process-customer-prepayments', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'as_of_date': 'Date used for the status snapshot and the card filename.', 'card_filename': 'Output filename for the Adaptive Card JSON artifact.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on (e.g., USMF).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of process customer prepayments. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-process-customer-prepayments-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads process customer prepayments, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes the current state of customer prepayments from Dynamics 365 F&SCM for a given legal entity and saves a draft Teams channel post plus an Adaptive Card JSON with KPIs and quick-action buttons; nothing is posted.', 'example_request': "Draft a Teams update on process customer prepayments for USMF as of 2026-05-24, with an Adaptive Card — don't post it.", 'inputs': [{'description': 'D365 legal entity to report on (e.g., USMF).', 'name': 'legal_entity'}, {'description': 'Date used for the status snapshot and the card filename.', 'name': 'as_of_date'}, {'description': 'Output filename for the Adaptive Card JSON artifact.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a reviewable Teams channel update on process customer prepayments status, with an Adaptive Card for triage, without auto-posting.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateProcessCustomerPrepayments(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateProcessCustomerPrepayments'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'as_of_date': {'description': 'Date used for the status snapshot and the card filename.', 'type': 'string'}, 'card_filename': {'description': 'Output filename for the Adaptive Card JSON artifact.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on (e.g., USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateProcessCustomerPrepayments().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
