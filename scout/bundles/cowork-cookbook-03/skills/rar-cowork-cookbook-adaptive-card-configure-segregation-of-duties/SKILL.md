---
name: "rar-cowork-cookbook-adaptive-card-configure-segregation-of-duties"
description: "Produces a reusable Adaptive Card JSON snapshot of configure segregation of duties status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_configure_segregation_of_duties", "rar_sha256": "b51241db1ab37ea712af1889c131270b72266bde6495ebce8e2d05d587a1763e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_configure_segregation_of_duties_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-configure-segregation-of-duties:948849e8562df3b875c10ccefc6709afd6058c064f8daf486a9bdbc2915b5187", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_configure_segregation_of_duties`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_configure_segregation_of_duties_agent.py` is
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

Configure segregation of duties Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of configure segregation of duties status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-configure-segregation-of-duties
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_configure_segregation_of_duties_agent.py` and embedded as the fenced Python below (sha256 b51241db1ab37ea7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_configure_segregation_of_duties_agent.py` first:

```bash
python3 adaptive_card_configure_segregation_of_duties_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_configure_segregation_of_duties_agent.py   # or on stdin
python3 adaptive_card_configure_segregation_of_duties_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure segregation of duties Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of configure segregation of duties status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-configure-segregation-of-duties
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_configure_segregation_of_duties',
    "version": '2.0.0',
    "display_name": 'Configure segregation of duties Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of configure segregation of duties status for embedding in dashboards, emails, or Teams.',
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
        "upstream_slug": 'adaptive-card-configure-segregation-of-duties',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-configure-segregation-of-duties',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '96acc2fb25272b6a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-access-and-security/configure-segregation-of-duties'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/adaptive-card-configure-segregation-of-duties', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AdaptiveCardConfigureSegregationOfDuties(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardConfigureSegregationOfDuties'
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
    print(AdaptiveCardConfigureSegregationOfDuties().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
