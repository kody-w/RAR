---
name: "rar-cowork-cookbook-report-monitor-compliance"
description: "Builds a structured summary report of monitor compliance activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_monitor_compliance", "rar_sha256": "4fd1ba02ab7122079038bfedcaf4bef3d6f340db93ae34d42519366adb6d43af", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_monitor_compliance_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-monitor-compliance:92570e1437029bcf7bb131bd48497b9ff682d68e1318b83b34c9d5af86c83d6d", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_monitor_compliance`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_monitor_compliance_agent.py` is
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_monitor_compliance_agent.py` and embedded as the fenced Python below (sha256 4fd1ba02ab712207…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_monitor_compliance_agent.py` first:

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
    "version": '2.0.0',
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/71aeZOi2Jb/KkzOH9U9ZKUge77oiEEBRRBFEdCujiz2RTZZZOnp7z4XNbOq5nW/eS9iYqyoTIR79nN+59xL/v5kNXWYl0+vT3vPyqCFlSRR6JWQlbnQPG/z8gx+5Wcb/IecPKvLyG7qvKyenp9cr3LKqKijPAPksyZK3AqyoKouG6duSs+FqiZNrbKHSq/IyxrKfSjNswiQA1ZpkURW5niQ5dTRNap7qI3qEKrz2kqqZ6guvcwFv0c97NKzzm7eZtULEOt1FqD1qqfXX397forA9dPr709OYlXg1tPuJmp9FzP/kALoEisLwIKiB/Zm4HvhlX5epuCW6/nQ49tPlZf4z9B//Me5tcqg+vn1SwY9Pl+exn+7JoPq0AN6WlUNTHSswrKjBOj/ArFJa/UVsBZYnz1cEWXBy53yG6e8gH4Zn/10F/ISePVPX55yoII1OvPL088QcNGXp7IZr19GLsVPP78keeuVP/38jU/V2LHn1CMzoPXL2+P7gy1Y+G1p5N+k/gK43sNme1+evjNu/Nz1Hu0ElE8vcR5lP90ZF2V+9bLRjz/9/FdsndBzzklU1f8U31/vjEPPcoFND8V/fr45+TcIfhj0wfOvxRYgrP+KJWD5u7hn6OGov+J98///YJ1EmVd9ePxP2f0ZAfwL9Otf2vaPCJ4h/8sT5yXRFWSHnXiv0O9v+y0///WT++3mp9/+AKz/Vzb7vCmdG4e31Moi36vqt7dfP1W3259++/VTU4Bc86z0rSmTP+P5Z369yfnBg49VP/1IC+QfsnMGqhj6yHTo97z4t/KPF0i3ksj9dr96hb6vl/EDQ6MR70LvLviuZiqg63d+/PnpDwAN2R2Kxsegyv/936F15JR5lfs1tHfypoZAgOso9UbltTCqIO1R1F/3kijLL6n7FQJ3x3IHEGE1SQ0tSitKIFAPY8RHCwCmff1P5waUn50HUE7uePf2ALu3b2D39QXSQiAvL6MgyqwE2rHbLWQFXlaPkm45AUDz83UUBhSJ7mCzm4sj0FRN4v0N+vqX3N9ujF6KflT7SwbiYIHguFDtpYDCKqOkh6wRl+y+9j4DHAXYUeZJYlvOGRp/NMXL6Asj9LKHhxzQE7zOc5rag5LcARr7EcDeZxDkKk+uAAdHv1XnKEkgNyqBU3KA9yNoA9++jsy+fv1qW1X4JbsDLwbdm0Y1AQs+FIY+fy5Kz0+iIKy/ZJ4T5tCn3//4BP0X9I+obsxHGVuA/TdHgeRNoNV+o0CgEpsULKugMQ0AzNwi9fsf9wiM2mWgy4H6ifzIuxEDbt/CPlpwD8t7TIDNo4pe+ZD0o9+gNgR+gaIaeAvUdPX8JRtZ5GBp2UaV9+7EO/Hd9e9BvssZY1I9fAji5Jd5elt7y7gxmE5eui+Q6EMfnnr01TGiYV7VIEkL0DS9zOkBpVV/C2GW11AF6qTy+2eoqYCpI+evNmA9OicFYGTVX6H1fAv6Wp6AH6ODbuIBNcizMfCPLL3fBkzKTyDHZu8sXiDFA96ECqu0irC0Ku+2zrfuGQH62Ts9YG5BmddCY+v2xhjdKviWeeu/Hw/2jxni3tihL80UQXHo/2faGFViF4sdv2A1noN4Rdsd7/kzjkKjOffpaeQHpod7MXybCN7B4x1Wv2RJBHxe9n+7r/RvKXNf850dO3Z34z8Wb3njG9Ug8GMky3JMVutL9o7fQOUxiasRikB9nsdqzz8Ejk/fNQ1BEY7fv/Vy6J5To9EgW6GisZPIgXzPc2+JXYflWDYPh4Ms8EaXgjx3wh+sggB34HXAHwJKRCAdge9urlNA+oP5557LH8ujcUICWriNA7QF9eG9QMaYriDlKsj2wJgzrgFe+HRjBaUe8DFQ8cPDVWgVd2XG8fShoPWIxff+fzwCiTe2CSDto6oAT8u1auDJFoQAFE13j+uHlo9IAVXTMcNvRD8G+2Ep9H2b+dtYWUDDb4gO5umxQ3/nGgDHZVrdUg30znMFajf1HukD8uDWjF/u/fTesD90ef27ifynf21ov3XIw49xe4XCui6q18nk3sXem9gLKBrQyJyo8KpHQ/v8qKfP3+rpB4Z3/7xC/5pSP7B45PIrhL4gL8j4SI4cb0zWxwf4YP55dvyMj0+/ZDvvW3CB+DwFWDL6vAd4+tEz3peAxhGUXjAuvveQamw9Leh2N+i69YCPBHgUB0DGLBgbXpV/V7SjTWM479H6gFjwKBvB2x0Hs8AbdyvJqH7lPb1mTZI8P2VW6v3DXcqInyA5gRvGXQ0oEzDh1JF3+2Y1bjT6Yrz+cfO1uV1YyVhJ+dgFATZGH2B509stgVJj6QWgP3nlMwR0DQAEjqa0Y/mNrd4GplUARz131L3ui1HZ+y5mnKg+xq2/1+BWwQB63Px1LGTQLMFo/Ax9TLnP0Pu+47aHyxqw8fp1nLBHm8FS8Otj7cfe0vaefvsTNR4D918r8UCXO55b9tgFRxP/xCbArfQuDei67qjPNwO/yc3vwv646Vnft4y/P70DyHh9HwHuKQUI/vf5bDT2va++jRytke42Rd1sv82abxYI/Ng/v3sUjMPA2z01n14B7HjPT4AYTDFggB5ue+KnuxpA/29T6qiUVX6uxnlgAioLcAJduhh1PwPw+07AeDtyb+vHi9e/GG3/BAlemSlBIR6KYxQyZWzHp2wbxVDbxWmcoWzG90l66pK0B27SNo3ZGO4wLmH5NOnQmEu6QHoFUiC1HtIn6OhzoPeHY//5OfvpTggaxZQgASXuu6htIVPLptDpFKEYBKNt33Mdy8dtzwfifQxHXJvBLA/DXXxKoAxGkpZrky6OWf7I7zHw3bV5ex+u36NwR4JRhTQadZ1alkM7FIq7DGWRjochNuZ46BR1KcxDCAbzadrDvZvVd9JHJMZA3Q0ekxPMemDSuo5yfn9Edkw4Egcrl3glsvfPfMLoFmXKthLaTEn6bBUz57qz9JPsu7qCVehy4doLy1IWSlYzSqfsO1ENV5coVVmktA2cOMO7FdxqlJyZOevn6T7DTlijcUoj77Zs55jMZus6B55XYwE3GwuXRGIVmcbJIvLznpjopOygi0xK+/XKxAnL8ztfsU7kWT/UsYTyib4gDhJJOieFRI/R1mjkVXKAz4W5wBb1hTDy6FykzDk87JpD4VcVLdjCjo7FuszWdny2lzIKe5mN037mk4kWMjRMVQ06p40+E/u+0XVENlArb1eL6cy0LnodSbvi2KG7atLquLly1bOb6P12HSI2ufWElIrV1LikDEt0bjYs8Iu5SYxF1wSlcGkv89jlpV1H1icLN/vkpOpoWxwxYxeRnSiXC1Kqy9qStZ3Tm2CmxBvNXCROaXGHQxIe4rKdryflRtmsjHmkd7FEhDypnmUppPuVeVqXZXIgDAN2dme2K1XKYtmynJdw5ayyWsOXA3GIunXl4SlOam3UZ/tNvvCkqX6QZMLtD5fjpnQiPUk6zVTaCcfLfFoJU9KK0XI2XR2abG/wjaGZBeXC2EZDfakIN8ApC30/d8VDn1aFFFtMQGuModDTTZmZjqILA0ev8WJKUyhBKxeib4+YiXfHCjuf02F9reh+4WzqTEP5whksJ+mSTQkjx8SokiNtwPI016xVsO6XG9jYlD3fO8JyUM+khMfbhb/hQnMdOtfqaCwYPY4c9kJM4QjfVbGt0jFNUFZ2Sle6bhmuZjkrGRnoJuSK9eFAk4J8uhwaL3JgZ39yCN/MNgq37aaodtlPZt2m22xbxA9FvKPLnSKAxjvB/TY7w76v+eS8dRcnMuml8tigJaedvGgbxfZ8hRh6UtDTw35OmrsILZxq71XGYmULTLhYNfvpwaunGLJfzZuT3Jl7rLMYTNLi88xzzzDnbOf05agtDjoTkOhujoXb9TxQjnlUXKp4Lnea0m/I2Xym6UfxsmBTNtrKTiVftOUywteRQmBSveaAE+PkjGQx7/XL3swDUsYHZp/SE+Pa87IC4kQd6jWVrhbV2d8pyjQ3pQXDy5PtJLbsDRVFvs3Yu6VeSpMzkspot4sI87CNNWMvl5I1xOKE30h43SqaNd/ONZxzmJZ2UcPlM5xGgi5euSTa2adFdxB0YefE8S4AuRChxsXD6Ovai5Oiq49G70zhq5JliC0lmw2h99fZZKGHSrZvsaIwKN9DV8pcki4YTnNc3OQnQaERPmcocxoF9sXvpSF2r5luzrMqMAV2Ry6zbkVrhlK4xmo+KVltgorXBdJtO3UCi6Ja7MrOvE5ZlfeDlFmxDYxGhL6N5wjuFCJv1vmxclJvEqzOzYZacidROmo9HhpNue6PbZEEgXYg16buhVpAraW+rA+OsVRPEeldhw26acoFtu3EgiZUAz73WIGZ3ZYOvKu9Lnl0wXcw213JqIvJ3eDlSWlXpjzxGvg6S5e0Fl7NFQUSAZ+1Di3tlXPt4BZn2c1i75y8yxKbaoTAHNWh17P4FFvtQURCOh9Q+3Re4M3yvOOGiZaymlbD5z2XSGbJkMIgEdYhrxJYWJ0Nz154orwR1gHC89gwK1a0MWE1fTMYx74yFRnk4w6O1ueUXHS2VV97kgy5wwSbrfViN+MLgdNWejK7RtKastoLPytmAW8RRBpdZqt64QkofWTKHgkLkToZ3amt/V2uaNiJbo7IkBf4HoyF/hW7EFtNgY2UU4oj3Vyza7GS1vsaP3j20jvbbJY2sYpMTzAsrYWjgqFLuVJmnRpqw4TStzjqX1t8ch2Gor2itXieXvswp0+6iSWqw5/ZeLpa7oX6QrMKXrJngzE20XkIZmmFIvywV6XTTml5e29FmhOkYXhCuwOh7GXFg1dSsWpSa49ZWj6f8sjKDuEjT634Iqoum8tuhhgcWUTnlCP8rWdK+YlBYAHHRJZ0ds1a5prCZRANsTdTmz/sdZ6DPeV0pWS8NQrNqQiks1wFF1aG1IE+TbfckWVPQmP1yVDKJNdjeKt6Un2K5dCNOPHK++tBS5FdMgSSIu+ZpiOkk6xU+ixnVA4VDyl+Kfk0o6pNdo0rlRNjrWA0ijqLLVGInSvPd86y38i8FNTDcOoP2iGEO2Fw67k9v3aE7TuoSBz4lbqN+R5GKvdwVk8tQV+nsJ6eOHzJ8tEivRh6H+etvOrbM1uuLkSTW77VSoq2Bdvb1eUseUHYCySXqCooWTw382SNZmlPX0WVUHVJs84DvzaHy5lAReuoBKdUoltN5buB0KsL5oMZVLys69VS1BZYuDLXm1WNWfVR6s67o1olgaWwVGZnBJCnauQUSeJFCNJ82Ye2hwmzTYoWl0zIQ6n1yaY8EALeM2iuiLK6sJiE3R6cpnLqUMAH1uw2MU4V/SEIm3UhXfkTlfRnJJjTUruJirUR7I3VatjJboCmK/USHqMo5AZxjS/19CBv2AiFyVig1mC2uU5jab9U2HWTmlTDAZIJyVxgxAkEDT2w3obry3TtAD02hXxszgYneV5s+10/oQeEOiKOtA66ziMKHWOccCNbFmop3q4rrtVWk/tedjWJzKi1KZLGnrZN19LzhSFo/Ny+GqkF40KwZw6BPJvpNOJWgin1xmwSyTuxYgdUDjuBmDJbjQxni0PF5fUxOEfbIJGyNRa2LX1Gl6v4gFHEXpMTV6RFeb8ntP1+yVlOpa86R0cLiy16LRF21UaNKmFWLvSCNKXIOmt9xvnoJjh1/G7YDevTvuuSy7GPYUvFC9FDkos1a/CVypsiv2LVJo1Z/ISu2HyOTA/pmhqk5dAz3PqiRpdYztEU2afbyGMuDS1OuXnf7IilMtWDjkx4ng41t7lKsL6xJON4Ks2BcyRDvBqHdIkgQ92b83QIsby3W9RSjyJuWDOYHI5oLx6dDaoarVhft3ZsU4Fy7jL3PNsfhnlSDwSVrNn9dpUjjhwlw0yKpQRT9xfFjQ5IN1XpJs04plr6tHgiZvg1s2ZrbHDgxVboxDp3D1EbF6JgkPy0I8mDeOxxm1qRc8d01rowO1HUAjEWwb45L8wmsDmi7RkdcSanNJqHK5lzDl243x1Uqh8idzO/6JNkgy3wYpXZHEAZzICLRddbMbbb2NkWk8S4LlnUgFkYrvALzmnl3pjzNWurC0FNDxp8tN0BTtp5B4bbYlaUSLpZHISDUM5UKluqFraT0uV0f1aQNECvEx7RluWUzYIUFXxeyo/GwBMyq27aCUjYfr4gs4nuOIEW03kFqi1fK9tW18TUJHYXuW7XSRgtdodt0tih12/QkERTh7UzZafnpCA4uXLQPRTN1WsVnUlF5Kc1wajO5ShJIekXJ8mZ9oMQOGcP490yX2Gpya1MbbWTlmY1uU5lfYETjkEriFJVXgYAWqK2iikuUMOf11xM5Pas8HfbVIydZSlsZU9OtdO0w3GSXyvdLEQ11tzqXY1eYbZRz8SxX5o7vV95hshG9BqOw4Nenc1typkpam8ugSbqE4aS0OhqlXqJxrFHqFYM4yXwrD2zSGJtFMkyRbYcSUzg0t0LTMPR8FIq/cZvHdmbLllXJYL5vE5rs8Tdoi04YcoKm2GNTwtkprciLGGeXqkGX8Nbbyhpc80dE0TQxa7EjeHqF4g0y4xqyKnrRXSC5cRGlvCeU9UBXunmhZkY6PKYo+wSu3oXp4ePFMC8mnbkySUvCK85o8GMcyeugWWH0JhuydZY4InKNpvS52CTO5Mect1OYH45mYOZTyOpCUWrkwFBaoTqTlujnzbIsrRMplIFmTEWfS3M8I03n0gbQS7P8lzor23BsC2hBOpyfz0JR+20BmMBQuDR5rzkl4mY7FWRO2/7E5a0jayvZWaQpkdSjg/irnex3NrO2jntGpwygU2BGrJMWnfk/rjohUQYK+4sO+sypRcsh00kMkTgzA/gBRyRs1M3D+ArsuFpSqKuZxmuGh7eT7diLgW0Sm+oYVI0bOselCLeho0VWQ7sRe5p2RBWPAGTHHChuYXxY74fCvvqsEnO51Xgbq9ttQmp00BjdSqm8Ympc+/YCd1Rr7tTacFMQnpUV+qDAaa0jaF4ldutKX+LYzYxUype2LCZfT1UqVhvu/Uh4jeisZqKGeJXuDwV4Sb1iSlp10HOMg4aedfgKsi6oMqoo2Eom+xbh3cmNYrzm1m6B8moDc1yF2S471BDKGNLwzE3W+9Q82abBJEoTMwKnpS7vHe3bTxDlm1UH+mp0yjMHknXRRBjc5s991eFW11V0IGy/ZFDNgLj0ZkOJuswGYSBosU4VC7kNlXiphI9iqT4pdKlWECtKOTgDBsOtlsfAFMZdqh3mkk8OtgavaAForyGm/oy7T3MaLKFPw25aCm0yiqLowjM0oG9WHDXAUUXXuvMFo67gUNYXQVodqksygpNbnZ0aw4tm+ncjBuqNFdgBsQjW2kkjt8wVgcvcryp1QW9ZPAdwSLcbGFPjwXqIdjxvGNP+y1+hIUhYCzx6C1z0NX6C1mY9bK+wv7Rzl27Y5V5g9VMgG+vslLDYHQuk4nuV1yPl1kyyKrd4XuGdYvjRlEnuaBak6bh7BzUiL9l7SM6I3f6VLIIzelc1sRmpxoeMHxJMTTPUomvbjBaL8k8EHbt/LoQeJXLEklDE7yGLdqlxOnFdHY5ebpQi/4awkhJH43Ams+PwsWC5SUG04eO27X9cj/dU5QdeNtq2hCVi1eT/IBj1m5HMp4orQt3CSAPEfFtsGWwZM6to/QaDSCglBMeDlPadursMMWoKZLZ2zTHaz3YzpF4TlLYBoAKEXC4s2XworRoaUls0IzLWaEM555cqsLpyqQ7QYcLl1hbwQk5XZj1+jqHq3p6dCX47KGZjJVrul3yRqv77slYLydbxN6LnDzh+RUV12zV89PGVN0Bc0P7SrYzPYEH9AS3Fa8ut1s5U+ZJrIedQewm62h2mICZViuvmRuD4X+JE/SsD9JuWG+wehadFqnUiXP3elmArboQMjtCWKYZfXJUriGpmjuvwXzcKFicHpqiZWbwVq5WpBIFLMv+8svT89PtxejTK4pMGfz5aTx+fxyi/1PnrMEQFW8PFhg5JZ6f/u8OBe8HdO+v027n2Z7lvt6kv/4T2v32/FQ6EdDkfiRbJU3wOAD8Hwedn//y1HUk6++vcMf3fF39/qKhtoLbaXCUuU1Vl/1blSfN7SwYeLSpxj/aqMa/63HA76ebGWkxHrzfJYELy02j7Paq4K3O3+4H46O4KBvfX3lu9O1r8Dgzf35yexCbyKneMJJ488piNPHxSmc8Ex3f6Tz98d9GGBIjdCYAAA== -->
