---
name: "rar-cowork-cookbook-adaptive-card-monitor-storage-capacity"
description: "Generates a read-only Adaptive Card JSON file visualizing monitor storage capacity status for a Dynamics 365 F&SCM legal entity, with header, KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_monitor_storage_capacity", "rar_sha256": "64130eb9d42ac37480cbf130f97f346cd6a176fa8fe56ad9883525ea753ec5f2", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_monitor_storage_capacity`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_monitor_storage_capacity_agent.py` and in the RCI capsule.

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

Monitor storage capacity Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing monitor storage capacity status for a Dynamics 365 F&SCM legal entity, with header, KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-monitor-storage-capacity
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
      "description": "Date used for the card timestamp and filename.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to report against, e.g. USMF.",
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-monitor-storage-capacity-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_monitor_storage_capacity_agent.py` and embedded as the fenced Python below (sha256 64130eb9d42ac374…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_monitor_storage_capacity_agent.py` first:

```bash
python3 adaptive_card_monitor_storage_capacity_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_monitor_storage_capacity_agent.py   # or on stdin
python3 adaptive_card_monitor_storage_capacity_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor storage capacity Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing monitor storage capacity status for a Dynamics 365 F&SCM legal entity, with header, KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-monitor-storage-capacity
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_monitor_storage_capacity',
    "version": '3.0.2',
    "display_name": 'Monitor storage capacity Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file visualizing monitor storage capacity status for a Dynamics 365 F&SCM legal entity, with header, KPI tiles, RAG row, and action buttons.',
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
        "upstream_slug": 'adaptive-card-monitor-storage-capacity',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-monitor-storage-capacity',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '111af8474417496c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/monitor-systems-environments-and-capacity/monitor-storage-capacity'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/adaptive-card-monitor-storage-capacity', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'as_of_date': 'Date used for the card timestamp and filename.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report against, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-monitor-storage-capacity-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical monitor storage capacity status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-monitor-storage-capacity-2026-05-24-card.json' that visualizes the current state of monitor storage capacity. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-06-01', 'what_it_does': 'Generates an Adaptive Card JSON file with current monitor storage capacity KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file visualizing monitor storage capacity status for a Dynamics 365 F&SCM legal entity, with header, KPI tiles, RAG row, and action buttons.', 'example_request': 'Make me an Adaptive Card showing monitor storage capacity status for USMF as of 2026-05-24.', 'inputs': [{'description': 'D365 legal entity to report against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-monitor-storage-capacity-2026-05-24-card.json.', 'name': 'output_filename'}, {'description': 'Date used for the card timestamp and filename.', 'name': 'as_of_date'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable Adaptive Card snapshot of D365 monitor storage capacity status for Teams, Outlook, or a dashboard.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardMonitorStorageCapacity(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardMonitorStorageCapacity'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'as_of_date': {'description': 'Date used for the card timestamp and filename.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-monitor-storage-capacity-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardMonitorStorageCapacity().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
