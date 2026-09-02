---
name: "rar-cowork-cookbook-audit-manage-and-implement-encryption"
description: "Audits manage and implement encryption records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_manage_and_implement_encryption", "rar_sha256": "6e544ebae7531d73140b606e63e4da68ab79e3382434ce9221eda85e945fbba2", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_manage_and_implement_encryption_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-manage-and-implement-encryption:80823b1d8e7d82583f7ec28a36f6e8f4af5a2d7d0780074355b726b7f3c7ab80", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_manage_and_implement_encryption`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_manage_and_implement_encryption_agent.py` is
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

Manage and implement encryption Completeness Audit — Audits manage and implement encryption records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-manage-and-implement-encryption
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_manage_and_implement_encryption_agent.py` and embedded as the fenced Python below (sha256 6e544ebae7531d73…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_manage_and_implement_encryption_agent.py` first:

```bash
python3 audit_manage_and_implement_encryption_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_manage_and_implement_encryption_agent.py   # or on stdin
python3 audit_manage_and_implement_encryption_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage and implement encryption Completeness Audit — Audits manage and implement encryption records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-manage-and-implement-encryption
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_manage_and_implement_encryption',
    "version": '2.0.0',
    "display_name": 'Manage and implement encryption Completeness Audit',
    "description": 'Audits manage and implement encryption records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-manage-and-implement-encryption',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-manage-and-implement-encryption',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9ce67394e458c4c8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-03', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-access-and-security/manage-and-implement-encryption'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/audit-manage-and-implement-encryption', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.556, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:audit', 'word:against', 'word:audit', 'word:compliance'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class AuditManageAndImplementEncryption(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditManageAndImplementEncryption'
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
    print(AuditManageAndImplementEncryption().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/716eZOjVrbnV9Hk+8P2U1ayb9nREYMQkhCgBdACLkea5bKIfRMgP3/3uUiZWeXX7tftiYlRRaUkuPfs53fO4eq3J7ttwrx6en3SgZ1NlnaSRCGoJnbmTYS8y6sYvuWxA/9P3Dxrqshpm7yqn56fPFC7VVQ0UZ7B7XzrRU09Se3MDsB9e5QWCUhB1kxA5lbDfeGkAm5eefXEzytIb1zRgAzU9X1HkSeROzyuR3bmQjqBHWV1M6naBHxx7Bp4EzcEbly/QAFAb48E6qfXn395fhrZPb3+9uQmdl1/CKTexeEzT/oQRvyUBVJI7CyAS4sB2mD8XoAKCpbCSx7wJ+/ffqxB4j9P/vM/486ugvqn16/Z5P319Wn8p7XZpAnBpMntuhkltAvbiZKoGV4mfNLZQw3Vbtoqg1pOamjCLHh57PxGKS8mfx/v/fhg8hKA5sevTzkUwR5l/fr00wRa7OtT1Y6fX0YqxY8/vSR5B6off/pGp26dC3CbkRiU+uXt/fs7Wbjw29LIv3P9O6T6cKUDvj59p9z4esg96gl3Pr1c8ij78UG4qPIryEYn/fjTPyN7d1US1c2/RffnB+EQ2B7U6V3wn57vRv5lMn1X6JPmP2dbQLf+FU3g8g92z5N3Q/0z2nf7/zfSSQQj+NPif0ruzzZM/z75+Z/q9j9teJ74X5/mIImuMDqcBLxOfnvTd6Lw8w/et4s//PI7JP0vyeh5W7l3Cm8wdSMf1M3b288/1PfLP/zy8w9tAWMN2OlbWyV/RvPP7Hrn8wcLvq/68Y97If9DFmd5l00+I33yW178r+r3l8nRTiLv2/X6dfJ9voyv6WRU4oPpwwTf5UwNZf3Ojj89/Q5BAoJJ1br32zDL/+M/JmrkVnmd+81Ed/N2RJqsiVIwCm+EUT0x3pP6V12WFOUl9X6dwKtjukOIsNukmSwrO0omMB9Gj48a5P7k1//t3sHzi/sOnog9wtHbAx7fINi9fcLj2zd4/PVlYoSQd15FQZTZyUTjdzsIgiOIQq4P6GvTL9eRMRQqegCPJkgj6NQQJP82+fXf4vR2J/pSDKM6XzPoHwi0kGID0iKv7CpKhok94pUzNOALRFqIKVWeJI7txpPxT1u8jDY6hSB7t5wL6wfogds2YJLkLpTejyA6P0Pn13lyhfg42rOOoySZeBEsBLCODHfchzZ/HYn9+uuvEOPDr9kDkInJo8DUCFzwKfDky5eiAn4SBWHzNQNumE9++O33Hyb/Nfmfdt2Jjzx2sDrcjQaDOpms9e1mAjO0Hc1TT8bwgPBz9+Bvvz+8MUqXwYoI8yryI3DfDKl9C4dRg4eLPvwDdR5FBNU7pz/abdKF0C6TCNbFHuZ6/fw1G0nkcGnVRTX4MOJj88P0Hw5/8Bl9Ur/bEPrJr/L0vvYeiaMzxxr7MpH8yaeloLrQr83o0TCHBdUDBcg8GA8D3Gk331yY5c2khvlT+8PzpK2hqiPlX53qXohBCkHKbn6dqMIO1rs8gX9GA93Zw915Fo2Of4/Yx2VIpPoBxtjsg8TLZAOgNSeFXdlFWMGqfl/n24+IgHXuYz8kbk8y0H3rJe6ZfY889V90GsL33cW9GZh8bXEUIyf/v1uVUVp+udTEJW+I84m4MTTzEVpjRzVyfTRhsGG4M7vnybcm4gNvPpD4a5ZE0B3V8LfHSv8eTY81D3RrK8hc47U7/TGvqzvdqIExMTq5qsY4tr9mH5D/DM0MPVKPasPUjUcgyD8Zjnc/JA1hfo7fv5X/dzuNVoGBPClaB1pm4gPg3WO+Casxo95NDwMEjNkFU8AN/6AVtHwDnQ/pT6AQo39gWbibbgMzA7ZMjzD/XB6NTRWUwmtdKC1MHfAyOY2RDKOxnjgAdkbjGmiFH+6kJimANoYiflq4Du3iIczY5b4LaEOq1whG3Hf2f78FY3KsLJDbZ8JBmrZnN9CSHXQBzKf+4ddPKd89BYmmY3TcN/3R2e+aTr6vTH8bkw5K+A34YVs+FvXvTAORukofsQjLbVzDtE7Be/jAOLjX75dHCX7U+E9ZXv+hsf/xr/X+96J6+KPfXidh0xT1K4I8Ct9H3XuBGYLACIkKUD9q4JdH3n2BXL585t2Xb3n3B+IPW71O/pqAfyDxHtevE+wFfUHHW0rkgjFw31/QHsKXmfmFHO9+zTTwzdGQfZ5CyBntP0DY/SwtH0tgfQkqEIyLH6WmHitUB4viHeHupeIzGN4TBQJoFox1sc6/S+A7DEHXPjz3icTwVjZivDf2dQEYx55kFL8GT69ZmyTPT5mdgn9z3BkBF4YsNMg4KMHkga1SE4H7N6gYvBHZ4+c/Tnbb+wc7eYR23UBJ7eoOEO+p8o58z2OfnEFwGWeSsapk37dJo+TNUIyiPkagsR377NX+kes9lyEPL38dUxpWVNhXP08+W+TnycfQch8FsxZObT+P7fmoJ1wK3z7Xfg6rDnj65U/EeO/W/4kQ0QgnIwA91AXeN6y4e66wGwiJB02BIuXuvZMYa1g93GvdP6oNGVagbGH19kaRv9ngm2j5Q57f76o0j5H0t6cPtBk/P1qJR8zBDX+t5xtt81Gr30bq9kjj3pndTXV32JsNY2Osyd/dCsYG4+0Rx0+vEK/A8xPcPMZNEt3uk/jTQySoy7eOGFKAyPOlHnsMBKYhpAQrfzHqEUPU/I7BeDny7uvHD69/3kb/Kwh5ZVEWJxzMYwHjsTjFEj4DXJy1CdqnAeuTtk/ZuMd4KMOiKEMSFOUwOO0wPuEytsOOAtYwelL7XRIEG30Bdfg0+P9df//0IAIrD07RkAoNKJIEjg0YisA8hsBI1KFRGtAEID2bZm2H4QBBsDhJkC7gcBwDns1SgCMp33FsfKT33lw+JHv7aOQ/vPOAkzeIwmk0yo3btsu6DEZ6HGPTLiBQh3ABho/cAUpxhM+ygIT7P7e+e2h04EP5MYBhXwm7uuvI57d3j49BSZNw5YqsJf7xEhDuaNOE4vTheXqjfTO/sPlaN/Lz5qofdSDnpQ50b1CZuW0cjEsuJpG8JEW+DhrTupzs4bCLBV+NEZexzl4v4cTK8CITrG25a3F/xxn1WZXKaDiCIZ578iBIBhylE7sE8qkMoo3fllh6CJW4oE9lI5z06zZFb2eydX2fkP1qE3Gko2n2KR7km52Ip9QXCzwfkiEDiOcOg7TItLYQsFpBp1p5LayTpSteeTVOfbFbTzXPPy+wqeszLHvZ9FPfoDAHNvAKddwubgdP9mo6xQpPIbJyWjZNJB+T463K1kxY9aWTstVJqzNvvfEqiSWmtdfCEIjlEyOEOrguya1dsUOdzin7YDoyfalPxjLXN+g+HwxBmBJR6NzI/UGh9H69WsOGyCXPlt94zt6ebnq5pU+IjG2nB/6gMGfYgRaw9Djb5aHWluWpa1Ds2s343CqZLheGs3xxLg6d7ZmYh10iiwObr7v9yiyYrsyZZbyemrlTG6sEThKqbhICckyNoJ42apSfCLyDTQremSUxsDmD73ddIfYSM/OwNMbs3ovqqkeTwiliTDDza6NUFU0NgGDnptbYZJjEQRYvVKuST/Html/Vy0HH/VVyaa7LcO7GOtKl9qK/ngdhJ53UmX12+n6XzhVSWjm7hsWG1vSs7Ypen6zWdRXOX1Ta2XFLwDbsvLVOG31moWvW7JAm72pxL9W0eLSIkumzW0gV6T681vxx2RSXqFUba0lfMBTzllktpxnrn9K8aLKjh4NjFPvKDFtPFXFfK1Np2yYLTBKqJRUxPKUUKSEazlUq+x1OJ4Xs0durQS4YdqOwR4aVV7SY6BxW1uEKMZCcTJUp7fi3OSOS7VH2AAyo1tpi64q49uf86iwL9Og1C3ytSGnfXpw0vEFLD65zWsm4aiWUtF6XKJRjJjWMTB7O5hJHjCiRxeUiOywDeqnk5bDoj2uNnBZqwHWb+Sye4YO1FiMJ1V3datfTvbgWF0Xbx81M1+LjAbMI8xTPI7v1jwITaqeCYkmSHeae1S/EFGgzqYurw0m/RWvDYM9VHEScweXq7bZpSuzWxsRcwbtNp6MxpfiNgzTT/WoTdk7sutc1cQn9LXZVRNI30MVqrnXBGYsGpu/L0DC8k4rVlsvXR4UtUp9s5aacRrq3u/IhPk2EE6uRh8Jbn5yVgZpSK2+pY5E1CIHPtZhF8FrabB3oo75nkyExjAS4Ze/TDtr266qhraSt/WUcdwmnwUmt6xqOyhPziOUElTcL8ZRdl0KxaDGtrA+mzEnxYZUDf7/eAlFIm1MRkTfJQXBuqhQbsVqRBcsGum1qi90BEfe4NE9US537qtMwwuWW0qLQApynUVEc5pcloEXV3LC3xFmUenILiY1n724XkUcDQsOY7Xa17xC1JcLBaITlhiKRDYnb3qlpfXpd2EYplyALryFvShxL1ZXab08YO7ccfN6dufXcujrtxVU6xcx7A/i7hRP4F21LVCR7JHc7Ahq4mtWZZQrSjLMMcm2smjze9+UydlMJZXhnL5eptMoWV8VNBOQWk/GanZYEv9ZuB9tKe464YdQqU49HRcKs247CTxpD+d2W0/T1XuI982pJR2c6A3tpsJD1sClmvLmPG1K/zlKAOi7VskxU7Q+SFZzkZH0+ZbUnB3LUVjvtwBjXnWDu9Xw5D/sYnGRebNG6lgWUIhcOKsQnZ5co4rzu051JpusAdw+0wrlKnJ17ytoqA+3vlDyOozLT7TqiEXaaizlmX6NBcTOPJ80wiz1BqefIlKjX3CorlytXEuGg4h+u5351Y0iU9MuORKbpijaRRmSiC3to7IuyxpATM1vzMoi0LsxcX6BuZRdU3Mm+oIN95bhdIjnzVExifLvohCq69LtzhZBIfEFWPb8lrI3hWhtdkgC+r8JylTD8VqW6Vbg1t0OXpTyino4WPqRJtGdKijhQc0xA6BZPLjulrPa1fznbu9DD3CLTlya3LRtZHFxkmYIF3uNutosLPoNjB9hc1xXnMFGwrYajdvUgbBD+dp+HDLvfHOa7fYHgx9alhHOHGBBO3Iuf+MI2PWxSmzvPKTU5UQdsseeuZ+64UpqbVK40TYoT/maVrV1rxYAQF3OnIqItFhU5jRaISKLHcnc5pOf11NB7thAWYZvfaHEnhZt9mWen8qBcGqbit+X6lCPJ2olcHKth6oQxTbdTe6FZMcergeqG5kCGlTjTqzyolVlJn6WL35KSueDPrdHusdt+IfAXa8vtMVGfXtiZttME2pEajAZ5JIltWqKXuERTF3MWkazp0WzRri2hiGSrohAWIVLCcVR6X663qrnIQuXMH/eBhxDZKc46iT3ay2xfWSvxqnJeT26QbYCX0lmpsMGpjgvKM894Zp9SquS1LXqd56fS16hU7FJJqeK6G/Brcrliunc4Fna6KBA9Jza0mqy6is5PZ3qZ3WYn+lZzyn5LJyoIl+laumkrL8DB+lhczEjXeKHczHaVmhPqbD4g9G3BcZtWQfCLAjN3P092144846zWYdeTHZPJLatyUV+IC5yxi3zKGKW3xxdu4VP6Db0dkV2GNDMebBQsDBZu7NLWhlO7S7xc+XKNdTCGbxd6OOEWAzxCYKyIzILhXLkr31nzWdf5+zOBN+s6F/h1WfOzCKYWwHG6SuTdjAtnVgok001VVrcozj8ns8ybHZahxvD2zOVQZkanBTPrc6mb48dUSxPsqBnnwnFnZJBlTKyegwsmhjNe7abbc1z26P4gGwe1ESRUthsXoHW6cU/hDESr1pNWUdLA0gjRkj13AbXciYKXr4NcsK1g6ZzlY+eT+lw7YhsFpOr2eDEa6WzyhH8gZtcS5zJxiUq8cc0yd86VxkJQpBWYmVxwQsuZ1ayUa4Cg24bZ5VHg9vXSmIcmVQWosKpnW8K56Uem1G8aslitCEzVj6sEW0l6U/DpjdwJQI0EdZHh1F5nb+RG0C1Yj+eXwwxlTv3BRrLtIqpYOVAHt7kcE/di0uRwuq7JKnU7G12fXBQN9xvv5Bj4en3salbdkFye6XgW31J3Q0g3R9aTHcLalAbMVl0KiFRslz2WTPut6nRFtl+i+8C8DtspAScBaZDB2tmr2SZNkTOMqUaj/FQv2lSXuaWb+kQdKbWm58GN9UGl4H5cdRhR7YMsobXLcHG6eRtsGxfG2kAUF6aZlTjCV5QK0jNiWakonhkHZVYWMsdsRis8LKjqkkGGvc/jnONjB1S+zoB1JPVgLgr9Ydid5bPQtXC8nIYWP1/jabpQpqbvUeogJ3URrCuh7yI+M3RRQ+dJF/gGJybd6uJKKnMGnbCJ3GPCa+a+2GdLc1sWrnxx+QOx0Lszlnat1eGzJFDsRi5kYNnsXEHW+lJO4+th5Ut7HmPq/fzoGHxhLmqLDkgq3vErcz3oEVPHN96h5aKiuMuW3CqzCGulOU1v3GBqKvquF6gcnStzV2TreLO6bb1tCOhc1cNNdzkGPAR/jV8I86pzFlcQGKsKk/ZmEA/9dKNfeEZeIwqJTuWzdpnPwmZj53hxcm6ytcQsXTwbR8VfmCh7Ps222TYts8x0hJlLOOtpT4aKiWWYGK3SbT5UoizPVpVtNEkXkjEk1hUCLk4Jvp52Rbw1nSW/pMQpJw1t3VYzGZ0FhRPawnEq2HPBpVXJl7GSDskBQNOhKZUsteVt8BZcahwWPWiqc6JboPL38jZvg5KX+MjoSgpbHNbqEnYOWpSgVLhyD8Dw9SnF9TuGkwjWgMPMcM2IgIRBtVvbdLUL2TQwMYo9nwP2fJxujWC6cujl7Oqch62p+a3V9kGwkdsDWqboyVhrOQU733bPTJegsWp/7s4ZvymZqcOqVLk4uOuDSBJLB5iUdzOjXcRA5+nsyUp0kkS4Zhco6hS/idTs3DFbYsD65bLNtVu2xvyYFLbELuz6eThl1n5vy9wR3QQKiFx/G3NtvSPizYyCZt7ZuQV8IxscdrfZ7abSyoPCx5yDTK0rSYPlbEPlVyRFrqiqWKuI2htnvOIaPckO2lQhq7k+c48ettVoJCPFfp0tc9Se5f7BQrQIlmXtwqy4maDtBqfXvFlp7OzWQFmxh52Df57R5lJJI9U8OpnZgXk+a8vBCHD1mmwB2/fIbHNR4qOZmgbixLD9Q8+0516yBcvBSImnaI1eM9cID6o6teuVxvM+mAY3infZipPQJLjJ5HzTX40y9c9g1g2sU1nWxfOWeH3baXgb7l1CR5Swwq7MaScOm+XMtEuq021ez/QZziGRyKzabMcAPI/oWWIzZjS4WV7snSoaln3D2Di7TfQS7z2V3CYb0MpkdthQhEBcySLPyZqWjWF6Sc7h+bxkIwmQoai1azxKdublSPX+8rpHapmPfVydE5w4Tj25yp33aEIKsF2Lq604ZSGgoHO81pidKRaxxytbGxZUWBuFdb9SGzSdFqW8OCAlo1xT1N4RBIlc8BUeUMp6GRlWeQNpv9iImpniDVLmfIRCG6l2211vBD/kcUGIPYl4vjZ1i/nBITWrqqpVi7e9WbkWR+9swIkrlcm5U8lQRlPSwryr09iVuZAHio/K3ZY4HwZMzThyM6BnODmQxcAulwQssLeTEfvyMrx2CeaJObmFAKQwYiDuDoXd9E4Jq2ykaLW3ba80u/NmFW66tUdXxSwv5oohqZxrZXPRP/Ood12QUxLshYCWyunxsLpi83ZN7sUDbEgJ2IxsT5GcFZRKzNQyLAtmv+w9P1Rqh2nFnbsl2qOWi7tbgCPzSqgvxMlnVxie7cKysyJqhrRTsNJU4GpXw4kw9MBaWjM94X5HNyUnENK8qT032TPN6krIDsmIJlEgAZeRygpTNDXAyJzsZh7NF9x+aCKVRihcyzEKiyActsBKL5thF3GcmpqmEFO3A8UeCeKSSNFm729iqu9pu6aQ2Jt7rXtKA5sWgI7N6qWYHrET76N2Gp7nNI/QYilsZbAsjq4dLqWS2jT7s2SxOMmBtiXrzWpdbfQCTipn4gxWF2y2qkl/XhzO68bIAuMKtkceF2Yqub8uuFx0kQ7Wp+NU8jgXk25yaqtwnl6t0Mza08eFXNG9famrIQ2LTCSI0/y4Z8gttzvtxbbkPN1dIMEpp/vBPFfe6iC59PVsU/OCI4xkQw1q5yxJZR96p5w9cvgZg9VHoEN2wLCMIARqlW42uxlDLum5tSpRyjeXcmSbltCJlG/DwVUXQ28txcQyY0Nqa2x4ijG2koYC7mQJNGNAFJvJ7XxnhBDLef7vT89P98Plp1cMZRj6+Wl8wv1+wvCXnzEHt6h4eydHMCz7/PT/7sHn4yHkxxnk/dE/sL3XO/fXvyjpL89PlRtBqR6PpuukDd4feP63h7xf/q2nzyOJ4XFUPh6a9s3HSU1jB/cn5FHmtXVTDW91nrTvO5y2Hn80U4+/q3Lh+9NdvbQYzy7uXMd3L42yCFKu3pr87XFuAJ7GH7WMZ4HAi759Dd6PFJ6fvAG6L3LrN4Km3kBVjNq+H4mNj4PHM7Gn3/8PGZRgNAcoAAA= -->
