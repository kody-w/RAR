---
name: "rar-cowork-cookbook-ppt-exec-issue-blanket-purchase-orders"
description: "Builds a read-only executive PowerPoint deck on blanket purchase order issues from Dynamics 365 ERP data for a given legal entity, with KPI, trend, red-flag, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_issue_blanket_purchase_orders", "rar_sha256": "d583c6976fbf36aaf794112e3f099ec7722caf6ca6c9121fef6e7e3403641dc9", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_issue_blanket_purchase_orders`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_issue_blanket_purchase_orders_agent.py` and in the RCI capsule.

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

Issue blanket purchase orders Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on blanket purchase order issues from Dynamics 365 ERP data for a given legal entity, with KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-issue-blanket-purchase-orders
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
      "description": "Dynamics 365 legal entity to report on (e.g. USMF).",
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-issue-blanket-purchase-orders-2026-05-24.pptx.",
      "type": "string"
    },
    "review_period": {
      "description": "Reporting period and comparison prior period for the trend chart (e.g. monthly review as of 2026-05-24).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_issue_blanket_purchase_orders_agent.py` and embedded as the fenced Python below (sha256 d583c6976fbf36aa…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_issue_blanket_purchase_orders_agent.py` first:

```bash
python3 ppt_exec_issue_blanket_purchase_orders_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_issue_blanket_purchase_orders_agent.py   # or on stdin
python3 ppt_exec_issue_blanket_purchase_orders_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Issue blanket purchase orders Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on blanket purchase order issues from Dynamics 365 ERP data for a given legal entity, with KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-issue-blanket-purchase-orders
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_issue_blanket_purchase_orders',
    "version": '3.0.3',
    "display_name": 'Issue blanket purchase orders Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on blanket purchase order issues from Dynamics 365 ERP data for a given legal entity, with KPI, trend, red-flag, actions and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-issue-blanket-purchase-orders',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-issue-blanket-purchase-orders',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e7e61084b3ac3dcc',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/procure-goods-and-services/issue-blanket-purchase-orders'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/ppt-exec-issue-blanket-purchase-orders', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to report on (e.g. USMF).', 'meeting_length': 'Length of the review the deck must fit, e.g. 15 minutes.', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-issue-blanket-purchase-orders-2026-05-24.pptx.', 'review_period': 'Reporting period and comparison prior period for the trend chart (e.g. monthly review as of 2026-05-24).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for issue blanket purchase orders reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on issue blanket purchase orders for a 15-minute monthly review. Produce 'ppt-exec-issue-blanket-purchase-orders-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads issue blanket purchase orders data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on blanket purchase order issues from Dynamics 365 ERP data for a given legal entity, with KPI, trend, red-flag, actions and appendix slides plus speaker notes.', 'example_request': 'Build an exec PowerPoint on issue blanket purchase orders for USMF for our 15-minute monthly review.', 'inputs': [{'description': 'Dynamics 365 legal entity to report on (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-issue-blanket-purchase-orders-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Reporting period and comparison prior period for the trend chart (e.g. monthly review as of 2026-05-24).', 'name': 'review_period'}, {'description': 'Length of the review the deck must fit, e.g. 15 minutes.', 'name': 'meeting_length'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs an executive-ready PPTX on issue blanket purchase orders status for a short monthly review, sourced from D365 F&SCM without changing data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecIssueBlanketPurchaseOrders(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecIssueBlanketPurchaseOrders'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to report on (e.g. USMF).', 'type': 'string'}, 'meeting_length': {'description': 'Length of the review the deck must fit, e.g. 15 minutes.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-issue-blanket-purchase-orders-2026-05-24.pptx.', 'type': 'string'}, 'review_period': {'description': 'Reporting period and comparison prior period for the trend chart (e.g. monthly review as of 2026-05-24).', 'type': 'string'}},
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
    print(PptExecIssueBlanketPurchaseOrders().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916V7PbVrbmX+Gc+2D7QhISkXSrqwZgAEFEIhAErS4ZOQcikAA9/u+zQfJIdtt9p3tqnoaqIyLsvfL61loEfn1zhz6p27fPb0boVgveLYo0CduFWwWLVX2r2xx81bkH/hZ+XfVt6g193XZvH96CsPPbtOnTugLbuSEtgm7hLtrQDT7WVTEtwjH0hz69hgutvoWtVqdVvwhCP1/U1cIr3CoP+0UztH7iduGibgPAN+26IewWUVuXi/VUuWXqdwucJBYbXVsEbu8uohpIt4gB2WpRhLFbLMKqT/vpw+KW9slC1IQPi74Nq+ADECX4GBVu/GHh+rOY3UMtt2nA3XRcdEUKdFg0xdAtuiZ0c8C/qvuw+wS0C0e3bIqwe/v8898/vKXg+O3zr29+4Xbg0pvW9BugnTBLyz010V6KqLMes33A5RgsbSZg4AqcN2ELZC/BpSCMFq+zH7uwiD4s/vM/85vbxt1Pn79Ui9fny9v8Tx+qRZ+Ei752uz4MFr7buF5aAIU/Ldji5k4dULMf2lm5RQf8U8Wfnju/U6qbxd/mez8+mXyKw/7HL281EMGdzfLl7SdgfcCvHebjTzOV5sefPhWz13786TudbvCy0O9nYkDqT19f5y+yYOH3pWm0+Gpom9WLVxv6aRMC4r/Tb/48RX+Re5nk63Pxj3XzYfHXlGd9/gbkfUagB+j+NVlgA7Dz7VMGIu/HF4+2BoHjVn7440//jKyfgBgt0q7/l+j+/CScgLAH1nqZ5KcPD/f9fQG9dPtG85+zbUDA/DuagOXv7L4Z6p/Rfnj2H0gXaQWi/92Xf0nurzZAf1v8/E91++82fFhEX97WYQEyt3W9Ivy8+PURIj//EHy/+MPffwOk/49kjBpk24PC19Kt0ijs+q9ff/6he1z+4e8//zA0IIpDt/w6tMVf0fwruz74/MGCr1U//nEv4G9VeVXfqsW3HFr8Wjf/o/3t0+LoAlT5fr37vPh9Js4faDEr8c70aYLfZWMHZP2dHX96+w3ATwW0GZ4YBvDjP/5jIad+W3d11C8Mvx76BXBwn5bhLLyZpB3A0QdqtCGwa5cCw77WgfifPTxLXEeLX/6n/8D4j/4L4+Gm6b/OuP31AcRfXyj99R2lvz5Quvvl08JMZshO47QCCKyzmvalcmOAxDPnpg27sL0CtPKmPvwIkvrjfLBIq8Uv/xqDrw9an5rplwdkp08M1FfCjH/dUISfZk3tBNSAp14+KF7PehMuitoHMkUpQO+5BnR1AUpQP1uly9OiWAQpQBhQxKYHbWC5zzOxX375xXO75Ev1BGx88axuHQwWfBNn8fEjUC4q0jjpv1Shn9SLH3797YfF/1r8d7sexGceGqgeL78ACfeGqixAng0lWAZcBpwMQOThl19/e5kYkKlAWQJeTKM0fG4GcZqHwbu9jR37ESPIhRcCOwMbl03d9qAKLNL+00KIFt/kBUznW3OdSOpursRzHQwrfwJUXaDON0uCIrjoQDB2EaiqQxc+uP7ite5DxBIkvNv/spBXGqhKdQH+m8V8LAKb6yoF5v8WDc/rgEj7Q7fg3kl8WihzZC4at3WbpHVfPCL36Ze5xL+2A+LuogpvX6q5BoezqR5p8jQPWAQs479c+nH2OWhTSoAJQffO+7HGnWun+aih7Zeqe6WA286u8EFJAEzjIQ3mwvBfr5Dqknoogof9gKQzpZcXgpdXHjH4aAH+STfTLTZ/1QKt5xboy4Ah6HLx/1XbNNuD5Xl9w7PmZr3YKKbuPP00t46zP5/dJmD7kOeRk98bmnfQesfuL1WRgqBrp/96rnx497XmiYcDEBWAj/6gD0ILSDLTfUT+HMltO+eM+6V6LxJApcUDEYEpAUyANJqj953hfPddUmDcZD7/3jA8IqUNZmOA6AYe8AoQeVEYBp4LnNMnswvf/QrSIJwz+ZakfvIHrWa7g2gD9Gd/piAfQSH59A24n3ffRf/DxmdfNG959IxD9fA8IADkCGcBZzfN3gTi9c9OHej5+UEEqFE2/ay7B9IHaPq8GLbhZUi7tJ+h8mnXsAFg/XH+fmo6Xw3HBmQMMBbIi2YA1n1k0gwyJeh6gAwgPkFilWkFugBglJcRHgTdcoYFALuvNvVJ8XH5pVD4SL+5fL1vnBWZ98wdwTOo3Wr6PXqYfxUmgF45r3jw/cdI+8Ztpj0jaAdQEHB8v/tsHT49q/+zvVi80/38p1Hox39vWnrUc+uPAfB5kfR9032G4WcNfi/BnwB+wU9Zu7kcf5zx4OMjwT++sv/je/Z/fMLMH6g/Ff+8+Pck/AOJV4Z8XqCfkE/IfEt6RdjrAwyy+sg5H5fz3S+VHn7HWMC+LkGIze6bQP3/VhDfl4CqGLcAgMDiZ4Hs5rp6A6X8URGAL75Uvw/5OeWAslU8h2hX/w4KHp0BCP+n674VLnCr6gHvYO4p43Ae5h4J0oVvn6uhKD68AXwM/8Uhbi5Q5Rzb3Tz+gSwCbVqfho+zB1SM/Xz4x1lYfRy4xScA9QCWiu738fcqK3NZ/V2aPBUFCvqAw4cZskH2g9AEis7M5xRzOxCzIFxnhfqpmTV4zntzh/iA9K9PSP+zQH8oCb9H/0ftfrQFMxj9GH6KPy0sQ97+9JdMyjCck/4rMHDcJ39mIz2uz7D36j3T8PY4fFSvcgBNR5QCDH6wQYkFwIvhNW7/ide3fvjPbGzQfsyCB/XnuRJ/eIEb+AZO/LD4No4AM74GxMdAXw1g9v55HoVmvz62zAdgD/j6tunbDxte+Pb3v5LrgYBf5wB8htE/SqfMyPYywSeQv+MzWIG8gGcw+OFL/38ttT9iCEZ+RIiP2PJB7C9t9bT0PD+ndfBnifTwvSV8rnjCK9DfbdMOuL0BF9v3e+94+OgF5sQDofGMixKEe1JM736d61e0+C7eX4XMQzZQYECZnk3/3affLVs/Js5ZC+CJ/vkDya8g0np3blteSfcaWcBygMcfu7k9gwE2AYbg/Iki4N7/5TDzotIlLmij519nCBr3SYYiIy/CSdeNKGaJoliIRwjDhD5FYZjvRqTvkj6DYmgURmRIhfgSwcklGvgMoPdEpK9zJ5rOkhEMNW/GoiWKIUEQRtgyCGiSJn2CwhCX8VzCIxjX+741T6vgpe5TvdmW3+aq2SwvrX9988glWLlbdgL7/KxgBvVgh/LG9gSfEHosbvbQbN0U5ngqOY3M5tT3HO0qlAMOWAxjc0wXsHLaysXNEKHteNgz6ZpIKsiE7k1+Ti9GjXsnc89jsnJ00jMQXNUhmL7z92rwlVPZBIa3lW9X3S9S8ZqWsemm5SQ07nbb0fDkxhfU8huzlSX7PJZiim/lsQxSHIZgHU5d1zZsoT9s16LcoKVLCWZXjmszWd2Yrm4OoyDYl0nyQIdAKcp0MYQrtR4hgcAYTdcnuz4mBXc8n2Psdtm0ubqZdqbV2FTqJQfC8mgcqqTUiKXSd8yO22tHpFxWdXwTC9uOWwTZlny4JHFyvzNS5zId94Rlq02UqMFZ69D9JbpzS7pDcOAjmIZMhsaiFAqvuEfB+BgNynbL20WRKMnWJqZD3U39ZPHkcbtVvcRKT8haYcS1SExrk1pRBqdPk9AFNSzf9kex4YYVezxax4Ezrzt8KrpyJ8aWp2/d47VKznHF6aLEntftObkUZ6NgUhViU8XZ+Onk7u/3FXkPs4Ik4XTjrCNEM+gpXfWycCvP+p5FVrbIEow1WeetY+j59QClBb5fY/aeaYpcqEScH62AL3sdMgJqk2EXfXcMpZN+uOhXNwrKU6gSjIO04jgZupJ3zUUQyyPj3Bsnlw+u6ASIymZSV6yltDhg57GNI2I49WpR2KumQ8zJSqJptIqGO+tyaxKFVlBdA4dOj+QaIZ4DfWVsi+O5OG3UlpIUozD6IOVpb7PGpqmQj3ZzuGgCs2Q2twFHdqmzV1lfzVu03hGXfpI4ZEOygl+a6Y52dxOZOJ4Xywq2b25Ha1W72Fgb5DHeuvbYsgbu9ZeC3Bsr/6IFQZpjG5RBzxXNLffY4TpmGS3quDWYrSi162zXQiOdRkzKbEj+EsU8LOYKt6GtAdEEb5vdbHe3q7UisCHl3hmVdJKZqlvGlV654Q47eaW9te6wSFd7KTOZ0mwYT2loSmluZ7nsTKUZopSGk9Zq16rMBThsXqGddyfQ4mLBhyCpNlMUZTCzSumdBx3dW3dcdXHcVTaaWK6BVsdsSISlWJwDkqidzfLUBCx/uPEcnXADXqlwvDmVio50fOwGcG4HSTmk7hrdVuulnVNnteed+8rcbuJM2ZLF/uyqrB1t+aZFWFldC7vVsIvNtPNiH1k59M5GY7En/JC1Yk9uu7vEZR4mhex0K/CYhJX+clav9sGI94bhs5eVO4rsJTRuYpK7cuE4ulhA47qKIp8+Zo027yqu1crZ8maOeHZwqaKjltzCu2GbwZXSlB6j6f7WmjvKEzNjEMQjdRCD/WGSbsvckdJBscUtyu4Mmd4PIe+ucxP1GkbJndORKw86NZDsJl/5K7Nz9skAMS0mDcVue91zZ84XhJ4eJFbW9RS+1zWY5fKxwbzlOF3yFZdaxlXE2MPdEzvLVJYsNxAsmavFDusBtMeOIVY323LUMEQhM/MhgEWu7pt3bX3FAlXE1qVBQ9gmPo1sDR1xku3oHZG2NzZYRgl396Z0j5zA4LT3LF6KET+Tk4BKZFZEpoqWsnpHHtkiGVwj29udvKKsy9XoQ0o83LxxPGIyq5zaGIqGNG80RiU7a6v3XH8csXCdqcMR33lVwx/z44olYY4cnHxPMOyesV2iR9Tbrt/j0n0iEHuP55YLyfoNH++b0jlgfiUKOKyGrpgeyV4WrXhryGQxkhvXtG40N2CMIu28/da4F8TmQMNHIt6YO6Ok2JvMwbxwEo56o/BCJmOktbG7ZcmE1ypUpjK6n/U8Xd0lgw9rz1veSddZForjgPzPld2xDKRVt7ZkgzdEYxc3BLGZ0gt/59nzpgx6dNepAFYu+pkN466LekXP+Xa9C1EBzsONLO65pI6UzIDGoT3mmd3Hp6Rd4ek9J5zivj/v+2bU0UyjmOG0p5kIwKxWb9eS1m2geCICfa83BbQqpA5CuEQnpIZnbz6kMbu7caDIJuEw1Bcc1YiIAyBCEQgaSRC2RbTlMnXRAMuLYK3IMH2UhC0bOLEN72Ffk1NTOuTB1m4L53LhxHipLc2U4y8XypTZI66N/CVf4uXUbkoFOexv+LTaQS1nKRdsS63A1LEpJy/erEbBiCdxtxc634hHyZSb5CBva2Tc8ks1oe+1Yl0s0mwlJ8O2njWh0ppasZrZhQMTdFtv37PCSRUcJeaq4USE1EkTW7W6H6mG3BHOOQxOKbk/kWwueAIjFeKmbz3CXK2KVupzXtX4jXAxGGrSOjs2fBrWTWHsqp2heZ1fphO7PyBHjo1R314ZHKVyJHEcFX13yrfrDeHAe9M82PVaQNBkO5IsHpeYXYSng97mTTVKcObE8t5elpszeaVWbTzpsrtPti5tCdbQjJvuTmVQNp5EPm3SfWNq9k6SVlm63a2dwlf2k5cLZZQuMccp5EulL7vCy7l0lQvHXULbQz5AYmHIwiUzXXuXGoHgtIWYb0JYJDunsfelP4jnYR9w/GGNNNmEEJ60JbrO8UFlxQTOWOZ6FkgAmEu64Lf7KTQMeV8ePTiQsSO9ga8nK3U8Qdc774YBsAw81Oh3B297nLihWCrGaBjVAeXZkQ1k4m56aGXUOo+lkqV0kGhlU6EjcD1Z69UADHkqj2PhZyc7ylMWukHSrbUOm/te5AXYOZKZlY4nIU4ODSkM/D6/lL24SoM4dZstl0VBRuq0Qtv5Jo0zMogyw/QPLDPyntx5mdC5UHff6BAj7MdAOhFoSZcoJdvyiuOPpONF1zT12FGIHeI4wRHGTfWSyWp5R162oIoGZKSZ9JKWmdHTBJCvoYq5MzTqLEVoy00WNHnnYr5zFgWUyjcHuwHtJQ1NObyXePQsTZIqtBx/Oojusq1jT5Mg0KnFU3lz2GqVxxPtXSE+rdaCK6/RftQ4YpgSgg7gq1mQybBaI8qZ98obS2js7SzJh26VxDRid2Z3pKY7Z2Fcxt+Ck+SWsgvLds65RX+rhwglylvWhMtIELpYFLbF/mhwyHXSd7lC0fuUadN8RKt1VGg4fLtrm3hCzkONszKhbu5r6oDdwybaumzRwbfVOfBFv20NkxDQKaOps+/65QmZcIW/7RnpSA2HvGG1wK8rRLwdy8PaGFZUWlZWY9oHIcW51lnWe8gzAgW960ldag7o91e3c4v7aSkmB3W1KdCcLqy9nxlCxSK1Lhyh5UbuJN4gy+SYFqvIJQSJppHiskTIfktJVdOikmRtRNdaMTHb6cw+giCRCkgmzPaVfMzbS8zae1Pxy2sF1tNxsN52UeHd4wwdR2/coDddMaz0jDDLnXNpD1NvkJvpKKgGl29kxBwUl1f3oZPZFT2huu3E9T0TG9FGBmQFRWZYnTqtwf3QVBlm9HU6v3eH7LaxLqYktsvzNfSueTe457uX4sjeSFOWj+LS7FUsqE9qbyI3dyUXkntoBu+sBvmBx9UiiO8suw3Rcy5dGMiCfBeAigVhSBE0FS3ny6bwUSFRpa2T63jZVLCwPGglez6u9cJdNjFKe2d4K28KvZQP0lVEnA5LKtc7Bl1cFuNFkYelkNwsbucal3WqrVxOvYhpt65pNELMJASd6LGtQSB4osI7CUoLvhfG4kXSTDLeXkdVvW+ifl91191aiQIIswhhZ5Z3mBXOk+dcgXdtT+u9gEOVTByxlnEL6VASGIZfIBLbrov+6GcqqTouVzgDWgm5h4+lkN3uKWcdVXzNnxpSI5eE5USBfz3KKtuu5WRCCcyz7ECx+FDZZ7Qj35KhZw5sWmDt2qDD7BoyoAlu8CZPb7zR7C9cZXheCIX7gk+PR2mLRF7XMConpChzkofiCJX72/3QrOo86qBpynaNu7oes+uAMsrqpCpT7yM8czgD5ORaUM30tVtlQXipivXRa0dtnxmSgcaULEBXA5VAD3mHikSsilN8WO3o2ykaexj4YhK34sqpD1x1PWJrGqVMSulZRYEgYceWsSzGR/+yD/XLrdruI0820CDZ7eUsP8kqWaksr6BDFyLkOVxylkxTTktxN17tvHYvovp2dArRz2F1h5ios14b2qkwWkU9VGc/kM2W3Xr5xt5yMmnv1OHAb7QdMk1XRjO5bkco+VyzTl5gJRTEFK2YyHCi5Ex+2LFVdiZDpeHzwS285SFMNic6nu43ce+eubWmGU18H1Itl+RxdRKlg8FfSF0Fw29s3Vd0ICkO3DqQbxsZe44oa6oycojyFiOOZk0sdYvjwBy4bzFIx1BELbas3HXE+oyZftkxjTZhjpLpkg+FeQIPo1o1EAWH3p4sW3sbrPDibp3OG6XdcYLkhoMDo8TOPDTrUhAQa6wz0OdJRwCihBnlVExcBwtfCgoLHa8brUf76MaRR+yQbIbWKlQ0EEjXs3Snu2CZeBHKBCqESnWKKmzHIWDMmjqbF8rCW8nUr2WQ8CMfEkued51eJmt3pen1CWJU3SyvIoFqB7wmdjWt6RS/lD1MH9R1ZkNS0vXWyZftBuTOHsLNnPd06li1x0gCWWdPYVg5pRIwKHHiM2N9OAVqMV1wVMNji9zKjHtV7rl/8MpB2jT3vne64425Eao/nFAM9Bm6ja18ahtisNhSSLvTD4xGSI6nVzcQLYgU2ScylhID32DnSXUmjzqMkEMhppUdAgH1nMDkRLYbCMkez4zEkRbVMjyrEkm7vQYweeEG+RodHcjEXK0vQeC7NIpfvXyksYtmcDaf0WdoBeUyBOzkZtNNCxkYHrQrtNkkxWDm58FrI1rXWCbodUkMKE2Vum3Wci1p3juqyBrQRdGQqh/x0jcIEeQRiBNY9JMjUYVLnEEHlkLX7sStcfl02+SluhJl2oNIU4vW+mAe5VbGFajm9/e1P9G70yHsY8FG/eBwUcoT4d253SaInW6iHe+OwGmkjOKp8apgxYSiuF7pmiVKTMsEQQDZhKFPyBaNbts9gaG2KQjX5WiEypH1FViSl3YUiLh2ikxaO9g0SS5dJctGUrIRd5e7O5RtopFgbBVbnvuLG5v7mAN/yyAKQ3Wg5PsyaWLhEPQuOW5sxSSc4zCdwVlfACw+ZKesYuvuam0zFTvn4Z0pC5OJeYeWYdmUq6qT6EMw9ldxM8iGam9K48jrgsSed00DGyub8be6sAk756adTkWKXMVwQgMAJJ68O212myWmM46lrhG+F0oqO6DZHp+qu5Wl2M5RwTBcOWhBNIQ+2oWowagXDCftWg0wRcTqtrpYq+yqEKZKYfssiZjqIqAhLjo3qgzwxAk22BYCVimEYcTBiJVl8L3KdWTqgpPXgVl/o+BnTEikVG4JMkuc0s17NEYyT4SoyjiwnK/fxSEwlMYzhH7tjxhyPknnMgu684XcqKKqVYcdhsV4mJnXFQmGUKYp+jMkiSpTRPXg3YdT2XcRQvBEdld7hYcwtQxzKSPESqGLJQIx2tgnh3OSNNXtMO7OE7puURgrJYCMq4a5sD7hQTdnm68hUoMOl5NubcZS4+7+crrw9enijHmKmuY+P0rlRgOTOY9AGtdr7hGvcqY9lTuSaQiqdQdSSXfhabns/YHQqTDcrtXrGqNUGsk5xsuWpcBe7/saA1OIivcN2ZLQJj0PV6vvPbKWyBI3i6porlHjhwVcIwVGuCnO7q+TIsfmKXZdrxcsPMMr+3rUkVRvsEFxKG57xkWmmVhzvJzw9fWE1HBphaR6D/1deA450G8WciuGgmJJJIMJ5M3jLvJUnXuD8SxvpAj/ZLO8Zw2DE7H9Ko+8PtmABqNb0oeldYPztES2u8pEaofsJp0qrzfnCDl7SawdZock2T01tPQurd3hjI+6JzXqmQu9NQ/jwLDOUTpX7YE0oWNAbU/XBipZDT9wtVdp6njAuHxdB7mCFJC4490bzO9qJ5PpNozI3W3JdPCdyKJUcvtpRUurmLGx3hu66+3uuTQrRlc73XGwW4p5uKuOvYh0BHoP7bLyxmLqaSqyxMux6BSHkXZKfhpJz7b7A4KZ/JIigXQKFbmeEoY1dY23ElFd1li7t07cuYKWSr7dOEqpj0o0DgBarqPkLPOrh6ada8Amy6FuVcirHkya+rJgzkbjO6aD5kh/OrTaZPZrc1CFq5DTQXlqbQK/w9iSwR15ukOpNopZq9EhHlaVcD0NR3btQT7dyoFXqql8O7iTaXDEZq2V2xwB9WXYAaCE6Gug7rkIH3fKJFwPod0BUJ86FS+tBs+u6nCy8UIDM7ByjtbL65YcwilZUmep5FXaTit0v2VSM9lfcI8PnIHf5inXXjw+CTyfiMoOI5JITpWMvpGBw7hV1at3Ed/AkwqGn63rsrfS0/TAplxckUpouO29yvJjbKnLctyvR17g1C7YILt7r6Ek668SeymfEszwgkq53JuAV89g+HILIyHhEd+t7cDrw8MasoO17q13tra8KizjOMeoaLaRiY9FFHQRoTQn3AK504a1BNuoc/EirdKYrtlWEeKxGBHdoSSgV8mAxwChQl3vgdJ3VL5kAxgvPRBSV/pSSx2cLEuRoeHkDKF+g1aKXe+uHD5IsN8GI/BSA8qtL+uwKWsuUcrYJroy1A025N3Vt6NzWF08ydejxGwHeH8BI4BJqEtFUfWlwF62V0LZLE2TPW7o7eF0OBGr/r50hRAr6wu5D0gMoIG2821YPE9KrU7bvgFlCbtFhYAUuXxv8Twb7O2IH0gMlvtkO+AU3J7IW7W647wCh7LK4OmpaXcxXaOFQNmhhFL88XaSS2jtC30rBvrWXHerstrXwxqEKrY8RTDN0HzBUh2nVxpV89dLaro1shLvBsQzon4PojjJqHUaXRp96WUjosEJY1vnc3e2ZJZl//a3tw9v358hvv2bb8XNz4n+nz2uej5Zen/L5fGINHSDzw9en/9dwf7+4a31UyDW8/FcVwzx6zHWPzyc+/ivPf+caUzPl87en7Y/n+H3bjy/m/2WVsHQ9e30tauLx/suYAdAtPlVzm5+29cH33943vtS6Pujtr7+2rizSdNqfoclDFK3D1+n8et55Ye34PUI/StOEl/Dtpk1fb0nARTEPyGf8Lff/jfHuriQTy8AAA== -->
