---
name: "rar-cowork-cookbook-ppt-exec-record-tax-commitments"
description: "Generates an executive-ready PowerPoint deck on record tax commitments status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_record_tax_commitments", "rar_sha256": "b14bba12dafe2c8fad1ae6978500c53bdadb59aa7773ce3e130e81357c185af4", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_record_tax_commitments_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-record-tax-commitments:93be03b3f16fcfdd2032c49f4d1fc79b90374c9c9c6349260e60561def83fdc5", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_record_tax_commitments`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_record_tax_commitments_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

Record tax commitments Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on record tax commitments status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-record-tax-commitments
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_record_tax_commitments_agent.py` and embedded as the fenced Python below (sha256 b14bba12dafe2c8f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_record_tax_commitments_agent.py` first:

```bash
python3 ppt_exec_record_tax_commitments_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_record_tax_commitments_agent.py   # or on stdin
python3 ppt_exec_record_tax_commitments_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Record tax commitments Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on record tax commitments status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-record-tax-commitments
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_record_tax_commitments',
    "version": '2.0.0',
    "display_name": 'Record tax commitments Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on record tax commitments status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-record-tax-commitments',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-record-tax-commitments',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f5ee99bbf19dcffa',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/record-financial-transactions/record-tax-commitments'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/ppt-exec-record-tax-commitments', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class PptExecRecordTaxCommitments(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecRecordTaxCommitments'
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
    print(PptExecRecordTaxCommitments().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6aZPiyJLtX9HkfKjuISu1b3ntmg0IJEALQkIg6GrL0hJa0IoWhOjX//2FgMyqmu67tNmYDWmViaQID/fj7sc9QvXbk9M2UVE9vT6ZwMkRyUnTOAIV4uQ+IhRdUSXwT5G48B/iFXlTxW7bFFX99Pzkg9qr4rKJixxOl0AOKqcBNZyKgAvw2iY+g88VcPwe0YsOVHoR5w3iAy9BihypgFdUPtI4Fyg3y+ImA3lTI3XjNG39PNwrU9AApIubCPEip2rqm1KNkyZxHn4ub9LyAq74ApUBF2eYUD+9/vLr81MMvz+9/vbkpU4Nbz3pZTODKhm3NTfORfi2IpybOnkIB5U9RCKH1yWogqLK4C0fBMjj6qcapMEz8l//lXROFdY/v37Jkcfny9PwY7Q50kQAaQqnboCPeE7puHEaN/0LMk47p6+hzU1b5dAOaGYFjXi5z/wmqSiRvw/Pfrov8hKC5qcvT0U5IAth/vL0M1JUcL2qHb6/DFLKn35+SQd4f/r5m5y6dY/AawZhUOuXt8f1Qywc+G1oHNxW/TuUeneoC748fWfc8LnrPdgJZz69HCH0P90Fl1VxBrmTe+Cnn/+RWC+CLk/juvm35P5yFxzBuIE2PRT/+fkG8q/I6GHQh8x/vGwJ3fpXLIHD35d7Rh5A/SPZN/z/h+g0zmHwvyP+p+L+bMLo78gv/9C2fzbhGQm+PE1BCrOsctwUvCK/vZn6TPjlk//t5qdff4ei/6UYs2gr7ybhLXPyOAB18/b2y6f6dvvTr798aksYa8DJ3toq/TOZf4brbZ0fEHyM+unHuXB9K0/yosuRj0hHfivK/6h+f0G2Thr73+7Xr8j3+TJ8RshgxPuidwi+y5ka6vodjj8//Q7pIYfWtN7tMczy//xPRI29qqiLoEFMr2gbBDq4iTMwKL+J4hrZPJL6qykvFOUl878i8O6Q7pAinDZtEKly4hSB+TB4fLCgCJCv/+3dKPSz96BQtCybt4Ec3+709wbp7+07+vv6gmwiuGpRxWGcOylijHUdcUL4bFjvFhl1m30+D0tCdeI75RjCYqCbuk3B35Cv/2KNt5u4l7IfTPiSQ5840FGQWEFWFpVTxWmPOANHuX0DPkNehTxSFWnqOpC4h19t+TLgsotA/kDL+6B8gKSFB/UOYsjFz9DhdZGeIScOGNZJnKaIH0O1YAXpb2wOcX4dhH39+tV16uhLfidhErmXlhqFAz4URj5/LisQpHEYNV9y4EUF8um33z8h/w/5Z7Nuwoc1dFgLbnDBQE6RpbnSEJiV7b3uDCEBKefmtd9+v/th0A4WNQTmUhzE4DYZSvsWAoMFd+e8ewbaPKgIqsdKP+KGdBHEBYkbiBbM7/r5Sz6IKODQqotr8A7iffId+ndX39cZfFI/MIR+Cqoiu429Rd/gzMHjL8giQD6QguZCvw7VE4mKeijAJch9kHs9nOk031wIaylSw5ypg/4ZaWto6iD5qwtFD+BkkJic5iuiCjqscUUKfw0A3ZaHs4s8Hhz/iNX7bSik+gRjbPIu4gXRAEQTKZ3KKaPKqcFtXODcIwLWtvf5ULiD5KBDhlIOBh/dsvkWecaftw6z96bj+3ZjOrQbX1oCwynk/7JFGfQeS5Ixk8ab2RSZaRtjfw+yoasabL43YrBdQGC7cc+Yby3EO9u88/CXPI2hY6r+b/eRwS2u7mPu3NZWMGiMsXGTP2R4dZMbNzA6BndX1RDRzpf8nfCfIeDQN/XAXTCJk4ESio8Fh6fvmkYwU4frb8X/HSpoPQxppGzdNPaQAAD/Fv1NNGD87gYYKmDIM5gMXvSDVQiUDsMAyh/gjyGcsCjcoNNgjkBI7wH/MTweWiqohd96UFuYROAF2Q0xDeOyRlwA+6JhDETh000UkgGIMVTxA+E6csq7MkOn+1DQGXxRZDBSvvfA42H4CCL/W/JBqY7vNBDLDjoB5tbl7tkPPR++gspmQyLcJv3o7oetyPeV6W9DAkIdv9E/bM6Hov4dOJC1q+wedbDcJjVM8Qw8AghGwq1+v9xL8L3Gf+jy+of2/qe/tgO4FVXrR8+9IlHTlPUrit4L33vde4G5gsIYiUtQDzXw85B9n+9B8xnm1+fv8usHsXeUXpG/ptoPIh4x/YrgL9gLNjxSYg8MQfv4QCSEz5P9Z2p4OrDLNxc/4mBgNsi2bv9RYN6HwCoTViAcBt8LTj3UqQ6WxhvP3QrGRxg8kgQyRR4O1bEuvkvewabBqXefffAxfJQPTO8PHV0Ihq1OOqhfg6fXvE3T56fcycC/3OIMhAvDFEIxbItgysD2qInB7eqjVRouftzU3ZIJsoBfvA45BYsbbGufkY8O9Rl53zPc9mB5CzdNvwzd8bAkHAr/fIz92DG64Alu0Zq+HNS+b4SGpuzRLP9RiSGVoMYeGMp38ZGbw4p/EAK/hCGo/ihkdfvipA+CgBw+sDWsxI+0rqGePuyfnhHoOJhuMIMgMbZwwh+XgetU4NTCIuwP5n7D75tZxd2W328wNPfd5G9P70QxfL93BPegGTaf/2bTNiD6XmzfBrnOMPvWWt0AvjWjb9C4eCiq3z0Khw7hIf3pFZIMeH4aYKxi2GFfbxvnp7sy0IpvbSyUAOnicz00CSjMICgJlu5ysADWOP+7BYbbsX8bP3x5/bPe95/l/StPugAjXTLAmcALfJ/ASMKj+IDy8cBjeZfHSJbyePjDkBRPMBhgMJrBoc0cGfgeDXUYvJg5Dx1QfMAfav8B8l9tx5/u02GRIGgGzndxynUdnPCdABAeFzg+7gCGZzkawzyadH3Hd2necViWJT1AApzEAIeTNOvhHO0E1CDv0RHedXp7777fPXLP/ocOcEXCcTzOY3HK51mHgTIxF0rGCdxnSYDRPBlwHKDg/I+pD68MTrubPYQrbAZhK3Ye1vnt4eUhBBkKjpxT9WJ8/wgov3VcW3cv0Xx0TfmLseHXZnJc+1lDdqnpy4pSg/hA6IrrbmZuVIyD0BSpGZVNvbUhV5h1GRlzOgqSLDgb3ngiJfTmFGxiCxCyfwVkRY1asgnF2e6o9cuN71HqmZAORNYnxP5oOvPDaMEqUi+cJ/apqSyX39XHTX3ywpYwOVhWehDjikWOjxpQ09liSe7CNnDRwvG0U2zie0/H9o5rJGix21qLBR/jmtTuKjtt4qnWyAKdtodyl6Zt6UkLTiqxUYCyGarnZYuucla/bttrEFxGV39XTJaOJ2w5z6m3JqmlMb69ehfHKd1LfAJ9IQXUdS9QJ9ecNMvGWPgrB+fr8xyIphjL61CeLjfiSskVjA52+sHrMlzZNuX+7ArhXPRNVhEcVVNaY+NsJlG+ZZTdLC1suTrP3JPuUESI90qegYRAt+yOmcXWWb3M1YmKz4HGJJF33VtFyNEb4bg7aHQVpMp2fcrS9sIoro4fj5Sar+qGM52rSUeGDTUgzFqEpXm74w8n7CJOMbwKUeW6XKx8BxeWGckQ9N7ebmDXI69TbDP118EOO9QLYuoG2trZnniaNg2j2dfq5nywJc6QyNEJq8+LS3KtI1M6ddQ1IYP5WjvRgG7nEnBX9vVaSGuJPoJ2Z9vnLT1l524bNjme9mol4SMjdUgypuTcky75bHeYne1ZtK2PvVWtcCIMAwUVOKct1U46qWfXgjrNM3Z2OWy9kdUm10t6IXjRiif0NRK6nNlRtDCbi6wiSk7Jb0QKzXR7S64IDTqL45O6vtTXc89L27pbz9yFCdLD9pCUtJZbkZpY2cZuD/gqOE2nRp73h31OrXTymrLSdLSYE9NUopNlnKDoBN9TGcnyaLDRd2Nj5C9YvCr9hDNxpcEusPHu1TzcmZHM75ptaHg7hS9GMFKvU0kNqZSieIdGm2Q8OVlyJ60x+WQXzHo18mVaiKl2vKbVPZNgq2kxlxqraqdjoSsIcykZeVKNN/6xjpem7FeGCN10ETVndDoZ23xSEMd4W59H1iH0g37rcTU2Wmy55DA+z2I/Gqdcom9HKmrTZ2OnXOJVt89b39x2drAs5mjZLbse8ygGLa5oOVrPZ0ZfWIEZiFUXBYRUXQ3CprrJJCSF/bIpthszoeyjcMmyY+jyzhIT6qmOblTy6m3Vw4hLmejKzS5CzJy2EmkvTLy327WphSe0Isbd9XoNuojrMS4L8uNlZYiEJuJMNtXXFQzW5YlnwLZ1yakJFibVWdt8RdkmA8NHYxSfIutoz8yAtWXcQ0FuveVaZA6Fza65UVgJtXboK1u1JXqWn02dnW/dRaYQCs6hSdrFitejyRhdHNnTaemm5/Kyp1TyUnLd+UCVadON6xV5Skn/EMxW0owxdmWSElPtAESqLLDaC0/uXDsdCAmsNxtqwV4VObIEl5ofRxWM0lJsrvwiS8pgFp44l/UFcTIpxWuoyKXQy9wEC9iMWvKzFMNkviJn9phv9eBooLTMTNnFee/5U/K83+8TeZzpjTLRwpE6YWbh8kJ2HN3HlGdSlDshSplWxOkCO/panC2OrnrlzzY5XQR7TaUtN9Yzet+QNSCUdUYQvN2e+mzBGkw3MS6mMD9Ha5ceBygMJEG1QQ2Td7kZWaU4mQUy7aDjAm9PpFu19cJd605C77fhQTthC1A6ybmB69EeE46VoyU0XKcIuFTjxm4koT7XdPJmWVkjjBKa1AIN4WerDeGXhb84MJuKpWv7MHJaku7oUj5Zqa+RMEvY2biTIrOyDxQ5DsvkWO4cQQ/4zbiCxXJPgig0l8loGy8Ull5gI3uqoMu6BeuRpffZSd0eWlSXiOV4rNbSKlXlNR1BRYUJl6ptel1WgqsG12AzblZSWQlKOLPSuQHQadEHmwk1yo4XzLw4647W+pkGsq4qZQGjx9K47KahvJa6NekJo5OxE4pUiMx5kixL5iCiWC9H3Fw2ndEajM1CKGjVtnDlapH6Tqk7LqHr5XYWGtasqMbtwttRBHtwhdbVRQx3jiuayg6aSdZxYKx33Wwz3eulKYa70t+cV5TQ4pJfx13tdObuhLP7gnU3J7S3NtF1sqwBOWP9U+msOHUirHuj6MeHHRstRnrjexs/4llhvVzZLJWpnNhO4xOhZSakC1DglzNxBNFhOfe6qQOLAghkVT9uYqngxCnKxaDfnlxnv1/7Y1IeYa6142RNsK08T0lnP6OnPR6aWhZefOgBnQezJRFh5CQp7IPSj/cddlSLuKWubVLh4WSHyu4KutwPZdHJzIlfrRrGXZY7+YqtdJXQavU0MTR0Mc0mXFU1ZlUICwa7rCWQ9CSOj7fkmNifVtOtq6wsPIrm/ZkHh0m5Vrm2KdUxcel5ZzSvAqI+kpaJZYmTJXtbm8pMYiZse2i1yWnC+Ne28Y+nFboEAqckUSFvA4vQN22+NAVhJNca2GdhPVFd+dAVC4CztjRN6uUILNx6xUWO7yliZvaiHE83qFmkR2FtHi/JxV0dr40zStRE3UrhgQlQPgrcVT41jwf5mKxrUFCTpTdPyGjNSCbhm+TW2K5NlQMgZs/0aMRdvYmYav1G50OfGM/4So3DTMsnSxYrmwsWM3hgOyW3YgmwM7lsA91DkIfzVNrvw8vs6Kgi8LeedJyPD4tietiLDmmx1q47Sx2aCXRfjbVyMwbLHR/kNGq0Uz3TghMdimKkyz7W7AgQcpdrKQj13jJEpi69Tp+3q2LLoDHNZLSy07YjOWwPPYUrWtr4uSOUobrYnLOUX/rSYSY43rHMtd3CYZYjbt3b09KcTPNC4O0krcUym1YFF27KZHZmTb8LlzjeYldDV8OWDIOeLnUjvx6FXT4zObopiXM3ZcPWNUXXKi5RJqej4z5zuENtbeWZQKU8WCbFOrgkvY8W+yIXyiI2N0RP9MlFyTB0Vh+8ueTkC54+Cf7qjC0uuqkRpQY731S0ZNhf7xrJO+GOPKrLHrOXO86bulHlbUzOpXWnVqCTDeOiOVyZrxdX9bxr1pZ6oDx31Z+yrrRE+7zS5D5mTJuzMnMOkaEYNjci0VFmeWvii2p5Zt3rUiB5fTI289aY8nmBi/NZaawkaU9HM8aczHIf67YTwV5Lcbp0jaxZ7+IqV1YTq1tsA40KrrMIqCfNDda6npWMdzzmsaXN04mWd23pSEk4oeXmNM5Doam7xfq4dowmrtXEFmCn2I+aKZbEha3Kc21xmnh06ropnrHdqAKlJ0Tynjw4bLiVTn616OR+3hGXubu6NjO8MMbYeeJPr0qW4Btvpbv4MuCsoyD4h9HKNVlndZm2dUxDX3D+StuFFTufwHJyKi35KLFGMZUPHsHW202yQvlDpOdMUNjNVFPQoNfiTUUuMbwwFzOVkwMHZ/awZON8f22MFA0uYyzbJRgpVkJnjkJOvxw79OR0ltAyQaRhwqhkxpt2jZ3Q5KiN81YL46uvOfa+6MPlBJcma3WadCJwo3HVd7We1oYsuYtLYZ229AkjPS7D6+l2YhIhm2mMaFNxCKg9OfeIbmmqniDhksjXc/tKabOiq/ZHgafmU2NyYukY4NZEBtY6JfhgiR8A7It4TDwDlTzgWA60zdZKuRBqIiviVcurzfbabC9dQXVRyMl2djlfxrCHxVmaPQSAg7F7tLzgBJl9xVuMLTt4IAC2p1S2DhiR9OyWymTKG3k7VxEuzdX1Dri4Xkzm+PWMiy3GpklLSam9bTQty8PlylhyB5/kL4Q3vRAqbrDaPPfCeBcvtv41bqhl47pU09mlsK7X7l7bpSqZYdiY3859GxVIz2+F0ZJj+L2C6idPR3WLQRuD8larYxsuSJ7epq0CmVHoRj7hNzTebWGLJR8pMswvIlmza7fivIikKpRDJ9oIE4stIed8xY6UHKcFwKAseq56KV2ZbGwRjUPY3TRR1wkwSm7nzeqsr0NNgd3xadQlm/Vlr4HzorKP65mQT51kp4IQ7RbKAl2etyI2X6roidGP+Q7vGdtd8XinJhJ5wk7EahLyZCIVDRgz81VFcPSUjBTdMfcSI0ZiKgWYNTlXW55TrXE58cki0HUUrnfFcWl/0ERWtfxxw7ftqFZomVf1zCgVzS7WCddVk1F/Pp7H3UFYiedV1O6PNQ2bX705kfMldu4xl3NR8ogvItpwg63BjtXdcsYreur70x7LHf2c7bPO4f1qQl1Eey/gqUeqeBOAnmr44npiqLGiu7yxueDzlmm11ci4zo3JJjwQLKmLp+7K56KaKbUYlYclP69MlY/VoBrzjR+tQ3M6vpq7nO0VwsRxq2TOuR6DadNPONdRVroc7fXGW08alhDVfdaE9o6jIKMt8/k11EX5Alm+YKYeeqIXQdbtNdj1Lig/GhXT08bUqiPP+GA3uez9vbyv/AVfYBtmv9fFcVRb3Va+cuh+LeM7cn+0j0w8CrGCrecjpvKODsWTONFN3LN2XhJXuyjoPosvzNhPR9gyrdBVqVIb243QiCTVmq81vJHaDUHjPEWyx3URXf2pFXJawO2mNZCkc9GJaAC3G4RyWl3Z4447O+2+ubAVG1qhPd3s/WatXQAhkWXPyeQyz1p25TZAFosDo+Hr3TGmiXGF+/pkmo33QqyhG20yL0hyl6mCPOGOc96qj5dTZnTB8cqYst7C/fv8rM47m7UYyth0YaPUtpVCePlzK6A43TIkWrdHEABpqxvnWUS2ozNpFZBAzvu2U6R5azRBq4lkc16HqwpwouLigTf3HduvNgfePmM2yZKLiO1Hl0Nbk+cSXBy15EK2i4zZmKZOilu6qj5qYkqDe3du77rnrDpDMhsdg82hlSblSsC1QLxeWVem4j1WL5sLIylXTY+zbIRrVEtQ7IrnZT1Sqskat6kAW7WRvRmNx45WCUAWyHiD7Qp9vVlsGYmuFEtCWcI6z/O9QSuT3TSKt5g/hY1hwvndhVrNL3yC887siM5YcpqMxawXuRUu7Ijxao45TX8aWcR1j4ekmy1mHHSI1M+tC5No6rylnWnbXDdU3x9LHmsOYcChTqOF6jm2Q7aV8el1sXFof4Kd+UxsPReCFoxAtblOMGPs9VxrYvJO282d6nRELUc+jvp1e/A5FA8WYxq1FUj3wmollhhfLNYLLLMX403Na1Y4WrRWKu1MIAeHCrc80vZY79LPDxKlr2wR9uhXZtrN/R4c4B5hPH56frq9tX16xTGaJ56fhuP+x6H9Xzj1Da9x+fYQRLIE9vz0v3cseT8ifH+ZdzvCB47/elv99d/W8dfnp8qLoT73Y+I6bcPHQeT/OHb9/C9OgofJ/f2N8/DG8dK8v+ponPB2Th3nfls3Vf9WF2l7O6WGGMNmIwd1/fZ4VfB0Mykrh/cO7yYM568PI4q3+2vxp+F/gwwv0YAfOw14XIaPA/3nJ7+Hroq9+o1k6DdQlYOVjzdKw/Hs8Erp6ff/D7aASyxGJwAA -->
