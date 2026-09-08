---
name: "rar-cowork-cookbook-adaptive-card-deploy-service-resources"
description: "Generates a read-only Adaptive Card JSON file visualizing deploy service resources status from Dynamics 365 F&SCM for a given legal entity, with header, KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_deploy_service_resources", "rar_sha256": "815b107025eb560a37d7753b2db4d10553c4e35aab6b5a844301bf2b739ebbca", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
