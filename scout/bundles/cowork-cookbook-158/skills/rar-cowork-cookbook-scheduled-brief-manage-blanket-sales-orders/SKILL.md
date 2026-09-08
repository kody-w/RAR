---
name: "rar-cowork-cookbook-scheduled-brief-manage-blanket-sales-orders"
description: "Builds a morning brief on blanket sales orders from Dynamics 365 ERP (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then drafts an email to the owner and a Teams"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_manage_blanket_sales_orders", "rar_sha256": "b48da0277a22816d389d2c54ec48f2b11f164836e94ce8a76abc8d6323fef20d", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_manage_blanket_sales_orders`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_manage_blanket_sales_orders_agent.py` and in the RCI capsule.

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

Manage blanket sales orders Scheduled Email Brief — Builds a morning brief on blanket sales orders from Dynamics 365 ERP (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then drafts an email to the owner and a Teams

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-manage-blanket-sales-orders
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
      "description": "D365 legal entity to query; defaults to USMF.",
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
      "description": "When to run, e.g. weekday mornings at 7am, daily or weekly.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_manage_blanket_sales_orders_agent.py` and embedded as the fenced Python below (sha256 b48da0277a22816d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_manage_blanket_sales_orders_agent.py` first:

```bash
python3 scheduled_brief_manage_blanket_sales_orders_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_manage_blanket_sales_orders_agent.py   # or on stdin
python3 scheduled_brief_manage_blanket_sales_orders_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage blanket sales orders Scheduled Email Brief — Builds a morning brief on blanket sales orders from Dynamics 365 ERP (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then drafts an email to the owner and a Teams

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-manage-blanket-sales-orders
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_manage_blanket_sales_orders',
    "version": '3.0.3',
    "display_name": 'Manage blanket sales orders Scheduled Email Brief',
    "description": 'Builds a morning brief on blanket sales orders from Dynamics 365 ERP (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then drafts an email to the owner and a Teams',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-manage-blanket-sales-orders',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-manage-blanket-sales-orders',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7e623ad7c694f318',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-sales-orders/manage-blanket-sales-orders'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/scheduled-brief-manage-blanket-sales-orders', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query; defaults to USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'When to run, e.g. weekday mornings at 7am, daily or weekly.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where manage blanket sales orders stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on manage blanket sales orders for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads manage blanket sales orders, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on blanket sales orders from Dynamics 365 ERP (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then drafts an email to the owner and a Teams', 'example_request': 'Give me the 7am blanket sales order brief for USMF and draft the email to the owner.', 'inputs': [{'description': 'D365 legal entity to query; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'When to run, e.g. weekday mornings at 7am, daily or weekly.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a daily or weekly blanket sales order brief for the responsible owner, as an email draft plus a Teams channel post summary.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefManageBlanketSalesOrders(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefManageBlanketSalesOrders'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'When to run, e.g. weekday mornings at 7am, daily or weekly.', 'type': 'string'}},
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
    print(ScheduledBriefManageBlanketSalesOrders().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916adPaWJbmX2He/pDOxrbQhiR3VMQICYEALWgDKV3h1C6hfUNLdv73uQJsZ1a5eiZ75tPgcADi3rOf5zn3lX57s7s2Kuq3T2+qb+eLnZ2mceTXCzv3FkzRF3UC3orEAf8XbpG3dex0bVE3b+/fPL9x67hs4yIH2zddnHrNwl5kRZ3Hebhw6tgPFkW+cFI7T/x20dip3yyK2vPrZhHURbZgx9zOYrdZoGt8sVXkxbvUD+104edt3I4LXRW4nxd93EaLtigX+CJu/axZOOMizkrbbd8DK4vMTmMg9t4s2shfEB88e1zUBfACmGDf/doO/fcPb3J/aBdgFzC3eT8vzhdebQctsDlf+Jkdp0DLQ0jR568I2AvNt7PZWX+wsxLY//bpl7+/fwP607dPv725qd00c+zcyPe61Pc2s9OCnQOtm6fb6uy19HAaiAHXQrC+HEHQc/C99OugqDNwyQPBen171/hp8H7x7/+e9HYdNj9/+pwvXq/Pb/M/pcsfhraF3bS+t3Dt0nbiFMTs44JOe3tsFrXfdnU+56MBOcvDj8+d3yWBgP5t/u3dU8nH0G/ffX4rgAn2HKLPbz+DVAF9dTd//jhLKd/9/DEter9+9/N3OU3n3Hy3nYUBqz9+eX1/iQULvy+Ng8UXVd4yL12178alD4T/wb/59TT9Je4Vki/Pxe+K8v3ix5Jnf/4G7H1WpQPk/lgsiAHY+fbxVsT5u5eOurj7uZ27/ruf/5VYkGA3SeOm/T+S+8tTcOTbIO/vXiH5+f0jfX9fLF++fZP5r9WWoGD+iidg+Vd13wL1r2Q/MvsPokHbgGb6mssfivvRhuXfFr/8S9/+qw3vF8HnN9ZP47lTndT/tPjtUSK//OR9v/jT338Hov+3YtSiq92HhC+ZnceB37RfvvzyU/O4/NPff/mpK0EVg37+0tXpj2T+KK4PPX+K4GvVuz/vBfr1PMkBdCy+9dDit6L8H/XvHxcGwCjv+/Xm0+KPnTi/lovZia9KnyH4Qzc2wNY/xPHnt98BBuXAm+6JZwA//u3fFkLs1kVTBO1CdYuuXYAEt3Hmz8ZrUdws4idG1j6IaxODwL7WgfqfMzxbXASLX/+n+8D9D+4L96HmK7p9eWD6HF2Ab19euP7lgetfnrj+68eFNiNoHYdxDpBcoWX587w6b2f1Ze03fn0HkOWMrf8BdPaH+cMizhe//gUtXx4CP5bjrw+Ujp9oqDD8jIQNkPFx9vkyQ/zTQ3eG+MF3O6ArLVxgWBADce9BLJoivQMknePTJHGaLrwYYA2guPEhG8Tw0yzs119/dewm+pw/oRtdPLmvgcCCb+YsPnwAHgZpHEbt59x3o2Lx02+//7T4z8V/teshfNYhAzJ5ZQhYeFAlcQE6rsvAMpA8kG4AJ48M/fb7K85AzExVIJ9xMLPgvBlUbOJ7X4Ou7ukPCL5eOD4Itj8TZ1G3MzfG7ccFHyy+2QuUzj/NjBEVTbvw/NLPPT93RyDVBu58i2RezFzexk0wvl90jf/Q+qtT2w8TM9D6dvvrQmBkwE/Fg1TrF1+BzUUeg/B/K4nndSCk/qlZbL6K+LgQ5xpdlHZtl1Ftv3QE9jMvgJe+bgfCbcDs/ed8pmR/DtWjYZ7hAYtAZNxXSj/MOQdDTAYqy2u+6n6ssWcW1R5sWn/Om1cz2PWcCheQA1AadrE3U8R/vEqqiYou9R7xA5bOkl5Z8F5ZedTgcxT48Qj0bWhYbB/Tx2N2WHzukBWMLf5/HqfmwNC7nbLd0dqWXWxFTTGfCZsnzDmxz6F0NhpU7bM5v884X3HsK5x/ztMYVF89/sdz5SPNrzVPiOxqEGSFVh7yQY0Bc2a5jxaYS7quZ5/tz/lX3gAuLh4gCeIN8AL00+zMV4Xzr18tjQAozN+/zxCPkqm92WFQ5ouyc1JQgoHve47tJsCqem7jV5pBP/hzS/dR7EZ/8mrOGig7IH9OegziCuL48RuWP3/9avqfNj5HpXnLY4zsQBfXDwHADn82cE7FXAbAvPY50AM/Pz2EADeysp19d0AfZe9fF/3ar7q4AQXzzDWIq18C6P4wvz89na/6QwlaBwQLNEjZgeg+WmounQwMQsAGgCqgw7I4B4MBCMorCA+BdjbjA8Df1+T6lPi4/HLIf/ThzGhfN86OzHvmIeHZAnY+/hFGtB+VCZCXzSseev+x0r5pm2XPUNoAOAQav/76nCY+PgeC58Sx+Cr30z+dmN79tUPVg+L1PxfAp0XUtmXzCYKetPyVlT8CIIOetjbfGfrDAyY+PLnzwwsqPjyg4sMTKv6k4un9p8VfM/NPIl5t8mkBf1x9XM0/nV5l9nqBqDAfNuYHbP71c6743xEXqAeA086MkI4zEH2lx69LAEeGNcAwsPhJl83Msj0Amwc/gIR8zv9Y93PfAfrJw7lOm+IPePCYE0APPPP3jcbAT3kLdHvzrBn6H+cj2mx+4799yrs0ff8GINX/Kye8mbOyucqb+YAI+gnMcG3sP749QGNo549/PjxLjw92+nHB+gCg0uaPlfhimplp/9AwT2+Bly7Q8H7hgRjNbDB7Oyufm81uQPWCwp29asdyduN5GJzHxwc1fHlSwz8bxM4U8if2APhXdf4MsuCkancpiCW4NHPKD8V/G13/WfYFzAfzXq/4NFPl+xfogHcQz/eLbycH4NTrLDdr8PMOHJN/mU8tc5QfW+YPYA94+7bp298lHP/t7z+yayajf7ZJ8ZsSENljKH7yVQ+GNxBjHxTGMxsPdgNF++S2R5/90POvvfgjxwFJPseh9wv/Y/hx0ft+MjPsi+QBB7ULYiYYD+h4DDrzinT8gSKg6QHKgNrmsHyP93evi8fBbbYJRKl9/p3htzdQnDaoFvtVnq/JHywHGPahmWcbCLQyUAi+P5sO/PZ/cyZ4iWoiGwyiQJaDkZ69QgjCRhASXnsoSXmIi2O+i5EB4sBwAK8xEl37FOb6pE2sbcclvTWKoIEfICsPyHt28Zd5lotn83CKCFYUhQQYDBaAAkUwzyPX5NrFCWRlU46NOzhlO9+3JnHuvXx++jgH9NvxZI7Ny/Xf3pw1BlbusYanny8GomAHwghnqK/L64oc0v7SlZwdJ3V0uNzzNX+31o4SFyYiX22FazbXcnuLlR200aW1c+kvR1peqUGTQGfCwkxdNfb21enwdoWG/emeTIfMIpcCgU4pK2HY5DMrrTOseOemSdVXkWWrK1UWadwo3WXUGOlhexz2SdOvQnJcSfD2DmEIBXHNdBToGEliUSAZS4Iv8rEWpeTaCrV2YafgoPFSoK78IJBg6URhx5WtXJqWr45nPsZRDAtOcEzsMLboxKN4EAIGZc6NYZ/2bnxj5ZIbhCiZ1It+joc9cS7EpCSlHk20Tik5cXvBad/AxnB1ipjDMg35ia41ZUsVLnNkrkfsSLCJEieUVjJ9ctdxfcqlxD96SU37bDlSwbUcoUCuO+iUYBBEeIO57Hze3wRloSPH7mw53MGl6vHYrCK+1ZgUT90o2lIMiV7GpL9K9lkscsYa0QlF6MGNrF0VZRt6rXgpezd8+QSHpHZM7hZrNnuWq/ojQ+K9dKL9QROOxqo670JTrPbbYVs5EOdsxuRSEL5xv7vqCYlQQiAhm1azIDriQrVX/Linp/6ewvsixg21N07ry7I/bEMecXA+04XheN1RTEAJaxZOahTnGiE3+UA/QETG9rcEz9HUIJwEZcdsl9n88WhEonK406e8wNqjWNg7kxFkfMMlZnBK4h61htwM8N7wpDg9CQfMjJbVVYZBHErfDHshmE/E7SCuL+SSv8H6fpJTDt6ol8iyGPuyVNd6N3JwvPM2S+VIH1PXi7bdcZjWXm5qx91w0XXT93vd5veUIRIcr4vE+YyU+1AlLGg3jnozyViXDKt4EztclJ1u5xS5h8fR3NwZ9eosK2M8KaTMtFzZ6BVs3D2jzu7FqYucW7Jf6amnEtKqa1bo8nj3TvcthBxWlc+iJ2IHuTuJumvdFuVNI19aa/aQQC2zWnJ4F4+yQop3EQeTUN5dMXsihx2lD9eQ5VL5cNuxDK7FfaoNhVr2ppYxnZO40K7XNDNF+NiMR8g7Uf2dlCwZrtAmoFgeCTTrRskBtryG52plYMmoXpBNGdJFc4MNdMM6QI/UrE5iFTPBdT30WOTusa1Tn50aFJJEw1xssOyhlLRunzqIOh4qSLdVuVprt4QUrIY86Il63mn+QdcvbMHzF0x0p4LGzX1uBPvO94+HbpOfeWVQnXH0uutmzC6GhjaYcEDNDL+hveHvW5Jtb0WWpgUBe/LJPlnLKb44LeZsAhnZGYVlZCLApP1Kym7rPDmv41GV1pS9Jvd4MdjJ7Vi3fA1lN473kCDE88CK8pQQT0vFNiHHELYjs72tURI924LBSwfkiJ3YqxpRpk+L8h6FNMEE1Qzvtxu/USuKr3US35br7c7cbtSK51XUIJb37VlBQpepEExay5aR99jVSzFoWE9asHIT212WFAQPx7GA/a1aLGWVvp0igazOZp9KQX+2DLKghc6OoAPHHjisEbeUOOG3aIDa8rymtquVlDuFQ2qO1CA4VqNiaGBnPmIAqkW0slN93Lt55uXI7CN8UgRxU59os2lvx5s1egSyZY+rMdePMRRdIhNtIjcJO23oLbxjSndHCC7RxmR82d820yXB5Iy4c6oGac2Ehg1brKPLniblATYiZL8L8pJL9+2e3o43P+e0cqBEpbMtnMVY5HpL0RNEHlRbQcuzNbqaVbDZESlMdFcV2pnE8SQ6dv00rUMGUXqhi/tduAqNlRSSxfUAD/omJJdubqa53BcNn1hrHpW0zeUc9hfXTIcysZC+UDZV3xDwknIxuBWZ8aheNwM/HqO2HIsku26iPbxSx7xH24rK1b4WYJXpaM5MzlbiHo74EdCKsSkt0aNYmpLp8BBdwn1RX9m1phd4fd5URmj1+8uGK5XKDLywXw5Vna4apO3NbR2vmKnBbeK2cZQuHZVmKKjKu1rLILjimAZJ50pFOQkTxlxVdSsKRpO+C/JBVjFzpE+Sfd91E1Wa0qbte8hmtoJE2WAsrdq9cL9doKUt32GSWt550LtQczgGO+dA4M2Flulms2mx8xYRVqfdJeWkTdcZFRcoDbtfqttCmTYaYZG+d9OvKCZ12Ap2uSi+yV6Jn+Fxx9B4eaHRUO9ZLKVZ16KjI5eu/b7csGqMuZdWiPPrwb6w2k6XMXzPHifaK4RJzMqCQ3rBzW53ppxYmlSsOgwMvx/jitqJVcfKlsxF6Rr2oHPI8NsVa6Olo0Scdxqd4kyxZbA7bwduW5IXVSNXSdTYQRZMKTKOqM3U+DqzCpXm6/3B6ZN9w0wwrbr4SRPrzIs3Qnxu63KiOE+I7LNwUyQzd0peV0/6XSzMGDFO0HK3Hvi+Cw+pYk+EXcNMWPoMVRRX016fqjO5F+lb72LJMZYqjznXu2MudCroYI11o5t4qJycL6B0uFvMNjYAzTUhVu7iDX/FBAa0q11yMbktt80WpW64u6f0tQqfAPun8fIkhJEm2HdzFfb6tqf3Pbszqgpp6skrByHmCkFnjIhnd/geDewLZRxOWAaHqngSWIQVtZtv3CC0tCvT2S6VzoF3LSUoLbH3TmePAxkDg6JdW/xeShFhE9Hrw5Rn7enMbXhxn0i6CGqCNHtftvWchq6KQYZaDcsjLkEaluhHikVlF1aOJyExzRsVXQtRo6VT46tRqWuIoAmcKO+2gDzOd7e6DUE8UcpKdHcFp4YQtg64VBx4tlKG6Shtl4YkW2LC5yYHRyFCUe0KoVEwHg7hbTXJbLD3GkMzDZGj95xhX+F8v+Ykay2z4qbIEknx7rcV1KEnwd0FQ0YD0oS4MqtY366WG429J0Zoi0ilbk7OKUqSm5OZB3pdOHQer4+GYDhxm3R8ElEOj1Qbq1RFfTJxb7UhsFPVrvcCrSfGrU1Wt2iTslnSU5fVLXUhp3SRE0RgpI+hdrhiTfgm6ycyPJs2s9JZ0Tgx4/3kKrsxkCqZPfLADG1FmyuogKPNOqYbRaDqnsr9EYernkvCit7mkaHkej0paCGsRy6majMrq165h/kegu55ZUA7XAqRrUsKHJ5RJeHdt3edjMbxiilC1J2rw/ogLnuxKJjl+rrLTxy1X0JCf4I07sqxm+TQHiPPCLeHpK3OW5UByKd3jhUcLdq29D7nfddIglst7UactHz1iGPWWYyaJc/p6THMktIpAsst9ITVAwmv+HDDU3a2XV+2e9jlb7axA2cW84pO5qWftGq1v7d0NRW7mgVD/WhjyY52sghXpksvaQmYjZzhLDXycF6WdeYWF3JbE7rHKIhm5dzuZhnCznVbOJv0NIaSE8wpNr2JPaa7tNcr08HlpXa4+0Rj+oFUR1SguQPisaG99WFXLVJjOtC2pqQtK/JVyeWBp+TkWbdTIfbp9DrGtWGu1jRd6fdQErUJVlJuorVyg28KcASxWt7rdvQ2yJpRJq3TGVbPicVZ52478bGgdYPmHeo+5PSkCTPSzJaMAOn18Xgs0fuOhshAdtCj7ahcMmQi5FCKV9OeHO3uRMIUg0ZcmmMTiMfsqmxWq6Dryc63kGqKCnoFN66KlW25yVi8FEpyhB3SQ/hma9QDDx1DkSb0WFrireDTRZ5jN8Vteg8LOiTfOsuMF5a3KmFXGQbR2rnACmyVJ6Z97mLFBiWTp6dNrZu8mfsbYSWVZzBmetQ+a1L5NtaVYCJFsp74RtsKzrFmxdMOvx/iQq0Eu8gJIoKLW0mkEs8rXSbRcXHd0KomZjjc8rDQ+y3MNUOtLE1KTGTmbAnVyUqvaKfRetXInDDxKOhWCx3Z3XG3vpYiQ8p2K5rd6SoXCifdw42HqcSYcNd0C3tr50r1mL+DmGvD6zAxEHl+ieRCW4EDYxtS9AW1HRPqcyMSuPbMnrMjftOsE8IsU52LK1rGjvsEcyW7vUpoZiG4n2Bb5CzdGJiXJLUXCLZO20EoDo2J7ORYQAiJ0IiSUsGsG5zY4ZgOO1c/eIqOTRg4/0VIZqfXek05m6V2DleibHRocPagrnLuhdYJDRbjCmceM/mYkhsn2Y6TQEfttNq1XHKDvU1xGav7WAqicfWkOrIz+KjTxCXHe6Jy7ZCxEZXWrqWCHnJyK1Y3XZiWoQbdMqFwOFrTD93R12gkverrda7TRyuTuPB615Y3MBd0TNLEZkS3CXKQeb+CwZwROtQazJ2szmaKwOCTelc2TuhsD+KAdL1StLvLVc996FDxMDeUVsAbU+XeE2088NfRvsCFv9fyoFWZ9eEEToi9p1aQZsMuugoGxVLx7lpm0947wPmdFVjZTikV0XLT3WAHAdbW5RqGiVG9I2gwSDippRUx+WE9KCHrn4jlnvJuobtn7pIDV6mP6tGFIQfbAfAu6fBpQO5ITF5RK2tH4i4Ngk0Qt76LuhtzdbxOkWrUYPYadHGOaW5m0Sjx53VFChuPmaxTRbPUcq0c66qzxKULKYidreVoefApuzhSx+UmwJkTaI6gy11sZ1H6mc7peFdU6dmdwJoyLA/jPdLWVLc8ebVNGkvrhFYX21Kv0LJOVgbato2rEbaR9htfa43L+tQuTd9pZGQ4sQoiodE5yc5tE8kKYeKdDiAdQ6HN1uEu1yReOlcICyH2rK7oHe4kbVtnNgXTfXIYaq9ScHDaP3G3/Jx7+U5zMdQQDngJnZO8kvAVcogCkt5uTeeibrshXIZNOGSeNwwxYQlDJ14omUmtBJcnZlgG2v6+gVf72g6Ds9CxhWS7VOaJk7NnzAaxWqyv2BuUrLV4qM+lhKetqzdSUoAp5g7Vnuh5kqcnU747XaYQ0oi2dZobg904EYMvEi6X2yuDrtvd0inX1oSrU3a9XpWG8WRlh9zOJKosM06tUugid6ZZN1NxxLaKSItKSZN+0HVCRxQTNrQVnyv1ZQ3vL8oOTlbRdX/I4NpGDA7zjqIvVFs4wkPSGibhhvhuX91JYWRvOZZZCeUNTuwtDxV+joZwkIZEUa2Rj0yWx4Vg1aBesrOO/a3YufLYp+0V3WzEdn9gXRQSVuVWzg6dWDNNn/XqKlZJZ0NaoOmoUNzvG4kPaMSSLwaJO3wWXeCDBKUpRZKeca27zt73Nz4d9yavBZdmWTZhl6WrUWqIErDbxICjqsfBsIFBJEJX90OQEmDiNgJJx5edDYUTwB3DoW6dGk9bMM3DBAu28cOKK7pMp8ygiYbz4I17n7ha6R1ZWntw9igkRMtwm8Qs0U98XoDq8+5CQwXJEK7uWdez7OcQDh+qtdtAyL5BwVGvIkGlkX3v2+5UawpUr8O8ZbBzFt19e2lDmpFfsEY4Y/BJNu1bhds3eKQI9NQzPFOoa3DV9+UtSTNHBfJzcTvsWosd/P1mX2zGap3q4KC7RAiWrgE7B5hYEyzG9SQvloRLYjh0WeGFix+WnrFH/OMtX5o45mnd1KJrwPIJ699ZYn3BG1Nr9RhTSDRQcDDnCZ6waVuknqBhe/UgOesgbePoZ1uW6y3qtIwkHxHJVmHoytSpoHmkjhZMXjlOQGr2svVRuErkbSWlNkD0qZQ6OK/ugurLLN6s83Hr4YZ8HQZB0gLBoKtYMQAT+gdRP60pRLj0CKPjWZClOXovphjFyOuFvjjgPGoGucgkgQmT45bHYV9KdN4MsHPpCRN+MdXIKgidVMGU1y8dwyDyoks8WTrwy1p0HHGcAvjQSZU+VqEaiAI9iuuoOUFNpUk2hFR3s0YKeWo3Yig59f2UYfzAqVLPrDuSW1bM3QqJ3X7txkITkaMulwOhBjg53ZW2vOKGTpQ9mJmWKWLLHou6RTw62OpITTBWkBcHWVv3Ukkn3+9SR1nWdolAh9YsTqYPY5ctqkBE2hw6eHMzPOs2dZchdFEpnRzfLlNo4Hgir/cX67RFd9p1Cd8FY2uKV2VMZQzpAB4sJWuv7pb3CxgKNVikNRWRbZfDy3qzV1TYXGdu2KKX0tKvUeb0E85qnYXfeRP2kca74IFEXFbTqiDxaWkqG3jwA6w2MGAu5JukvA9WmWcoSMGPxdRH5XYZbyaesQU2KluIuMt39Fjd08MhJxzvLJTGenkKMfEmllqFnm3/eplSmfIsdadNPty0MIEr0ilLu8jHI4QLVucrP//BT4PO/UnEe+GiSuSuLc8ZJNynK+EURRF7N6pp0hqtJB+WqSOWLw9oySdmXewZS8AlGMp1DMeW8NKTmeP9tturcrTlIh8QdgkgPqMrmyKynDMZ2glhf8+X7bKBHXdYTeM9ZqKYiqR7Y08kKnXZ/sosb3t160+DwaLHDbarcr8h94lBXfLouAxw6CbZgXe1IOnWsPcOBoekewz4B1ndqey+cjYIDtEiQ2Dc3r3TVIg0GTgoIdfVyTuSYlyBJupW3Qi5LRgtJv4YQvA0cJmzntT6Yt976LLJG2OJI0SI5HCbZZzPQ3i8a8FZNC1uFFW7e1EYfHZjU1dyr5aTc3Urvw5WXCVXJJ9M14CBzRgACoAL6CY2HKBfRfaUfaJ0CYwqhNutoxpLEcCAh2Eve6pcthsEU1dnXd9TK+iorKJEmO5ofLvv4p5IKM3LkD5GCQqCT5TDnguozcBMnl/woSanm+pftuVRgK8dZW0qT8Xz1dnJOfWcotuWlcKj6e9iUlrjOYFTFMnmvamz5cStPcjsU3w1suwg75oV1PpMgbZLYdogR4IpYLSN+9wkl4wrZiVgv9WWpum//e3t/dt8o/V1u/S/8zDXfHPm/9k9ouftnK/PZDxuHPq29+mh69N/y7q/v3+r3RjY9rw71qRd+LqB9A/3xj78hbvxs6Dx+dTU13vDz9vOrR3Ozxq/xbnXNW09fmmK9PGcBtjhdM38VGIzP7jqgvc/3g/9B9fAlYeiL23xxbWb6G1+bnB+BMP3Yrv1X1/D163D92/e6xGiL+ga/+LX5ez16w4/cBb9uPqIvv3+vwCIty4ENS4AAA== -->
