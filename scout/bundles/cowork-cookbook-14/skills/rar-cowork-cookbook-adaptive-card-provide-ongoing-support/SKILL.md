---
name: "rar-cowork-cookbook-adaptive-card-provide-ongoing-support"
description: "Generates a read-only Adaptive Card JSON file visualizing provide-ongoing-support status from Dynamics 365 F&SCM (legal entity USMF), with header, 3-5 KPI tiles, a RAG row, and 2-3 action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_provide_ongoing_support", "rar_sha256": "6c232847535af18f24dde587177fd452e069b90f2ea2461c45e205880d589084", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_provide_ongoing_support`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_provide_ongoing_support_agent.py` and in the RCI capsule.

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

Provide ongoing support Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing provide-ongoing-support status from Dynamics 365 F&SCM (legal entity USMF), with header, 3-5 KPI tiles, a RAG row, and 2-3 action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-provide-ongoing-support
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
      "description": "D365 F&SCM legal entity to read from (e.g. USMF).",
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
    "output_file_name": {
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-provide-ongoing-support-2026-05-24-card.json.",
      "type": "string"
    },
    "snapshot_date": {
      "description": "Date the status snapshot represents, used in the card timestamp and file name.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_provide_ongoing_support_agent.py` and embedded as the fenced Python below (sha256 6c232847535af18f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_provide_ongoing_support_agent.py` first:

```bash
python3 adaptive_card_provide_ongoing_support_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_provide_ongoing_support_agent.py   # or on stdin
python3 adaptive_card_provide_ongoing_support_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Provide ongoing support Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing provide-ongoing-support status from Dynamics 365 F&SCM (legal entity USMF), with header, 3-5 KPI tiles, a RAG row, and 2-3 action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-provide-ongoing-support
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_provide_ongoing_support',
    "version": '3.0.2',
    "display_name": 'Provide ongoing support Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file visualizing provide-ongoing-support status from Dynamics 365 F&SCM (legal entity USMF), with header, 3-5 KPI tiles, a RAG row, and 2-3 action buttons.',
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
        "upstream_slug": 'adaptive-card-provide-ongoing-support',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-provide-ongoing-support',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1ab201a0b6340b37',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/train-users-and-increase-adoption/provide-ongoing-support'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/adaptive-card-provide-ongoing-support', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 F&SCM legal entity to read from (e.g. USMF).', 'output_file_name': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-provide-ongoing-support-2026-05-24-card.json.', 'snapshot_date': 'Date the status snapshot represents, used in the card timestamp and file name.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical provide ongoing support status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-provide-ongoing-support-2026-05-24-card.json' that visualizes the current state of provide ongoing support. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-06-01', 'what_it_does': 'Generates an Adaptive Card JSON file with current provide ongoing support KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file visualizing provide-ongoing-support status from Dynamics 365 F&SCM (legal entity USMF), with header, 3-5 KPI tiles, a RAG row, and 2-3 action buttons.', 'example_request': 'Make an Adaptive Card JSON of provide ongoing support status from D365 USMF for 2026-05-24.', 'inputs': [{'description': 'D365 F&SCM legal entity to read from (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-provide-ongoing-support-2026-05-24-card.json.', 'name': 'output_file_name'}, {'description': 'Date the status snapshot represents, used in the card timestamp and file name.', 'name': 'snapshot_date'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a Teams/Outlook-renderable Adaptive Card snapshot of provide ongoing support status from D365 ERP data, without modifying any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardProvideOngoingSupport(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardProvideOngoingSupport'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 F&SCM legal entity to read from (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_file_name': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-provide-ongoing-support-2026-05-24-card.json.', 'type': 'string'}, 'snapshot_date': {'description': 'Date the status snapshot represents, used in the card timestamp and file name.', 'type': 'string'}},
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
    print(AdaptiveCardProvideOngoingSupport().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
