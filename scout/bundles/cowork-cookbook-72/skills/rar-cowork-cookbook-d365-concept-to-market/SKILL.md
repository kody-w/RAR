---
name: "rar-cowork-cookbook-d365-concept-to-market"
description: "A Dynamics 365 Finance & Supply Chain Management expert scoped to the Concept to market end-to-end process - covers 6 L2 areas and 31 L3 processes from the Microsoft Business Process Catalog."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_concept_to_market", "rar_sha256": "2b60df5c23ae412bc6c9391d33e41cde6a3a01bd6c776b56d3789b61bdd85857", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_concept_to_market_agent.py` and embedded as the fenced Python below (sha256 2b60df5c23ae412b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_concept_to_market_agent.py` first:

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
    "version": '2.0.0',
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
