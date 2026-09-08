---
name: "rar-cowork-cookbook-adaptive-card-perform-preventative-maintenance"
description: "Generates a read-only Adaptive Card JSON file visualizing preventative maintenance status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons. Call when you need a card snapsh"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_perform_preventative_maintenance", "rar_sha256": "519e228304406e104fef280d235a2d6238fe83f66af78a2a379ba3ffd2eb86c6", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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
