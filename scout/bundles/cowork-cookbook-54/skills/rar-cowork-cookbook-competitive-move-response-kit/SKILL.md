---
name: "rar-cowork-cookbook-competitive-move-response-kit"
description: "Get a coordinated response to [Competitor]'s move on the table by end of day - one story across PR, sales, and field - backed by our own performance proof."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/competitive_move_response_kit", "rar_sha256": "0e7912c61ec7ce31b67021d2e2b1470ce5477a015af256242b9f8a12b5e12b76", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "concept_to_market", "advanced", "integration", "fabric_iq"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/competitive_move_response_kit`. The original RAPP
agent is preserved byte-for-byte in `competitive_move_response_kit_agent.py` and in the RCI capsule.

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

Competitive move response kit — Get a coordinated response to [Competitor]'s move on the table by end of day - one story across PR, sales, and field - backed by our own performance proof.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/competitive-move-response-kit
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
      "description": "The process to automate.",
      "type": "string"
    },
    "trigger": {
      "description": "Optional. What starts it \u2014 schedule, event or manual.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `competitive_move_response_kit_agent.py` and embedded as the fenced Python below (sha256 0e7912c61ec7ce31…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `competitive_move_response_kit_agent.py` first:

```bash
python3 competitive_move_response_kit_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 competitive_move_response_kit_agent.py   # or on stdin
python3 competitive_move_response_kit_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Competitive move response kit — Get a coordinated response to [Competitor]'s move on the table by end of day - one story across PR, sales, and field - backed by our own performance proof.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/competitive-move-response-kit
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/competitive_move_response_kit',
    "version": '2.0.1',
    "display_name": 'Competitive move response kit',
    "description": "Get a coordinated response to [Competitor]'s move on the table by end of day - one story across PR, sales, and field - backed by our own performance proof.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'concept_to_market', 'advanced', 'integration', 'fabric_iq'],
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
        "upstream_slug": 'competitive-move-response-kit',
        "upstream_url": 'https://coworkcookbook.com/recipes/competitive-move-response-kit',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4d2160db17ac407e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'advanced', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'fabric-iq', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/analyze-marketing-operations/conduct-competitive-analysis'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/competitive-move-response-kit', 'uses_skills': {'custom': [], 'ootb': ['Word', 'PowerPoint', 'Email', 'Communications'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class CompetitiveMoveResponseKit(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'CompetitiveMoveResponseKit'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'The process to automate.', 'type': 'string'}, 'trigger': {'description': 'Optional. What starts it — schedule, event or manual.', 'type': 'string'}},
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
    print(CompetitiveMoveResponseKit().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
