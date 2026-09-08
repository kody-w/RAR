---
name: "rar-cowork-cookbook-ppt-exec-insure-assets"
description: "Builds a read-only executive PowerPoint deck on insure assets status from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_insure_assets", "rar_sha256": "26181d2d5366c6ab147e1d59b1b9e424c55ea57dd15d97aa38104dba70bba5f9", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_insure_assets`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_insure_assets_agent.py` and in the RCI capsule.

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

Insure assets Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on insure assets status from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-insure-assets
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
      "description": "Prior period to compare against for the trend chart.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity to pull insure assets data from (e.g. USMF).",
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-insure-assets-2026-05-24.pptx.",
      "type": "string"
    },
    "review_length": {
      "description": "Length/format of the meeting the deck is sized for, e.g. a 15-minute monthly review.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_insure_assets_agent.py` and embedded as the fenced Python below (sha256 26181d2d5366c6ab…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_insure_assets_agent.py` first:

```bash
python3 ppt_exec_insure_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_insure_assets_agent.py   # or on stdin
python3 ppt_exec_insure_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Insure assets Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on insure assets status from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-insure-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_insure_assets',
    "version": '3.0.3',
    "display_name": 'Insure assets Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on insure assets status from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-insure-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-insure-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '64dcb354cfe0eff9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/manage-active-assets/insure-assets'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/ppt-exec-insure-assets', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'comparison_period': 'Prior period to compare against for the trend chart.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to pull insure assets data from (e.g. USMF).', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-insure-assets-2026-05-24.pptx.', 'review_length': 'Length/format of the meeting the deck is sized for, e.g. a 15-minute monthly review.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for insure assets reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on insure assets for a 15-minute monthly review. Produce 'ppt-exec-insure-assets-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads insure assets data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on insure assets status from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes.', 'example_request': 'Build an executive insure assets PowerPoint from D365 USMF for our 15-minute monthly review.', 'inputs': [{'description': 'Dynamics 365 legal entity to pull insure assets data from (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-insure-assets-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Length/format of the meeting the deck is sized for, e.g. a 15-minute monthly review.', 'name': 'review_length'}, {'description': 'Prior period to compare against for the trend chart.', 'name': 'comparison_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs an executive-ready insure assets deck from D365 F&SCM for a short monthly review, without modifying any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecInsureAssets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecInsureAssets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'comparison_period': {'description': 'Prior period to compare against for the trend chart.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to pull insure assets data from (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-insure-assets-2026-05-24.pptx.', 'type': 'string'}, 'review_length': {'description': 'Length/format of the meeting the deck is sized for, e.g. a 15-minute monthly review.', 'type': 'string'}},
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
    print(PptExecInsureAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916adObWJbmX9G8/SEzG9vsILmjI0YICbEKgUBI5Qon+76IHXLqv89Feu3MrHJ1dUfMp1GmLQT3nv085xxffnuzuzYq67fPb7pvFyvOzrI48uuVXXirXTmUdQq+ytQBf1ZuWbR17HRtWTdvH948v3HruGrjsgDbmS7OvGZlr2rf9j6WRTat/NF3uzbu/ZVaDn6tlnHRrjzfTVdlsYqLpqv9ld00ftusmtZuu2YV1GW+YqfCzmO3WeEUudpr6sqzW3sVlECoVeaHdrbyizZupw+rIW6jFbjM/A8rUeU/rNraL7wPQATvY5DZ4YeV7S7iNR+e+thVBR7H46rJYiD8qsoAy6by7RQoXJSt33wCavmjnVeZ37x9/stfP7zF4Prt829vbgYkBWqqVbsHavFP6bdP4cGezC5C8LCagC0L8LvyayBvDm55frB6//Vz42fBh9W//3s62HXY/PL5S7F6/3x5W/7TumLVRv6qLe2m9b2Va1e2E2dA1U+rbTbYUwM0a7u6WMzcAFcU4afXzt8pldXqP5dnP7+YfAr99ucvbyUQwV4s8eXtlxUw5Je3uluuPy1Uqp9/+ZQtDvr5l9/pNJ2T+G67EANSf/r6/vudLFj4+9I4WH3V1f3unVftu3HlA+J/0G/5vER/J/dukq+vxT+X1YfVjykv+vwnkPcVbA6g+2OywAZg59unBATZz+886rL3C7tw/Z9/+Wdk3QiEYxY37X+L7l9ehCMQ4cBa7yb55cPTfX9dQe+6faf5z9lWIGD+J5qA5d/YfTfUP6P99Ozfkc7iAsT7N1/+kNyPNkD/ufrLP9Xtv9rwYRV8eWP9DOR+bTuZ/3n12zNE/vKT9/vNn/76N0D6X5LRy652nxS+5nYRB37Tfv36l5+a5+2f/vqXn7oKRLFv51+7OvsRzR/Z9cnnTxZ8X/Xzn/cC/kaRFuVQrL7n0Oq3svpf9d8+rUwb4Mjv95vPqz9m4vKBVosS35i+TPCHbGyArH+w4y9vfwOAUwBtuhdsAfz4t39bybFbl00ZtCvdLbt2BRzcxrm/CH+J4mYF/l9Qo/aBXZsYGPZ9HYj/xcOLxGWw+vV/u084/+i+wzlcVe3XBaK/vqD46wuKf/20ugBqZR2HcQGwVtuq6pfCDgHmLpyq2m/8ugfo5Eyt/xEk8cflAsD56tcfE/z63Pupmn59gnD8wjhtxy/41nSZ/2nR5Br5xbvcLqhDr9Lhr7LSBTIEMcDjBdabMgPVpF20btI4y1ZeDBAE1KPpSRtY5vNC7Ndff3XsJvpSvAAZX70KVQODBd/FWX38CJQJsjiM2i+F70bl6qff/vbT6v+s/qtdT+ILDxVo9253IKGgn5QVyKMuB8uapbi1ACSedv/tb+8mBWQKUGiAl+Ig9l+bQRymvvfNvvpx+xEjqZXjA7sCm+ZVWbcA5Vdx+2nFB6vv8gKmy6OlDkRlsxTVpbL5hTsBqjZQ57slQVlbNSDYmgDUy67xn1x/dWr7KWIOEtpuf13JOxVUnTIDfy1iPheBzWURA/N/9/7rPiBS/9SsmG8kPq2UJfJWlV3bVVTb7zwC++WXpWy/bwfE7VXhD1+Kpar6i6meafAyD1gELOO+u/Tj4nPQceQg573mG+/nGnupjZdnjay/FM17iNv14goXQD5gGnaxtwD/f7yHVBOVXeY97QckXSi9e8F798ozBvk/tST7H3Uv7NK9fOkwBCVW/390PIviW47T9tz2smdXe+Wi3V4OWdq9xXGvDhGwf0r0TL7fO5Nv6PMNhL8UWQyiq57+47Xy6cb3NS9gAzbwAKpoT/oghoAkC91niC8hW9dLcthfim9oD1RZPaEN2BDgAciXJUy/MVyefpM0Akm//P698j9DovYWY4AwXlWdk4EQC3zfc2zglTZafPfNoSDe/SVlhyh2oz9ptdgfhBWg/3QkcB+oCJ++I/Dr6TfR/7Tx1eAsW57NXweytH4SAHL4i4CLmxavAvHaV3cN9Pz8JALUyKt20d0BeQI0fd30a//RxU3cLpj4sqtfART+uHy/NF3u+mMFUgMYCyRA1QHrPlNmQZMctC9ABhCYIIPyuADlHBjl3QhPgna+5D/A1/d+80XxeftdIf+ZZ0sd+rZxUWTZs5T2V1jbxfRHmLj8KEwAvXxZ8eT795H2ndtCe4HKBsAd4Pjt6asH+PQq468+YfWN7ud/GF9+/p9NOM/CbPw5AD6voratms8w/Cqm32rpJwBU8EvWZqmrHxcg+PhK+I+vhP8TtZein1f/M4n+ROI9Iz6v0E/IJ2R5JL1H1PsHGGD3kbl9JJanXwrN/x08AfsyByG1uGsChfx7pfu2BJS7sAbAAxa/Kl+zFMwB1Ogn1APbfyn+GOJLioFKUoRLSDblH1L/WfIXuHt551tFAo+KFvD2lmYw9Je565kQjf/2ueiy7MMbQET/n85bS63Jl+htltkM5AnoqNrYf/4CrgCP46YslikjLr3l5p9nVRXcrlevpwuWvLYAYcNnsH6Prye4LorV7SJhO1WLSK/Ja+nVnrgztv/I4PS8sLNPoGAAjMuaPwbzezFaivEfcu5lRWA9FyjzYakAAEqAHMCKi55LvtoNSAAg2w9ledaJr6868Y8C/anC/LGkLOpXwOB/V51eBWhJ4p/9T+GnlaHLh19+yPd7M/uPTK+gt1joe+Xnpcx+eAc08A0GkA+r77ME0PZ9unvO30UHBue/LHPM4unnluUC7AFf3zd9/wcIx3/764/keqLe1yUIX6H099IpC5oBtF+M/wnk7PgK2MUedel1LnDCU/Ufp/NHDMGojwj5ESOem39oG9CSx/7wFUgQttE/SiA978PLIAwM9S5K7vtPkF6un53D0uvGM8hasO5dJHuFkh8BcC8dcg5iMMoWHF14/UCMpxygYICyu5j1d3/9brXyOQouEgMrt69/ufjtDSSYvcTBe4q9zxJgOcDXj83SV8EAewBD8PuFEuDZf3PKeN/VRDbod8E2jELXqId5JE5RLmU7KEH7qEduHNTZ+ARGuCTp2yTteSjpbWjbxtcoQoAaTiOOY5PBBtB7IczXpWWMF0nIDR0gmw0WECiGeJ4fYITnrak15ZI0htgbsM8hN7bz+9Y0Lrx39V7qLLb7PvAsZnjX8rc3hyLAyiPR8NvXZwdvUMfHYGeSLNgiN/EUCpYRtxrmzOfHZjDyTXIauihHiXiWNLsbDmyqn0SbB1UEKanuZm+DsoKGArpAc5Xe+/Ryv7R141y84cbn7slSc/VIF/JVPbpn0Brp1SxaU3YXj/vJcO/Z3kQE17z7MT43sybuin0TIv2Y0PDGcoaunCMDADi5kZUqb840HzR5xJ6ji3Exygci9lNsXk9WZUZzvy/WDmOUaz8g5UIa6D11CCBONMl460+0EezI1DAczolPXYlto3VyMvfwqWi8nShaOydidtMeQa2mnoIdS5TlRTtDgngcmmHqS2KzG819mblRLInpRJkw2KNV/N2gOWmmyKrFhQ209ovNJO0pyIfhTkP9NY6EWrXPGfNmBoeqQUZIki80J2TbZD0fNpx8wdl2ENkJmZi9taZjUcnozqcPeB2K5SM73njmbjLbrXggNlDppbCfMNxwxuxoGK8pM4BBLDRQuFGvF3tnmuEV40UyrZ19sbetnYAZpi0ZXi/d146F4aVP2oU5S2OKMDtxz9nRpPPbO2VNcyiO+1p0TxnLu1cOlW3xogj7uDhndeJpDQfyFdJ9mggxcWQeOrW+xKdhQxsU3MwTXuXHTBRk5AzayViPL8bptj7qI38rMeNMly60v2rautM99l5wHQPn4xWhbDPQlBgMNNEMWfL9cQ4f+RiRUz5R+B6vFAzSjs1Dzc+DuNulbUxNe0OBij5+xPcdhgVpsh6YUMqvUCLIUhIeA3VUh1Y50Uf5Eh+TiEcfAmXXRji0vJoR50zhe7LqJWgftTkHX8+F1XlnUUtsO1If19AsnWu6lTY5+sDKjI/Q42Qbej7qNea4DylQtuf+vitU5Xizi9NoHqjCty1IMH2pPwSJTGUFEfXDAUJCfyfcCpfPz4ikNrjJsRpsc+1aSu6H1C5Ih3GGUWZll1CQ0+YkP7L8ejDVCRILjF7+7G5j7+YkxGpQHuny2oUPJkQkm/HoB1zTTOrMkiWU1zjkqo0lDZeOzIptVUzDVqc858owla371xPF7VS5FBVHYdUjtJnDfcfxk4pJ96kZ0fVWhEZRztaIpBXrhxYSk1fL6c5Uoslt0xNWX4x9g8RbaS9FpimElMYMuQhFp3NAnPrtmto8fAGlxHw4tEN2ZJiHE8389bKlxXyWCfmE33IowUPDl9o117WJnZkMVWz50SSu4dU3m+P5wqq7ksxUXiKKTZHeHvoMIJXIIIQ1auouSUbLQq2rMdCct3Kh9wmt2Cd8PWTrepaIm5Zmt6EYsSKtkrEOIm07WdVZKkXIYMhQWle5a6+D+ILo980mVMPjRbMrhqpE9KoXqXgKd+u7ljAOhCOKPTvpeVK27CAhd4FQDoRdb0+qZTtUElys3DzMsKWWxkwPcVqP+HVPIXGulfisUmQmkDKYTHAdeRgTywzxXtt2Mbmejfuam6vHlJyt7nornbV5R83UbYzjnrYHBWDc+sz5jAyLzTjLtOvqkEJIm3Qmcp3DGB07MTwy5JugS8ZrbsyR6W4LHWha52k3mazE7KWmtk4KTUv30Oq7WCl5kevZdWDSoh6gpwR2Yz+xGuikDAE5o82Nbjf80KzJkMNDDoiYXdWKEqfZUigkSPC4wGv8jI+qqzu3rXLDzXnPe5vKN0PCqYv+GihOBj9ipUu1TLogPJGPI7KTN3A1cOnMm8kOuR8I2Fa3fC6mSkF1sleqgX6+Jsyk1NypueGp3YT5RrXwnupnuWItXUMeaXU5GEKS3z1V1qZ0byBQmvIHw25ov4n1vU5pw3TgK4vcDbGEoNRWOHL3FrEapUkT0fS33rZuglZ51IfZnHORGrbbmotD4npgB6xrrJi8N8OjBMEYKkn7sC0KSxQ1Sw6igTl+oU1BUNzX56o76wQjM0RhBxpplgeVPir7HPdHjZL4dRhgzrGb19VWadthoO1uv+c2wVhxuylQj41dn85JZ9ablt7X8jqvbkJUBPF8C0PGSXc4qdARSaw9cV9E3AM1jOzIjdyaxtOLzeVxTW/krTkmI7RRE3KjcDPlK4XCCQ5fnRk+T4+sI/KK3wGYapEiFL2KuJy4fqjYIiJ3pXESr8SNENZXyjvvYIof05MkhdbhbJ35Oc+ksqNF6JS3NF3yqJ47GXYPB4dnj82R9GhWEmqqHkwpo8jIdfzWYof4uB244YDZiSTylACTbbSVrik27Y/7+bgHwbGuL1VU7tPiOMh3CkYd2aRd9mg2d/KwQyMy1qCkmvfMHDiB4UxBzEa85gbZHDCQwtjxTWSyQVRNhE+Uhmk2Dgc/Si5lOVPfmZj9gHaPfkh1Pt6OZl9mg4kM7BWU3g05CiiDGvf9urqwUpbtruMOqdIzv0tJFNuf1Y3r9MgO5G8oXw0vheIdiKlLtOb6tIIEYzxSd4ZpWXYtnPb3fBL3TuxnlHG762Luoti949dboWQsS9vYp/pOIYgtIzNzprlt6Z5LrcgQy1t3lbk5e3WYHjlnk8/oxYr8bTBf0TI+TIPr7Emj8os9tkmuYJyKS0Kh9bUd3aqJTj12ewtPnU92MXs5WUhy0I6akvbzuZ5yjYLLyWB3fbQ18Mc94ty+RzpB2T3CzWTJhmSMgkiJvixCZ1E414R+bJOK5RNcv+vUAeJrmzc57ULgZQPbciSV6BZNIXiTwXasRaGKCResiJpMjBx2VDR0fpROTUEXWfU2x5rb9g6yPow9Nl77iE8l3k3uYe/4VI2Jlq1ucibNypPuFSTiWpeI6iSF2OqmAxqNO3Io2Ztl8ez5bLdGxhqbeicwXCIP+Q7lT1s1w42YFO5YLfiaEHI3Hhd9oYqxUWvWHbXtbEa3u6SY1LBxhPzG6nCmHJiEzNLEaWCHdG0HnkvYL7tHaLDXjPGM6hoMMqdne0nlbwGzrxF878v5KJkpYnNsTUrnKAk2fjXwJWhuhDzzHZnETo+GOZIpU26bTnxc9RTSZTTqnVB2rp3oZaarQHs4gFlXexjXWUD2uFmceu4W2Dscn4LptHXbbNwbUp2L4sEtIJ05lCRjSbOVxp1vkcQ0qOQJO+72GX8OHtkeVEE9nZiHNj5c5UAp/F6bYbyd7OYmANxBthmL6Um249cmc48kuKQVj0V4McLnM+bYD8/VTPFejIGcu+k9Bg2ldYKp5tbqnRg+dp380GVPNJkb75qmpN/dVlflncNtdpk+7UPMAB1/nJcg1uuJMCUXlVwLrcsobtFZOt37gwRzbiYoUFfi1+oib/G0o+3DBXJ7HJnRTsg6q0uPIe/zPeER2m6daBG6d3iYih6iePKG7ryVZfII2SzVrisKtE+FeXUVUxDXm1o6XieXw2Eu4/ZbwlKItq18DTse8TwId+51b8HimMqzKEIQyDuPabK7sd+mjO7kbFVoCpZhHLLJSb2NcROAPjoVNhaLtd3DUpIGGmQKu8w+wFlQtS0psWrJzjUD91dKL7zsOkhX6bCTBfMg+LmHg+LjCH6DIAEV58PcrJnytqvwmiEunLAbHaGIbAWG1D73E0k6DHdizBJsNFR9nmfkcvZnZjasBn6ACpQx1mwVPT9Lio+rvN70kPAIoogT4HPqSZuqlDH9iMhudWAPVmCdiFsT0+kN9BnXo962x1Ee/WS4clB+lG+TkWdhKew9FeSUvM88w22dc3Q+qLLOKgRrPyJZKFB1q6PqLp5cmEvY2pEcMx3qklWKEqqTNjQIxOg6P3SRwUtambD8jevey72rZSI2gi638OVI1k1ZUrrs1B8zSr8ne12YVYOozpN5LmwEK/Z0wTjxo7rUt9m+0WvuwN5zik7v8rkT8AwvK8KYLQqNJoqwkWZQ50lIjY3W3+JmDcIoJ9m5QBkYP+C3W+DxdR0jmh/iB3RyVL8xBPLaoUJVsBZ7OwWGqJQM7403SdxbR2OQ7Phi2juuSwVKXxNzoehCj7lNWpF9ozV4rMiTJ/lmQBuShtSS6uvaza06xqHXhmoxp/mQASyfqC64qGN8ULgRdKVcdJksPhE6Dl/fzyY7hh7ACyZLO5MllQYVlGLAapQ4h2cU6cwBDwgbKgmjIWgOmq/Hcm+jUk3BBnSrL6SDjWeaOBACrUV9k04s4fZ0m+x6Qe9uczvBnn8ImL64IukBpTFPcDagT2It+nHzAreFU22KBkOmRb9IiKM8n+l+F9QVqcPb7UHQxhprNY7sbKgJzZN+is6I1zlBZ6jdTZYfVRagytSgqLWZ9BvWkwitXE8hBoaRudKRM2VkkR3oDmFqrBw/uFihlXtKCGM0+42My9sDv4H6vTyaXTAIEGgpIaRLlDuOewSZs+6552xFA2Grni8uP9fi7tLgyMkra7TdlU70uF1KNjkJcQami8vjwePR2o/VQio3/N1Vk6BxLilyDWdl04hDROIRcdj1hO2YscMcE+260YMWJaF48O8jiVgUSclkU2gVJiSO7/ne6Bhg0n5UqJadNhUhBpeUvKCP/YxpG2ZnJ/IOR/eouY7gBrRmDogxCdqpdtPxvXeFPOFwP6/x4lLPu8GOiuZa6/WmJ53NWQQtZXTK3Tnd55trKlHVQ3iIFUwrvQEnD66EawqXSOZItDQa8P3+otHcKb2i0ua2Ps1gaOoTowOXp/OMI4/a8jbtLE3t2g72azA2Ojp3j6oSU0rkWD2KdULDMHuByswX5eQwwvANJmx/h8UXLjetkaR9r0ZdBnR1iqSbBzD8D/Phcb0MUBoH3rZg1EGIrCL0lFrCT/w2T5WKR3B3DLaazhMCz4wFLfBQs+EIRUdt6l7MqmbVMcpStM3ODXM9P3j9cO6vEHtyFTKJ832uUqx9MtfzRhBzEoHo8BIwPn7fMfdkVz8ShMTxu5kI+P5mtfNOxBPbuctRSPtHgUetky/BOs6NlHCC7GtdJw9xzo/BQXMVv490M+lvmQb1bOfrFnqD/ejRSIW2T7con7IjCVHERDetmnAYH3vcWNeGd0OFNrw6h8KsS+ya0c0OvarNVA6bra3QfqzRAV6aFqXewWywBlOIDxHNeIIPo1tqRHijb7Gpydc7L21vx6qCNf2a8sP2yhTJQZboCh3PaNaU967awmN+qeOd7as8JouFut1hjWYlZxToO0s60sfI0cFCRy5UNCXvpMZyGd/DaAn5/YVo/I6CwtMhu173R15WVVaklfX+3igKW5/K27Hgh3atsmXePOYjfCmv85re2d69nw7r6RHeZh3yxEq9jg+qG7eSq8m30xk0Bhs5KdxrbN8v5tHmNgzrqrcD3bbKwQUtSJNDXSjdTw5aj5GMrDMAXJ53tm/dNBIKRPAPqt9GkD8Wt7QmqRjSmuF4UxXxBpvMoYrmU6twm0t2UuzD2CpK3ml3JQhmN4sl1jidhsw/lmVulajb+GBA3WqiobTnokg0nN02YYDfYR307sDITjJcsFMTQw9k0vb84yoJDr5j/YGpMjxoXInbUAApaev0wAolRhl8rlXcRKyj2l9m2M68OcIoPTqPa6zu6STEKarYgPae6lPxcaL3/enY1hSNUffJ6npkbOg8u5QNZc2PtCULp3KDw8mF8q4Jdtaa7XeHQ8gWD0cs+AZxIhq/tgCjs0t17U7uyRaSmSQSMi2SvAiKW+8wqlz5Vl8gPBiL90yXOnsHjPkadXMQx/WRkBMsCOUnil0jJdzj0zZWQsu4eWm+OYkKD8Ht+kgE8w4xzzwxbNJdhKJwJgtn0iCR0uDVHJ4JNMlNfbLxSjketxEcNRYH3wI1TlE89kcqhYSWvduklptzz6VjDliaM4dnQYAhW2wLlXVqKcNlt0SoUnghs3lk/T2kjwSBPFSZ0WRRpWgStFRkf02cuB+mCmbCisMbqUEgJLhPKSv07Tmp02Fox3vvVDmWcX4wjWntKPm9Lpx1rsVpG85Wd7uHCYRLNwA+bB7f5mPvtgkzu9RFaedMVSGzrHK/2dhpc3FB6KCcT4r8YMtJfoOT+4TjTpyPG94v+sMtjeAi3D1QVTwfhNnaJ6NIRcLFGOKxvrc2Ful+ivtcId8qT1PIWa65dq6OawWlutDLkq5QKzEy1bWP20XB91Zns2MPg+F/PtoDy7fqnisLxOr07QUL74pMxHQLw1OfSkdTPRckrGWu7BhSVhZXp3GcjjRPfkr7dGY2RO1dM527TFAtOHXRBl5nnyHb6ra3FK7MInQNqDPo8wAmnEE29BPFMZWVwyfrHivdzcH4+byRscJQAU7R16ZmGWmd6Ncx4uJIJvMRKdymZWmdVIsOjKk4V27dPXuUpOB8jofLAwx92/XaIZ3tkS3Rjj2obZ7j97naU4o25h4f7GmDuDZrlBxR3CYsZLvOji5yPW+uCcRqAMpBb0FRcV/1xJTknTSqpnkNZrnbbqC894I6UTN40zipaWDOGiPUmxK3xIGFpPw8sJcLQ6I23afy4wh6g8qOySVgkBMOsjyhTkMQErANudR8ra87afDp3fzInE6xcUTJOliIVegW1ZYwIkO8qfuAts0I1JWZkjDvogaXuse8ptio+jrQA2HeVmR+ZbaHcwuDlm/nlLsyCR/6Y4cLUWfN2g4r0IOlqf01TyOBoBO8uqiawmDntuK1s6uy6/KYNlHunYjMm8Iee6gWTkYtj85eD7VBvXMl1T3jG2KgcR+0+aXPThFmsO2d6K3mjjPGdCSEIZ6bytyb8mmQHm4eE5i4qY/RHYZnfLANthsOnAuHwx16CIpWFgVnW+MRE0/QA2TzAZNYxhqzTXUcCRXe0mNKNOjuHG63bx/efj/Pe/sXr5st5zr/z46XXidB394qeR5P+rb3+cnr878S5K8f3mo3BmK8jsuarAvfj5n+7rDs44/PGpc90+ttrW8Hzq8z8tYOl9eU3+LC65q2nr42ZfZ8fwTscLpmecexWV6DdcH3n85S3wUGl7b7PBr82pZfvbipysZ/W95BXF4M8b3Ybr/9DN8PDT+8ee9HyV9xivzq19Wi3vvLCEAr/BPyCX/72/8F88IueFguAAA= -->
