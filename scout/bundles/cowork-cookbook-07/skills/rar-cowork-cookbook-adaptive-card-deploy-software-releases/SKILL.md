---
name: "rar-cowork-cookbook-adaptive-card-deploy-software-releases"
description: "Generates a read-only Adaptive Card JSON file visualizing deploy software releases status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_deploy_software_releases", "rar_sha256": "b59ffb03f9d4883bc882e4e11c07586ed247efcaa8a3c72674d3eff83d64905e", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
