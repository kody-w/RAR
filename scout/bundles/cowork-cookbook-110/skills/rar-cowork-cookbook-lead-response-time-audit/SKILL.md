---
name: "rar-cowork-cookbook-lead-response-time-audit"
description: "Measures how long leads wait before someone first works them, and highlights the leads that are still sitting untouched."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/lead_response_time_audit", "rar_sha256": "8122afe519f09d14fe79b5b1b4e32690c7c59cb5c1b95e608dfd0ddb4c3fe614", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "lead_response_time_audit_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/lead-response-time-audit:a45b39f91959300d9c87919ef7da136b020de21a2ba67d4c8d39ee7a31d9ce51", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "prospect_to_quote", "intermediate", "integration", "dynamics_365_sales"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/lead_response_time_audit`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `lead_response_time_audit_agent.py` is
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

Lead Response Time Audit — Measures how long leads wait before someone first works them, and highlights the leads that are still sitting untouched.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/lead-response-time-audit
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `lead_response_time_audit_agent.py` and embedded as the fenced Python below (sha256 8122afe519f09d14…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `lead_response_time_audit_agent.py` first:

```bash
python3 lead_response_time_audit_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 lead_response_time_audit_agent.py   # or on stdin
python3 lead_response_time_audit_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Lead Response Time Audit — Measures how long leads wait before someone first works them, and highlights the leads that are still sitting untouched.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/lead-response-time-audit
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/lead_response_time_audit',
    "version": '2.0.0',
    "display_name": 'Lead Response Time Audit',
    "description": 'Measures how long leads wait before someone first works them, and highlights the leads that are still sitting untouched.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_sales'],
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
        "upstream_slug": 'lead-response-time-audit',
        "upstream_url": 'https://coworkcookbook.com/recipes/lead-response-time-audit',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9cbb47434cf8126e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-sales', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/identify-and-qualify-leads/manage-lead-identification-process'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/lead-response-time-audit', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'search', 'plugin': 'dynamics-365-sales'}, {'action': 'describe', 'plugin': 'dynamics-365-sales'}, {'action': 'read_query', 'plugin': 'dynamics-365-sales'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.429, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:audit', 'word:audit'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class LeadResponseTimeAudit(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'LeadResponseTimeAudit'
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
    print(LeadResponseTimeAudit().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6eZOq2LbnV6Hz/VFVzzwpIIjkjRvRCAoqgwyCWqcii3keZIbq+u690cw8p96tukNERzQZqQx7r3n91tobf3symzrIy6fXJ9U1M4g1kyQM3BIyMwei8y4vY/CVxxb4h+w8q8vQauq8rJ6enxy3ssuwqMM8A9MF16ya0q2gIO+gJM98KHFNp4I6M6why/Xy0oWqPHXzzIW8sKxqaCJeQXXgps93dkHoBwn4r+8336fXgVlD5jS3DpMEqsK6DgHtJqvzxg5c5wUI4vZmWiRu9fT68y/PTyE4f3r97clOzArceuIBHcWtijyrXC1MXapxwhrMSszMB4+LAeifgevCLYGQKbjluB70fvVj5SbeM/Tf/x13ZulXP71+zaD34+vT9Kc02V3aOjer2nUg2yxMK0zCeniBqKQzhwoq3bopswoygQ4lEP7lMfMbpbyA/j49+/HB5MV36x+/PuVABHMy7tenn6C8BPzKZjp/magUP/70kuSdW/740zc6VWNFrl1PxIDUL2/v1+9kwcBvQ0PvzvXvgOrDjZb79ek75abjIfekJ5j59BLlYfbjg3BR5q2bmZnt/vjTX5EFzrHjJKzqf4vuzw/CAfAV0Old8J+e70b+BZq9K/RJ86/ZFsCt/4kmYPgHu2fo3VB/Rftu//9BOgkzEPMfFv9Tcn82YfZ36Oe/1O2fTXiGvK9PjJuELYgOK3Ffod/e1OOG/vkH59vNH375HZD+l2TUvCntO4W31MxCz63qt7eff6jut3/45ecfmgLEmmumb02Z/BnNP7Prnc8fLPg+6sc/zgX8T1mc5V0GfUY69Fte/K/y9xdIN5PQ+Xa/eoW+z5fpmEGTEh9MHyb4LmcqIOt3dvzp6XcADBnQprHvj0GW/9d/QUJol3mVezWk2nlTQ8DBNUCISXgtCCtIe0/qX9XDjudfUudXKHyAE4AIs0lqiC3NMIFAPkwenzTIPejX/23fgfOL/Q6c8wnK3sp3DHqbWLyZEwr9+gJpAWCXl6EfZmYCKdTxCJm+m9UTo3tIVE36pZ14ATnCB9Yo9G7CmapJ3L9Bv/4V8bc7nZdimIT+mgEvmMA1DlS7aZGXZhkmA2ROqGQNtfsFYChAjjJPEsu0Y2j6aIqXyRJG4Gbv9rFBhXB7125qAM+5DQT2QoC7z8DFVZ60AAUnq1XxhNROWAKT5OVwx3Zg2deJ2K+//mqZVfA1e8DuAnqUkGoOBnwKDH35UpSud68FXzPXDnLoh99+/wH6P9A/m3UnPvE4Aty/2wmEbgLtVUkEBcRvUjCsgqYgAAa7++m33x8OmKTLQM0D2RN6oXufDKh9c/qkwcMrHy4BOk8iuuU7pz/aDeoCYBcIFD63BxldPX/NJhI5GFp2YeV+GPEx+WH6Dx8/+Ew+qd5tCPzklXl6H3uPt8mZdl46L9DOgz4tBdQFfq0njwY5KK+OW7iZ42b28Ciiny7M8hqqQJZU3vAMNRVQdaL8qwVIT8ZJARSZ9a+QQB9BVcsT8DEZ6M4ezM6zcHL8e5A+bgMi5Q8gxtYfJF4g0QXWhAqzNIugNCv3Ps4zHxEBqtnHfEDchDK3g6ay7U4+uufvPfKmyg19lG5oqt3QvXhDXxsURjDo/1fLMclGsayyYSltw0AbUVMuj0CaOqRJr0dTBZoACAjxyIpvjcEHhnyg69csCYHxy+Fvj5HePXYeYx6IBZQEhqCUO/0pi8s73bAGETC5tCynqDW/Zh8wDrSbormaEAkkajylff7JcHr6IWkAsnG6/lbSoUdwTfYBYQsVjZWENuS5rnOP8DooJ7e8uyCbbAtyCQS8HfxBKwhQB64G9CEgRAgsDKD+bjoR5MFk0HtQfw4Pp0YJSOE0NpAWJIr7AhmTJ0DsVcCboNuZxgAr/HAnBaUusDEQ8dPCVWAWD2GmrvVdQBNQbUMQX9/Z//0RiMCpWgBun+kFaJqOWQNLdsAFIHv6h18/pXz3FCCaTqF+n/RHZ79rCn1fbf42pRiQ8BuygzZ7KtTfmQbgcplW96gEJTSeghrE+0O5KYynmvzyKKuPuv0py+s/NOo//me9/L1Qnv7ot1coqOuiep3PH8Xso5a92Hk6BxESFm51r2tfPkrPl6n0fLmXnj/Qe5jnFfrPZPoDifdQfoWQF/gFnh7xoe1Osfp+ABPQX9aXL9j09GumuN98C9jnKcCUyeQDwNXP2vExBBQQv3T9afCjllRTCepA1btD2L0WfPr/PTcAQmb+VPiq/LucnXSavPlw1ifUgkfZBOLO1J757rRiSSbxK/fpNWuS5PkpM1P3n6xUJhQFkQmMMK1rQI6ALqcO3fsVUAY8CM3p/I8LMul+YiaPCK5qIJ1Z3nHgPSNM/47Wz1OLmwEMmZYTE/hl33c4k7T1UEziPVYvUyf12Wb9I9d7ygIeTv46ZS4ok6AlfoY+u9tn6GO9cV+5ZQ1YcP08ddaTnmAo+Poc+7nGtNynX/5EjPdG+y+ECCfUmHDmoa7rfIOEu7cKswbId1J4IFJu39uDqTBVw72A/aPagGHp3hpQkp1J5G82+CZa/pDn97sq9WM1+dvTB6hM54/+4BFnYMK/7N0mc3zU3LeJoDlNu3dYd+vcffRmgnCYaut3j/ypUXh7hOvTK0Ai9/kJTJ5CJQnH+1r56SEFEP9b/wooAEz5Uk29whxkG6AEKngxiR4DPPyOwXQ7dO7jp5PXP216/wwcXk0MtxakRyIkTi5g2CHtFQEuXI9wTGSxtGAUdlwUMVHLXBIOZq+cBem6hLlAwFAXRwDzCsRIar4znyOTxYHYn2b9txvwp8c8UDlQfAkmrhAUNT3Ag/Rg0kEwzyVIC7cQC3MX6JKEbcLGSdvCbcQicXcJrxzPgR3HwuyF5y4RbKL33go+hHn7aLs/fPDAhjeAomk4iYqapr2yCQRzSMJc2u4Ctha2i6CIQyxcGBjIW61cDMz/nPruh8lND32nyARdIOjB2onPb+9+naJtiYGRHFbtqMdBz0ndXGKE1QfnWbl0L0I0izVVOzj1AMdWvUWKRjRXazTiz9pO9HfjnrJVV0pU1mTrQ9dsq4DBqWzcHxfSmQ5VrC728PKww2xZvc4soTkTmezra4ED1UvIm0Bd8meqRY0U20rLWjOsree1t+tRcWwELnLQYaE83Q6i3XRnS3B67HopqTxJ6SWaV/7WgNPkQFxKhNdT5HStCmzMDk67I1WL8XAdX+7wM4tgvZbaZWrowrC8qfl2ken6JmNxls1J7hoP7nkLz6VzQq4GFXdbnljxqdraWles4jKWtvU5hfm9Wc0pqgr2o7J3V0mQkpvRbGaFqsNlR6ihVrn723wVNGchEWb04nKibX2/kw9jiImuio+53F+Ny7ky5TOtxmnu72bocQ9WmGq962vsUBiGIg/ZXjzhZ+UsOOU5n4lI3y65pghLO8QXcZiu9/tc59VRjo7LMdRovdrH9mXVyNdjWPXrW0Xui5VxILTLgJ61+GLSFRmrli9vgNwmwdEFcTpRsxvHJmGDBMKg6BRo7Bx5NxPhwz7mEH6WOEiZcgyzt7Zc7s/FXLvoMb1YmoFSikQHZzsa7ktDosNZYvBnJIrJc9fkUeJifbmmjjvhoi2yrTK2+XEz30poywVRnbEBY8stZxy2i0hqkw4Ncl6t3aOSX8Y2vDgsCcZcyADJhZlBn096UJ1HVplpCiaMxJWO7blxCDiZNaR2FFw2lk8Ejw0+Dus95wpzMYsTV1i6GJXvCSU9zFUktsJz1IS309HnRIu4GUa5FvWrvhSuqwxPmXDM9X11XTAcKhfkvgsvy6vNCditl1jh1A/ooGciLwYttgzEzspqv4aPBHZeVMe9sM95G27R9Uxyx56ci1y67x0ahEt11vvr9RwnKnmds+7ypO2rej+2wzlcEifVJHObtY95JY6MS7CCCmdlvrJuvG+qjD0/yzEZRMk1j6MgVtgqQhnrGHb5Jb5s0jLGkuGABE3H+OIlDzlcUfoNcR0v4YZmFOoqNMxark78qrleDFsKL1Jxtue4nq6R+c5A+lVn9Ws/WMXmbqBCRbD5C3fWbjkhHNUdN3PVAkm9LQly2FubpeilnI6jEdmijFGhRzKMIty6EsmIOKvyzC3NvJNLlIs8U+VL2ir6RECjtBI18bSk/DyZ7V2AThJaSqEGL0m82DSKvt3qCjM3FPWc53ZXRPHpNnM5gm2IVD04hLntUqkt4WokuTR16Ah3paKTMyQ/mzGi1qducTySpu1TNbuNr0MvHdCx5TYWwoQ9UtKHPbdb4PtuWF3RQqZVXE5VKoKPbUhl6cqxh5Wy9Boa9SrFFUvfqwLSPuWBSptu6+VUgnnoTZfoJiXWtsd0A2wLwnpN97zhBwZT7LU1Qm8ZT7hG69L2F+qZNY1rMvI8rdvaXrd1k+WZXjQvIsGGc2O9z8Z+zhu33lO7a+twQmkclpUmzLjQi7CDu+zGqtzqLEuumGiGMOdopoxNjmRWxQudffS8sGFgrt+JsbEX+1a+8NdkzWLmreKZZcUsYYUpG1XGk2Os4aGqMWe0WUgH5kqvRKlDa9lcYd4ACC0lTNlpzSlV2IDE562CmEJuZagi7gpMd62r1/ENxfh6oCHLnD/x4blbExlxElmduLo7V8a5sVMlcmjiFNXkA9pfjsc5RntBrUiXm85KunFy4V1wQ/vUl9en7bZDtJ5b72QDTXqgI+EKtW8qUmSxcEzfalm6zc4Zlx4F7DDb4YNWzMlWW2GVUdLDYX+4+dSa2qnzSLoph2NIYLcVusYVlqPSTVY2JOa0IsWUdXq+8EEoB4vB7Y8c047jimTZYda05Bpf7fEhak7imrqNGV5Gu4ZSB5oLwZrRRs5HUaLlLdvo0aEQYOaKBcFawHB7qcANldg86e/xtdpaTXiIlErBQ2TYX/YSXJ44i3XW6LXmDCwyA/emHvJ6Hw3+zh0MRxcscdemY52jct+ygJbZ6GcJyVZ8c6WMYCWWsYBUw7p0LX5kEYY/7SXJE4urkQraFvjDo7KyqDYYad48I6NxnKbTxG9cS+/VcSER+WXDiY6cljgbhgZuVZc9sVWqfrgmFcPCm6DueRJLdqUESvaNbIJkPJGcWpwpMjFGliN5jLiqiEYmh11gzkllRNhTOFJRucSEOBnzZT0goa70N/eUNuN5vtVxbUHskKOd94fbid9XpM6cT9nmZC19EdWdE8AXtTlINezDbUBvtd1+e3TPrIj4bXLZYFhun+l9NF8tFBa9CrtEC+VGtTZrObtxTXjqhqVvo7pkrLTiKOaY69+21DEskqDgB10+8dt0bFS8w138ROWXQ7EkEjsiImu7TpxO4ehGWCsCaC0Odc+Mvc8zGYaF8GKveIR/PZjNruPmbnPV5ZmqRnbLRhYu0J5uw/U11LXtJZc4vYqj7egiuUjxSqAlpS1edXQJ04GQ1IYZHo7mlbvOlXgvrcmrbbh5NxfWTLktu5tPXHTVpG1hbwBW2HZLIUZh8Js8DkMxT8NQsUzavzJ+0aFw1o8oHMzNTb2TEOkIj/NtGPeixMwXgcmqTjHcKG1k8Nw6V86lNworbwZsWNolL9fzFebOUNPFhO3BKIp43eZmAjO05OUO6M30pjKJBQeHsypc2CRqo8ftcDzEGbs8uknDLoLLzPf5qjc2h44Ko04+7EinaOGhKHdqJ166mbH1U2mnomw+i/QBq0czPbNryqNz/Fw3dGJolyTbeDItW2kmRYck2hc7tUryESxH4IGsV9Vywoy8GNMtrS8OZbXBD3G8NU/BdiuUpwXJ7RNrR8nnPADILy2L01DkyR5tjpjMY/uN6uTbzjcOTenpfUydEAEz15qEbI/mGKopLaf9erbMd7p3MvtKS2GCvR6rsVmvEM5fXwoa6RixptlMIdKGdCqJ7Jp+66TSZg8CyWJTl2+VITD3lF4vV7k0qHG1aIOuc73TiJ1YzxACGo0HTWoFRrjIV79Cs4MhV+hKjlPFXq6whLoaSJsc2gJ0MDeHLkeh5C8Ia61ZqRHim1XJpdqwFkMczFsm8Y3Wt8QmvgkyKgYLSdsTEchcR7MZsSmIbjWvSzjShtGXOQJXk/PV15I+2q80Q3dFQx8COdhEEilQILhiZKOMfW+KxVhIGcZU/VYXekkV1+yAXGOkwttFyplM1Ugn73zErU05M9JVwa7XkuuTpRWLB+FISUsKTxSjG/hZdkyowCwrtk0UovBINtZ8xVuWS6Wj1yepmrEGw56qbBtJoRs5Sob6NbPl6TV/QszheCO3uBNl62ChXgvLD1uFC8iNnpjCiTufG8qnc83lo41KLRx8M3hNTnbwMt0KuZQydbwds3i/WvtdpfqFURwubB6iprqx4OE6NrR4QteGEVi7o360jop3pS/wKk4uJ6uCN92+45ALutiO6+tNKOBlBmo3tWVPM7NLRp9wEBl2bNDIICuqs+S9d5OOO98Sa5zBeJu8hfAVVSRh2I7LVCi5mX3Cr9TpdFmt8GOMk1K4FhpsHYt8SNO6ItBr5rAl+A3vmfJhfrvKs40bDhq9gZUwYgMH1fd5fgLlrtZPt5WeqbR4ZTFHNW8Rr527c3DLLSS7bDU2v+0czPfQMbFnbTSSPO3UrFEy67bnfUzOUALFuZQVVWRVrOFxx6QhFld1X4aX0GE6WhQ27mFOiWoicXvKBAUI1BvTPUkmal4tVl5gS0UQAqFvTG5/aIdlsN4AJcO1FR81DEdL+WiPF9IdVvMgvWBiEZIGmS4zM+P8cRCVhZ0QRS0ZYDVUX6yw5ls7xWZIsbieF7aezFElO9UXAt2WZTYeL7TlqE10TE3xUpTkgaoYhmUOFifhNIxdTD3z9vDmGKQLvsRbbNwd67llVzRlFsIsuGFotUN5ON2vN3O40J055uHiyRdPTaFEA1VGCIrzMrWRuJLhhLGZ73e+sFj42KXvFtkpkiiz104kxhuD0zB70rscIwDTyDbILKvEVTvSZ+181YrH2a4NeVvcExYx23lLVBCo66ifO2Rs4Yt12651+XLGKrLWb1o3EVC8XcvI9cmgLHEu7GlQ2dzEmCuuork3Aa1shbH2Mwqn0qvYBZJc7jNJywpuI6zSvcTveiHak/KtXjbRohKkhoWpM0PniV33i5SXOgYsDhN3lwIZaqL3xaWltk0ZzDzeIHurWGDHWWu2FDfyclv22/UerKhQlF2AgOBjJFJN1jga+nkYuBrtqsprpkYhLEPCdLKSZ5XKNfN5nZzzdl6e0YqlNzdelxcb1GeLje9d27q2Rf6cOQvvFIhrjXRu1Ko8LAV4vbSLzTUVy+vsnFQ6Xx/TFa2g89MGcCGEIrLm8Qbp1LV5mQvLk9Fd97PuhpwplIJjIZ72EEPF2BGNdCRUEqwKBJ7h4L202FlNYNeekugU3QbZrS1VW9rana6xfuQgLX0a9sF2yRunhb23sd6m8LhJzl2c56oyK+HZvHRb2T52EQ1zQ4j3dLR1Wxg5uhegH2MgkrJY69EFQ7mr058Zb2x8j+NvACOaOaJ3Sb2GO6L36hnSDyCeLSFpNjcvK9Z66KRud+ZNp8qSwEbk6iZrDaIi1IJrTrjFElGZLxs3tVnCLrn4YA9O665rt71IaFwshxl1JknFkYmGKiUGnbejpsSwHlUCF1M2zLWopMlXxuaMDFkkM4MxfVzrTMxgZADdKcVGN2wZ1VjFlCG+XjJ+nBGSzM5QpucZavDdbvTyVr2I8VXSYNmmcT3QtVkqhmqzImR4saJcjGxY0H7Lc6m2SM6mQ8m5zvbzs2vPl1sQTXiwQEB4aUf3RLeePZZcJNyWc1zoI41Dx52m745XZ0xQ0Pru9IPuNJ07Xw22dbnOXWSkLdA21Su0ZS8r2bnItxV1mhWiMaaWRHBsLrrOpbtoVpKuMSMl0Os8ZXbiWr3gN7vhuQW5StZ0sV8ONZZf2cLwrlF4TfUQhuFMjBQ3546XNDweMMaIDLiUPZnr+4Mf0VFw03W2DcKhcawzMi49sZHOZdkgjDNUrq/z/DKcjfjCNvJ9nTHYdb+2416YKewMA4vGKqXGYMhPaSf3nnI7H8qZZm0Zg7RTU96HCXZgESKRcbUpxRt71ZKjdpYObTQI6xNJcSShU0VnWMuz3y4S5HA4atrV7ld1lG6b2RmTWC+uz1YlxQxG4M6JyOHMr5ohOxyH+KQf53F66o7j3AiDMasdaX3zhWN64TJ5i/sX9XqzNjyjMVjt8/1exRMujtjrrI42V65R7YBZCuz8kIm3taS0K3Y00fXpLBQURf396fnp/lr46RWBlwjy/DRtY7+/Ovh3NpL9MSze3iksCJJ4fvp/t+/52IP8eIV439IHEr3eub/+a+F+eX4q7RAI8thyrpLGf9/i/B87uV/+ald5mjU83l5Pbzb7+uPdSm36983uMHOaqi6HtypPmvtWNzBnU02/VqmmHzTZ4PvprkRaTNQ+qIIbVeHa9Vudv92avHafpl+STC/rXCc0Py/995cBz0/OAHwS2tXbYom/Veb0uzSg3vsrrGnHd3qH9fT7/wWFfnyVeicAAA== -->
