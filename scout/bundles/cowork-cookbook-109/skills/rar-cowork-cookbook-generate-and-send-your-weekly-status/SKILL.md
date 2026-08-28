---
name: "rar-cowork-cookbook-generate-and-send-your-weekly-status"
description: "Replace the Monday-morning scramble with a status update that writes itself."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/generate_and_send_your_weekly_status", "rar_sha256": "b7b6e3a7c93dcee8c1662b725ab3a4dd3597ce1b3fb5f81acd53de217b19eb21", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "work_management", "intermediate", "integration", "fabric_iq"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/generate_and_send_your_weekly_status`. The original RAPP
agent is preserved byte-for-byte in `generate_and_send_your_weekly_status_agent.py` and in the RCI capsule.

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

Generate and send your weekly status automatically — Replace the Monday-morning scramble with a status update that writes itself.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/generate-and-send-your-weekly-status
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
    "audience": {
      "description": "Optional. Who reads it \u2014 this drives register, length and what can be assumed.",
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
      "description": "What to produce, and about what.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `generate_and_send_your_weekly_status_agent.py` and embedded as the fenced Python below (sha256 b7b6e3a7c93dcee8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `generate_and_send_your_weekly_status_agent.py` first:

```bash
python3 generate_and_send_your_weekly_status_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 generate_and_send_your_weekly_status_agent.py   # or on stdin
python3 generate_and_send_your_weekly_status_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Generate and send your weekly status automatically — Replace the Monday-morning scramble with a status update that writes itself.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/generate-and-send-your-weekly-status
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/generate_and_send_your_weekly_status',
    "version": '2.0.1',
    "display_name": 'Generate and send your weekly status automatically',
    "description": 'Replace the Monday-morning scramble with a status update that writes itself.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'work_management', 'intermediate', 'integration', 'fabric_iq'],
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
        "upstream_slug": 'generate-and-send-your-weekly-status',
        "upstream_url": 'https://coworkcookbook.com/recipes/generate-and-send-your-weekly-status',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3ec977d736fa8623',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'fabric-iq', 'process_roots': ['work-management'], 'process_tags': ['work-management/manage-communications/produce-recurring-status-updates'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'work-management/generate-and-send-your-weekly-status', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Scheduling', 'Meetings'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.429, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:report', 'word:generate'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class GenerateAndSendYourWeeklyStatus(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'GenerateAndSendYourWeeklyStatus'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'audience': {'description': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What to produce, and about what.', 'type': 'string'}},
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
    print(GenerateAndSendYourWeeklyStatus().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
