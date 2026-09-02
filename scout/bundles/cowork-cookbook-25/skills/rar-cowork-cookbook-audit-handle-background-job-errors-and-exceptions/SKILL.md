---
name: "rar-cowork-cookbook-audit-handle-background-job-errors-and-exceptions"
description: "Audits handle background job errors and exceptions records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_handle_background_job_errors_and_exceptions", "rar_sha256": "fad47661b487978a231c7ef9baddd321a0007bc8be3fc4932a551c30cc3c3df7", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_handle_background_job_errors_and_exceptions_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-handle-background-job-errors-and-exceptions:e819ad6aa79c19296d62c741165fe6fdee6006c96e1056b7c6177a02e107499b", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_handle_background_job_errors_and_exceptions`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_handle_background_job_errors_and_exceptions_agent.py` is
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

Handle background job errors and exceptions Completeness Audit — Audits handle background job errors and exceptions records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-handle-background-job-errors-and-exceptions
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_handle_background_job_errors_and_exceptions_agent.py` and embedded as the fenced Python below (sha256 fad47661b487978a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_handle_background_job_errors_and_exceptions_agent.py` first:

```bash
python3 audit_handle_background_job_errors_and_exceptions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_handle_background_job_errors_and_exceptions_agent.py   # or on stdin
python3 audit_handle_background_job_errors_and_exceptions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Handle background job errors and exceptions Completeness Audit — Audits handle background job errors and exceptions records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-handle-background-job-errors-and-exceptions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_handle_background_job_errors_and_exceptions',
    "version": '2.0.0',
    "display_name": 'Handle background job errors and exceptions Completeness Audit',
    "description": 'Audits handle background job errors and exceptions records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-handle-background-job-errors-and-exceptions',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-handle-background-job-errors-and-exceptions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a87b058c0d7a9355',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-03', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-background-jobs/handle-background-job-errors-and-exceptions'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/audit-handle-background-job-errors-and-exceptions', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AuditHandleBackgroundJobErrorsAndExceptions(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditHandleBackgroundJobErrorsAndExceptions'
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
    print(AuditHandleBackgroundJobErrorsAndExceptions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6aZOjxpruX9HUfLA9qm6JHeqEIy4gCcQiFgkk4XZUs4PYdyGP//skUlV1e4499/qeG3HlcEtA5pvv+rxPkvXbk921UVE/vTztfTufcXaaxpFfz+zcm7HFUNQJ+CoSB/w/c4u8rWOna4u6eXp+8vzGreOyjYscTKc7L26bWQQmpv7Msd0krIsOSLkUzsyvazDnLtS/uv59TjOrfbeovWYWFDWQnZWp3/q53zzGlUUau+Pjfmznrj+zQzvOm3ZWd6n/ybEb35u5ke8mzWegjH+1JwHN08svvz4/xeD308tvT25qN827cvxdNeZDM6Fw1ne96Nxbf2gFZKV2HoJJ5Qg8k4Pr0q+Bihm45fnB7O3qx8ZPg+fZf/xHMth12Pz08iWfvX2+PE3/6V0+ayN/1hZ200662qXtxGncjp9ndDrY4+SAtquBI+xZAxybh58fM79JKsrZz9OzHx+LfA799scvTwVQwZ6U/fL00wz47stT3U2/P09Syh9/+pwWg1//+NM3OU3nXHy3nYQBrT+/vl2/iQUDvw2Ng/uqPwOpjwA7/pen74ybPg+9JzvBzKfPlyLOf3wILuui9/MpXD/+9Fdi70FL46b9P5L7y0Nw5NsesOlN8Z+e707+dTZ/M+hD5l8vW4Kw/h1LwPD35Z5nb476K9l3//830WkMcvnD438q7s8mzH+e/fKXtv1PE55nwZenlZ/GPcgOJ/VfZr+97tU1+8sP3rebP/z6OxD9vxWzL7ravUt4zew8DvymfX395YfmfvuHX3/5oStBrvl29trV6Z/J/DO/3tf5gwffRv34x7lgfSNP8mLIZx+ZPvutKP+t/v3zzLTT2Pt2v3mZfV8v02c+m4x4X/Thgu9qpgG6fufHn55+B3ABYKXu3Ef9vzz9+7/P5Niti6YI2tneLboJc/I2zvxJ+UMUN7PDW1F/3YtbSfqceV9n4O5U7gAi7C5tZ1xtx+kM1MMU8cmCIph9/V/uHVI/uW+QurAnYHp9gObrN9B8BaD5+gDNV/Ds9Rtofv08O0RAj6KOwzi305lOqyqARj9vJw0egNhln/pJCaBg/AAhnd1OANQA6PzH7OvfXvX1vsDncpzM/JKDuAEoBtJbPyuL2q7jdJzZE445Y+t/AlgMsKYu0nSSfe8FXfl58t0x8vM3j7qg2/hX3+1af5YWLrAkiAF+P4OkaIq0B7g5+blJ4jSdeTFoFaDrjPfOAGLxMgn7+vUr6ALRl/wB1Mjs0Y6aBRjwofDs06ey9oM0DqP2S+67UTH74bfff5j95+x/mnUXPq2hgv5xdyBI9nQm7JXdDFRul4FhzWxKGwBL98j+9vsjMpN2OeifoN7iIPbvk4G0b2kyWfAI13usgM2Tin79ttIf/TYbIuCXWdwCbwEMaJ6/5JOIAgyth7jx3534mPxw/XvwH+tMMWnefAjiFNRFdh97z9ApmFMX/jzbBrMPTwFzQVzbKaJRAVqu55d+7vk5aMhtZLffQpgX7awBddUE4/Osa4Cpk+SvTn1v1X4GwMtuv85kVgV9sEjBP5OD7suD2UUeT4F/y97HbSCk/gHkGPMu4vNs5wNvzkq7tsuoBn3/Pi6wHxkB+t/7fCDcnuX+MJvavz/F6F7x98zj/wYvYb/nInfqMPvSwUsInf3/JDmTFTTH6WuOPqxXs/XuoJ8fKTfxsskDDyoHCMZ9sXv9fCMd7/j0jtxf8jQGYarHfzxGBvcse4x5oGFXg8V1Wr/Ln+q9vsuNW5ArU/Drespv+0v+3iKegftBpJoJ7UBJJxNAFB8LTk/fNY1A3U7X3+jCm58mr4AEn5WdAzwzC3zfu9dCG9VTpb2FASSOP1UdKA03+oNVMyAdJAWQPwNKTLECbeTuuh2oGECxHun/MTyeAgS08DoXaAtKyv88O04ZDrK0mTk+YFLTGOCFH+6iZpkPfAxU/PBwE9nlQ5mJK78paAOpfQwy8Tv/vz0CuTp1IrDaRyECmbZnt8CTAwgBqLPrI64fWr5FCgjNpuy4T/pjsN8snX3fyf4xFSPQ8FtzAOR+IgHfuQYgeJ09chG05wSkdpH5b+kD8uDe7z8/WvaDE3zo8vJP24Mf/94O4t6EjT/G7WUWtW3ZvCwWj0b53ic/gwpZgAyJS7959MxPjxr89K0GP4Ea/PSowU/g2advNfiHhR5+e5n9PWX/IOItx19m0Ofl5+X0SIpdf0ritw/wDfuJOX9Cp6dfct3/FnSwfJEBWJpiMQJo/mg/70NADwprP5wGP9pRM3WxATTOOwre28lHYrwVDQDZPJx6Z1N8V8yTTVOYH1H8QGvwKJ/6gDdxwtCfNk/ppH7jP73kXZo+P+V25v/tTdMEzyCRgWumjRcoKUC42ti/XwETwYPYnn7/cdeo3H/Y6SPhmxasZtd32HgroDc8fJ7Ydg4gZ9rZTD0o/55sTTa0Yzkp/dhITaTug/H986r3CgdreMXLVOig/wJ2/jz7INrPs/etz31rmXdg7/fLRPInO8FQ8PUx9mMj7PhPv/6JGm+c/y+UiCeQmWDpYa7vfUOQewxLuwVAaegSUKlw77xj6njNeO+M/2w2WLD2qw70em9S+ZsPvqlWPPT5/W5K+9jY/vb0jkHT7wfxeGQfmPB/zxYnP713+ddpJXuSd+d0d7fdg/dqgzyZuvl3j8KJmrw+svvpBSCa//wEJk85lMa3+y7/6aEesOsbxwYSADZ9aiZ2sgDFCSQBzlBONiUAV79bYLode/fx04+XPyfmfwdkXnwSomwPt22CciEKpnAPh10ChSAcC3w88HwfXy5xl8J9aInhDuHiEEHYSxhcEihFOUCrBmRVZr9ptYCmGAF7PgLxr+8enh4CQc+CMRxIDGwPJXAcclCSoAjShhHIJfyAcmzP8xAYspfLJeG4pOMjgYtSCGxjGOQiS9dFXMQLiEneG119aPn6vjV4j9oDfF4BfmfxZANs2y7pEhDqUYSNuz6ydBDXh2DIIxB/iVFIQJI+CuZ/TH2L3BTYhyOmJAdMFfDEflrnt7dMmBIXR8FIHm229OPDLijTxhHJuUan+Q0PzsWF2gr7faHwx/0yNfKm2qJEvFd0xLbHfeh69LoZHZOmd+jmIMn2zdcistCxJMdyiYj1tlOS3EDJfaJHHjn354tcoc9yyPHIhrxpB0lxhJtZmJ6Fj5vlSY424mYZXuuDdFX0TS5s26Ap2viY2dFaqvUMQ4xKXDjS4bZwDljZIoWyXydZZDTQMToKQjrWrYi2spD3xEndkuvz2HfuFbqaey82c7k1IquJeOGiYXyx2PEXHO14bLnoFyN7OmBY0JurUcB6hibyYhNeT6nvaE1aOThe7VLxFgkumUYJNUCkuWv9tC4PIQytszN5MhcF73XCVrvCCBNdqtIujk5N4v2KzwZB0CIR7zTVxugjm5RbeVeMiIKt68qWG8xnbSOSyU7EaDuvcBG7pGcqv3bdbqEj1bk8bS8ee7zCup5Y6KnxNDZthMQS2UGXi3LtUL61lszqdnZi5XAwSJ9pyupAaBbH0s7GaVwxb/eahJE3065gyXYEK9mAioPoC4poRaYFziIqefMsMZbV2DK15qmGlbg25IiDYe/Ovc+lmK1rO/QMrYqqL3cR5BmECt1YGI2OnbwftNu44gyIuC41FL9B6hVuqyvq4hYT7hGM7rPDbo4eLhiXJxK3TTxCXokueTiV8C6cj0goN4SDnwVTO85bNHOvPSoHG/MS9aEHS8fYYJVMbbIgP8uSQCtMxEhoHQuNtXBUQSaFgRoiYw9fZCOC+i2yrjnvfDwrNL8jFtXxWDM70zJx2SJzLFvFt+K4jQ45qVkWe7tlG5i8cjA+7tooi52jfXHONnTU2xY5dc0YOc3CvLRGvpr3HB1EdhCJpj1PiyQMkNOiEHwJduXAyhcM2kViKzoc5B6PJiY0DRdcAUlYj460dwkyRbsOZEtv80wm4c7KHXD4eln3Ai+qHG9eB2GzWh27sCR2e+Goi3zNdTsGV3PfXF8v9pEc2mPJSAl0YYpwgcLxuPbqjbS+eZcm3mribiFJ6XDebuIySG8SfYvIAwOJRB6w3aD0hMtldSYdj+0aymtdhKBtGgK2YAsNY0NQlBBxgve6qoG9w3lxwI1OJnB1sYUXErxGzO3J7Ov+usByVjX64+6cORSyUwKCiG0UOUCwklyuZdcU1DLxTmuCv4jXnGsFZ33aunI6XyMqyW8cswe2UUioEZXZeYcta25MfW2WvCAfrTWGadV+JBeuHaMY2RUeZYni5XKbY6tbd0Lx00Vs+Lln87CwCfKDrEIjVh6OxVCJ51vj0gqWxBKELyuyFo29EkmYiAkdrMfDZh0f/LMoauR8dSNTHaPY5sDdlgxH1DmVH8oqXhObeYcm+1JXGGOxlNbbrWBULuP21wJnb+SwPkeo2+zhYnukccjcQucz5pSX3YUzmazp5WVxBV37aHib3dZEje6aXNEwTxyXOgtZtKcxkjJB+bVZuwz2ZmGv5kIXSBeVIW80aC1NvTE5jprvfaLjex4FUG7WSh/4bJAU7cm9kVYjDTueUPo8K5b4XLaacd/ltt2QOTmqdXIKjhrUpaLiDmqUIgTvXthzc91vUEvR64JezLGOo9UAZtErrRNGdeAqAsMWq2Fpy/0p2MqSlRx9Qg8GHWZHulgzC1GBY3Gz2OI7dM3xW1KuMpaOBCIsAirBq4yqA5TmJOswuLQflXtlmZhZFXa45K5BipoZDXsoK4a5chD2sd4Y1vHIq27jn21dqc/HzfrS2ZDnlG1AiQN5IeQ4L5WGxMngBA1z/2QJAs2LbLyM8AWOGHvD3pwoD5NPcChvdWlUIgzBFvP19tJTELTatSpPOpS6aJZqjSyOJ9EOmnox73lqTmI6InLh6DoZpvRiR+/HzULfnjWs67u9tSn1FXYs0uRW1VSnbs6utFPYaukR4fa04SJVQpDRHwz1ujhcMshLTutLUjGrNtmf97XqCfPESvq9nNT7ljY1ZZsaBsi0w/wYSYM4VFaNrqVVS1SeSPr7Rs5YmQEN53CjyPwsBBzR6UWyJ0N0ecwPUgbZ6dyOuUI66qov2CSMNRFoi9SKDTftyj9VHJamgoq0ynbjxXPkvGENOOqxuMB0iZerpq9vWQ0veIRmxvNwPAtLyaS1iyhCKr7fVgg3L7uxxVgtEgKJ2CFLM2bjquvjfc4mZ2cFsbp8RJw+2HEJEap0NYhz2C8vjnna0HuRMbzsZHRplTYMIwURdtQ6qMSHUT8So3VQuqXesGlnG4qjn2FaFPMrlHIonQPqLua4XtB7jqIXoXBbbTWJ72U5JXIQG11DQqPisvRGM20OHQeL5DM+DnawI6+VfXfuKkfbOaA5Wby+0a/MRWtcQZOPLJchh+OyUdRLRG+3oqQzFiKnzcAAZnlTei4WT87munEWeuruQiQB6VehNcPQcJ8mJ1ZH/MtSi9abuQ14zaBQJ49eCarTpLTpL2P11uXCuCrS+WDv7NjRxhwT8rwVDllTHg1lyVytHZnUmzgx9CHcaAEubNpCZGhGzA7OdmEHwV6liv0yJJZMcKhdiSvXmdfSt8Y++n7JZloT1umOuLWFbUOiZy7Z7dDWBWBOSr7oypDMYHsPrWMGKRUI5veVW1AefLh1lOfc+KVL9XGuLWAS3m32qpQgIq4e4zlnlf2cjmhE2MEHeV3YqLxZM73MLIe+Ro/DbjtQx02RKFuL5c54bC3JXsLjlMvlja7Eh1RfCoa0spmGzlbaIcxrpthfDDgx90l3TI6wIvfOKleXp2XIeHR4NbQe8vqQBtRM08v92jBulJUu3cps2pgF/MIdmUHMuKyMk/6MqtFq3PrbNWg9abgtuJUIOBzPLKKtzM1Fx/eyAo25bK3NR0bBirPIFBzHgAKmlfM8JxUKVzvGpdeRNrgDYWtMCgMG2pyIVe86iXay6mK1p84c5UU+e9IKby7B6V4nD7eCWPmLYIFqVSnHhYefXK0sSGoobsm1W4/2thYgibqxnbFZ5Ugc7s6NJCnmQoI2jEtsTpV3PKallymMqmyzigj1G3VWjetqa1e14nhS6h93qlHkZbweec7pxVE/BV1VMRmyJkz/cm1xGyXlgWO68VRCo8VZGcjsrHPdOmEjbsvt5pam0cZhbW1UflfAJzbDF+HmtraMm8eIy+Yiohezti6+JsdLaeO65XxOVDhITpuA0/OaRvED3HQaXMINTRSrhr54oXFqxaA6b+y64fpUR4fzbmNYtB50+app8wVitm0HK+Haw07KfL/BVhLUIuJFr9wNvjm1LOuGTSpe8GqzhCVpX+TbgysI7JI7NailzkPeIfWoMugql0/b5aUp2TWppY5yOrA7HunzxpMh001MlRWS9JYa+irbsLqSpVXN3A7HvWh1hiuQ5fKauF5RLdPyvBlb1fC6dOMl0iGztUO1aY1iV6KyppqXg1sua0uD1qKtydtgr+yMkzKkQbHSTI83KPviX611XSbQXFYLmmSkarPX51dHtYV4IA4nabPSqUNmhqeuWrFb092aFimh+XLBQqtqkHa7Rttd4KoQZG1vab2jWZpnrBd4bKhhurSS89DFC9rnNnzgZvtUNyIWXgoHTOJi1dEEyDYgMwurZXjaHYf+IlspbFMgduxNOjvmDVurB6gRYMjacuIhDBszkmgnQTL/bMDO2RN9zqQXmGUDXnlbiYl4Eta3HJWWLIRr6HJv3Sp2hBELwrTm5JnZ9nYkhEOFurtlf+XXVrevXUrvrp2hHLO6jfuNpjPu3NTCUfRI0zFR2rA6JrRXQ1TZuEfoTUuWJLXcqwiqHhr/sptzNHzFRHKrsliJlQGSDIjfKFt8QcRkH40eunYQdmhuZ9KCttfTZlUi3T492u54OKnqEIXzjCE6mrbpEbJgcqdLuBRcbg2ywLRDj4Ik3IwWv6NOBbw7ZmzHxu3monHoUIannOzxVN+rcKdF+Uhf8m5xrO312bG3+d7NPeqQbgnX54O1wmF+JlTWWVTCQveWhxaH8vR6mc+1hJCPoudV8xSbyyelH0aSBOXvnWV5JxABQWqL61Iu5FuWNVsntwoc0XLtulL6aEPg7ZCFHuBgzGXbrzTg4xWhqbJwPWgCk8CAiGM5RVvXc5Hx8AplRl0enSvrRtxBdXNpr6AWKrPuiQFlvrAj00k9PkR9KpVcnWdze/QNlLgxuXEprlbqbzPzNLTENWwHGz0N1LhYSEo71iUIR9TbPc3fhPQMWiO7WvFEXcgdUDW77XeCZhaBbHcp6S+dcT7MjYYfSVM7OYeW2A7Q7lIbPMgKEqpJZw5drlrMjAW7Flpa3gvr+U21CZQD+36iWxSjJaonuObNzVHPyNt+42Zy1DrK2PQrzKwoJDkofHW5XCLYgkjfJzu+Y8/bg+Slh3jOCkGnnWySvWZolBzW+9aMlSsvLaNupwZGI9FJAHN8PUrZHmG2S++kJSnKUivEVbX4JG9CnNXhNuL5M1cmu5WjVp2wQ9Mb2MapplSapKDRF3YHUdmO8vO6P0UxR4WymV7jwfHYbgmrShira66/zcuQlpjb0EQ4Fs8VkktZStGgy4VKSR4bkmjTy9wtdxzea71mPAJ+MfrJEt/CFsK4bQqN3dlbhtzaCHO3GigaETsPszni0hd458Meh7j6Cj66o90zTBs4ZwVKCnGM6BNJbaPCPdHGiXBc88YzKeBaDX/c092RGZydBBMyzByiPrCI1Dwc2oTger0UeWUvw0kx7/zi5ks6dXMFfBXGNT7X9ovmiOYRDSoC1fqlbSncKOcCzsCMW8XVdaGL12Zz9Um5XdBchzhg4pzmr4s68KFweSXKfqAw/JbP1VBDyOGGLtRVnajiCtl3FpWUGUk55NFiytKvdjtOHueSJKzaweXSwGn5/qbUeLzWkDoYslsm8UsvCtZn13AxxsPpktK5XSYT1PxoFBAGZau13XFOfqks3kLIcwYwYG+APtVtef46GLpSGDbeoWdMPZHwladvcb0pC62Lk9Q7Z76+WftoQStRbaG0CjHskLMXpjquLofhLNen40B2gYO0ekx53vzsdGYo09uW91aLTErQdjBQX72kYl0lAoELCL9KQskKRdRnAGtmldPS0jAzGB1jtaNl1C2NRFRTG+6NSjXy4mIDpj9CzQDUQosIHtsiWyhIunHTbJ6eJapsozgT2qbb4qcITrv56bzj+sI7OckugTfjjaPGMcZ3V0Jyin480NUKF0gqgS/EKV7yCm6dV9HA2zeXGyHdP3PrzC5TJi7nlDSYaFLK42Vk8l0g7BLygq1yTNUYxLvhVrJrMBXs2FiA/c61GAuapn/++en56X6U/fQCLSkIe36a3pC/nVX8S++ow1tcvr6JRsgl+fz0/+4F6eNl5fsp5/0Ywbe9l/vqL/+C1r8+P9VuDDR8vOZu0i58e0n6314Sf/rbb7IncePj8H46rr227+dCrR3e37yDXXzXtPX42hRpd3/vDiLTNdOf9zTTX4C54PvpbnZWTucjdw2mby+L8xhIrl/b4vVxNuE/TX9+M51C+l787TJ8O7Z4fvJGEOLYbV4RHANOKSfL3w7gptfJ0wnc0+//BTB5HS/HKAAA -->
