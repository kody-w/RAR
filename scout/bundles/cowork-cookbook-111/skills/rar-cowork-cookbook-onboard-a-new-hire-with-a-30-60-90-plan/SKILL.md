---
name: "rar-cowork-cookbook-onboard-a-new-hire-with-a-30-60-90-plan"
description: "Set a new hire up to succeed from day one - without building the plan from scratch."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/onboard_a_new_hire_with_a_30_60_90_plan", "rar_sha256": "96132de281cbd1920cd14db062100b705919cc271dcf5be58dfd0cded2c772fa", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "hire_to_retire", "advanced", "read_only"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `onboard_a_new_hire_with_a_30_60_90_plan_agent.py` and embedded as the fenced Python below (sha256 96132de281cbd192…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `onboard_a_new_hire_with_a_30_60_90_plan_agent.py` first:

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
    "version": '2.0.0',
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
