---
name: "rar-cowork-cookbook-ppt-exec-define-security-approach"
description: "Builds a read-only executive PowerPoint deck on define security approach from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_define_security_approach", "rar_sha256": "29fd84925593e6d36baae497512796492062eae5d21a4cc8f9bba9d306fa7799", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_define_security_approach`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_define_security_approach_agent.py` and in the RCI capsule.

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

Define security approach Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on define security approach from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-define-security-approach
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
      "description": "D365 legal entity to report on, e.g. USMF.",
      "type": "string"
    },
    "meeting_length": {
      "description": "Briefing length the deck is scoped to, e.g. 15-minute monthly review.",
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
      "description": "Target .pptx filename, e.g. ppt-exec-define-security-approach-2026-05-24.pptx.",
      "type": "string"
    },
    "review_period": {
      "description": "Reporting period and prior period used for the trend chart comparison.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_define_security_approach_agent.py` and embedded as the fenced Python below (sha256 29fd84925593e6d3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_define_security_approach_agent.py` first:

```bash
python3 ppt_exec_define_security_approach_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_define_security_approach_agent.py   # or on stdin
python3 ppt_exec_define_security_approach_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define security approach Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on define security approach from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-define-security-approach
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_define_security_approach',
    "version": '3.0.3',
    "display_name": 'Define security approach Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on define security approach from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.',
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
        "upstream_slug": 'ppt-exec-define-security-approach',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-define-security-approach',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '106156c1ecfdae5a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/define-security-approach'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/ppt-exec-define-security-approach', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'meeting_length': 'Briefing length the deck is scoped to, e.g. 15-minute monthly review.', 'output_filename': 'Target .pptx filename, e.g. ppt-exec-define-security-approach-2026-05-24.pptx.', 'review_period': 'Reporting period and prior period used for the trend chart comparison.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for define security approach reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on define security approach for a 15-minute monthly review. Produce 'ppt-exec-define-security-approach-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads define security approach data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on define security approach from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.', 'example_request': 'Build a 15-minute executive deck on define security approach for USMF from D365, with charts and speaker notes.', 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Target .pptx filename, e.g. ppt-exec-define-security-approach-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Reporting period and prior period used for the trend chart comparison.', 'name': 'review_period'}, {'description': 'Briefing length the deck is scoped to, e.g. 15-minute monthly review.', 'name': 'meeting_length'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs an executive-ready PPTX summarizing define security approach status from D365 ERP for a monthly review, without modifying any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecDefineSecurityApproach(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecDefineSecurityApproach'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'meeting_length': {'description': 'Briefing length the deck is scoped to, e.g. 15-minute monthly review.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Target .pptx filename, e.g. ppt-exec-define-security-approach-2026-05-24.pptx.', 'type': 'string'}, 'review_period': {'description': 'Reporting period and prior period used for the trend chart comparison.', 'type': 'string'}},
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
    print(PptExecDefineSecurityApproach().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916ebOjVrLnV9HcFzG2H1WXfasXHTFCCCQ2SYAQyOUos4NYxSJAfv7uc5DurbLb1a+7I+avkV0lBOfknr/MrMNvL27fJVXz8unFCN1yIbp5niZhs3DLYLGqhqrJwFeVeeDPwq/Krkm9vqua9uXDSxC2fpPWXVqVYDvXp3nQLtxFE7rBx6rMp0U4hn7fpbdwsa+GsNlXadktgtDPFlUJvqO0DBctWNKk3bRw67qpXD9ZRE1VLPipdIvUbxc4RS6E/22s1EXgdu4iqoBoixjQLBd5GLv5Iiw7sP3DYki7ZAEu8/DDQt5vPyy6JiyDD0Cc4GOUu/GHhevPorYP1QA38DQdF22eAj0Wdd63i7YO3QzoXlZd2L4CDcPRLeo8bF8+/fzLh5cUXL98+u3Fz90W3HrZ190aaMg/FDHe9Fi+qQF2524Zg2X1BAxcgt912ADxC3AL6L54+/VjG+bRh8V//mc2uE3c/vTpc7l4+3x+mf/T+3LRJeGiq9y2C4OF79aul+aA1etimQ/u1AIVu76ZFVu0wD9l/Prc+Y1SVS/+Nj/78cnkNQ67Hz+/VEAEdzbJ55efFsCun1+afr5+nanUP/70ms9e+/Gnb3Ta3ruEfjcTA1K/fnn7/UYWLPy2NI0WX4z9evXGqwn9tA4B8T/oN3+eor+RezPJl+fiH6v6w+L7lGd9/gbkfUagB+h+nyywAdj58noBkffjG4+mArHjln7440//iKyfgBjN07b7l+j+/CScgLAH1nozyU8fHu77ZQG96faV5j9mW4OA+Xc0Acvf2X011D+i/fDs35HOQdi2X335XXLf2wD9bfHzP9Ttf9rwYRF9fuHDHCRv43p5+Gnx2yNEfv4h+Hbzh19+B6T/KRmj6hv/QeFL4ZZpFLbdly8//9A+bv/wy88/9DWI4tAtvvRN/j2a37Prg8+fLPi26sc/7wX8j2VWVkO5+JpDi9+q+n81v78uLBcgyrf77afFHzNx/kCLWYl3pk8T/CEbWyDrH+z408vvAHpKoE3/xC+AH//xHws19ZuqraJuYfhV3y2Ag7u0CGfhzSRtF+D/GTWaENi1TYFh39aB+J89PEtcRYtf/4//wPiP/hvGw3XdfZlx+8sTn7+84/OXd3z+9XVhAsJVk8ZpCfBXX+73n0s3Bjg8M62bsA2bGwAqb+rCjyCfP84Xi7Rc/PpPaX95kHmtp18fIJ0+kU9fbWfUa/s8fJ31OyUA/J/a+KBkPatMuMgrH4gTpQCvZ9RvqxwUnm62RZuleb4IUoAroHRND9rAXp9mYr/++qvntsnn8gnT+OJZ01oYLPgqzuLjR6BXlKdx0n0uQz+pFj/89vsPi/9e/E+7HsRnHntQL968ASSUjJ22ANnVF2AZcBRwLYCOhzd++/3NuoBMCQoR8F0apeFzM4jOLAzeTW1slh8xklp4ITAxMG9RV00HsH+Rdq+LbbT4Ki9gOj+aq0NStXP9nStfWPoToOoCdb5aEpS9RQtCsI1AOe3b8MH1V69xHyIWIM3d7teFutqDWlTl4K9ZzMcisLkqU2D+r4HwvA+IND+0C+6dxOtCm+NxUbuNWyeN+8Yjcp9+mWv723ZA3F2U4fC5nKtuOJvqkRxP84BFwDL+m0s/zj4HzUkBkCBo33k/1rhzxTQflbP5XLZvge82syt8UAgA07hPg7kc/NdbSLVJ1efBw35A0pnSmxeCN688YpD/R93L+ns9Dz/3PJ97DEGJxf93fdJsjqUo6mtxaa75xVozdefpprlfnN35bDFn4WexHin5rYt5R6p3wP5c5imIuWb6r+fKh3Pf1jxBsAeiAtjRH/RBZAFJZrqPwJ8DuWnmlHE/l++VAai0eMAgMCdACZBFc/C+M5yfvkuaACiYf3/rEh6B0gSzMUBwL+rey0HgRWEYeC5wUJfMbnz3LciCcE7kIUmBg/6o1Wx+EGyA/uzTFKQjqB6vX9H6+fRd9D9tfDZD85ZHo9iD3G0eBIAc4Szg7KbZqUC87tmeAz0/PYgANYq6m3X3QPYATZ83wya89mmbdjNSPu0a1gCmP87fT03nu+FYg4QBxgJpUffAuo9EmjGmAK0OkAHEJsirIi1B6QdGeTPCg6BbzKgAUPetN31SfNx+Uyh8ZN9cs943zorMe+Y24Bndbjn9ETzM74UJoFfMKx58/z7SvnKbac8A2gIQBBzfnz77hddnyX/2FIt3up/+Mv/8+O+NSI8ifvxzAHxaJF1Xt59g+Fl43+vuK4Av+ClrO9fgjzMmfHzm/sf33P/4nvt/IvzU+dPi3xPuTyTekuPTAn1FXpH5kfIWXG8fYIvVR875SMxPP5d6+A1dAfuqANE1e24CRf9rKXxfAuph3AAIAoufpbGdK+oAivijFgA3fC7/GO1ztoFSU8ZzdLbVH1Dg0ROAyH967WvJAo/KDvAO5h4yDufB7ZEbbfjyqezz/MMLwMjwXxjY5rJUzCHdzmMeuA1asi4NH78eCDF28+Wf597d48LNXwHKAzTK2z+G3VsxmYvpH7LjqSRQzgccPsyADZIeRCRQcmY+Z5bbglAFUTor0031LP1ztpu7wQegf3kC+l8F4udS8EfMf1TqRxMAsOfDInyNXxdHQxW+S7sIwznFvwCbxl3yV+ocQKhoxoDngoc+j1I191mzPjO2vjFByY8AHOberADWS/I5V29pOHyX8df+9688T6DxmJUIqk9zDf7whmvgG8wsHxZfxw9gyreB8DG8lz2YtX+eR5/Zt48t8wXYA76+bvr6Dxle+PLL9+R6gN+XOQCfYfT30pmglwu7xSvI2nHxvuzNAv80kz9iCEZ9RMiPGPEg8F3TPK02j8dpFfxVAD187/2eKx55UoOr5v0GiL/gK+Y96v2cYSAeAOqAoE9b0Fj9lfGDMygUoNzOdvzmoG9mqh7j4iwjMGv3/NeN30AMde7chbxl0du8AZYDXP3Yzl0WDIAGMAS/n5AAnv37k8gbgTZxQSMMKGBsFDAEi5Eki4dUgFOe64YES5MoRrMUeIBQWOiGZIChLuH7TMR6nssGOEJFLk2zLKD3RJYvcy+ZzkKRLB0hLItFBIohARAEI4KAoRjKJ2kMcVnPJT2Sdb1vW7O0DN40fWo2m/HrUDRb5E3h3148igArN0S7XT4/K5hFPQhXvLGz4RKBxs29NrMUkbCMbqmARzV6ne9crS5PcVZjqEj6y7hdHfT4sFpxxnQXWxzZRtd1dFage5cH+DKR22SPZ9Vwl7aboMWiPWn7fY9v/TO+bC10nSZniSuOkWDeknN+DaCWW5cbeFWlGqn453M4wUN7OUurjXqLjdv9TsPMoWGqiq/tQTdo1peqgjnS21ucJeYxNiOOdM71qTzhImPAYyesLuPo7UridropBB2m2vIWKYLsT9PIteh63CjdiGwLzj3vx4119JYGNJbbFC45bJcIglJrw7L0VpTRYOi4TzjkdJSK5bg6Zehti0ArztpU1iFNkTa3Vh4rk4UirbDMj0M+R1k4sumJ9XtcYqKUlHqcZCGa6FExTTltlQ5XWFGcWh0o1bLabXpc7eGdfTze94x8WxK8ZBLqPuJ7oGR0I+kmC/ttnbpOEB+47ChF8ZGc4H3hDfsp1FUtrX3fui59idw4mhp5eyQ7Zbnl8Lf05g9WkJqpplxW9Eru8usOz1tIa+4eIkKygO6HLJM4Kds5yeokL0noOF1iecwukg91nNYaa63NKFPgatmCJGqNrMd7hB2wvRogxjnQ4yPUJLstvcI7s4HueyUsnPBYZXedG6+9JEvagbwMgbJO0stZ56/JndDPwmYipaNW+C6xgTzBM+vaYteYLEHyZk86Y1GvVldP3JSypzS+GRZmh8TgQaBy8WmdS2fByuTKQ7VIsMRJyFtY2pDxhbDVDl0bhL1Z9liQwonjspDqlGttk+r10WTQk8Rd3CHih2Tl6PDdDG1E4T21htpkd/Ov8ZEXMXRln7plY2DadmXTWm11uqxfrvvMqHIt7ez2RJ5OobFMwmndQ3I/WLsolRV0x0wdUwuBAq9YUWCl/ahFscLWS2ZtjDvCVJP4FJFFpRYdhGomYReUskU3A7bCk9TZueTBuwbu0bMUtZdls4Qt/kaifAP+1GRG0SGNjsxG7LRV6+zJXh4hJmETPoA19ZzBlepfru7tVrNQeg55ny5OzIqKLksQymjrrKe8lUiHrpwtM8UV2iIqE9H4bmmqzkWGDvFGvm+CgWvodZXa8EET0ela8BcJ6yf9fMQiCQNOd/v8cFSMw3I69IJ1LPh6vV2dGkpYc8OSYfh7Q56J0q5Sb3nCV0d/LVq9oiZnjb8IWnEmnGA37tlNtawZ2yNyy1NR8Sp2O1HXLlPH++x1oPeuyFWyXpFrctltmfhG77fjUbi19J2iB0YX0yo10ERFrjc6dZworL3zFYM2wskLfRvO64Ttj4PRbg22se8WV92FmCidJm4F34jzbRRwcJqdxyqAzp2u4Th+INBKvYUyum7vWlFTSzdb0aeDo9nUjQnkds3VepiscgnW2p5fqZyewuZNBaMYMtaYwoysXDI738pCs1uOJ+zsbMsgXl0Cg7Ikco93qiac9SyzN3F3iB02oIlUJpku0o8Cdjv6KqzbxHWSzzJJnBnZFxBv6PstwFG8zzGf7LV+v7f5AwlNkL8+896yczd85jpmcVMP28aUo+G2W8r1HqnQi2GflaTN7AKR8/ul2t09RyDohnfXqws8wCIaTlnJmhWMV/lSufYnZIDREb21FNup97YdL2IZb468X56inJBT2tZ2bMjuqCCKoJQniN0tOniEehjw8b6enL2BNMIWh3ehuzaa65qx0z2V2YISIluiyEdi5bUsCik2KezuF2qdMlBOxmtTMMQ7bDM7arPvtmZS6yJ9UU7ice22hcjubLyh0vteWocGsm6V8zVR08u+Pl9Ox+kUb6nrYbRMGemoASSaJG2jrb8q7eyQbm/mectl/rnAw3AgU0OtLYKDVtMIIag8uM0QkDbdL8lhcCpxSggsV3CR6k9G7k7LAGv5gN5d8mSj5qVIlYKYqvDtQgUbSRv9kuNP5F1Q2jV5mVzLkPRegA1JQ3okTMYhrrftvQ33/obzJtoLEk5EcAfjCDaE78gp4hzuejvkoLY7aFBkucppKswclaWw9If4BEuUv9+7F/KYmVv0dAWJ6mB8EnHQ0qHSus2Yva3igsakEHM6ewKA1P1OZg4HWj+PuN4ur2098I3siCgf+0fRG5jEkDfCurwe+WWHXDONc27iaVlRCRHtqgI5TRO2VunTaKjILrytVtrxVpBBcVBP43KiOcgOh2lyoetScMlo59gi3lh3kOnO0kCElVE21y1RX/GAX6qVzCK7XbTabh3jTnK43R/O2u6WHSYhVca4IZnCrY7D+rTjzcTx8QNCFGu83Qe7pghSvtvqqplfYIHVODdWO11clwARwlWquzkR7KjbqrgpN2g7LZHci0O9vMK13DHSZqhyxmqmnZ9b6nJMY71aRsZ4QCyFVGU5G0nJOSjWMjPi9JJL9ybc5iDie/ggnK2TkJx16KBt5UN8DDeDixk0kZvrqM4HMoOR7S47bo1Jca4mJyDHs34tHCzQKyklVksAevoYhnW+gnAQj1vQNgpx6xjx2OaSbSeRZkCxlefHfnXOXQgztTyON4SFqo2Ybm1vPSwbyBSuQeilW7e4EsrdAN3mud5MVXDjnOUq9Umqke9osDX1SYjF0oi01U2WNgpUSgdVJtYrAIDi+jxhsEGUR5nlcckn9aW5zsAgSQwNs5SClGB4klq2xSqjsEheGec0hTiBu5z6kQWophr52o0TStzD9RnbLiOn0a4nbRzcXX/1x7Vt54nQ1FeqRfA1djtPY2wO8J71zgFjyc6RE1eljB1Bb6pYO6HtOFasBuN42/b3jNIUfWBxoYWSs9oTss667sQbfJPdD66Kuafkeq7jbCid4nBeuSK7KlOoNtWs89Cq3SLDqj3a0LLuLhBH9swOW/ZXfulBl9w4EF0sVXdeN/MIFRIKjS85QxPA9cw2WiP1oT/ClR4ZFpGcSZ4jqs4vnOaeFWLqlxIjXfSLAzK9M3Y7GA0yzsi7oeo9i8wGpQ4rfytlsbwV8tEylsht0sVMoxkpcVHyYMl0chtuNExfYs2IK36KzbTwSeHcwxXthdJeJbkJs4lkDZA8a66GSW+xNJbRrNV6806xuCYOKjMmy9Y+JopRZYTGna/WttCWYhIItjL0ZsAjPs42TnXdwYoReHSBsCfVtk6sbh1uYl8Lx9yN3bUkX9l62xvnVcuFXAX0vrKxenZEbZAyi5UtNpDPW4Vh8PxKZFTH0d5B2RW14cRny1xu1tWq9jpstH3bQ+k7DXyJ7pXJqYs2OOksZ4ZJnJWVzgymwPZDsHOlvrqK992uPBJm0qYg35xaMwWsYUmRQWMpN+w+W2+3bnXDTktiHNauD6/2txWiVHiQQdF+00zevqmoyJRy5L5E9YwHEx8XoIJcBPZQbgIZ3nXlRoHjHbmKwwOXJKRl+ba15/V6y9FZbHFxkivxsaDwe3YhUcYlugo9QS0kN8StZzdkyCCuaiCOmyfX4YZQ6PISRwcNP2wvp5Rs9WrP3nmETtP0mBxlejWcI+Iygta/x/TBoHWMghm+b05ijKg5QIlEyRoJja8RyiQwonGdmTpgCJka2qb2rRMJ8Danw5hcKVgX6HiJlY2UeNe7XUCnW483TnDxxquTVFwrCXta6EYArfEZFcvtNPCQs3Jvu3Y4kN7B3g7hBT9tDPSm6dspvKiWCBWCutnjCc2ZKBmmiu+3OA4K+BrbLPMxPZyzpWD5W/UMuow1e4grJt+Pw3jBJhz1EMVT/Z1yhnbU2fSsxrwElcaRdUxL7nnqA4ogTEcmeNnqagQjy6ObEoN8Ppn+FfTQTVDGhqooNkEak7VsPOTUbG722U23naXUt/NFIQThfm6pcuv7h1LCUVSuqcPddtnLZCPhsTvs7uvdJu2qg6d1Zb6XkXJ7ZeAah4gTzQf3RmOPx7RhRKLvpTNJjV6Ze3ROlWWgwwk3HmqxpDi4jtut5QfHZXcNx2N1DYDDjJMt5o6wtMMKoFDnM1d2bxiK4zdhsrXZI4dhuuUeuHyJ7dprXCIofCbMqBVrS6+OEJ7yDeghIf4Qu0exCBChm6q1dFrBpzRIbxa7K4YwQxy1O1g+e3Q2N2ISGXU9XSgL4cik1PRreLWTilgvWdOJOI5aHwrXxKQxKRXc6TZ7rN/Ghig1hnRCN1QC2WYQEzhTS71677I9Tq4HkQ74CLTSN/bMVLp47TGEXEGaDWGdWvWYX/penCnLTTbRt2Pnlpx5GxmPgKf1JYVIKsRNu9REQbMnfFWS2JHySw9nV+xI98yphxGP2dAHFgc2UhxIP8KdGY43V9L2xuGi6421cuOjJLiYqUrJplTEMZSgrajrFyaqBKJpm5xHLseblkRijl9PV+nOit0hakvsIlyFUwxRJr46CbZZ1RmcKdXkAot0l7Dq4yLTdluKh7xaV91cjjaaqoQNn2bUfdpZlykgQl3el8huwPkdm3l8TKBbl3DNY01LeaHboOx1CFmIU1igFGZPFKWi7SY7Y9LFjoLQumPIEeFQsymvAWkqxGrnCvvT9b4/b5DN+doOSuTfLYWj8eNOvwvkDvOotbcJJ6WMmklC3G0Z25jR8fuERNgrGuQRC68iyoXWimPWpUpJICPq+7oKJzd1Y2vZXh29klUqbbS9ZyhI6yW2sQf+KLL9hkVdMAmDTpu+dnc0dAhKO9wJt+lMJ/Bh8a61rpNV6obAA6EAcCOW/B0H02HbwLAaRcyBtY71pONQGsHjHhZTrjtUXS0IbDBgyXFJjZKCBpMO29TEC5ejeSBLjjYEHIEGjT1cl8GupksVPzBLrT5gSKsHPAfKpxQPI74RlT67iwSABEq2yksZHWkRsik74i/V/sSKmzT3KwtUHF8DM3Wm1qrrRepySd0Q1vDdnTeSmNPTcb5k8hRdwzANQs82c2ydRdFo4EwsR4GWZNN6Q26RMrW20ASvpVDZ94WXN14v3a9KaAW+trsLK3RTuwILhj/ycASADYdJ1yvNPAdM27U9ETsRvzdxs7tj0NZwVwPtncJKF+xDAWKtK+pTfyH9E3TcH4nrIPEeyzuXhD7jFRuSXuCM6Zrfs/KdZMgVLJz9JhkSr1lerHqbCafMSBmRo04BEiXXU38wuPIiqApdo6B9zNvtua/XMFqY1WolhtoWU+Vy56+w1ryMlTuuaWKsU2t0+Rs9aIUZXydfRaqAdzM7mpBobzfTuLEC2LFWBL9dWTdt1DEPly6XMbCvW0vH14eBLoIycYI1JkAnhgIQ5eCHu3lRWMSOz0iqnvFTZJ0NRMNzbJt48fZCUnzilNesRWPk4smU0Rj2PXS4u9wH4rny9lXH+iOGnG3FLC5BW1/l9U7e4+VhU/jxLbyYtxUI3IFw8+sZUuSdW98keD+C0m+cNpjKha5/b3Q9cmrTPMU+rejnJrPMzZ3Caz8eUB70bGZKeVxOsZ6yua+Q5VFHed6XSIcJh+Ve2rCEjxiZY2WRQPhb6EJvb1dtWeh6WMqGzA5gtF26QWC3Hj/eTmXX08rdzUFz1hkBA43BSRNHHkaZCLvaPhH1QmarN+1KZy2thXgvHWABtTSMj3zifMpvN9Q/Nn7EBGd7z55Q/p6F1HTE9iodKJeixgsksQrCgJOAONS5Wqzyi7SRKkS5e+ipcxjH8prTTjztKG11JwmORJqYxZvyFpmrfdsEzh5ogA33NZcWXhYd11eLdGjk7O+GRKw9Bq0gkleJBr419+VKuNigDGTFuJO7JQyzyJq4gXFH8BViSeYrnURg+SRWKhCSbzcApgl/oidZD0B/WcU84UMDplxYZl2MlEHp9ok1bjLOqV1YeWsCUgzvruOt5dMC6Q1wsJQvN1Olhb0jHk5JeMAPOFGZ5JVnvD6ZVHbKh1sFsrtoWLrQIKW74lsFV2Ue8dyxpw16pXXK4NcM6iotT9uIIDP9CXetuh6VAmo7Eb10nUe6mHxELpJDjJS487a3hMFazU1qtddGnFG2wxmBEMhhWEe5FWeZxK87TOPWOHSy2K66ra4r0Yyh/LaFg06iaTJ2DdyaJpGVfalaVx2PlFxo2FxFmYW6OXFrraeurqURZk6emaQuhQrP/LD1NlPjT2bUuAF93LkOfLvK0O18h+XrKWEnuob7gfGZWmX7aZcuJ9OddGPHCvwtXefZBjT9CgS7kL9nd2cuQi0RRYjbUrQm1tPHjsIKpEP57tbbBZ3fBN2WapsjqO7ah5SOn1GFqncoN12wXKak8S6gDlvu2g3PT9wSjCx94ntHEsZSDE+8U8pemAF4lqX4vAOt6X59H3akshauLjcU5k7vQpKFpWUB9XeJvljOYaQO6jLu2HGz5eTWR+L13d0P/XBcJhih2f1kekED0IaoxMJiAtXcHEYMGsu9dgqiLow37BGMXB4vHPfOdb9kLdq6JbUQ2cEoRDvfxsirTFAF6nM0K0QUS/ORB8YaXI2qtoG6g4jTCI0oZXzQRmZViN50FW6eZPmScAwsBG38WithMuCDEh6IVX8rGUXDmm7Xnit8STGbXZVTJEZfTjnGk0l1J0osdwr8rkqiDEM+GoqFt1OqW9gzOWJDuItPJX2mm5UAV0TsML1yyFaVSIOxINEQ7ngYLM3ilGy0zXOdKCadNlWBN7ZxyAh/pJG6JIqYdgwkc6rdJqGO/GTo9/DiGxB5sBt909AMQEOX6EvYvqHJXiivWw8izgHdCDfzsOfIIy1zWMvYDa6CWnPmiTWhn/HjNZWLjbNGd/bBV4QIvQ8tfCNxQtst8a142e1RSYV1oSAG437XZIKG7Y2GsgW2aU/VVOVlkdzsIwNxgYTQdNIf5yOXv/3t5cPLt3O9l3/99bT5uOf/2anT84Do/X2Tx4ll6AafHrw+/Rsy/fLhpfFTINHzbK3N+/jtIOrvTtY+/tNTyXn79Hzn6/3Y+3mQ3rnx/DL0S1oGfds105e2yh/vm4AdXt/O70+28yu2ABvaPx26vqkBLt3g+cJI2Hzpqi/PQ8XwZX7FcX6XJAzSbz/jt/PGDy/B22tOX3CK/BI29azs20sLQEf8FXnFX37/vz7KdFHMLgAA -->
