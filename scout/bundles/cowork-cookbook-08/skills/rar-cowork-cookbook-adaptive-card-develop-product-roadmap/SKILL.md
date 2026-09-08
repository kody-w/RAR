---
name: "rar-cowork-cookbook-adaptive-card-develop-product-roadmap"
description: "Generates a read-only Adaptive Card JSON file visualizing develop product roadmap status from Dynamics 365 F&SCM via the Cowork D365 ERP plugin, with KPI tiles, a RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_develop_product_roadmap", "rar_sha256": "c121ea3847757a4f7fc265cd9fc6ecdfdaafb6cfe2ae6b5679500bf7bf2b42c5", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_develop_product_roadmap`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_develop_product_roadmap_agent.py` and in the RCI capsule.

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

Develop product roadmap Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing develop product roadmap status from Dynamics 365 F&SCM via the Cowork D365 ERP plugin, with KPI tiles, a RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-develop-product-roadmap
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
      "description": "D365 legal entity to query, e.g. USMF.",
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-develop-product-roadmap-2026-05-24-card.json.",
      "type": "string"
    },
    "snapshot_date": {
      "description": "Date the status snapshot represents, used in the card header timestamp and file name.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_develop_product_roadmap_agent.py` and embedded as the fenced Python below (sha256 c121ea3847757a4f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_develop_product_roadmap_agent.py` first:

```bash
python3 adaptive_card_develop_product_roadmap_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_develop_product_roadmap_agent.py   # or on stdin
python3 adaptive_card_develop_product_roadmap_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop product roadmap Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing develop product roadmap status from Dynamics 365 F&SCM via the Cowork D365 ERP plugin, with KPI tiles, a RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-develop-product-roadmap
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_develop_product_roadmap',
    "version": '3.0.2',
    "display_name": 'Develop product roadmap Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file visualizing develop product roadmap status from Dynamics 365 F&SCM via the Cowork D365 ERP plugin, with KPI tiles, a RAG row, and action buttons.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'community',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'adaptive-card-develop-product-roadmap',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-develop-product-roadmap',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5a0acee7539354c3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/develop-product-strategy/develop-product-roadmap'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/adaptive-card-develop-product-roadmap', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_file_name': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-develop-product-roadmap-2026-05-24-card.json.', 'snapshot_date': 'Date the status snapshot represents, used in the card header timestamp and file name.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical develop product roadmap status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-develop-product-roadmap-2026-05-24-card.json' that visualizes the current state of develop product roadmap. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current develop product roadmap KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file visualizing develop product roadmap status from Dynamics 365 F&SCM via the Cowork D365 ERP plugin, with KPI tiles, a RAG row, and action buttons.', 'example_request': 'Make an Adaptive Card JSON of develop product roadmap status from USMF for 2026-05-24.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-develop-product-roadmap-2026-05-24-card.json.', 'name': 'output_file_name'}, {'description': 'Date the status snapshot represents, used in the card header timestamp and file name.', 'name': 'snapshot_date'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable Adaptive Card snapshot of develop product roadmap status for Teams, Outlook, or a dashboard, without changing any D365 data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardDevelopProductRoadmap(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDevelopProductRoadmap'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_file_name': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-develop-product-roadmap-2026-05-24-card.json.', 'type': 'string'}, 'snapshot_date': {'description': 'Date the status snapshot represents, used in the card header timestamp and file name.', 'type': 'string'}},
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
    print(AdaptiveCardDevelopProductRoadmap().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
