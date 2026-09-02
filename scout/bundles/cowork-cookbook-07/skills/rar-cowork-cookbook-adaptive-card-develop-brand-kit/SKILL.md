---
name: "rar-cowork-cookbook-adaptive-card-develop-brand-kit"
description: "Produces a reusable Adaptive Card JSON snapshot of develop brand kit status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_develop_brand_kit", "rar_sha256": "40b2e906c692b66e79f0f89672aa5693d6b658a5b2d808c01b9fb5aec5a7ebcd", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_develop_brand_kit_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-develop-brand-kit:3290ba800c24df932e7b0bfc0692876271aa818cd98f7674214865ebe5045a69", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_develop_brand_kit`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_develop_brand_kit_agent.py` is
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

Develop brand kit Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of develop brand kit status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-develop-brand-kit
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_develop_brand_kit_agent.py` and embedded as the fenced Python below (sha256 40b2e906c692b66e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_develop_brand_kit_agent.py` first:

```bash
python3 adaptive_card_develop_brand_kit_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_develop_brand_kit_agent.py   # or on stdin
python3 adaptive_card_develop_brand_kit_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop brand kit Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of develop brand kit status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-develop-brand-kit
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_develop_brand_kit',
    "version": '2.0.0',
    "display_name": 'Develop brand kit Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of develop brand kit status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-develop-brand-kit',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-develop-brand-kit',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '137fe3fa21cf8525',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/develop-marketing-strategy/develop-brand-kit'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/adaptive-card-develop-brand-kit', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardDevelopBrandKit(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDevelopBrandKit'
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
    print(AdaptiveCardDevelopBrandKit().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
