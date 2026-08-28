---
name: "rar-cowork-cookbook-audit-design-warehouse-layout"
description: "Audits design warehouse layout records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_design_warehouse_layout", "rar_sha256": "7b56b9837a26f7584a0ccbde42a912ca3abfbd03123a5d13075c6d06c631d5fc", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_design_warehouse_layout`. The original RAPP
agent is preserved byte-for-byte in `audit_design_warehouse_layout_agent.py` and in the RCI capsule.

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

Design warehouse layout Completeness Audit — Audits design warehouse layout records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-design-warehouse-layout
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
    "criteria": {
      "description": "Optional. The standard to review against, if narrower than the default.",
      "type": "string"
    },
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
      "description": "What is being reviewed \u2014 a file path, URL, document or system.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_design_warehouse_layout_agent.py` and embedded as the fenced Python below (sha256 7b56b9837a26f758…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_design_warehouse_layout_agent.py` first:

```bash
python3 audit_design_warehouse_layout_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_design_warehouse_layout_agent.py   # or on stdin
python3 audit_design_warehouse_layout_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Design warehouse layout Completeness Audit — Audits design warehouse layout records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-design-warehouse-layout
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_design_warehouse_layout',
    "version": '2.0.0',
    "display_name": 'Design warehouse layout Completeness Audit',
    "description": 'Audits design warehouse layout records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-design-warehouse-layout',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-design-warehouse-layout',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b827adba283ba279',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-warehouse-operations/design-warehouse-layout'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/audit-design-warehouse-layout', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.5, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:audit', 'word:against', 'word:audit', 'word:compliance'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class AuditDesignWarehouseLayout(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditDesignWarehouseLayout'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'criteria': {'description': 'Optional. The standard to review against, if narrower than the default.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What is being reviewed — a file path, URL, document or system.', 'type': 'string'}},
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
    print(AuditDesignWarehouseLayout().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/716adPiSJLmX2Hf+VBVo8xEtyDb2myFDtCFDgQSqizL0gUSuk8k1dZ/3xCQb1ZNd/VMm60teQBShIf74+6Pe4T47c3t2qio3z6/HUI3X2zdNI2jsF64ebBgintRJ+CtSDzwb+EXeVvHXtcWdfP24S0IG7+OyzYucjCd7oK4bRbgYnzNF3e3DqOia8JF6o5F1y7q0C/qoFlcihrIyco0bMM8bJrHQmWRxv74vB67uR8u3Ksb5w2Y1qXhR89twmDhR6GfNJ/AwuHgzgKat88///LhLQaf3z7/9uanbtN8U4R9qGF900J+KAGmpm5+BWPKERidg+9lWAONMnApCC+L17cfmzC9fFj8538mwIxr89PnL/ni9fryNv8xunzRRuGiLdymnVVzS9eL07gdPy3o9O6ODbC37eocmLdoAGb59dNz5ndJRbn4+3zvx+cin65h++OXtwKo4M6Ifnn7aQGg+vJWd/PnT7OU8sefPqXFPax//Om7nKbzbqHfzsKA1p++vr6/xIKB34fGl8eqfwdSn77zwi9vfzBufj31nu0EM98+3Yo4//EpuKyLPsxn7/z401+JffgojZv2fyT356fgKHQDYNNL8Z8+PED+ZQG9DHqX+dfLlsCt/44lYPi35T4sXkD9lewH/v9FdBqD0H1H/J+K+2cToL8vfv5L2/7VhA+Ly5c3NkzjHkSHl4afF799PWgc8/MPwfeLP/zyOxD934o5FF3tPyR8zdw8voRN+/Xrzz80j8s//PLzD10JYi10s69dnf4zmf8M18c6f0LwNerHP88F6x/zJC/u+eI90he/FeX/qn//tDi5aRx8v958XvwxX+YXtJiN+LboE4I/5EwDdP0Djj+9/Q7YAbBI3fmP2yDL/+M/Fkrs10VTXNrFwX8wU5e3cRbOyptR3CzA3zm36xDg2sQA2Nc4EP+zh2eNi8vi1//tP9jxo/9ix6U7887XJ/99fee/r0/++/XTwgRCizq+xrmbLgxa077k7jXM23nBsg6bsO4BlXhjG34EJPRx/rCI88Wv/1Lu14eIT+X464NI4ycvGYwwc1IDyPPTbJcVhfnLCh+QfDiEfgekp4UPVLnEgEo/AHubIu0Bp80YNEmcposgBqwNyH58yAY4fZ6F/frrr4CQoy/5k0SxxbMKNEsw4F2dxcePwKZLGl+j9kse+lGx+OG3339Y/J/Fv5r1ED6voQEqf3kBaCge1P0CZFWXgWHAQcClgDIeXvjt9xeyQEwOyhbwWXyJw+dkEJVJGHyD+bCjP6IEufBCAC+ANiuLugXMvIjbTwvhsnjXFyw635q5OypADQrCMsyDMAcVqo1cYM47knnRLhoQes1l/LCYi9286q9e/ahdYQbS221/XSiMBipFkYL/ZjUfg8DkIo8B/O9B8LwOhNQ/NIvNNxGfFvs5DhelW7tlVLuvNS7u0y+gQnybDoS7izy8f8nnghjOUD2S4gkPGASQ8V8u/Tj7fC63gAGC5tvajzHuXM/MR12rv+TNK+BB1D0qOFBlXFy7OJjLwN9eIdWAgEyDB35A01nSywvByyuPGGT/ojFg/tgMPGr34kuHwgi++P/VUcza0dutwW1pk2MX3N40zk/U5oZnRvfZI4Hy/ljskSHfS/43wvjGm1/yNAYhUI9/e458YP0a8+SirgaLG7TxkA+0AqjNch9xOMdVXc8R7H7JvxH0B+DaBxsBV4CkBUE9x9K3Bee73zSNQGbO378X6xdOMyog1hZl5wFkFpcwDDzXT4BW9ZxLL8hBUIZzXt2j2I/+ZNUCSAe+B/IXQInZL4DEH9DtC2AmSKNLXWTfh8dzCwS0CDofaAs6yvDTwgLpMIdEA3IQ9DHzGIDCDw9RiywEGAMV3xFuIrd8KjM3oS8F3ZmX4/D+R/xft76H70OTWXkg0w3cFiB5n7k0CIenX9+1fHkKCM3m6HhM+rOzX5Yu/lhH/vYlf2j4Tt8gj9O5BP8BmgXIn+wZizMNNYBKsvAVPiAOHtX207NgPivyuy6f/6Hv/vHfa80fJfD4Z799XkRtWzafl8tn2fpWtT6BDFmCCInLsHlWsI/PfPv4nm8fn/n2J6FPjD4v/j3F/iTiFc+fF8gn+BM835JjP5wD9vUCODAfN+eP+Hz3S26E3x0Mli8ywG4z7iMome/F5NsQUFGudXidBz+LSzPXpDsogw82BS74kr8HwStBAFnn17kSNsUfEvdRVYFLnx57J31wK2/B2sHcfV3DeVeSzuo34dvnvEvTD2+5m4X/3W5kZnUQowCJeQMDsgV0Mm0cPr4Bi8CN2J0//3mnpT4+uOkzlpsWqOjWD0Z45caL6j7MbWwO2GTeMsyl60nzYKPjdmk7q9yO5azjc4cyd0vvrdQ/rvpIXrBGUHyec/jDYm57PyzeO9gPi297iscWLe/ApurnuXue7QRDwdv72PfNoxe+/fJP1Hg103+hRDzzx8w4T3PD4Ds5PFxWui3gwKMhA5UK/9E0zIWyGR8F9R/NBgvWYdWByhjMKn/H4LtqxVOf3x+mtM8d429v3+jl5bxXdwiGgzz+2My1cQmCGywIvj/DENz79/rG12TAhaB1AbMpjyC99QqjXJS8UMQKd2Hf94IQR901gvou5noXL4AxBMVcIkAwmCJ8MoBJn8SQgLj4QN4zkr/O1T+eFUJd11/5FIIHa8ol/RCDPcwPERQJKCyEiTV2Wa1CHGDzPjUBVPqy8mnVDOF7Czuj8TL2tzePxMHIHd4I9PPFLNcnl3Jkr43sdU0GdGYsXfNgSr5TZKnXBd7+7CGTquJIQk2Wjm6v51jQUyeudBHOWsRBLyO3yxmNy7VeZ3ExxFw3qFVR1c7clfft/aj5qxXP6+aGlLkxLFHRRbLKPOGeeJKIEWqlXLU9IbVOY6kPeG2oAXOClpfEhlaZQAjEqTzXk3Lj49TxYyqpdOsgSdreHqYbZStFd0q2Xang+zRwq+yApkehk/ZxtVbUTRVoeTr6FypZ723ijO2g5d7m1ySPtyf+nHN8LFpG4F3Ew2nqw6otCwEVnVE6qaSRQScn8nnyXKXBqB5ruHG8lHKYsAukesVzY4GTIDQuGk/qlhzBVeXIW5JpbJMpZPkYd/7ZO5yyE14eYZTjt+ujax/C2DxoNcWQY9m37t6sO4fP9DUkKzl0U24k3Bq84whmvjbELXfo0qSylJqkTZExGjKetFSJbDyvbjiM9RotHcYBE/mUoZcif3Em1lkNUz6unfgUel5wE1Urrpt8rQ/r/VgcCzvucDip0GAr85ZrrxV/t1sq18aw7p4nVuy2Qf0b45aSfSJHN1J0zEoRzDtSGoJtUOnQNvex0qeIzjgkF2Hz1OSxXdWX060gkInVjU4yHNwMIILKR0YoLH/jqp4xapYpUeLQTdRePMmdbCERGR07z9qkUN2MRbTv02NndSzWM8Rt4zTiyhGW+6JWuEu5gmVl1SOgh8V28LFJFU3hrG3r3GJfKQmVOMhQU8kreHB2lLdeG74nVZWiaY6sunxzamwhCrKYDgKJVc2UL80MyU2xVrN9rZJKhRBEJ2FVYJ3wrYjJN1zd4bqmaKIy4GUML+Hdlhj2/XKAoMxXbjFxJBGnya11Wvp5qFI7nzFUu6tuysRBIrErg+p22t/aKyXGA8psOeWMKOPSjYb+2HEho06tKZiQdDBzTPdXlYHwm9F37CRlBXdk0ibfAoD8LU2zm5ZP/KUibYQczxwuul+VZqvXVyoRDmlyPCJOHkXKjpu6cHQxhtSuMkkcyjVeI8ZWX3OmFcbSPR8yEmlGTgy5yForK9PTa+UmT/D6fjkbhTSecvuwRCCdpEIMPx6pJXWmV1BTd6ZzvpjptmuD+/qAj+GpNl3/bConyjLKPckZdDnUS5jdQJhxtC6lbLF3vqZF1+yKuNqJiDi2GKK6Lny46bcJW/uCxvhr1N816s0zRGxJ7HkxVU44XlqyYsMgHt1uKtMdGRxgcXBFSZpwUpbdVpmmgYNrpGvdVCl3EtayJV+gE3M9nUdUPDK7Irxwu82+ADxg3SdhtzG1ge4zwFZxtA6i8/VwC5n+kphH4d5LRWGgy7BONW0UmvuVwM9GK+itCJNt4ThdhW450vHXTLs/lKmXNYFT6AfGTe3UisZhryqHqF+tzlvd0bahRlb13kp2njYJBHLWl6fRoe7Labwwwu6sTtIkp4wXXgk7MAIcSo55vXdRiodprc4nLOpW/HQN0mDJRvgdh1bS4YjvnXOFxVfN3KhKb0i7pbi51oJUErI55DhK89JeuEhMYOEFo8oxxQ0ryMNosZw43yHu7W5ar3lbqJWLbVeUBk+DHGAat/Ui41bQO3bMsINALOlDulIsf2hqqbzB+8OWEdDLhXHK6xkLgnRkkpUMaN09Br4rrJhBZdaowZPNcLb5DXctOc9wkrhgpP3W5x3cC6YRi8oNORr4REsocicnx/KhW4NarowGMNJmU4le8gmBwgSO9WI9FENZLw9MLVaq6WlKh4WDoBobPQg7L4+mlUPvg3ag+LUl0YJlU9CKVcSgv91X8PKOoMEyOO9i/nrcj70stYO12/C0GFQmHJnOZQz0gk7CtdVluHnlqxUGJ+bBqso7hDN8vR9s5X4UhobEK39b7rKdzfFwQpkt7SAlzAaSu+0G+8CsyZuyWlWKZ6b3hCXbVZXt1twplyJLVdEL4xn5tRX3VOhyfqwsu7Fp+I64xNJF4M/s1J82CXbqYMksR5S9nRxbiaoziSC6dMKutMxtxdveVhO4PGvBbbvHpRZSO3sUlMM4EZoa9jhychMs8uySUAhHCYIMUnYjB5XMFeINvzzeIghB7uqww+I9kyBQD9umYCWshCrGdqoOKnuUrvtppNKqlyLovjXDngmZm5G4dwKRiCNn35WA55clnJrmVuMz1a9rqzxSdJGIheLYLWrt02ujKIxyVbZlRw4TZG/2+BXUeu3E3Pb0cbkR09oXD3QEc9Zw0u7FVMl7GA+LG7IjDynMRB7RFPLNv+2mYHvO7Ma7W+xm6B2vZt0VFh5L76DqxT5nDp10NisLoQbXOsBcKIlHkW7kPsiczNTt1bR2z5F/2W35gNrayWj37Rnen9Ynunf6QD5WXAERuzOy5dg6b/UxuWUbrBM8HR2FXlpyqWZWqTiqPM4U1cq0yR45RPryXm2IMUzHI8mITrILuC5jg3MqxaeYEfZ8ZPAG7KbSdBVaezoAdw0qcYGKMYkmneZLbIkCa3QNzSmQhMImgU40zgg389wS7sZsmTMS6FxVkeOu73uASW8jrCqI21sihAS9hxpXuxu7muiCgK8tQifknrpJyRqDw8YJb9Kglp7W2smqhvdKbDQMkteXoB9pPboW+j6Lqe54REF9cCgaMgh2axUhyRfQLY2XykSm1La5GsOK3CQqikknpTdlS7hKdsBtDaXKvC1oRDsHxrv8hiLIVBhkvBxz6J6q9qG63I1UOOO5mQhJkbpZWhBWDScCj54t2IUY1SfkTGUR/cjJCXMq2GthSVDvnKpM4rS1vLkye3M7pRHrOLACy5VuttXA9VUT5LwEC7TchTnDriuloaejGF4Ve5Rhkt0omJwnPex2S83gT5B7FxUkGW4enNAqfQhQG81i3DpMG2ibn1S8OUTqmGwQrfdyXL0aotJBIVefErJBRKcciIbcjShIrFNft5t9Q9JYJaOedojOUYquYrcVxVUnO3TjLyW1BvlIadsM1XUq7XDi1FTW3UgkL+zO201OcQTg7vs+wPWxtZINhVqirOXxeMK23d7phF6XoLOv9JCrbqEz2CRLnmhNSlamJGSovpHKhJjcTM2hU3vtiVTp7qB7UV0NbaB8a2KOp7p3T0edlZydPRKsm+sC61xVitmKTmA30RILTrrtWKV2gwTIg4ruGEOOitkeRWFGm53SDGX6e3GEzJrkMNPrlg3p3H33GHLU/X5XePfWS2kCS8VYYnqT3xPTxBiczDS07lsh1o99fcz8Rr+zpcMIED06qVxeeHM3TehYVc2aLgwO9Oksc46NzRbEqyE5AHbWPeJSREMcygOXNFwhno/quTYH2TuEdqkg42YQYRSr2BViUFsaERBMOm68NDBz36gjBmb8Q9EHw+5C2MZ+bzMa2CUMgmLl+jVEDXncTeyRWhmVi0SHlvLCvbSd8Eytz1HAOalOQnq1wQErNdAm2tzxfZL1uBMPZSGqZ9DKhqIc3dFCvEh5r+jLbQZvGdg1WZbsqA1S2VIlHWo2rVwj1+1w2qdcjqTHk33vbJWfTtWO2odcY1dq0R6bCWUjHzI8eGUyQQ2apFj3tymTymfsGBB5yO/jcS1OYL08L2U7jWHXsCLitPM3fVzc2bN4qg2dLZXWc/utScYwOtVKOmHo2F0pc4wvirNauUkHV1S74fgJn3j/qAOfWrlA55OzX0qMFOVDHdTsNkBLsiVIjQL9qiZX9dAu4a3ALD2058y+Zq84aMhLLHTs9V05TU430Z6sjgob+APMyPShVanl9rYFSWqurZ3qXeEMmvY6Nmz11MMo0t8hkxdPK2zl9DcYaZRxw3lxuT+HqFNMOyNJoBLul4zBI8s9ciyE/L4+X3hpZM8e2Z43g1EdVkMU2IQ2mhnofOANQV3rDj/0hFGwrKtem6WE3kLdhXFIvSNEhUpsayzzYZSPfL+kRmVJ0gR5OrvBZGurw4WNaLycsvGCW1aQweSVo30oqduKaSimHfxE4WnnfsJMfNeuLlfzkB19dlNw8QrO13u5HelCUy6wIBRLsT/y950oLGNSu2E3OaFJyKeo5Iy4XKdMDbm9TY0QDNuDztxBDTB7SfHp6Vw6SSBkIELa8W7v4UmS7xehr2+Id7yNa5TBqbG+x8Mt4amLQPMEiiK2YAee71iJkrrMWoTE0fdvZHBVZXt0zpNwyYosyUVSHmCPSgE7BEhYLslhTd02jM9MU86I7kaShZ1Jrfa3IkSbpUI5sVyQoCpeZf4QVjzddrLi7aa2l6fznqwCAsGuhACTA8VNEBQOHTZy3lmi1TENNX1l4fF+6PQKGLsVUS4/arfEiNdcMCJLPIiODNsMUXgpUJ4NuIuI+OxBu27hHhM1TYh0sAjMeJAcTWemAPtvWbE6qcOhO0vgvNTey5BjkaFICKjarFahdr2znEZdz7XMVUYDC7V5HjOGXglukBP2tTiyO8Njj9vdurvnabxW9cG7EekKbOg2frTcyErQCgGGoFLkxWLuYDezqJ3M52NYxyTiZqu7TKnOuGHnOIO3YycvbTpYW8gIIhejbkKol+NtjytinWsbVNvRFqfs+tvqto0Hf2NdWgYjIVVMsF3W9JK78RU+QhHNu01nUY3XhN2Zp32I787tKLNHNSRv6q5ooksxhcxG0Xya5yddHqiitwPqnOg0YWk4R1X3AvaE1WVX7M7Z6JFVvtY8rrEgQMxYTLu7oL967P0SWmsbNKBbyApO6wPm9epyGGhWlVmtXV/UVl8VfEAv1WrnrUEvQ5rRvkxDCewPG2iNUILtCqibXrzVrl/u7V3I69gtuG9JKLUxWuiOZsi55+u2Z45ZY2aHhlrn3f56UmHQIWo2JcJxALExC2umztLlgUeCpcay/VkUbhbfsvalOPVHuHc9eW81Vtcj055gj/yuMEJvp9FT4aO9sFnTfivqkemmVxJRGFM6rXvNy+G153q9ZwaxtUzSrKQtdrxBIz+FFrAqZ3FIYsBu3F0d1kREXDdnnK4jkhPNM030Rmqm2uWUHW/qVbkHaVJwWmohPVyoByrT281qPbKrwNmcl5601i1I7rHqytiDBx8oAaqJZN80XULa3cRiqggxlLy6VZgfSUqkbh176/IyR+1iMV5CJ0EE2zs1U7Pski0T2qfq9L7b0kEu3V0V5sWj68rJSkDVNDeWtL07ifkxPPjDbZmpcp0fOh9fy7lP7fi4gUp8vV3rAMM0PyQ0Tf/9728f3uZT09dx9f/sYfN8FPj/7ETyeXj47XHV49A4dIPPj7U+/w/1+eXDW+3HQJvneWuTdtfXAeV/OW39+C+fccxTx+eT2/l52tB+O8xv3ev8a6O3OA+6pq3Hr02Rdo/D3g9vXtfMv35o5h/I+OD97WFOVs7SHqu9zb9CAObNT2y/tsXX1282Hpfnp0RhALq/8PX1+jp7/vAWjMAnsd98xUjia1iXs5Gvhybzqe381OTt9/8Lpl8aScAlAAA= -->
