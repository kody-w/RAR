---
name: "rar-cowork-cookbook-user-access-review-audit"
description: "Audits Dynamics 365 user accounts for segregation-of-duties conflicts, inactive accounts with active role assignments, and roles granted without recent login."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/user_access_review_audit", "rar_sha256": "d274d9c1c300ae5f3e8eafe595379d5d50ec69b4b4e4a112785cbd3d17bb130e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/user_access_review_audit`. The original RAPP
agent is preserved byte-for-byte in `user_access_review_audit_agent.py` and in the RCI capsule.

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

User Access Review & SoD Audit — Audits Dynamics 365 user accounts for segregation-of-duties conflicts, inactive accounts with active role assignments, and roles granted without recent login.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/user-access-review-audit
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `user_access_review_audit_agent.py` and embedded as the fenced Python below (sha256 d274d9c1c300ae5f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `user_access_review_audit_agent.py` first:

```bash
python3 user_access_review_audit_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 user_access_review_audit_agent.py   # or on stdin
python3 user_access_review_audit_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
User Access Review & SoD Audit — Audits Dynamics 365 user accounts for segregation-of-duties conflicts, inactive accounts with active role assignments, and roles granted without recent login.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/user-access-review-audit
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/user_access_review_audit',
    "version": '2.0.0',
    "display_name": 'User Access Review & SoD Audit',
    "description": 'Audits Dynamics 365 user accounts for segregation-of-duties conflicts, inactive accounts with active role assignments, and roles granted without recent login.',
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
        "upstream_slug": 'user-access-review-audit',
        "upstream_url": 'https://coworkcookbook.com/recipes/user-access-review-audit',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '37bcf4aff678f487',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-23', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-access-and-security'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/user-access-review-audit', 'uses_skills': {'custom': [], 'ootb': ['Excel', 'Email'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.5, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:audit', 'word:audit', 'word:review'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class UserAccessReviewAudit(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'UserAccessReviewAudit'
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
    print(UserAccessReviewAudit().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
