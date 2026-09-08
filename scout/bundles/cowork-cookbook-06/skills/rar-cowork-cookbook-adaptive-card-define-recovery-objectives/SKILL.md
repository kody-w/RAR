---
name: "rar-cowork-cookbook-adaptive-card-define-recovery-objectives"
description: "Generates a read-only Adaptive Card JSON file visualizing define recovery objectives status from Dynamics 365 F&SCM for a given legal entity, with header, KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_define_recovery_objectives", "rar_sha256": "b21691666330436b00f3dd9d28dfa0cffbb5f3be0c96c078781f35f9c701c5d2", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_define_recovery_objectives`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_define_recovery_objectives_agent.py` and in the RCI capsule.

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

Define recovery objectives Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing define recovery objectives status from Dynamics 365 F&SCM for a given legal entity, with header, KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-define-recovery-objectives
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
    "action_buttons": {
      "description": "The 2-3 action buttons to include on the card.",
      "type": "string"
    },
    "as_of_date": {
      "description": "Snapshot date used in the card timestamp and output filename.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "kpi_count": {
      "description": "How many KPI tiles to include (3-5), each with current value and trend arrow.",
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-define-recovery-objectives-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_define_recovery_objectives_agent.py` and embedded as the fenced Python below (sha256 b21691666330436b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_define_recovery_objectives_agent.py` first:

```bash
python3 adaptive_card_define_recovery_objectives_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_define_recovery_objectives_agent.py   # or on stdin
python3 adaptive_card_define_recovery_objectives_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define recovery objectives Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing define recovery objectives status from Dynamics 365 F&SCM for a given legal entity, with header, KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-define-recovery-objectives
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_define_recovery_objectives',
    "version": '3.0.2',
    "display_name": 'Define recovery objectives Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file visualizing define recovery objectives status from Dynamics 365 F&SCM for a given legal entity, with header, KPI tiles, RAG row, and action buttons.',
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
        "upstream_slug": 'adaptive-card-define-recovery-objectives',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-define-recovery-objectives',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '21cf2611ac5c362a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/define-business-continuity-plan/define-recovery-objectives'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/adaptive-card-define-recovery-objectives', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'action_buttons': 'The 2-3 action buttons to include on the card.', 'as_of_date': 'Snapshot date used in the card timestamp and output filename.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'kpi_count': 'How many KPI tiles to include (3-5), each with current value and trend arrow.', 'legal_entity': 'D365 F&SCM legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-define-recovery-objectives-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical define recovery objectives status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-define-recovery-objectives-2026-05-24-card.json' that visualizes the current state of define recovery objectives. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-06-01', 'what_it_does': 'Generates an Adaptive Card JSON file with current define recovery objectives KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file visualizing define recovery objectives status from Dynamics 365 F&SCM for a given legal entity, with header, KPI tiles, RAG row, and action buttons.', 'example_request': 'Make an Adaptive Card JSON for define recovery objectives status in USMF as of 2026-05-24, read-only.', 'inputs': [{'description': 'D365 F&SCM legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Snapshot date used in the card timestamp and output filename.', 'name': 'as_of_date'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-define-recovery-objectives-2026-05-24-card.json.', 'name': 'output_filename'}, {'description': 'How many KPI tiles to include (3-5), each with current value and trend arrow.', 'name': 'kpi_count'}, {'description': 'The 2-3 action buttons to include on the card.', 'name': 'action_buttons'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a Teams/Outlook-ready Adaptive Card snapshot of define recovery objectives status from D365 ERP data, without modifying any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardDefineRecoveryObjectives(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDefineRecoveryObjectives'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'action_buttons': {'description': 'The 2-3 action buttons to include on the card.', 'type': 'string'}, 'as_of_date': {'description': 'Snapshot date used in the card timestamp and output filename.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'kpi_count': {'description': 'How many KPI tiles to include (3-5), each with current value and trend arrow.', 'type': 'string'}, 'legal_entity': {'description': 'D365 F&SCM legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-define-recovery-objectives-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardDefineRecoveryObjectives().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
