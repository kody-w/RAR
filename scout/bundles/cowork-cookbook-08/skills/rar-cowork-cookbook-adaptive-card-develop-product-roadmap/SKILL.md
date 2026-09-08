---
name: "rar-cowork-cookbook-adaptive-card-develop-product-roadmap"
description: "Generates a read-only Adaptive Card JSON file visualizing develop product roadmap status from Dynamics 365 F&SCM via the Cowork D365 ERP plugin, with KPI tiles, a RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_develop_product_roadmap", "rar_sha256": "c121ea3847757a4f7fc265cd9fc6ecdfdaafb6cfe2ae6b5679500bf7bf2b42c5", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
