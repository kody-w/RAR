---
name: "rar-cowork-cookbook-d365-administer-to-operate"
description: "A Dynamics 365 Finance & Supply Chain Management expert scoped to the Administer to operate end-to-end process - covers 13 L2 areas and 132 L3 processes from the Microsoft Business Process Catalog."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_administer_to_operate", "rar_sha256": "c6a1a4c62921efbcf9c76afa1300a19013c1e600278493703a134b1c14af07a5", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_administer_to_operate_agent.py` and embedded as the fenced Python below (sha256 c6a1a4c62921efbc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_administer_to_operate_agent.py` first:

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
    "version": '2.0.1',
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
