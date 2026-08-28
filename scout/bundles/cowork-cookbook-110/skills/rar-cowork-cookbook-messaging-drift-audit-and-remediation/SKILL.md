---
name: "rar-cowork-cookbook-messaging-drift-audit-and-remediation"
description: "Catch messaging drift across every asset in [Folder] before it shows up in market."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/messaging_drift_audit_and_remediation", "rar_sha256": "1b72e8b0bd7f3e54571bcd27d9b27bfeb05361b30ecccc75e7fbed00bbb627ee", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "concept_to_market", "advanced", "read_only", "analysis"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/messaging_drift_audit_and_remediation`. The original RAPP
agent is preserved byte-for-byte in `messaging_drift_audit_and_remediation_agent.py` and in the RCI capsule.

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
