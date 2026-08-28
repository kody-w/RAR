---
name: "rar-cowork-cookbook-messaging-drift-audit-and-remediation"
description: "Catch messaging drift across every asset in [Folder] before it shows up in market."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/messaging_drift_audit_and_remediation", "rar_sha256": "65d5b351a8c7e7419c991d910386fe7f06018577cd24bf8378e750928fb4fa43", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "concept_to_market", "advanced", "read_only", "analysis"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `messaging_drift_audit_and_remediation_agent.py` and embedded as the fenced Python below (sha256 65d5b351a8c7e741…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `messaging_drift_audit_and_remediation_agent.py` first:

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
    "version": '2.0.1',
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
