---
name: "rar-cowork-cookbook-new-customer-onboarding-automation"
description: "Close a new customer and trigger the full onboarding sequence in one prompt."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/new_customer_onboarding_automation", "rar_sha256": "527ace04654f2b2778dbb8147853d3c79e0e9fcd031fc644dfd4db17d0c3e170", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "new_customer_onboarding_automation_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/new-customer-onboarding-automation:b075636cf664e893680c7cd89847c09fcd74679e3cccf35b5d42620c7daf7e9e", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "advanced", "read_only"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/new_customer_onboarding_automation`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `new_customer_onboarding_automation_agent.py` is
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

New customer onboarding automation — Close a new customer and trigger the full onboarding sequence in one prompt.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/new-customer-onboarding-automation
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `new_customer_onboarding_automation_agent.py` and embedded as the fenced Python below (sha256 527ace04654f2b27…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `new_customer_onboarding_automation_agent.py` first:

```bash
python3 new_customer_onboarding_automation_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 new_customer_onboarding_automation_agent.py   # or on stdin
python3 new_customer_onboarding_automation_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
New customer onboarding automation — Close a new customer and trigger the full onboarding sequence in one prompt.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/new-customer-onboarding-automation
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/new_customer_onboarding_automation',
    "version": '2.0.0',
    "display_name": 'New customer onboarding automation',
    "description": 'Close a new customer and trigger the full onboarding sequence in one prompt.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'prospect_to_quote', 'advanced', 'read_only'],
    "category": 'general',
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
        "upstream_slug": 'new-customer-onboarding-automation',
        "upstream_url": 'https://coworkcookbook.com/recipes/new-customer-onboarding-automation',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '618b1e2db4f33a0f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'advanced', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'none', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/estimate-and-quote-sales/conduct-post-sale-follow-up'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/new-customer-onboarding-automation', 'uses_skills': {'custom': [], 'ootb': ['Word', 'PowerPoint', 'Email', 'Communications', 'Enterprise Search'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['word:trigger'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class NewCustomerOnboardingAutomation(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'NewCustomerOnboardingAutomation'
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
    print(NewCustomerOnboardingAutomation().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
