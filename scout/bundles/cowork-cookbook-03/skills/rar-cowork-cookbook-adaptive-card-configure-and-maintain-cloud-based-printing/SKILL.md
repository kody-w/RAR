---
name: "rar-cowork-cookbook-adaptive-card-configure-and-maintain-cloud-based-printing"
description: "Produces a reusable Adaptive Card JSON snapshot of configure and maintain cloud-based printing status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_configure_and_maintain_cloud_based_printing", "rar_sha256": "f9b2cbb310a77a5856940feac81977ac9c1b04a93e6a900008fbbcc51d90e312", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_configure_and_maintain_cloud_based_printing_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-configure-and-maintain-cloud-based-printing:1fc66efa10668ba3dd5acf500b385d77c49f80fa2db21284968f33dbaa05d81b", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_configure_and_maintain_cloud_based_printing`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_configure_and_maintain_cloud_based_printing_agent.py` is
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

Configure and maintain cloud-based printing Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of configure and maintain cloud-based printing status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-configure-and-maintain-cloud-based-printing
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_configure_and_maintain_cloud_based_printing_agent.py` and embedded as the fenced Python below (sha256 f9b2cbb310a77a58…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_configure_and_maintain_cloud_based_printing_agent.py` first:

```bash
python3 adaptive_card_configure_and_maintain_cloud_based_printing_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_configure_and_maintain_cloud_based_printing_agent.py   # or on stdin
python3 adaptive_card_configure_and_maintain_cloud_based_printing_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and maintain cloud-based printing Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of configure and maintain cloud-based printing status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-configure-and-maintain-cloud-based-printing
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_configure_and_maintain_cloud_based_printing',
    "version": '2.0.0',
    "display_name": 'Configure and maintain cloud-based printing Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of configure and maintain cloud-based printing status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-configure-and-maintain-cloud-based-printing',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-configure-and-maintain-cloud-based-printing',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6ea19abd1c8ac20b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-maintain-cloud-based-printing'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/adaptive-card-configure-and-maintain-cloud-based-printing', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AdaptiveCardConfigureAndMaintainCloudBasedPrinting(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardConfigureAndMaintainCloudBasedPrinting'
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
    print(AdaptiveCardConfigureAndMaintainCloudBasedPrinting().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
