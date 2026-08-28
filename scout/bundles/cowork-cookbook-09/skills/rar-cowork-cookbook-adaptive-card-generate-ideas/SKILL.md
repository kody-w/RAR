---
name: "rar-cowork-cookbook-adaptive-card-generate-ideas"
description: "Produces a reusable Adaptive Card JSON snapshot of generate ideas status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_generate_ideas", "rar_sha256": "26e4e642b49fd7115e63ea8fe6d698ff35d3f10d0e4ff585339cbaae441c2060", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_generate_ideas_agent.py` and embedded as the fenced Python below (sha256 26e4e642b49fd711…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_generate_ideas_agent.py` first:

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
    "version": '2.0.0',
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
