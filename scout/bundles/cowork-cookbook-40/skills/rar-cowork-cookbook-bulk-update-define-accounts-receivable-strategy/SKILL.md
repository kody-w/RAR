---
name: "rar-cowork-cookbook-bulk-update-define-accounts-receivable-strategy"
description: "Applies a bulk field update across define accounts receivable strategy records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_define_accounts_receivable_strategy", "rar_sha256": "a15e6b10e808c064db3d8eff8892b430465ae4871a61bc0cc05f45216c7b2474", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_define_accounts_receivable_strategy`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_define_accounts_receivable_strategy_agent.py` and in the RCI capsule.

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

Define accounts receivable strategy Bulk Field Update — Applies a bulk field update across define accounts receivable strategy records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-define-accounts-receivable-strategy
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
    "operation": {
      "description": "What to do: run, plan, checklist, describe.",
      "enum": [
        "run",
        "plan",
        "checklist",
        "describe"
      ],
      "type": "string"
    },
    "subject": {
      "description": "The process to automate.",
      "type": "string"
    },
    "trigger": {
      "description": "Optional. What starts it \u2014 schedule, event or manual.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_define_accounts_receivable_strategy_agent.py` and embedded as the fenced Python below (sha256 a15e6b10e808c064…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_define_accounts_receivable_strategy_agent.py` first:

```bash
python3 bulk_update_define_accounts_receivable_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_define_accounts_receivable_strategy_agent.py   # or on stdin
python3 bulk_update_define_accounts_receivable_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define accounts receivable strategy Bulk Field Update — Applies a bulk field update across define accounts receivable strategy records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-define-accounts-receivable-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_define_accounts_receivable_strategy',
    "version": '2.0.0',
    "display_name": 'Define accounts receivable strategy Bulk Field Update',
    "description": 'Applies a bulk field update across define accounts receivable strategy records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-define-accounts-receivable-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-define-accounts-receivable-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c6f2abe196e1d0a3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/develop-sales-policies/define-accounts-receivable-strategy'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/bulk-update-define-accounts-receivable-strategy', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


# The toasted capability. The upstream entry supplies the WHAT; this procedure
# is RAR's own method for that shape of work, generated by
# @kody-w/skill_toaster_agent from the metadata we hold. No upstream text is
# reproduced here — see the module docstring.
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.857, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdateDefineAccountsReceivableStrategy(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateDefineAccountsReceivableStrategy'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'The process to automate.', 'type': 'string'}, 'trigger': {'description': 'Optional. What starts it — schedule, event or manual.', 'type': 'string'}},
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

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

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
    print(BulkUpdateDefineAccountsReceivableStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816aZejxpbtX+Flfyi7ySoQEgLVXXetBiQh0MAoJHB5pZnneRL4+b+/QFJm2e17+7W7+0OrKqsERJw4494ngvz1xWybIK9evr4orplBrJkkYeBWkJk5EJP3eRWD//LYAj+QnWdNFVptk1f1y+uL49Z2FRZNmGdgOlUUSejWkAlZbRJDXugmDtQWjtm4kGlXeV1DjuuF2XRl523W1FDl2m7YmVbiQnVTgYH+MN3LK6eGvCpPgRJQmBVtAyVh3bxCfdgEkFMNn6s2g4rK7UK3hyzXyysX6JamYfMFqOXezLRI3Prl608/v76E4PvL119f7MSswa0XGih3vmu1vmtDPZWRP3RRnqoAUYmZ+WBOMQAXZeC6cCuwWApuAVOg59UPtZt4r9C//mvcm5Vf//j1WwY9P99epj8y0LYJXKjJzbpxHcg2C9MKk7AZvkBU0pvD5ImmrbLJecARYeZ/ecz8LikvoL9Pz354LPLFd5sfvr3kQAVz8v+3lx+hvALrAc+A718mKcUPP35J8t6tfvjxu5y6tSLXbiZhQOsvb8/rp1gw8PvQ0Luv+ncg9RFpy/328jvjps9D78lOMPPlS5SH2Q8PwUWVd25mZrb7w4//TKwduHY8hfY/Jfenh+DANR1g01PxH1/vTv4Zgp8Gfcj858sWIKx/xRIw/H25V+jpqH8m++7/fyc6AWlWf3j8H4r7RxPgv0M//VPb/qMJr5D37WXtJmEHsgMk9Ffo1zdF3DA/fXK+3/z0829A9P9XjJK3lX2X8JaaWei5dfP29tOn+n77088/fWoLkGuumb61VfKPZP4jv97X+YMHn6N++ONcsP45i7O8z6CPTId+zYv/U/32BdLMJHS+36+/Qr+vl+kDQ5MR74s+XPC7mqmBrr/z448vvwG0yIA1rX1/DKr8X/4FOoYTduVeAykAKBoIBLgJU3dSXg3CGgJ/p9oGYORWdThB2WMcyP8pwpPGuQf98m/2HUs/208sRSaQfHvA49sDF9/ecfHtOy6+vePiL18gFSyTV6EfZmYCyZQofstM382aSQUAhrVbdQBcrKFxPwNY+jx9AegJ/fIXV3q7C/1SDL/cOSB8YJfMcBNu1W3ifplsvwRu9rTUBijt3ly7BesluQ2U80IAv6/AJ3WedAD3Jj/VcZgkkBOCFQF9DHfZwJdfJ2G//PKLZdbBt+wBtHPowSs1AgZ8qAN9/gys9JLQD5pvmWsHOfTp198+Qf8X+o9m3YVPa4gA/p+RAhryinCCQOW1qTsR0RR2ACv3SP3629PXQEwGiBDENfQmYpsmg8yNXefd8cqO+ozhy3cKAlSTVw1AbwgQEcR50Ie+YNHp0YTvQV43gAgLN3PczB6AVBOY8+HJLG+gGqRn7Q2vUFu791V/sSrzrmIKIMBsfoGOjAjYJE/AP5Oa90Fgcp6FwP0fafG4D4RUn2qIfhfxBTpNuQoVZmUWQWU+1/DMR1wAi7xPB8JNKHP7b9lEou7kqnvhPNwDBgHP2M+Qfp5ifidhENj6fe37GHPiPPXOfdW3rH4WhVm5d64HqgyQ34bORBV/e6ZUHeQt6B4m/wFNJ0nPKDjPqNxzcP2faCcmuoe2917kwfrQtxZDZwvof0e7MplBsay8YSl1s4Y2J1XWH+6deq0pDI/2DPQKEJj3KKXv/cM7+ryD8LcsCUGuVMPfHiPvQXmOeQBbWwEfypR8lw8yArh3kntP2CkBq+rulG/ZO9q/Ag/doQ3EDFQ3yP4p6d4XnJ6+axqAEp6uvzP/0ztTrYOkhIrWSkDCeK7rWKYdA62qqeieAQHZ604F2AehHfzBKghIB0kC5ENAiRBEAjDC3XWnHJgJ6u3u/Y/h4RQqoIXT2kBb0My6X6ALqJspd2oQANAUTWOAFz7dRUGpC3wMVPzwcB2YxUOZqf99KmhOscjTKUF+F4Hnw++ZftdlUh9INUE6AV/2ExA77u0R2Q89n7ECyqZTbd4n/THcT1uh39PS375ldx0/sB+UfHJPyu/OgUCppfUdYyfEqgHqpO4zgUAm3Mn7y4N/HwT/ocvXPzX9P/y1fcGdUc9/jNxXKGiaov6KIA8WfCfBL6AKEJAjYeHWd0L8/CjAz4/K+/xeeZ+/V97n98r7wzIPr32F/pqqfxDxzPGv0OwL+gWdHh1C252S+PkBnmE+0/rnxfT0Wya730P+zIsJfJMBMPAHE70PAXTkV64/DX4wUz0RWg849A7FICjfso+0eBYNQPrMn2i0zn9XzHdKBkF+xPCDMcCjrAFrO1N757vTNiiZ1K/dl69ZmySvL5mZun91+zNRBMhi4JlpBwUqCrROTejerz7aqOnijzvBe60BkHDyr1PJvUJTy/sKfXSvr9D7fuK+XctasKH6aeqcpyXBUPDfx9iPbablvoDdXDMUkxWPTdLUsD0b6T8rMVUa0Nh2J9rPP0p3WvFPQsAX33erPwsR7l/M5IkfdWNOJB4271VfAz0d0BK9QiCOoBpBgQHcbMGEPy8D1qncsgVs6Uzmfvffd7Pyhy2/3d3QPHaav76848gzBs+uEgwHBfu5nvgSATkLFgTXj+wCz/67/eZTHABC0OAAeeYMd5fWDHVJlLTR5cKx5g7peh5JrjBrMUcXS9x0FyQxM5czy0ZtG8W9BY7NljZhYQtiAeQ9UvbtwXxAJGaaNmkTs4WzIsyl7c5Ra267M2zmEHMXxVdzINxdAG99TI0Bij7tftg5OfWj9Z388zT/1xdruQAjd4uaox4fBllp5hIjLDmw4Grp6sYV4axM49F0NtdmaLeMAuEUMyqdmUvZ3ewJnrIV7aTueGN9aTYm3eWSZ3PwcCWyUaRCJdu0YX/BJKfgMj4eDZJIhBVp7P2Q6WVhhvKxcszxU2Joly1TXODYYEt5jx1YpUiS7tZuyu6mCQ0ay2QyOAs+I5CV6tzS1i20xOA2zm7hg2Q8DUTUJ34Vd7YUpW6q7G/6ltUbgzHQJHET5XBuZGwfDbjGhS22KNd7eQsXbLnAuNmROyu1nHaOlRhrauF5Vr3oRmPpdiMPH0jcbQ+7wQpXesnWMz4pDFpr1f32UNlMiSo4mlibY+HKahsbXXHRr4ImyWQ2406azOldo2FEKMUnWezPalmFNTCTC1fHwzZc3Zr8sJV85NZxqp+nzGF90ge0b7Yyvg7lQLuk6BDzFcEuGw7FVlvQFDl7LNBWY9+M+bg3bnZh0ZHB01ngymYq3M77gucPt9NVYQJOcmI50zFm3BjlNZrZOE4z0vWCc03OMSxN9qlPJi5b9N1lLK0TfpwJUkTws/NR1NzyTIs35FxeqMacH3dNeYqk3e0GD9xhe6lZdDCpW6WN/DwtojBNLqqxg8eiWOcXfsaCULA9Im72560p4bfN6hjRdGKJm+7KutZBHsd6p5R44Lbu5ep5yw22n9k372hVpFmz+KBoRkos7ULG6GqjsaWeznn05EctYYSGY+1vfU1ayzzUKsbc8B5Za9uYrxfHHXI9pkLNIYs0UhZnycv15iSMu03XqIPAbqOUufQBvsYzl+iKkte0LHUi07lVfb9q6zQU7YKLD9kQL4qFrbcz8HMjjVmUz60d3V0Fx3JuclLzEX5EzcVmR5IjeV0PushR3ArJL1uWhCO4H5psQUpIJGKn3t5vTRlpJFRQ6EoPsb42t2NcE5XpbuwqBinFpQHcdwKZzhm2Puqz03ArKZ4uSJs8F6mCaTtyy2UGHC/wbZcJlU+CJCkOnDlskjpj2/3FZmOKooeNbmCNrgTCTcCodbDTXe7cM5ge7lnFjWapsz8v7Oh0W/CNvc9JocuMjm0MRD8td6PqBuRmZcKM1nnBQeuCZOk2Q8l7GxmrDDLDWrOYc9bMC+DtbIH2+HlsT0iFSCJtCrJrFCd3d7uYq66QD+FKu0oYvaPdC5arWiFfbCeqpb4Me0FPUc7nutthnK9vc81tmx1repJ2m223Fz7v6bBSKRyV5X2wgfsM9fQscuEdv20JuZZQBEH2hzN9xW0Bn4V1whRNpJRqUbHFDCkVKdCToLwpdhbPJCNrJJXptEMhNYmEXx1U2IHEcEZaj456F4qZ73hnPBA4LJkROy4jt0dkY8JmHHGyiCTLzaCbpibC9N6OvEVJooLqZE4VzMVcw0EtDFJjSTdLAa06vE0xRV94N3Yfq1dUQGf7VGW1sxlLV0qVypV0nGGsbfGMq4F8i3UTAO44I6+JXM50DIdL+pSVPFazMCGWNyHdjvnOSIytEohd78zbvMnh/IxVvDknpDUF74XO2Wd9vKIRu9KPs/XY6D1+UqhMrA5bbw1z21tcbmiW8shkzxx7ZBdj7GbFIkwVBDTem06uUKsQh29HUcRpnRYFcuXHu+2myyrYPR7h0hzno2/teLRFj7UU1ZRO60d+FUaSujwtioMq43rE9I7QMtJ2X3LzsaAsTRzZG+FfNreThNJzNtlsrr4hbYuGVOYqD58pgLrMmcpZhzfTYdPvabgce9xaR8Nw2Wj0jkCpwzUJiEuR2oRY4BMApM7JKk4kIo7Jys2KE4eut9HJXi4RNSz4vXC20Fs6y2plXUv67lqYI46QFrVtndt8R8TczoDZa4jaw9lHkFWpLdP1IGVIQ5F6y9B5gONGq0j9gaPVRgljwSrG/Sz06fPhpi+rhKPmWO9ZmsBjSb+7UmFjtFwiMCt2lmi86s94csmKskAtj4moVpSp3/p1epTYUZqjJcVuA5VNd9qa0onaTVhVtMexGcu9Vat4nC4YoRhs59J3WTQ/rme9sCtgWI2y02xvy+rldmEXzHBYO7GJj2rSYPFBw3dUO9zOJ0KpsN71qVC2sHplL1U3jRvyqB8iseIc2wzXTnKjpswUqtkpTZuW0AiNGm6Ycej7Y3CKb1J5zlvTVAnEXi7YRbzaGAu8ltf6agsIrqBuzn4j21i8rQ0+Ma4JxslOsrNZz2ZIep9cGHc5NrlqFgnDbBf84Kv5ubmNO2aMzttuppQYfwjkmLHbgGa313yFbobwZJtlqrSAYutgvUm1w9LODbwYKO5Q02mfLthNf+62dnE47BfF5RosqXm53eNqvNUOZF2iZ+Nowty4NbxeD9Kjx4tZujqchlJBg7NS6v6xC+0aObouKEzsfOCzTPGo1ql05Die8VFU2eaScNfDOJys8rYF/tniZZqC3l8XV6y2tMOzsST6C0Xl6sldrkJfRzbOJTygQuRs9zKh5rMTiDfFVVZ/PqzoReGXzVITN+acd7dsoF54fpQPjT+LKUVKhk0uGQFTH6NyxW13nDKIWO4jh9BR5qt8yOXUFzxVRNr12jO9RpjnusAwxahSnBWSxEUm1mY+liZKVooueh4ioisPPuWbG2/Ge/q62WFp5FkDt3CaKj+bjhpVhg53l5liWdFoKCt2XTpMilidZpg5r7ERx1y6y9DtJDk4agpVb5fIiGO4Zle8voO521HWg46bs7pyrUiAS5uzOficXaGgg68v2ZW9lviwHndszJu4VBawWMrH3Y2Ic3bvXPhrJLHOzva3Q5lcSx4tbT1ZKSlHUwNLbuc822OYHB2dKjyH8mxQV/TmcD2EBbM7HFUU02pQjWbEDzxzcnqGcjY15s3oLi6OTdMGGz8zNEsScfss5gfjFroAClp+bSN03hOFhmOKpcQOZyrsJSTJtRb1IcOHUnNC+L4GzhhmAwJLiSYUjoyj3Y6zSjsW2KNwrjwW43qCb1J7UxqeXzLi8hBEp1JHSpcZ6uVVZW4nQ/PCVmXIMVVLa9gYEXFRvWK80J5JlEgu2YyA2sixrG1lNnOc8WYztrHXbNlgdtcqq/R9Vxg35exEyO6imM6hGou9yzjIvqiwg+VGx06bq/q6y0PlgqecnM64c+RL5QHg2d49oFmyvkl8EnOLszxbUcyGSHyBbhfSkmHGWVUJ8R7NxOvyNC82g2Vwo26IMmdgywHxYYIfN5W94pqrlEiO4WpiHjfcJjUHM6ZJeoSPZ44iTOXY0NqCooZWsc8SNsrrmHbOdBvLoJ9bFstwQDuSNsq41aTdBtCnBVrgIil033a4yIiyZBx2hicsOEpmZbfOt8V1b2yyedduu63J+Ccys3ih8Q7H8KoRF9ct1wy26E7nPYfmx/0lVpJhq/uWv0+vHntay0TEetmZX/nqkW565Ki5RuMV4u5ERGZw7PWxhzdlip9lm2xnp3pFXyXxzHoWvdUKAD92ng02eyZFVy61TOENOGxnxm5rhafCROKIL9hWCKMYdbetZhhrTayP9NA7KRMPx2PBHuSQZm1tz1rcrcymDYHQ4quOKuRjMUqUkQOGR2KYvji7loBH6cSdmIKKFmEpWcGcgjfSAbWFfLYTN16Zn3aqu2fZsTRmSuydz9vLVZ1LMK4sHWm86S273+LLLANAmqy8s34EqXhZctGqHNLTau2oGFmhe8HdVs1CnLUzoQPwvoTFZbn2na6E3bmwusBdTVdNkDXrzmvnVnkNti7hIyI8FLND0xDMmATIzhRyqajMTG1lA5DfwZnt2Mwgj6fS82WaAmFrlTbEAk8IlkRrVkrssmwv7xepcb4MYkhXEdLPuQiVTqQ8Kvuyu+xm+tnMLH+gxLWj1faqUfBmFtUKVlU3fBlHSzSjR3MpYHTkDeyV3GuWDrPwcawrYlVS1Xq9Wu7CAaRVu8rM9eoa+ak3dh2C7bslne4BjiHIWSQtV52viCorVp61ohPsvHQ3MLai/TKM1XyPbEdUkHYe1xx3M9y68XPJtp11tFrbQyX50eIgRfx8YJZnW3JBX7sG7Ml48SiOlXsx9avVavVIXqjFvuLmQuiv5tSu3Rr7vPMwHNmbDi5HBmNt55Rf1H0ERx1PDuO4LH0vIIl2aaMRvPHU+VVSZ1xtjbCMMhnuOY58BRh06+pRYZlqrW/mKhYsx+6UUb3BiXjFkm2aGQMX5B6htcKqcYzCW86RbLdLj6Ft1Yyo0ynHZV2/OnR+y5LEiVhFfL1vrybpHGnjRh90zcCsyISRBLZweW6NJq0Rbr472qe5OBfZ5XUk6JNEbWEc7NH8Kluo276hwm1rKzy2qVBlpRxSn7Brb6bNU5rudYo4oHNbtc81OZCdxpHIgqNRfbyN0cDZTI3RVDqPdEGlhT5E1Iy5uk5xWy0AXNW0Re9hLrg2Kh+tLmt6Qbqqoqurxa6U9oqBZCZhDAuRi3x/FCw/CeneQrFeOcM7V12dL+KqlZqrVp1XAiIOFbWRN7hyQarMbSzSmWsY11rpqcOJUNVTPAX96twneFyxTruAy/WFdT1wyEDEwB0thWPWdU/UGKHzynIjbOx5J2XwTFqzUdaxy6jrET05WfAmFNgGYWp6vrNEVge5RRXSwa1bASvN5cVZF/Xc0ax4rs67rLkU26DcievblUYbWcxHl6GPe9ArHUL/inoSjKyxG+dTQ+3xI2pk8gKTFrBICzc+mc9UcWlhO36ltcGs21DonvDsdOvDZIMhM7k3b8YsmweOAC/h1GbywPaILoPRikgpCyMXho15NIvBy9rqMjdwMuMEsIGUa8vxr/NtZMPtfCEiZGd7MbEkgW3YNW6RlUyB7cxCLkLKJE+yPnOWIayt4B03lJ4t50u+JOh6DODZgdQvvskw+rY04UM2Xy6121puTtqc0+1WihE1cm6mdbMOo6p5bLLvtEXdw+pCXO7o/NZ7kn5Qzjq/N9fXXbrOHczYl20zXvBKaJrTvClaXFjuFs05ItbnSCB2o+AWm1VEL1xhvShKk2RwPMDjtc5tqmBvH1R9g3d0Iieed07R5BSRCzvZxKyYKJiJH91ElC+z7NAfRKfPNleweUa3ls4i7nje23zm7cndas12l9tgXqtaxMV6PBGE7Q8wog8xuVjmp8gpULmNJHmP4SektJlAKLxjo/HwatIuUg+S61KEovrzpDoM/g3dSRlIdkFEXaaDQ0nwmzUxqnBpWzK9Gh3AleWcJTBxtzWcaFyse8E8gXjufYp6eX2ZTrKf59H/1ZfT06Hg/9jZ5OMY8f2t1f0w2jWdr/e1vv6XNfz59aWyQ6Df43S2Tlr/eXj5785mP//FVx+TsOHxNnh69XZr3s/4G9OffuvpJcycFgwe3uo8ae+Hxa/A0fX0Wxf12/NQ/OVuclo092cfJoKrvHLc6q3J32yzDl6m34mY3ia5Tvh4PF36z6Pr1xdnAIEEW5G3+RJ/c6tisvr5KmU64p3epbz89v8A7149oWUmAAA= -->
