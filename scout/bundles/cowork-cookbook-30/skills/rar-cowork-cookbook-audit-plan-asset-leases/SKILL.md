---
name: "rar-cowork-cookbook-audit-plan-asset-leases"
description: "Audits plan asset leases records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_plan_asset_leases", "rar_sha256": "4f430a7d962a075d93604ed97bbe649eb12413e0ec015944225e028b0b610914", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_plan_asset_leases`. The original RAPP
agent is preserved byte-for-byte in `audit_plan_asset_leases_agent.py` and in the RCI capsule.

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

Plan asset leases Completeness Audit — Audits plan asset leases records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-plan-asset-leases
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_plan_asset_leases_agent.py` and embedded as the fenced Python below (sha256 4f430a7d962a075d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_plan_asset_leases_agent.py` first:

```bash
python3 audit_plan_asset_leases_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_plan_asset_leases_agent.py   # or on stdin
python3 audit_plan_asset_leases_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan asset leases Completeness Audit — Audits plan asset leases records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-plan-asset-leases
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_plan_asset_leases',
    "version": '2.0.0',
    "display_name": 'Plan asset leases Completeness Audit',
    "description": 'Audits plan asset leases records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-plan-asset-leases',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-plan-asset-leases',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1886312d97607e39',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/acquire-assets/plan-asset-leases'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/audit-plan-asset-leases', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditPlanAssetLeases(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditPlanAssetLeases'
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
    print(AuditPlanAssetLeases().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/7V6+fPaxrbnv8J83w9OHra1b76VqhECISSEQCCBFKccLa0F7Tsik/99WoDt5N3k3XerZuQFpO4++/mc0y1+e3O6Nirqt09vR+Dks7WTpnEE6pmT+zOhGIo6gR9F4sJ/M6/I2zp2u7aom7f3bz5ovDou27jI4XK+8+O2mZUppOI0DWhnKXAa0Mxq4BW138yCooYUsjIFLchB0zxYlEUae+PzeezkHpg5oRPnTTuruxR8cCEFf+ZFwEuaj5AluDkTgebt08+/vH+L4fe3T7+9eSlk+FWEPRSAn/hvH+zhIvgghKPlCBXN4X0JaihLBh/5IJi97n5oQBq8n/3nfyaDU4fNj58+57PX9flt+qN3+ayNwKwtnKadhHJKx43TuB0/zvh0cMZJ07arc6jYrIF2ysOPz5XfKRXl7Kdp7Icnk48haH/4/FZAEZzJip/ffpxBI31+q7vp+8eJSvnDjx/TYgD1Dz9+p9N07hV47UQMSv3xy+v+RRZO/D41Dh5cf4JUn/5ywee3Pyg3XU+5Jz3hyreP1yLOf3gSLuuiB/nklx9+/DuyD++kcdP+j+j+/CQcAceHOr0E//H9w8i/zOYvhb7R/Hu2U6D9O5rA6V/ZvZ+9DPV3tB/2/y+k0xgG7TeL/yW5v1ow/2n289/q9t8teD8LPr8tQRr3MDrcFHya/fbluF8JP7/zvz9898vvkPS/JHMsutp7UPiSOXkcgKb98uXnd83j8btffn7XlTDWgJN96er0r2j+lV0ffP5kwdesH/68FvI38iQvhnz2LdJnvxXl/6p//zgznTT2vz9vPs3+mC/TNZ9NSnxl+jTBH3KmgbL+wY4/vv0OcQHiR915j2GY5f/xHzM19uqiKYJ2dvSKbgKXvI0zMAl/iuJmBv9OuV0DaNcmhoZ9zYPxP3l4krgIZr/+b++BiB+8FyIizoQ4j2D48sC8L0/M+/Xj7ATJFXUcxrmTznR+v/+cOyHI24lVWYMG1D0EEXdswQcIPx+mL7M4n/36NxS/PBZ/LMdfH7AZP7FIFzYTDjUQKj9OupwjkL8k9yAMgxvwOkg3LTwoRBBD4HwPdWyKtIc4NundJHGazvwYYjQE9fFBG9rm00Ts119/hfAbfc6fwEnMnmjfIHDCN3FmHz5AbYI0DqP2cw68qJi9++33d7P/M/vvVj2ITzz2UMeX5aGE8lHbzWAmdRmcBp0C3Qhh4mH5335/2RSSyWF5gn6Kgxg8F8NITID/1cBHif+AU/TMBdCw0KhZWdQtRONZ3H6cbYLZN3kh02lowuuogBXHByXIfZDDetRGDlTnmyXzop01MNyaYHw/6xrw4PqrWz8qFchgSjvtrzNV2MPqUKTwv0nMxyS4uMhjaP5v7n8+h0Tqd81s8ZXEx9luir1Z6dROGdXOi0fgPP0Cq8LX5ZC4M8vB8Dmfyh+YTPVIhKd54CRoGe/l0g+Tz6fiCrPeb77yfsxxphp2etSy+nPevILcqcGjXkNRxlnYxf4E/f94hVQTFV3qP+wHJZ0ovbzgv7zyiMH9PzUAwh+L/qNGzz53OIqRs///PcMkEb9e66s1f1otZ6vdSbeelpqamcmiz/4HlvEHs0dWfC/tX4HhKz5+ztMYur0e//Gc+bDva84Tc7oaMtd5/UEfSgUtNdF9xN4US3U9Ra3zOf8KxO+hOx+oA80PExUG8hQ/XxlOo18ljWA2Tvffi/LLTpNVYHzNys6FlpkFAPiu4yVQqnrKn5exYSCCKZeGKPaiP2k1g9ShvyH9GRRi8ggE64fpdgVUE6ZOUBfZ9+nx5CAohd95UFrYLYKPszNMgSkMGph3sF+Z5kArvHuQmmUA2hiK+M3CTeSUT2GmBvMloDPhbwyGP9r/NfQ9ZB+STMJDmo7vtNCSw4ScPrg9/fpNypenINFsio7Hoj87+6Xp7I/14h+f84eE38Aa5m46ldo/mGYGcyZ7xuIEPQ2Ejwy8wgfGwaOqfnwWxmfl/SbLp3/qqX/499ruR6kz/uy3T7OobcvmE4I8y9PX6vQRZggCIyQuQfOsVB+mTPvwyLQPz0z7E7mndT7N/j2R/kTiFcmfZthH9CM6DW1jD0yh+rqgBYQPC+sDOY1+znXw3bWQfZFBLJssPsLS+K10fJ0C60dYg3Ca/CwlzVSBBlj0HtgJjf85/+b+V2pAaM7Dqe41xR9S9lFDoTOfvvoG8XAobyFvf+qvQjDtONJJ/Aa8fcq7NH3/ljsZ+PudxoTeMC6hDaZtCcwQ2KW0MXjcQV3gQOxM3/+8c9IeX5z0Gb9NC4Vz6gcKvPLhBW/vpxY1hwgybQemEvWEc7iJcbq0nYRtx3KS7rn7mDqhb23SP3N9JCzk4Refprx9/0Dh97Nv3en72df9wmPjlXdww/Tz1BlPesKp8OPb3G+bQRe8/fIXYrwa5b8RIp4wY0KZp7rA/w4ID2eVTgtxz9C3UKTCezQHU0Fsxkfh/Ge1IcMaVB2sgP4k8ncbfBeteMrz+0OV9rkb/O3tK6S8nPfq/OB0mLsfmqkGIjCsIUN4/wxAOPY/7QlfyyDyweYEriMDkkAdxudo3EEZyucIGiWBzzGuC2iSAy6GkxgBUOChGMWRJI5TAMVZF3VpDOUwEtJ7Ru+Xqb7Hkyi443isx2AkpOLQHiBQl/AAhmM+AwlRHBGwLIA8vi9NIHC+9HvqMxnvW3s62eGl5m9vLk3CmRLZbPjnJSCc6dDU1tUX7pyhg0I8sSzPWJ61TSgNa9UoXrtVtDgmDG/s3Gh1xqt9Rq1S9IilZIk7SkQL8lyXuWuXd7gpc/Fx2C7n4aHAW+ZKcXU7p0ZxZVxtJm+i5fGcnreXVVbXy7DeYefOSY3CYc0ymacOsq/v2zl9Ev0LCKr9Ec30c70qrmhH2efzMVZyzXdb7L61WkO4JKl/FmvLLr2TDcJkk6K1L9drkluXJBtcqAHZ5xiFFAYZIO5I1q3Vi0MtCRTf6M5YwQ0YGpzPNV1f8KI0zFwpPaJau3cD31Hn9morruHQF72s2wPj38qLarbZYplwzm7w0Et581UpHsoB1zHJavLdIXSLce1JaywpzEDBIjW6Hdu0FshtYgflzmAu9qXx64M1xziloy8Qo1JQWcravybhdXO/9WkqKGchM7dnk17aFL85q6mInyN9mxx3eOfXeT8KIo+f6U078Au7qIey2Mq5DA513ZyUVO59O8GyIcDshNzu29OmEtt5J58zrlkrJdsray5ZsqquHtfDxber3bm5WK3C+rLj0PbukCk1c6RpUHl5iizwlXvuNra9kanFae2MaaW69Pa+wdZtfqMsxr0VB0Lme1bO5p6LseF1FK/8OcVJ70olN5BYjM3lSZfel/Upmsdm5l4lAbncXMOkCeXabwOeycyrEZ59IVgLe8ZR75qEbrXIPptkz7osCSoppEjuFlkunmnyIFC5S6/NU8paIJxbRGD0u5tbdcq9C+7mZp7ty7t6lqNFjhxSd3M/GiustGPYSd12F+OGVadcvKuX3qKj7XDp28t2CPZkGFjauTxFJlUG7B4tuZ1EoARyas76za9sbOFdzlRSG/npzEieUDbOxTdxGH0J29VKJfROvl34rnhrSfdm3apzwoli7S9YgTaLs8mWmrXBNFvekPZql2/KGFfU0jkLg7lzGG2nRv5wOcD+tjNkYZUl6NGLd40u6KJdqNFaz1V9baamgdv5osiusdn01MqO/GCkVNZDcXVvb4SVK6/H5W2XhozKUYwv6Us0QshLlm09qknQJdEOixJgFnW6VHRwp1G4FfBVbu337Nwf+tS5pJnXR8O1XjSWX/aWmnGbay+urjLYYZ4O+E6XWRtA9NGyqstO/qLmI+SY61FnYmtTOMZjW1SALrSFmVkWEQHu4i3lvca1AnqqsNHygoA6wIxEL3llGHOaU5rxHGmZ76Q5V8lr0TSyXgyTXZDRLp8wy4WydiW5Kknd3bTneGcK3cIs1XDJLe90vrjVi5qoMCllqC2YbyiaMBbzrUQMIJQWA7cvJLAMWSI9rIm9eU+3QX8gSWu+ZfM2XLWLVdi7FIQRTVnT9qkVWvlIkUzWtCKlp4K1dvHKurEnaUWFRHPeeOQKt/cSW55zw94GGRd7tEfW1c1LyQDjBsSScml3tTN5wPtwpXckEIJIcXeYjzIRbe2la8aYgFtchr3R4eGwb3xRW+w0b136drE5SGWYn69FeqITbhjkFWklB5JYuqEQrot9srjsXTEKhshV7ywImdBoSHenjtaAUHSTbzOtsxPRoFiU2W5aRCPNrgBJQWrHQm1QkUf4wFrtNmhCrTGBsDZHh5SCYdBsrm/wzPbMEV9Fm/lYxCZWMNKxkMiqGiGoQ+waqhVfLULSKaU0jhdyu90Kdqdpd4fiSzEb6+MtpJvqimljY7O9rcbzi0rJGNefZDzI7uLcX60yc++czIQIqN7cpOutOb/obm4XxJJP0Wtx9sMAwcOFmXv+gDhRuCVyFGURpIfuZrb7fZ+TwzGoBnbOFki0NKyuDvYydj+SC3mzAcr5tLjb3tiSBW843FnLsJHfpax0x+6wJ7EkgVyYxP623BqpebV3J8PexXtV6w5VVGapGzP6aaPhRrJzIo0XaaupxjbbKfyCWZWEQS2Pwpxej4kuSXsI1uRtJeY20iy6Nc8knZrwPiGxKCmw5x5ru80Gd87WLh3qs4NQ40ZyGbKlJTUIbiJT74UAuKxXnkSxu5XD6baI4y2WJSwHyrHE0cM5u7RMrBg3o1zJ5Y7fF7aa1LsKlubA1TRmdOPl8YCygXlCrpYjYLyt0Vqe84eTgDVEmntu51RLl2GW3ClCDUUb8V20vBqweF6EKI92gZPta+dQSV52kU4kOp5RZSHAtCuVWxripCybt0VyZkxCMHpk20T+ammTHcWTrZQQx0XiYgtc346qk7Dsyk2bOD+1tLf2j/Pj6dh5BY8hhiompV2JQmYlF+XEZ1kf4qPrY7t5M5Zjk4QRfwGryquUpCJckzqOl8X1pm8dnzeSbcbdxVsWXlhm6RSR1+WOze3OF2xYBI5ZOkxWLYJTwHalVWrbxL0eYKcTe/e7fJyHFWWg/KZ3UsWAAnNabOTFYORKV91MvyAuikh1zHaVR5Qb3hxecZPldsWoa2Qhp2qdHA9OaeBHSczMGudDWYtkgWWkjiFQCcdl5+BXzr6691wcz5usK/Vul+/3hqwLa6EZ8fVtQIFBp22VHvJjmRdnBPGD+sjNNXV1S2lP5hl0c6XzkNDQc7uSKazzmFxEvXk/4gPT29lN1PdSgqxp4txKC7/U53yoVGvA3FL0MBYbcbVo0fvu7p8rw1u6jjSqhXGjlhaZSiPZ59TaNQILTw/XgzF4CTrqTlH3OhZvhJgweT9LF7vTCaaCVyZdnt8jNGMjbN2v9iR61qRDuUftvOIPu1JYmcYxOp1QKzdZe7EAmdjtVLFKEAXo46lVg3toDfoGpQ6MrjbYTh9rQjGHHtWXkSNukfNiNbfDo6HurBDxjAPXVkssW9Hshj9FQc5uuWrN8RtLWvEkFZ3ReLlsCKU+IPiau2tF3AGfFY5LKGmdNAvpIGvEljmaYne6R8xKwlZz455iwDo0pRqcCoEGtrDYUClaKvg5O9h4ckthEcAUBgYujlZs3u2sWl1f1dGo7kvRFzZ4PZ5rebAdU6BRHldRImJF61yfTHnjj6q3n+OckO7XdX4TDipBEq5SzbW+c/FTd2i2ZwXZlNraTuz5db6m2k1/UFjL2/Tz9XkNijQZFUe+nNR8l2bzo6bqqU7Fyq6MNK1ScD/Z08vILsQjgeqsh4jooWUcVwiN1eqGCxBNrKRAWZ4oltllkbRqRVvIKefMC7nz5SsycC6itod47gLCJgiiq7uRNnxLYZQOoRNpkHuH4GgVr4cgM8DKHYahMb1rfUzDRnGKtR/J22iDN9JiS2oBE7qwqxWPQDqJS0rgtS7ZnAZBjrx5qtr7sNdIx9ZK7lCAldXf+biI9cVaCTldp47VpUv0m6mKnNxsM2/nyQcBr4/xMY9Bp43IaFFRVMroQIxLdgeYFY9djEGxDScqYSWIdyxvRScnX18i1eEqWpGZgV7Gg1rKMUo3S0aRz/E8bI69vSPJTpLvIoU47FI6VRctUtHCBYXJL414IPbWLdzwyzvnpks9vp8SfLPxQiNGPbCmFltqM08Hfb7bFxu5QLS0aardHtOuTgLbiohP93HjVEzJ56fohJ3u+k4XOjfNEMsdU9zx6au+uN89URR2Ir/kWvlMk6rnLMPDYEQM7yuwrbXQubjFruqyqQKQLIxzxywUdKfCRNSW5lxwloKPGzxtbk20vyVs0boNe5dVN+vHwxF0+WWVAMZW7ncm0kURX2VikOwFCF31hseyG8Mm0vwq5aF/Ehifkakdpe2XzAqVWvyC4RxzPrHqaFZCgjCjpbmm5Ok+F3mXgdK42A9Ca+23YMMsYNuQuuu5gjrUCa/O9oXNsqvgMhq1PJHWEVvPt+hmX+LENqeQ4W4X+m3ADsrVLdtgmRK7bkNvm1zWVKSQl4OaFw1K85IWeFTM8lnN9fENCxXRP19z9R5xsjr4Xb9sQ2nJMSMRz7G4LGj+7CeEx5xwekBASDLhWfS4ap7e5vtA6Ad6ZBHyxlXdbcjrAKFT5HoJD4t+JyLhhZuHJ1f1FUWg52bZVrrKxP0NiBtB38Z1lwnbC4as8lL10PX1IC4Lbk8vCDs5qsBCGv24oE/A2ReaYDNmEkj9Wdss7iRF3NWbmshXofbo9fUOG+PWOVpCl7LtncjW2sEuLG/sV3ehpnVsrZxHZrUd/KKvw21tBPgdj0hmLJTodrVEAsBopHAMv2xO+LJD78fzclX7K2JNaYrO+aS03N6alkp2GOo6pxUnOY7I3f0t2637S443QF45e+2QYfeFivOili1bjhNv6N7vAtTf6RLKKRh+EBOq173wchGTtnZxM2Uahbu0wugO3MryPf+u9dd7l/b+cNL1G8cec4oThV7wOpNaHVpK2FyNQ5uM4LbeYXdESgvDkMJhQWflHHa9Ri/WFaiLg85a8ypqlvexbnhMdRa7fsfq2WIj9yAdszra5xIR7uVlabbiXUkStrL3fTZ4sJcLw2u2J0J7u10VF6vY49kNk1cLMsbEIOV43doDMVQv1oViBts4rpjlvLn0PXnTjFs5Z7dNg90xwpW8Uuw2OHcpNW2UMj9xtrrvlTji3QBzPh6BCJDDdtWPts1s+7pS5iecoynPDeKNd6DA9WKR28asF+g+XRoouZ73MW9JJifZTI6yS7TPas+EzXoyiAOuSQCj2b3NlyPRN8ztdD9TBb7z4gFb5LpqD/4uvXOSewvlRuI3RUfznsJtZVq+r9hQ29yQaO1jmLil9hHJyTaPm4G5IoqU7NrOZ9UW4dddf+mChScR1/4SMCriWhxGnDKWFTkmikkR6SBC6yTwdEQHEYfksDS2CKte3IIoidPStDQqvepdvAfHql0jBM0jc0FQAdo3DuzZ79xG3W5ssNHYjQF4DRjZ3rp2EnsfWQ20xtyqT2lWNlev9VrkKqfrEGZNqgQix3H+yEZG0luaavhZdQTU1UMNaVcVVhbk9/Ko3aJNujPnki+UhYly4Z4Kzdt2pZ2MJvc3oSiqEUG6sdqdXLc/Hf0jiBKzqw7e6qjUdS/c5vk146WIZPdJ1t6Hti8kh/R4vvM2l5FCBccaKF+vgo07B05sp0tNUnRZuNJGW+yUJabQLV5Qitq4TnkzOdXs3G2xRDqyEYEwAgEWJqwr5rrgXraxJiLN0BLxfVGmcx3z5zBBDtIGZm8rpJwZ3c6YjahjXCAxds8BDnAk4T2mLoedx3csoVuV16tL6bhbWpGlBIEAucjKoUuag3u9zE3vog9XSfWiMeoqe06CZQEQ3WsNl1e0OOF5/qef3t6/TWekr2Ppf/XyeDr4+392/vg8Kvz6KupxOAwc/9OD16d/Kckv799qL4ZyPE9Um7QLXweR/+U89cPfvLmYFo3Pt6/T+7Fb+/WIvnXC6fdBb3Hud01bj1+aIu0eB7nv39yumX610Ew/bPHg59tDhaycTrAffKZP73F2/KUtvvhxUxYNeJt+UjC98wF+7LRfb8PXqfL7N3+E9o+95gtBU19AXU7KvV6ETKey05uQt9//L84ImNFqJQAA -->
