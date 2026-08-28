---
name: "rar-cowork-cookbook-onboarding-checklist-generator"
description: "Generates a role-tailored onboarding checklist as a Word document for a named new hire."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/onboarding_checklist_generator", "rar_sha256": "56f1094f7a422ba7a11fd49a38b35c1927625fd05c1d233945eb2343950867e7", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/onboarding_checklist_generator`. The original RAPP
agent is preserved byte-for-byte in `onboarding_checklist_generator_agent.py` and in the RCI capsule.

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
