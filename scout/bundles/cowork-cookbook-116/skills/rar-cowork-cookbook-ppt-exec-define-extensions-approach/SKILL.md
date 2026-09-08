---
name: "rar-cowork-cookbook-ppt-exec-define-extensions-approach"
description: "Builds a read-only executive PowerPoint deck on define extensions approach status from Dynamics 365 ERP data for a legal entity, with KPIs, trend chart, red flags, actions, appendix, and speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_define_extensions_approach", "rar_sha256": "10172870bd575cda52699046db7ee0b9831a6daba6bdc12f0c4e499235cb79e2", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_define_extensions_approach`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_define_extensions_approach_agent.py` and in the RCI capsule.

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

Define extensions approach Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on define extensions approach status from Dynamics 365 ERP data for a legal entity, with KPIs, trend chart, red flags, actions, appendix, and speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-define-extensions-approach
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
      "description": "Prior period to trend the KPIs against.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to pull data from (e.g. USMF).",
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
      "description": "Target .pptx filename, e.g. ppt-exec-define-extensions-approach-2026-05-24.pptx.",
      "type": "string"
    },
    "review_length": {
      "description": "Meeting length the deck is scoped for, e.g. 15-minute monthly review.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_define_extensions_approach_agent.py` and embedded as the fenced Python below (sha256 10172870bd575cda…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_define_extensions_approach_agent.py` first:

```bash
python3 ppt_exec_define_extensions_approach_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_define_extensions_approach_agent.py   # or on stdin
python3 ppt_exec_define_extensions_approach_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define extensions approach Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on define extensions approach status from Dynamics 365 ERP data for a legal entity, with KPIs, trend chart, red flags, actions, appendix, and speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-define-extensions-approach
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_define_extensions_approach',
    "version": '3.0.3',
    "display_name": 'Define extensions approach Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on define extensions approach status from Dynamics 365 ERP data for a legal entity, with KPIs, trend chart, red flags, actions, appendix, and speaker notes.',
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
        "upstream_slug": 'ppt-exec-define-extensions-approach',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-define-extensions-approach',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '41288af9c7ec030f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/define-extensions-approach'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/ppt-exec-define-extensions-approach', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'comparison_period': 'Prior period to trend the KPIs against.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to pull data from (e.g. USMF).', 'output_filename': 'Target .pptx filename, e.g. ppt-exec-define-extensions-approach-2026-05-24.pptx.', 'review_length': 'Meeting length the deck is scoped for, e.g. 15-minute monthly review.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for define extensions approach reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on define extensions approach for a 15-minute monthly review. Produce 'ppt-exec-define-extensions-approach-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads define extensions approach data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on define extensions approach status from Dynamics 365 ERP data for a legal entity, with KPIs, trend chart, red flags, actions, appendix, and speaker notes.', 'example_request': 'Build an exec PowerPoint on define extensions approach from D365 USMF for our 15-minute monthly review.', 'inputs': [{'description': 'D365 legal entity to pull data from (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Target .pptx filename, e.g. ppt-exec-define-extensions-approach-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Meeting length the deck is scoped for, e.g. 15-minute monthly review.', 'name': 'review_length'}, {'description': 'Prior period to trend the KPIs against.', 'name': 'comparison_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs an executive-ready PPTX summarizing define extensions approach status from D365 F&SCM for a short monthly review.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecDefineExtensionsApproach(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecDefineExtensionsApproach'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'comparison_period': {'description': 'Prior period to trend the KPIs against.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to pull data from (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Target .pptx filename, e.g. ppt-exec-define-extensions-approach-2026-05-24.pptx.', 'type': 'string'}, 'review_length': {'description': 'Meeting length the deck is scoped for, e.g. 15-minute monthly review.', 'type': 'string'}},
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
    print(PptExecDefineExtensionsApproach().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916adeiWLbmX7Hf+yEzLxHBDBJ33bVaZRQZBESkolYkM8gogwjZ9d/7oG9EZN7Kul3Vqz+1Mahwzp73s/f28NubN/Rp3b59fjMjr1oJXlFkadSuvCpc7eqxbnPwVuc++LcK6qpvM3/o67Z7+/AWRl3QZk2f1RXYvh2yIuxW3qqNvPBjXRXTKnpEwdBn92il12PU6nVW9aswCvJVXYH3OKsisKaPqg6QAFubpq29IF11vdcP3Spu63LFTpVXZkG3wilyxRn6KvR6bxXXQMJVESVesYqqPuunD6sx69OVrEvdh1XfRkD8IPXa/gOQJ1zFhZeA616wCLt8aBqwInt8eOrZNZGXA52ruo+6T0Cz6OGVTRF1b5//8tcPbxn4/Pb5t7eg8Dpw6U1veg5oxj4V4L7Lv3kXH+wvvCoBC5sJmLYC35uoBRKX4BLQevX+7ecuKuIPq3//93z02qT75fOXavX++vK2/DGGatWn0aqvva4HSgRe4/lZAZT9tNoUozd1QLd+aBfTAZu1WZV8eu38QaluVv+53Pv5xeRTEvU/f3mrgQjeYoovb7+sgCm/vLXD8vnTQqX5+ZdPxeKvn3/5Qacb/GsU9AsxIPWnr+/f38mChT+WZvHqq6lzu3debRRkTQSI/06/5fUS/Z3cu0m+vhb/XDcfVn9OedHnP4G8r9jzAd0/JwtsAHa+fbqCmPv5nUdb36PKq4Lo51/+EdkgBdFZZF3/T9H9y4twCgIeWOvdJL98eLrvryvoXbfvNP8x2wYEzL+iCVj+jd13Q/0j2k/P/hfSBQjc7rsv/5Tcn22A/nP1l3+o23+34cMq/vLGRgWAgtbzi+jz6rdniPzlp/DHxZ/++jdA+v9IxqyHNnhS+Fp6VRZHXf/1619+6p6Xf/rrX34aGhDFkVd+Hdriz2j+mV2ffP5gwfdVP/9xL+B/qvKqHqvV9xxa/VY3/6P926eV7RVZ+ON693n1+0xcXtBqUeIb05cJfpeNHZD1d3b85e1vAHwqoM3wwi2AH//2byslC9q6q+N+ZQb10K+Ag/usjBbhrTTrVuDvghptBOzaZcCw7+tA/C8eXiSu49Wv/zN4ovvH4B3d4abpvy6I/fWFzF9/IPPXb8j866eVBUjXbZZkFYBeY6PrXyovARC8sG3aqIvaO4Aqf+qjjyCjPy4fVlm1+vWfoP71SehTM/36ROXshX7GTlqQrxuK6NOi4zmNqneNAlCwXjUmWhV1AASKM4DaC+R3dQHKTr/Yo8uzoliFGcAWULimJ21gs88LsV9//dX3uvRL9YJqfPWqaB0MFnwXZ/XxI9AsLrIk7b9UUZDWq59++9tPq/+1+u92PYkvPHRQNd49AiTcm5q6Ahk2lGAZcBZwL4CPp0d++9u7fQGZCpQj4L8szqLXZhCheRR+M7Ypbj5iJLXyI2BkYOCyqdse4P8q6z+tpHj1XV7AdLm1VIi07pbquxS+qAomQNUD6ny3JCh+qw6EYReDWjp00ZPrr37rPUUsQap7/a8rZaeDelQX4L9FzOcisLmuMmD+76Hwug6ItD91q+03Ep9W6hKTq8ZrvSZtvXcesffyy1LS37cD4t6qisYv1VJ7o8VUzwR5mQcsApYJ3l36cfE5aE1KgAZh9433c423VE3rWT3bL1X3Hvxeu7giAMUAME2GLFxKwn+8h1SX1kMRPu0HJF0ovXshfPfKMwbZf9y7cH/W87BLz/NlwBCUWP1/0ycthtgIgsEJG4tjV5xqGZeXg5Y+cXHkq7UETJ9yPJPxRw/zDae+wfWXqshAtLXTf7xWPt36vuYFgcMiobExnvRBTAFJFrrPkF9CuG2XZPG+VN/qApB69QRBYEaADyB/lrD9xnC5+03SFIDA8v1Hj/AMkTZc9AZhvWoGvwAhF0dR6HvAMX26uO+bT0H8R0sKj2kG3PJ7rRargzAD9BdfZiARQe349B2rX3e/if6Hja9WaNnybBMHkLXtkwCQI1oEXDyy+BKI17/acqDn5ycRoEbZ9IvuPsgboOnrYtRGtyHrsn7ByJddowZA9Mfl/aXpcjV6NCBVgLFAQjQDsO4zhRZ0KUGjA2QAMQkyqswqUPiBUd6N8CTolQseALx970xfFJ+X3xWKnnm3VKxvGxdFlj1LE/AKZq+afg8b1p+FCaBXLiuefP9rpH3nttBeoLMD8Ac4frv76hY+vQr+q6NYfaP7+e/mnp//tdHoWcJPfwyAz6u075vuMwy/yu63qvsJABf8krVbKvDHBQs+vnL+44+c//gt5/9A+qX159W/Jt4fSLynx+cV+gn5hCy3Du/h9f4C1th93F4+EsvdL5UR/UBWwL4uQXwtvptAyf9eBr8tAbUwaQH2gMWvstgt1XQEBfxZB4AjvlS/j/cl3wAYVckSn139Oxx49gMg9l9++16uwK2qB7zDpYdMomV0e2ZHF719roai+PAGQDH6p0a2pSiVS1h3y6gHLoOmrM+i5zfgI3A76+pqGVSyOlwu/nH61cHldvW6u4DMC1mXUFuQFhS2ZzAvAvZTs0j0mteWDu+JQY/+72lqzw9e8QnUD4B3Rff7wH4vVEuh/l3+vYwIjBcA+T8sNQDAChAMGHFRbcldrwPJAPLgT2V5Voqvr0rx9wKxS235fTFZNG2Gpbt6FpsldX+OPiWfVidT4X/5Uw7fm92/J38GHcZCMaw/L8X2wzuMgXcwoHxYfZ81gF7v099zVq8GMFj/ZZlzFjc+tywfwB7w9n3T998r/Ojtr38m1xPrvi7R9oqZ/yqdBZq2qF99Akn6WH1b9mH1VPefSNyPGIJRHxHyI0Y8SfypcUDPnkXjV0A76dO/F0GJoicMv+4/Hf7sEpYmd3F4uPj1XSSU/AgAeumMSxBfabHg5UL8T/g+GYPCAMrrYsgfHvphp/o5HC4iArv2r98yfnsD+eItnn/PmPfpAiwHOPqxW/opGMAKYAi+vwAA3Pu/mTveSXSpB5peQANFUBpb04gfkjQZhB6JUQyDEFTo01GE+MwaRz0q9HyP8sMAxWIkICKCYTCcDHyaiTBA74UkX5e+MVvEWmQC1vgIEjf6cRtcCt/1ecm/GOv7mLPo/a7Wb28+RYCVItFJm9drBzOoDzsH/9E6cIVAD+McDJN74WBDrMh+j+7pS+7OU88RWNGz0TUoN8fzXpaOG3a7afak6rbNET7uocnCwzUxJJuTZLZ7i5kU10WS3YDFetXBseb3kyiE44EPDal21icl5YxzmaV7poiiWhRwcToe3YKz0X3gNtEEj8jV3e9E5Z6c7jPT4murXdc1e+U9UpX0BstNGtnlLrKXOEbiqjFwTrUdF9ytW1fH9lpF+zuB7PYuCUGnKbiznV3bMHFpnPK8K8/evD4rWZldroGBosKDc9ZE7Cll3aUFVzcJAcX8Vp+4S+rQ3jzjCbE/l/3WFLY8M7KBYu8r5ICdhrw1j1OKKE5Fz7M/WD5KRdVjOuQYrOMwnmR3TeU5wUtUewcJ54fpKN1kj6cSyfajAq9dw7IUeLwph6vC769jTyjEeXChezUMW4rKzrzLKvJGyZrDJYLjSXR1XHKFYDp5vMwQJ2k/V/nFqLdFB2e2a14sCBr2EmmeZs5zdnvsZHsHJLzLM4Hf+/boj1fUzFyIyzNJyq9zrl/Wo65OwinanrncPVR43ajZkSwyxzy2arPrH/dLmbDAiXsNXRu0sU9RYXuFOk66DhUeFTgfQL1nJ+SUGWqu8zepq/OCLfTtOJjnncLkm4sYF2KO+FJuBJi7vV9jN7H7aMgdzvdqcd0EcGEIcn2Q97kXKWCQDlGdIne4eYTzNEe4reTZRe6ejlRV3W7TXkbLQ5uujzp92B0hy5Wl66hFeqjMKrMjcCJIcL2WeYGFbpWbJQarjYKw59YZXJbrO2EKmHNg3F0YkfamEdTmxkGNtz2nvXfc3DH/3EbZKRNP8b4xZJ+Xe9tHbY+sBY6WTgRBQVl9rR0DKtCygDOJRgOiWj+0RoWkltjGDCckWSTjJp+r2UyofHhF9AlqY4HEtgbfDN58DjbWZtZ1Njz0Fqvd3KI4W0rVNMyNbAh0tqY7qF5VKwYw/5j56jTvImUb6fgpHiR6JuuZAxzXeWAZDBPoyI4eg/tebXcxPE3GNIaHG6+5ohyWMslNrVRTj2OH3SSSgh0tkg7bQWldmQ38TSSOQteZSX3BFFf1a5vIqXkvFPYtsvo+HR/hbeywPGOVnWQ75kUojoQlxhsE1ZIM2qyhFlbn+bHpHwq1VbVdexk5Khic7ZSJokwr03jBogyf1J3ZjmF8Q22FQpEj3I7mForQOnYoRWsZlkNUacyz4GFN+r5hrEmxtz6tUYxHoPp0RNCDl5V+6BAPwdO9inYrrG/Fs3NE7+udWYrI47qXx1TAe33vCOKmFLmZD4qk9e11y1aJukauSijApX+ybIDESjhj1sB7peOW85HZHExDnqzL2WKcQSvOJofkdyXRTnCJOdtU2HRj3OClxtw81QtLWI7NBrIq3hVz2lRKX+k4i6q3otzPN2tyHZXTeNrmc95Ku1NyYdSZLLPHur8bNi9keLCejw5xt7QaIokWYF5BXMZIkxl8gw48FZHRdtBhfaO50EytJYP1ud4Txajb7ye8O4otuwvHYdiZJIvV6NVy9odtlzkl4jXj1dEmh1BJAFwep7WXJIqryMyr2eoYvO53wJDncaTxB2pDKC3EVcMXYg94rWVE90rzSsVZkOOzmO7oCIrjO/QQXSmOeG8+PgQxEjtrPJ7zve0KEDnjRsa7RjVTRxipto2yTUFNCKI6HSGEqIhNY4wnT7t2ZiuCXZyp8RdZZIcHTG12SWCZM6L03kXa4O6gUpDmBOh81UeTPwTITXLlRJ32BRoc0VRQXETL5SpFVGra31Fp5KREPDUoyV2yw4grCZdeOyDRWTyaj0K+J2rSdXGvml15W4sRuqNz7ZIrhXBLaU8u6GvoHPZe70qR11tB5ou+o1wOnoJAZ6VW6O6KQZrVEoxG8WO+7rqHRRj2TKlyz9XwhmnyksZl3bxI3nl7tpwItrmU7FEv7HeaLBhHZ35A69524KGBkzt0Hj2tuqK+0HZj3oy0qesqOxoel2x8Nx8itmRCqN1ZPHrO0KyWJuM6BfQYp4Jwu9Ghwtq4/jjEGxwvH4eGPXFWdAikJt5eJgXAb9zJxwNWbGTMSsqT6I/r1JTFgsO8kN30SFnabOqfz1y9TolYq0vkPE0Yp1D4lLttSATKAc0QtwQpc71x9kXyVQqTHdMh7YYWPcrSYEzdtXFNRDzXbKwTT1FXWb4wbTRbu83YH/p8qx0Fbr8xGRJNZrtGulI8Kq6n78/JAaMEAIojInMqSw1C1V2MKA1xCrIxaSASzhAcfe3giJ1tpmLjmx1Loow2pkhcwbdbTeuV4wjjpk/tjW7fbXu9sfV8UykySojR+VZuLuMxRfg4awy02BjKxI+XddKbxLEb1YwjGtMMSARfRwxFPIKNfTrZ5x7IcDxK8ik9afroZXy05nw+3tczlBlEXpmy7dqcIouPcyEIp6zI+fzsZwdudzwyrEF6QVNQa9wLZmNHUIftcSzYkuLm/X2KzIpJQBHMO2mWGbgrzW2y0Wm730pqDpB434jOupQk5upldVTeLtvUXXuNu+cfiPZIlKNoaQF+Zhqq43Z0J2kc5fGQZOtOs7fGi/mo7WBtXdQJTaHy4d1PiJXk80MUAvPU72RvFyvUURHNNIq3PLrxruLRtsI0kVpXuoDYJLBLB59C1tnetlotQUzBnLlZSCBQ/b1Ia/I8tjA3k5qq2d1jC3WNdmj6YObbXZVCIYVRJCGfJmrHCcOtie/+kT7JZwypkNt1uzfXHaNZ9diLLB6cZ0oEPSpv6a11Ph4uYVBBO6PETYS3NIUrczqfdtLhRNTc2uG9NC9ar+MfQrmxs+sh4dWbXye+fhiSQ5kQ5VyTBKhEx3G+GeMwtanxYFRLJnEdI509Ba8pDb8doFradRyd4RszoTany24WDuLG1Rm14a77ILCZs3pNrxftWvSmpsHImGxJEyFOsUoFlGec7oEO8KkulN10yZqdF5PS1eOYiJuuHnIQdwPldzoE6wjF5oW8VbqCaO6iRLMYA5uU8ZiLejBGiHDlNlM2zHSMpau1TzsG9IuUAetlcILY8hBseNZMJITqDbPm81bJXYmAZCljosJ0HxBdAuU6rtOJ9bGwpuPV3sswv3XTA17jjBkj0KmgL7hsXY6yn3QPZbwwiDzfB9bCLo/QDlDeEYMLvVEesr1lJM85W2YTYBtx3IZXM9XSeBoP9ZHdP4yTEx9sMpJJpTkEsd2CUaZ/zG5erC3OK9zddGjy5pZg+UB7fAjFdwdh0HYPOqE6j4j6ZmheEBDFmLtHONNa3tBZbjtZN8pVRYumAr2qsTiW+BzUuOMhk8nDSTyXg7phSHk6IzR8MfEZR7bazr5XNO4f9JbADNCZmLNUkSCJUS2+BhlZSEFrTE5IXfbhGRFa0A4X6OjghQE5d1W7ck3JF6MjT7g1X6kTh5/YKN+TUYHYkE0zuzWikznW6PcdQWL9bsgrmXa1U4GlYTbsWXO+TeG9Z0f9tpVMSr6BGqTfIDem+NDeljaDuycYC4fuWAf2WqqMtUsSg5CshdEJGao21yjlTMo4t32B7eYDnJkVUO0cYzfH1L2MRfM8vLYbhZTU29qjHZYvZJBZlC65Id8Kj0rKL7pRHq6xBSLkas4ebSC0GK63e8cW19jm2LH3brdRJRXkgFwqB4W+3NTqMhJrbEJRv5PL4+xTQfHAp8A4pQ82LHtWOmVxqnK0o6HR2rzIBCs4trnvJ4nAuQd2enQYfaK7yGkOmpJupnXUjObhZnOih2K4oFWpn3LkWXatKKcDnivMAuOkh7Kle6yIJNmlnDo0IXrM5Qa7bEnJdMUE80l9F5mIKPVrmMYh4kyzzKO9QJlsoNg2cGK5C6lHWPU+UcpVFsZxYpDHQqvr1Cm1KeUf6C7DasI+J9dDvbvtzrjQX4qNHhWY7bUkYWJ6wLKKcNbHbg/dNGoy0IvRudtmnPQTrDmIPKnQRLu2YDjURVI6TPQ2YbkrihMA6iDnze1FNjr7fBvK+RJjntQVR3vdoAp+JSasFk7IFbudLUxW9vvW2zrhfTequKFP2lbldOWUkOmj61pWuFD0cN30TXA/X8FUvI9Ux/MpXmyzhDZYWGSz5NyOBw1uz/A63GyFu6Em1+YMS9eAJ/lwu77jjVxJFLsf1PB+E3k1dsZEX1+ScHfdz+cpHgVWW59k9C7uZb09Wg0F6uN4d/Az9cB1yLhs6ZuCIDu0JnbUPnfudiob53tiH7WrYMeq8Eh7UG3FrmASn/cLMEFsDhOMFYg7C12BXwHePHhyMkDGHy8I60RnMKudwjLKrd5VPdmEVCt3VX69OzE1fU0kICo337geCdT6XiIySHVRJL2DgKcYi7LaAxrjDejzPRYUHa5EPb+2bm4rFDp2W9MpcceoKOQh6JxptIoWauZ6B7ydB313PdFrO7pzTUXqqDWGvex1ZyyadEI63pTxEJ9Z0FzRTMVujd5QEZgQwlbOj8yYwnR9e4BmTOPiXDctjpmYIxr1ay+mLiXbZQLljpqa+er6WN6Kuqwp3O9APeq1DLv29/aUtZD+8FET2kMmV3UEZfuHalqjYRrBdMwdA2C+dc0vP8AMMlrPPtmDof5AeNqEJY2piRp6VB7UZXtnYxh2HRiMAxwW5qPeVvH6CMuT6dvCwRua2Om2TZGeXVneh5MBO9jE8tdTvCFY3aozUAHWc3DCatHyjvYMj4etcKp9L5KGtGY2QT5r9JxeC9h0r4HXeyEvz+R8v9nXOAv39y2Jia39YFMzON3uYaEdogvBGPurluOiVAb4dG4GVejxnNKccDKT8/HhNXCsMShqIwSa+XpPpO4wqurgX1zlwCK5589yHrlxJvV8BRvqBm1wmJz5+64bhLufpV6K9rs1eU5hbW9B9/h+xBweK6+7jZvv9uRa3/ouM9mVQd6zS5Vd7L7VAzm7JodDdsVmtHWMdbmPb2ITNMc962Pb3iCYjkai+7roOoLcbUWocgMsSOOsG+yaOKpMYshIaWZXc/+I2A3DK9T6OB8cab+ZH1nJMxhF1JfNjeJ8ylGJpiaUMUsfLjdtAxPdlXja+UZCE1YfnVNZ7Fsl1sR78uhqcu+ltXnACROuasRVqna43w7kkS0ePJtdrndOy5jdEbTICfQYEpWYFDFgE+jQ3vIRpl3WNso5m2IV2twr97QVnWqG7T2knA83mgNzM/dIyC3IGMoVtUvJ+a6DbL0NRJOJqNwIZDf7WPDwKZLt62k4V6rA3MZ8OmiUXM8j/xBHv38YaBpuLSIoqkvZNtOVzC8PEfVVj0DQFCGTeSgUYbarw/3EUcAesyNdy8Grhx3Ks7l+Hs1MrInhXIfBPVpP612+PfX2FrCme2HrbuDhCgHR9rfdZRITeAhcgzn56P7YbWrnGDf8mUzYme3JRLLVlsBbB4NDm9S7aY3hVnkfWuSm3b20ghiddg4DImBJti+ciImlIS4ix+9Bh8SfGASKFTxtKRqD5MwZ7mjYteV4kK/XGr5WqeWHhysGxpn87lzrM5yqjGHtuHqHtrIoNpeC3NLtuYYvvTHOVm1dh0zqhoCIhEMIaXSAWJRUU42/f0AxCTrEU3Zudo2I7uUq6lRaHdRTIuwdyC3jMJ1kOZ6Z4LIxux0VsusOabLW1Kl7xAYinXq7+kSM6yS9EFT8cJPbnrs6Np2sZwW+lnZEUodGt67ZUa/nA9/gvEU0KoMU3dCrWRuqnQImcNatCtRWyBrG5OFCrXsiGpLiiONykOGdKcWno3To/DWn9cieuAwkpDG7dBYulnnF7pBd8pBPG73rUO4Jr5cfTbECu8Se05HmvsTPtaVmoPkgOqz37b55FNfoLFT+49Z45ATtT6f2cJFQWtB86Z6OWMdcEgyzBIKm+CQQQr1Xy0psBRXR947GGGfyJpXwlGluz1/O1p7cseve394FoPEW2d5bNFGo09o6bpCeRaptZDrbmjJAj3Le5upAIQd5t97MkRYZl2ZNYiTLtQID30S5ALNgGcmiqsQzzztxTsa9czhCdIjg1QXSotM5PM8aGA+tYNwh1eBuZip1z5tQYyYYJp3ZBd1QfWC4Ghq2KrWdEOtGYOqA3W2rGrR5IG1fM3G7qTdj5DD+ITzCIV08zIrkmOOBv1PCHgcl1y80RNmhvZDeRsM5TqBJw8mUQckzakQP7SLubz3Kok0Eren9OJqwBFx6Mera0twu3GO+PELIYJF0UnThNed0c3vNi3tnZBurFbfyNr48mH5kE0TGtxmOTX2PBVStpafAFQ1nDFCNb3U1CsIQG1RqE29SFMsocTg5j+B0QKvUZZxTyKixdgpUMmLLW2vd2xS/wqQXPvxhDZ3g0u8UNW6dbT9BDLOjCUUgIHe38UxPH1o7BJPrMbCPeBvYanlHbilEQ6QSGhg7iRV9flwLXBVqDk9IlO9wGQ887N7qh56/czFCb7BIGTddCK/dBBJKV5fre1AqwFMD7OK3Oxj0rk1KDgqn37LO5DcbqrhAaFnu2npT66rN59u71R7rtglRB1WrR5ucDoKVadEkxJO37Y9Cs0UCkc1hacsJRUWi5JTirCG2OPQoR3q8OswA03xUsLUEsNFl5oa/x6a+f5zo2xbpFL/Fg3vSNhaZbzJ82Ks7JzARhdoMKeEdYL8tL3GF45MCsUESatLdEieedWgLNFbcup4tSF7fjdgPnEdJ2PvoxjtlCotHGBLpvoRP++aYbDZvH95+HMe9/SsPkC0HOP/PzopeRz7fngt5HjVGXvj5yevzvyTVXz+8tUG2yPQ8FeuKIXk/XPovZ2If/4kDxYXA9Hoy69sB8uvIu/eS5cHlt6wCc1TfTl+7ung+GwJ2+EO3POnYLQ/DBuD9Dyem76qAj174ergjar/29dfXgeByKpZVy3MfUZj9+Jq8nxV+eAvfn0D6ilPk16htFnXfHy8AWuKfkE/429/+N89iOAJwLgAA -->
