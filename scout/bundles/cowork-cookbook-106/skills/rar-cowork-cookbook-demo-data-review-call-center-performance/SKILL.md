---
name: "rar-cowork-cookbook-demo-data-review-call-center-performance"
description: "Generates 25 realistic demo records for review call center performance in a sandbox Dynamics 365 F&SCM legal entity, staging them in an Excel workbook first, then creating them and returning each new record's primary key"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_review_call_center_performance", "rar_sha256": "2b23f25584b2531edbd73c57d7b17c5997c3374572af290838f3452b43f7dc60", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_review_call_center_performance`. The original RAPP
agent is preserved byte-for-byte in `demo_data_review_call_center_performance_agent.py` and in the RCI capsule.

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

Review call center performance Demo Data Generator — Generates 25 realistic demo records for review call center performance in a sandbox Dynamics 365 F&SCM legal entity, staging them in an Excel workbook first, then creating them and returning each new record's primary key

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-review-call-center-performance
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
      "description": "Sandbox D365 legal entity to write to (default USMF); must not be production.",
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
    "record_count": {
      "description": "How many demo records to generate (default 25).",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, e.g. demo-data-review-call-center-performance-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_review_call_center_performance_agent.py` and embedded as the fenced Python below (sha256 2b23f25584b2531e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_review_call_center_performance_agent.py` first:

```bash
python3 demo_data_review_call_center_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_review_call_center_performance_agent.py   # or on stdin
python3 demo_data_review_call_center_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Review call center performance Demo Data Generator — Generates 25 realistic demo records for review call center performance in a sandbox Dynamics 365 F&SCM legal entity, staging them in an Excel workbook first, then creating them and returning each new record's primary key

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-review-call-center-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_review_call_center_performance',
    "version": '3.0.3',
    "display_name": 'Review call center performance Demo Data Generator',
    "description": "Generates 25 realistic demo records for review call center performance in a sandbox Dynamics 365 F&SCM legal entity, staging them in an Excel workbook first, then creating them and returning each new record's primary key",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-review-call-center-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-review-call-center-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '72e8828e2a73d26c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/analyze-case-performance/review-call-center-performance'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/demo-data-review-call-center-performance', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to write to (default USMF); must not be production.', 'record_count': 'How many demo records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-review-call-center-performance-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic review call center performance data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for review call center performance. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-review-call-center-performance-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic review call center performance records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo records for review call center performance in a sandbox Dynamics 365 F&SCM legal entity, staging them in an Excel workbook first, then creating them and returning each new record's primary key", 'example_request': 'Generate 25 demo call center performance records in USMF sandbox, stage them in Excel first, then create them.', 'inputs': [{'description': 'Sandbox D365 legal entity to write to (default USMF); must not be production.', 'name': 'legal_entity'}, {'description': 'How many demo records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-review-call-center-performance-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need seeded demo/training data for call center performance review in a D365 sandbox tenant — never against production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataReviewCallCenterPerformance(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataReviewCallCenterPerformance'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to write to (default USMF); must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'How many demo records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-review-call-center-performance-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataReviewCallCenterPerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916ebObWLLnV9HcFzFV9WRfFgkQftERg5CQEIvYBIJyh4sdxL4KqFfffQ7Svbar293TPTF/jewqCTgn9/xlpg+/v9hdGxX1y6cX1bfzxcFO0zjy64Wdewu6uBd1Ar6KxAH/Ldwib+vY6dqibl4+vHh+49Zx2cZFDrYf/Nyv7dZvFii2qH07jZs2dheenxXg0i1qr1kERQ1+97F/X7iA0cL18xbwKv0aPMns3PUXcb6wFw3g7hTDYjfmdha7zWKFYwvmf6q0sEj90E4XYF/cjh8WTWuHcR4u2sjPHlvzxX5w/XQxC/6QOYjrpv0wL8gXLhCr/bp81rD2267O51u+7UaLHAj2lPWnZlHWcWbX4yLxR6CsP9hZmfrNy6df//rhJQa/Xz79/uKmdgNuveyAlju7tZWHcjTQjX6oJn3TDNBI7TwEi8sRWDwH1296g1ueH7xb4efGT4MPi//8z+Ru12Hzy6fP+eLt8/ll/qN0+azAoi3spvU9YMnSduIU2ON1QaV3e2ze1GpmSwKH5eHrc+c3SkW5+Mv87Ocnk9fQb3/+/FKUsweBOz+//LIArvr8Unfz79eZSvnzL69pcffrn3/5RqfpnJvvtjMxIPXrl7frN7Jg4belcbD4okp7+o0XMHNc+oD4d/rNn6fob+TeTPLlufjnovyw+DHlWZ+/AHmfIekAuj8mC2wAdr683oo4//mNR130fj576Odf/hFZN/LdZA7of4nur0/CkW97wFpvJvnlw8N9f10s33T7SvMfsy1BwPw7moDl7+y+Guof0X549m9Ip3EO0vfdlz8k96MNy78sfv2Huv2zDR8WwWeQOmncg7hzUv/T4vdHiPz6k/ft5k9//QOQ/j+SUYuudh8UvoB0iwO/ab98+fWn5nH7p7/++lNXgij27exLV6c/ovkjuz74/MmCb6t+/vNewP+SJ3lxzxdfc2jxe1H+j/qP14UOoND7dr/5tPg+E+fPcjEr8c70aYLvsrEBsn5nx19e/gAAlANtOvfxGODHf/zHQojdumiKoF2obtG1C+DgNs78WXgtipsF+DujBoBfv25iYNi3dSD+Zw/PEhfB4rf/5T5A/6P7BvrQDOBfPIBtX57I/WVG7i9P5P7yHXL/9rrQAP2ijgEiA4hWKEn6nNshWDjzLmu/8ese4JUztv5HsOvj/GMG7d/+VRZfHtRey/G3B3jHTxxUaHbGwKZL/ddZW2OG+qduLqgH/uC7HWCUFoAqKAcAwz8AKzRF2gMMnS3TJDGoRV4MUAZUtvFZGLr800zst99+c+wm+pw/QXu1eJa8BgILvoqz+PgRqBekcRi1n3PfjYrFT7//8dPivxf/bNeD+MxDAjXkzTdAwpN6Fhcg17oMLANuA44GQPLwze9/vBkZkAHFdgE8GQex/9wMYjXxvXeLq0fqI4rhC8cHxgNWzsqifpS+uH1dsMHiq7yA6fxorhVR0bSgXpd+7vm5OwKqNlDnqyXzogWFuY2bABTervEfXH9zavshYgaS3m5/Wwi0BCpTkYL/zWI+FoHNRR4D83+Nh+d9QKQGhXb7TuJ1Ic7RuSjt2i6j2n7jEdhPv4CK9L4dELfnav05nyuxP5vqkSpP84RzKzL3Hg+Xfpx9DnqXDMSQ17zzDt/aFW+hPepo/Tlv3tLArv1HFwBEGRdhF3tz7P3XW0g1UdGl3sN+QNKZ0psXvDevPGJQ+edNztwuLOZ+YfHWNc3FtkNhZL34/7mNmi1DHQ7K/kBp+91iL2qK+fTY3FnOnn02o0Cmh46P7PzW3rxD2DuSf87TGIRfPf7Xc+XDz29rnujY1cAtCqU86IMgA0aa6T5yYI7pup6zx/6cv5eMD8BqD3wEYQAAAyTUHMfvDOen75JGABXm62/tw5vKs0FAnC/KzkmB4wLf9xzbTYBU9ZzHb24GCeHPOX2PYmCw77WanQLMBegvgBAxyExQVl6/wvjz6bvof9r47JLmLY8OsgNpXD8IADn8WcDZVfe4BWhmt89GHuj56UEEqJGV7ay7A3ybfXi76dd+1cVN3M6g+bSrXwLg/jh/PzWd7/pDCXIHGAtkSNkB6z5yao6HDPRAQAYQvyBCszh/RvObER4E7cx/RvFb0/qk+Lj9ppD/SMS5mL1vnBWZ98z9wSIAooM74/c4ov0oTAC9bF7x4Pu3kfaV20x7xtIG4CHg+P702Ui8PnuBZ7OxeKf76e8mpZ//vWHqUd0vfw6AT4uobcvmEwQ9K/J7QX4FSAY9ZW0exfnjXDk/PvHg42yVj088+PgdHvyJ/lP1T4t/T8Y/kXjLkU8L5BV+hedH/FuMvX2ASeiPW/Pjen464+E3vAXsiwwE2SzqCLqBr8XxfQmokGEN8AksfhbLZq6xdwA9j+oAvPE5/z7o56QDxScP5yBtiu/A4NElgAR4Ou9rEQOP8hbw9uYeM/Rf59FsFr/xXz7lXZp+eAF46f/LY91crrI5vpt5JASZBAzfxv7j6gEXQzv//PO4fH78sNNXUAwANKXN9zH4VmTmIvtdqjxVBSq6gMOHhfeoEiA8gaoz8znN7CZ5lIdZpXYsZx2eE+DcMz4w/8sT8/9eIPW9WMxF4vvyMCPgHWTKPHEufgaTqt2l7eKiCswv/7XIOtAzzEZ1HhjiPVvSH7L/2s/+PW8DtA4zda/4NFfRD29wBL7BDPJh8XWcAEq/DXgzBz/vwOz86zzKzF54bJl/gD3g6+umr/9S4fgvf/2BXE+zfgHVPf+Bn47FHYAYQJc/VWAg63u0fjMJiv3yQ8Xfi+iXZ1T9LYdnpX0vwY+4nRd+WPiv4eviX83wjyiM4h9h7CO6fh3SZviBJA9dAZyDojib7Zs/vlmleEx7s9DAiu3zHyd+fwHBbc8ivIX327gAlgP0+9jMbREEcAAwBNfPjAXP/q8HiTc6TWSDBhYQQh10FaAYtlk7KLZCQDn1iJWLER7hIISLkSThrlbEGiNQO0BJeLPaBKs1hjrrVUB4Lj7L9cz/L3MPGM+yYSQRwCSJBmsEhT3gP3TteRt8gwOyKGyTjo05GGk737Ymce69KfxUcLbm15lmNsyb3r+/OPh6jpt1w1LPDw0tEcdHIWfkr9AVI2M+bF21Svelh2Udsu34mz3k3p2aZBFt247hxvBytrh1mYTdcWXBO1ki9xK6h1SNzDVhwk507NCBQxgof7ird0XA3fNV8HvobCa+sA4nEWPctN4H0cBTnJXu2GvmDlfbIZAEprk9kYqDmQbLjtO1g9alaNJBfZ33WNQ30faowXIHaWE1xqHMyivJsnaZqTLU9gT1p+0mBVDM5GuNJ0/CGlWvSzEsuI13vWobjYemOxTEYtwF1i28pkqndHzRa9eLwxrYxep8o4i124YRIudqX3FME0W+MeuxiCYt3Mt7k+uaCBVEgREN/8JJ5ZZsFIo/MBzZsQ67Qfsa09KJWxm7OyQadUOK12launlx09oBOgf9bh+t4Yss18sE4de6k57c1W5/Hu+ri3kkrWA9xl1i9RmzvRg6Q8s2Gk6RjcW7jU4hruLsYXmiQ7qhlZ1wtTaTkBGwK3PYWVST5YZP9utpFFlUISlTZDi4wzauep3YpND2drA9GTawM+z2mr5x+iGWyeUk8ahKu63jWP5ecHeTHaU7a2zKO34JriybX6jI6i+ZrZ4O3SBdsrDaNZBFjSztyExGhVx/zM/9/hDel/AZup434mhHpXHTRHZ/sKFDkZR0FohwQ9MnUedlT1e6bY5ZWHsYufq4PXgCBZFdU+7hvvB2rbFbXrpgLOOiYJXbzdiUmmXxmQMzkM/e0Es+sVa63apGqVtbm1mqEkpPBl9HG1lytpbRmbBquQfYH53MwS+jgV6Qwd4uq9qN7972HNLHU7KOoEO36Qt/rxuCreXXWJFxPbS5VqgOjV7wRko5Q4LgRJWaEXykjWvkxYkhoBveY6vdqCT8RsaCQT3gyd0tl7K2PAnVMMS+urrxHERdHXW7LtrQkzNnFybQZIaqvSIuiBSdnaYZOfQq2xtBoSboTAO19dvW0jY9eaL52OQEP0j2cjb2+zztJAcTDdRa8tOZl0v76JuxR65vxOroSyLh6BJ+3CiDdMyH+1Jd+VROGWjf0FleelTnsDG2MutEU6zt0dBTYbJopkeI/E5TwpB4TQHR49G50zWxL2yDCY3phun1bkgmw7JOjM0nEMiO9nouztFpn9ox8HgSnfhoOLK1zfBbjNoY9Cg048ZYl9n64FFZTrPUrc/P2i7GcvSiWZnPHbX2RipEyAVHA9Kd0kLZy7AvrYRhDTVOeLTDaM7QI8696hEvr2PPuu7P0RXLE5PR84YYrKxwN9JRu6SVrLZ6flzm5vkEm/joRjyAxAzbK9ma13bEvUDVhuUZQrGYw01ku0yK+KqhE1somGbHUUeozMyTuExlhzrCJ2jPdmOkoub2zKqn0jlcLDmEsmWUEDCObHn3zpR8pvrdVRL1YjfgkxbArt2ctasjIZel4urM4ZL7krCNjVFfm6F5j9nzNbqMnX2EJjSRx1iJlS0bJqQ4YWk1LLte5TmG7vBzHPUD3+P3XR6bG3wZr2iawcygkI21ucZEis9Xcnu6iJ7mZe66HG10q8JnjrHhKeqFO1VptHYfOkoppXWhT8ZFH9Q9M+xoSa+M/GhZ5NG911vEyi5n4ZTnEMtNabeq8iEeo0uYFVjjNNBUR9GwKnEltTCNkvr7gSSS8igVRVyLLkJw3G21r1OIcJfi0VnxxunGyC7lD9v0UBhKuk52ko+zSm2zy0ndMixjaFwKT4c+bK/m7pqZtXLqMrpV7kE8uBBN3+OouR6m4bpe4gfpyJrq8bBPz/RZFys5ysjMQYbNJpXrasdWiuJmx4t5cf12EAP15nFWdD6RfingNmld9XvShG4iDwpLq8d9nqXCcKRNftVdyAjdN5ZayzszBSF4qnRZ7ysCLZPNdowihTp7HeacESQmjZrraHQXGIkUkHyU0qSY5jSepxQiBhCELyWtXarJVhvxiZGa/T2/W7p9UpYlpJ5EwMuPB0XjoErJe0gPKchYt2c0utFDfiHWRCKSGzdQzxIkkiSjYOTRiAm4PLuHasCwyld5+SZv20TdFrSTrjBX3fOmzRtcGBcHoSHQtRYfsqwmrixdZ9eYZ7ZI36b6KdGlbTdZrrkjXRE/KeL1JIXiXZOztX5QI5aX2Iufy2XFbOXspJUDVXAu2oRba7Nb49Zy3fgEhF20IDMwPJB9HsMnr8n3TGyz3c4xO2FFuKWvVEii1KC0T/RmRXLVsTGDG+2H+v7ADAf3MhCBdNjZNOKd21Hast3AawlxPdMFrdy2x2FYQ8WWXo9mOar85W5g6919p3WTX5uEs1ThAydeDsddc3W5ceTyCCYqkjPXB2gdFvRBj0751iN1PS/Zdbq/gVnk0hUjbVDomJFQldL15XAZlSzN2RYdqSbep1JLNazhVlZ8hEjX6WEV1bfF3dh7yX3cXq60eHODEBHS22A0CoAD2dFk8pCNrGDpBwGR7E0tsAWjn7XVfmJ8eWtSyVhkKX+9i74jHuwNGAUj6oKeQNKPhG1m14QrULY19xU9lr3qc9peuB83g2Czkdswh+2Ssa/lfdObaWHzRXVWYbinC4Ozfewo3w/srr51dsVekAxKrz5rn7rUV1Mf5qScPMihqXgUOXmlIVxHR6+WGnuwylV2bgqz5C4XeI+aSMkq40kxeeZEsqTpVyJnr6XIcqLtfSyR/ZT2hLJnyUNB46EENf10kQVhuxw447LZdrjjNbopihcZL8meJ8W7SGR+U1BXO4+7tkNPGMzuAioayzBetkuuD8ntXYIihlbDdmqXwTHdrO06nIJ7kR42Zm6bfFzx8GFdSbwmu3Z7SXdXmdidtkwj3DMa4X1KuiGX9HSy0PrkK6fwYLLw6JVlbERts2lxqrO38QjpU3l0D26u3UtntNwbzoTdsqV2U11N2iY8bLVIRztiJ64PzEmOmTwRjnGMjDaYptW9fRr9XnE5wdkiblvJQ01qgrJKuVtYWv01845+4oRFuFWpIjSujM5oKnTYD2HvhIKJdpwjtGt+fVpC0DGZ1KLNtOKcD2ddNgfoEvWr8TqeKLe9YXuJrzOO2+3zpbq7rvsqvjZ1SnVuMA1Z5NGWuLkwnHzjtbrgqO0+a1W6GHQj3ad+pEa2JEwQ2u5Cqrq2IrrKDx7euD7XVuPUx4inCnpV7jAWNBS5Kup6vGPoZqcYrOKie/aAbmO3smkjQUjXTa58cBStqmEZZbOdLpuDynshwoFuv87PJr2CTeqWbkqqjztIWPGwJw2KqcQE5cn7jN6NzVkt8XORUSx3ifUN6yxPBHo4qAbhFXsxS8zTLjjcTqOQmUYZ87eKjeJK1+SV6Fk8zftZKwVHGd41mJ9PMOlrQ7LJFdDuS25wPLkoVFcCWV0YY7pkce1kFono1z5VyGvOjsHQ7lE1BdlOFStV1m+s5hyz0ZA8wVCXuF1NSJ0dmaWs3CXDhLNsSMzEpMbUTw5ZRbHMlm+y/XgoJpFr4lSXikNqUWK0by7dXcxRokSgbS4cuPt1z9xuGSPG+UYucwzC90Tmbk+8eLfENj/VbLVPA4MpjqG0E9ZOtLbHfmxhGTfFu2dugs3K02H1sll6vYbgmyUqOTlZLBFWo3PSOGwaZbW1vVLYY9XWEduqyCoTvxPHSrYPspDXVaQpfBv68DYC+M+ujWZ/yBoolk9p6Cv1psC6NOhSrfM5Bnf7FYZ6yA3unPRap6UPsxwaRpcEafi9TuilWBxPKoMNG7KmuU2FjKzChTAYB3ntJAUStCHOq7rFSXhbVZFuIwHHM0K1i1PygkC3id2dlJseZ8hlZW8Dleyba3qvm/VhORJbxjHwapsFB2KS8zHNNVKrjNW5iG4+oXJJYOuKfLBJUhtaZdThIpbwol/dnE3Fn5J8rStsSNx5ETmVRiZiQ2W5vRQq69PqFofssQwbechHZO9L1yS6F+2qjG8jXTArhtYN68aumKY8pt09OwmpJPVgHcq1HF4u9UpQO/aojL7jd2p9QyaXRSY8oQx6e9vpEurVQblCi53BuIIycmWb9MU2TK01TKxCjh1Ezz61IYUuq57VN2XJbYz9bavLEnNvziYbr2yMPssMxWBC7vSo7Qqkvr3evCB3IMLrJYYRN3QG81SEl610A/ld+9hqBcLQ3SeZBa3va5fznNWZMXegk5Sj2/5aZdtuhKA+h2jzBBpgw2UEMnWWYTKxADFT/YrCAZ4Io89FuXX1kmh5Q07MUN9JOcV6HEoiHQ/ggbPuxGpD3beRFh64PddMTtqyoWlBWnrouzByttdGMqZtAfPcPlKGTdLGvI0oLuYohy5BprK2lmMg6hlBZvdDFZBH4i4VV13jj9ge5bMTVDlGP5bBWXb4g3cu085wixt+cwq90DzGOiorveJQ2QENckmu0TiCV4Tcu8lRcLeMd4kOnk9uryuYtyrtluDXsROmqSWyiLw2zbbxiFAy3bt/7GJqVSv46azaLW5CTj11x1yyFGJ/JTDnTjQro0CttOj9/rzGK42IqUttn+PlDUXYLr6Ih4t3Xkrk3lKOIzFcTqiOEk5xVGsS5o3ePlW1dG8JjzNIyA+0fm0z3S6Qh81uhdyqiNIO/sVicccdrItmiEp77+6BB4PwvyRJ2fSOpsGNGJZwv/ELu8xTY+1B66VgpAjq5E2DesohOJ8cG1/VQuuAqdFpufs9uNV3o6BDyYEl2uZoYgJdyYhBwxUdkvy0byscgvb9pl2Kmlyv+mNKess+XjcH7kKFO1W+95IMG2dlP1Xurd0fPUOjcmRnbGE8X20mnYOpixo11TrCDzuYGZXdLQT9tESeElHBkRK+1GJ+RkvjbLR4h4YbgtKZyVF3OCO3KiR27sWNpjLWeCS6HPklB+fMzS9yD+Vj6GQKJ7ZVpmBcwQiywqzodNyu8nZFCXlu1QKuRKRFJxsVVOjjJuM7i4Rbz3NaPfbO9lTXUYHyYl60jtJ3SgGpcYnRy/pIXMQdlLGawEYnSlRP1MYPuk7o6pO2HuFhH1RI65m3+nTDvViuyWawEaTmNys0qnLQT1m1fxer86HN/RtSpwhyO7CyAOlA1SmdNkY6Nkea6RowDmXqXucUfrqbx5JYJneRG0ZaBi0SFvneuTsd4FITPYQ9upvJc2V+21WRGF7PVsi061tgRPVe66M4Ox2Z4gz1FGoJRn2aVqlYlpcGWuo7BDQ/WuJbBC5zzO2g7gnMsnirN7MzjyB+cdMh19rtOgvxT9FKM69YO6y4QfA6ogqO1+kmUVN5XU+n3dEhza5uZHe11+xdckyLrkxcbONEbRpcxILfQAKFRdcz0mvMKsiWSxO3hT4pb1ep9cSdXE6RbvhUXxm0h5/PDV+A0fuGo6ds7Ra4022iDXuza4B5rsPusXISW3Q7Ncj23DTYGh3XSJH1UtFGshWB5kpf27cYsyNkJIlJvFN75mJ6ori2Othkkt0Sl1BTabL76cbaOx8b0iOi9Bfg4Ut+5Q8VcyDDncZ3mGkaIgEj9Wo9eognNSpMrqabeL0m16PUahNkp94UofhpC/Jxc/W3V6UjrW66sac+tysNrnwXrgPk2i7DfR8Eqmhfe/mib5yU6ygwVa83tYuVPIPZTL/Wgkq96+fAzPhA0+1zj7sVqROqeMhtzNpuNkpuSmi+y6Ta6ePc670tJBTucAUd7HkzXrZCsmMt47KU8eKKOI2MhOj2gpeC5ylL+xJMEybr9p0rhXOsBTlDJ4FChse1NtGwp7DmHUroFEakbNoXJu7iyk2aWDB6l8m18eNRQ7CBPd5LBBSNRNlcjBFXUe2aDUp/IHYCo9b1BTF2YzDmvVkta2dcReia0k9uYC05X97f2q1w67b9IFeEfDShYJcoVepgg7yUjnA9DBmJn1oO4uoqVXiDbL0sRzPCv4Slt6n2mpnTScWJhI869sXCIN5W2wa1ssqTRt3mVHSH+HiUqRIBulrBKMQmGTJxGVmHXUfAmebkle9tTEsTyBlgzGw9qks7QamLUlrCrrIhvSMcLZ8mCk77GglhXN1o8gmxjyVHF1DXIdKUJRtjzJDKZk645q1NF19PjhLhZNPb7RQyyxYjOtlKtGUF655/ypeM2e+IdAW6CGrIyVNmJWdEPiiccTLYGr6efUpTQ8e4uBK5RDbYihTKrYQebv46XBU7TvG7u5lBDplyXoOjRIo02LRu+dytw41hkFfJ3xPCOkUuuUENGpGFOLTGQrw8DLkhhqOQqCIu8Hp9c278yuydDN/EAixppxLZIaW/nBzhflchFk4bUykK7WA13gkmRHkJdxpGhGnjDRV13FLDCNB0zzZ7PIKV8AhPAS9Ta+/Q34PTsnG0oEeuR1k4Czv2tt7jPYVkcX7uMuJKL+NjEuLEoO9W3G4t6WfSWvuejhxd7Tol+aQbSdlVsHMP/IKADN7UwHieSMvcovMArimUCKxz5G3obSeF8p30laglLJ6PhOrWVVnrRKcGgtjCAcB23F/EBoqsJeIOOJa1Lu3cXXxjOLnTMc7KvEkC6JUgTRBtDBXw/bWHbXojwrjPWT6JWE7ted2qp/vz7cqXw911TwEXFeqWojy1CfBJ2eoXaq+tLgomXEvRgn2Jj4sGOnSpYo3r263SghTeHuC8ZMzqnEfryw6XFbFWOitwC2cobggGmYQtuvsVVOfLIY8neC9CrrDE4HjVlsdwXXkIhRtnCSEy/a4D/KMFXiRwRWamY0tzN469+ssr6W54iVi6y50WiuO2mG6kG+V4kSCH0eCi1DWh+3BfYryzHXcie1EhVJPyxpaoFaLBK7uOaIqi/vLy4WU+Lns7rP233yKbT3f+nx0yPc+D3t8FeRxL+rb36cHr078v2l8/vNRuDAR7Hqw1aRe+HT/9zbHax3/1gHCmMj5f1Ho/k36edbd2OL/V/AKguWvaevzSFOnjzRCww+ma+RXIZn5L1gXf35+zflVqPmy1G/9LW3x5vFf3vjmeRch8L7Zb/+0yfDtxBLvf3kn6ssKxL35dzhq/vVUAFF29wq+rlz/+N48g5AmeLgAA -->
