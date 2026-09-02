---
name: "rar-cowork-cookbook-develop-messaging-and-positioning"
description: "Move messaging development out of scattered docs into one working surface the team can pressure-test together."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/develop_messaging_and_positioning", "rar_sha256": "4b5fe52e2821bce76747177d2a9306a38a61a4826524886f5171fdfbbac13ddc", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "develop_messaging_and_positioning_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/develop-messaging-and-positioning:ed1e7783da80d8a96695b652f03b5ebc7784dac4c126c6879b2f9200cec4805d", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "concept_to_market", "intermediate", "integration", "monday_com"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/develop_messaging_and_positioning`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `develop_messaging_and_positioning_agent.py` is
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

Develop messaging and positioning — Move messaging development out of scattered docs into one working surface the team can pressure-test together.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/develop-messaging-and-positioning
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `develop_messaging_and_positioning_agent.py` and embedded as the fenced Python below (sha256 4b5fe52e2821bce7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `develop_messaging_and_positioning_agent.py` first:

```bash
python3 develop_messaging_and_positioning_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 develop_messaging_and_positioning_agent.py   # or on stdin
python3 develop_messaging_and_positioning_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop messaging and positioning — Move messaging development out of scattered docs into one working surface the team can pressure-test together.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/develop-messaging-and-positioning
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/develop_messaging_and_positioning',
    "version": '2.0.0',
    "display_name": 'Develop messaging and positioning',
    "description": 'Move messaging development out of scattered docs into one working surface the team can pressure-test together.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'concept_to_market', 'intermediate', 'integration', 'monday_com'],
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
        "upstream_slug": 'develop-messaging-and-positioning',
        "upstream_url": 'https://coworkcookbook.com/recipes/develop-messaging-and-positioning',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'bbf2afef0d8a93ee',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'monday-com', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/prepare-marketing-campaigns/develop-campaign-themes-and-messages'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/develop-messaging-and-positioning', 'uses_skills': {'custom': [], 'ootb': [], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DevelopMessagingAndPositioning(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DevelopMessagingAndPositioning'
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
    print(DevelopMessagingAndPositioning().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
