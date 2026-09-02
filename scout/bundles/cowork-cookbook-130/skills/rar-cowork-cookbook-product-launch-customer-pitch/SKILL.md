---
name: "rar-cowork-cookbook-product-launch-customer-pitch"
description: "Turn a competitor announcement into a sharp, differentiated customer pitch - built and ready before tomorrow's meeting."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/product_launch_customer_pitch", "rar_sha256": "5b3ee2db68235a54b97a3b422dac62f8d8265ec4a62bdbf4e85b5a8495c6157c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "product_launch_customer_pitch_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/product-launch-customer-pitch:87ed06d3e7748b20c7915c179645b111968d542d975492a16977be59ada129d7", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "advanced", "read_only"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/product_launch_customer_pitch`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `product_launch_customer_pitch_agent.py` is
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

Product launch customer pitch — Turn a competitor announcement into a sharp, differentiated customer pitch - built and ready before tomorrow's meeting.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a convert capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/product-launch-customer-pitch
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
      "description": "The input to convert \u2014 path, URL or payload.",
      "type": "string"
    },
    "target_format": {
      "description": "Optional. The desired output format.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `product_launch_customer_pitch_agent.py` and embedded as the fenced Python below (sha256 5b3ee2db68235a54…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `product_launch_customer_pitch_agent.py` first:

```bash
python3 product_launch_customer_pitch_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 product_launch_customer_pitch_agent.py   # or on stdin
python3 product_launch_customer_pitch_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Product launch customer pitch — Turn a competitor announcement into a sharp, differentiated customer pitch - built and ready before tomorrow's meeting.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a convert capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/product-launch-customer-pitch
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/product_launch_customer_pitch',
    "version": '2.0.0',
    "display_name": 'Product launch customer pitch',
    "description": "Turn a competitor announcement into a sharp, differentiated customer pitch - built and ready before tomorrow's meeting.",
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
        "upstream_slug": 'product-launch-customer-pitch',
        "upstream_url": 'https://coworkcookbook.com/recipes/product-launch-customer-pitch',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8500d2c63ef4fe8d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'advanced', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'none', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/pursue-opportunities/nurture-opportunities-and-finalize-the-sale'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/product-launch-customer-pitch', 'uses_skills': {'custom': [], 'ootb': ['Word', 'Excel', 'PowerPoint', 'Meetings', 'Communications'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'convert', 'checks': ['Record counts reconcile between input and output.', 'Every unmapped field is listed with its disposition.', 'A round-trip on the sample is lossless, or the loss is documented and intended.', 'The conversion is rerunnable and produces identical output.'], 'confidence': 1.0, 'deliverable': 'Converted output plus a mapping table, an unmapped-field list, and a reconciliation showing nothing was lost silently.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The input to convert — path, URL or payload.', 'target_format': 'Optional. The desired output format.'}, 'refined_by': 'rules', 'signals': ['word:into'], 'steps': ['Characterise the input completely before writing any mapping: schema, encoding, size, and every optional field actually present.', 'Define the target contract with the same rigour, including what the consumer requires versus merely accepts.', 'Map field by field, and write down the fields with no counterpart — silent drops are how conversions lose data.', 'Decide the policy for the unmappable: fail, default, or carry through as an extension. Never drop by accident.', 'Convert a representative sample first and diff it against the input on the fields that matter.', 'Run the whole set, then reconcile counts and checksums between input and output.'], 'subject_label': 'input to convert', 'verb': 'Convert'}


class ProductLaunchCustomerPitch(BasicAgent):
    """Convert agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ProductLaunchCustomerPitch'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'The input to convert — path, URL or payload.', 'type': 'string'}, 'target_format': {'description': 'Optional. The desired output format.', 'type': 'string'}},
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
    print(ProductLaunchCustomerPitch().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
