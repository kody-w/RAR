---
name: "rar-cowork-cookbook-adaptive-card-define-recovery-objectives"
description: "Generates a read-only Adaptive Card JSON file visualizing define recovery objectives status from Dynamics 365 F&SCM for a given legal entity, with header, KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_define_recovery_objectives", "rar_sha256": "b21691666330436b00f3dd9d28dfa0cffbb5f3be0c96c078781f35f9c701c5d2", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
