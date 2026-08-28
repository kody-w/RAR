---
name: "rar-cowork-cookbook-audit-analyze-asset-leases"
description: "Audits analyze asset leases records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_analyze_asset_leases", "rar_sha256": "761b0292a1dc3359c0f30cd14004b4ac3c9efff75385d40b50e6836ac9ba381a", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_analyze_asset_leases`. The original RAPP
agent is preserved byte-for-byte in `audit_analyze_asset_leases_agent.py` and in the RCI capsule.

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

Analyze asset leases Completeness Audit — Audits analyze asset leases records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-analyze-asset-leases
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_analyze_asset_leases_agent.py` and embedded as the fenced Python below (sha256 761b0292a1dc3359…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_analyze_asset_leases_agent.py` first:

```bash
python3 audit_analyze_asset_leases_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_analyze_asset_leases_agent.py   # or on stdin
python3 audit_analyze_asset_leases_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze asset leases Completeness Audit — Audits analyze asset leases records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-analyze-asset-leases
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_analyze_asset_leases',
    "version": '2.0.1',
    "display_name": 'Analyze asset leases Completeness Audit',
    "description": 'Audits analyze asset leases records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-analyze-asset-leases',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-analyze-asset-leases',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5fe5c8ea0b1d0c27',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/analyze-assets/analyze-asset-leases'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/audit-analyze-asset-leases', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AuditAnalyzeAssetLeases(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditAnalyzeAssetLeases'
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
    print(AuditAnalyzeAssetLeases().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/71697PiSJbuv8Le/aGql6qLDJKgJibiSYAwssghqaujWt4bZJDp7f99U8C9Vb3TPW8m4sWjDAhlnvyO+87JFL+9WG0TFtXLlxfZs/LZ3krTKPSqmZW7s03RFVUC3orEBv9mTpE3VWS3TVHVL59eXK92qqhsoiIH08nWjZoazLPSYfRmVl17zSz1rNqrZ5XnFJVbz/yiAkKyMvUaL/fq+r5KWaSRMzy+j6zcAXMDK8rrZla1qffZBhLcmRN6TlK/glW93poE1C9ffv7l00sEPr98+e3FScGCbyjIBwZygsDeEYB5qZUHYEA5AHVzcF16FYCTga9cz589rz7WXup/mv3XfyWdVQX1T1++5rPn6+vL9Edq81kTerOmsOpmwmWVlh2lUTO8zsi0s4ZJ2aatcqDbrAbWyoPXx8zvkopy9vfp3sfHIq+B13z8+lIACNZky68vP82Anb6+VO30+XWSUn786TUtOq/6+NN3OXVrx57TTMIA6tdvz+unWDDw+9DIv6/6dyD14TXb+/ryg3LT64F70hPMfHmNiyj/+BBcVsXNyyfXfPzpr8TeHZRGdfMvyf35ITj0LBfo9AT+06e7kX+ZzZ8Kvcv862VL4NZ/RxMw/G25T7Onof5K9t3+/0t0GoG4fbf4n4r7swnzv89+/kvd/tmETzP/68vWS6MbiA479b7Mfvsmi7vNzx/c719++OV3IPr/KkYu2sq5S/iWWXnke3Xz7dvPH+r71x9++flDW4JY86zsW1ulfybzz+x6X+cPFnyO+vjHuWB9NU/yostn75E++60o/6P6/XWmWWnkfv++/jL7MV+m13w2KfG26MMEP+RMDbD+YMefXn4H1AAopGqd+22Q5f/5nzMucqqiLvxmJjtFO/FL3kSZN4FXwqiegb9TblcesGsdAcM+x4H4nzw8IS782a//x7nz4mfnyYsLayKdb0/m+3Znvm8P5vv1daYAiUUVBRG4PZNIUfyaW4GXN9NqZeXVXnUDPGIPjfcZMNDn6cMsyme//rXQb/f5r+Xw650/owcjSZvjxEY14MzXSaNL6OVP/A4gdq/3nBaITgsH4PAjwKCfgKZ1kd4Am03a10mUpjM3AmQNCH64ywYW+jIJ+/XXXwEPh1/zB32iswfz1wsw4B3O7PNnoJCfRkHYfM09JyxmH377/cPsv2f/bNZd+LSGCHR82h8gPMkCPwP51GZgGHANcCYgi7v9f/v9aVYgJgelCngr8iPvMRnEY+K5bzaWD+RnBMNntgdsC+yalUXVAE6eRc3r7OjP3vGCRadbE2uHBSg9rld6uevloDA1oQXUebdkXjSzGgRd7Q+fZm3t3Vf91a7uJcvLQGJbza8zbiOCGlGk4L8J5n0QmFzkETD/ewQ8vgdCqg/1jHoT8TrjpwiclVZllWFlPdfwrYdfQG14mw6EW7Pc677mUx30JlPd0+FhHjAIWMZ5uvTz5POpyoLcd+u3te9jrKmSKfeKVn3N62eoW5V3L9wAyjAL2sidCsDfniFVh0Wbunf7AaSTpKcX3KdX7jFI/lkzsPmxAbjX69nXFoHg5ez/Swtxx7XfS7s9qey2sx2vSMbDXlN7M9n10RGBkn5f7J4b38v8G0m8ceXXPI2A86vhb4+Rdys/xzz4p63A4hIp3eUDVMBek9x7BE4RVVVT7Fpf8zdS/gScemcg4ASQriCcpyh6W3C6+4Y0BDk5XX8v0E87TVYBUTYrWxtYZuZ7nmtbTgJQVVMWPe0NwtGbMqoLIyf8g1YzIB14HcifARCTUwBx303HF0BNkEB+VWTfh0eTgwAKt3UAWtA/eq+zC0iEKRhqkH2gd5nGACt8uIuaZR6wMYD4buE6tMoHmKnlfAK0Ji6OvO5H+z9vfQ/cO5IJPJBpuVYDLNlNFOp6/cOv7yifngJCsyk67pP+6OynprMfa8ffvuZ3hO+sDTI4ncruD6aZgczJHrE4EVANSCTznuED4uBeYV8fRfJRhd+xfPmHLvvjv9eI38ue+ke/fZmFTVPWXxaLR6l6q1SvIEMWIEKi0qsfVevzM9k+35Pt8yPZ/iDxYaAvs38P1R9EPIP5ywx+hV6h6RYbOd4Urc8XMMLmM2V8Xk53v+aS9927YPkiA6Q2GX0AZfK9hrwNAYUkqLxgGvyoKfVUijpQ/e4kCuz/NX+PgGd2AI7Og6kA1sUPWXsvpsCfD3e9cz24lTdgbXdqtwJv2oOkE/zae/mSt2n66SW3Mu+f7j0mJgfRCcww7VVAnoC+pYm8+xVQB9yIrOnzH3dUwv2DlT6iuG4APqu6c8EzK54k92lqWnPAI9MGYSpXD2oH2xqrTZsJbzOUE8DHfmTqjd4bp39c9Z62YA23+DJl76fZ1OR+mr33q59mbzuI+24sb8EW6uepV570BEPB2/vY902i7b388icwnq3zX4CIJuaYuOahrud+p4W7v0qrAeynSiyAVDj3RmEqjvVwL6L/qDZYsPKuLaiG7gT5uw2+QyseeH6/q9I89oe/vbwRy9N5z14QDAcZ/Lme6uECRDZYEFw/YhDc+ze6xOdMQIGgVwFTCRy2IWSNWLDroCi2diAfhRwXXkLQ0l5aDuqsPd/3CQxdYe4SsjHIw1cobjlr20JXsAXkPWL421TuowmNB/keuoYRx0VxBMOWa5hArLVrLQnLcqHVioAI3wVV4vvUBDDoU8WHSpP93hvWyRRPTX97sfElGHlY1kfy8dos1pqFo6zdh/p8xH2jiNfHk3wuWlS3CqsRzJ3Wix63PDRpebryXUJeuhPvbEg90DkOLviTcBgoMZP9q3vzqP2Q4FYTizBD7WlUgYmqmWPBbneOOWzMW3hBH/uKla+XjYXTZujTTd3vTjoT8kp7U+Gs11ECR3RCjqkVUSSSfKXlUbNoA4pRYYXJmiRbyk2HWs8kAuJUsTrtcrCZGb21OdfZOU7C2o0TO1ewtacry7UP3ELZzWrlV9cW26zRIHDGZN8b1dDyxUWGXczRLkhiBsnNk7vRK6wFkw2tDENlZ3uxwlnMdQHHLbpLufkeNXaCq7H6ZtT8XFsaqwvFMslJ04YTph2ZQQ0P1KoRLphOpq4ipTmxVOS6Dk0tOqMCDWmjfoHwW+44LBLeoEa7UQK2c6trtD0P3Y3Dw5Q15CKAsDrhPZKhYSHAWJSlolC37Ys84E6+PdNgN6QYWxKROaN0t6a8YoaTd0PUQkNQazyxYrCoJKET3D3ww2CPIA9OWEUXbY3wOy/arpCQDy9n1i+v9L5Gb1vZSZliv+IsaqWhajvgwtXPrT60V+dK31PW0ey3MWMtlhbpuRieLu05ajiCy5HLk70KtLHM1s6pX8XKQMdnL8dXTtj1jZcYiEiwAtePfHUNYG0D4j42FWYBXXrFPuoj3UTrK61GxVbc62UmbmWOnbOQtGaOhZ2xq36wbhS3MFW4CwsF3jp2RI8MnOi0R0ORF8xV1FeDFrlapczO7bGneg5lk3OtbA7iKpTxbZa3pytWn65mfarMWijkhi3Nml/sVczbOOuO9vqNF15dw5OXytkgykWyo2iCy9EVOo85XUovYRNdW5a1Vgmj38RljCqReUpLz53LK0W3Bv3SbJOhbOiwNfyFEWZ60mCH2IVdenO28+uczutjkHtk4jgRByfXzi6XIHR5Y4gaJ1ev58uKx0mLquidOmcZ4ZjbB3t3TiSL3J7SwGFpUMzTWNyOYSdTsEDkN6HphGrpIK2UKd6JV8VkpEiTg5TLds+j8CY7K/F8twkXSwzPVdOx0UT21wy0hwUZr8UQLRddzs2rttHWe/i2Qm4LMWOqURP05Upaxmp9O66hxFWTIY+ZPt83J3unk4YqLxgzn7NBwyyqXSWx3VFPbXm4RNciPKaGelnTSkZzQZTqZAUaGwttzaJE2+IyGPi84fN4YMLhdpBrUwoWRHn2eubq4GY4v6D8BhQSOShigemuGswkfgqduiUiSCIuSHSNmFFBO5teTCi28HwSE9wAtJyX09qvSNuHYm+dBX4dzp1NQtX1Ibz2iwD3QVTLRQdDa32sBlHxzsE2HHr2EoTqoSgVVg8jqck4hL8kgjHUoxJfMqMsLkcGt6pzbxgnZqRuxkrDz5SAeyJmwRfWqpp8nVhyupIpry984iauxIPgH8e0TBtxt13ywRoTVQW3eg8icmLni0VtLPx1vivE5Loku2CvEq3NBSfd9vXQ8PWj1youAW8JRjkW4y7P9rebG+y4nqqTqkMpxXbImI0II5mvDDbe91kvlytTuOUVJCjGIYbw/tTbXDQuDNajYqYgmTYuT1tb2mlidwx8fomYhzA99tgmCcQNQ6A2LtsuH+VGGsznZLJxIXNrydaoMkzEOMkajlIVrWGSZIKqza6eeaT7KLa6DiHCuIkvR5jd9WlnXioJVkd5jWPleLhIB1F2bWyFOHo6AC6WTid4t6fTkoIX87V0kgrNhxdJ71tkF9Lo8XrI/XyxlAKhJ+LrnjhzG9D+xqkeqQta76BFSIGN/2pxbEb64BQWt9XyQ+/vTYc8JHuRZuMAS1rPUvcFQztV5kpmI61u22gHLVeRhra7yNldTEJUwuk/iRAOMRIfmitxbCn6BG1o+3jbJIiHhW5nG7l0qC9JkLvHtapqEq7wOXn0rzWTGR5kem5snmGiSVCiu/h5OOd7S+0ZPz1jPD2/CUFCs+6FUGuF3aOMJTMoxuv7wzbfdKTTkZTSCesjytXNMWianqw5FSEOpx3ScZQj7WvuhkZOVI80BsOEtxwv55saidB+2EklFwypk+57oT3wOoSa0io4GtmtWecHawPYz7qsekGhZU6M+HOumPWRyFdeYSRuqeIHDxHKuFJjWjXmIbrnfVCKq8v5KNYr/YjA10J0Dhta2AKSSp0CW29C01XwfdvX24QXx3az6c/jOiCSI5S32+SEh8gx4bi6oJpkTG87XBkt4XAbiPOpKE3DuK40le56rSba9iLorUYe5M310ia6IKBIfzZ1ZyeldkyqCotly+rShHuOspwh5jSnuEBBNLam4u/oxU3nrkv7eJJa3aSadWZXBQOldgTrtHFk9toKtP9yjxbr3VGi/Kw60oIGUSgeFFmDXELmZu0OJaok2J70MVWbdxWvy/Z5kcMmuSNvqcocDKDtmTgf6ADFyz1LF0mcXQ+XOJJscxOYG7RcItYBlYmrtmg2l+QgRz3u+qERiKOJoArflyaGJ8yZxLVcRRbCPthWagnr1imjXTB/QcQLVq8QEg5KIZbPHna8zq+4EIeHCr647q2SvOM8ztcrFddxJOvrSiqNHNMlAmLJgWfGbudKGruuLnl4qINAPe8XilreFto5DUC5XtasdHTOuMFK632VYo4OnxCuVRkJiw6nptmpFWsEDb6hSL5XPDOUk6RLTC1to9xHCBJ0+SiXoQG3scQwKEpHNnMwNqWpfXqUJEWA7YM0lHJvJTR+FLAsZhg1sfaMvI6D+U48hsvgvCZ3NCmpKMaE3AmlFmFB70QVq5e8NO540QjWNem6bsbsszBehmoY7PIAQ8kFHpnni0wqwUU06IYJApdfEcvTOly3PM6dOGm/PSHluWlyhzo4JwFlcVk7MMqYEFsJUwJpZ/LHzY7F/YNzXd04ISSTCMfVUiPHCsLk5XqotnbuyXHpD76r6EKt4lstMy2tDHGk3ima2RtwJwFKP0M7REW19mj6eaxop6Nl0pwBu8Th6GvoWDmB2fYtohqc62cELpqjURsstMKckkvdAfCa1qmDqUfb9W7OYRBMk7dMUqSRoeMOy9rl6HT7dAcbPXY695htp0nc9nsBl3cFqRImD/tiOZebtWluSGefrIltyl8lh1zPSSIl835jYckN46hGGrY63qx3cRINdnW8KXJ4EdCF3aLIzcqkyFteUbndrtIY36NxmPPC1rVyhGw3B4I/HysudkDNLDjbkOuA9xmFX3CkhhULO5AuWkGd5663jCiWEvb1MTYObHvO8tW4bcVc9Ur5SgQ7eU+MzC46h+dMOVHW9WrX1Xmf2jS78S2TM9Gtzqhkw57rpMTzJjNudcgZjiy7XLMKFo1PR9S1sG2YufKhArsbi1uRLpnTDHtzZLBRgjRFQxWchhx5SzcQdyiKZUiteijxa29EakY7OO0SPlriVR3qDQyfkZKsKKY8BHns9x252cajTW/rrrwi1m4nnJmLJB62RpAuSDR0jrfIsTe7nblVuIt2MMlMTmU1yOBUzocLf4jgQLnC5bXiRtqlWqYM/YvfpVcrXsbwZjwYrDZiO1GB6xOCmlwtb4Kg1kJ2Y/No5hkqwrJILm65CGy3m8uFNUPaAnxv2d0axikLZhyL2TlM0TQOYnnq/op6bsS5fK9GTG+Jig9jwC/jQJRUQneYw3uJuFgu9klF9hGEuwbIgjN0JPbxxsYViL2d/EMnanNR8t183ZQ+sZDlplDyhu3mmdHAJaprC0dJVojUHrdnDIELO99yyqYxlTZWIstVr3OeCup4t9/i3k4wD9bSyFSgBBLcQhi1b0uRJJzbJht5g92gg8Ieqtgu4uImG8l+XGwyDRfDRYLWJC4T4148bhBRt51GlcKmSpxycEFRrOOmX7qr89KON3rW0naBb0A3IAlodfH0vUhgG6XuDQ1GKlzPl71zXmzZcQTNQK95YSlaCz9drFyeIi8OpM1tn+A3NX5eWqqorY4LW40haNP0bmpstiN0k/jAQ9tx4ySDfDYa0rikzqLQ3Wq3C+a9f2bkE6J4x21wGkwixRgJ3Yp0oERLQTkOK5W5OVWx3G/RW9eEOwcSbkCPHs22/FkxRpO+AJ73u4ZdRw3jeDcKi+Y3keNlsUJBa3ZjbpvDlu1uRE9SWBO66bBDMzYVITiUmUMsAvsMmWg3lGQtXJZytrxGIytCuOyF+LxCpYXC3Hp9oYupxe149cKUYCtO8nJJzseFvFzuvUog2nkRWZvcJtR4qKsiPx/KIZEyA2lyzLuEagvN7e50sNdnqZ8T9YDwt7mk6NTxUBbOWEo2leQEW2nO1mDl8yBd2f1g0kbcLrFFc0SvEdWZx3l4mq83blKnFc5VxVlZmVZMrHI20jla7QsSWV/JmNuoshfCGWh9fOHok56sKJXB6NopWKqZ78O4l2/7+d64BAv1wJxUY8lnOYWPdApawlBJ1yvdEPZkONfP2nlcoMZ2GC6p0VXxGl7R2DniziuMYNcN6SIwMp5ssLk44YpSxGbu0AOi6wyW6fzZzpJdFeq3juoJeHMJ50scb29Jk7stysDLzWGXEZ1h69wcxL9A1YWxX4iqBnnbgKnCAl23duJkUa0FRB5QY+dtjVJAdxnYYGPVKDrX1nJzxYBxhiocPBi5reQ6CylbqbHdLimGjSJ2ZM/7OXwx8oDsL+KSuqF6uaEHJwZFjCGBiMK8yWlf2t56KdlzkndbHTWp1ZGPF5cVyZ7KGLVd6TCOub6Qx0BfGNjSPYRYd1iz1eEmGP2KUOY0InEBNN5iK9nX83VHbOKmtlIGbNdFv/V03jmGN2sd8rlwuZUx5R2H5REaKH5Olo3h8xyHrRVPKLQeiqRUaJFLFuE2ai4gxAwDRsl5Je3V1VxQoyNM6RfQhB+wa54jBrG3UqPhRXesIf+62SKnAkQgORZww0AHiJpDJ3VvqI4oM2d4xXlgKyavWt8mGilau+7csFsNNB6h6UM64rdjBFPbeukfGFU/cYqY2DdPUMnLljS7UmUV44j5YaYx1Vy2YVHdclezGKVT5/hyk/qlqlaoFsEH00/J2OaYWxaBREA7d/Cu5MlPqSE3CAikcRMmHXpZiUcZwwwHtoQQdQUVUY52kPGLJNzgfE+wdnEbtufkACsYcWoOSEt3IodbxlbrBChb8ul1WHWceYQEmQ5KQBWdtkxKbogHKuf9vRY7zarDBgUK3N5x9uYWzwBNj7drNcIVaBjJl08v01Hp84D6X3ikPJ3//T87hnycGL49mrofE3uW++W+1pd/Bcwvn14qJwJQHserddoGzyPJ/3W4+vmvH2ZM84bHk9npqVnfvJ3aN1Yw/YjoJQL5WjfV8K0u0vZ+sPvpxW7r6XcN9fTTFwe8v9wVycrpRPu+1PTu3M+SvzXFNzeqy6L2XqYfHUxPgkCZtZq3y+B5yvzpxR2AIyKn/obi2DevKif9ns9GgFrIK/QKv/z+P2pohtOSJQAA -->
