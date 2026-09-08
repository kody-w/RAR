---
name: "rar-cowork-cookbook-adaptive-card-configure-and-maintain-cloud-based-printing"
description: "Generates a read-only Adaptive Card JSON file summarizing cloud-based printing configuration status from Dynamics 365 F&SCM, with header, KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_configure_and_maintain_cloud_based_printing", "rar_sha256": "754d339cbc29b0fd9d66ed417d4d5b563d6e9ec19cbc92ce7f9a9d27eeafcbfd", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
