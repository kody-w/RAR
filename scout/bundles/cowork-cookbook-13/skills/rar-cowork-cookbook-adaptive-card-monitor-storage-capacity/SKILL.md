---
name: "rar-cowork-cookbook-adaptive-card-monitor-storage-capacity"
description: "Generates a read-only Adaptive Card JSON file visualizing monitor storage capacity status for a Dynamics 365 F&SCM legal entity, with header, KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_monitor_storage_capacity", "rar_sha256": "64130eb9d42ac37480cbf130f97f346cd6a176fa8fe56ad9883525ea753ec5f2", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
