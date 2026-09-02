---
name: "rar-cowork-cookbook-ppt-exec-release-production-to-the-shop-floor"
description: "Generates an executive-ready PowerPoint deck on release production to the shop floor status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_release_production_to_the_shop_floor", "rar_sha256": "d7c8401a42142c810c74a07b6a091b17f95290ea8a35c79391e1d34e97fe32fb", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_release_production_to_the_shop_floor_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-release-production-to-the-shop-floor:ef3508bc703ab200188166fb625a884b2aaa22afe27b7c3ca3680019d69f5d41", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_release_production_to_the_shop_floor`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_release_production_to_the_shop_floor_agent.py` is
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

Release production to the shop floor Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on release production to the shop floor status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-release-production-to-the-shop-floor
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_release_production_to_the_shop_floor_agent.py` and embedded as the fenced Python below (sha256 d7c8401a42142c81…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_release_production_to_the_shop_floor_agent.py` first:

```bash
python3 ppt_exec_release_production_to_the_shop_floor_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_release_production_to_the_shop_floor_agent.py   # or on stdin
python3 ppt_exec_release_production_to_the_shop_floor_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Release production to the shop floor Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on release production to the shop floor status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-release-production-to-the-shop-floor
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_release_production_to_the_shop_floor',
    "version": '2.0.0',
    "display_name": 'Release production to the shop floor Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on release production to the shop floor status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-release-production-to-the-shop-floor',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-release-production-to-the-shop-floor',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'fe24c243ec08efd6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/plan-production-operations/release-production-to-the-shop-floor'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/ppt-exec-release-production-to-the-shop-floor', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecReleaseProductionToTheShopFloor(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecReleaseProductionToTheShopFloor'
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
    print(PptExecReleaseProductionToTheShopFloor().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
