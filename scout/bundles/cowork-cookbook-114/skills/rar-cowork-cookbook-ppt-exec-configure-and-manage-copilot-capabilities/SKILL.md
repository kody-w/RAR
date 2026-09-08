---
name: "rar-cowork-cookbook-ppt-exec-configure-and-manage-copilot-capabilities"
description: "Builds a read-only executive PowerPoint deck on configure-and-manage-copilot-capabilities status from Dynamics 365 ERP data for a legal entity, with KPI, trend, red-flag, action and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_configure_and_manage_copilot_capabilities", "rar_sha256": "b5785452f23b7d04c5611f263938c271254c8d923950ea10059f06d3c2637fda", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_configure_and_manage_copilot_capabilities`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_configure_and_manage_copilot_capabilities_agent.py` and in the RCI capsule.

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

Configure and manage copilot capabilities Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on configure-and-manage-copilot-capabilities status from Dynamics 365 ERP data for a legal entity, with KPI, trend, red-flag, action and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-configure-and-manage-copilot-capabilities
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
      "description": "Dynamics 365 legal entity to report on, e.g. USMF.",
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
      "description": "Target .pptx filename, e.g. ppt-exec-configure-and-manage-copilot-capabilities-2026-05-24.pptx.",
      "type": "string"
    },
    "review_period": {
      "description": "Reporting period and prior period used for the trend comparison, e.g. monthly review dated 2026-05-24.",
      "type": "string"
    },
    "topic": {
      "description": "Subject of the deck, e.g. configure and manage copilot capabilities.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_configure_and_manage_copilot_capabilities_agent.py` and embedded as the fenced Python below (sha256 b5785452f23b7d04…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_configure_and_manage_copilot_capabilities_agent.py` first:

```bash
python3 ppt_exec_configure_and_manage_copilot_capabilities_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_configure_and_manage_copilot_capabilities_agent.py   # or on stdin
python3 ppt_exec_configure_and_manage_copilot_capabilities_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and manage copilot capabilities Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on configure-and-manage-copilot-capabilities status from Dynamics 365 ERP data for a legal entity, with KPI, trend, red-flag, action and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-configure-and-manage-copilot-capabilities
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_configure_and_manage_copilot_capabilities',
    "version": '3.0.3',
    "display_name": 'Configure and manage copilot capabilities Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on configure-and-manage-copilot-capabilities status from Dynamics 365 ERP data for a legal entity, with KPI, trend, red-flag, action and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-configure-and-manage-copilot-capabilities',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-configure-and-manage-copilot-capabilities',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6b8a927d9758456a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-manage-copilot-capabilities'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/ppt-exec-configure-and-manage-copilot-capabilities', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'output_filename': 'Target .pptx filename, e.g. ppt-exec-configure-and-manage-copilot-capabilities-2026-05-24.pptx.', 'review_period': 'Reporting period and prior period used for the trend comparison, e.g. monthly review dated 2026-05-24.', 'topic': 'Subject of the deck, e.g. configure and manage copilot capabilities.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for configure and manage copilot capabilities reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on configure and manage copilot capabilities for a 15-minute monthly review. Produce 'ppt-exec-configure-and-manage-copilot-capabilities-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads configure and manage copilot capabilities data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on configure-and-manage-copilot-capabilities status from Dynamics 365 ERP data for a legal entity, with KPI, trend, red-flag, action and appendix slides plus speaker notes.', 'example_request': 'Build the monthly exec PowerPoint on copilot capabilities for legal entity USMF, with charts and speaker notes.', 'inputs': [{'description': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Subject of the deck, e.g. configure and manage copilot capabilities.', 'name': 'topic'}, {'description': 'Target .pptx filename, e.g. ppt-exec-configure-and-manage-copilot-capabilities-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Reporting period and prior period used for the trend comparison, e.g. monthly review dated 2026-05-24.', 'name': 'review_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs an executive-ready .pptx status deck for a 15-minute monthly review sourced from Dynamics 365 F&SCM, without changing any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecConfigureAndManageCopilotCapabilities(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecConfigureAndManageCopilotCapabilities'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Target .pptx filename, e.g. ppt-exec-configure-and-manage-copilot-capabilities-2026-05-24.pptx.', 'type': 'string'}, 'review_period': {'description': 'Reporting period and prior period used for the trend comparison, e.g. monthly review dated 2026-05-24.', 'type': 'string'}, 'topic': {'description': 'Subject of the deck, e.g. configure and manage copilot capabilities.', 'type': 'string'}},
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
    print(PptExecConfigureAndManageCopilotCapabilities().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
