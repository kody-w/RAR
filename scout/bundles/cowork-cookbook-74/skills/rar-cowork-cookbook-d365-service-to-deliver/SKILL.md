---
name: "rar-cowork-cookbook-d365-service-to-deliver"
description: "A Dynamics 365 Finance & Supply Chain Management expert scoped to the Service to deliver end-to-end process - covers 5 L2 areas and 37 L3 processes from the Microsoft Business Process Catalog."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_service_to_deliver", "rar_sha256": "c8140c41fa4d2f40767dbae313c474cd567b3cedfe9798cb9b0e00ace9ea9193", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "d365_service_to_deliver_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/d365-service-to-deliver:15368f44df2542844fb0e7100608b3ab0cac6c38bf5d91ced9cd46717688089a", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/d365_service_to_deliver`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `d365_service_to_deliver_agent.py` is
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

D365 Service to deliver Expert — A Dynamics 365 Finance & Supply Chain Management expert scoped to the Service to deliver end-to-end process - covers 5 L2 areas and 37 L3 processes from the Microsoft Business Process Catalog.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-service-to-deliver
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_service_to_deliver_agent.py` and embedded as the fenced Python below (sha256 c8140c41fa4d2f40…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_service_to_deliver_agent.py` first:

```bash
python3 d365_service_to_deliver_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_service_to_deliver_agent.py   # or on stdin
python3 d365_service_to_deliver_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Service to deliver Expert — A Dynamics 365 Finance & Supply Chain Management expert scoped to the Service to deliver end-to-end process - covers 5 L2 areas and 37 L3 processes from the Microsoft Business Process Catalog.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-service-to-deliver
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_service_to_deliver',
    "version": '2.0.0',
    "display_name": 'D365 Service to deliver Expert',
    "description": 'A Dynamics 365 Finance & Supply Chain Management expert scoped to the Service to deliver end-to-end process - covers 5 L2 areas and 37 L3 processes from the Microsoft Business Process Catalog.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_skill', 'other', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'd365-service-to-deliver',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-service-to-deliver',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd8f32c481828d42f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-24', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver'], 'recipe_category': 'other', 'recipe_type': 'prompt+skill', 'upstream_path': 'service-to-deliver/d365-service-to-deliver', 'uses_skills': {'custom': ['d365-service-to-deliver'], 'ootb': [], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class D365ServiceToDeliver(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365ServiceToDeliver'
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
    print(D365ServiceToDeliver().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
