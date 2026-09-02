---
name: "rar-cowork-cookbook-partner-and-channel-activation-kit"
description: "Adapt the [Product/Campaign name] launch materials for partners and channel teams and route them for review."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/partner_and_channel_activation_kit", "rar_sha256": "671861042a9a2b2268b882baace5e9f62f131178ab5294e1722fe71b76c3bf36", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "partner_and_channel_activation_kit_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/partner-and-channel-activation-kit:2e160485fca868e124521bea69cfc6d2886bd028fa6b9f7568636ee1c6d4984b", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "concept_to_market", "intermediate", "read_only"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/partner_and_channel_activation_kit`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `partner_and_channel_activation_kit_agent.py` is
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

Partner and channel activation kit — Adapt the [Product/Campaign name] launch materials for partners and channel teams and route them for review.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/partner-and-channel-activation-kit
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
    "criteria": {
      "description": "Optional. The standard to review against, if narrower than the default.",
      "type": "string"
    },
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
      "description": "What is being reviewed \u2014 a file path, URL, document or system.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `partner_and_channel_activation_kit_agent.py` and embedded as the fenced Python below (sha256 671861042a9a2b22…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `partner_and_channel_activation_kit_agent.py` first:

```bash
python3 partner_and_channel_activation_kit_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 partner_and_channel_activation_kit_agent.py   # or on stdin
python3 partner_and_channel_activation_kit_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Partner and channel activation kit — Adapt the [Product/Campaign name] launch materials for partners and channel teams and route them for review.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/partner-and-channel-activation-kit
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/partner_and_channel_activation_kit',
    "version": '2.0.0',
    "display_name": 'Partner and channel activation kit',
    "description": 'Adapt the [Product/Campaign name] launch materials for partners and channel teams and route them for review.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'concept_to_market', 'intermediate', 'read_only'],
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
        "upstream_slug": 'partner-and-channel-activation-kit',
        "upstream_url": 'https://coworkcookbook.com/recipes/partner-and-channel-activation-kit',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '057c7b6e05b24458',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'none', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/prepare-marketing-campaigns/create-marketing-material'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/partner-and-channel-activation-kit', 'uses_skills': {'custom': [], 'ootb': ['Word', 'Excel', 'Email', 'Communications'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 1.0, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['word:review'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class PartnerAndChannelActivationKit(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PartnerAndChannelActivationKit'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'criteria': {'description': 'Optional. The standard to review against, if narrower than the default.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What is being reviewed — a file path, URL, document or system.', 'type': 'string'}},
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
    print(PartnerAndChannelActivationKit().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
