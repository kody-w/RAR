---
name: "rar-cowork-cookbook-demo-data-configure-and-maintain-cloud-based-printing"
description: "Generates and creates realistic demo records for configure and maintain cloud-based printing in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_configure_and_maintain_cloud_based_printing", "rar_sha256": "e4456c6e51b07f0c8c73ad505286edc5a26d6cc7cd57fec3f96c9fe74c564255", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_configure_and_maintain_cloud_based_printing_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-configure-and-maintain-cloud-based-printing:d4130fbce4cbbf2d6685749997ffcc336220b368e9b07560ef0dea55d7fe05b1", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_configure_and_maintain_cloud_based_printing`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_configure_and_maintain_cloud_based_printing_agent.py` is
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

Configure and maintain cloud-based printing Demo Data Generator — Generates and creates realistic demo records for configure and maintain cloud-based printing in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-configure-and-maintain-cloud-based-printing
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_configure_and_maintain_cloud_based_printing_agent.py` and embedded as the fenced Python below (sha256 e4456c6e51b07f0c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_configure_and_maintain_cloud_based_printing_agent.py` first:

```bash
python3 demo_data_configure_and_maintain_cloud_based_printing_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_configure_and_maintain_cloud_based_printing_agent.py   # or on stdin
python3 demo_data_configure_and_maintain_cloud_based_printing_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and maintain cloud-based printing Demo Data Generator — Generates and creates realistic demo records for configure and maintain cloud-based printing in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-configure-and-maintain-cloud-based-printing
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_configure_and_maintain_cloud_based_printing',
    "version": '2.0.0',
    "display_name": 'Configure and maintain cloud-based printing Demo Data Generator',
    "description": 'Generates and creates realistic demo records for configure and maintain cloud-based printing in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-configure-and-maintain-cloud-based-printing',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-configure-and-maintain-cloud-based-printing',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1e846f414e9978dd',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-maintain-cloud-based-printing'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/demo-data-configure-and-maintain-cloud-based-printing', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DemoDataConfigureAndMaintainCloudBasedPrinting(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataConfigureAndMaintainCloudBasedPrinting'
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
    print(DemoDataConfigureAndMaintainCloudBasedPrinting().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
