---
name: "rar-cowork-cookbook-adaptive-card-configure-segregation-of-duties"
description: "Generates a read-only Adaptive Card JSON file summarizing segregation of duties configuration status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_configure_segregation_of_duties", "rar_sha256": "8f2a86c3f55e90957680298caa3aa418109016835ed9620c0e3cc26020cd1226", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_configure_segregation_of_duties`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_configure_segregation_of_duties_agent.py` and in the RCI capsule.

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

Configure segregation of duties Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing segregation of duties configuration status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-configure-segregation-of-duties
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
      "description": "D365 legal entity to report on, e.g. USMF.",
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-configure-segregation-of-duties-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_configure_segregation_of_duties_agent.py` and embedded as the fenced Python below (sha256 8f2a86c3f55e9095…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_configure_segregation_of_duties_agent.py` first:

```bash
python3 adaptive_card_configure_segregation_of_duties_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_configure_segregation_of_duties_agent.py   # or on stdin
python3 adaptive_card_configure_segregation_of_duties_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure segregation of duties Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing segregation of duties configuration status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-configure-segregation-of-duties
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_configure_segregation_of_duties',
    "version": '3.0.2',
    "display_name": 'Configure segregation of duties Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file summarizing segregation of duties configuration status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.',
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
        "upstream_slug": 'adaptive-card-configure-segregation-of-duties',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-configure-segregation-of-duties',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd62f7c7d220cbcfd',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-access-and-security/configure-segregation-of-duties'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/adaptive-card-configure-segregation-of-duties', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'as_of_date': 'Date used for the card timestamp and filename.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-configure-segregation-of-duties-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical configure segregation of duties status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-configure-segregation-of-duties-2026-05-24-card.json' that visualizes the current state of configure segregation of duties. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-06-01', 'what_it_does': 'Generates an Adaptive Card JSON file with current configure segregation of duties KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file summarizing segregation of duties configuration status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.', 'example_request': 'Make me an Adaptive Card JSON showing segregation of duties status for USMF as of 2026-05-24.', 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-configure-segregation-of-duties-2026-05-24-card.json.', 'name': 'output_filename'}, {'description': 'Date used for the card timestamp and filename.', 'name': 'as_of_date'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a Teams/Outlook-ready Adaptive Card snapshot of segregation of duties status from D365 ERP, without changing any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardConfigureSegregationOfDuties(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardConfigureSegregationOfDuties'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'as_of_date': {'description': 'Date used for the card timestamp and filename.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-configure-segregation-of-duties-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardConfigureSegregationOfDuties().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
