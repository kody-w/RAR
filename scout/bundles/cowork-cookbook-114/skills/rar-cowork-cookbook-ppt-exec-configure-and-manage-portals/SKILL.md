---
name: "rar-cowork-cookbook-ppt-exec-configure-and-manage-portals"
description: "Builds a read-only executive PowerPoint deck on configure-and-manage-portals status from Dynamics 365 F&SCM data for a legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_configure_and_manage_portals", "rar_sha256": "c769e2a829f0c376baeeb44b4dc75029413cecda69988e69e44020d0a096f4c0", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_configure_and_manage_portals`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_configure_and_manage_portals_agent.py` and in the RCI capsule.

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

Configure and manage portals Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on configure-and-manage-portals status from Dynamics 365 F&SCM data for a legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-configure-and-manage-portals
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
    "comparison_period": {
      "description": "Prior period to compare against in the trend chart.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 F&SCM legal entity to pull data from, e.g. USMF.",
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-configure-and-manage-portals-2026-05-24.pptx.",
      "type": "string"
    },
    "review_length": {
      "description": "Length/format of the review the deck must fit, e.g. 15-minute monthly review.",
      "type": "string"
    },
    "topic": {
      "description": "Subject area for the deck, e.g. configure and manage portals.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_configure_and_manage_portals_agent.py` and embedded as the fenced Python below (sha256 c769e2a829f0c376…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_configure_and_manage_portals_agent.py` first:

```bash
python3 ppt_exec_configure_and_manage_portals_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_configure_and_manage_portals_agent.py   # or on stdin
python3 ppt_exec_configure_and_manage_portals_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and manage portals Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on configure-and-manage-portals status from Dynamics 365 F&SCM data for a legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-configure-and-manage-portals
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_configure_and_manage_portals',
    "version": '3.0.3',
    "display_name": 'Configure and manage portals Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on configure-and-manage-portals status from Dynamics 365 F&SCM data for a legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes.',
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
        "upstream_slug": 'ppt-exec-configure-and-manage-portals',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-configure-and-manage-portals',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ec3c5215d53ce730',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-manage-portals'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/ppt-exec-configure-and-manage-portals', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'comparison_period': 'Prior period to compare against in the trend chart.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 F&SCM legal entity to pull data from, e.g. USMF.', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-configure-and-manage-portals-2026-05-24.pptx.', 'review_length': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.', 'topic': 'Subject area for the deck, e.g. configure and manage portals.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for configure and manage portals reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on configure and manage portals for a 15-minute monthly review. Produce 'ppt-exec-configure-and-manage-portals-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads configure and manage portals data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on configure-and-manage-portals status from Dynamics 365 F&SCM data for a legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes.', 'example_request': 'Build a 15-minute exec PowerPoint on configure and manage portals from D365 USMF, with charts and speaker notes.', 'inputs': [{'description': 'Dynamics 365 F&SCM legal entity to pull data from, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Subject area for the deck, e.g. configure and manage portals.', 'name': 'topic'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-configure-and-manage-portals-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.', 'name': 'review_length'}, {'description': 'Prior period to compare against in the trend chart.', 'name': 'comparison_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants an executive-ready .pptx summarizing configure and manage portals status from D365 ERP data for a short monthly review.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecConfigureAndManagePortals(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecConfigureAndManagePortals'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'comparison_period': {'description': 'Prior period to compare against in the trend chart.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 F&SCM legal entity to pull data from, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-configure-and-manage-portals-2026-05-24.pptx.', 'type': 'string'}, 'review_length': {'description': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.', 'type': 'string'}, 'topic': {'description': 'Subject area for the deck, e.g. configure and manage portals.', 'type': 'string'}},
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
    print(PptExecConfigureAndManagePortals().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
