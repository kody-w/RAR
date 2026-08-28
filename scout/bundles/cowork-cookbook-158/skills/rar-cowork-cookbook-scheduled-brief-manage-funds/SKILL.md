---
name: "rar-cowork-cookbook-scheduled-brief-manage-funds"
description: "Schedulable morning-brief email summarizing manage funds for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_manage_funds", "rar_sha256": "4e5f9fc5f22e92cc4b7880ddb2f5f3662b72e8d32100136a7c3344f01a7e2be5", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_manage_funds`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_manage_funds_agent.py` and in the RCI capsule.

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

Manage funds Scheduled Email Brief — Schedulable morning-brief email summarizing manage funds for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-manage-funds
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_manage_funds_agent.py` and embedded as the fenced Python below (sha256 4e5f9fc5f22e92cc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_manage_funds_agent.py` first:

```bash
python3 scheduled_brief_manage_funds_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_manage_funds_agent.py   # or on stdin
python3 scheduled_brief_manage_funds_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage funds Scheduled Email Brief — Schedulable morning-brief email summarizing manage funds for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-manage-funds
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_manage_funds',
    "version": '2.0.1',
    "display_name": 'Manage funds Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing manage funds for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-manage-funds',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-manage-funds',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8902ce6b0873f094',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/manage-cash/manage-funds'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/scheduled-brief-manage-funds', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ScheduledBriefManageFunds(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefManageFunds'
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
    print(ScheduledBriefManageFunds().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6eZObWLLvV+HV/cPukV1iXzwxEQ8EkpAQSICERLvDZt/3RaC+/d3vQVKVu6dn5s5EvIgnu6IE5Mk9f5nnUL++WF0bFvXLlxfNs3JoZaVpFHo1ZOUutCiuRZ2AX0Vigx/IKfK2juyuLerm5dOL6zVOHZVtVOTTcif03C617NSDsqLOozz4bNeR50NeZkUp1HRZZtXRDdyHMiu3Ag/yu9xtIL+ooTb0oNpryiJvoolBcc29+q8QkBAFuedCbQHVXQ65gNEIAfqr5yXp+AqU8AYrK1Ovefny8y+fXiLw/eXLry9OajXND6U8l5s02d3FLiepYGVq5QEgKUdgfw6uS68GqmTglguUfl59bLzU/wT95S/J1aqD5qcvX3Po+fn6Mv1TgVqT9m1hNS3Q1LFKy47SqB1fITa9WmMDDGu7Om8gC2qA+/Lg9bHyB6eihP42Pfv4EPIaeO3Hry8FUMGanPv15afJ5q8vwAXg++vEpfz402taXL36408/+DSdHXtOOzEDWr9+e14/2QLCH6SRf5f6N8D1EUbb+/ryO+Omz0PvyU6w8uU1LqL844NxWRe9l1u543386Z+xBZ53kjRq2n+L788PxqFnucCmp+I/fbo7+Rdo9jTonec/F1uCsP4nlgDyN3GfoKej/hnvu///jnUa5V7z7vF/yO4fLZj9Dfr5n9r2rxZ8gvyvL7yXRj3IDlAqX6Bfv2l7YfHzB/fHzQ+//AZY/69stKKrnTuHb6AiI99r2m/ffv7Q3G9/+OXnD10Jcs2zsm9dnf4jnv/Ir3c5f/Dgk+rjH9cC+cc8yUGlQ++ZDv1alP+n/u0VOllp5P6433yBfl8v02cGTUa8CX244Hc10wBdf+fHn15+A+CQA2s65/4YVPl//Re0i5y6aAq/hTSn6NoJY9oo8ybl9TBqIPD/gUzArw9getCB/J8iPGlc+ND3/+vcgfKz8wTKefMGO9/uCPjtgXff7nj3/RXSAc+ijoIot1JIZff7r9PjvJ3klQAGvboHSGKPrfcZYNDn6QsU5dD3f8X2253Dazl+v0N39EAldSFOiNSARa+TVUbo5U8bHID23uA5HWCeFg7QxI8Ajn6acLhIe4BokweaJEpTyI1qYG5Rj3fewEtfJmbfv3+3rSb8mj8gFIMe7aCZA4J3daDPn4FJfhoFYfs195ywgD78+tsH6L+hf7XqznySsQc4/owB0HCjKTIEaqrLABkIDwgoAIx7DH797elYwAb0DghELPIj77EY5GTiuW9e1tbsZ5QgIdsD3gWezcqibqe2FLWvkOhD7/oCodOjCbnDomlBOyq93PVyZwRcLWDOuyfzooUakHiNP36Cusa7S/1u19ZdxQwUt9V+h3aLPegTRfrWziYisLjII+D+9xx43AdM6g8NxL2xeIXkKQuh0qqtMqytpwzfesQF9Ie35YC5BeXe9Ws+dUNvctW9JB7uAUTAM84zpJ+nmIO+Dlrz1Iqfsu801tTN9HtXq7/mzTPdrXoKhQPgHwgNusidmsBfnynVhEWXunf/eY+e/oyC+4zKPQd3v2/+7w0aEu5Twr1PQ187FEZw6P/HSDFpyK5WqrBidYGHBFlXLw/PTdPP5OHHwAQa/FMMqJIfTf8NMt6Q82ueRiAN6vGvD8q7v580DzTqaqCMyqp3/iDYwHMT33suTrlV11MWW1/zN4j+BMJ7xyMQDlC4ycOWN4HT0zdNQ1Cd0/WPdn2PXe1OZQzyDSo7OwW54Huea1tOArSqp3p6uh8kpjfV1jWMnPAPVkGAO4g/4A8BJSJQIcC7d9fJBTAThMOvi+wHeTQNQUALt3OAtmC89F4hA5TEFIEG1CGYZCYa4IUPd1ZQ5gEfAxXfPdyEVvlQZppInwpaUyyKDGTq7yPwfPgjie+6TOoDrpZrtcCX1wlQXW94RPZdz2esgLLZVHb3RX8M99NW6Pe95K9f87uO7xgOqvmRtD+cA4Eqypo7fE5g1ABAybz3PH103NdH03x05XddvvxpDP/4n03q9zZ4/GPkvkBh25bNl/n80breOtcrgII5yJGo9JofXexRdJ8fJfb5XmJ/4Plw0RfoP9PrDyyeCf0FQl7hV3h6JEWON2Xs8wPcsPjMXT7j09Ovuer9iO8zCSYQBaVsj+8d5Y0EtJWg9oKJ+NFhmqkxXUEvvEMqiMDX/D0HnhUCEDsPpnbYFL+r3HtrBRF9BOwd+cGjvAWy3WkAC7xpX5JO6jfey5e8S9NPL7mVef/LfmRCdpChwBHTDgZUC5hl2si7X73PNdPFH/dd9zoCAOAWX6Zy+gRNM+gn6H2c/AS9Dfj37VLegR3Oz9MoO4kEpODXO+37ps72XsBuqh3LSenHrmWaoJ6T7Z+VmKoIaOx4U7cu3stykvgnJuBLEHj1n5ko9y9W+sSGprWm3hu1bxX9lo+fIBA2UGmgeEBKdmDBn8UAObVXdaDJuZO5P/z3w6ziYctvdze0j63fry9vGPGMwXPMA+SgGD83U5ubgxQFAsH1I5nAs/9oAHyuBYgGhhCwGPcIn/EdwkdRj0EdB7cpmoZd10Z9wsdIErUp1KNdDEVgGMFIi3IwDMd9GLEoD7U9AvB7pOO3qY9Hkz4e7HsYg6COi5EoQeAMQqEW41o4ZVkuTNMUTPkuAP0fSxMAh08jH0ZNHnyfRSdnPG399cUmcUC5xhuRfXwWc+ZkkShlq6E9q0nvQvjkATtWxwwh0ZNuSUpF6ry7SAJz7xY5u3STSCm3Sck3uxAno1WgE0JOcfumpYkdNYpJiaIRbUSAXsx5Ob/1CG2SQbAQ7L2pEWctutV76Ryd7I1hmWh52gx9uaMEHNnWpR8jBDKzlmqaa9mwA/Gk5QtCnPRVWuuObXiVTy+HZhaN5zLUT0aRaqgjJadwxzsEWtPVUkxdo16L7kktVURKxSsa1Ifz2CKpgfGwF8Okq0g06eU1PZsLndOfU4Ze4vX5sjEu/XJDbAzVrY9oWZHwXF126ihIK6WS85mIKfWhtdNj2allpmhI2q1v9aK8XJw8OAjuSTptNI1QJCRg0g1/ANNNhbB0RS/wUDKNkVvBMNymFZ4d8Aquat0iRmEYCV8t4mp/UhsSaVc92WuxbBBnab9Y1putuQudmy6Y1NmxLnpzOlSxcRo5M2dFw7gRo7XuTDvyKlRnLviMLW+S5AuGIHDntLpuEwq+wiyjGBszg4clDyNSOJdURVRcK9WKI0YSqXq2MDG1zE67WBXPZGq2jS9yCyNcbdTZOdzw63R5abLRJzJx7E/trWprTtuFM68U8G3CxZ05JpVSZ2tkvzz3+cK1Z/ZwExdatD27HXo2emRYULndBm7fXgdJDNEVlzI5lYm1dou24bGzl4m1GdUzkg1y2J+46oi4ZlIYAiqe5uOwNA7dLRhBZ7d3p8s4x7volNQpHkU7mNo5TjjqCb2U1juhLWN6fTtT3SwrWuSkntB92aQ9vx5mtCTYK0tcLOFCoWR5UddwVpdJlosjc0pIkr4tKUKpbrSwppCBXm5IYYPEhBF526Ddz4NDrpTFbJ5h5GJwV0uyvlVzi9pgy0a18ZOspcjRba2Dut4i29bYRgsZjQNUkgzxMt6io8Qz1d6jb+Ipl/ztueEWVLnRovKAE7BfbOY0MxyvmVjWGAdXzbLjQKZvV1q8XZXaDq8FERNuYnRcNJ274vKdmkpiUUY3heeKtUB53ohjC7IPJYKQS5zQFUEVKDHfKpEcqBdqbmYEj+5xVt2jlVcyhZG5w4r399iSSdESk1bM8jZfowYmOKflSuiHDt026Gm+SZ1zN94ErS8srCUExDiiVqy50Vp2DBlMnovlsbz6c5jnaEw9Gj7XWLk6EoeiKYVqpWUmv3WPWFWfFvtj1jLnSODmal0tWUyNCpyez26qZupLz5MFDd4yu047Tw3Zgt35MalK87TKl1yx8JnTtm6XSY+YrXWlNHVsZ1pU9IaHnxau0+gtW5LrfNgcdE8qXWMz4jqbzIlTvxqpgxbO6C0cabGhFfuCgy9MsxUb7dqh6M6ke/6W2QnXeejBohP+StUW1hzDS65vnat1FpdIvsDwIT8rSVeeKvtQByUDEr06nKPzfsQ1NNdXNOOmtWa7WaXs5QUqc7cExiq33mXi4cA6BXkT42vebs2c0S/EXDR7Y8u0yFm9Mp2/Z4iePAlrVHe3g+xY81ZYqSeXRG9aKjc8iQh60DeeJi9Bqm1G1I5CtUyPF2pBXzZLeyNuC4Vv9JiidUXUQVII5UDXN5NkeC5mZHZ2yfb6iWhLOB6DhcrvRNfZ6o7Iy7NDvyyUuLol5lnyo3BzuMSiLUj7tkBx28EVI9YvLBeBx0bbnETe3qSRNpzl1WnEm2xRqjvj6lhmo8m5S7L1Oj53ioEvN2t7z0tKbYB+3aJuphxQdzA70ST1mpq1uTm7tGeCpFbLnVmRUs1ckHGjjmcf5GXDxIGzWISa19qH8MZYpy1m55mMRdfNclRcP+cHEVn5w+i58xkWEnRzzPcpT5cV27bS7XZ2jmFgFoKCSOMBbCJ3tbLdVrIn5SfNZAAmyHRfEKnAo/BCKjZHRGaUdX5F934KzzpOL9r4uNQTTAwQ0mabJEftsexV5Xiu8tO6dME+a7smzqvT2tzljnBq0DQtazKTsDJBeFo5Ngh9jc4sYisusezwfbEKIrPQ9gzZc56iVG1hAJx0CTTT25I/ZaWN6jUNBvo1d415VMscMzrTN71j9WZIb9nAxSRH3gD40pFP7WzeRPhYT412Edm0L2XUMql3DRraQuyKl6Nt+RGT6BqGzlEUz/AQP2aayyTUTBlYzvdZAj0mlzNlIdvewlFMN3bxhZ3Dx+tqYStjmFmGxq4wNlS2GymDEV3lOr5azauTQZRqMRysU2mkrXOlKzbQ8xNr9Vnd5CFBlJVKmnQAazwc6tRlpfXBSVycAzNa7hhh0zW0cW5ni7XF9+m+4Jf8eDoZOVqEJouG2WHlFYfdWtCRYXaoBy/DRyURQnWtsIRz3OWm3MqxtNISwdsaG+siRcGq35HCAJqKTXqydQndpjfdljqeWRKkTBLLTbi5HrSuFgjhelOQQmYlXfHmqdKVqhswxUJCQ4sz9qQrlHs1K108qbb92jnu1UjPh0iQpNy8JEMQJ4SKHWwig0stEPACjvNVy5PjtmwWBy9MjnMLzjEHdkVfDLING0fOvG19e9XPQCmhaxFx6OVhxRycjqLt7dXWC31V10UTFpvI2ft+v4cZd9YqPpkYW4ejGn5HoushiJTcTFE4bG18RFE/T1O4w2CvMb14M+xK22+x9CpR4m2zC/YHr1277CGqrirL3Vibl/H55hTl62AOh8dSDlZM6Sli6fX6dV4My0wSmmNGmqLs79BS63jl5Hg3YrVoBCtdpJtzea0Ud+7E2jb1GFaq4JHt07GKD3Y7Vo7VMmy6FQ7jil5iUjvUeDTGoSsg8aFY4ZsO1806hEs2HOGVl+llzm3Pm+A4sgAHLgJpctW80j1RAxNzK+N6LNYtvqY7S4eXNH7VBTw6J7204pxLllySThPxY5zyozri5308E9bblFOWmjATs8V16RwNRl856LLkBpMyAcwWVzprhJM6rI+HDY4qjXTdXvluoSWUeZLJ/fEUBryCllJzbU7n1JiZgkDou1w4JVuSQXtlpgOl2cIsh4Bq7dzuye18bzRqvhuC3U7HlcFJEC7NpdgoqhYfmNOxXJLnFdgCDHWRhXGYUIOh7i9yTBxGmnFmlcykqhvvVEvqLU7hZurIBVd1cAr/uGdYDj2G6m2HwtxijSmGw5dXlWTs8VYXMldh6Xy92MmjtFDmwdar80rrZnLBb4/SQpIq10pqLaiT2ih4X5Sq3DgU6GGxbmUkCApd0ndrAp5t1qAhuMeFpYo7RrPyM5hR5tdlluo4wh/DToSxa3fCJG0IgmQf3gSr7kNS85zrTNR2W1NJsIxz6tsg+BrZp1t2pBjldjuiM4JguwXRNcxOEGTEscTjfnNQ4JqIVjMuvuo7xbAoeH5d7eZieCPdPtg6rLnxqe40AD/dXMYSslDaLdhZb56sJR6e/dI+2L7N6NSNXxvZQTXcIPU2haezy/nSjMyli/Zbu85cOWIHhCdT86bi7OVsWypx3hR1qrvLSIVXnNqsh6Kgc1bItyR1llhpycsJvpvn26S2qZl2qgDIxZzHsrftbauP+8Pa25O3wLocQSVEUp7B1HGtkqFUs5EeNQW948YMaSOuMCNJmys7o5bqfIYhfDuvu03nb/CDHFO1QrZtKrAHmWV8boNivYOgIFTJzQvm1pkOsXPg2Q5Jm8zQDzOB2gyVQnn9XtY7t5OmrXS5dwlnhZzmDBikN5ijr53uvG9lN74YQ9/hRFUkoooStBWdLd/Qzu48bGFL319KfMUnmgJG7BVJ4vGANohMyevM1kYnEvXTLWqvm+vpRqOE3URGsJUDrxm7XqbGftAtFzuIC8lG/IqhNaKd6z3IYBKkZL5nCpcPB9ij+dUcoBihdQPSbHhzbqJYfuGMy54m+dhZnNmzR4G2F9/Gan87nzFqxaOcEZaYMZ9X+UzJ0mbukQNTnhEiutiLWbtwNl7hmOGWL7b7BZKlCZ9zB7oP1G6YcUoWjocLvlewXdWVmx1XqjhBLPZi3PDXjLnanHOMZ5JIKi5ll6XbEBi2GxbZ4BIZgcjrCD+SwEeVea3kvaQxAHa6plt4pqFtwpReOzA29Kth4/FsDWYgy2IZbs7R8pDCq1tkgXuqx9/atpsd9mRFLAjpQiaCmKMC7qMHxoW5OriZF17ws6IX1zGs1Zc5Kh39nARYMEf6ucKfFobLMwwnNCxiJvxozfkLuW7zPbzXZZVyawQNlrFw2AQGtszamkLPKdWsmLMqa9R1LlwYV72ldUx1KcsMugC6emeiN1xZzpacIwW70K5YVcFzTz4XRsQILorQKDyKl/WWC/2+QJe8JxTx4O/9Jc63g4oPKbfep4eLOEpwdJmRUbLT/XiZ2nvh7NUNwGOeNxqzX2hH/JQwsxqfKef8KrIDz+Br8rC9mtj+kl8MHEQiZm+cycYFl7ujeVE2XLg7XE9pPfOPAoKtUFHVMdrMFybM0+v+6sIXdL53y1MkZrRuK16WZtvdblm0s6Nk9ce9edWJJOjX5hCuZ7fGDfYIs+p0g0CZAqOu4rG6tWubvazmWONbtMNdDld/5mbsDQXOuNUlRq2HfmfQDNLC6kEKg0ZBixXB27yNmt7JT26x7s5dtFvayY4xyLrjBpcKVLLDguC2aRbL5e2AXKkCOyv5TtuydLymYS+mKzAI+/xA6qTUZLPC7O3+upIr1xFl/LAKsZpcBDOZRDHbR2jMtOdXTO39zgJbq2kr1M18yii8A9df+HA5MnRlnylXtWYHchm6xx3m+4MxuEi+97TBbP3+ep4Tw6W8jgptdyKGwaVThOKouogK0gDBrepW2Y1On8ZCUdvTbDDiMKt7bTvjKa0fygtXsCCrSgpvfF/izwK/imXdccMRR3RKrjv77Ekbc21SOFvKq+5irLa+ejtcGVbhUZ4lFxyXbdL62lwZXsHYkyz3K4w3GbmdMe1miImSkJYX/iqLQdcxt5z0lItFK+uBSZC5JTBzgYq54bCsQ96T4oNcxgBGlscZ2ADsyMC8bjJ+v8vZkCnRC7Plc4UQpIOLdAc/lkSl7+Jernsek26leuZszMl53yaKvUXIEjJfRj19banaCejZ3BzDncNf2tgvT7prJPGpHS94RKesbMxNy9Yp0DZ4tFT6AcF5mVU5vFfOIReVSrIN2YLy/eN6HompqxJLLMtp9VLFHcpkcbPLUreJ13WWKCHFcHhwYYpDuj2w7Munl+m0+Xlm/G+99Z1O8v6fHSg+zv7e3hndj4vBduXLXdaXf0+dXz691E4ElHkcljZpFzyPF//uqPTzv3rLMK0cHy9Qp1daQ/t2nN5awfQXPy9R7nZNW4/fmiLt7ge1n17srpn+BKH59jyQfrkbk5XT6fbfKT8dxd6P+7+1xbfHy96X6e8Eppc1nhtZrfe8DJ6nx59e3BGEJXKabxhJfPPqcrL0+fICGIi+wq/Iy2//A8PkDTFWJQAA -->
