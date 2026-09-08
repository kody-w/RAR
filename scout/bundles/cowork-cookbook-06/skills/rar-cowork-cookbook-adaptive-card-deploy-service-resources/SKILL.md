---
name: "rar-cowork-cookbook-adaptive-card-deploy-service-resources"
description: "Generates a read-only Adaptive Card JSON file visualizing deploy service resources status from Dynamics 365 F&SCM for a given legal entity, with header, KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_deploy_service_resources", "rar_sha256": "815b107025eb560a37d7753b2db4d10553c4e35aab6b5a844301bf2b739ebbca", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_deploy_service_resources`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_deploy_service_resources_agent.py` and in the RCI capsule.

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

Deploy service resources Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing deploy service resources status from Dynamics 365 F&SCM for a given legal entity, with header, KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-deploy-service-resources
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
      "description": "Snapshot date used in the card timestamp and output filename.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 F&SCM legal entity to query, e.g. USMF.",
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-deploy-service-resources-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_deploy_service_resources_agent.py` and embedded as the fenced Python below (sha256 815b107025eb560a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_deploy_service_resources_agent.py` first:

```bash
python3 adaptive_card_deploy_service_resources_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_deploy_service_resources_agent.py   # or on stdin
python3 adaptive_card_deploy_service_resources_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Deploy service resources Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing deploy service resources status from Dynamics 365 F&SCM for a given legal entity, with header, KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-deploy-service-resources
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_deploy_service_resources',
    "version": '3.0.2',
    "display_name": 'Deploy service resources Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file visualizing deploy service resources status from Dynamics 365 F&SCM for a given legal entity, with header, KPI tiles, RAG row, and action buttons.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-deploy-service-resources',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-deploy-service-resources',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '129670cb690d01bf',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/manage-service-work/deploy-service-resources'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/adaptive-card-deploy-service-resources', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'as_of_date': 'Snapshot date used in the card timestamp and output filename.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 F&SCM legal entity to query, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-deploy-service-resources-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical deploy service resources status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-deploy-service-resources-2026-05-24-card.json' that visualizes the current state of deploy service resources. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current deploy service resources KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file visualizing deploy service resources status from Dynamics 365 F&SCM for a given legal entity, with header, KPI tiles, RAG row, and action buttons.', 'example_request': 'Make me an Adaptive Card JSON of deploy service resources status in USMF as of 2026-05-24.', 'inputs': [{'description': 'D365 F&SCM legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Snapshot date used in the card timestamp and output filename.', 'name': 'as_of_date'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-deploy-service-resources-2026-05-24-card.json.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable Adaptive Card snapshot of deploy service resources status for Teams, Outlook, or a dashboard, without changing D365 data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardDeployServiceResources(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDeployServiceResources'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'as_of_date': {'description': 'Snapshot date used in the card timestamp and output filename.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 F&SCM legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-deploy-service-resources-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardDeployServiceResources().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
