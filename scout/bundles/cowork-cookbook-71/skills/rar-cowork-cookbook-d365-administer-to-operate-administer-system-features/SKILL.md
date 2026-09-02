---
name: "rar-cowork-cookbook-d365-administer-to-operate-administer-system-features"
description: "A Dynamics 365 F&SCM expert scoped to the Administer system features area (a level-2 subdomain of Administer to operate) - covers 20 L3 processes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_administer_to_operate_administer_system_features", "rar_sha256": "c958d1cfb99160ecd3029d1e13c273ba3e35015aebad83f94b470118604be556", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "d365_administer_to_operate_administer_system_features_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/d365-administer-to-operate-administer-system-features:802b78af89aeb6876be62a041f28ca9aa60d1f6c0051c21a00127eea5e50ce53", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/d365_administer_to_operate_administer_system_features`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `d365_administer_to_operate_administer_system_features_agent.py` is
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

D365 Administer system features Expert — A Dynamics 365 F&SCM expert scoped to the Administer system features area (a level-2 subdomain of Administer to operate) - covers 20 L3 processes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-administer-to-operate-administer-system-features
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_administer_to_operate_administer_system_features_agent.py` and embedded as the fenced Python below (sha256 c958d1cfb99160ec…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_administer_to_operate_administer_system_features_agent.py` first:

```bash
python3 d365_administer_to_operate_administer_system_features_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_administer_to_operate_administer_system_features_agent.py   # or on stdin
python3 d365_administer_to_operate_administer_system_features_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Administer system features Expert — A Dynamics 365 F&SCM expert scoped to the Administer system features area (a level-2 subdomain of Administer to operate) - covers 20 L3 processes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-administer-to-operate-administer-system-features
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_administer_to_operate_administer_system_features',
    "version": '2.0.0',
    "display_name": 'D365 Administer system features Expert',
    "description": 'A Dynamics 365 F&SCM expert scoped to the Administer system features area (a level-2 subdomain of Administer to operate) - covers 20 L3 processes.',
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
        "upstream_slug": 'd365-administer-to-operate-administer-system-features',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-administer-to-operate-administer-system-features',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '199f030de51c9810',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-24', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features'], 'recipe_category': 'other', 'recipe_type': 'prompt+skill', 'upstream_path': 'administer-to-operate/d365-administer-to-operate-administer-system-features', 'uses_skills': {'custom': ['d365-administer-to-operate-administer-system-features'], 'ootb': [], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class D365AdministerToOperateAdministerSystemFeatures(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365AdministerToOperateAdministerSystemFeatures'
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
    print(D365AdministerToOperateAdministerSystemFeatures().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
