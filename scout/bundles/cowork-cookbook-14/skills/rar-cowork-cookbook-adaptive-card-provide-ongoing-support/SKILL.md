---
name: "rar-cowork-cookbook-adaptive-card-provide-ongoing-support"
description: "Generates a read-only Adaptive Card JSON file visualizing provide-ongoing-support status from Dynamics 365 F&SCM (legal entity USMF), with header, 3-5 KPI tiles, a RAG row, and 2-3 action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_provide_ongoing_support", "rar_sha256": "6c232847535af18f24dde587177fd452e069b90f2ea2461c45e205880d589084", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
