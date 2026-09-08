---
name: "rar-cowork-cookbook-adaptive-card-analyze-asset-utilization"
description: "Generates a read-only Adaptive Card JSON file visualizing asset utilization status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, trend arrows, a RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_analyze_asset_utilization", "rar_sha256": "4a444b402548a12e475c253428e22fc068075b5e453535618d545ef819f25b2c", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_analyze_asset_utilization`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_analyze_asset_utilization_agent.py` and in the RCI capsule.

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

Analyze asset utilization Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing asset utilization status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, trend arrows, a RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-analyze-asset-utilization
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
      "description": "Date the snapshot represents, used in the card timestamp and output filename.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity to report on (e.g. USMF).",
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-analyze-asset-utilization-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_analyze_asset_utilization_agent.py` and embedded as the fenced Python below (sha256 4a444b402548a12e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_analyze_asset_utilization_agent.py` first:

```bash
python3 adaptive_card_analyze_asset_utilization_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_analyze_asset_utilization_agent.py   # or on stdin
python3 adaptive_card_analyze_asset_utilization_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze asset utilization Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing asset utilization status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, trend arrows, a RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-analyze-asset-utilization
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_analyze_asset_utilization',
    "version": '3.0.2',
    "display_name": 'Analyze asset utilization Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file visualizing asset utilization status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, trend arrows, a RAG row, and action buttons.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-analyze-asset-utilization',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-analyze-asset-utilization',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ffbdd6c299160e91',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/analyze-assets/analyze-asset-utilization'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/adaptive-card-analyze-asset-utilization', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'as_of_date': 'Date the snapshot represents, used in the card timestamp and output filename.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to report on (e.g. USMF).', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-analyze-asset-utilization-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical analyze asset utilization status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-analyze-asset-utilization-2026-05-24-card.json' that visualizes the current state of analyze asset utilization. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Generates an Adaptive Card JSON file with current analyze asset utilization KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file visualizing asset utilization status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, trend arrows, a RAG row, and action buttons.', 'example_request': 'Make me an Adaptive Card showing asset utilization status for USMF as of 2026-05-24.', 'inputs': [{'description': 'Dynamics 365 legal entity to report on (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Date the snapshot represents, used in the card timestamp and output filename.', 'name': 'as_of_date'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-analyze-asset-utilization-2026-05-24-card.json.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants an embeddable Adaptive Card snapshot of asset utilization status for Teams, Outlook, or a dashboard, without changing D365 data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardAnalyzeAssetUtilization(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardAnalyzeAssetUtilization'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'as_of_date': {'description': 'Date the snapshot represents, used in the card timestamp and output filename.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to report on (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-analyze-asset-utilization-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardAnalyzeAssetUtilization().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
