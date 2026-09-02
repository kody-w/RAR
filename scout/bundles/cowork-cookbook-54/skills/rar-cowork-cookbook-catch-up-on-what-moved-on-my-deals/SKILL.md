---
name: "rar-cowork-cookbook-catch-up-on-what-moved-on-my-deals"
description: "Know what changed across your top deals without reading back through a week of threads."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/catch_up_on_what_moved_on_my_deals", "rar_sha256": "3efae1999657ddd1dc7e525cd8e51b7133a9412a54bea00a7d60933eafbbbb18", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "catch_up_on_what_moved_on_my_deals_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/catch-up-on-what-moved-on-my-deals:44a83c219b485c4f5b7a5d60c8a34175574f9c2acd8c6baeb93093647e7967ac", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "beginner", "integration", "dynamics_365_sales"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/catch_up_on_what_moved_on_my_deals`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `catch_up_on_what_moved_on_my_deals_agent.py` is
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
