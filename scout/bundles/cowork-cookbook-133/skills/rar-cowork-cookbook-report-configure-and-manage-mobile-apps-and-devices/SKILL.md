---
name: "rar-cowork-cookbook-report-configure-and-manage-mobile-apps-and-devices"
description: "Builds a structured summary report of configure and manage mobile apps and devices activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_configure_and_manage_mobile_apps_and_devices", "rar_sha256": "e4cdb7a2e91aa33dbf40b6393785bb6e5e9c8b13f099c5bf55e3b1bd4a690e89", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_configure_and_manage_mobile_apps_and_devices_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-configure-and-manage-mobile-apps-and-devices:c7804bf8e007760fecb080bb130a5b00536cb9847a12bd1dd015a663d8f66074", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_configure_and_manage_mobile_apps_and_devices`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_configure_and_manage_mobile_apps_and_devices_agent.py` is
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

Configure and manage mobile apps and devices Summary Report — Builds a structured summary report of configure and manage mobile apps and devices activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-configure-and-manage-mobile-apps-and-devices
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_configure_and_manage_mobile_apps_and_devices_agent.py` and embedded as the fenced Python below (sha256 e4cdb7a2e91aa33d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_configure_and_manage_mobile_apps_and_devices_agent.py` first:

```bash
python3 report_configure_and_manage_mobile_apps_and_devices_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_configure_and_manage_mobile_apps_and_devices_agent.py   # or on stdin
python3 report_configure_and_manage_mobile_apps_and_devices_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and manage mobile apps and devices Summary Report — Builds a structured summary report of configure and manage mobile apps and devices activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-configure-and-manage-mobile-apps-and-devices
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_configure_and_manage_mobile_apps_and_devices',
    "version": '2.0.0',
    "display_name": 'Configure and manage mobile apps and devices Summary Report',
    "description": 'Builds a structured summary report of configure and manage mobile apps and devices activity with totals, trends, and breakdowns.',
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
        "upstream_slug": 'report-configure-and-manage-mobile-apps-and-devices',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-configure-and-manage-mobile-apps-and-devices',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd5f917aad3b3fbda',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-manage-mobile-apps-and-devices'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/report-configure-and-manage-mobile-apps-and-devices', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportConfigureAndManageMobileAppsAndDevices(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportConfigureAndManageMobileAppsAndDevices'
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
    print(ReportConfigureAndManageMobileAppsAndDevices().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6aZPiRpfuX9HUfLA9dLf2hX7DEVeAEGgF7eB2VGtJCaEVLQjw+L9PCqjq9ow993reibh0dJVIZZ79POccqX578fvuUDUvn19M4JeI6Od5egAN4pcRMq+GqsngryoL4H8krMquSYO+q5r25cNLBNqwSesurUp4fNanedQiPtJ2TR92fQMipO2Lwm+uSAPqqumQKh5JxGkCb94ZFH7pJwApqiDN4Updt/flCJzTEMDrsEvPaXdFhrQ7IF3V+Xn7AekaUEbw97gzaICfRdVQtp+gQODiF3UO2pfPv/z64SWF1y+ff3sJc7+FSy/GXYj5mwB8Gal39uqdOw+Zw6XFgzUklvtlAk/VV2ieEn6vQRNXTQGXIhAjz28/tiCPPyD/9m/Z4DdJ+9PnLyXy/Hx5Gf8ZfYl0BwCF99sOWiT0ax+yg0p9Qvh88K8tNA40Vvm0XFomnx4nv1GqauTn8d6PDyafEtD9+OWlgiL4o+2/vPyEVA3k1/Tj9aeRSv3jT5/yagDNjz99o9P2wRGE3UgMSv3p9fn9SRZu/LY1je9cf4ZUH14OwJeX75QbPw+5Rz3hyZdPxyotf3wQrpvqDEq/DMGPP/0V2fAAwixP2+7/ie4vD8IH4EdQp6fgP324G/lXZPJU6J3mX7OtoVv/jiZw+xu7D8jTUH9F+27//0Q6T0sYyG8W/1Nyf3Zg8jPyy1/q9t8d+IDEX14WIE/PMDqCHHxGfns1N8L8lx+ib4s//Po7JP1/JWNWfRPeKbzCRE1j0Havr7/80N6Xf/j1lx/6GsYa8IvXvsn/jOaf2fXO5w8WfO768Y9nIX+7zEqY2sh7pCO/VfW/NL9/Qhw/T6Nv6+1n5Pt8GT8TZFTijenDBN/lTAtl/c6OP738DvGifCDXeBtm+b/+K6KmYVO1VdwhZlj1HQId3KUFGIW3DmmLWM+k/mrKa0X5VERfEbg6pjuECL/PO0Rs/DRHYD6MHh81gBD49f+Ed1z9GD5xFX3A4+s7Nr5CaHt9YOPrAxtfR2y8Lz+x8esnxDpASaomTdLSzxGD32wQeKDsRhnu0QLR9+N5FAOKmD5gyJivRwhq+xz8A/n6P+D7emfxqb6Oqn4poe986NAI6UABaflNml8Rf8Sy4NqBjxCQId40VZ4Hfpgh44++/jTazz2A8mnVEJYdcAFh3wEkr0KoSww5Q4BvQFvlZ4ido63bLM1zJEobaMgKlpQR/aE/Po/Evn79Gvjt4Uv5AGsSedSlFoUb3gVGPn6sGxDnaXLovpQgPFTID7/9/gPy78h/d+pOfOSxgUXkbkIY8DkimbqGwOztC7itRcbQgdB09+5vvz98M0pXwkIKcy6NU3A/DKl9C5VRg4fD3rwFdR5FBM2T0x/thgyHsUqmHbQWxIH2w5dyJFHBrc2QtuDNiI/DD9O/uf/BZ/RJ+7Qh9FPcVMV97z1KR2eGVRN9QtYx8m6pZ+kePXqo2g4Gdg2rLyjDKzzpd99cWFYd0sLcauPrB6Rvoaoj5a8BJD0ap4AA5ndfEXW+gbWwyuGP0UB39vB0Vaaj45/x+1iGRJofYIzN3kh8QjQArYnUfuPXh8ZvwX1f7D8iAtbAt/OQuI+UYEDGHgCMPrpn/T3y5n+nAzGfDcyjd0C+9ASGU8j/71ZnVIMXRUMQeUtYIIJmGbtHzI0d2miCR1M30oNdyiOBvnUebyD1Bt9fyjyFfmqu/3jsjO9h9tjznYYGb9zpjwnf3OmmHQyW0ftNMwa4/6V8qxNQ5DHw2xHyYE5nI0JU7wzHu2+SHmDijt+/9QzIIw5HpWGEI3Uf5GmIxABE92ToDs2Yak9XwMgBo7FhboSHP2iFQOrQH5A+AoVIYQhD291Np8GUgX3WI/7ft6djJwaliPoQSgtzCnxC3DHEYZi2SABgOzXugVb44U4KKQC0MRTx3cLtwa8fwoxd81NA/+mL7+3/vAWDdSxHkNt7JkKafuR30JIDdAFMtMvDr+9SPj0FRS3GrLgf+qOzn5oi35ezf4zZCCX8Vh9gmz92At+ZBkJ4UzyCEtborIX5XoBn+MA4uBf9T4+6/WgM3mX5/F8GhR//3ixxr8T2H/32GTl0Xd1+RtFHtXwrlp/CqoAFM0xr0D4L58f3TPsIOX18ZNrHR6Z9HDPtvvzMtD+weljuM/L3xP0DiWeUf0bwT9gnbLylQDZjGD8/0Drzj7PdR2q8+6U0wDe3Q/ZVAZFp9MYVovN7BXrbAstQ0oBk3PyoSO1YyAZYO+9AeK8o76HxTBuIs2Uyls+2+i6dR51GRz/8+A7Y8FY5loJobA0TMA5R+Sh+C14+l32ef3gp/QL8/eFphGgYy9A24wQGswo2Xl0K7t/8PkpHA43Xfxwh9fuFn4+JV42FFoJs+o66d2WiBko6ZmoCSyBoPiBQgQQi5qjfMGbr2E0EUN8WAjKIRoW6az1q8BiuxkbvvQv8rxLcEx4iVVR9HvMe1mPYsX9A3pvvD8jbOHSfN8sezoO/jI3/qDPcCn+9732fkAPw8uufiPGcA/5aiCcYPeDfD8ZCO6r4JzpBag049bCwR6M83xT8xrd6MPv9Lmf3mGR/e3nDm/H60WU84gwe+Geaw9EMb0X9deTljxTvLdzdKvfm+NWHITEW7+9uJWMn8vqI5JfPEL/Ahxd4GLZQsOO/3Sf7l4eAULNvbfUort98bMdmBIWJCCnBFqEetcogin7HYFxOo/v+8eLzX/TifwtSPocsh1FBzAEMY1kGi0EYYBwWBDiJ+XSAYTTJhMGUo1gfJ4IIjyIMp32GISMuZhiMpaBcLQybwn/KheKjn6BG78743xgZXh4kYZUiaAbSBFQYBaxPgCnu+yQZBTGFBQw5JVmODgIG0GAaclCHGJtOQzqIaRqQAR5ElM9MMcBNR3rPDvUh5+vbNPDmuQfYQCGLIh21IHw/5EIWp6Ip6zMhILGADAFO4BFLAoyekjHHAQqefz/69N7o3IcpxlCHzSlsDc8jn9+e0TCGL0PBnSuqXfOPzxydOj7rUoF2CaYNEydWia6DE25gxYVsw5qxo+jSJqKvKfObezF7VThr9kxpMI+/lorYadsbto5PQrxfT6e0cpOtvHYPpjIrqG7BlcoV7S4srEwzWxj0o7e3T5PTNin2krs+qmxu7grV1VvX2igxpy9Xnp7vXW9pBkfzSlD5La/T4/J2QyeSwpwiqU7yZpbboZ3P5t58UhTLgvDd9ZnZea4RMkUXBa2rKR1INdlR2b1QzWk7nwjYbUm5pkMV9NUdKLEmOLBaTqa9krFRdgvjgGHjnKy8lHUa43gKJPMq12FByZliY4dr4xLr2qcvKostVhOnWN5ybMlKN/PopIPsb0jbyhkTlNM1TZ5LSd/1UA91mU6dXF4yrrAc7CKhhiEpcbvLTKaqG8c5dGot+hP+1JhTrTUYHS+LrsZRg/Rg457DYcc5zuJgfRIWx9ucI04Gkydtbleu2jBzq55vW769ZvAf1+L+ZXIGYLvNhmGyVfw5r5xXjVRtJO/QhwreS3tXIFjXDJczqrGWyhJb6d384MrBFFyXguu4wXJ7CoqDbh0nBe9Kx53UZfjy6Cq920cbYbkEbXG2CHZ6CssTZ1vzSAlU9ZSp1FY6aPtrJ2iBROVMF9BttNL7YQfJzSiaNichStKtVtFzzCctDLRiuNa0IohrJg8Hmeg2tlmnFaEMS6N0cL+92QHtr1ex5XjC/LizqGqNalWjXuTykNCUH7IeH0+UZNvm6lnlXbHbH9NQrWmdnitMYy43u616Rp3p1FAbtb127KbWdH/ZOpx3KXY3w7pVnlbUJtNJGa5awcK46JYD/7uHUldWmxNg9FtxvIXWSo56h5prjHRgVkdOWombzAf4QpiUk+Gml9lpwhUxFyTM8orf2sDdp5piOewubR2XUI5b4BbldG+sm9xfut0qS1d4MVwGqlV3g5a6q6N04jk9MxrCJeyEF/1bvTe58IDeGnIA+H6f1Qd1bzrEojEEBczdQeOpeSoz5VVbl0LLZnssVReiTxm+OtNmvKfproTV1mEI+3ipBgdDvOAc42D4ySNL1Fjj6DpNLD2eCrcjZ0x2YQzQiXq2L2fXUFg9Koi4pquCia7i1GHRJLCDbHvak1cUQk9wIXrcW5mmceC8EvUY+0S1Tj7RE1Nwbo2sNULW6L1HmevBy7dO5V7aGX2ap7UbU72aK5PcoHiquFiLHYNdgrUg2YV6zFbSQFZHbTaXguY2HU4Lr2Suh12EBbJaxmiW2pk9Kcse37WXuHAlZTbpWz8yJg6WzS/M0U6TySbWpra4ZyHSNHjTycu2XslNn3Mc52s6uEqssDlUIJ7lF7PDKBfTy1293KR1SSWk5WLSxYP1Z5eZRzDUKKVjW6NywHbVTTLPkKa1ZWVqlhuASMzLdc9GWwg+/Y6Kpdkssz1MxHC5sHqfr9aTizZvsHZLT6tS1rZk6oI5pYozdMEFjlhXZKDedlOMSm6OybIQHwdiTzZGS0SF428xzsK25BK3iSu4+oGbRgE3z9FYnrC8f2YEk9WIC3/rNzq7WGS4Mo/6tnXlDVOWolntI6ZkOdNZ7QR+kVOeyoniqb0YEnszjco9zBJmYzhxbIJh7kdcMJP1ZhmeSWqvnvXmersYh10jYTqmqXxjq1mi2SctSbKYUji5oWfr3qi3qrySpPmyXIYzpu58YbZYGNfutM+kicAd02qhOvMZI3WcGZNwiYfHZIdPxEg6JUfdWGnuZLUJORDK21MFgViYU/kOUL5fbqzpZsnke0svWoyZxmXNTM/HtBHC+lSuPJZhTPO4VEDRXtootdrUUpmpYoIVSie8p5CrMCbWu20qbfJ0EsSrmLavAAJTmw8ZlgDZu2yxQh2aAGv1ucnvWCGtFwUBKmxX8bk89fQTZSYi3+IQ1E1Hjgx8EALTT6MwGYzj3pnbtGYqmj6RrrWcFv4Wn1vUYitgUuUMYiUK5lL17chGlxXnTc0iKzQU3eieXN0W2CSKatZXPBoCT5uf4AAAC2zO0NfIygUXN51so3eufJzugnKjw607LSyiKylpW7R1UMfe8n3mGs3e0zNSmpfxUVxReHETPOkoiisjaktlE7iypweNvVJ6VMyajAaD1qf5jBZqE8/6Ni7BZrpoWlToOaOyi3M0KVZ7dTjswZDK+l5eLTPBKhw6SkVvb5BVSfIef5acKt3siBXZOWY+k8KlffG0yJUSEwPFGlNgwjn9PJ+rvI1j5PLiMIa0sI7iYnGqi6bapPTaP0i5P5mcVoxvJ+6c5UnK4hYLSlmltX3I89BplGFC75yFHdbEnFoytuPLWqHtbR/O07tk5oa6GWynqEqeLpqZd+v9YktwkrxTjEUc1OdgtpNdU1/Ok7N86VFif7IIuQomES7vDmG88nPUEr3stvSKwvdrP082WODtCfkiLXqDUY2DSlNKqPc0SkXLdIMdsrJyUKs6SIy6XK8bhbMbTb7W2+zMkvyMu1HV/LbFlbCiqyU3+LTQ2Ha2NWDPJKDc/BTx2Sox7VCzDyihMnl82+b1rKwW/dFji5m1rtjAKHdY2C4tseUdT2OJYb1x8bq0nbIA2NmeAXCEnSXDTYNwe1wkkn3YpNPGis+5tgw3ls8ymn5kyd2uLzznGuytgilY1VszjkEREwqDFVrTxbWg6DQOcOwwV+QDX201Nimomo1k3SjbBS3uRLXbSqFmRJtVwUpb/8QK7ZbPm2Yl2eVNdoAvL2yWYU3fK5jhKJv7sJFW0DKmc3XtdKDJm2bC3gz4RCKHGb3FgkW2bmY8wCSxVkxuWblXTwMO3S6ZNZukYgDyW1rYhr28WKi2Nt3sbK4dfE6EQqUd1DWeDHvLWO9Uv7r6RnBrNhW6kLJrZPe5IZOmp1W5DgRl40YV3onLQ6hdraZllynOYxItFnK90SeOauPhZePJokg5oQHa/VofgkJaq6rjgD1vEb5mOho/V8Kc1Nsu5t0Fb4V6Z3rboWhRtNoH231plrvJYS/QFUB37eEq7HSizEIhg1aenwLBLhOv0rSUXAdFEuSxvmqMHTrMsqxMJybFD7GG0rs5IVndospcIbwkDL7FDNBf56Laa4fdeSelLOyE+psWoyAZ7LlD8hyKN9tIL+LDJItp1Z5NJIIK0oOwNk/pChChKe1CCUrWCr1sAmKg82tH7k5OGxbVFNu69E3D9DUbbCXnnGzOjS6LS1E1svCgbEVsZlZmKitq17OitRM3B13Js+zCbsmFPD/NiuSSDxrl+BXuqaUERGZhBOQ5DfTjwPAWZp0O8WV+EpftRTcHYdFu2Mprh0Nfo9jtmPFhnOeHYILOis6de7R4jaWNSfLydrgspNPqSsi1f9049Q1fVfOAnPl54EJimSbnO2LJ8H0rtIy2W2PtnpFCZivLBwaQEuxS0ttqKwl0VrFbo4/lnjGrcs4Y+mbLxC3olw7sF9UZ2XFw9iF8U26UjUeJmBtrnXAkTsEtD41zvz5GvCSLwSoIB6y1OgJfC7vjcVMV/Gl3ugX98eTS5bGUsjxWa4e65FY1yzj5uKfo1Sow82sEgjWfcofJ8WA7Ku0JhNBmuLeZJ2AdTY+siXelo7iKuzkep0tsszpVhEbiZrGcStN9G2nbeJVfjhFAI+XcL7jJSiYL0tmJyzJQUn2wqVlD3M5wxNrXeC045FUkDSpkQ4bHBhGrgw4w9qogg/TGTWCGee4lUlzbDtYztMQYfJHCNryMiMvUwPsFCpsYSijty24jnE63XezcWELWrDm63pw2/JEFVwuwqDg/o7Q8WZ8aNVxsyT3hTAly7dSHSTg7Em0rLfe3SbjAAJhvUDjXoxQfaFJIrGW25dCLwK149gJnOmLaZzCsjt1uK98uZkHU4QwT4pT1Z4pV6XGoJKA7TWbqGlwGVd6IuDU/zwXr2A18tlFjjF8nk5pOrNnOPk5usFMG3BnDTkTIBillzxOyMNpoYUDMFEltq6Mb2vLOshqvrd2JFhypEONhqk5k3QfHnNeVcnrzLtaZMhabKJqd7fRyPtMbUw7zKU4uY9kTt9O9mKnLa8td3F6b4mUY6PL8OngDoc0iTb9R7nE3JRQ7hr3IxTwzU5RcLOdFpE25QWh5fJktaHqyugx6AOIi4i4CpikkcaCPQugcXHJZaA1LeDV7FjtPO+FkQu8w5kIKt8kkuvTQv8F2LXNLnQSHQL24cRoesnW4C612v6k8f+upBjdtNxeN9GezQaJoRUAhOsj6VT55J6rYn6RrzlMybVvnoQrn4bLji1UZ6kdpM4jXS5nugN4OfQiwxlfLw8JRXUU/MxNwtiqOQxfqahvPZcwruvzWoUV2gUkBKGu/Ugz6BNSVcB1CZsHHh6RpSIyo+nOiznfXOL4U4UWzGA7v4DDUEfEqrOl+3U9LX9evZbFPghuwwqrAw1Qn4Mw3W4LYDw4kbqkRp+G4Ekuei0a90HXzlaA3SWhtBE8k9BXvCuoKLZWTiqfUQmCDCJ1xjjVrNppP0A7fi/MBNlbncJ+JJQeIhpROcFxVGpdeHk4rbXZZzTBie8b25WxTaCG/lG5WflEqyTPYXbblaXdDJdPVfmtuMm61wBLb2muRo4DmnKRBHFBb9pJos967lgdqcVYmBXrbc8SVPfXRlGEakiOUrXejTrQc1fZG48l6OZym4gQ2yChhe3EKJtdIbDBg+x1u9fM+qzV8Nj0PAOV2rUc5C6CRfNAwNpzD+OVZ3Ktby0rkwLndTNdGuWZJno6+sbuKTZMH3ew6gb1IfDj5s91S3k6ahmLgZDwzRG1lyhEbKOfVWcjO+2XAcGTqTVGrNM54wtrrbIJeE55ZReXAo3Aim4nLU1Alt+iWYmtcw88+Ke0d/NxPc4W4kN4q6uaL7UG5gXRyI69Ar4RotWBDmWHquTExO5qj+ZlPbcuUgQVlh+5bOGEUS3DUazGa76EfpGFzlqOCNM/7NdjPcfaGrsGxUdWy8bwsJYdowp14k71NsXogyYm/CFZSDTrqnHQ3Do2CTHfIQLfLFX+bqcFZni8JP505pHSeWryt4AFdnuoV3u+Hjcrsd4vbsPKvoch1BrBFsWC06zKpJxw/OFPMlGCSeqEf31YpJet9NLALvekDbzeNygOho0m8HZpIAdeM5/mff3758HJ/K/zyGYeAOv3wMr4teD7z/yefACe3tH59EicZjvjw8r/36PHxGPDtjeH9GTzwo8937p//Kbl//fDShCmU8fEYuc375PkA8j89gv34P3hSPBK8Pt6Gj68/L93bW5bOT+7PttMSDrxdc31tq7y/P9mG/unb8W9m2vHPqiCN++uVpirq8QXDQwZ44cOuoby/EnntqtfHCwDwMv5Ry/haD0Tpt6/J893Ah5foCj2dhu0rydCvoKlH5Z/vs8anteMLrZff/wN4KLDVIigAAA== -->
