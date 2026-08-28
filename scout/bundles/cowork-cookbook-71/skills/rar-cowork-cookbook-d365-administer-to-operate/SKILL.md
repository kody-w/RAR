---
name: "rar-cowork-cookbook-d365-administer-to-operate"
description: "A Dynamics 365 Finance & Supply Chain Management expert scoped to the Administer to operate end-to-end process - covers 13 L2 areas and 132 L3 processes from the Microsoft Business Process Catalog."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_administer_to_operate", "rar_sha256": "7426e52d07d3c45a633a8d0203ed58a64da9533f2b859dddbd2ec23f331fda7a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/d365_administer_to_operate`. The original RAPP
agent is preserved byte-for-byte in `d365_administer_to_operate_agent.py` and in the RCI capsule.

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

D365 Administer to operate Expert — A Dynamics 365 Finance & Supply Chain Management expert scoped to the Administer to operate end-to-end process - covers 13 L2 areas and 132 L3 processes from the Microsoft Business Process Catalog.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-administer-to-operate
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_administer_to_operate_agent.py` and embedded as the fenced Python below (sha256 7426e52d07d3c45a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_administer_to_operate_agent.py` first:

```bash
python3 d365_administer_to_operate_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_administer_to_operate_agent.py   # or on stdin
python3 d365_administer_to_operate_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Administer to operate Expert — A Dynamics 365 Finance & Supply Chain Management expert scoped to the Administer to operate end-to-end process - covers 13 L2 areas and 132 L3 processes from the Microsoft Business Process Catalog.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-administer-to-operate
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_administer_to_operate',
    "version": '2.0.0',
    "display_name": 'D365 Administer to operate Expert',
    "description": 'A Dynamics 365 Finance & Supply Chain Management expert scoped to the Administer to operate end-to-end process - covers 13 L2 areas and 132 L3 processes from the Microsoft Business Process Catalog.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_skill', 'other', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'd365-administer-to-operate',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-administer-to-operate',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5a7c78e64d4ef45c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-24', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate'], 'recipe_category': 'other', 'recipe_type': 'prompt+skill', 'upstream_path': 'administer-to-operate/d365-administer-to-operate', 'uses_skills': {'custom': ['d365-administer-to-operate'], 'ootb': [], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class D365AdministerToOperate(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365AdministerToOperate'
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
    print(D365AdministerToOperate().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
