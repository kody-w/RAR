---
name: "rar-cowork-cookbook-generate-and-send-your-weekly-status"
description: "Replace the Monday-morning scramble with a status update that writes itself."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/generate_and_send_your_weekly_status", "rar_sha256": "db94ab2c81b668d9e81704c23a28d8401cd9b63203dd54d595c2f1186ea5f0bc", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "work_management", "intermediate", "integration", "fabric_iq"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `generate_and_send_your_weekly_status_agent.py` and embedded as the fenced Python below (sha256 db94ab2c81b668d9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `generate_and_send_your_weekly_status_agent.py` first:

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
    "version": '2.0.0',
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
