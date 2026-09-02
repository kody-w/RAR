---
name: "rar-cowork-cookbook-report-test-prototypes"
description: "Builds a structured summary report of test prototypes activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_test_prototypes", "rar_sha256": "727771c3182c86859be479d1e86e5242333ea6cf2f2aebd3593170f469a66d54", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_test_prototypes_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-test-prototypes:bc300c33b2fa9aaf9d25fc7a7558c60107f556b701ac7c2db49ab5ee89278a89", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_test_prototypes`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_test_prototypes_agent.py` is
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

Test prototypes Summary Report — Builds a structured summary report of test prototypes activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-test-prototypes
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_test_prototypes_agent.py` and embedded as the fenced Python below (sha256 727771c3182c8685…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_test_prototypes_agent.py` first:

```bash
python3 report_test_prototypes_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_test_prototypes_agent.py   # or on stdin
python3 report_test_prototypes_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Test prototypes Summary Report — Builds a structured summary report of test prototypes activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-test-prototypes
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_test_prototypes',
    "version": '2.0.0',
    "display_name": 'Test prototypes Summary Report',
    "description": 'Builds a structured summary report of test prototypes activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-test-prototypes',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-test-prototypes',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b4672b37774457e0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/research-and-develop-offerings/test-prototypes'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/report-test-prototypes', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.333, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:report'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class ReportTestPrototypes(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportTestPrototypes'
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
    print(ReportTestPrototypes().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/716aZObyJb2X2FqPtg9KpfELurGjRi0gRACiU1Au6PMkixiFYsQ6rf/+5tIqrJ9p3vu3IiJkcOWBJnnPGd7ziHl35+ctomK6un1SQVOjnBOmsYRqBAn95F50RVVAt+KxIV/Ea/Imyp226ao6qfnJx/UXhWXTVzkcPusjVO/RhykbqrWa9oK+EjdZplT9UgFyqJqkCJAGlA3SFkVTdH0JYDLvSY+x02PdHETIfCqk9bPSFOB3IfvAwi3Ak7iF11ev0Cd4OJkZQrqp9dff3t+iuHnp9ffn7zUqeGlJ+WmR4M6dh8q4KbUyUN4t+yhpTn8XoIqKKoMXvJBgDy+fa5BGjwj//EfSedUYf3L69cceby+Pg1/lDZHmghAkE7dQOM8p3TcOIXgXxA27Zy+hnZCu/OHE+I8fLnv/C6pKJG/D/c+35W8hKD5/PWpgBCcwY1fn35Bigrqq9rh88sgpfz8y0tadKD6/Mt3OXXrHoHXDMIg6pe3x/eHWLjw+9I4uGn9O5R6D5gLvj79YNzwuuMe7IQ7n16ORZx/vguGoTqD3Mk98PmXvxLrRcBL0rhu/kdyf70LjoDjQ5sewH95vjn5N2T0MOhD5l+rLWFY/xVL4PJ3dc/Iw1F/Jfvm/38QncY5TNh3j/+puD/bMPo78utf2vbfbXhGgq9PC5DGZ5gdbgpekd/f1N1y/usn//vFT7/9AUX/UzFq0VbeTcJb5uRxACvk7e3XT/Xt8qfffv3UljDXgJO9tVX6ZzL/zK83PT958LHq8897oX49T3JYwshHpiO/F+W/VX+8IIaTxv736/Ur8mO9DK8RMhjxrvTugh9qpoZYf/DjL09/QF7I7yQ03IZV/u//jmxjryrqImgQ1SvaBoEBbuIMDOC1KK4R7VHU39TNWhRfMv8bAq8O5Q4pwmnTBuEqJ04H6hoiPlgA2ezbf3o3ivziPShyfGe6t4Hm3r7T3LcXRIugsqKKwzh3UkRhdzvECUHeDGpuCQG58st50ARRxHemUebrgWXqNgV/Q779uei3m5SXsh8Af81hBBwYFh8SbQaXO1Wc9ogzMJLbN+ALpE/IGlWRpq7jJcjwT1u+DF44RCB/+MaDfQBcgNc2AEkLD8INYki5zzC8dZGeIQMOHquTOE0RP66gOwrI8QNXQ6++DsK+ffvmOnX0Nb9TLo7cG0U9hgs+ACNfvpQVCNI4jJqvOfCiAvn0+x+fkP+H/He7bsIHHTtI+TcvwbRNEUGVJQTWYJvBZTUyJAAkmFuMfv/j7v4BXQ47G6ycOIjBbTOU9j3ggwX3mLwHBNo8QATVQ9PPfkO6CPoFiRvoLVjN9fPXfBBRwKVVF9fg3Yn3zXfXv0f4rmeISf3wIYxTUBXZbe0t14ZgekXlvyDrAPnw1KOXDhGNCthLfVDCXglyr4c7neZ7CPOiQWpYIXXQPyNtDU0dJH9zoejBORmkIaf5hmznO9jRihT+Mzjoph7uLvJ4CPwjRe+XoZDqE8yx2buIF0QC0JtI6VROGVVODW7rAueeEbCTve+Hwh0kBx0ydGwwxOhWu7fM0/5hJFAfQ8O9mSNfW2yCEsj/wXgxgGE5TllyrLZcIEtJU6x75gyDz2DIfVYa5MGJ4V4G36eAd8J4p9KveRpDb1f93+4rg1uy3Nf8YITCKjf5Q9lWN7lxA0M+xLCqhjR1vubvnA0hD+lbD/QDKzMZ6rz4UDjcfUcawfIbvn/v38g9mwajYZ4iZeumsYcEAPi3lG6iaiiYh7dh/MHgT5jhXvSTVQiUDl0O5SMQRAwTEfru5joJJj6cee5Z/LE8HqYiiMJvPYgWVgZ4QQ5DosJkqxEXwNFmWAO98OkmCskA9DGE+OHhOnLKO5hhGH0AdB6x+NH/j1sw5YbWALV91BOU6fhOAz3ZwRDAcrnc4/qB8hEpCDUbcvu26edgPyxFfmwtfxtqCiL8TuRweh668g+ugSlZZfUt1WC/TGpYtRl4pA/Mg1sDfrn30HuT/sDy+l/m78//2oh+64r6z3F7RaKmKevX8fjeud4b14tXZLB5eTGsmkcT+zIU05fvxfSTtLtzXpF/DdFPIh6J/IqgL5OXyXBLjD0wZOrjBR0w/zKzvhDD3a+5Ar5HFqovMkghg8N7SKMfreJ9CewXYQXCYfG9ddRDx+lgk7sx1o36P6L/qAxIiHk49Lm6+KFiB5uGWN5D9cGs8FY+cLY/TGIhGJ5N0gF+DZ5e8zZNn59yJwN//UwycCZMS+iD4QEGehnOM00Mbt+c1o8HRwyff37Ikm8fnHSooWLofJAS4w+OvIH2K4hoKLoQ9iRQPSMQaAjJb7CjGwpvaO8utKuG9An8AfiACQq/P7MM89PHcPVfEdxqF5KOX7wOJQwbJByEn5GPmfYZeX/KuD2u5S18zPp1mKcHm+FS+Pax9uMZ0gVPv/0JjMd4/dcgHrxyZ3LHHTrfYOKf2ASlVeDUwk7rD3i+G/hdb3FX9scNZ3N/QPz96Z06hs/3tn/PJ7jhnwxkg6XvjfRtEOcMm25j083w21j55sCoDw3zh1vh0P3f7kn59ArZBjw/wc1wbIGz8vX27Pt0xwDBfx9IB0RO9aUeBoAxrCkoCbblcgCeQM77QcFwOfZv64cPr38xxf4jAby6Hj6ZeDjuYoHDOE7A+BgZeLRDk+TUoybohA5IknLpCep4tIf5LsE4LgnAlMHoqTNloOoaBj9zHqrH6OBtCPrDpf/Defrpvgt2Boyk4DYao2ka9XB0inlTakoyLiBoxkfBlAIkRmA4jgOH8gIswBzg+jjJ4Cg9CQiKcSjKJ4lB3mO2u0N5e5+j3/1/r/43yJJZPADFHMebejRK+AwNJQN84uIeQDHUp3EwgfKD6RQQcP/H1kcMhhDdrR1yEo51cKg6D3p+f8R0yDOKgCt5ol6z99d8zBgOfaBdJXKZigKWbY7Xbjw5af6a0xeOKJ8obeHPs9DG/SJnV2ks8JNmr0dkErmHWmJxbL3LuMDejpjtuNsr2rkRq4qdZUTjYW6LiwkMHUEbM3ZZjAM1Pa27ttHSppwd8hVwtUOPEUl3wEotblBmtFKnVeoYh8t2cyiTatPXkX5YjKWWS6mNdwLFIixRWz81I8FJD+2sxFfZcaKUtkDHPtnnVrZKAiE/UUzPFQx/oRg/L6nRDkZmJOp0cD6O6TUEiaLrRI6Z1CxOxKYJnERUU+kkeJu+Vdt1aG5OUj7anJfk5sSGRxEcFxt0u1q0rd0ShpDVJa7IHm9PL61wTPXzwkp1Oz566WzWHil2ftTsvhIsYuV7B0NauaXJ7anW0076MXAnh7ghryfMGRcuJFUV2F2+jOxNs8zLbr6dVhfHVmtF7fO9IpDBfq4IapNvWm+SYucVVdkieuVDXtgujGTex6F67qlrxvXNpcp71I+dQM1yq9e6OOVKVJ/v/EDtV7PpmSBFy6m8uDC3zMKUuoDnxWVUC1zvHqNqgeWGJy+xSXvQDCsbj6saL0d6Nfd5TnCNcDWJ8jlx3LcEs0RdgcqntUvWPi+3nXVysxlBkopPjqur5RrXVXFpc4KxajxaSZkb2Gg2DVeNC/rF6Lq1e5PTT2daiSstUJXuPK3iVlOlaBvzuxE2D/tlD5wFfooZoM/HRLbwLnlOHA+YLrJAHV12a9NzGyfauKCL7B15RNHttVZpsaupbELsTSEn/Uw+SqsdFyYzRkuviaaWjZBdbd/yiHY75nlGTjfT5ZJekiP+OBV4bpdygr2ZT87jBaFPMxEfWbutGVLLHhvX2gFEshmHPbOy2qZep4pyyHLG3hfmCduaEp/EEhp33aY811YnxQf3eDkFo+6yRnNulNQRc7q2gup50epa7DpXIqukiba2amKL0liKYE52Qoiq8YYq1e36vJrja7pYrlcSWsSZNbfmy0uwiqSDTdTaLFHOO4LAl9QurEgCFeg9fQ6LyFuKesvtmhTP48n0yNkVToFN2iRTzTldNGpbbCcnSr8WQkDstqIJMEtX3KDi2VMKzKlVxYxuWiPlOjMPeOIbtrL3bJ7IL0W1ZnXuLIRsOppcpSk+26eBJoJZtt72VlJbXCfxZCn2e8bQ0qTSCZ04nRmwdvspze9FjjovlWQ0Gs83ahkdd2e9EMjTaIL5m0jOaifVGH1rrXRjXgmzSQBcp/C0USEoOVWkwhJLzomRH3AANhkr2st4wy4mu1282WcnKt6gG1Po+KAtciLFFlOHJ3oFsJuVvp4G6/yysGNc2XNYOzkI5FS6XlNzuUsBxjp9L5h+mJlOtN3LSZfPd2K2pFZRqrXOPCzCDtbY6WBZI+4aK4V4FReRN9dcMR6ZjdY7EnbdYjtDLraNvY2IMUr6voavMz+0M73PziG74i0TDRzBXcFWL026XUi0oyCSF8SuLaSZPMrHQDVHIJ1x20MGeC5h+UuScYdTEZ0oUCQ4e2wPqXft3K7XVsu84vqF47OC0Hux4I3n3HWu2ucilXdH7Bqc95R18TU+DY9nBTrRX7trVlSKaJEJkZTEfNCtIqqttlYrqqVWyKrF8c7murhq9qpRs8kx1nRfIesiWq30zb6azG3fXWeSvNqKUcftrWieAbsU2FhT8hnMNdyHz+SbvVNzbR3Oy9QDBeVl8oYCojYfZb7klhLGyFozAjljWdbFlNszviuFzXZb0Urr07WqhGtBqyaNQATjrJsZpudfRsSc1c010Wbm9UKc8+OFZtprOelHoNfK/XizCfeGAYAh9So7562lvzlwx+s8Ds/zPW14p0zdhPL2GjiXLdEoF3BiY2phaGK3Kj1tXcaVcFJWJaQncy0tde3QdH648XJlIcthl8vr0RY96f5yfKFnwkgH7VoJJMpWUCMGs5O6aCy8N0/zk9AmBAtsMbap1lLbkVfKo2lC2CSjLpc6ei2YHDfEeIYl2MLVjLLO/XVMmwSZWCinW6y4sLpEw/RMt3MgYfmWrcBxlxHxgqu3m/kR96lketzmbo/hU7OROQf0lbNMVDkMiErV87W0PuqBdA78xIzYaL5hdtk+SK4cn4r8NZiKxlYUOoAZJHyyMW0Fy/Ire5wRetlZBO6fjsaGkzoxZampXtjcvJy5i/Q0djjVTlrWYxXrdDibRbIZz2aOqTOCK5uSsViMzdlMtZmZvl/pkVIs5f15747nfGhFy9F0aaQe6eVOP5ES56Ie9pkRhq2fpmrRlEfDyKzqOuNZjYec22s+hmKtP1GsyzRaumCZerWVWU2Bg31tpVOHXLkSe0jEM5M5qaFu5uPcV7O1yQtYGRiXlNxGLgn7rH5WO56W6IJaWVmKr1Fu3cX+1Cg4TR+p8uQyP7H49SwEE0qIwVHeS5FzJlY1bGcND87+hr2m0nHCHjpBBmu/5urORnUx0fWNOfc2i1O3TWF6OUdd6VCZp+0rpTDS/JBwzkJjsIip2R25whhVUmKSUEOsC70zpNeFSR4zDTsVxTY7pb2+C8ZjnDiD8ZrTJNVbUWsOi1aBDzhCikrFmlJjYMcxZQQmKCcynYE68o4lubs0DVqprO7o9R5WpeY2uW7OxGjPegK103Z4g9obgdgxa2PjW7Ok21wuK3IE648KF5wid71y2vCSkbVJ4133yxjHpKQG4iHnRZXcF4KZClSsrrGtEtU1cBKi2FBpM9dJoYsLbLXuARtKOeQQcIqqpdnnYmDYIdevj3GcmW16jH39ki6mk8tFXVeOWa4309DYqlN2m7Fqb22PZaIv5Vic6Yq1qHbFeCEkva8DTuFc5SgV6RYs6cbwC7ThVpEnXUTTxnar06xW+tVuQjQircPJ3Y6cVvdW3YmIGXtuoOtDHWuEdTUAyYpTwk0wh11Cb7YC6qjrYLmVF1xhWttmt3CO9PjoxmeZ2pEL/brJmwVKp/V2XwnJxKvC5Kpw4SYdK6ozA+FkItZRTW1H+dRyzqsrznIx8MWVdlxciMkYLTbEcjOR576tnDC2QmV5dcKW63VPYMYJC7NFnW3aYLu6etRitS9xWN8+kGdbOMqfJ/a4jKPxZXlZeHoXzX19T2PX2Fjs/A2OVQs70D2mjUyxcjd4ttiPZeVapw1dWsvanqDdvhp3pn9YlszMpqm9uqzZSl+t2BoTpxRGB7YQwmZG1L2mmZHs1eG66NUjjUtciMaxveXkdK1VUnoMRlUI0ydZ7CKpF8A633dNIqgHNmSisb80kmXD7EYOQbI8T9rWYXzu7JMWRphS59d0stAccjFbbuNTUHld7xbjAy8eQDdrPYM7NIVu9N6kAWbnUN2cLlH2qKJ8Aa728nTiI8JJSMyp1h7b2/hq1kZHQCn+NN3LxiT2QISO16S/oRXyZLlnt2SZXY3GpzocBZ2p2jVuime1OCewO4HJUQo3u3R6aTAyKq08qE/s9sJzwX6r6J2B4Z60t32vulQjSZgdCGFq7rN5x7dzCANdeaKxi4+Gv5kz64jvLx4ZzkGrVxxFciFTSjPaN+gLJKrSDZRcny+uDg9In87353xOYrNRwKRabe5EbJW7/EgOrfM86C/yFaW3E5ov6Lq5Hojt8Wzn3Tphr43gH8CFJWSMqMdyMLNSdGrKaGJwZzaACA6Vp+0OW/qk7jbsuRt3LjhO9hIdXwDZmNmRPCxYy3AwkTRzs4mC5SLGLdYcC4baNz533PMU3VL1mWsWTS1OwqnUCePS92WKm4749ZI5B8F5stph7OmgcwY+xslgzGu9aZ5XS8YUqbHiS5F8jbbiWVDcTbLnQ3sqYsWIaw+LEU+HbaSNZuHcnx1HArgY6QqwXM5rx2jtWMFe3keozYYyexXyqTkjPKJvzH1l43UrRWK6xsGxYOgFr8zcLb6gPTyX5GlxWZZS7Baqftjb46t7IGyjJCfWrh4ZqFRK8ngWoEw64Zh4t6KDwluTmIGbljlFPYFJa2e/11IyNGy835Ut2/m6VB53o9aJHZUB8dbmR6RzHMPZodfG5m5EWJZx3fOAmImspNjsCASR5zEZnpN5sFWkeU/R+sy6rFLLaC720RkxKQXoy9m4Oo1PyAdJrv3LFg92BO6SC6lermQ2d896na3Pu8tW75fy+iBg63xiwsLE1qM2C8iWrqKwmM9k9bLDLTNO6zhPqXbtePG83MvzNlhS0w3P8jNzLxzpMz8Lc8Lw8Gsk4vzBC2TW32BHgVAYDQa9ulhjs5iAHW8pcMohtMN8akAnN9tJK1kzdjd32SVkL00475MDk6sWM5FXDJhmxgqdjhJtdaWn62MkncggkWq5Xsk0RS956ZLhIS2QE927youR27npFq2iI6ras80S7WltKgbj6RjteIA7JG/nuBuJ7j66LE4ktYSD9sWPoisaMbMxOaIayW3Zi4ydAxHfVTuuGKGu5uhzvBIXzaltjHzvHBTcOJDSBKVmtHFSLCe6Ep7U+eISPr3gIXSGyc5Ub7JvcHA+O3kUKvtdYo1PFyNo2LWsdR58olSYBEejlqZ23gqTmS7mo4VDH2qH5y9nDFAulWbXale3pLdCGb0pJ1YNm/Lh0tDqGejsWdxFq5k/FWmTUkJ0yrldNTFzxb7EmNpeBOoa4krVjBbjsSDODqsAz/2Oo0apeGH3M/cSa8vlhJhnqD3F0uQ8pbrDTKdVidszgVcZ4QxWWjwmnCw8zNRkd6JGcpaDTlcWShfnYNL7c4bIVzDUo7NENAwxuUwcxsTQ+QqvpwQrR7g9ZXf9uNwrUXkaCVvcI5q5pPku1vQHw3fps60yLXNatFgEOiUtK2VsH+kdr89hQU/ledye9gmcE4Mtz7KiOV9OzUO4ue5mmbIyRiVDbp28nNgpm3FmXLiSl/G2MhGx2t5t6wXPeXYgoWBLuyxOo/RMPG55UgvPTX2lMFlTmeASzMYZGTJuIhu4K+s5v9NmW3e8nRuYE88OeHuORdbhKZvsy4ZHW/uKbynbWlw73uk9btooQOfmGcX3q7DsR+NuxUxUweAT03MCJg+t3Zwij/O6pmNlXIvpZMQXOEbRVtytNizLPj0/3X4HfXpFJxhBPj8Nx+6Pw/N/fsQaXuPy7bEfp/DJ89P/3qng/YTu/Qe02zk2cPzXm/bXfwbtt+enyoshjPtRbJ224eP47x/OOL/8+WnrsKe//1A7/KZ3ad5/V2ic8HYEHOd+WzdV/1YXaXs7AIaObOvhP2XUAyIPvj/dDMjK4aj9rmY4lS6gNSWEXrxlTpWA4VqcD79TAT92GvD4Gj5OyJ+f/B6GI/bqN5wi30BVDrY9fr0ZjkKHn2+e/vj/OMcp4UomAAA= -->
