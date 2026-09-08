---
name: "rar-cowork-cookbook-adaptive-card-perform-preventative-maintenance"
description: "Generates a read-only Adaptive Card JSON file visualizing preventative maintenance status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons. Call when you need a card snapsh"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_perform_preventative_maintenance", "rar_sha256": "519e228304406e104fef280d235a2d6238fe83f66af78a2a379ba3ffd2eb86c6", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_perform_preventative_maintenance`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_perform_preventative_maintenance_agent.py` and in the RCI capsule.

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

Perform preventative maintenance Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing preventative maintenance status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons. Call when you need a card snapsh

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-perform-preventative-maintenance
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
    },
    "output_filename": {
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-perform-preventative-maintenance-2026-05-24-card.json.",
      "type": "string"
    },
    "snapshot_date": {
      "description": "Date the status snapshot represents, used in the card timestamp and filename.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_perform_preventative_maintenance_agent.py` and embedded as the fenced Python below (sha256 519e228304406e10…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_perform_preventative_maintenance_agent.py` first:

```bash
python3 adaptive_card_perform_preventative_maintenance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_perform_preventative_maintenance_agent.py   # or on stdin
python3 adaptive_card_perform_preventative_maintenance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Perform preventative maintenance Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing preventative maintenance status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons. Call when you need a card snapsh

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-perform-preventative-maintenance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_perform_preventative_maintenance',
    "version": '3.0.2',
    "display_name": 'Perform preventative maintenance Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file visualizing preventative maintenance status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons. Call when you need a card snapsh',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-perform-preventative-maintenance',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-perform-preventative-maintenance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a9286f38beb9905f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/perform-asset-maintenance/perform-preventative-maintenance'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/adaptive-card-perform-preventative-maintenance', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-perform-preventative-maintenance-2026-05-24-card.json.', 'snapshot_date': 'Date the status snapshot represents, used in the card timestamp and filename.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical perform preventative maintenance status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-perform-preventative-maintenance-2026-05-24-card.json' that visualizes the current state of perform preventative maintenance. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Generates an Adaptive Card JSON file with current perform preventative maintenance KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file visualizing preventative maintenance status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons. Call when you need a card snapsh', 'example_request': 'Make me an Adaptive Card JSON of preventative maintenance status in USMF for 2026-05-24.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-perform-preventative-maintenance-2026-05-24-card.json.', 'name': 'output_filename'}, {'description': 'Date the status snapshot represents, used in the card timestamp and filename.', 'name': 'snapshot_date'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when a caller wants a Teams/Outlook-renderable Adaptive Card snapshot of preventative maintenance status pulled from D365 ERP, without modifying any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardPerformPreventativeMaintenance(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardPerformPreventativeMaintenance'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-perform-preventative-maintenance-2026-05-24-card.json.', 'type': 'string'}, 'snapshot_date': {'description': 'Date the status snapshot represents, used in the card timestamp and filename.', 'type': 'string'}},
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
    print(AdaptiveCardPerformPreventativeMaintenance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
