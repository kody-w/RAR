---
name: "rar-cowork-cookbook-d365-acquire-to-dispose-acquire-assets"
description: "A Dynamics 365 F&SCM expert scoped to the Acquire assets area (a level-2 subdomain of Acquire to dispose) - covers 12 L3 processes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_acquire_to_dispose_acquire_assets", "rar_sha256": "2c0950f3725fad108aaaa71def9e121cfbebbb96b23061659182c4be362eec7a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "d365_acquire_to_dispose_acquire_assets_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/d365-acquire-to-dispose-acquire-assets:5feb53636e581eb5a4ad450a69db8f667349d48a4bdaadb922637308eda54a96", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/d365_acquire_to_dispose_acquire_assets`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `d365_acquire_to_dispose_acquire_assets_agent.py` is
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

D365 Acquire assets Expert — A Dynamics 365 F&SCM expert scoped to the Acquire assets area (a level-2 subdomain of Acquire to dispose) - covers 12 L3 processes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-acquire-to-dispose-acquire-assets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_acquire_to_dispose_acquire_assets_agent.py` and embedded as the fenced Python below (sha256 2c0950f3725fad10…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_acquire_to_dispose_acquire_assets_agent.py` first:

```bash
python3 d365_acquire_to_dispose_acquire_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_acquire_to_dispose_acquire_assets_agent.py   # or on stdin
python3 d365_acquire_to_dispose_acquire_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Acquire assets Expert — A Dynamics 365 F&SCM expert scoped to the Acquire assets area (a level-2 subdomain of Acquire to dispose) - covers 12 L3 processes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-acquire-to-dispose-acquire-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_acquire_to_dispose_acquire_assets',
    "version": '2.0.0',
    "display_name": 'D365 Acquire assets Expert',
    "description": 'A Dynamics 365 F&SCM expert scoped to the Acquire assets area (a level-2 subdomain of Acquire to dispose) - covers 12 L3 processes.',
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
        "upstream_slug": 'd365-acquire-to-dispose-acquire-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-acquire-to-dispose-acquire-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '87f438f8ab12d9b8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-24', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/acquire-assets'], 'recipe_category': 'other', 'recipe_type': 'prompt+skill', 'upstream_path': 'acquire-to-dispose/d365-acquire-to-dispose-acquire-assets', 'uses_skills': {'custom': ['d365-acquire-to-dispose-acquire-assets'], 'ootb': [], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class D365AcquireToDisposeAcquireAssets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365AcquireToDisposeAcquireAssets'
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
    print(D365AcquireToDisposeAcquireAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
