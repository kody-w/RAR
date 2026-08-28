---
name: "rar-cowork-cookbook-catch-up-on-follow-ups-i-owe"
description: "Close the loop on every contact you met but never circled back to."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/catch_up_on_follow_ups_i_owe", "rar_sha256": "9e995fae1369a852687aaa25c0855404c71d764521f066aaf1065589a4c4ed82", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "beginner", "integration", "dynamics_365_sales"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/catch_up_on_follow_ups_i_owe`. The original RAPP
agent is preserved byte-for-byte in `catch_up_on_follow_ups_i_owe_agent.py` and in the RCI capsule.

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
