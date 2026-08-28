---
name: "rar-cowork-cookbook-report-monitor-compliance"
description: "Builds a structured summary report of monitor compliance activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_monitor_compliance", "rar_sha256": "8b65b1229e92cc643980da80f839ad45c984d63c557d7bb99ae9db09f14ce33e", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_monitor_compliance`. The original RAPP
agent is preserved byte-for-byte in `report_monitor_compliance_agent.py` and in the RCI capsule.

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

Monitor compliance Summary Report — Builds a structured summary report of monitor compliance activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-monitor-compliance
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
    "audience": {
      "description": "Optional. Who reads it \u2014 this drives register, length and what can be assumed.",
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
      "description": "What to produce, and about what.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_monitor_compliance_agent.py` and embedded as the fenced Python below (sha256 8b65b1229e92cc64…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_monitor_compliance_agent.py` first:

```bash
python3 report_monitor_compliance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_monitor_compliance_agent.py   # or on stdin
python3 report_monitor_compliance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor compliance Summary Report — Builds a structured summary report of monitor compliance activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-monitor-compliance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_monitor_compliance',
    "version": '2.0.1',
    "display_name": 'Monitor compliance Summary Report',
    "description": 'Builds a structured summary report of monitor compliance activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-monitor-compliance',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-monitor-compliance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '865a7b11b998fe8e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-compliance/monitor-compliance'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/report-monitor-compliance', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.286, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:report'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class ReportMonitorCompliance(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportMonitorCompliance'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'audience': {'description': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What to produce, and about what.', 'type': 'string'}},
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
    print(ReportMonitorCompliance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/71aadOi2JL+K8w7H6p6rHoBWYS60RGDKKgsIouAXR1V7CD7pmBP//c5qPVW9dzuO/dGTIy1KHBOnswnM5/Mc/S3F6fv4rJ5+fSiBU4B8U6WJXHQQE7hQ2x5LZsUvJWpC/5BXll0TeL2Xdm0Lx9e/KD1mqTqkrIA05d9kvkt5EBt1/Re1zeBD7V9njvNCDVBVTYdVIZQXhYJmA5E5VWWOIUXQI7XJZekG6Fr0sVQV3ZO1n6AuiYofPA+6eE2gZP65bVoX8GyweCAuUH78umXXz+8JODzy6ffXrzMacGtF/W+lPRYhn1bBczLnCICA6oR2FuA6ypowrLJwS0/CKHn1fs2yMIP0H/8R3p1mqj96dPnAnq+Pr9Mf9S+gLo4AHo6bQdM9JzKcZMM6P8KMdnVGVtgLbC+eEKRFNHrY+Z3SWUF/Tw9e/9Y5DUKuvefX0qggjOB+fnlJwhA9Pml6afPr5OU6v1Pr1l5DZr3P32X0/buOfC6SRjQ+vXL8/opFgz8PjQJ76v+DKQ+3OYGn19+MG56PfSe7AQzX17PZVK8fwiumvISFBOO73/6K7FeHHhplrTdPyX3l4fgOHB8YNNT8Z8+3EH+FZo9DXqT+dfLVsCt/4olYPi35T5AT6D+SvYd//8hOkuKoH1D/E/F/dmE2c/QL39p2z+a8AEKP7+sgiy5gOhws+AT9NsXTVmzv7zzv9989+vvQPT/KkYr+8a7S/iSO0USBm335csv79r77Xe//vKur0CsBU7+pW+yP5P5Z7je1/kDgs9R7/84F6xvFGkBshh6i3Tot7L6t+b3V+joZIn//X77CfoxX6bXDJqM+LboA4IfcqYFuv6A408vvwNqKB5UND0GWf7v/w5JideUbRl2kOaVfQcBB3dJHkzK63HSQuDvlNtNAHBtEwDscxyI/8nDk8aAw77+p3cnxo/ekxjhB799eZLbl+/k9vUV0oHAskmipHAySGUU5XPhREHRTYtVTdAGzQXQiDt2wUdAQB+nD1BSQF//UuaX+/TXavx6J8fkwUcqu524qO2z4HWyx4yD4qm9B3g9GAKvB5Kz0gNqhAngzw/AzrbMLoDLJtvbNMkyyE8aYGgJOHuSDfD5NAn7+vWr67Tx5+JBnhj0IP4WBgPe1IE+fgT2hFkSxd3nIvDiEnr32+/voP+C/tGsu/BpDQXw9xN9oOFO28sQyKY+B8OAY4ArAVXc0f/t9yeqQEwBKhXwVRImwWMyiMY08L9BrG2Yj3OChNwAQAtgzSdIASNDSfcKbUPoTd9nhZo4Oy7bDvKDCpSfoPBGINUB5rwhWZQd1IKQa8PxA9S3wX3Vr27j3FXMQVo73VdIYhVQIcoM/DepeR8EJgNfAvjfAuBxHwhp3rXQ8puIV0ie4g+qnMap4sZ5rhE6D7+AyvBtOhDuQEVw/VxMVTCYoLonwwMeMAgg4z1d+nHy+VR2Qeb77be172OcqY7p93rWfC7aZ6A7zeQKDxA/WDTqE3+Kvb89Q6qNyz7z7/gBTSdJTy/4T6/cY1D6+2KvPTuCR5mGPvdzBMWh/5/eYVKJ4Xl1zTP6egWtZV21H1BNjc0E6aMXmuSBeHmkxff6/o0dvpHk5yJLgN+b8W+PkXeAn2N+sENl1Lt84F0A1ST3HnxTMDXNFLbO5+IbGwOVoTv1APxBpoJIngLo24LT02+axiAdp+vvlfnurMafjAYBBlW9mwHnh0Hgu46XAq2aKYGegINIDCZIr3HixX+wCgLSAepAPgSUSEBKAOzu0MklMBPkTtiU+ffhydTvAC383gPags4xeIVMkANTHLQg8UDTMo0BKLy7i4LyAGAMVHxDuI2d6qHM1Gw+FXSevvgR/+ej7zF712RSHsh0fKcDSF4n8vSD4eHXNy2fngKq5lOW3Sf90dlPS6Efi8bfPhd3Dd/4GiRvNtXbH6CBQNLk7T3UJu5pAX/kwTN8QBzcS+vrozo+yu+bLp/+rr9+/6+14Pd6Z/zRb5+guOuq9hMMP2rUtxL1CpIGlCkvqYL2Wa4+PvPp4/d8+oPABz6foH9NqT+IeMbyJwh9RV6R6ZGYeMEUrM8XwID9uLQ/4tPTz4UafHcuWL7MAZ1NmI+gPr5Vj29DQAmJmiCaBj+qSTsVoSuoe3f6BPB/Lt4C4JkcgJ2LaCp9bflD0t7LKHDnw1tvLA8eFR1Y25/arCiY9h7ZpH4bvHwq+iz78FI4efAP9xwTh4PgBDBMexSQJqBf6ZLgfuX0fjJhMX3+41Zqf//gZFMmlVM9nAj7jSzvevsNUGpKvSiZaPsDBHSNAAVOplyn9JuKvgtMawGPBv6kezdWk7KPPcnUH701T3+vwT2DAfX45acpkT9AU6P7AXrrWT9A33YR9x1Z0YNt1C9TvzzZDIaCt7exbztFN3j59U/UeLbPf63Ek10efO64U/2ZTPwTm4C0Jqh7UPD8SZ/vBn5ft3ws9vtdz+6xAfzt5RuBPL30bPbAcJCpH9up5MEghMGC4PoRbODZP98GPicCpgPdCJhJuSThovM5HdBzzyNxjKYQ36GQkMJox8cJj6Zwn8Q8glj4C9elaSegfRehQxT3Agyb5D1idVojTyZlAiQMMBqdez5GzgkCp9HF3KF9B184jo9Q1AJZhD4oBt+npoAonxY+LJrge+tI7xH6MPS3F5fEwcgN3m6Zx4uF6aOzsERXjl26IUOmPdNpNzjHkxj6Rxlr0Q3vu7zjyLxcdLQ8yNqwPcS7OskPDNK4Jk6kM3U3u+oLsbBKJixzrcBOWK+v5F5UFWbwLHqv+J6xXh/OHG71Di5siV1imSeHKFONgI+k6KF8IeSjtLNwwgnCIZSdE5keje4soOvsyBOGQJLeSSZRO1HMXtxlxiytLB7ju5owyyStcjqNDbU3qrBtKc7lVOq87ZpCcs+puxHRWVC4OBUWIZnpMU3NFm2PspQ5Fttx7I9HRDRRp7zu+PnScupjlwhqZQ+o2sLXI27t/EPqZ8dRkWLEJZWAyxfnQ27WOc0Qg1/ceLy29pnJD33UcPW1Zs/+WlAHsjs5uDVmp8MRvVY2ZqoJOWzFhieFrukcUVe90QJdD97rFp95jbMyjCw2zs2VleBmL+93Jpsch7NAxGvykIpCTI076yQ1TWYQpjnz1JQZmsPCYZimYZtZ6+2KTsc3N8JIBqkN8Bwn9WsyFtq+5ANhfjQEkfBHo7b3jZccs2zQLfkKr9biOm+5Oemc0WY53xl9oZnr3tStauHPsL2OhkIV7wEo/FFj/a0x5m0lnB06onTalKn5viksTz5ytxUl4dWcWqAEJdfEeLUxCx/sFkvT/CZdWmrkvX1X6Oi68m6Olw3Zvpkhdma2mU2ZM3Fe6s4uksbNfmbum3E9etzmdkhJAT8rfLhfxZYUe5fWNnn6eE48pibmswRX27N7oM4UsXCKU747Hh3T1x1vJyI3qo9XlWQYFMmJp9rog8SbedrJI0Kr2MsrZZijeq3By2E/7JUrEsZbfKAaVeZAaYDx8FqkszDUQ5K9+vyJzEahsXu0WemnIFGSs8vuEPOYVdTc0FjSUhO08lotaE1+53J0zO96bW4E3RxDtB3bn8TB0rDBoTFBP6fLwE9nK09hqdrWeeNIRySqslisSGwk22VS1e2ZFQddHvfkkl3qR3tb80zOJIrotWKtbzYJLiUygQmdtAIgnrMUKc7rYNyMVhmRIn6jtZyCzct1zRU3T1nPUFHfE4na7DaIrvs1N8YXlYVvMD7Pbz1eFnPYRFTUGS+EvEtoz7D7I7rCETRNSOBvfFSGVdKL3sqYR+drOmMwxVM2/rEAqa/IW8keraDzzLnaHpdH1bC2OGKv9oLdHeuig8XbpiQczzW5tpAvze1E0PxY6ef+6DXXcMhs/YS0MukcewzrNP2QJHU3U5grvqh5VQ/lpaAEKF2WPFlQSYtjLoEer9Viyw2HdRATlBau0bNjHZPDhbyuYVoTh07SKUOBE3YtGA51XNDRernBdxftIF46YJyOX7v9RtCW3MLhxc2uuODsSTz3w3Wusfma6rfHpr5JuSSc7O0a3Z851CoNfH9j23px3HAxwtt90VC3Tm/qobtRmhDuDe5SSR3po5QObzfN/CYMshpLYSS5s7K1Z6mH1TtnvuBGGGsuzfUUw2vcRccAWzGRXIfZkh/NPJCXmYKdd5J08VcLdzcDbYZwIoRhkIbOriX7EHgu2aXXFWUtx21FwLsFs6vmtFYtr1mDzmiWKDyZNc0RZtNRVECogzBg0wMpMO6pnIPQC6OqLk7i+mSKfTZoTAkP/EH3RbvrTIzwfS2uw0XEC0jJ1GayrNJ6jNCB4/0O9xnGiEZWNqib6jPpvFFYZ7YPUMI+GG3YioceN4saySuiDSzJOSEGVbny/oIRqHdpclhUlzzSBlg4YEaa8TtzJly480WTI123wOZVl2BYXrPtniDP3Zxn8PpQETQtXChHwXAvhBcEgh/Jeaq51qAhM6ls3LHcsw6jLtZxxc7RgNlTx8jZBeJG1U5X9jbXSPYUC1wb5TjLNfKwbA+6PbYkXnt8tckVa50hKaZ3y1O3Q1Yu6/DdAZNYuo0M1bQ2Rwbk1I42BkdfUkV2ETtTmpEh6+k54/NbjOfOGJLPyN2oFAsuESohWcIK31poQdmiUe3NgMQ7KffYvOEOWHec2Utpy0gsppw0As383cL1DluFC9ohu7ZDnB4TpXcr3dmOJ3zDZ3GA2VQmZT0iREhQLsdc0L3jMXFVeq6omDrbLtenBgkqmtYk2zNau+dioT8THMfKmnkaeqLe1QfYjoj9LJaXIUl1l95JjZpNy82QqKEz52ttK+HezCJCYQGYdhWxw0o/isJCNexNShwOzLFFPctTFNnm+KoAsb3GNE45HE4CvNSibbCMKaNBDjl5G06BlW+pSMiq7nBK9jvi6ATkWt7z1/WNCw5iydoEJcyO7mXWHVN/ba6bfLdyr2nTb9bmAgDMOeM23ZoarvCRf+tuyE1WGZFeOIdhZWfisVkcusspiS6qg9BqYhwK+0Jbx9pIKMLEET7dlGfZG6NNuccCyTzUsxOzIguVCpGTcDhYvJFZ9Z4eh4NzXXqcregGvzrsRCklyqy9Ord1eTy0qmrHxHrvrWpAN5ut7oS+mtD5GsvghZrtlnnEW3pDY0uuH0PfxEJnr7HVWDLKZkmgt/WeT7nCyHpLW60yRdE7BV+EsxPpt5rE8baDK968Xszaw4a7yGTGXwBzYqbSZKcT1+86X6dzMfVXYtCd265GVmISR8sOa3Q5DFigd32Qk6ie2fs5C+aIDKxyZWpuTySHkwm1CIodrUVnwVgaZnsYVe46ZmruXnF75tjnlKhdn6p22dimwXpT7Yyq2q3irg+EFO8F0uhYg9hdk3LObYeAidBGQPxVpsrajrhVHbmx9zi7JcpTvq/w64hKqg7L28BIFUc7cgzmrUu2adl1xBx1tfQkJ02MWDsJ+t4nuBVBzECgb09HNUOcG7nTN8MmQC1z7S5j1yqpc+4KVxuozwZ21VtWFgqFwonSHhWHc8+JvNUI+spx3PlpFevEdYGABtGRmf3aExUmPLqtM6ylfuOUor02rctlkOmRH+2h15hKICptfqLAje1ukyL2PiMOBJPpmXYrdyjfD4LmLErzqN/i2fxczNYSElHW4sLwOtHDIpfgqYnsE9VWqZxtjqxrgzZpvXY9Gc1B8Rf7XEgiCYXP5Gp5qKzDSoQ1eYmQp1lC7uF0UJd2nsW9YB9iod76i9PAF0tUgMdCjz2kvXVxIWaLJjRWh4Ws3sC+fJEtOEmdo5HdwEwYmoblLWO0anasyXD1Kol0YQfv5Z6gNXvpxIFoRGCTqRfilhUELCr927mUT2WmLxeVtiZvto3Btb07owRzw3UnKRIOkcQTa2TRVrFDTNudlmKow0m/PyyHmWHKlwXF8wW+rVJ3R21pbo7vD1d1ta0LEpMPxWnj4LCj7xlZ7+sa8ZmkN/i6vjgkwhznquPzqeCaINz3x/WGu9Iy0mZ7l1Cja+8oLstjSLoYxLhtqnWZga7GxxZcfaaMVpztcX4eKLrO7Tj6kjbpym4ulRmrFCJHVFduFmt1L6JJ0V04fdkvbMTzk/0aj3CyisSsxmc4BjPWVjP606opa2LdiWtGD/hQB906ojWXYdks7G7ja7tUoGd05gxWZ9VHQGSKUcsqHBxbue+YLvR40RjPC2ezpD0YPvZVMsOWM2uVoRdMsXnu4orJfmtcl3EwmCI92xu4GbMLli3U1Ft4JCNc+TBzL8KcEdk5xl0ImhL5XQsqVJnaKCUScIeAIL6J5gnxMXTd2yu4G5fwbllvT/C6bugAbrRzazjRaoFdjr0aSjSSUPOZxIW0aVDFUXNwNu6xtlks6kOjb2h8tfK0iLEK/xKHq/NIK45VYDC7gmPhmIm0j8GzrUWQZED6eFo0hH50VnQnBjOBzebVigiiiNrIS7jj2Iy+ckuBsHBjFuFGet2KlSXV7U7qWYQZPWpQDqtkNaZavF3H44Zob1cc4+qcmy8yVwo5tea3BE8gMmhhY1Nq4pyGxZom9FvB26gonU/MmMyWl0Dj+vw4BKvtchF24YEM9cvVWoWg52jtWAuxccMGfuZbIwfPLTasdC41OC0og41/wuZYdJBqnhqKA6aoHR8q6r4/W95Fhc/1BQUQbkBRMHYnpMNaZkQYY27vC+xqbg50T8x05LZ21TaYz5XWTvBWQHAJ7cJghBUfx2ribPSUsuMvwR7P/UvhuR0V5QjLXhi9w0rzJhkFnm9VdsOL6wWvk5u5x93WIeYqlOvL84PHBnttAO2MlWRJUmZkv3PJRKsOe7YPEZISNoy+tA67eIGtylGnlNY/4cXi3EhisemEebLDtau+TrBmHoZYiZykwga7yxWum6152mM8VZHu2riqRNxFh5PVn1MAiLi8NVJMbtjZxdPrJJ0dyEVCoNR6uKYorQz8gJlrxaf9RMxx3R39FCWF/lQsQxlXxouLXq/4RYoK1iG6aiZ6LEWj140J2vHNqcHcWHEP8bCqcX59uw2Df46vXLxawiCuzrLdM/G+v4SHkFmD2oqZst8dxDhqQT9Cothp2RCYf2zSm255apejXFxvgu4ArxDvaJZisAoogWKcVXTmFhIyXpxFq4EOqtlQks8S16BLJWWFHMD2zveNZnaeY5jcdpTU4REfY+58dvU4LMvnMHIi0REuL+aS8NDFSHClglNLL9oj/SaPQoQt5dAKVx2i2JZySWRJS+gyWXCy0fR2H4lu2c9hdUGdUWrGbsPxUm7cgEVpxGZKfHk8s/V2qZPZziFnJix7ezp1j2IO6qaE+eeTdQ01ayatDvJyt2dROeTONzgQ7HOJq6vK3fl0hyubuWt5Jk+ZMCKA0BJK2uzW3N7oV7N4cCRvc1WohRYv80E/DgRwqJ9rdQ1KT2/ealcHLZILttmeZ9bAAY569ulFoRhjcI2p/SagTFQOuBV1sW9LimGP11jh6JJtMepWJjVs5FQuHyQStHo5b8Xh3CSkPgu1izNkCzQN8FUi4sKlb5v1Cr7g8k5aZnDNrOlhHs1V1rXEek8s2quMgW4zGeHT2MK4yWzPlyzT+7Om1iMueiXMq2wdgp62otHbfugivaG8gFkc9MMiL9x5NKzPOndIl3sMXS0vZHKYlVTS3PTZut0uYd+fxyOvawLG34abYBn4LILPNMYMoB1iGObnn18+vExHws+D3f/9O9jpOO3/7FTvcQD37Qud+4lq4Pif7mt9+id0+fXDS+MlQJPHWWWb9dHzgO9/nFR+/MtvAKZp4+OLzOmbpqH7dtTdOdH0i5uXpPD7tmvGL22Z9fdD0g8vbt9OPwJop9+JeOD95W5GXk1Hv4+VwAfHz0GzMB1Wf+nKL4+j2Wk5UH6DJg/85Ptl9Dy1/fDij8ATidd+wUjiS9BUk4nPLxWAZfNX5BV9+f2/AVw8aTvEJAAA -->
