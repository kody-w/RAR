---
name: "rar-cowork-cookbook-adaptive-card-revalue-and-adjust-assets"
description: "Produces a reusable Adaptive Card JSON snapshot of revalue and adjust assets status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_revalue_and_adjust_assets", "rar_sha256": "71f8b65839f05b3399fec6e858bff260c17603ce89801b0078cc2bf258b0f12d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_revalue_and_adjust_assets_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-revalue-and-adjust-assets:0537698e743756193d1e21d2577a8c98eb3c941b35bb6509ebca5e52762ec6dc", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_revalue_and_adjust_assets`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_revalue_and_adjust_assets_agent.py` is
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

Revalue and adjust assets Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of revalue and adjust assets status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-revalue-and-adjust-assets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_revalue_and_adjust_assets_agent.py` and embedded as the fenced Python below (sha256 71f8b65839f05b33…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_revalue_and_adjust_assets_agent.py` first:

```bash
python3 adaptive_card_revalue_and_adjust_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_revalue_and_adjust_assets_agent.py   # or on stdin
python3 adaptive_card_revalue_and_adjust_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Revalue and adjust assets Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of revalue and adjust assets status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-revalue-and-adjust-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_revalue_and_adjust_assets',
    "version": '2.0.0',
    "display_name": 'Revalue and adjust assets Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of revalue and adjust assets status for embedding in dashboards, emails, or Teams.',
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
        "upstream_slug": 'adaptive-card-revalue-and-adjust-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-revalue-and-adjust-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e509bc95d41b7804',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/manage-active-assets/revalue-and-adjust-assets'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/adaptive-card-revalue-and-adjust-assets', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AdaptiveCardRevalueAndAdjustAssets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardRevalueAndAdjustAssets'
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
    print(AdaptiveCardRevalueAndAdjustAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
