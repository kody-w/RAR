---
name: "rar-cowork-cookbook-competitive-move-response-kit"
description: "Get a coordinated response to [Competitor]'s move on the table by end of day - one story across PR, sales, and field - backed by our own performance proof."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/competitive_move_response_kit", "rar_sha256": "45f0c7fceb9d48154c2535ec62324e1c0f9e2e456e3bd9209ad4715dbeb866dc", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "competitive_move_response_kit_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/competitive-move-response-kit:db95e3676e9c435f15897218731ec311ceeec566e9cbabc0f6b4f23460f096f9", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "concept_to_market", "advanced", "integration", "fabric_iq"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/competitive_move_response_kit`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `competitive_move_response_kit_agent.py` is
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
