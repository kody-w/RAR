---
name: "rar-cowork-cookbook-d365-acquire-to-dispose"
description: "A Dynamics 365 Finance & Supply Chain Management expert scoped to the Acquire to dispose end-to-end process - covers 6 L2 areas and 43 L3 processes from the Microsoft Business Process Catalog."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_acquire_to_dispose", "rar_sha256": "c12fa47287fb4511c647cfc873118d8f03d95526d0e6f5302836de219278dffe", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "d365_acquire_to_dispose_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/d365-acquire-to-dispose:29ecb7b4ede7e0eebb27ef31e559d688dcfc789334c7d9980f4d22805aa4bc55", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/d365_acquire_to_dispose`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `d365_acquire_to_dispose_agent.py` is
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_acquire_to_dispose_agent.py` and embedded as the fenced Python below (sha256 c12fa47287fb4511…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_acquire_to_dispose_agent.py` first:

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
    "version": '2.0.0',
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
