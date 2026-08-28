---
name: "rar-cowork-cookbook-ppt-exec-release-production-to-the-shop-floor"
description: "Generates an executive-ready PowerPoint deck on release production to the shop floor status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_release_production_to_the_shop_floor", "rar_sha256": "d7c8401a42142c810c74a07b6a091b17f95290ea8a35c79391e1d34e97fe32fb", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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
