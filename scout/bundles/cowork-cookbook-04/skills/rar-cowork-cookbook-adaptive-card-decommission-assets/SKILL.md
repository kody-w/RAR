---
name: "rar-cowork-cookbook-adaptive-card-decommission-assets"
description: "Produces a reusable Adaptive Card JSON snapshot of decommission assets status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_decommission_assets", "rar_sha256": "b57f65510120117f5a861b2dbeac139cb4fab0cc02f5bba0ec36e61f5dca302a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_decommission_assets_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-decommission-assets:a9678c05cfc0e32c7a84bb1a05dd698289441d65a64cc8f71b0b52687ae751c6", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_decommission_assets`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_decommission_assets_agent.py` is
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

Decommission assets Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of decommission assets status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-decommission-assets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_decommission_assets_agent.py` and embedded as the fenced Python below (sha256 b57f65510120117f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_decommission_assets_agent.py` first:

```bash
python3 adaptive_card_decommission_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_decommission_assets_agent.py   # or on stdin
python3 adaptive_card_decommission_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Decommission assets Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of decommission assets status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-decommission-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_decommission_assets',
    "version": '2.0.0',
    "display_name": 'Decommission assets Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of decommission assets status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'adaptive-card-decommission-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-decommission-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '378227b6827035ec',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/dispose-of-assets/decommission-assets'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/adaptive-card-decommission-assets', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AdaptiveCardDecommissionAssets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDecommissionAssets'
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
    print(AdaptiveCardDecommissionAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
