---
name: "rar-cowork-cookbook-scheduled-brief-define-sales-quotations"
description: "Builds a morning brief on define sales quotations from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves a draft email to the ow"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_define_sales_quotations", "rar_sha256": "73ab3f3507ca5bef599625eb4d464f42120f8b6f4f78ed2f7c5a51ff554e82dc", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_define_sales_quotations`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_define_sales_quotations_agent.py` and in the RCI capsule.

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

Define sales quotations Scheduled Email Brief — Builds a morning brief on define sales quotations from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves a draft email to the ow

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-define-sales-quotations
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
      "description": "Dynamics 365 legal entity to query; defaults to USMF.",
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
    "owner": {
      "description": "Responsible owner who receives the drafted email brief.",
      "type": "string"
    },
    "schedule": {
      "description": "When to run the brief, e.g. weekday mornings at 7am.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_define_sales_quotations_agent.py` and embedded as the fenced Python below (sha256 73ab3f3507ca5bef…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_define_sales_quotations_agent.py` first:

```bash
python3 scheduled_brief_define_sales_quotations_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_define_sales_quotations_agent.py   # or on stdin
python3 scheduled_brief_define_sales_quotations_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define sales quotations Scheduled Email Brief — Builds a morning brief on define sales quotations from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves a draft email to the ow

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-define-sales-quotations
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_define_sales_quotations',
    "version": '3.0.3',
    "display_name": 'Define sales quotations Scheduled Email Brief',
    "description": 'Builds a morning brief on define sales quotations from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves a draft email to the ow',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-define-sales-quotations',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-define-sales-quotations',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '573ce4566cc5975c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/estimate-and-quote-sales/define-sales-quotations'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/scheduled-brief-define-sales-quotations', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to query; defaults to USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'When to run the brief, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where define sales quotations stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on define sales quotations for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads define sales quotations, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on define sales quotations from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves a draft email to the ow', 'example_request': 'Send me the define sales quotations morning brief for USMF and draft the email to the owner.', 'inputs': [{'description': 'Dynamics 365 legal entity to query; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'When to run the brief, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a sales quotation owner wants a daily or weekly (weekday 7am) brief on define sales quotations with a drafted email and Teams channel summary.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefDefineSalesQuotations(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefDefineSalesQuotations'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to query; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'When to run the brief, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefDefineSalesQuotations().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916WbObWLbmX1Gf+5CZF/uAEAjwjYpoBAIBEpKYBKQznMwg5kkCsvO/90Y6x3ZWuW5XdfRTy+GQgL3XvL611tn88eL0XVw2L59e1MApFryTZUkcNAun8BdMeS+bFHyVqQv+L7yy6JrE7buyaV8+vPhB6zVJ1SVlAbZv+iTz24WzyMumSIpo4TZJEC7KYuEHYVIEi9bJgnZR92XnzFvaRdiU+YIdCydPvHaxWuOLrXJa/JwFkZMtgqJLunGhqwful0+LrqwW+CLpgrxduOMiySvH6z4AIcvcyRJA9tYuujhYEB99Z1w0JVACSODcgsaJgg8PZZrAK/M8KPzAXxTB0C0AhVmMD/PGAkh3C2bp/cYJu0WQO0kGuD6IlnegbDA4eQUUePn0628fXoAA2cunP168zGnb2XZeHPh9FvibWWn2obA663v+qi6gkTlFBBZXI7B4Aa6roAnLJge3gIkWb1c/t0EWflj853+md6eJ2l8+fS4Wb5/PL/M/pS8eYnWl03ZAGc+pHDfJgLVeF3R2d8YW6Nr1TTGr0wKHFdHrc+c3SsCcf5uf/fxk8hoF3c+fX0ogwkPYzy+/LMoG8Gv6+ffrTKX6+ZfXrLwHzc+/fKPT9u418LqZGJD69cvb9RtZsPDb0iRcfFFPW+aNF3BHUgWA+Hf6zZ+n6G/k3kzy5bn457L6sPgx5VmfvwF5nyHpAro/JgtsAHa+vF7LpPj5jUdT3oLCKbzg51/+GVngXS/Nkrb7l+j++iQcB44PrPVmkl8+PNz32wJ60+0rzX/OtgIB8+9oApa/s/tqqH9G++HZvyMNkgbkwLsvf0juRxugvy1+/ae6/XcbPizCzy9skCVznrpZ8GnxxyNEfv3J/3bzp9/+BKT/j2TUsm+8B4UvuVMkYdB2X778+lP7uP3Tb7/+1FcgigMn/9I32Y9o/siuDz5/seDbqp//uhfw14u0KO/F4msOLf4oq//R/Pm6MABC+d/ut58W32fi/IEWsxLvTJ8m+C4bWyDrd3b85eVPAEAF0KZ/IhjAj//4j8Uh8ZqyLQF4qV7Zdwvg4C7Jg1l4LU7aRfJEyCYAdm0TYNi3dSD+Zw/PEpfh4vf/6T1A/6P3Bvpw+w5tXx6A/uWJ5l8eaP7lG5r//rrQZqxskigpAH4r9On0uQDoW3Qz66oJ2qC5Abhyxy74CLL64/xjkRSL3/9FDl8exF6r8fcHnidPFFQYYUbAFux/nXW9zGD+1MwD9SwYAq8HfLLSA0KFCSD5AdigLbMbQNDZLm2aZNnCTwDGgLo2PmtFX3yaif3++++u08afiydkrxbPgtfCYMFXcRYfPwLtwiyJ4u5zEXhxufjpjz9/WvyvxX+360F85nECFeTNM0BCUT3KC5BpPahUHXAacDOAkYdn/vjzzcaATAEqNPBjEs61b94MIjUN/HeDqzv6I4qvF24ADB3M5bJsurkiJt3rQggXX+UFTOdHc6WIy7YDpbqaK2ThjYCqA9T5asmi7ECN7JI2HD8s+jZ4cP3dbZyHiDlIeaf7fXFgTqAulY/S2bzVKbC5LBJg/q/h8LwPiDQ/tYvNO4nXhTzH5qJyGqeKG+eNR+g8/QLq0ft2QNwBNfz+uZjrcDCb6hEiT/OARcAy3ptLP84+X8ylHzi2fef9WOPM1VN7VNHmc9G+JYHTBI9eAYgyLqI+8efS8F9vIdXGZZ/5D/sBSWdKb17w37zyiEH2nzQ8X7uExfbRXzyahcXnHkWW2OL/5/5pNgrN88qWp7Utu9jKmmI9nTW3lLNTn13oLDGI2Gdifutr3rHrHcI/F1kCIq8Z/+u58uHitzVPWOwbIKVCKw/6IL6As2a6j/Cfw7lpZqWdz8V7rQA6Lh7ACOwNsALk0iz9O8P56bukMQCE+fpb3/AwTePPVgIhvqh6NwPhFwaB7zpeCqRq5hR+czPIhWBO53ucePFftJpdBkIO0J+dnoCkBPXk9St+P5++i/6Xjc/2aN7yaB174KPmQQDIEcwCzv67Jx0AMqd7dvBAz08PIkCNvOpm3V0QVvmHt5tBE9R90oKIeToY2DWoAGR/nL+fms53g6ECaQOMBZKj6oF1H+k0x04Omh8gAwhekF15UoBmABjlzQgPgk4+YwPA3rdu9UnxcftNoeCRg3MVe984KzLvmRuDZ/w7xfg9hGg/ChNAL59XPPj+faR95TbTnmG0BVAIOL4/fXYQr88m4NllLN7pfvqHEennf2+KepR1/a8B8GkRd13VfoLhZyl+r8SvIP/gp6ztt6r88QETH58Y8fGBER+/YcRfyD81/7T490T8C4m3FPm0WL4ir8j8aP8WYm8fYBHm48b6iM1PPxdK8A1pAXuANt1cCbJxRqH3svi+BNTGqAHgBRY/y2Q7V9c7QJdHXQDO+Fx8H/NzzoGyU0RzjLbld1jw6A9A/D9997V8gUdFB3j7c28ZBa/zSDaL3wYvn4o+yz68ACwN/uVxbi5U+Rze7TwKgkQCDVuXBI+rB1oM3fzzr2Py8fHDyV4XbACQKWu/D8G38jKX1+8y5akqUNEDHD4sfGCgdi6HQNWZ+ZxlTgvCFkTsrFI3VrMOz8lv7hUfBeHLsyD8o0B/KSB/qR0AAOs+mFEWRJfTZ8Cg4NZcUX7I5mu/+o88LqA5mPf65ae5Tn54Qx3wDWaMD4uv4wJQ7m2AmzkERQ9m41/nUWW29mPL/APsAV9fN339S4QbvPz2I7nuILz+USYlaCvgx0cn/FgCIq2cbR0ktzeAfdQyELnPavZItB9q/p6MP1IclMbveqEHjQ+L4DV6XdyDIJ2r7Vu9B+WoWxBO/gMOgMUDjkFRm+3xzdDf1C0fY9osDDBP9/yrwh8vIDodEC7OW3y+9flgOUCvj+3c0cAgkQFDcP1MOfDs/3YCeCPTxg5oPQEdYuW4q3CFI4Tn4KATxSlqjeKBi/nYGgsxdIkiIemuQywkyMBHQ8LDHXwZhjiOBSTqe4DeM3+/zI1HMos2ywUs8hFAQPDtMbjlv+n01GE22NeBY9b9TbU/Xtw1BlbusFagnx8GppZugMLuuDdhE6eSMRJNPekUFF1PyfrmceLNmhKRbvGusZdta263dqoeRQer0qN09u8ae2Yp7oRuYXU1pdMd90qULHqq4Tc0cksnMZ1weEtch4worh5mgNlD1/f7C18Mt/S+v+hKVbYG13JGzDvduTguU05ozcDRLlhMwRDRYbpuD7Wg6/2knMr8fDVu91rTFSyWrbW2ChNfhAVTUUoyTE2N1GxIaYekM/ghFTLF0NrB9MxmCR3xtSgcYG6rCKbjuDsnQRNzdBiLEfP0OGQ7Ydd3issZWNtV0slLNOhoHUXWlCrPVQKZSZ02WgVLfVvuV8oOKTdMdOaHo5MLDOEgphcTmcch+wEvaz1xrFVE7qaGIKETfFtDfj/pqx06+beJWK0GLocYmSnoWtxkrb6csCLw8SrSHGUnaNI6yUWcixtvRJBLj/PYWVl3Hn7rC7un10mlu1HEZbp4xi/sAIctkYq6ah6ovCQPl4YutanYWe1m6m2F7zP1jDFHyrSu1lXD6Hq6u5l77bD1qfFVF8qIrA6BjpxYclEb6JHK9xu8t+rrWRoNJvPGnhZPQNkxqA66lE4mllvuxr9dwjQ2IBsvU0K60g3VbwvyHmx74gCR3rReVhe2kLjt8kyaZaLmUY5DWXRWuKbaX9xajo42t0sRp0x9D7U3t2ton40uiAwXTVct0Kyh0EtqqTZf40wx1k4D2wpEDm5VhvW5dhg6laVx3JYCdUFqX9+hbXWIyfOR3RsqlOCCcL2fgpNy1I5o7A3XLRZjmHpykgCtkfKwP5vW9jqIRykc2taQDxO/rw7UibbqjX4gLET06zvT7c6rSHQ71HCW24rfJcayavX1lK/6GpnoA4eeu+GuQFw5laYIZXKewbGxqpf3ghz6jB63BsTe0Gh/V04cEdMjP9hk3reDsyPM5S32XKFNEPhk74+MGNmr4k5xeZxtKeSO3avyvtPvB16/O6xzRngtqPLl6jR45zsqGfEtF24hZMN4Ae3kYj2IqAmdh7ZAhjDUThCbYdzQcbvhkKZZ5Ki01Am4QWFn5Ngm10amJxk9VzLeerRgbiA6wh0Wdu9jcefLXt1GtkyPock01gi8w60bLSbds38onOuhi8W0VjkEmIPjovV1u+nppbGmj6eN12dk6Kb6RGpdxLpxeolXSNXu97hvy7mB2l0yyNPuRjt3CUBhyIfGoTDxulAHW0T6azqajc0Vjc1fqwufqrVHxhMJ++TEqhd1WqlEeFTIyyEpo1ForD0sStdE7sf2AjuE59u92IWjsOIJIGQmnDOXR+ElXxzWbOIlR75eioy2THvaFtiQOkwA7VZ1La+hpaAK4yhmuNqteUbfRmp9sE9LKkX6lcpfs5ulktnYnOLotr9g7JBPWohAmOONTbDCA9XqpTHZKPtIUmyxuCabK7PFiQ2bGZMmxoFRXM4ppap00Sc4Neg2fLlnvnK2NFhrEQ7ay0sDI0md4OH+Yp3PxV4mNhCAiMB22J480psdRY0ddpCI3davWW6dr7brZuRZ6X4vdKm8K4ZwplAeL5tDLiHolXI4F0YNU1kdeJhcdhm7Yew1POntsvYhm/TaUhbEGgrZuycO0x3DRMq6tyQe8avyFEx6djylrZ8NvUMhsUCszYGUhZDX4rWBphGXBjSesMd9oyoZ3TKnABKVRj1CN5WhBFrXrNLru60IndEzJE9bG/fvd8M+aq26J+76ZaseqczNNmGcSTgD6Ssh5r3rAZX0g9NWPBXezIuM5tFkr3XlaGcDe9LlCAyS8iFQCx1BoCI9GhfU3zPtVb9LqmBsE0mIevskqHjPnSV1MEOv2rOtyFhctVGZ1b1fryTvMtAVW3HHDXGno4KvYxLlWHxT96a0dJab29DtT42sZXV+4G7c+lLxuc+22po6Ts0aPzInazQuF6uC6QyBripASUjdctiGOq/ZHadv7BFvXeKExtFquWLZrhHOkbvED7cTDV924pIit2cFlIRwL2L8UppuYg0zjr3CSlQQaFekO+HMYIGaXZtzHJawvmba0urZCN4cD5ZTN613z3u8F9zq6GPteIu5aHPCmmGzL0+FclVbuseqaNdJdx5haPoi2TbOpPpB2jNYqgkd4qR7przyRyyF4XZTpFuGg4G7rXiVpbudjU671mw4fWwcfb/zZDbZFJcSqyilJC4MnxtLNBhRuTJ3rhVc1UtUJVsoVEzuEKwGP45pC8r6UeQEluFj7gL5hyF1QlRgLjJraaPZjVQfq2fKIjNW3LY9r+JHPRdXXoOPROImO2WrejdQzctmS2cOP3DtKds2uJOJ1U7HieR6akxTpKNK7c4aNCAmzpkqo2bjruDG8WoOmkqLSlkGHJRQEsfYmCghlnk0zlklkEuZkUYkr9ooqSC3UYdtQ9e7PTDoipa2FL0aBYEKhREUUuTcjqNmXYrmHg3KsLe6pDqUoNXI+NpO8IzP+dNGFjYAdkWn7OoLhDre/bzpYY6uLFUY5qbnIt4MaSxlpVOUq7zJ2ZV2MAz6RCyXQs6PtOHylN4EJidR1zop1Vw9kdV250C8otcqETksbV2PgbOuGB0xED1OJZaTSUQiy214WnsZHZ4jnW7dJpMmLCcULD9L/AQLnq2I2qGsS5G8N5kgVQmkq506SDHOVx2TKbkQ+WUc2ct9FKgwVSZb8qrz4bkhj6abCHwvwFbGbgMA9DXR+tulrBtev741nXg/EajdWoxpF3Hf9egeJ/f8dcOm5nZFWfQxTvL+el9FjugwyG0XT36xr/JgF2BJZnC4Ozh2HaF8fYtsmsA3GH/167x00N6yJWGFp8z5UrNnkYSkTOP2x6W1H8UDTWx4+SzLno2ocpHBd244k5qjHwNWwOxExlcbRUsEud3j1XBS8J6IcUgjTXFNKb5CqzlyPV4t4bArHY/LpbwvzaqzMms/ZcuNLW5YfvQL1klJH3JkendndQK5ybXnurZ+Otu0hGzFPdPnQmXmV/hsoeVpt9zXucEVbKicUHgVFI7B9qO86RRxbVe8hl47HMrXV223V8g4hTCcrRNNhNMIVuV7zlNLkd1XBUnZdw3Kzb3BMqkIGTzRRYIqinpiIbRjIJUHptN2I17wlZxjVibQaLtemaeVhG6CQmzk1i/qs2nrpagwlzp19No4nruzGTmMyCS3iDm0LI9tR+eYxaqJ5ioDn+TKZeRjowQjjju+to8ya0dKHs8rpzpeK5wxIRYt43Ssa7F5LA+WAJKG1I/MJRD3ih+CcpyPZ7nON71zX0/eXmf2EzfWSEvTqeOUOX/VlbGDMSx1KmndMK5C0iM3Cnucs/V0QLRUHuXDBUH0pCl4Z2OQ5r2zhr1tJLs8ErVKOEx7htaW0vm+y6vlul6q5O4g0Gu8wRi1yhEJ5S2uzTVPhvHTkFmZxEiZQFyF2BqliVv6YpDKdMSVKhYoFoGJhWM7+5FyzOE2QdeL29NxPXg8iVmQfOM2UBsh5La+h5FjbAm+ua61Si4TX9msyPCYDl3fljW779ht1jvqjm4H6sZ1VV1u0ImjTGKQoiY6RO4WJCxxOwTbyt2liVKDdRgdoqutswmO150aRBstsC2J8U/xCcewaK2HqgArm6VlR5J7ZZit2ErXTcSw+q1usQ7dXtulWE/7lYU7A1EfmO7ExFGSBsLtXBN5lTuxVW7WV/ZWX/JRygsE6mONsazkJGCeJJCH4tgZdY8UuzSFK0mT2p2Yg0lzNTDsuupRbw1NFu1n1brK4+0yFRvfHi76tnZcVkUOmi87EKEdBEWWV2cxwGgkExn0Vg5TV4RFQpDiauiQzNjt2NXp2Hor3UdM/1APq3PWofnqRG5s67xxeXoSk75EMABt18rYOHXojCroNleslK2K3fXgtkV3zMOtWhuj1TZdbF3Yy8Hu/TMTEe1hE9nk5Av1fUjaCtH421QOZtGK0YXFveaaLAXluJWQ6dxQoSa2u0oe2QOyvBAGEa8grOup+FiNGWnUqspU3dZYIjJi81OPjq6FqPQFEQNX2B/M4kL7AYF3RzBP9Fpo2mloFZsVVm+EmJbwU4Q16nQvKYGV747YFqUA4+Jal1ivMtYrcRcKF9/0HFjUb5CZ9zuhD64Uo6xwT6cs/2pmVJJoZYqVe0GLETIeNqD9Y3Egh+at6UTyu3FnYs1+OMXLLmULJxbPm4DDikq2lvzFhiIvqUZKP/k8poy4aVSHvDpiQcallOmCmRh10q0MG6OvsZy43OfQsQZhs4czQ+R9fdkxqHkiEZbLjqhW98xyIPqE6P3VJfGgHaQtjV6VmWawwzMZ3n387kl35IYiBtFjbSsJsOPC/e4IhtehvaEjaa7svCOJ23E4OARxvfdxkHim6x0VqVkZG1hDLq50vFl5PB7KxFBwy1uzeWQatMmSK/pyqSFDJj0KFNEcD69lSWR5U6c3gruVe1nFShaZio04alB3p6vzdtxwQWOB0NWBLVVu34O2QCIuJ8UoMdj22PLi2Ip5wsGMeSQmDj1JfsWOOH0Sk27p8yh0CI891bXqHfGvN0wXhtR0T1ckQGUiO8EEJMPziFFOh9SdKBdOKoyDuabrFHhfK73lrrzN5nyjm84JHf+o2a2/3mpg5nNB21jFYCZbMvomWxcJWWSnjD6rcWtj1zV/RTajJhBtcDmGlJjLQ72sEL85FBuoRLkJP1zIXWF5nSWTiYD5zORiLX5f5UfOUizIkkusWYVIWrsparbxSecKPxU2+bgMmZNZhH4XeLlnxu7qsKsDv/LTkd8npJdeDQ/H+nLy3ALM7ERX2A2fuYHlkwZ3xzFqi1+ObGLs1ogv1iYewHbcQax0vdyFq0o7qbrBSPiAuT5qFMM13Cp79rLM6lPLi7VY8S3KHhrTaLv9fc05rYVzRryOSNBPHq5o2N7rG6mPu7jAEjulqMFNOkgciXM2JAM6pLFajeLGYgX8ECLHws95WxrYkvdOSHntwhUn8aB48Xg82rV6OHtciba1SyeqGmnh2LeXXRvv270S73ddcRAKdjmEAUqVPnBf0aBLWJqmFQEHFLyazj5DcpftILLEuircHAIA0bexUZj76zW3VhAXI5pu4A1c6Qxx9+3D6ggTajAQZ+e8DJtJkWHL7fetwaxo+zKlO3bwBsEluHJuj9NAj3TvzuacR6zc/UoF0z5+rcoRUlH5AlvTkRQ83TWL8w49RmZw1W7MOmnuZJiFNrR3juv0Np0E0A1P6mW3DOjeIadGUUJjOGsgOYW9YjepoRWg/FdedF+yV82akrULgo1y97tpg9C6ldFLdFdclRVLt1EIK7AqbTJDObjX+/l49JKkNpC8PHVJcl8Pd2bV047vmZHLDhFadGv8NjlZM3ntmiKpidNkfmDhE+nxtelhVN8i2uHGrjHRQzqJry+eGDgE4jgkERSFtF5SBu5TyvZk4v1SxgWO8ndl0BhVUbilZ3AHD8oujc00y51yss5LLM8rIiT8YSBcs44wpUQak28De2ujPWUPqRaXoOnqzFSAcz0g+uHg7QI72PQMmx0aKRBkfb+mUGF9dzf1YSzsTqHcrTsUuGdeaN6F+sAKdzIDMLwix62A40FQ6oIVjoq2lq6TMuoHI7CFSSdHmWj05iTUXIqEI3M8xiy8t/qjBdtygqyQpBz298v50HrYSaLq68nS9rBTU4lLWQEhbV36gHQ3N8OEzUY93Zmxv+vwUoDbu39lPV7hQdYeuB1OBoMBwwnrdIkEj0lKXkA29kg/XQmV2klaexlPTB93t2oXE0tC7eSj7K2yqkJJ22vCkzkwdWa77OWkDpPNkUG+zBpdltOhP0KxzbPBCs0ns6g3PtWKO5k688tKyIlphEtvixnKebR3CEWBZrM7hqcDGOWg24WZKm2Q6cwogxTbr84lt1P8penmylbRgqXPpKQIkYejhWho4o6oeOnc1eVYELelT8NSIQvhhuPcUMBvy1A6B7CX8pMLeWRz6Oz1MTncz86oqRt8y55yYOHjlTgREwwwy1ET03f3LZd5t8vo7TZd1e19b80RGdUT2so0Jse4B8fGaYp+7UuUildTqXslFRu+JuBXp+DH4rKL42obA7Qyz1BXeyBv3f25KzbBAFmc2EG4MqJdiJgJcJ8HmrPlgcZMsRDQ3qN211RzTRuh7jV0sCghoc8XHE+2dHo5QhYj1kV/8/Y0Tfh8c8dEuUfyKcxF3tFJPz0UBIVAm+bEXny/g1qO4mVRIU6cftLLU4Tru+U1HpamTg1yGKzDpWLX63U+BUezo8M1coUFn4Q8GHX2sASXyKZbkxuKwTGO9UIaj1Gyjl10BCPgPb2AFviCXV05rAzWX0EXT9EuE8QVhAFM4C2dyA/Ym36hvMYf3Avu2lVsJifIiRtTHtB7QlW3cCcpMZWB9N8jW3Xwe7dXgp4gPVnxujLX2AqTjhuaO3ewWBWMYzHlNarVmoHZBODqkVUGf6m5Q1NZF+8o4IQ+Ye7Zb0VHPRg77Q5JG0oUqpvS26HXulMZcThsEY7s7Uy4KaChSCaEl2HvAOFIsuqqXUTW1JJeX/rTksiNu0nGJHsQOqI2zpy26xj+KpXBLmklHDdPEzWRTEG7Kausdmto2ZTJZNmi1wOQa0A8seXB97ihwdkkrwebtIsBk2G6rE5ZKFvnM02/fHiZj0vfDj3/3dew5gOY/2dnPc8jm/c3Kh6nfoHjf3rw+vRvS/bbh5fGS4Bcz9OtNuujtwOivzvb+vgvnqPPRMbne07vB7vPA+POieZXgl+Swu/brhm/tGX2eLsC7HD7dn5/sJ1fMfXA9/eHmH+n0vNRO79M8aUrHzrNB1xJMb88EfiJ8/Uyejv6+/Divx3cfgGj8ZegqWat387ngbKrV+R19fLn/wZ6+gZs4C0AAA== -->
