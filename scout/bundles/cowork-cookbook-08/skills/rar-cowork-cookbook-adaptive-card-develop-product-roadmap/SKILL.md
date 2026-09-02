---
name: "rar-cowork-cookbook-adaptive-card-develop-product-roadmap"
description: "Produces a reusable Adaptive Card JSON snapshot of develop product roadmap status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_develop_product_roadmap", "rar_sha256": "048d36a6b6ef5b17968eca32e0b96237deba6ce59e7929d028280fa20e577bba", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_develop_product_roadmap_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-develop-product-roadmap:f8628d62b7e9b91a03e0c050eebe25695765d86df58dc3c0480bf3d48c30786a", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_develop_product_roadmap`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_develop_product_roadmap_agent.py` is
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

Develop product roadmap Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of develop product roadmap status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-develop-product-roadmap
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_develop_product_roadmap_agent.py` and embedded as the fenced Python below (sha256 048d36a6b6ef5b17…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_develop_product_roadmap_agent.py` first:

```bash
python3 adaptive_card_develop_product_roadmap_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_develop_product_roadmap_agent.py   # or on stdin
python3 adaptive_card_develop_product_roadmap_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop product roadmap Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of develop product roadmap status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-develop-product-roadmap
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_develop_product_roadmap',
    "version": '2.0.0',
    "display_name": 'Develop product roadmap Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of develop product roadmap status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-develop-product-roadmap',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-develop-product-roadmap',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8ef07f7a09dac069',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/develop-product-strategy/develop-product-roadmap'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/adaptive-card-develop-product-roadmap', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardDevelopProductRoadmap(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDevelopProductRoadmap'
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
    print(AdaptiveCardDevelopProductRoadmap().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
