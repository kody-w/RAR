---
name: "rar-cowork-cookbook-ppt-exec-track-and-analyze-software-licenses"
description: "Builds a read-only executive PowerPoint deck on software license tracking from Dynamics 365 ERP data for a given legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_track_and_analyze_software_licenses", "rar_sha256": "4b49e6ce9bb4bcd28c422ca40a48c1eadef31aee761fe507b1de4b53b5a1283d", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_track_and_analyze_software_licenses`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_track_and_analyze_software_licenses_agent.py` and in the RCI capsule.

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

Track and analyze software licenses Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on software license tracking from Dynamics 365 ERP data for a given legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-track-and-analyze-software-licenses
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
      "description": "Prior period to compare trends against.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity to pull license data from, e.g. USMF.",
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-track-and-analyze-software-licenses-2026-05-24.pptx.",
      "type": "string"
    },
    "review_length": {
      "description": "Length/format of the review the deck must fit, e.g. 15-minute monthly review.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_track_and_analyze_software_licenses_agent.py` and embedded as the fenced Python below (sha256 4b49e6ce9bb4bcd2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_track_and_analyze_software_licenses_agent.py` first:

```bash
python3 ppt_exec_track_and_analyze_software_licenses_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_track_and_analyze_software_licenses_agent.py   # or on stdin
python3 ppt_exec_track_and_analyze_software_licenses_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Track and analyze software licenses Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on software license tracking from Dynamics 365 ERP data for a given legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-track-and-analyze-software-licenses
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_track_and_analyze_software_licenses',
    "version": '3.0.3',
    "display_name": 'Track and analyze software licenses Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on software license tracking from Dynamics 365 ERP data for a given legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes.',
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
        "upstream_slug": 'ppt-exec-track-and-analyze-software-licenses',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-track-and-analyze-software-licenses',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'fd105d5a4f6a4a41',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-licensing-and-entitlements/track-and-analyze-software-licenses'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/ppt-exec-track-and-analyze-software-licenses', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'comparison_period': 'Prior period to compare trends against.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to pull license data from, e.g. USMF.', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-track-and-analyze-software-licenses-2026-05-24.pptx.', 'review_length': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for track and analyze software licenses reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on track and analyze software licenses for a 15-minute monthly review. Produce 'ppt-exec-track-and-analyze-software-licenses-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads track and analyze software licenses data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on software license tracking from Dynamics 365 ERP data for a given legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes.', 'example_request': 'Make me an exec PowerPoint on software license status from D365 USMF for our 15-minute monthly review.', 'inputs': [{'description': 'Dynamics 365 legal entity to pull license data from, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-track-and-analyze-software-licenses-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.', 'name': 'review_length'}, {'description': 'Prior period to compare trends against.', 'name': 'comparison_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants an executive-ready software license status deck for a short monthly review, sourced from Dynamics 365 F&SCM without modifying data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecTrackAndAnalyzeSoftwareLicenses(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecTrackAndAnalyzeSoftwareLicenses'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'comparison_period': {'description': 'Prior period to compare trends against.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to pull license data from, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-track-and-analyze-software-licenses-2026-05-24.pptx.', 'type': 'string'}, 'review_length': {'description': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.', 'type': 'string'}},
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
    print(PptExecTrackAndAnalyzeSoftwareLicenses().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
