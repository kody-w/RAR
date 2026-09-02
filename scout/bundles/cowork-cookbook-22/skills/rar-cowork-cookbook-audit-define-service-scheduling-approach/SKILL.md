---
name: "rar-cowork-cookbook-audit-define-service-scheduling-approach"
description: "Audits define service scheduling approach records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_define_service_scheduling_approach", "rar_sha256": "e121d686bc91c6beb93413269ef06564e63b3602b070cb13525c6f863568045c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_define_service_scheduling_approach_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-define-service-scheduling-approach:ca291afb2b0c1771c52ec56b6bfe96991a1a10c49db8be2d418e678f12d1dee7", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_define_service_scheduling_approach`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_define_service_scheduling_approach_agent.py` is
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

Define service scheduling approach Completeness Audit — Audits define service scheduling approach records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-define-service-scheduling-approach
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_define_service_scheduling_approach_agent.py` and embedded as the fenced Python below (sha256 e121d686bc91c6be…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_define_service_scheduling_approach_agent.py` first:

```bash
python3 audit_define_service_scheduling_approach_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_define_service_scheduling_approach_agent.py   # or on stdin
python3 audit_define_service_scheduling_approach_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define service scheduling approach Completeness Audit — Audits define service scheduling approach records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-define-service-scheduling-approach
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_define_service_scheduling_approach',
    "version": '2.0.0',
    "display_name": 'Define service scheduling approach Completeness Audit',
    "description": 'Audits define service scheduling approach records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-define-service-scheduling-approach',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-define-service-scheduling-approach',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd158c52f5d237ab5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/develop-service-strategy/define-service-scheduling-approach'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/audit-define-service-scheduling-approach', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditDefineServiceSchedulingApproach(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditDefineServiceSchedulingApproach'
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
    print(AuditDefineServiceSchedulingApproach().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6eZOjxpbvV9HU/GF71N1iE0vfuBEPEEJi04IQArejmiXZxCYWAfLzd3+JpKpuz7Vn7ImJeCiqxJJ59vM7J0n9+uK0TVRUL59fdODkE9FJ0zgC1cTJ/QlfdEV1hl/F2YV/E6/Imyp226ao6pcPLz6ovSoum7jI4XS29eOmnvggiHMwqUF1jT347UXAb9M4DydOWVaF40WTCnhF5deToKggyaxMQQNyUNd3nmWRxt7wuB87OSThhE6c182kalPw0XVq4E8gUe9cf4IygN4ZCdQvn3/+5cNLDM9fPv/64qVOXb/JtLhLpD8E0t/lYZ/iQCKpk4dwdDlAS+TwugQVlC2Dt6A2k+fVjzVIgw+T//iPc+dUYf3T5y/55Hl8eRk/+zafNBGYNIVTN6OQTum4cRo3w6cJm3bOUEPNm7bKoaKTGhoyDz89Zn6jVJSTf47Pfnww+RSC5scvLwUUwRnN/OXlpwk02peXqh3PP41Uyh9/+pQWHah+/Okbnbp1E+A1IzEo9afX5/WTLBz4bWgc3Ln+E1J9ONQFX16+U248HnKPesKZL5+SIs5/fBCGNryCfPTTjz/9Gdm7t9K4bv4S3Z8fhCPg+FCnp+A/fbgb+ZfJ9KnQO80/Z1tCt/4dTeDwN3YfJk9D/Rntu/3/E2kYVKB+t/gfkvujCdN/Tn7+U93+qwkfJsGXlwVI4yuMDjcFnye/vupbgf/5B//bzR9++Q2S/m/J6EVbeXcKr5mTxwGom9fXn3+o77d/+OXnH9oSxhpwste2Sv+I5h/Z9c7ndxZ8jvrx93MhfyM/50WXT94jffJrUf5b9dunydFJY//b/frz5Pt8GY/pZFTijenDBN/lTA1l/c6OP738BnEC4knVevfHMMv//d8nauxVRV0EzUT3inYEm7yJMzAKf4jienJ4JvVXXV4ryqfM/zqBd8d0hxDhtGkzESsnTicwH0aPjxoUweTr//HuEPrRe0LozBkR6fUBkq9PkHz9BpKvbyD59dPkEEH2RRWHce6kkz273UIoBHkzMn4AYJt9vI68oVzxA3v2/HrEnRpC5T8mX/8qs9c73U/lMCr1JYdegogLiTYgK4vKqeJ0mDgjarlDAz5CyIXIUhVp6jreeTL+a8tPo6XMCORP+3mwloAeeG0DJmnhQQWCGML0BxgCdZFeIUqOVq3PcZpO/BhWBFhThnsBgJb/PBL7+vUrBPvoS/6AZXzyKDb1DA54F3jy8WNZgSCNw6j5kgMvKiY//PrbD5P/O/mvZt2Jjzy2sEzc7QZDO51I+kabwDxtMzisnoxBAkHo7sdff3s4ZJQuh9URZlccxOA+GVL7FhSjBg8vvbkI6jyKCKonp9/bbdJF0C6TuIHWghlff/iSjyQKOLTq4hq8GfEx+WH6N58/+Iw+qZ82hH4KqiK7j73H4+jMsdh+mqyDybuloLrQr83o0aiAldUHJch9kMO620RO882FedFMaphFdTB8mLQ1VHWk/NWt7hUZZBCqnObrROW3sOoVKfw3GujOHs4u8nh0/DNoH7chkeoHGGPcG4lPEw1Aa05Kp3LKqILl/T4ucB4RAavd23xI3JnkoJuMVR6MPrrn9z3yFv9918F/32ncG4PJlxZDUGLy/6FzGWVmRXEviOxBWEwE7bC3HgE29lijvo+2DDYPd2b3bPnWULxhzxsqf8nTGDqlGv7xGBncY+ox5oF0bQWZ79n9nf6Y3dWdbtzAyBhdXVVjNDtf8jf4/wCNDf1Sj0gGE/g8wkHxznB8+iZpBLN0vP7WCjztNFoFhvOkbF1omUkAgH+P/Caqxrx6Wh+GCRhzDCYCtPD3Wk0gdRgCkP4ECjG6CJaIu+k0mB+jY+7B/j48HhssKIXfelBamEDg08Qc4xnGZD1xAeySxjHQCj/cSU0yAG0MRXy3cB055UOYse99CuhAqtcYxt139n8+gpE5VhnI7T3tIE3HdxpoyQ66AGZV//Dru5RPT0Gi2Rgd90m/d/ZT08n3VeofY+pBCb9VANiojwX+O9NAvK6yRyzCsD3XMLkz8AwfGAf3Wv7pUY4f9f5dls//0ur/+PdWA/cCa/zeb58nUdOU9efZ7FEE32rgJ5ghMxghcQnqRz38+Ei9j8/U+/gt9T6+pd7v6D/M9Xny92T8HYlnaH+eoJ+QT8j4SIGcx9h9HtAk/EfO+kiMT7/ke/DN15B9kUHsGV0wQPx9rzFvQ2ChCSsQjoMfNaceS1UHq+Md6u414z0enrkCkTQPxwJZF9/l8KjT6N2H894hGT7KR7D3xzYvBONCKB3Fr8HL57xN0w8vuZOBv74AGsEXBi60ybh6grdh89TE4H4FdYMPYmc8//2Kb3M/cdJHgNcNFNap7jDxTJgn/n0YO+ccQsy4ShkrTP594zQK3wzlKO1jUTQ2aO/d279yvWc05OEXn8fEhtUVdtofJu9N84fJ2zLmvj7MW7iO+3ls2Ec94VD49T72fRHrgpdf/kCMZ//+J0LEI6iMMPRQF/jfEOPuvNJpIDAaewWKVHj3rmKsZ/Vwr3v/qjZkWIFLCyu5P4r8zQbfRCse8vx2V6V5LFJ/fXnDnPH80VY8wg5O+Nst4Giet9L9OjJwRjL3Ru1urbvPXh0YHmOJ/u5ROPYbr49ofvkMgQt8eIGTx9BJ49t9hf7ykAqq861NhhQgBMGUhy3HDCYjpAQbgXJU5Qzh8zsG4+3Yv48fTz7/cW/9F7Dks+dgDOoELuYiHkpRqDfHgDcnXdINAEMy8Bn8IB7B+C7tAswnUBqQFB2gmI/6AFBQmJFs5jyFmaGjR6Aa72b/H/f9Lw86sBBhcxISAiiG+iRNuh6DeqQLXAYnUBwjGRAg5JwkAIm7OIlATSjEc1F8js09MqBJfE7SCDH3RnrPjvMh3Otbd//mowe0vEJQzuJRdMxxPNqjUMJnKIf0AI64uHcXg8IBMmfwgKYBAee/T336aXTjQ/8xkmGzOao58vn16fcxOkkCjlwR9Zp9HPyMOTokRrn7yJ1WJLDsE7N2Y+OiHwDFYyZz2bQEtuMasUnKZWFUtaANkoCqZ69TReNYiZtowbA5JW1bvw3YbO67rdWs2Mo8bW7S+TafyT7VdUdOXRX1MZFOC7ZBxdYmVmAQzMwfTjcNLLNLGHuun87rAemNdeQ7NaWS6f5EMcAPKD7QkKunGPy6PMqVfUnZmtxVMIIreV1uJTwhT9u1t7621oD2x4Ov25nqe7G95x18E3XaoqTo9jAQdW7HxHVFbRQ7putgd7XjNcUSEa3LNKzES6E0AaUdG1t0JPd2rr1bIQbkRVXOre8YAk4Qg6i3LVPM6l46qZE05fnTUUd3BXWaz33xutzpepgcUysCaMnVS0kn2CFRvFmqt9FlSCJKsXVz75HDuso58lIWzUXbV1Mgkh3OLIKWXlbneaMYe9PUhTluqAXFHwUxV8/9teDYrKxPJei0ZBm3CCaUbpMXPlc3l4PLWsthcVoqRSDlkUGsmKE3ahPLreEgFysGuV24PGqjvRpPcZwfwGVuK4oU73GtmynCvlcsvjmjq8RcoVHpm2dE8UXNICSFNK0GoJsDGnRMJh+ZRLwILLnroy3wjqsNE9IH2nBJ2hc3U8/htV5XpBCF3SZJ30R5uVqbiUwEidVngYBgWkVt1YhaVA7CmPzJQEMLWNe9WCNYv9TnDrEF8bHI2Ns+ptSIdvd7d83m2x1NykQcCEGGdlJeqTkmKDw4u7HHXuYmnRFVeEkPw+LWUmS+zPrD0TmC2wZIJvS4ry8Hy5oTZ/m085C5rVWapOXwL2sP7sY5VPwVmFnFbc9QrnB36sMG21LdCa+3a5SJza45MOEt39jobKpu6xt3BqfianRNTGJXSTpPE0xhaHYheY18m2FGLM9O+qUvvWznlZ42JFgiqgsrVYjBkVfs/Gz2xDWySf7qI0ZpbnYIiW6LzZWmhiJT7d0pW1VHQfHEilDZlZzIW0kSz6c61bANybFcdlopYWcoS7Uj1GmlekAKndq/XSPDWp2YaHbY3haVtImd/rBugXFZHeW5hAx+IXsbIzfZm1wE87l8Mm16Ncu0IFItjZaFxj255JZmbyhxEPHpuVf9ZbFkAto9iWRb94W8FJVNl5zMHboyO9oGGwItFSMmuWnYzJAFN8VtwwzahSGJeIsfWcNLjwKCLDe20PHrI79mZz5T9bJ5yAEV8WVekNvNbLseBLn2lRKV+SloeAqku/xgasOFuRzy8HQ8ylZIawC7VSvhxnDxEaBHQVqtc0az0Ro7xfWSXXBbQ7gWIGCXPVh7fmlKB3vBHgJM2Jozee9FU68yznp8HIpZIemWcDYck/evEMdnN2rgd7ZRWxKGrE3vUp6mqO4OfhRpiTaNzLBVh/pWZaYplEOmX8gLIpv7wWALl9nK0Zk/zE/JdNccY6yg7Km9VCGakJeDMc034GD17HyPuaZ82UgUsjhSsXTNkShn7MoM9MRYRadhViGzZSNu3UbjztfalxbiQa2lwjXxFAny9UbNdjKeq+qQy2raa1V0ozCDO6qWu9ZJbbrDhJ0CgpxS60BcWH1sI8bFyiJ3Tk55Fq3o6uSiW98+mwHFOestLpesWCxWFx7V5w3DLhBaTLgImIeEXetnQnCFqbQ6Hrp5S7pJJpW9ESoEVuTefr2wbTNd1fwGa2g7F3gj2vMbg77tnMUyq7Z8DDYbgfF2BhQF7Eu2yS1CS2bXzckDUCy6pLabK6yQwXVVk4UkhGl3NFu5njJ0lpp7YyZg+yVTL3gD8HFHMMxsu0j7svMbv3c5upYFRZ92s1ma9HS9uljba0JXt35KsspS2RXOfGFUOLrLpDV3rHk11dzDPM58RxAPMmoUmb9zCrO/xQ5t770cZ/c+d+lskutM6WyiwRldhwhFhNXZGvQyOVpbVjVvXawoHnGYC+Ai8wVTRkokkOHFjqgsnWPSUaiAmk1BmC/Pez/PLOEIl1/UdjuweEq7y+Vys1c6PNk7Adkqy8tpXp0d0BzO9DmtbhbiC3q/QLz1oG26wiX3puHmVw7JvWXbr+xa7mirM7BhE8yETLAzNFlAOAaYJTLzOmGR614Lr/sTdjnwQnLzZ01C1SUgvLV+ujBDQ+RWdy6tvg5jPSvPhu2hWqUe8/44PSTTfrVbF0J9BGpprrCGkUNK5BBFupaSfKRUoTN96SY3zmWBRH2kE0TXhCdZm7FEoPJ7EzG1SI8l2l/v0vVZQxa20evSmd/hxUrgRMvyJZWx99nVQzaMvp/zV4RD5cwQV3l57CxvmeHtVMX8Ex+wRaZU4u1gOrC87ZG95fFWreX8/sAUZ7Mh0FxZJAih3zI+1jc4/LhC6DKad3P7Qk+x3nNNqraDxNDmcra8tHIXkFqV2ssiKfGCEda7yM8qY3ncMwLlrw+Se8yKOEelhKaKwQhhol/kwNIyNdIKjaIvoYxALBdWqi3Xa6ZYxp1jCRu1jmN9DeNea9TI9LiFPHN3HF1qmHLFEllfaew6y08EWBx2BuHaVxXxQvGAGmxixa12xctigyFSc0R5h6iqNZjOpoHN4/7CWrBpZZtsy2+aGtSxsB8YNE8c8jRLtrY99Y6b85RJW7fqLNPGjHqKciFMvTWviTsVgOboSQnH2vJ5YRVrD5+5ltnVRTfLuPJssrbHq97+GGwVmixnfXrjDklPigfXr0tDhwhmxWzJ0LuLQV6C2NnxNxYvbYQOMFT21ZkgTo3paaXb6MW2xPmUP/IXLxJQ4WKg2lpGA3kXnuzI1Q8bN6xRAxzOt8OKtFYXIZa2yKLeKcs9wrsLeb9Wuv2tLBAxuuxlXwzncWsaIeMIvn91ZBF3I2K/i0LnWttdMSUFid0s+bRYaLNYE8O95k8pW2MiH9cQy5yHhJo7Kle5NMJuWN3HTkgak5l+A9Pl4pIjZs2m9rCe53h6y9zwKNUtXF9H+8u8RiW77KmaEERM2m6OM0VbajXJ4hcFc7c6ZRXpXI2daqNknmCUAa/x21RD3atozgkEH3Q+aw6rxtL7WgC8DNcAXKdSVm5W3XR5PWwDRS1Dk05J38uOde1T2wRUdHkerufVTaJtvMQyCTar2S2rldX+oAW9fou1UiorychOeulIpg4oedgeQAqhVFGuCmwYjepgmkixlKQt6OaBe2YLzSo2F2tfLcua1GfGLSmnhjNtqkPBWNcslFVUqE+HBscoZl5gjOpkGEzFwpgeYD/mRg0ugkS1xI281beEulPTOLnJ6RmRFb3EdxkVrjG0lbk+D5g9OHMCVQZ66c29KFyZg8AR3BnfnPR2k2/zpJ7ZsMNki73gysqKt+K9uOIlOTs6Udgzdl8bEDDKc5/zmlfueKThez2/AAyNp4OgpLJ+KMvWODEXgTZUIwlACdcghRMeNTETtt0iPi6rWroSTiG28QXUaGCFC9mxtE0UUcvFqhftG6F5DCxvAUbU4KjlvWqb0oKESBalXWQcEL3f1lMu4jpCyzJMEHrXw2Ciy/bu6qRd58J2ghyMbZgiJ9XqQJzsPHJ5tTktleOCW151KLHpa8tKwI+X09G0N5iz7FBTI5N20eA7V2aIsDe7xAPpAVWvC1+RzVIXzOVyuKzXJz+xYWPlk8hUUjB8vbjIbnCOTNM9RityhS1JNqKPGO8u48iVLVexmAzPePuImUSg9TbPOO5lwLfypbDtPEnTDZYpjZyzO07yANvtludhmqWxy7YIvtqScV64GbdBq2bDmPCTr1akEoOtjrU5RInuNF1eZralFcGquXG+ScvVrF0M05WMFyfXEpe5qySbkJ/yhzYHuQEzOzNtJTYUYlqGIAkXS4j5x6srX9ggaqbbze3KpPrWRzp3LYUQHGeHDGu8JeNKO5PHL5XKn4bkSuPHXRpS2EUX9CnrRMypt4gClRyfmFZ0nkiIrQJqTc97DcfK1kOrxUJXw5qS25ujO8gAuyOdkZQlhxGz4TxfVku4bJybAR1um9SUcz/Hp+u8I84bGcy5lsuim73xSZ4DW1PDlptcC3PvxC2E3cZJSSfksRmwD0Mc6AeuEOMe5IzkXq3zcZUpJMdL20FBOY+T9S19lXSTtularE/cQIicmRyrs7/aIYCpuHZ9i1jMxhXHn+9vBUvIpr3SpfRIbwFtKUC8LOktsprP52h7YLgZ52nMkeA8m1jOwHq3VeuqbXdw+T3HMLMvWX55mKco3SRoBcvc9qZ3p3Wvcb62uaFpYtEbxQiogerMGXqdYeJGIMRVuI00i7so61XmkqcTOzQS5uM3AZalWeAgQE39pcsr8nHwbiJKU8qAbBIszwFnUOCyUr0Npc1W1VWxmTDjhR63j9Y1jE9UssSubG23nq4kkngp83WSkjyu5LPaXIby5rZYDfMlvnaLs7qhzvq+5oJ9VeR5pJ74wrqxTGXNPJK72Ivd5RZVsev5854lElQnjwHvyev64AclzPwZCDs/ErVie1z2saAcOYDAVcOu3fBibU2ZWle4W1Fzgxg34ixD+emGxeeJ1MxWdpf6izTGy5tNVVXSYi1mK0Cq8a2uHwRKRcO2RVb2dYvMCYG47E4JylsRJbsqvdD8PT44+PV0SpRWjXopo1fnvsN3N/EQuqKYVF3X53trI1w24nS2gyXb6B2tZy4KP4SnhWRrWEQyps+V2Ky+NKRdKv2JOia7DlVSXsU5BN9dEfvKrbNVzfIxVcr9CdEqhFF1maWTJR178xoJw/lmnzESKmwOgWmcLjSxyuZ4Kxj0Wjm4DeYRU1UcZrAxX9bYQIVt45PU7XSTwnAWd7duelokxpbksD04+Ge3qcgTY/TVYcPEurWx0xmNCS22J5wjc0XATCWvibVfAH/Gu3DlHximQO+j+X4e87DAHpxocJ1bhUe2mBgncy2yqF/PYOcYN3nQxw5XSNIOVBfiAoJVtBecaFk5VJRoJJpjFtHicm+TgrvDjVIH0wi2xUa0mEado9YrhJsiKb9QL+KqNFhtW+YDw4CDjjJNy8DALSlyH9MmW68ikcG2Ld3sZGqz6AYYGAcDJXLqltxYsbP4i1B0jRYesql4FI8L5uCepYLLD+fLuevpSuypc08emaVretddTU1Z4jLlekDiDpvP8Co6hXU+5Nz22lSescuwgUxKsFIVn246U5utyQaHvaPA3W7Z/LYrrdTy09YI4MLhuJ3FmXFz53jRd1Lfbk6sV0iIpywbamdl+1KsDTZ3STXa0nsLGGC/m5fz/BoK3ZSUqlza7m0c9Jhz3Vb2dhekeY1nEXFhWfafLx9e7rvNL59RhKKxDy/ja+7nTsP/5EVzeIvL1ydFnKLnH17+9957Pt5Bvu1I3rcAgON/vnP//PeF/eXDS+XFULDHK+o6bcPnK8//9Kb34199Cz1SGR6b6ONGat+8bd00Tnh/WR7nfls31fBaF2l7f1UOzd/W449q6vF3Vx78frkrmZXjTsad8Uj1qU9TvD5/CPQy/uJl3BwEfuw04HkZPncXPrz4A3Ri7NWvODl/BVU5avvcIBtfCI87ZC+//T+T7cwSKigAAA== -->
