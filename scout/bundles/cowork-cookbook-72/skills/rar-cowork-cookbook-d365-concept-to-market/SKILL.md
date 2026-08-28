---
name: "rar-cowork-cookbook-d365-concept-to-market"
description: "A Dynamics 365 Finance & Supply Chain Management expert scoped to the Concept to market end-to-end process - covers 6 L2 areas and 31 L3 processes from the Microsoft Business Process Catalog."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_concept_to_market", "rar_sha256": "345038f3865403f5fdb4eed1857334b4524eb9116dfaffb379922d6f94bb63e9", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/d365_concept_to_market`. The original RAPP
agent is preserved byte-for-byte in `d365_concept_to_market_agent.py` and in the RCI capsule.

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

D365 Concept to market Expert — A Dynamics 365 Finance & Supply Chain Management expert scoped to the Concept to market end-to-end process - covers 6 L2 areas and 31 L3 processes from the Microsoft Business Process Catalog.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-concept-to-market
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_concept_to_market_agent.py` and embedded as the fenced Python below (sha256 345038f3865403f5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_concept_to_market_agent.py` first:

```bash
python3 d365_concept_to_market_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_concept_to_market_agent.py   # or on stdin
python3 d365_concept_to_market_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Concept to market Expert — A Dynamics 365 Finance & Supply Chain Management expert scoped to the Concept to market end-to-end process - covers 6 L2 areas and 31 L3 processes from the Microsoft Business Process Catalog.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-concept-to-market
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_concept_to_market',
    "version": '2.0.1',
    "display_name": 'D365 Concept to market Expert',
    "description": 'A Dynamics 365 Finance & Supply Chain Management expert scoped to the Concept to market end-to-end process - covers 6 L2 areas and 31 L3 processes from the Microsoft Business Process Catalog.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_skill', 'other', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'd365-concept-to-market',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-concept-to-market',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '97e5339c8e1227b5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-24', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market'], 'recipe_category': 'other', 'recipe_type': 'prompt+skill', 'upstream_path': 'concept-to-market/d365-concept-to-market', 'uses_skills': {'custom': ['d365-concept-to-market'], 'ootb': [], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class D365ConceptToMarket(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365ConceptToMarket'
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
    print(D365ConceptToMarket().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
