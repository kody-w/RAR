---
name: "rar-cowork-cookbook-onboarding-checklist-generator"
description: "Generates a role-tailored onboarding checklist as a Word document for a named new hire."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/onboarding_checklist_generator", "rar_sha256": "56f1094f7a422ba7a11fd49a38b35c1927625fd05c1d233945eb2343950867e7", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "onboarding_checklist_generator_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/onboarding-checklist-generator:483e0b4d8afcc07088003cfc76b65c9ee95d9dc7401cb3a2a09b6d6eeb5647f4", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/onboarding_checklist_generator`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `onboarding_checklist_generator_agent.py` is
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

Onboarding Checklist Generator — Generates a role-tailored onboarding checklist as a Word document for a named new hire.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/onboarding-checklist-generator
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `onboarding_checklist_generator_agent.py` and embedded as the fenced Python below (sha256 56f1094f7a422ba7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `onboarding_checklist_generator_agent.py` first:

```bash
python3 onboarding_checklist_generator_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 onboarding_checklist_generator_agent.py   # or on stdin
python3 onboarding_checklist_generator_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Onboarding Checklist Generator — Generates a role-tailored onboarding checklist as a Word document for a named new hire.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/onboarding-checklist-generator
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/onboarding_checklist_generator',
    "version": '2.0.0',
    "display_name": 'Onboarding Checklist Generator',
    "description": 'Generates a role-tailored onboarding checklist as a Word document for a named new hire.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'onboarding-checklist-generator',
        "upstream_url": 'https://coworkcookbook.com/recipes/onboarding-checklist-generator',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '538f671449e451e0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-23', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/recruit-and-onboard-talent'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/onboarding-checklist-generator', 'uses_skills': {'custom': [], 'ootb': ['Word', 'Email'], 'plugin': []}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.286, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:audit'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class OnboardingChecklistGenerator(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'OnboardingChecklistGenerator'
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
    print(OnboardingChecklistGenerator().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
