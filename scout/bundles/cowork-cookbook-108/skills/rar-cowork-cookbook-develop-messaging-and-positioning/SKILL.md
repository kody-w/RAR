---
name: "rar-cowork-cookbook-develop-messaging-and-positioning"
description: "Move messaging development out of scattered docs into one working surface the team can pressure-test together."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/develop_messaging_and_positioning", "rar_sha256": "4b5fe52e2821bce76747177d2a9306a38a61a4826524886f5171fdfbbac13ddc", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "concept_to_market", "intermediate", "integration", "monday_com"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/develop_messaging_and_positioning`. The original RAPP
agent is preserved byte-for-byte in `develop_messaging_and_positioning_agent.py` and in the RCI capsule.

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
