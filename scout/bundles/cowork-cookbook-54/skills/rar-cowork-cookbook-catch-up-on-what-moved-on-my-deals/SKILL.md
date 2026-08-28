---
name: "rar-cowork-cookbook-catch-up-on-what-moved-on-my-deals"
description: "Know what changed across your top deals without reading back through a week of threads."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/catch_up_on_what_moved_on_my_deals", "rar_sha256": "82967557a114e98e7171fc80fbf68ca03b022793bd53efe8f3c7f431512a76c7", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "beginner", "integration", "dynamics_365_sales"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/catch_up_on_what_moved_on_my_deals`. The original RAPP
agent is preserved byte-for-byte in `catch_up_on_what_moved_on_my_deals_agent.py` and in the RCI capsule.

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

Catch up on what moved on my deals — Know what changed across your top deals without reading back through a week of threads.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/catch-up-on-what-moved-on-my-deals
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `catch_up_on_what_moved_on_my_deals_agent.py` and embedded as the fenced Python below (sha256 82967557a114e98e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `catch_up_on_what_moved_on_my_deals_agent.py` first:

```bash
python3 catch_up_on_what_moved_on_my_deals_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 catch_up_on_what_moved_on_my_deals_agent.py   # or on stdin
python3 catch_up_on_what_moved_on_my_deals_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Catch up on what moved on my deals — Know what changed across your top deals without reading back through a week of threads.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/catch-up-on-what-moved-on-my-deals
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/catch_up_on_what_moved_on_my_deals',
    "version": '2.0.1',
    "display_name": 'Catch up on what moved on my deals',
    "description": 'Know what changed across your top deals without reading back through a week of threads.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'prospect_to_quote', 'beginner', 'integration', 'dynamics_365_sales'],
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
        "upstream_slug": 'catch-up-on-what-moved-on-my-deals',
        "upstream_url": 'https://coworkcookbook.com/recipes/catch-up-on-what-moved-on-my-deals',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '95ec6e32e943320b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'beginner', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-sales', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/pursue-opportunities/manage-opportunity-process'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/catch-up-on-what-moved-on-my-deals', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Meetings', 'Communications'], 'plugin': []}, 'verification_status': 'draft'},
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


class CatchUpOnWhatMovedOnMyDeals(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'CatchUpOnWhatMovedOnMyDeals'
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
    print(CatchUpOnWhatMovedOnMyDeals().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
