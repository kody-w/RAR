---
name: "rar-cowork-cookbook-dashboard-replace-an-asset"
description: "Produces a self-contained interactive HTML dashboard for replace an asset - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_replace_an_asset", "rar_sha256": "7ff5bb0d3efe3bce4c4442fdd57ee76112c2976df098db6d791f567459fe3941", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_replace_an_asset_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-replace-an-asset:1b5919fa6882099e59c1bbf6ec6987eea4e665372ff90a1480770cbb612163f7", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_replace_an_asset`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_replace_an_asset_agent.py` is
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

Replace an asset Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for replace an asset - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-replace-an-asset
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_replace_an_asset_agent.py` and embedded as the fenced Python below (sha256 7ff5bb0d3efe3bce…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_replace_an_asset_agent.py` first:

```bash
python3 dashboard_replace_an_asset_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_replace_an_asset_agent.py   # or on stdin
python3 dashboard_replace_an_asset_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Replace an asset Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for replace an asset - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-replace-an-asset
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_replace_an_asset',
    "version": '2.0.0',
    "display_name": 'Replace an asset Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for replace an asset - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-replace-an-asset',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-replace-an-asset',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1729444ecdddc1be',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/dispose-of-assets/replace-an-asset'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/dashboard-replace-an-asset', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class DashboardReplaceAnAsset(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardReplaceAnAsset'
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
    print(DashboardReplaceAnAsset().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
