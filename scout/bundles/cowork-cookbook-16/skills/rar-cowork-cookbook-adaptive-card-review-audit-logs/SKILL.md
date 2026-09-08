---
name: "rar-cowork-cookbook-adaptive-card-review-audit-logs"
description: "Generates a read-only Adaptive Card JSON file visualizing review audit logs status for a Dynamics 365 F&SCM legal entity, with header, KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_review_audit_logs", "rar_sha256": "98ffa496b6160a467ee4ac2dbc95af3a8932fa150f3d802b8789ba3ee84e7670", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_review_audit_logs`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_review_audit_logs_agent.py` and in the RCI capsule.

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

Review audit logs Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing review audit logs status for a Dynamics 365 F&SCM legal entity, with header, KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-review-audit-logs
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
      "description": "Snapshot date used in the card timestamp and output filename.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 F&SCM legal entity to report on, e.g. USMF.",
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
    "output_filename": {
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-review-audit-logs-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_review_audit_logs_agent.py` and embedded as the fenced Python below (sha256 98ffa496b6160a46…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_review_audit_logs_agent.py` first:

```bash
python3 adaptive_card_review_audit_logs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_review_audit_logs_agent.py   # or on stdin
python3 adaptive_card_review_audit_logs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Review audit logs Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing review audit logs status for a Dynamics 365 F&SCM legal entity, with header, KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-review-audit-logs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_review_audit_logs',
    "version": '3.0.2',
    "display_name": 'Review audit logs Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file visualizing review audit logs status for a Dynamics 365 F&SCM legal entity, with header, KPI tiles, RAG row, and action buttons.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-review-audit-logs',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-review-audit-logs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0a5b6000b5778da1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-access-and-security/review-audit-logs'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/adaptive-card-review-audit-logs', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'as_of_date': 'Snapshot date used in the card timestamp and output filename.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 F&SCM legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-review-audit-logs-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical review audit logs status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-review-audit-logs-2026-05-24-card.json' that visualizes the current state of review audit logs. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-06-01', 'what_it_does': 'Generates an Adaptive Card JSON file with current review audit logs KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file visualizing review audit logs status for a Dynamics 365 F&SCM legal entity, with header, KPI tiles, RAG row, and action buttons.', 'example_request': 'Make me an Adaptive Card showing review audit logs status for USMF as of 2026-05-24.', 'inputs': [{'description': 'D365 F&SCM legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Snapshot date used in the card timestamp and output filename.', 'name': 'as_of_date'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-review-audit-logs-2026-05-24-card.json.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable Adaptive Card snapshot of D365 review audit logs status for Teams, Outlook, or a dashboard, without changing data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardReviewAuditLogs(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardReviewAuditLogs'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'as_of_date': {'description': 'Snapshot date used in the card timestamp and output filename.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 F&SCM legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-review-audit-logs-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardReviewAuditLogs().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
