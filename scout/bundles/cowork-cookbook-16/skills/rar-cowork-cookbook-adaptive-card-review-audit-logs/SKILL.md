---
name: "rar-cowork-cookbook-adaptive-card-review-audit-logs"
description: "Generates a read-only Adaptive Card JSON file visualizing review audit logs status for a Dynamics 365 F&SCM legal entity, with header, KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_review_audit_logs", "rar_sha256": "98ffa496b6160a467ee4ac2dbc95af3a8932fa150f3d802b8789ba3ee84e7670", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
