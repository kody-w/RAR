---
name: "rar-cowork-cookbook-ppt-exec-troubleshoot-reported-incidents"
description: "Builds a read-only executive PowerPoint deck on reported-incident troubleshooting status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_troubleshoot_reported_incidents", "rar_sha256": "b8b8536b818e2487e4ba31459cf0bacacc01e350ba2e688102c404e05608b881", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_troubleshoot_reported_incidents`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_troubleshoot_reported_incidents_agent.py` and in the RCI capsule.

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

Troubleshoot reported incidents Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on reported-incident troubleshooting status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-troubleshoot-reported-incidents
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
      "description": "Dynamics 365 legal entity to pull data from, e.g. USMF.",
      "type": "string"
    },
    "meeting_length": {
      "description": "Length of the review the deck must fit, e.g. 15 minutes.",
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-troubleshoot-reported-incidents-2026-05-24.pptx.",
      "type": "string"
    },
    "review_period": {
      "description": "Reporting period and comparison prior period for the trend chart (e.g. monthly review).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_troubleshoot_reported_incidents_agent.py` and embedded as the fenced Python below (sha256 b8b8536b818e2487…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_troubleshoot_reported_incidents_agent.py` first:

```bash
python3 ppt_exec_troubleshoot_reported_incidents_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_troubleshoot_reported_incidents_agent.py   # or on stdin
python3 ppt_exec_troubleshoot_reported_incidents_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Troubleshoot reported incidents Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on reported-incident troubleshooting status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-troubleshoot-reported-incidents
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_troubleshoot_reported_incidents',
    "version": '3.0.3',
    "display_name": 'Troubleshoot reported incidents Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on reported-incident troubleshooting status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.',
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
        "upstream_slug": 'ppt-exec-troubleshoot-reported-incidents',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-troubleshoot-reported-incidents',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9de6251d212a8618',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/support-systems/troubleshoot-reported-incidents'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/ppt-exec-troubleshoot-reported-incidents', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to pull data from, e.g. USMF.', 'meeting_length': 'Length of the review the deck must fit, e.g. 15 minutes.', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-troubleshoot-reported-incidents-2026-05-24.pptx.', 'review_period': 'Reporting period and comparison prior period for the trend chart (e.g. monthly review).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for troubleshoot reported incidents reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on troubleshoot reported incidents for a 15-minute monthly review. Produce 'ppt-exec-troubleshoot-reported-incidents-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads troubleshoot reported incidents data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on reported-incident troubleshooting status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.', 'example_request': 'Build the exec PowerPoint on troubleshoot reported incidents from D365 USMF for our 15-minute monthly review.', 'inputs': [{'description': 'Dynamics 365 legal entity to pull data from, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-troubleshoot-reported-incidents-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Reporting period and comparison prior period for the trend chart (e.g. monthly review).', 'name': 'review_period'}, {'description': 'Length of the review the deck must fit, e.g. 15 minutes.', 'name': 'meeting_length'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs an executive-ready incident troubleshooting deck for a short monthly review, sourced from D365 ERP data without modifying it.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecTroubleshootReportedIncidents(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecTroubleshootReportedIncidents'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to pull data from, e.g. USMF.', 'type': 'string'}, 'meeting_length': {'description': 'Length of the review the deck must fit, e.g. 15 minutes.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-troubleshoot-reported-incidents-2026-05-24.pptx.', 'type': 'string'}, 'review_period': {'description': 'Reporting period and comparison prior period for the trend chart (e.g. monthly review).', 'type': 'string'}},
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
    print(PptExecTroubleshootReportedIncidents().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916adObWLLmX9G8N2Kq6mJbgBAIT3TESAIBQmxCiKXc4WLfF7EJqKn/PgdJXqrLfad7Yj6NHLYQnJN7Ppnpw+9vdtdGZf328U317WLB2FkWR369sAtvsS/vZZ2CrzJ1wN+FWxZtHTtdW9bN27s3z2/cOq7auCzA9l0XZ16zsBe1b3vvyyIbF/7gu10b9/5CLu9+LZdx0S48300XZQGWVWXd+t77uHBjzwdP2rrsnMxvorJs4yJcNK3dds0iqMt8QY2Fncdus1jh68Xhv6t7YeHZrb0ISiDqIgQ8ikXmh3a2AJTidny3uMdttOBl7h2g6xfeu0XcNJ3fvFvY7ixx89DQrirwLB4WTQZkaBZVBhg2lW+nwARF2frNB6CoP9h5BQR7+/jr39+9xeD67ePvb25mN+DWm1y1NFD08p3055du3Eu12VqZXYRgdTUCcxfgd+XXQPgc3PL8YPH69XPjZ8G7xX/+Z3q367D55eOnYvH6fHqb/5y7YtFG/qIt7QYwWLh2ZTtxBjT+sNhmd3tsgGHbrp71AwasgR0/PHd+o1RWi7/Nz35+MvkQ+u3Pn95KIII9W+bT2y8LYNVPb3U3X3+YqVQ///Ihm3348y/f6DSdk/huOxMDUn/4/Pr9IgsWflsaB4vPqkzvX7xq340rHxD/Tr/58xT9Re5lks/PxT+X1bvFjynP+vwNyPuMRwfQ/TFZYAOw8+1DAuLw5xePugSRYxeu//Mv/4ysG4GIzeKm/Zfo/vokHIEkANZ6meSXdw/3/X0BvXT7SvOfs61AwPw7moDlX9h9NdQ/o/3w7D+QzuICJMAXX/6Q3I82QH9b/PpPdfuvNrxbBJ/eKD8DqVvbIHE+Ln5/hMivP3nfbv709z8A6f8jGbXsavdB4XNuF3HgN+3nz7/+1Dxu//T3X3/qKhDFvp1/7ursRzR/ZNcHnz9Z8LXq5z/vBfy1Ii3Ke7H4mkOL38vqv9V/fFhcbQAs3+43HxffZ+L8gRazEl+YPk3wXTY2QNbv7PjL2x8AgQqgTfeEMYAf//EfCyF267Ipg3ahumXXLoCD2zj3Z+EvUdwA7HugRu0DuzYxMOxrHYj/2cOzxGWw+O1/ug/Ef+++EH9ZVe3nGcU/f4/Nn79A9+cv0N389mFxAfTLOg7jAoDweSvLnwo7nGEd8K5qv/HrHuCVM7b+e5DW7+eLRVwsfvtXWXx+UPtQjb89kDt+4uB5z80Y2HSZ/2HWVo9AIXjq5oJy9qxA/iIrXSBVEGdzAQDClBkoSu1smSaNs2zhxQBlQFkbH7SB9T7OxH777TfHbqJPxRO0V4tnvWuWYMFXcRbv3wP1giwOo/ZT4btRufjp9z9+WvyvxX+160F85iGDIvLyDZDwqEriAuRal88qL2ZHAyB5+Ob3P15GBmQKUJ2AJ+Mg9p+bQaymvvfF4iq7fY+u8YXjA0sDK+ezLeeKGrcfFlyw+CrvqwjPtSIqm7k2z+XQL9wRULWBOl8tCWrhogEB2QSgtHaN/+D6m1PbDxFzkPR2+9tC2MugMpUZ+GcW87EIbC6LGJj/azw87wMi9U/NYveFxIeFOEfnorJru4pq+8UjsJ9+mev8azsgbi8K//6pmEuxP5vqkSpP84BFwDLuy6XvZ5+DxiUHuOA1X3g/1thz/bw86mj9qWheaWDXsytcUBYA07CLvbk4/I9XSIHY7DLvYT8g6Uzp5QXv5ZVHDH7fCXxtcxZfA3lB/6gtoua26FOHwgi2+P+1lZqNs2WYM81sLzS1oMXL2Xw6be4sZ7mfzShg+pDmkaDfOpwvKPYFzD8VWQwisB7/x3Plw9WvNU+A7Gpg+PP2/KAP4gxIMtN9pMEc1nU9J5D9qfhSNYBKiwdEAqsCzAA5NYfyF4bz0y+SRgAY5t/fOohH2NTebAwQ6osKOACEYeD7nmMDP7XR7M0vLgY54c9pfY9iN/qTVrPVQegB+rNrYxAvoLJ8+Irkz6dfRP/TxmejNG95NJEdyOT6QQDI4c8Czm6afQnEa5+NPNDz44MIUCOv2ll3B+QS0PR506/9Wxc3cTt7+2lXvwLY/X7+fmo63/WHCqQPMBZIkqoD1n2k1Rx4OWiDgAwgVEGW5XEB2gJglJcRHgTtfMYIgMGvvvVJ8XH7pZD/yMW5nn3ZOCsy75lbhGdQ28X4PZRcfhQmgF4+r3jw/cdI+8ptpj3DaQMgEXD88vTZS3x4tgPPfmPxhe7Hv0xKP/97w9SjwGt/DoCPi6htq+bjcvksyl9q8gcAZsunrM1cn9/P0PD++4R//xc8aP5E/6n6x8W/J+OfSLxy5OMC+QB/gOdHp1eMvT7AJPv3O/M9Nj/9VJz9b5AL2Jc5CLLZgSNoCL7Wxy9LQJEMawBAc/l/YH4zl9k7qOyPAgG88an4PujnpAP1pwjnIG3K78Dg0SiABHg672sdA4+KFvD25jYz9OcR75Eijf/2seiy7N0bQEj/Xx/t5pKVzwHezHMhSCXQvLWx//j1wIuhnS//PC9Ljws7+wCgH2BT1nwfhK9CMxfa73LlqSvQ0QUc3s2oDSAAxCfQdWY+55ndgMAFMTvr1I7VrMRzCpz7xgeqf36i+l8F+lNd+L4AzBBYdXOX9CgTIN3eLfwP4YeFpgqHHzLKfX/O/s/AzmEb/ZXV6XF/xr9XVxr798flo6LlHWhFgrh9cUHWCwAc3WsW/wuvr53yX9nooCmZhffKj3N9fvdCOfANppt3i6+DCjDla3R8TPtFB6byX+chafbtY8t8AfaAr6+bvv4HiOO//f1Hcj2g8PMch89o+kfpxBniXib4ABJ5eMbsbOy69DrXf+n/r+b4exRG8ffw+j2KPcj90FpPW8+zdVx6f5XpGd0zcD9XPJEWWMCu4waUowrcrL88+wKNj6ZgzsC6Xfz8EDkHQR9l48uzv/xAkocooLSAAj3b+psTv5myfAyfs9DA9O3z/0p+B6HV2nMcvjLtNb2A5QCJ3zdzl7YEmAQYgt9P9ADP/q/nmhedJrJBPw0IORtns17hzgbZ+Ci2IXzMsVcItibdAAZV3nZdGPFXa3CN+vhmg8Coi8GYD69xGOzcIIDeE4s+zy1pPMs2CwZMArzr+98eg1veS6mnErPFvo5Rs/Iv3X5/c3AMrGSxhts+P/sliThLlHDOtQMZ8GbI7q2rOo1a2GcRPly7U1Wbl+jQpEMldWW/56etJll8XqWxrmzMM7WVCVruaGi8EMVFpOw0OreV2HVE02pZok/H+9pdrTfrjS/I7sbp991oVweud/FRi5Rxwip1SPksNatMz6sByg7M1U4hlWV0wy3i00GseG2devsC2jj+Mh78q5pzrXK7Cxia68esiaDBodv97pTf0ZxU7NiTLQPX6lKI7/XJsg5tRBfodHFvdHw6rbHNIV4uSWg12APDWmqs6ybdXskwOZiZG5np9ni9dkfoyGd6P1SEaNDk/mpf7me1a3m8TLkSOWb8JRLNgc0l19HOOH3Z8LtDke+owu3vWmTGk3arli4bQpcgKI4ktFlOHm6mWBDI3XLrBf2hPdH6tVKvI3t1CmmfT8f+eK4rTdPW3WF/DBQviJuhc0uk24arEFbauKZMOdEu2Xg7k+ezcOP5kY+pcQMFxYVaa7wXhs2thge7USOu3Ycucm+22aW1VHxgWXqHZGVBh6luqEdEN3SH9hPRWtYav6xIYuI4/n5P1LNGM9fDheNMjO05I73GvK5v9jwTuynKW6Ke62oFbHo27EFvdQgk89lzyhS+XS97ldjfDqNInHF3MCdDrBnD0jtbOQhZJp2PBtN0VGbStGrjigsDxU5Cuz+plYqaQxXKpGi0fHRAmcqlL1OlTullbai3WLkyq4IPTiAWu7Rg1wyU7ciJsQ5XC9Gt60DdunHSHGZ0hL0FmUc8O1Hm7RqEONYKU2NsqcT0jtsGj0pEkfN82WqqYqJheT+y6XmjLSdliOHG395XZmnsrgofJQ4TnSp9ey2dvNk5XofeUDPjjuONRBjeMx0PvzLeldYKzijj1fLAalcmiKVTz8dpvxn3mAEdIGHVlPeDB4Es0RmMA+PO/WZRSgPxS8UUT2Rvr+45kusWThZnzVVOHNFLCXESU/2gsdB1LamakJ9uvuwhUyChqrjx/VhbJjB/DVc6nbN9KS+3rgmBySGTYRlLYr/vowiKNWYHeePRP6Scl9Jtg6HNvlBRxGza9MhGbnUKrmd5756ut5DiTIqD6M6D+vJqmLvYSSOTqUv94sBGLRzQs+rXgmukOJXlBHxOhaNi6HsOjVrhogv+vtFpxmCz3Zreqkhz93f+3u52K4W7wF7NcM2KRrAdfWxGCXax5uIOGLY7xR4bIbC5hJFqVx3VbbbjMTXMbpWiilpp6+lOK+Cg3G97NF4ma11Kl3vnuutJsTiXI10mztRa9fLqH7gAGUK8CC6XywnxDcysE08zlLXBHMyhY6CwMa27e2nOd01PaQqHqTuj08VS9RSNgCwG3cqlPyggU3aMpltU5kghsu3o3Z5R+4IcNIZQ8CHTAWAq9jhy3jQiMQ3ZXYOKp3NBaSI2kVfONJjyoKrJfUmjB6Xqb2khHDlDC91xqW2LgnIZpeEP/Ci5sBz4CHrBzxiAsk2ClahfLFPcFa+sdIDIdr8d4t3VbVYbgcUs8WDE8TiiazdsXciyICZCqpghqfgm8TTBcCwrRpFUasS5ckPWrmn4MCpL6xgN5dXOagLRCwsTGGiD7qL9dqyxZYacRzfrJuEuX5k7jQQnAE74Bo1cgpxzZizVvAhP8ak72X1KS7dMbyUcGsX1aS3hpDzpW5Ihku3OY7eFq1ZDYY98Ke2SVXKmhfZqkXm695Vbml/vqxKVglCJ2aHbFjpo3A52Ui4P8bChxYhOegU70Xd2L9FKfCeSGNg/Sac2FazewpGgD46CjCZnPkqTXcKODApWpCgBKVMub+2zdG+l9GL0DhqGWXrBYg4/luoWA53XLeeGXWX2HrlvWwmDVZtVKJu+eYE1XOSxoBzpKPdb9XqDNapQ4KDgocE/XROD6eJVAyLYE8cxssVDGqMSv9dwqHeuGz93WtylZf4MFTuB26wyLdZMK2gm1TmJbOm6Oq/eXSSQSXYyFGJjD+FkoynNkoJlyWyCQAxF4tA+2eBNQdX44KHa1d+S/maTy8dDeC5D9H7cbihxnKhzGu30k+XebhEXYug9SICnbw4rbw+TOOz6FD8n1nUbwSG9jFd7htVPZ1Xk0R0R56EP14pjctRg5mHIBRXn6leQuWbW5jAVDpM14odSEC/JSr2muCiRlqUaBQJngyzrDijLGu0pmCkh4bC6QxqaTZN2Pl0YfCndDVFUZLhf7QZVQY77qM/OR6X0N2xqKTphWm66VUHaOBsxW92UsJV62BxdhbudndUQGEq1DRu/C1NFHo/btWjkvOzWFerETnyI9lwXwHVXJjSb2fSQYUni6pTKWWsvEroRzP+Bq+d7hF/Tp/pyDvyrz6gccQ642rhV+4wUuCqP7xjv8ufz/irvRN6Lx/VZMcIyHRWYrk+5mScQ6yNU2qS6ronCvj0E4WHPRNyVDTeJeLb78+6o246KknuqonjQJ9xTdXK87GC3AitqFbw+YMydvW0p0IycjAPpabg6JBR2Isz74RjHvKAFmdec0LOptfyaO+7ytddMGsqZobEha+1KrXkeofxR7Kkw83GktGuzkRy08S9ao1VrWBhCQWEvjA0jiC2Ux+PaPdupqPNXQrlullWOMbSrHuJeIGK+OvRNf8x20R06KbWmwtORZ/iVKTrb6340uHTX1ciOSuhJvDjF/szclaGJw6Hu1uSOFDd6yuxDAm8upHnaqDQUC5JlgkyJGUJuIpoQyuZwsAIDdQavqJBhy0mTfNmzYmNMmCYyCcshnoEUNkof671IhtJNTenKZ1uAcFOUg8l8uc81gxK7G9brbBmvFWidw/yAHNoGZ0b7uD2uTzSvMnv5UpWIep1EniFVAEXbY31lKSWtq+IeOz21Dk+3jmdMk9EaxRwBHkZlNbBMppAudsJrnoz3qrQ3zzLf6bpy30gKkp6EsqR2NAGjtN9kR/iSkPIgMMJlC7tZZa7rZeGmF23rU/SE1FQeOKcUXW319KAoacPjh1vm2TK5S+xwEzQevbKa0iGqbloSMDTexJsCJjIlYNQxvckrUa48Pt3wsMxZcseo6uYUx5JKLblVjOl4zVme2E/rYiffXbWOQ04FXbEPouJGWTzF7SqWGYaT0d5LR25AHyjebJPl9tJmQIw+Z+NyDLt8rPd6EsRX7nrbxkxla7mlhddKv6vSMVNJLBmVrYIxFnnSxnuNVKq9FkTSnbxbqSw7hBDS1rPzXX5wlSzOOdfZH1OZ4A8ktAwCVFV1NK04DlcZFRdaFtWXIOfygwnhVHowQNUqRmrc5pCa9gWmSzv0MFpmFO4tLWWr3X7PxKdVVFEs3QvnZoLspmxMHtqlqaNqRNRLFbbxZbYcg2CHQV10Ona+Y3A8RvE7KbuytniZCs9XsXXSOTEo5if4OmzX2AHybgPajhij7Vo2pZD4WNgKH9QW02WCbFZB60qXpFxFDjQUmVNNG+d8kLDgfjvH5nkwYjpszpDKdXo6uM24vWiUTHO3a9WxVZLYAmbe9ic41YRDM1zFwxnOb5MptMdElaxDaCahxghwpnC0S8Oqs+1OIZ/cCyjRSCfKkBgTg3i8TTeEzvtIwFmESvYegW53os+uusia7MkrDCeJ16AOHTZFcaxtY3uQ1q0iohlUiQ7URxieA+zDI6hVJs6D8GBlBJ7dRCPa5OdwyQqiMDYXE6ZtkTUJRjetadvyORtFR4QUdGx9aQJP6JaCdDhdBLANtSgzdVfcpqGPIErZcmMtJ9OxwfjjKY20hZdMNxAust+buBGbOzD+bOLpeM3aoKdvScVV2cqCHLeApJ2QImItdpS6E05RqqviwPnwZlTzTbW69VkW9US7Y40OGdYNciB3I3HzmW6729Ki7ovtMaUsu7bso8U5Z1ztT1bE3m96lW4YPUjttdb0h/229nNkubkEk78W/Ejd5jtaOWBIkEqpEfhW1uyryBg4lIaHgacpddRTvjsOewOBtZtm7SCFWUsUZbV82PehczIQcq3Cu004YthA7oeObRziAuYTGUh/8Db1toDHZZNU98sBMW7J2eDzy6lOSJMjrDBecly/hzF4T9dRZZ23mYVDRWJSO+lO0at2FaheRCyrPhF2Xp0c6SFVlmmeiBTeCayXCAUn+zuSxlT5rClxAe12aX13o6FWz6ZxsRFB8+AAEsCAKbGHyqKiQCouCJR5ary+2Q7aKwNJtxmrYA6hjUWC5UFKLK/dSh3vUb+n0n16YW9eStWNJzHb7Ghf2FPlrO01oR6y7q7EqT5i0NEM3LgUu+F2t+XNcXX2UtAPKkzYxoNeHn0xzsbmNt44Cy1v3jGMr2Z9lDQUgdzUqZ0Tqa4UgZ6gXXUIrlgTpP72oDrxXU8umdp5DNrY1O7aTGPM3pwq0odDBloRPfCnK+Ykq/LqI9sSQZf3xIxkYUMxnqDml4u4Y7vjqXCMo4WimQCtKmflUTefwAwTjfogcqYQQ2Qfc4rrAY96wyrFo09EkwHVPp7h8A4KvMxGT7C73lv4SCRdK/gNHuqDJ02XEGGhcC/pQuuvZZKxLhPQECZRpGudkuVOJExey5WaDkV0QSeNpCAeF48TuiZEH1oeaJEQ8wmnWIRYmpqtXSKmEFZlnNtjd4/2m4tyvvgb4FDd2w3yUvOPpNP6cbLRybFfBTSgo0uNThJkjkro6JJyoge2JEEWQdDO1Th76LUlADgmexKkszMyrmLd0TMHs22zJBNiuaQCUglVbQ1Zzpp0lnGByYUYJRbRG9n1GjctJ9cVfzypfr5j2Aw9heWYkKII5QCfguiS3XoOX6mbzoP3Gheo59LGEihN0t39cioKH9175PomDvY6s/NKn+Sz7kToMfdEat1Eenmj9mCGQdcnyZXcYdjEF3q6x1S1vEJ2rPcX2F/TeJCKjBb7JeUQAQ4RBMnXhxWzKdrlVjASK3E7JQoy0HZZSgiMmDuxScJFQLaZmJKSMxF1XOaFXJQZc152arlEd0nAG4i5WUf55lYNdLpFuJRaryEMQ4kmkSf2Qp+tk40gsdDgRXyvxXBiEMQ5uctVpNc5ot7u5NaRXHcSyKIQTsVyK0aYBZ0OlhzIORYuY7NLj64JXxqLS29urOTbjXSioAQnUYyPFY4UhsjvauZA+tomu+FjcsdNqeQEMPwkt3vlMqZg7wS5UOTkKE/5pCUxzLJo6AjF5Zrh1vrc6NlJXmYl6ctUmfpLYh3Kh7y88uZKYFPSK+j1/eZPKzrPiIxTgkmaJqHDnf3y1EhXJbg6yfG2RkhsGiUc9UW28839KLJeZMUnfJPwknEEGk7wupAN/tiuLqvu6Azsrhdrq1yhkihuVgh8cI6t33qasDJUA0zuq/Jy2vXOtEWJMK5vG4qoCMmLtL735UDIu2UKNjNe4dWmQNRgaVtXtr1z16227rNCj1AROrb8hROkwF9StGucNLHfFb3Qb82QL/ISukQg/e4njl3CwWbQpPzGJYJPScOQGYjawyCGMzWPpy1hNFvfJDvCY7Y41OITibOBfmKlwG1RvC4IkZ9q1AShZZB1tuIBPGI3C1m1Pb7M7VCurIAOQDteicHSrY5o2/aXoL83Fy/BV620snaJhuAZTbZiTZ4SvAUtb9s3mo6F4uZcNVt7w6A5cUbFzcQTCF6joLYekfVYO7C2ai7oahXJBWNMBRbUO5mvIDOQK8UhJEUqw6vupbLG3A6kDVLa93e8MBbkWPokJGDJpj8R271YG1cuSPVof2oP94LgDoPrcyZvBuPuwjPJVEFXgVItjlidsWMHCXSWwq4a42dkPXDs3UIyuMjPm2s+4hf9bOD3MZGIbUPta+dGmna6zFh/CIh90feUCG/t4xqeGsULLcpm1pQH+pJIzBt56HCWm+RTX+TRRpIdGdqbKzNHazfs9/dSvra1Dry9oVG03+5Twk5VrBvvg1aPkKvD9TjlRos4dlszONJntV0ZqpAlNQu66CaG5Mm+I+NFtzZO1JvQJTQqsnLXBJ5VS4CRhV9eHA0ig8PgYzpj6mcO1Gnchi4QYV5W0HELt019SHt8c78o1dFmK2lPptLurCWdJaU653grrUmJSDKyYmTZbkBWaXNpnRVUucsiqPEzrkk2veRwwV/ex6XotRTRIqvdiRoMBGData9DIRQE1T+vysbdbNNkC7kqBhHTiUCXsAwzSyP1e5Pf7Cr9hCQGt6pZr75Uhkd4fbtUfRzunLGj6hG1CSI0wvra2TnIHl42r71+lOkODHMVEpmbgKMpQxu8PY6Ww9I12mFD3k6oPG2t06pX3LaW18y6gParI5eKl610GM1RrHtZWVcYiqCe7PI9xbCqHNKHrjPJ7fGQ9Ok2ce2l4+yUPeukqE+sRYTwHcHYo6Jbrxss7DIqWya5zzT4yiZDFitxY+dQNCpjrbglTcwLsvUhuPRDZfijv7Hh21R7JJatcH6JVB3XGUt8CvT+bMlLJhT7XijKlczFDnk/CN0q0WofNB9rlS9xqzrZ+LRkNzwuEbJpn+JVENybld1hiD1duz0xeutNu5JWro746/5UM8tDABN7FLIicWCJJUTA8HRYT1kNy/NB4uqgg17PCBhSysRsU2z2SHExue3t0K+lk3usQi72mRvPUVC0G9aSeurqGysPdaXpbsdhRLpaO9tze8TPEp/csADZQimt4rCTGyue2dgc6QegGCfGnlhmq6WVIBa+Z6BOD1z87Kzg5O5eGTzyThSDT6sTdrIV/wzROUnypZrFaMQqGS1TkLH2XGKJQWtod7mL4w4jYpIOLHjnetrtujOPBhMgd7xrAyIiDoEC6xM6yUkryWD0Y82co7oMFrbb7d/+9vbu7dtR4Nu//dLbfDL0/+wQ6nmW9OW9lcdZp297Hx+8Pv77ov393VvtxkCw58Fbk3Xh6+jqH47d3v+rR5kzlfH5XtmX4/PnuXxrh/Nb2G9x4XVNW4+fmzJ7vMUCdjhdM7+x2cwv9brg+0+Hty+lwKXtPV9D8evPbfn5efA4H7zFxfyGiu/F336GrzPJd2/e62z88wpff/bratb59Q4EUHX1Af6wevvjfwOxZ28JTC8AAA== -->
