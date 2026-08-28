---
name: "rar-cowork-cookbook-onboard-a-new-hire-with-a-30-60-90-plan"
description: "Set a new hire up to succeed from day one - without building the plan from scratch."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/onboard_a_new_hire_with_a_30_60_90_plan", "rar_sha256": "2ccaf78f37daa6af0887eef63129200d50638bef7aad811195df255a25d4aeb5", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "hire_to_retire", "advanced", "read_only"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/onboard_a_new_hire_with_a_30_60_90_plan`. The original RAPP
agent is preserved byte-for-byte in `onboard_a_new_hire_with_a_30_60_90_plan_agent.py` and in the RCI capsule.

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

Onboard a new hire with a complete 30-60-90-plan — Set a new hire up to succeed from day one - without building the plan from scratch.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a design capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/onboard-a-new-hire-with-a-30-60-90-plan
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
    "constraints": {
      "description": "Optional. Hard constraints \u2014 budget, platform, deadline, compliance.",
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
      "description": "What is being designed.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `onboard_a_new_hire_with_a_30_60_90_plan_agent.py` and embedded as the fenced Python below (sha256 2ccaf78f37daa6af…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `onboard_a_new_hire_with_a_30_60_90_plan_agent.py` first:

```bash
python3 onboard_a_new_hire_with_a_30_60_90_plan_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 onboard_a_new_hire_with_a_30_60_90_plan_agent.py   # or on stdin
python3 onboard_a_new_hire_with_a_30_60_90_plan_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Onboard a new hire with a complete 30-60-90-plan — Set a new hire up to succeed from day one - without building the plan from scratch.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a design capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/onboard-a-new-hire-with-a-30-60-90-plan
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/onboard_a_new_hire_with_a_30_60_90_plan',
    "version": '2.0.1',
    "display_name": 'Onboard a new hire with a complete 30-60-90-plan',
    "description": 'Set a new hire up to succeed from day one - without building the plan from scratch.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'hire_to_retire', 'advanced', 'read_only'],
    "category": 'general',
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
        "upstream_slug": 'onboard-a-new-hire-with-a-30-60-90-plan',
        "upstream_url": 'https://coworkcookbook.com/recipes/onboard-a-new-hire-with-a-30-60-90-plan',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ccab66f4acb9cee8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'advanced', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'none', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/recruit-and-onboard-talent/onboard-new-employees'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/onboard-a-new-hire-with-a-30-60-90-plan', 'uses_skills': {'custom': [], 'ootb': ['Word', 'Calendar Management', 'Scheduling', 'Communications', 'Enterprise Search'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'design', 'checks': ['Constraints are written down and the design respects them.', 'At least two options were genuinely considered.', 'The trade-off accepted is stated explicitly.', 'The riskiest assumption has a cheap test attached.'], 'confidence': 1.0, 'deliverable': 'A design record: constraints, options considered, the choice, the trade-off accepted, and the first thing to de-risk.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'constraints': 'Optional. Hard constraints — budget, platform, deadline, compliance.', 'subject': 'What is being designed.'}, 'refined_by': 'rules', 'signals': ['word:plan'], 'steps': ['Write the constraints down first. A design produced before the constraints are known is a preference.', 'State the success condition in terms someone else could measure without you present.', 'Produce at least two genuinely different approaches; a single option is a decision already made, not a design.', 'Compare them against the constraints, and name what each one gives up. Every design gives something up.', 'Choose, and record why the rejected options were rejected — that record is what survives the next reorganisation.', 'Identify the riskiest assumption and the cheapest way to test it before committing.'], 'subject_label': 'thing being designed', 'verb': 'Design'}


class OnboardANewHireWithA306090Plan(BasicAgent):
    """Design agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'OnboardANewHireWithA306090Plan'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'constraints': {'description': 'Optional. Hard constraints — budget, platform, deadline, compliance.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What is being designed.', 'type': 'string'}},
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
    print(OnboardANewHireWithA306090Plan().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
