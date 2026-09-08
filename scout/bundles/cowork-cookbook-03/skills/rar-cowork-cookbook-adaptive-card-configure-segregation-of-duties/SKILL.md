---
name: "rar-cowork-cookbook-adaptive-card-configure-segregation-of-duties"
description: "Generates a read-only Adaptive Card JSON file summarizing segregation of duties configuration status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_configure_segregation_of_duties", "rar_sha256": "8f2a86c3f55e90957680298caa3aa418109016835ed9620c0e3cc26020cd1226", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
