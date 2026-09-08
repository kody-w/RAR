---
name: "rar-cowork-cookbook-adaptive-card-deploy-software-releases"
description: "Generates a read-only Adaptive Card JSON file visualizing deploy software releases status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_deploy_software_releases", "rar_sha256": "b59ffb03f9d4883bc882e4e11c07586ed247efcaa8a3c72674d3eff83d64905e", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_deploy_software_releases`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_deploy_software_releases_agent.py` and in the RCI capsule.

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

Deploy software releases Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing deploy software releases status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-deploy-software-releases
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
      "description": "Date used for the card timestamp and file naming.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity to read from, e.g. USMF.",
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-deploy-software-releases-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_deploy_software_releases_agent.py` and embedded as the fenced Python below (sha256 b59ffb03f9d4883b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_deploy_software_releases_agent.py` first:

```bash
python3 adaptive_card_deploy_software_releases_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_deploy_software_releases_agent.py   # or on stdin
python3 adaptive_card_deploy_software_releases_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Deploy software releases Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing deploy software releases status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-deploy-software-releases
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_deploy_software_releases',
    "version": '3.0.2',
    "display_name": 'Deploy software releases Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file visualizing deploy software releases status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons.',
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
        "upstream_slug": 'adaptive-card-deploy-software-releases',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-deploy-software-releases',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e01533e18ea3e29d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/uptake-software-releases/deploy-software-releases'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/adaptive-card-deploy-software-releases', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'as_of_date': 'Date used for the card timestamp and file naming.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to read from, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-deploy-software-releases-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical deploy software releases status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-deploy-software-releases-2026-05-24-card.json' that visualizes the current state of deploy software releases. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-06-01', 'what_it_does': 'Generates an Adaptive Card JSON file with current deploy software releases KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file visualizing deploy software releases status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons.', 'example_request': 'Make an Adaptive Card JSON of deploy software releases status for USMF as of 2026-05-24.', 'inputs': [{'description': 'Dynamics 365 legal entity to read from, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-deploy-software-releases-2026-05-24-card.json.', 'name': 'output_filename'}, {'description': 'Date used for the card timestamp and file naming.', 'name': 'as_of_date'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants an embeddable Adaptive Card snapshot of deploy software releases status for Teams, Outlook, or a dashboard, without changing any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardDeploySoftwareReleases(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDeploySoftwareReleases'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'as_of_date': {'description': 'Date used for the card timestamp and file naming.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to read from, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-deploy-software-releases-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardDeploySoftwareReleases().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
