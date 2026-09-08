---
name: "rar-cowork-cookbook-adaptive-card-retire-software-licenses"
description: "Generates a read-only Adaptive Card JSON file summarizing retire-software-licenses status from Dynamics 365 F&SCM (legal entity USMF), with header, 3-5 KPI tiles with trend arrows, a RAG row, and 2-3 action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_retire_software_licenses", "rar_sha256": "a6dc244db59c78edd78d633e0d6540c08a39a3574313a52916460ac49a0399c5", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
