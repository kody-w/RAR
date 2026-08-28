---
name: "rar-cowork-cookbook-competitive-move-response-kit"
description: "Get a coordinated response to [Competitor]'s move on the table by end of day - one story across PR, sales, and field - backed by our own performance proof."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/competitive_move_response_kit", "rar_sha256": "45f0c7fceb9d48154c2535ec62324e1c0f9e2e456e3bd9209ad4715dbeb866dc", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "concept_to_market", "advanced", "integration", "fabric_iq"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `competitive_move_response_kit_agent.py` and embedded as the fenced Python below (sha256 45f0c7fceb9d4815…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `competitive_move_response_kit_agent.py` first:

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
    "version": '2.0.0',
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
