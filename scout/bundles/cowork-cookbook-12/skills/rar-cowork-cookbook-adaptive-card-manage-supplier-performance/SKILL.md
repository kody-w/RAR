---
name: "rar-cowork-cookbook-adaptive-card-manage-supplier-performance"
description: "Generates a read-only Adaptive Card JSON file showing supplier performance status from Dynamics 365 F&SCM (legal entity USMF), with header, 3-5 KPI tiles with trend arrows, a RAG row, and 2-3 action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_manage_supplier_performance", "rar_sha256": "239a13cc3fce9d7973fae27be2f437737ea193f6a9d811f0a43d92687744f9c2", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_manage_supplier_performance`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_manage_supplier_performance_agent.py` and in the RCI capsule.

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

Manage supplier performance Status Adaptive Card — Generates a read-only Adaptive Card JSON file showing supplier performance status from Dynamics 365 F&SCM (legal entity USMF), with header, 3-5 KPI tiles with trend arrows, a RAG row, and 2-3 action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-manage-supplier-performance
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
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to report on (recipe default: USMF).",
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-manage-supplier-performance-2026-05-24-card.json.",
      "type": "string"
    },
    "snapshot_date": {
      "description": "Date used for the card timestamp and filename.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_manage_supplier_performance_agent.py` and embedded as the fenced Python below (sha256 239a13cc3fce9d79…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_manage_supplier_performance_agent.py` first:

```bash
python3 adaptive_card_manage_supplier_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_manage_supplier_performance_agent.py   # or on stdin
python3 adaptive_card_manage_supplier_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage supplier performance Status Adaptive Card — Generates a read-only Adaptive Card JSON file showing supplier performance status from Dynamics 365 F&SCM (legal entity USMF), with header, 3-5 KPI tiles with trend arrows, a RAG row, and 2-3 action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-manage-supplier-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_manage_supplier_performance',
    "version": '3.0.2',
    "display_name": 'Manage supplier performance Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file showing supplier performance status from Dynamics 365 F&SCM (legal entity USMF), with header, 3-5 KPI tiles with trend arrows, a RAG row, and 2-3 action buttons.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'community',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'adaptive-card-manage-supplier-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-manage-supplier-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '812ef1ca7feba23f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/analyze-procurement-and-sourcing/manage-supplier-performance'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/adaptive-card-manage-supplier-performance', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on (recipe default: USMF).', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-manage-supplier-performance-2026-05-24-card.json.', 'snapshot_date': 'Date used for the card timestamp and filename.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical manage supplier performance status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-manage-supplier-performance-2026-05-24-card.json' that visualizes the current state of manage supplier performance. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current manage supplier performance KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file showing supplier performance status from Dynamics 365 F&SCM (legal entity USMF), with header, 3-5 KPI tiles with trend arrows, a RAG row, and 2-3 action buttons.', 'example_request': 'Make me an Adaptive Card showing current supplier performance status in USMF that I can drop into Teams.', 'inputs': [{'description': 'D365 legal entity to report on (recipe default: USMF).', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-manage-supplier-performance-2026-05-24-card.json.', 'name': 'output_filename'}, {'description': 'Date used for the card timestamp and filename.', 'name': 'snapshot_date'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable Adaptive Card snapshot of supplier performance for Teams, Outlook, or a dashboard. No data is modified.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardManageSupplierPerformance(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardManageSupplierPerformance'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on (recipe default: USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-manage-supplier-performance-2026-05-24-card.json.', 'type': 'string'}, 'snapshot_date': {'description': 'Date used for the card timestamp and filename.', 'type': 'string'}},
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
    print(AdaptiveCardManageSupplierPerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
