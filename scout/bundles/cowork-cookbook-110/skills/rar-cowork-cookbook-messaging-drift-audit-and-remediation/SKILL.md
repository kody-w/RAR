---
name: "rar-cowork-cookbook-messaging-drift-audit-and-remediation"
description: "Catch messaging drift across every asset in [Folder] before it shows up in market."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/messaging_drift_audit_and_remediation", "rar_sha256": "1b72e8b0bd7f3e54571bcd27d9b27bfeb05361b30ecccc75e7fbed00bbb627ee", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "messaging_drift_audit_and_remediation_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/messaging-drift-audit-and-remediation:39105db508b3541b47136ca80912b826be8ed4dbe1f8e8703fc867ffcaeaafe5", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "concept_to_market", "advanced", "read_only", "analysis"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/messaging_drift_audit_and_remediation`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `messaging_drift_audit_and_remediation_agent.py` is
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

Messaging drift audit and remediation routing — Catch messaging drift across every asset in [Folder] before it shows up in market.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/messaging-drift-audit-and-remediation
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `messaging_drift_audit_and_remediation_agent.py` and embedded as the fenced Python below (sha256 1b72e8b0bd7f3e54…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `messaging_drift_audit_and_remediation_agent.py` first:

```bash
python3 messaging_drift_audit_and_remediation_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 messaging_drift_audit_and_remediation_agent.py   # or on stdin
python3 messaging_drift_audit_and_remediation_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Messaging drift audit and remediation routing — Catch messaging drift across every asset in [Folder] before it shows up in market.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/messaging-drift-audit-and-remediation
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/messaging_drift_audit_and_remediation',
    "version": '2.0.0',
    "display_name": 'Messaging drift audit and remediation routing',
    "description": 'Catch messaging drift across every asset in [Folder] before it shows up in market.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'concept_to_market', 'advanced', 'read_only', 'analysis'],
    "category": 'analysis',
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
        "upstream_slug": 'messaging-drift-audit-and-remediation',
        "upstream_url": 'https://coworkcookbook.com/recipes/messaging-drift-audit-and-remediation',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a7fd62b0b1166c2e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'advanced', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'none', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/prepare-marketing-campaigns/develop-campaign-themes-and-messages'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/messaging-drift-audit-and-remediation', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.6, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:audit', 'word:audit'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class MessagingDriftAuditAndRemediation(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'MessagingDriftAuditAndRemediation'
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
    print(MessagingDriftAuditAndRemediation().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
