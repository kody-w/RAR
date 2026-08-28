---
name: "rar-cowork-cookbook-adaptive-card-configure-segregation-of-duties"
description: "Produces a reusable Adaptive Card JSON snapshot of configure segregation of duties status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_configure_segregation_of_duties", "rar_sha256": "b51241db1ab37ea712af1889c131270b72266bde6495ebce8e2d05d587a1763e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_configure_segregation_of_duties`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_configure_segregation_of_duties_agent.py` and in the RCI capsule.

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
