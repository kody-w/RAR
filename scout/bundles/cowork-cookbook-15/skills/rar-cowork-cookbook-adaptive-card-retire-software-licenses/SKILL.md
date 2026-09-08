---
name: "rar-cowork-cookbook-adaptive-card-retire-software-licenses"
description: "Generates a read-only Adaptive Card JSON file summarizing retire-software-licenses status from Dynamics 365 F&SCM (legal entity USMF), with header, 3-5 KPI tiles with trend arrows, a RAG row, and 2-3 action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_retire_software_licenses", "rar_sha256": "a6dc244db59c78edd78d633e0d6540c08a39a3574313a52916460ac49a0399c5", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_retire_software_licenses`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_retire_software_licenses_agent.py` and in the RCI capsule.

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

Retire software licenses Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing retire-software-licenses status from Dynamics 365 F&SCM (legal entity USMF), with header, 3-5 KPI tiles with trend arrows, a RAG row, and 2-3 action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-retire-software-licenses
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
      "description": "Dynamics 365 legal entity to query, e.g. USMF.",
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
      "description": "Name of the Adaptive Card JSON file to write into Documents/Cowork/output/.",
      "type": "string"
    },
    "snapshot_date": {
      "description": "Date used in the card timestamp and output filename, e.g. 2026-05-24.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_retire_software_licenses_agent.py` and embedded as the fenced Python below (sha256 a6dc244db59c78ed…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_retire_software_licenses_agent.py` first:

```bash
python3 adaptive_card_retire_software_licenses_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_retire_software_licenses_agent.py   # or on stdin
python3 adaptive_card_retire_software_licenses_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Retire software licenses Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing retire-software-licenses status from Dynamics 365 F&SCM (legal entity USMF), with header, 3-5 KPI tiles with trend arrows, a RAG row, and 2-3 action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-retire-software-licenses
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_retire_software_licenses',
    "version": '3.0.2',
    "display_name": 'Retire software licenses Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file summarizing retire-software-licenses status from Dynamics 365 F&SCM (legal entity USMF), with header, 3-5 KPI tiles with trend arrows, a RAG row, and 2-3 action buttons.',
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
        "upstream_slug": 'adaptive-card-retire-software-licenses',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-retire-software-licenses',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0223324a3bfe65d2',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-licensing-and-entitlements/retire-software-licenses'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/adaptive-card-retire-software-licenses', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to write into Documents/Cowork/output/.', 'snapshot_date': 'Date used in the card timestamp and output filename, e.g. 2026-05-24.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical retire software licenses status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-retire-software-licenses-2026-05-24-card.json' that visualizes the current state of retire software licenses. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-06-01', 'what_it_does': 'Generates an Adaptive Card JSON file with current retire software licenses KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file summarizing retire-software-licenses status from Dynamics 365 F&SCM (legal entity USMF), with header, 3-5 KPI tiles with trend arrows, a RAG row, and 2-3 action buttons.', 'example_request': 'Make an Adaptive Card showing retire software licenses status for USMF as of 2026-05-24.', 'inputs': [{'description': 'Dynamics 365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date used in the card timestamp and output filename, e.g. 2026-05-24.', 'name': 'snapshot_date'}, {'description': 'Name of the Adaptive Card JSON file to write into Documents/Cowork/output/.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable Adaptive Card snapshot of retire software licenses status for Teams, Outlook, or a dashboard, without changing any D365 data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardRetireSoftwareLicenses(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardRetireSoftwareLicenses'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to write into Documents/Cowork/output/.', 'type': 'string'}, 'snapshot_date': {'description': 'Date used in the card timestamp and output filename, e.g. 2026-05-24.', 'type': 'string'}},
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
    print(AdaptiveCardRetireSoftwareLicenses().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
