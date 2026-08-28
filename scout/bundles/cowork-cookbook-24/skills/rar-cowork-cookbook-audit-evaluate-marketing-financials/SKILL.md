---
name: "rar-cowork-cookbook-audit-evaluate-marketing-financials"
description: "Audits evaluate marketing financials records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_evaluate_marketing_financials", "rar_sha256": "57d05e4296224e1337e02660fa6fd62192e9fe59e2ebe92d3db59f6113b8c92d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_evaluate_marketing_financials`. The original RAPP
agent is preserved byte-for-byte in `audit_evaluate_marketing_financials_agent.py` and in the RCI capsule.

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

Evaluate marketing financials Completeness Audit — Audits evaluate marketing financials records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-evaluate-marketing-financials
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_evaluate_marketing_financials_agent.py` and embedded as the fenced Python below (sha256 57d05e4296224e13…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_evaluate_marketing_financials_agent.py` first:

```bash
python3 audit_evaluate_marketing_financials_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_evaluate_marketing_financials_agent.py   # or on stdin
python3 audit_evaluate_marketing_financials_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Evaluate marketing financials Completeness Audit — Audits evaluate marketing financials records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-evaluate-marketing-financials
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_evaluate_marketing_financials',
    "version": '2.0.0',
    "display_name": 'Evaluate marketing financials Completeness Audit',
    "description": 'Audits evaluate marketing financials records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-evaluate-marketing-financials',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-evaluate-marketing-financials',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c35d469fb6b6014b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/analyze-marketing-operations/evaluate-marketing-financials'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/audit-evaluate-marketing-financials', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditEvaluateMarketingFinancials(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditEvaluateMarketingFinancials'
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
    print(AuditEvaluateMarketingFinancials().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/716+ZPixrbmv8Kr90Pbj+5CaIW+4YgRCAQCLUhCm9vR1pLaN7Qh4fH/Pimgqtvv2vddT0wMvRSSMk9+Z/vOyVT99mK3TVhUL59fFGDnE9ZO0ygE1cTOvcm6uBZVAn8UiQP/Tdwib6rIaZuiql8+vnigdquobKIih9Pp1ouaegI6O23tBkwyu0pAE+XBxI9yO3cjO60nFXCLyqsnflFBaVmZggbkoK7vy5VFGrnD434EZ4CJHdhRXjeTqk3BJ8eugTdxQ+Am9StcHvT2KKB++fzzLx9fIvj95fNvL25q1/UbnM0TDP+GZfsOBQpI7TyAI8sBGiCH1yWoIK4M3vKAP3le/VCD1P84+a//Sq52FdQ/fv6ST56fLy/jH7nNJ00IJk1h180I0C5tJ0qjZnid0OnVHkatm7bKoZKTGtovD14fM79JKsrJT+OzHx6LvAag+eHLSwEh2KN1v7z8OIEG+/JSteP311FK+cOPr2lxBdUPP36TU7dODNxmFAZRv359Xj/FwoHfhkb+fdWfoNSHHx3w5eU75cbPA/eoJ5z58hoXUf7DQ3BZFR0YTQl++PGvxN49lUZ182/J/fkhOAS2B3V6Av/x493Iv0ymT4XeZf71siV069/RBA5/W+7j5Gmov5J9t/9/E51GMIDfLf6n4v5swvSnyc9/qdu/mvBx4n95YUAadTA6nBR8nvz2VZE2658/eN9ufvjldyj6fxSjFG3l3iV8zew88kHdfP3684f6fvvDLz9/aEsYa8DOvrZV+mcy/8yu93X+YMHnqB/+OBeuf86TvLjmk/dIn/xWlP9R/f460ew08r7drz9Pvs+X8TOdjEq8LfowwXc5U0Os39nxx5ffIUdALqla9/4YZvl//ueEj9yqqAu/mShu0Y5EkzdRBkbwahjVE/h3zO0KQLvWETTscxyM/9HDI+LCn/z6v9w7U35yn0w5s0f2+frGhV/fufDrNy789XWiQtFFFQXwXjqRaUn6ktsByJtx2bICNag6SCjO0IBPkIo+jV8mUT759d+Q/vUu6LUcfr1Ta/TgKHm9H/mphnT6OuqohyB/auRC8gc9cFu4Rlq4EJAfQXL9CHWvi7SD/Dbao06iNJ14EeRxWASGu2xos8+jsF9//RVSdPglfxAqNnlUh3oGB7zDmXz6BDXz0ygImy85cMNi8uG33z9M/vfkX826Cx/XkCC5Pz0CEXKKKExghrUZHAadBd0L6ePukd9+f9oXislhOYP+i/wIPCbDCE2A92ZsZUd/Qgly4gBoZGjgrCyqe92KmtfJ3p+844WLjo9GHg8LWJU8UILcAzmsWU1oQ3XeLZkXzaSGYVj7w8dJW4P7qr861b2agQymut38OuHXEqwaRQr/G2HeB8HJRR5B87+HwuM+FFJ9qCerNxGvE2GMyUlpV3YZVvZzDd9++AVWi7fpULg9ycH1Sz6WSDCa6p4gD/PAQdAy7tOln0afjwUYsoFXv619H2OPtU2917jqS14/g9+uwL2mQyjDJGgjbywJ/3iGVB0Wberd7QeRjpKeXvCeXrnH4OZfNgzr75uEe02ffGlRZI5P/v/2GyNSmmXlDUurG2ayEVTZfFhwbIpGSz/6KFj274vds+VbK/BGJG98+iVPIxgO1fCPx8i73Z9jHhzVVnBxmZbv8iEqaMFR7j0mxxirqjGa7S/5G3F/hG6+sxR0C0xgGOBjXL0tOD59QxrCLB2vvxXxp51Gq8C4m5StAy0z8QHwHNtNIKpqzKun4WGAgjHHrmHkhn/QagKlwziA8icQxOgdSO530wkFVHN0TVVk34ZHo4MgCq91IVrYdYLXiQ5TYwyPGuYj7G/GMdAKH+6iJhmANoYQ3y1ch3b5ADM2qk+A9sjXEbh+b//no2+hfEcygocybc9uoCWvI7t6oH/49R3l01NQaDZGx33SH5391HTyfX35x5f8jvCd0GFOp2Np/s40E5hL2SMWR0qqIa1k4Bk+MA7uVfj1UUgflfody+d/6s1/+Hvt+700nv/ot8+TsGnK+vNs9ihnb9XsFWbIDEZIVIL6Udk+vWXdp/es+/Qt6/4g+mGpz5O/B+8PIp5R/Xkyf0VekfHRMXLBGLbPD7TG+tPK/ISPT7/kMvjmZrh8kUG+G60/wFL6Xl7ehsAaE1QgGAc/yk09VqkrLIx3foWO+JK/h8IzTSB958FYG+viu/S911no2Iff3ssAfJQ3cG1v7M0CMO5c0hF+DV4+522afnzJ7Qz8ezuWke1hvEJ7jFsdmDmw22kicL+CesEHkT1+/+POTLx/sdNHXNcNBGpXd3Z45smT9j6OrW4OmWXcVowl7UH/cDNkt2kzAm+GckT62MWMHdV7u/XPq94TGa7hFZ/HfP44GVvjj5P3Lvfj5G3fcd/M5S3ceP08dtijnnAo/PE+9n2z6YCXX/4ExrPh/gsQ0cglI/s81AXeN6K4O660G8iHZ/kIIRXuvZkYC2g93AvtP6sNF6zApYUV0xshf7PBN2jFA8/vd1Wax67yt5c3qnk679lBwuEwpz/VY82cwRCHC8LrRzDCZ/83veVTBGRH2NhAGQTlIQTA0SWJojiYYxgFEJQkEd8mfY9E50sULH1ALAEKHLBEPcxziKVPzueYs3DhNZT3iOqvY28QjbBQ23YXLjXHvSVlky7AEAdzwRydexQGEGKJ+YsFwMF3UxNIrk9dH7qNhnxvc0ebPFX+7cUhcThyh9d7+vFZz5aaTeKUI4TOlCL94BLPaltHCFIxaDFuj+oFqM6ezhjFKbe1cT6vM64pM5kz9TNeRQztFyff3U8Hg9xtl1itcseGCvZOuUeapAA7YnbwqDktBtkKWZhWLtiLDYpx86NysapleiDiXuL4BSIOU9RSzEtyahtUy7yhqJYLr+uWpZDhNTlXImWrxJqzNYvUUJOFOk8tizla6NRVDlc1tgfiZqhbzUL3ujvMlTTrN+4FYxAQ1wsgHaOFlx+H6dSSfclIqen2eDBYfLcVFVmPBV8r0/WAlm1zKbDzUdykMaqxt9m6ubYKOefOis90B+sw4Gg8RTZzd9hg+IFrZE5Tutrfpajtygxns7y+zbbUJtlezyUXqCLfxINxINnqAKQ61lb2Ns6PUXuyL2QboSbBdhbuVLGPdJq6ZQnWOc1rJzlrLNhSO54unbW1Y6Vjxqrl+sQWUi4rhFnrByo+X9HO56/K1qKSGg3oXZaiIrzp8GtiEHcX9uiopZNs28GfBzmC0UF66pw4LCXNXcyjRD5TWSHFMY4ETahf4eALc6ix7qjYW7GyL7wZLkzk3JKUQPqJfUvNfdwolxNTMuxmSfRnl0KZXuq1ruoRkyL6Yo9t93XGaEuCqm68WZwhnfNVOBVj1lqoqol29WLY1WJTqXOT81R9leLZAu0Eodb0lo1WGN7Y3GmPmtNhO/WCok7odbYXwXahzWNpZhJ7IxCNlj8qSm0NJ7Ek1lRq3qpLypArhpuRu+ZyVS1NA9XW50gzNFNnO+wNogh2+qlYEoQc8DD/6sGeWdl86imasx8wsx9yIwV0BPhdG878NehjQo3s9b5Rl4FiiNZythCkWglI4YiohaH3nmMk2TAtqS0gTZVzm8Nthp6jw8xQLn3pZvKi5IUhRhiWZ8x0hQ82vWPKhO3xLrTIdb1E6lIRTzMSoYqDs6CGIuOtk5HtKm1zdNkM5wP2Eh+kI8GejToVUJ5crVerC1cDZxUEgEtFVbrcdrvIZKudS+Eau5rPHA25LSiynxXRQiKP7G6+q2KKVXGl58wYz/VZlV88Oe07IGNTIQ4cIO/JYYvJ1EwfYlRpIrqYIbNjqy6mxaUTNMuPTxtGsIZZjCny3FCyhaUI+Lw8nqPF+hwZeEpQIU7ZNbkSsXm2itcbYqOfNQ2X+zWDamKrEMpal3AK7TaFLHpUtp1lIC6iq+fL54OGk4Z64HcLz96h3sERs8SJ57dzbu/ry8EdCNMmmhyIXE4yG3JeXApFlDuSjY9yM0tPnAlZZe9O1cDGL0vRvV42RH0KrI5cGx3Q9vZpBo4HuZQPxOY4X8/SG2MiWiO2hiD6IBzsMllzIrqyh2QjLvmLb9/4s1gTaX9A5FumZZaroLeUo2+awWmhQjQqb62A1bBCcLAr3rmlZKEjmMPfimViB5imkEaPq4O/MSVaVA83LUyFjhboFm8XvnLw5npjL69sAXJ1OaX85Vq4TtuE3wkigZ14gR+CiGsc/dRP6RgfZKZqT71Pwi4Vo6+iwdTWlad6OYiOOJYxZ28Vc4Nfo8up2cQbayco5doa8pggWLm0iX17O4D1bV/P0PXi5A5bcYXTnnzW6mS4TGlmO2tiOQT66UbvlSTZ2O50s9PUkuvWzjnbEdd5wOFokbvynpFLPd11a5FtMKverM7haS1uFrfTOd5mlbT2p6I4W5qnc+2zTl8VjeEEgjrrpsYZWMh5UVKS2GHN4He7uj/p3GpXXxpehqk1BRrHyQvH2xrZVeJWA3e4VQjGLyQDzWiUxXa1ge55IUd7zS/T62zaFoXf07MWlsLBK3bRNjgLGHfRnKFWNwldoNxWYb1icSqCA51cCL3OkluwukaIcL6pweFyneLrbdGgjHDS9n1N4heXLXfZztik55RRGtpeWQgTsAp7XRn+enoONNk2dtrKdZt6erlGZzk4wkyaGvH0eCJuWIbOKN0BybnccY5EIRRf+ptupanJZbHFETvBnMvNTgfrhhYVHLTjLos5fjXJcqnsaHqT2GUjGXzdFT7jxysBvzSZoKpNYM6LXKiVGeCiw23bbdHOKSx3Ie5icx76h312MEvZsgudNAaMRcmconE56WQyd+ZSH3JKH5vtJpNuypp37WyeHSjy4kvh1CyD2Xq72arVUevnFzsqJDFQ0EGeH0u7NAMi6kOgIcdGAUFGc61/1I/2TE73+4AIzI2+nnfYYudB8Me1OfPom3U406t14g10HcgJm6KypPNOJQkJDiD50Be9SFfpnijqAxV1JrYTHcjlMr231xe928Nug0D7k+W4MHKXMa2o+3kehx06Z9gg4f1bdmiRHXlql6jFnFlmlleZepaipECqfo8umZ1HHrL0UtuFSQmzwk7PiZHzFFsggcfudDaGBHnsGMmK3bTQLyjjI+R+ADEvw50shm43c5h4K1aKCvoie4fC3VyTyzVGA/24KpZKrXMyx7OHIosi2bHXwZxxyut8mlPyjTwthbWesCxTLd1bbNLSskRvgyjHFn4J9oEsKAip1jvKPkFLE8fFtgwlX42lBQHamvLNTXZwwlkUV8qiipuNK8k2lmV5hWOYLlVzz9q1FtUSC51LPO0oNgGAhUiKoz5YLbFKN8LNlc4OBQ0RYM0NQbRif1hIeEBq2yDT6Dinz50RTt0zJdysoNowmaRQpifAYpns7CO7gaVG2+1Tvsz2l7x1E+mKWkLnmIaYGdERtnBHhhNJbXNgXGK1Dz3xFCmRdgFinCpNWpjH+tRU3I5XtOFy5BSripeblby2Njm54vfbqLxQKbCUFTNVaFe4Jb1HNHKxEaT52k6gXUJHWyp7tgfdmt7yirpkptvdjrbJFRrAeqO17qpDfSJvDYrpaqfA2xuPHKRt4uwziWIXoYW2VsiZmZ4ssDbUlvIg89bSWm+OrLrj0UXromDNbVNExbOI76SMYyAfeSmsD3OOGDrCK8omP7HLHvQW6TmbOlsmqmb1LhWh5zDzL+oFA3x368smgbh32Rq/bitz7/I6VmWrwJr2Ymn4i05PFKA7Kt1QxzNJ8ZSlULUBO+NS5bb+XmId/MaoOa8MxFbIJRNlo4ycBVq+sZSbocslX0fKYl0ny7mWiMntQpciepoaGIKUels35emgKGAWDuh8H57snvbalegq2bU8LlUpV90Su904HAgGJadbMjGq8kpWjg9IoZmhZR1U88N2VuDgNFCOd03zm8jESo7GIrNjuFNBDaEjRBlyEa5ca7JSc0yn7lZdmkbXy7ZyRi6+aJgmPa/TNaBl/pYil9ia4fhxh+mXiwLr5maAHWi2D07hKVPLrX3Zu8ezeeS4yF9bfImExsGlG+dUn7khay6Ltg5FkjsnpA23GDM7FbaMsMeMyKArZVtUlFSu2CnNK2UjhILPd77g7c6CZU77/eaMXE0vZtADyxx9nFc39tC7qFZ72rK68pbOMfb2dgibITyrcxh/3bQP6et+m2foftfDbnuD7ffWtbKEK+6cNx1+QY7hDk/16zVkkWsvHtt+a5PcRlYM000NpSZPR4Nri/O0vQzN1Tv0Q2unKix6Q6rPnX4bpdkU9445yYHdxVYb5SrUNhOcg3NJHciq46lrWetGI7qstpkSnLKoUQqaTTL3yLXCLzyNHjQbOdOk2juWxyPTohFq0hGJ2WyLQQcsqt1Nr91mr9uptwyGNb6Uku7ArRZ753ymLaLRu2Z1PGHC3KtkpYFdqoBepJz0QSvJ7bRaquZCmB5aQu4iRLoNuAEaMJtj8xXhM6mDUQ2/W9+a8Jqftt6K65TObGWrvB14D0G2tbO9+vJ1lRXLoBKHJbJfkkfc8jBnyiAiUV4zXZYDxGkrsbYRAcvEuNnGJx3fl4nhLDoyZeldakR4j9OqSrViOZcPLIqteoNYTM/5wFNYSPRx1YnKAtUMXQxMWYZNG4kmWh9P21NCrfU945XTlJvyxr679tPpDFcWuIHbGppjy24WO8FJyoWNv6gwr8Cw025bhJKB10tPj9Qrj2z5U58YZSkeKmaZd9mmLpNNgDorvDuVna07urgJy2QRLArVZa+nfO9nt5y7IWm08W98tQ3MRj7oFw1d7mSc3UjEzV7T+M1rrVu2A2cecELkFcpZP2mz4dqg5jUm5ycmTSkw5c75bBfcMOOkTZPTbkEoyHBdDxSlVMkxmwFLT/iDBmMGs+cSay1buE899ki9RYQb4qjqeengpLAamuOMt2c7f2kulnIQT1cufgv0cxC1fVg2C5ZDJAf1E4/vd8jyOEf7LeyM9STQiZx3dremO14XwuHiEXMsIPYI2VOb23QK+hYbWMc80t5Wy5YKZ9b1zJwrZUDRZs4nZKTVF07fU6D2B8KZIyHcrbh7ZAbCdmCV41o9oJuNz0iKBFi33dJXY5Wf+pbAmGTYhgLZ6ed2Qd6i3XWXJcgFXROIrOWHWM2nDbW8UTOJ7pkpzh6U67AWsvhIqtv8Km9DRhNmGn7Y0j2qX+d0P81ddQhBvre8fkFO1zV+amX35vBeo3lYj/WWU3P5FlXjorQylx3QMwY37YZEg4WinPfVDV+5+hKkhR+KbeUQBxtzmj6V9ic8uQFmbZPHqxdzV7g03Jzi+76oDdrIKUjQt7VxKLqtCdDNijCPqzrJnezmHsV2ThpTQxfEeWo208OqMEkNddn4QpCBh/O7AO5BEGbF+fNNkJJyM3jsaktPw8vslJwRe6+4eTFzYX/OlnnDOFveX1EnHItosPG69sDQ7kwXnBnskyLds5aeYeRiNzvSqr1nZt3CFdPTAl+BtZUaJ2CzlT9T2SU/IMsmwzMGlczp0tg1hc7mPrVg/RnsyUROxSSvz+YNJ0lhJCUG2BzMgJUOOls7GXBvC1qUSy3EYxlhNKpDI9L1rRlse2h+ne4NDVssBZEJkrgxdUTwpgO7VG4OctYd4dR5q2PlKGwhdGYUSeJptTsRzfTEkAFhKuEqmR9X8wvOZ+eKAsCQShJdzAHaUrCpP/TsitZv03B6S1GgFxtvx+DE4UKWazBVPeJK0CuLD40VUijJtb+58aU7rEDYKDxJ32RUVwJzqjn6TCmIIxi0i5i3ZzGu+EOXod153gXUkuzpdNA95HLtFpbNHHdc2TawPoa3gaobW5QxRzxn6t4J4NY1D9eE0B8PTtENR/qyI7nFMkFjyohgMHt8u8KvTEOwjIUGzSFey14hr6/IMD3j6wVZ8kM8MLkwE1bxoqGq3JJOFqbcEDIXKkuSuytzwylrja8TmqZ/+unl48t4jvo8xv47L6fHw8H/Z2eUj+PEt1da98NkYHuf72t9/luofvn4UrkRxPQ4ja3TNngeXP63s9hP/8bbkFHA8HjrO75/65u3Y//GDsbfXXqJcg82TNXwtS7S9n4g/PHFaevxtyjq8RdtXPjz5a5aVo4n4fc1x9NxuOEFZfO1KZ7qvIy/4TC+UgJeBNE8L4Pn4fTHF2+ALorc+itGEl9BVY56Pt+tjAe648uVl9//D+MyftARJgAA -->
