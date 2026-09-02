---
name: "rar-cowork-cookbook-adaptive-card-identify-strategic-initiatives"
description: "Produces a reusable Adaptive Card JSON snapshot of identify strategic initiatives status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_identify_strategic_initiatives", "rar_sha256": "69057dd60e40ccbb810b1f5ad7761bdba169a94697d40ae81056f5615415419b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_identify_strategic_initiatives_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-identify-strategic-initiatives:aa062c04993cc1a0d5b25755e1a25439ce9def7c58c66406e6154fde152e70ab", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_identify_strategic_initiatives`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_identify_strategic_initiatives_agent.py` is
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

Identify strategic initiatives Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of identify strategic initiatives status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-identify-strategic-initiatives
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_identify_strategic_initiatives_agent.py` and embedded as the fenced Python below (sha256 69057dd60e40ccbb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_identify_strategic_initiatives_agent.py` first:

```bash
python3 adaptive_card_identify_strategic_initiatives_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_identify_strategic_initiatives_agent.py   # or on stdin
python3 adaptive_card_identify_strategic_initiatives_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Identify strategic initiatives Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of identify strategic initiatives status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-identify-strategic-initiatives
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_identify_strategic_initiatives',
    "version": '2.0.0',
    "display_name": 'Identify strategic initiatives Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of identify strategic initiatives status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-identify-strategic-initiatives',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-identify-strategic-initiatives',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '81e43e4f7032681f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/develop-business-strategy/identify-strategic-initiatives'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/adaptive-card-identify-strategic-initiatives', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardIdentifyStrategicInitiatives(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardIdentifyStrategicInitiatives'
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
    print(AdaptiveCardIdentifyStrategicInitiatives().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
