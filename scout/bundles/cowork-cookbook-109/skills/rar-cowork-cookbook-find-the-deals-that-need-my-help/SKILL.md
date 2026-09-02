---
name: "rar-cowork-cookbook-find-the-deals-that-need-my-help"
description: "Know where your attention moves the number this week - and understand why each deal is stuck, not just that it is"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/find_the_deals_that_need_my_help", "rar_sha256": "ec6d291a1f54411dbcf7f2999c1bb7b9c0b2a22302c45e3d7a938d626976e8ca", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "find_the_deals_that_need_my_help_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/find-the-deals-that-need-my-help:9015babdbe5c3e7c5c579c1103a1d1b7ae6a8ede8773ada3b02d8e97aa835489", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "advanced", "integration", "dynamics_365_sales"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/find_the_deals_that_need_my_help`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `find_the_deals_that_need_my_help_agent.py` is
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

Find the deals that need my help — Know where your attention moves the number this week - and understand why each deal is stuck, not just that it is

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/find-the-deals-that-need-my-help
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `find_the_deals_that_need_my_help_agent.py` and embedded as the fenced Python below (sha256 ec6d291a1f54411d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `find_the_deals_that_need_my_help_agent.py` first:

```bash
python3 find_the_deals_that_need_my_help_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 find_the_deals_that_need_my_help_agent.py   # or on stdin
python3 find_the_deals_that_need_my_help_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Find the deals that need my help — Know where your attention moves the number this week - and understand why each deal is stuck, not just that it is

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/find-the-deals-that-need-my-help
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/find_the_deals_that_need_my_help',
    "version": '2.0.0',
    "display_name": 'Find the deals that need my help',
    "description": 'Know where your attention moves the number this week - and understand why each deal is stuck, not just that it is',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'prospect_to_quote', 'advanced', 'integration', 'dynamics_365_sales'],
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
        "upstream_slug": 'find-the-deals-that-need-my-help',
        "upstream_url": 'https://coworkcookbook.com/recipes/find-the-deals-that-need-my-help',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6aa29ccde9bda727',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'advanced', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-sales', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/pursue-opportunities/manage-opportunity-process'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/find-the-deals-that-need-my-help', 'uses_skills': {'custom': [], 'ootb': ['Deep Research'], 'plugin': []}, 'verification_status': 'draft'},
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


class FindTheDealsThatNeedMyHelp(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'FindTheDealsThatNeedMyHelp'
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
    print(FindTheDealsThatNeedMyHelp().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
