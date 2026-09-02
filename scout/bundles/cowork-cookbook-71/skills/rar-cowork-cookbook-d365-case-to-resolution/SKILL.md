---
name: "rar-cowork-cookbook-d365-case-to-resolution"
description: "A Dynamics 365 Finance & Supply Chain Management expert scoped to the Case to resolution end-to-end process - covers 5 L2 areas and 37 L3 processes from the Microsoft Business Process Catalog."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_case_to_resolution", "rar_sha256": "9c937b4b0264515e811f96196f22e326b3cf9795511e0a84931c5381509a28f7", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "d365_case_to_resolution_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/d365-case-to-resolution:a44ea76034fe2776c81dae9a9d45ad5f7407d411cafa5b2ef0a416f56bc92aa0", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/d365_case_to_resolution`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `d365_case_to_resolution_agent.py` is
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

D365 Case to resolution Expert — A Dynamics 365 Finance & Supply Chain Management expert scoped to the Case to resolution end-to-end process - covers 5 L2 areas and 37 L3 processes from the Microsoft Business Process Catalog.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-case-to-resolution
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_case_to_resolution_agent.py` and embedded as the fenced Python below (sha256 9c937b4b0264515e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_case_to_resolution_agent.py` first:

```bash
python3 d365_case_to_resolution_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_case_to_resolution_agent.py   # or on stdin
python3 d365_case_to_resolution_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Case to resolution Expert — A Dynamics 365 Finance & Supply Chain Management expert scoped to the Case to resolution end-to-end process - covers 5 L2 areas and 37 L3 processes from the Microsoft Business Process Catalog.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-case-to-resolution
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_case_to_resolution',
    "version": '2.0.0',
    "display_name": 'D365 Case to resolution Expert',
    "description": 'A Dynamics 365 Finance & Supply Chain Management expert scoped to the Case to resolution end-to-end process - covers 5 L2 areas and 37 L3 processes from the Microsoft Business Process Catalog.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_skill', 'other', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'd365-case-to-resolution',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-case-to-resolution',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6c365a36303644e3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-24', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution'], 'recipe_category': 'other', 'recipe_type': 'prompt+skill', 'upstream_path': 'case-to-resolution/d365-case-to-resolution', 'uses_skills': {'custom': ['d365-case-to-resolution'], 'ootb': [], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class D365CaseToResolution(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365CaseToResolution'
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
    print(D365CaseToResolution().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
