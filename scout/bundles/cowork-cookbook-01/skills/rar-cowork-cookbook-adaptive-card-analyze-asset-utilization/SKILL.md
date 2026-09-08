---
name: "rar-cowork-cookbook-adaptive-card-analyze-asset-utilization"
description: "Generates a read-only Adaptive Card JSON file visualizing asset utilization status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, trend arrows, a RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_analyze_asset_utilization", "rar_sha256": "4a444b402548a12e475c253428e22fc068075b5e453535618d545ef819f25b2c", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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
