---
name: "rar-cowork-cookbook-d365-concept-to-market"
description: "A Dynamics 365 Finance & Supply Chain Management expert scoped to the Concept to market end-to-end process - covers 6 L2 areas and 31 L3 processes from the Microsoft Business Process Catalog."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_concept_to_market", "rar_sha256": "2b60df5c23ae412bc6c9391d33e41cde6a3a01bd6c776b56d3789b61bdd85857", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "d365_concept_to_market_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/d365-concept-to-market:cb6d544dcb49dd10167acd92c13d31b43b100f8b43ea5dcd02c5147f67c7364c", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/d365_concept_to_market`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `d365_concept_to_market_agent.py` is
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
