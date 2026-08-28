---
name: "rar-cowork-cookbook-d365-acquire-to-dispose"
description: "A Dynamics 365 Finance & Supply Chain Management expert scoped to the Acquire to dispose end-to-end process - covers 6 L2 areas and 43 L3 processes from the Microsoft Business Process Catalog."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_acquire_to_dispose", "rar_sha256": "a83e55cc7d5b4b8821d3bbcfb55bcf52082f53b665f051900f155b58850c206f", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/d365_acquire_to_dispose`. The original RAPP
agent is preserved byte-for-byte in `d365_acquire_to_dispose_agent.py` and in the RCI capsule.

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

D365 Acquire to dispose Expert — A Dynamics 365 Finance & Supply Chain Management expert scoped to the Acquire to dispose end-to-end process - covers 6 L2 areas and 43 L3 processes from the Microsoft Business Process Catalog.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-acquire-to-dispose
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_acquire_to_dispose_agent.py` and embedded as the fenced Python below (sha256 a83e55cc7d5b4b88…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_acquire_to_dispose_agent.py` first:

```bash
python3 d365_acquire_to_dispose_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_acquire_to_dispose_agent.py   # or on stdin
python3 d365_acquire_to_dispose_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Acquire to dispose Expert — A Dynamics 365 Finance & Supply Chain Management expert scoped to the Acquire to dispose end-to-end process - covers 6 L2 areas and 43 L3 processes from the Microsoft Business Process Catalog.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-acquire-to-dispose
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_acquire_to_dispose',
    "version": '2.0.1',
    "display_name": 'D365 Acquire to dispose Expert',
    "description": 'A Dynamics 365 Finance & Supply Chain Management expert scoped to the Acquire to dispose end-to-end process - covers 6 L2 areas and 43 L3 processes from the Microsoft Business Process Catalog.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_skill', 'other', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'd365-acquire-to-dispose',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-acquire-to-dispose',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9a97a988bf83deb0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-24', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose'], 'recipe_category': 'other', 'recipe_type': 'prompt+skill', 'upstream_path': 'acquire-to-dispose/d365-acquire-to-dispose', 'uses_skills': {'custom': ['d365-acquire-to-dispose'], 'ootb': [], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class D365AcquireToDispose(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365AcquireToDispose'
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
    print(D365AcquireToDispose().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
