---
name: "rar-cowork-cookbook-adaptive-card-conduct-exit-interviews"
description: "Produces a reusable Adaptive Card JSON snapshot of conduct exit interviews status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_conduct_exit_interviews", "rar_sha256": "b9aa77a1e731b02365dad5aa141743c98872a5c3ced6e9f0a9895e43caca79ce", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_conduct_exit_interviews_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-conduct-exit-interviews:f350d33bd5ae0708082678cea891abeffce742408210bff7b37958b8aaa472b5", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_conduct_exit_interviews`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_conduct_exit_interviews_agent.py` is
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

Conduct exit interviews Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of conduct exit interviews status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-conduct-exit-interviews
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_conduct_exit_interviews_agent.py` and embedded as the fenced Python below (sha256 b9aa77a1e731b023…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_conduct_exit_interviews_agent.py` first:

```bash
python3 adaptive_card_conduct_exit_interviews_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_conduct_exit_interviews_agent.py   # or on stdin
python3 adaptive_card_conduct_exit_interviews_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Conduct exit interviews Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of conduct exit interviews status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-conduct-exit-interviews
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_conduct_exit_interviews',
    "version": '2.0.0',
    "display_name": 'Conduct exit interviews Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of conduct exit interviews status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-conduct-exit-interviews',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-conduct-exit-interviews',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '088ea9f4bc0f676d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/offboard-talent/conduct-exit-interviews'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/adaptive-card-conduct-exit-interviews', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardConductExitInterviews(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardConductExitInterviews'
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
    print(AdaptiveCardConductExitInterviews().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
