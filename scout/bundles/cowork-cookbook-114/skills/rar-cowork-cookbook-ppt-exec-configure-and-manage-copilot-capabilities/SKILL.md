---
name: "rar-cowork-cookbook-ppt-exec-configure-and-manage-copilot-capabilities"
description: "Builds a read-only executive PowerPoint deck on configure-and-manage-copilot-capabilities status from Dynamics 365 ERP data for a legal entity, with KPI, trend, red-flag, action and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_configure_and_manage_copilot_capabilities", "rar_sha256": "b5785452f23b7d04c5611f263938c271254c8d923950ea10059f06d3c2637fda", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/916WbOjWJLmX9HcfsjMJuIiNiGirc0GSSxa2EEgZZRFsoPYVwE5+d/nIN0bEVkV1VNp3U+jWCTBOb775+46/P5id21U1C+fXjTfzhecnaZx5NcLO/cW2+Je1Al4KxIH/Fu4Rd7WsdO1Rd28fHjx/Mat47KNixxs33Rx6jULe1H7tvexyNNx4Q++27Vx7y/k4u7XchHn7cLz3WRR5DOxIA672v8IWH3M7NwO/Y9uUcZp0X507dJ24jRuY79ZNK3dds0iqItssRtzO4vdZoGtiAWjygvPbu1FUACBF6kf2unCz9u4HT8s7nEbLY7y/sOirf3c+wDk8j4GqR1+WNjuLPNDRbsswc14WDRpDPRZlCng1JS+nQAb5EXrN69AU3+wszL1m5dPv/7tw0sMPr98+v3FTe0GXHqRy5YBmm7fFaJzT3ios31qs/1OGUAstfMQ7CpHYPccfC/9GsifgUueHyzevv3c+GnwYfHv/57c7Tpsfvn0OV+8vT6/zH/ULl+0kb9oC7tpfW/x1WLj64JO7/bYAIXbrs5nlzTAbXn4+tz5jVJRLv5zvvfzk8lr6Lc/f34pgAj2bKDPL78sgGE/v9Td/Pl1plL+/MtrOjvz51++0Wk65+a77UwMSP365e37G1mw8NvSOFh80WRm+8ar9t249AHx7/SbX0/R38i9meTLc/HPRflh8WPKsz7/CeR9BqYD6P6YLLAB2PnyegMB+fMbj7ro/dzOXf/nX/4ZWTcCoZvGTfsv0f31STgC2QCs9WaSXz483Pe3BfSm21ea/5xtCQLmr2gClr+z+2qof0b74dm/I53GOUiEd1/+kNyPNkD/ufj1n+r2X234sAg+v+z8FOBEbTup/2nx+yNEfv3J+3bxp7/9AUj/P8loRVe7DwpfAKLEgd+0X778+lPzuPzT3379qStBFPt29qWr0x/R/JFdH3z+ZMG3VT//eS/gb+RJXtzzxdccWvxelP+r/uN1cbYBwHy73nxafJ+J8wtazEq8M32a4LtsbICs39nxl5c/ABLlQJvugWYzEP3bvy2E2K2LpgjaheYWXbsADm7jzJ+F16O4WYC/M2rUPrBrEwPDvq0D8T97eJa4CBa//W/3Af0Aj5/QD5dl+2WG8y9fYfsLgM8vT9j+8gbbX76H7d9eFzrgVNRxGOcAl1Valj/Pq0ENAFKUtd/4dQ+Qyxlb/yNI8I/zh0WcL37768y+POi+luNvD1SPn9iobvczLjZd6r/OFjAjP3/T1wW17lme/EVauEC+IAYAP1eJpkhBxWpnazVJnKYLLwbIA2re+KANLPppJvbbb785dhN9zp9Aji2exbCBwYKv4iw+fgSKBmkcRu3n3HejYvHT73/8tPg/i/9q14P4zEMGBebNX0DCgyaJC5B/XQaWAVcC5wNwefjr9z/ezA3I5KByAe/GwVw7580gfhPfe7e9xtMfUWK1cHxgc2DvrCzqFlSHRdy+LvbB4qu8gOl8a64fUdHMhXsulX7ujoCqDdT5aklQJxcNCNImAHW3a/wH19+c2n6ImAEgsNvfFsJWBtWqSMF/s5iPRWBzkcfA/F8j43kdEKl/ahabdxKvC3GO2EVp13YZ1fYbj8B++mUu/2/bAXF7kfv3z/lcpv3ZVI/0eZoHLAKWcd9c+nH2OWhEMhBZXvPO+7HGnmuq/qit9ee8eUsNu55d4YJSAZiGXezNBeM/3kKqiYou9R72A5LOlN684L155RGDX7uERzA9Q3rxFtKLP7U9zI+6p93cPX3u0CWCL/6/7bhmO9EcpzIcrTO7BSPq6uXpv7kDnf38bFoB14cgj1z91gC9g9w71n/O0xgEYz3+x3Plw+tva574CWziAYBSH/RByAFJZrqPjJi9UtezVezP+XtRARotHggKlALwAdJrjup3hvPdd0kjgBHz928NxiOCam82Boj6Rdk5KYjIwPc9xwaOaqPZne8+Bunhzxl+j2I3+pNWs9lBFAL6s29jkKeg8Lx+Bfrn3XfR/7Tx2UfNWx49ZgeSun4QAHL4s4Czm2ZnAvHaZ8MP9Pz0IALUyMp21t0BaQU0fV70a7/q4iZuZwh92tUvAaB/nN+fms5X/aEEmQSMBfKl7IB1Hxk2g08GuiQgA4hVkHBZnIOuARjlzQgPgnY2wwWA47e29knxcflNIf+RlnO5e984KzLvmTuIZzTb+fg9qug/ChNAL5tXPPj+faR95TbTnpG1AegIOL7ffbYar89u4dmOLN7pfvqHiernvzZ0Peq/8ecA+LSI2rZsPsHws2a/l+xXgGvwU9ZmLt8fZ2z4+C9jwJ84PY3wafHXpP0Tibds+bRAXpevy/nW6S3a3l7AONuPm8tHfL77OVf9bzgM2BcZCLfZlSPoF74WzfcloHKGNcAisPhZRJu59t5BuX9UDeCXz/n34T+nHyhKeTiHa1N8BwuP7gGkwtONX4sbuJW3gLc396OhP8+Ej2Rp/JdPeZemH14ASPp/fRac61k2h3wzD5QguUC397g1j5czggzt/PHPk7b0+GCnr6AaALRKm+/D8q0KzVX4u+x56gx0Ba72P8wQDkABRCzQeWY+Z57dgFAGUTzr1o7lrMxzbJwbzQfQf3kC/T8K9KcS8X1NeJT6RxcBMOrDwn8NXxeGJrA/5PG10/1HBiZoIGZaXvFprqUf3mAIvIPp5MPi66ABNHsb/R5Te96BqfrXeciZTf3YMn8Ae8Db101ff8lw/Je//UiuB1Z9mcPj6eS/l04HPZnfLl5Bkg2L92Vv2v71xPuILtHVxyXxEcUfFH9oK9C/x/59nozjwvtHiVT/val7rniEdQk+1e8XQHx4XzHrUa7nPgiEY9x89VQGAjBKZzicmT2Cxlt8J92PBGuBRu4/CqS9/UIAKtnMcO5I3pi4/2o/9AN2D0OAugOq9+znbwH0zY3Fg+8sGXB7+/yd5fcXkHL23Ma8Jd3b5AOWA5j+2MzdHAxgCjAE35+AAu79D8xEbxSbyAYdOCDpEOSawAk0QDGH9Ja4S6wQJEBXGIWtXZREUAJ31x6FYhSx9G1kuSSoYLnyMBcsIQPPBvSeQPVlbmLjWcpZRGCcj8Cn/rfb4JL3pt5Tndl2X0ew2QxvWv7+4qxwsJLHmz39fG1hCnHgC+kMtQVby/WQ3s2uZO2Y33qoAeerfX9d8WqM6UCt5Xi6bHttzzO5YMT6bu8sTTbsl/ugYoLriZRQn0MO25hqZFElevpu1Ml0SCYCFrGpuK+noXOvUlJZqc8yt6M4sHbmVgiTSechKY04PaXukMz/qtMSX1e1UOPhcMhR26imeo+fXOPEnlf7ACYpHjoQrOarbLo3tMTRTwyCKv1ZjLlom2b7QwfhxmpJil0qkWStIXVMpKaZDcf62Pon9kToF6kNbuu1Jg5QdxXU09G4lMbZ3EWqTST79Hodumu3H8mbG8tr0p8M9Wrzmk0foaJLqsTvDgnHXMO7bNfrYer3d3hbYgzjOUdmNSbuaPTnLa/VrG7z99EPAgzJKKnPySUZaKzUYzlG5G3Qi51yE/dafE+v6bVr7odaUOvsQJ2JRsLZ/qBcrU65OO6t3eOZEcXUUhcw+nxYFX4YsmeT2YeJdZtIGtVTjDmKRdRYch2zfnY7MmHihtvNoHWpBg1cwG7ZMlymphVvUNMyT4zX2xOOGRlc+AiR8IhSLZHN5sCxprrV9vSVsMZRkQajKu1tFhXYYZdlulemWaWeLlpKNDh20lEF2ndeojneprIgXroqmd7bfJBZLjLZQ2necpFlEG3MirC6nfXNcs1t9+11L9n6NtSm0z4lzPLEEMv7DkbJMdE1KuVM6URUTIXsqXPNSYXDndIqOJXuzU97cmD9KoSIuGj2ttYce+Go5KilnTFupVYmPzBwI1Aa6zX4LWBwQlxOgpOxQ2ZqIS8XR9HcERWYU8LDTrpzHMusYzjL1hZz2jmnYsQueb45K8eodrjoVJr0uXS4ZnPyOrQyL+n+gLGrwjWyO1ojJoGcVdCh+CPvrxNPNQj0lED38TiS9wPZXvB8PfhVmxxrnAtghgtj/4hpbCLGE16Lm9tSHrs64Aj0oKZ150+mG+rK1Ms7Um6n3ba6Yqmvx8lel+CGlIitGm4mV6d8S6lNwXdiAYY28H3Tw9nYjjDO36+DkGNrGFb2/QaFDbPhvQOb8GmzQpstqeEM3njLI69eR8tPL/LWV1eWtvMvOxpSYt2esOC+IyeuqDQ5NPua4KxIra61kKw8ySVkdORIkap2o63tpeR0O5/LeKXc1AaJdtVAbCmN3tu1K9M9a1g0UjAELokT7Tjjak13bDN2k9BwYn9p8dslrta8RaTizmzPhlVtjZBSbMmnpTuj3tDN2YDDKvMK7VxvmNaS914tryBPrWWRIYvDaryuw07XktTjNlZwwTKUrGC1rssV5k8wWUP22bXXd4hfX8uzwGgezktMuLrd8eRyijsROx6QkAttPF5TAs6dZSTfFcJ6FBpWYQ3uujnnEpGs+z27ZLTIYqfeRay2OO/jbkUf96fzgZFZwh4YSbZMh7vVejpxzRWut2o6hbsjLi1vBTfWLANXtDoV25WxS61VyGu4vR356F5DkWrVXWBYkMC2R/4ScJq+BOAWxDWTbfs86gVUUYZgJ69vSxdEsk3QJiA7OK5k5KQU3c1l22yRyvUOo2B14217ti96x91w5bwfp3AQD15y57SroXK91kIrIXE3Ake56BBtGTS/wyyiVm4O5WoSDAdGPQsdFeHBjcrIa1NCfnI21aVAO5f6TlbXq1wcxEoP5I6HI3L0MGmwvTxrcTZ3btzRFbxBiBgOzs+mLeeyx+1BSgZtSLeajCZYxlBZOUCxuKOGTke5atqECSENstxv1Iu6J1FVLPSjRp9I97QZQpG/3PfL5tKKJOxXnjNuE/VMHOnauGoKigwGpJ8yJc6O2lUP3Zto3OoLmzljpCiHJW2UBjIKKWuwDUuX+9Sj7nkjX5ba9XylD2xwgbVLLXlTx4XBJBuaZN50BW53KhxV9XnZm11yZSyxo6VdW5ruuclM/cTZXIFeqSC/DtAato0w5aJ1OJGqqBPisWQKQgmaSXf4dFc0Rn1kanHVy9BOTbS1140hb8L7YoP3PaHCfn/jVwwFB7Kesvja19DW8sqTFfFbH3LYZLs84iF6L0/F1kmnkxpXh65na/ZyNUKzwWUFU7aibqHcZQuCKOSWG6JvI3Pkk33l+itFwUBwTlqz9T09koUysiRd2EbYhjE4VcFLBBr1wdGFMjdHUPduR23p8VM55V3h0b5VaklSxb3ekOWKuuxRAPRnpImSlWJmeIBgnduYfdbqVrQ/uGnUrhAXzsu14jCiqzTOap/gauLuDKHwzo0EKe6hsAHXA9vgbi9K+fKyCrX9WrQ5yLOUu1CZO1ExL1uDVQwuJiIRs8f1Cs/w0FAFS15dMOZ6o7Vyd1kuoxLe0crW9S03AhHaUyR5u9A63YTXEe0qiD5tz8oJWNDfJBZXHHfltVTWpsQ2RXWs6DzaL9vO1LiO1v2cFcZlVvZGjEEWhyTb7HBGYDbnid0lLLesigdsrXDToMXaqDWSWCre4bqOuU1pQye7KaZGa9Q0mdb6lQEplAid2Z88oCOSb/cGPrW1ZEj0QTs6dI8R7v1CHysNr6OaH8krflT3wc1aIsVS3ZKuuZ2Ucd+qmNRdosyuk4otJruNEnt3pkz6TosMMU0WAvrPEy+HNzxDfdY+43oB+curtAlzJiqcSSriUsVASzDehwiqlcLg3eFgS3v4ohLM2ohb9bChRY8+6fvxrE+bGM8v+6ZTlQuGXaAE5rqTvt0oHSUF96u+VGmoktGDMuS3ekfumpohmR5BtmFgmarq9CVxubP84RZFXoaeCPyQIUKcHPuaOncOs8R8bgDwPIVs6e9a1M8PnelzPt7kBn8SuyOyN7MmPCgQIS+PNzFNkyPmXw7ygayTrWLGk1LikHae2JNJ2af4tFdqlrPCyjEsNUR9C6YtlkakwwzbF2+ZjVCENyO1UzfUejpAgYh6gTz2FOT3jN0qKW9f+bJTOv0ubDdRzCaGwMcxMl7jHrSUlsZd4z3XJpTIiTLh0KOo6Ligy+YavQ4NoQfrbbUXt1vtXhd2ZREFvOTEajdAA6IrG+eOITrVw9iJPN7R8hih+J0SVpuUKkk/KLuKvZ8LSL1D0lnVA2M30s54805pYDfxGYlhmVPOkB6XLk1wWnhYrwg1KsSiFBjxiPfdYeVz2VSNU4J0F4Me2EKiqLHV7jqPn5eoqvhIXW36uDD2THTQr/LpvPNoz40CV9L2zJ6jdyd6kA5SRpY3gyXq5J4P08Ycp12FWU3sY/LRNg8Mcx82xPbmlgEEHcl2RQVZi04mfdT4xmD3vSY1oN1ITAOO+4rNrQCedi0FSbsIh7KdSkm8NW1Y7L6ldyS32m13hLQVaNGadvCBkzPTdwPQhqEniqJZlr0ZyD29rIset4oLhTV22JfOcKiIDUuwGZPkMsD8/YlPBLQ1e5wuGaTTR608m/wh4oM2g2NjzNrgAJtOWzBDyTq3UEKTY9DA41GNjStlaAzpHmjOnhgMTlqBn2ihiqA9HYzFuGEIy4PInKNZRa3sLXfiMLyPWGg51uT1JB51y7+ei4jfEAK3TcWzymrk1t4gyvlwYab0DOuGFLv6dvKyq3wNSpKIA2uI+9Myvcck2igHhOD9FduLG3JdSwnad4rjeulpGC55owmHimy9QycqJ/0o983S0y+G4JKBBLoJ1izk6hwseavau+39lNjBzeSZq3lq7fjA7dZeXKCacZe3pXLxNA/WiQ7IwIqXwuWt01Lnw+192ruValkm4whonW3NOlv6KiiwKwMdl0g2nhzMFqzbOiDhljQ8uhTFNagzV3nZjKpDYtNwDFH9mB4QEoWPvb7WTm1QTacC2Zap67J0zCp00K/D/WYQ7jHrknIqhZETdURY+TsfcVyWya+tcA1ZZXNC1+MWPyKoVXlHjjgm/hW9bMi9zop8dMTgG7M5j9CyME53zIKHlhJx2tZSLTrhWnU55L3ORcnRaWVvi7LJcMLvvqFoTrk/UWFTHFwdDPqV4fEnP5RpkU88QcoIacdJCGiTr5MSKDTOZVbjINFF7cH40xS2gHDBdD3QECSXKXJxbjGYFWIwQyrktYWaFqk3rcFc2Y22svJNsymPbI/soXN+w22xWpckPYiiBy1b3IfJ4IIOlkRMqnA2+MhQc2ht3Vswdo4h6RQkYSz9WGeo4nK/XnsfPdnu7tTtDbaKAA1UhSt3k6kV1XK0eqYKb32jDljumuJ+Gzurc0AzYJLi1cjarMl+mLiqTqs7OdQxmBVyrS49I69WrRBtiCi0GZ3vvalM16p1v7KHdhggrVsRDXxE8sbofEvOGiyJVj27jUKLC0DNc9FoT2dNLLuuydvQZoWixF3a9H28thyQ47QMqgyd2z4DKePROherFJeaIBFToUF9QjHO3G7glWnqj5oedU6zTnM70OybR8TdRuYJJiCRImivWOxvsGPWTYcSik5oxMLNDm1WvLYKdtiG5EZPKtZqm4RTf4e8u3scz257rlpR4+8usk1gp55CrvOhzRrLV8RKIJrcpdDDre67XsK9o0GyZImQorkuMZzLTSSv+XPv3uItcxIqLZcrYnDoDcznxLjar6jVyfbse4ldK+KwLpBAaZCdokKpQxwx86rsdkciV9YClQR0xeyzIs6aC02htb3VPKVA9BVy8HgeT7gURpukBip0DUpbEztQ1sai7i0kRpNqBdJqWOdNYfXMBurE2jIp9JoS/YXasxdbHnK8Xh3ycIkTJo7zbdHDE4/BvEyorWYQ3bUmIRUeJqWeRIO8YEHOHEbqKlVbz+nONGnfOEHeNeb5OvENKKzZVlDhROFw3lqtvGmjWCO/TGyu28PRnqBdA7+N/YmVoWbgccpe+tw5m0LKcLYrNHP83dSIJlkdKi4sEIg8utJ6GKzY4eyuZXpZhw5rjEn9zPJAKuJlIRwYSlnKKOgREIzwTF06GH3dMawsYfbVjTiYk7SharacdCwlFl5qHoWujeUJOfdCBx3jiwEFcXLlI+J4oxR+QgSo5klBxCj1sl+GXMmEvixPNod56XV9IS/V8YJ5V/tGbgsdBMmloRqPQ5F+FxpVlFrVeqdx080RNNmBJq6GaQANnB4eUAfF2G4v47cp1QKGtRxGS4/JHkzogh6O8GWS0lhkpGFXcK68xEGNsTagicjVmwtJGzAmnwRF8cyzGC73k3K4EZNYjN5aWK73eHpDp0TId+j+6pseo6yQ8kBCtVXfcYndYXAgbta1Pk4xGJFT2eooUdjXqF+EiO5St113xXw2WuoXi/AGtJq60gu4ms+xXlZuBUYwPUPkt8PSQwlzH9dLoSA8dhJusmJuKbfI8PayQWJ8y7G+o21Kcum2uwZBlgfncDZ7f8mYHcuzHD8VO1Iwgn7TYpF4PuMiqjpmEI+3/mrd+5whKaIgeWpU0ct6qnW173YVam9dwjlf86TPeoTwke7I7213iRqSCrmtglI+VUYEf9kW2+ooEd50FbSRhkUe3l963TDERN6QLh7HfJFXZ7XYrMoKH4/ItOGznQ3hbYPKt00rX1LCSqbJQVSvk9ZQsxpWYsz7Fo63bjdPUd0lu/o8fDdDYe1UssxGd2RNeu4yuq7vQdbXvZMZh2wF8xzZY0pfRe1R3h7DiLSC0lUkmmhBt65x1nrXHY+KhilG71wGOD/kWX9WEe5G252kBLVwxSaqHEudGGpo7lwSbzjzqE7AxKFPLqF3PVbMOZWTrhBXFCqYd2hrXFPZaW3quDrh1Fpgz80263ZNhuHHWJM76I4yyqnBKQU/x/CGS5Ysn/d35cJ16l5c7vCRpbNYq2xrp1Ebw3U1CzJVP9gOY5CWZct4dX5Y85fgRDd66mOlo6I6ZFAkazUtzNEypqgFWcrSoKGHZFd4ibg8Q0eOcwxIkI2Bv5YaZRhyOZAuLB3ygMsQJzuvz+lm1bRHkFFBQjn2mj4GvRnzG7jOQKnmrRZNbVMgbOzcVmjj1CYEPqTefjSlxk9voJvAYbHeWXvxmg8dR0UXfttPpHItSTKVyCipa784GT17tjhIxgnu4ut70G2uPWfTc3BoqstNXyNhszLWukIL7W2Zb/wVSRergySQZpWI3Wp5OnJrevIlX8E3ENIRJ6Y2KbjCtqApaQXK8C8s7I/iLtxlkHhpdmSKnUadHnJKyrwz1WpCLKwVd8+jiuTTuho60tYNWgihiGBl7XZwQew9dOjp43lNXa6jy6GYbawi7A56+2DMu+S0Ra07dDxc67w1fEnSiETvd0VJqeegSHDNbtEhN8VwEDJNhPihsExMsqiJQ1cndH+7wAKb9T6lj2jtdWTs4LyRxltKpC/6IS+g3sWc7DYF1pWhpsqnx5Wy3oftNArKVr2QRLjHTjKR3Q0aDBmiFY2a52PZdLivbtYeiqDjVIZEgJN5VEst2is8xc2/Gd0H8QYdICUwTTZYIXFfZnjc90OAQ8iJrDxuDWPVEUYSU0CxiTjB9lYtZOimcNgJk5cnUJacFk8vYn0oUKJNkVVy3twR3WyHFAxjZ2ODBQR74CU0uK9hECh+e60wmsIlarDI1OlkG5P79Dj1sby6Rk7AXTbmEYbh5WZ3EvIctXrPHFeX3C09soYCR1Pu0T0H6ZPrl/3WOAUjKFi6Tp8Z3E7KsB+ZuqDxo4+iRbMSvRG5jMJmwOgeDG/Xlkb2fBySXV5qcsiEmAT7moTbp113Q0TUcRiTDHqoDWraZ/lOcvy17Tk500++eCCU61FFuzUG0NVJqquHg3Z+aEqROQvSXbLdLMal41CT5RWGJyxe4js3dAQcthQXqg7ikCWKebSGGkF4igQ9ZuDUicg1UKvgJHa7wwRv0E1pqzRNv3x4+XYQ+fLfeFBuPhv6HzuGep4mvT/g8jhz9W3v04PXp/+OkH/78FK7MRDxeRzXpF34doz1d4dxH//6QetMb3w+n/Z+0v48ym/tcH7S+yXOva5p6/FLU6SPR2DADqdr5qdBm/mBYRe8/+lg+U1R8NH2ns+w+PWXtvjyPJicj+PifH68xffib1/DtzPLDy/e2zH6F2xFfPHrctb+7bEJoDT2unzFXv74vzFH+XCxLwAA -->
