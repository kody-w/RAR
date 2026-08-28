---
name: "rar-cowork-cookbook-adaptive-card-configure-segregation-of-duties"
description: "Produces a reusable Adaptive Card JSON snapshot of configure segregation of duties status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_configure_segregation_of_duties", "rar_sha256": "f7555934b74d72a8e8852269bca832b50d502b675c519cae3c54d69bc359666a", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_configure_segregation_of_duties_agent.py` and embedded as the fenced Python below (sha256 f7555934b74d72a8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_configure_segregation_of_duties_agent.py` first:

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
    "version": '2.0.1',
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
