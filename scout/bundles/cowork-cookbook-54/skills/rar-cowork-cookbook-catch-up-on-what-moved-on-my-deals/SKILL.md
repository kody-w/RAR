---
name: "rar-cowork-cookbook-catch-up-on-what-moved-on-my-deals"
description: "Know what changed across your top deals without reading back through a week of threads."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/catch_up_on_what_moved_on_my_deals", "rar_sha256": "3efae1999657ddd1dc7e525cd8e51b7133a9412a54bea00a7d60933eafbbbb18", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "beginner", "integration", "dynamics_365_sales"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `catch_up_on_what_moved_on_my_deals_agent.py` and embedded as the fenced Python below (sha256 3efae1999657ddd1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `catch_up_on_what_moved_on_my_deals_agent.py` first:

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
    "version": '2.0.0',
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
