---
name: "rar-cowork-cookbook-adaptive-card-generate-ideas"
description: "Produces a reusable Adaptive Card JSON snapshot of generate ideas status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_generate_ideas", "rar_sha256": "da36d6e0ddf239dd5938a21223027b8949e33c3aeca58f72c7f5f58b2d496359", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_generate_ideas`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_generate_ideas_agent.py` and in the RCI capsule.

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

Generate ideas Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of generate ideas status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-generate-ideas
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_generate_ideas_agent.py` and embedded as the fenced Python below (sha256 da36d6e0ddf239dd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_generate_ideas_agent.py` first:

```bash
python3 adaptive_card_generate_ideas_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_generate_ideas_agent.py   # or on stdin
python3 adaptive_card_generate_ideas_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Generate ideas Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of generate ideas status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-generate-ideas
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_generate_ideas',
    "version": '2.0.1',
    "display_name": 'Generate ideas Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of generate ideas status for embedding in dashboards, emails, or Teams.',
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
        "upstream_slug": 'adaptive-card-generate-ideas',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-generate-ideas',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c419e909121e7833',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/research-and-develop-offerings/generate-ideas'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/adaptive-card-generate-ideas', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class AdaptiveCardGenerateIdeas(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardGenerateIdeas'
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
    print(AdaptiveCardGenerateIdeas().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
