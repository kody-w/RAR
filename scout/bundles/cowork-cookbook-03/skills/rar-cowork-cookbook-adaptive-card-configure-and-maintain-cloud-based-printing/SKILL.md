---
name: "rar-cowork-cookbook-adaptive-card-configure-and-maintain-cloud-based-printing"
description: "Generates a read-only Adaptive Card JSON file summarizing cloud-based printing configuration status from Dynamics 365 F&SCM, with header, KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_configure_and_maintain_cloud_based_printing", "rar_sha256": "754d339cbc29b0fd9d66ed417d4d5b563d6e9ec19cbc92ce7f9a9d27eeafcbfd", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_configure_and_maintain_cloud_based_printing`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_configure_and_maintain_cloud_based_printing_agent.py` and in the RCI capsule.

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

Configure and maintain cloud-based printing Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing cloud-based printing configuration status from Dynamics 365 F&SCM, with header, KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-configure-and-maintain-cloud-based-printing
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
    "action_button_count": {
      "description": "How many action buttons to include (2-3).",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "kpi_count": {
      "description": "How many KPI tiles to include (3-5).",
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-configure-and-maintain-cloud-based-printing-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_configure_and_maintain_cloud_based_printing_agent.py` and embedded as the fenced Python below (sha256 754d339cbc29b0fd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_configure_and_maintain_cloud_based_printing_agent.py` first:

```bash
python3 adaptive_card_configure_and_maintain_cloud_based_printing_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_configure_and_maintain_cloud_based_printing_agent.py   # or on stdin
python3 adaptive_card_configure_and_maintain_cloud_based_printing_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and maintain cloud-based printing Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing cloud-based printing configuration status from Dynamics 365 F&SCM, with header, KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-configure-and-maintain-cloud-based-printing
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_configure_and_maintain_cloud_based_printing',
    "version": '3.0.2',
    "display_name": 'Configure and maintain cloud-based printing Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file summarizing cloud-based printing configuration status from Dynamics 365 F&SCM, with header, KPI tiles, RAG row, and action buttons.',
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
        "upstream_slug": 'adaptive-card-configure-and-maintain-cloud-based-printing',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-configure-and-maintain-cloud-based-printing',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c1efcdef9bbdbfad',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-maintain-cloud-based-printing'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/adaptive-card-configure-and-maintain-cloud-based-printing', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'action_button_count': 'How many action buttons to include (2-3).', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'kpi_count': 'How many KPI tiles to include (3-5).', 'legal_entity': 'D365 legal entity to report against, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-configure-and-maintain-cloud-based-printing-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical configure and maintain cloud-based printing status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-configure-and-maintain-cloud-based-printing-2026-05-24-card.json' that visualizes the current state of configure and maintain cloud-based printing. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-06-01', 'what_it_does': 'Generates an Adaptive Card JSON file with current configure and maintain cloud-based printing KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file summarizing cloud-based printing configuration status from Dynamics 365 F&SCM, with header, KPI tiles, RAG row, and action buttons.', 'example_request': 'Make an Adaptive Card JSON showing cloud printing status in USMF for our Teams dashboard.', 'inputs': [{'description': 'D365 legal entity to report against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-configure-and-maintain-cloud-based-printing-2026-05-24-card.json.', 'name': 'output_filename'}, {'description': 'How many KPI tiles to include (3-5).', 'name': 'kpi_count'}, {'description': 'How many action buttons to include (2-3).', 'name': 'action_button_count'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants an embeddable Adaptive Card snapshot of cloud-based printing status from D365 ERP for Teams, Outlook, or a dashboard.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardConfigureAndMaintainCloudBasedPrinting(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardConfigureAndMaintainCloudBasedPrinting'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'action_button_count': {'description': 'How many action buttons to include (2-3).', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'kpi_count': {'description': 'How many KPI tiles to include (3-5).', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-configure-and-maintain-cloud-based-printing-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardConfigureAndMaintainCloudBasedPrinting().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
