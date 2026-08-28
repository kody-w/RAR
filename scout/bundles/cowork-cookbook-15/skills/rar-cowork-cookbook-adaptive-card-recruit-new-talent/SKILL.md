---
name: "rar-cowork-cookbook-adaptive-card-recruit-new-talent"
description: "Produces a reusable Adaptive Card JSON snapshot of recruit new talent status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_recruit_new_talent", "rar_sha256": "de09f294bbae1e421b05a96e75dfb7ec6da413e5614834947d3793ef9022ae8c", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_recruit_new_talent`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_recruit_new_talent_agent.py` and in the RCI capsule.

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

Recruit new talent Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of recruit new talent status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-recruit-new-talent
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_recruit_new_talent_agent.py` and embedded as the fenced Python below (sha256 de09f294bbae1e42…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_recruit_new_talent_agent.py` first:

```bash
python3 adaptive_card_recruit_new_talent_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_recruit_new_talent_agent.py   # or on stdin
python3 adaptive_card_recruit_new_talent_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Recruit new talent Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of recruit new talent status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-recruit-new-talent
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_recruit_new_talent',
    "version": '2.0.1',
    "display_name": 'Recruit new talent Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of recruit new talent status for embedding in dashboards, emails, or Teams.',
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
        "upstream_slug": 'adaptive-card-recruit-new-talent',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-recruit-new-talent',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'bff4c1bd4aad497b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/recruit-and-onboard-talent/recruit-new-talent'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/adaptive-card-recruit-new-talent', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardRecruitNewTalent(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardRecruitNewTalent'
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
    print(AdaptiveCardRecruitNewTalent().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
