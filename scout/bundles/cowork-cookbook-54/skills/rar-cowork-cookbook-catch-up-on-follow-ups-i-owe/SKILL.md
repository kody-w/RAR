---
name: "rar-cowork-cookbook-catch-up-on-follow-ups-i-owe"
description: "Close the loop on every contact you met but never circled back to."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/catch_up_on_follow_ups_i_owe", "rar_sha256": "9e995fae1369a852687aaa25c0855404c71d764521f066aaf1065589a4c4ed82", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "catch_up_on_follow_ups_i_owe_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/catch-up-on-follow-ups-i-owe:983595776462608c7b0d286e4e53f2e049ca7a93edbfb6249ffb9b1d6a5efbb2", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "beginner", "integration", "dynamics_365_sales"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/catch_up_on_follow_ups_i_owe`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `catch_up_on_follow_ups_i_owe_agent.py` is
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

Catch up on follow-ups I owe — Close the loop on every contact you met but never circled back to.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/catch-up-on-follow-ups-i-owe
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `catch_up_on_follow_ups_i_owe_agent.py` and embedded as the fenced Python below (sha256 9e995fae1369a852…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `catch_up_on_follow_ups_i_owe_agent.py` first:

```bash
python3 catch_up_on_follow_ups_i_owe_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 catch_up_on_follow_ups_i_owe_agent.py   # or on stdin
python3 catch_up_on_follow_ups_i_owe_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Catch up on follow-ups I owe — Close the loop on every contact you met but never circled back to.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/catch-up-on-follow-ups-i-owe
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/catch_up_on_follow_ups_i_owe',
    "version": '2.0.0',
    "display_name": 'Catch up on follow-ups I owe',
    "description": 'Close the loop on every contact you met but never circled back to.',
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
        "upstream_slug": 'catch-up-on-follow-ups-i-owe',
        "upstream_url": 'https://coworkcookbook.com/recipes/catch-up-on-follow-ups-i-owe',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '010809eac7e6b811',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'beginner', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-sales', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/manage-customer-relationships/maintain-contacts-and-accounts'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/catch-up-on-follow-ups-i-owe', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Calendar Management'], 'plugin': []}, 'verification_status': 'draft'},
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


class CatchUpOnFollowUpsIOwe(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'CatchUpOnFollowUpsIOwe'
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
    print(CatchUpOnFollowUpsIOwe().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
