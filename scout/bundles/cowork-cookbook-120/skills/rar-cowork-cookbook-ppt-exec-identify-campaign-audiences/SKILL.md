---
name: "rar-cowork-cookbook-ppt-exec-identify-campaign-audiences"
description: "Builds a read-only executive PowerPoint deck on campaign audience identification from Dynamics 365 ERP data for a named legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_identify_campaign_audiences", "rar_sha256": "57d638b17936e3f96dbe9d9d7c3e3044ab824201757989e9c81cbbf8c691ded4", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_identify_campaign_audiences`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_identify_campaign_audiences_agent.py` and in the RCI capsule.

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

Identify campaign audiences Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on campaign audience identification from Dynamics 365 ERP data for a named legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-identify-campaign-audiences
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
    "briefing_length": {
      "description": "Length of the review the deck must fit, e.g. 15 minutes.",
      "type": "string"
    },
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
      "description": "Target .pptx filename, e.g. ppt-exec-identify-campaign-audiences-2026-05-24.pptx.",
      "type": "string"
    },
    "review_period": {
      "description": "Reporting period and prior period used for the trend comparison, e.g. monthly.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_identify_campaign_audiences_agent.py` and embedded as the fenced Python below (sha256 57d638b17936e3f9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_identify_campaign_audiences_agent.py` first:

```bash
python3 ppt_exec_identify_campaign_audiences_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_identify_campaign_audiences_agent.py   # or on stdin
python3 ppt_exec_identify_campaign_audiences_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Identify campaign audiences Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on campaign audience identification from Dynamics 365 ERP data for a named legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-identify-campaign-audiences
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_identify_campaign_audiences',
    "version": '3.0.3',
    "display_name": 'Identify campaign audiences Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on campaign audience identification from Dynamics 365 ERP data for a named legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-identify-campaign-audiences',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-identify-campaign-audiences',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e3d01d1b479f3554',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/prepare-marketing-campaigns/identify-campaign-audiences'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/ppt-exec-identify-campaign-audiences', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'briefing_length': 'Length of the review the deck must fit, e.g. 15 minutes.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'output_filename': 'Target .pptx filename, e.g. ppt-exec-identify-campaign-audiences-2026-05-24.pptx.', 'review_period': 'Reporting period and prior period used for the trend comparison, e.g. monthly.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for identify campaign audiences reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on identify campaign audiences for a 15-minute monthly review. Produce 'ppt-exec-identify-campaign-audiences-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads identify campaign audiences data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on campaign audience identification from Dynamics 365 ERP data for a named legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes.', 'example_request': 'Build an exec PowerPoint on identify campaign audiences from D365 USMF for our 15-minute monthly review.', 'inputs': [{'description': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Target .pptx filename, e.g. ppt-exec-identify-campaign-audiences-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Reporting period and prior period used for the trend comparison, e.g. monthly.', 'name': 'review_period'}, {'description': 'Length of the review the deck must fit, e.g. 15 minutes.', 'name': 'briefing_length'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants an executive-ready PPTX on identify campaign audiences status from D365 F&SCM for a short monthly review, without modifying any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecIdentifyCampaignAudiences(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecIdentifyCampaignAudiences'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'briefing_length': {'description': 'Length of the review the deck must fit, e.g. 15 minutes.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Target .pptx filename, e.g. ppt-exec-identify-campaign-audiences-2026-05-24.pptx.', 'type': 'string'}, 'review_period': {'description': 'Reporting period and prior period used for the trend comparison, e.g. monthly.', 'type': 'string'}},
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
    print(PptExecIdentifyCampaignAudiences().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
