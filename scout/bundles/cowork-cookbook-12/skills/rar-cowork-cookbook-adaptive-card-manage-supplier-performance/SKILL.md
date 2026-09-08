---
name: "rar-cowork-cookbook-adaptive-card-manage-supplier-performance"
description: "Generates a read-only Adaptive Card JSON file showing supplier performance status from Dynamics 365 F&SCM (legal entity USMF), with header, 3-5 KPI tiles with trend arrows, a RAG row, and 2-3 action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_manage_supplier_performance", "rar_sha256": "239a13cc3fce9d7973fae27be2f437737ea193f6a9d811f0a43d92687744f9c2", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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
