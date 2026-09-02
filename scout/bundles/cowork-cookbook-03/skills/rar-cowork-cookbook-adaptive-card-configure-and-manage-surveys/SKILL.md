---
name: "rar-cowork-cookbook-adaptive-card-configure-and-manage-surveys"
description: "Produces a reusable Adaptive Card JSON snapshot of configure and manage surveys status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_configure_and_manage_surveys", "rar_sha256": "07e38d68b1f98146076b934d580255d93cb10d5f619fccf58a08e862e757096c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_configure_and_manage_surveys_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-configure-and-manage-surveys:a63fafd36f4e37bd376326953d9cecbacb2780c11931f3f70c1622fc529310ee", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_configure_and_manage_surveys`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_configure_and_manage_surveys_agent.py` is
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

Configure and manage surveys Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of configure and manage surveys status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-configure-and-manage-surveys
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_configure_and_manage_surveys_agent.py` and embedded as the fenced Python below (sha256 07e38d68b1f98146…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_configure_and_manage_surveys_agent.py` first:

```bash
python3 adaptive_card_configure_and_manage_surveys_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_configure_and_manage_surveys_agent.py   # or on stdin
python3 adaptive_card_configure_and_manage_surveys_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and manage surveys Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of configure and manage surveys status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-configure-and-manage-surveys
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_configure_and_manage_surveys',
    "version": '2.0.0',
    "display_name": 'Configure and manage surveys Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of configure and manage surveys status for embedding in dashboards, emails, or Teams.',
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
        "upstream_slug": 'adaptive-card-configure-and-manage-surveys',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-configure-and-manage-surveys',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd608cd72fc7da7d8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-manage-surveys'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/adaptive-card-configure-and-manage-surveys', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AdaptiveCardConfigureAndManageSurveys(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardConfigureAndManageSurveys'
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
    print(AdaptiveCardConfigureAndManageSurveys().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
