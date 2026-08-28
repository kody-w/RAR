---
name: "rar-cowork-cookbook-audit-write-off-bad-debt"
description: "Audits write off bad debt records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_write_off_bad_debt", "rar_sha256": "36b438ddff41bee18987cbea2d549bd3bd82d7fe52f80be260e555df9f52aec8", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_write_off_bad_debt`. The original RAPP
agent is preserved byte-for-byte in `audit_write_off_bad_debt_agent.py` and in the RCI capsule.

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

Write off bad debt Completeness Audit — Audits write off bad debt records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-write-off-bad-debt
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_write_off_bad_debt_agent.py` and embedded as the fenced Python below (sha256 36b438ddff41bee1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_write_off_bad_debt_agent.py` first:

```bash
python3 audit_write_off_bad_debt_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_write_off_bad_debt_agent.py   # or on stdin
python3 audit_write_off_bad_debt_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Write off bad debt Completeness Audit — Audits write off bad debt records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-write-off-bad-debt
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_write_off_bad_debt',
    "version": '2.0.1',
    "display_name": 'Write off bad debt Completeness Audit',
    "description": 'Audits write off bad debt records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-write-off-bad-debt',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-write-off-bad-debt',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'fc3771795ac91f18',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-accounts-receivable/write-off-bad-debt'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/audit-write-off-bad-debt', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AuditWriteOffBadDebt(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditWriteOffBadDebt'
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
    print(AuditWriteOffBadDebt().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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PoxoB8+lPMzA+MqJlYZYhZqV20WHjljhCIS8lFVx1E9LsQtCOboIbbf1xiXqXQ6Ocg96I5l2iqA4g+o4jbntriLTlioLB7qOKIdkunftkroPramppj24miXhzl7okeMlupeyYq7RrAezsrINOvu6SepECq2kJlZJh7f7gr1vkK0vBKgeeoTdjYctPYU+7AXljbHk9KpoiOoyhLEx7oski0WMvKvYkqJ93Lt1PYPzwV7pYRylkJGsb8WaIO/NUmKHIyxJ1DEZcGK9COUtCV9xPbPhyR2Wm0bjMLEe3LHh7vLOp06G7cH9socpxbLg6ujKd+larGz3opY2r1C87tOKr+dHK1H27fbOKT7gTivRMjD5JG7ndnCyybiwktxMdNg7vFoxdKSnncVRupevzr6gtXa9yVFE0o5ahFX7i5q2t2nY9omOiJav7mE1C08LNUQP1f00jFft0K1WuHfMMY5EkaWdNcSOR0U2ck+Bt7X7o75T7iElZSc3RZXFhlnjhL61+N09YpBLHp7u8JavjQueLdG7vpXqa3k/CYMbnLvsWOl6c2vYWpluos/lQXY0i30VLwcP8ytaCDJ/yq0LondRF6VDYVJH/kwQQYtOR5XsG94RUnnQxLWmVgFnUUaX3RaVutujGlGU/R71D6FtIQiy78JrKS9vByNbh1Z9qpzdgdYSyg4blD8LCBdqug0jQuIWZ8kF87rIrcqCqHAlKtbctLyQq4wTVZp++/A230R93bf+l98wz3cG/5/doHzeS/z6bdXj9rFve58euj79a1N++fDWuDEw5HnTtc368HWr8r/ccv34V99uzLum55e085doY/f1Nn5nh/MPid7iwuvbrpm+tGXWP272fnhz+nb+eUM7/wLGBc9vDyfyapb2UASey8bzmy9d+cW12+ht/tnB/J2Q78V257/ehq+bzh/evAmgH7vtl+WK+OI31ezY63sS4A/2jryjb7//XzoFU2KPJQAA -->
