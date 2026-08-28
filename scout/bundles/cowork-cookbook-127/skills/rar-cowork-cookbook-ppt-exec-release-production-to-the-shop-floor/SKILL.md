---
name: "rar-cowork-cookbook-ppt-exec-release-production-to-the-shop-floor"
description: "Generates an executive-ready PowerPoint deck on release production to the shop floor status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_release_production_to_the_shop_floor", "rar_sha256": "300147818b583cda73f5f2fc16a3dba706f10c0f4bb647d558ca2bd32f473cd2", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_release_production_to_the_shop_floor`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_release_production_to_the_shop_floor_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_release_production_to_the_shop_floor_agent.py` and embedded as the fenced Python below (sha256 300147818b583cda…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_release_production_to_the_shop_floor_agent.py` first:

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
    "version": '2.0.1',
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
