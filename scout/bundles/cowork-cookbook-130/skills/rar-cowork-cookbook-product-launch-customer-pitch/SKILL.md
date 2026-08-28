---
name: "rar-cowork-cookbook-product-launch-customer-pitch"
description: "Turn a competitor announcement into a sharp, differentiated customer pitch - built and ready before tomorrow's meeting."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/product_launch_customer_pitch", "rar_sha256": "5b3ee2db68235a54b97a3b422dac62f8d8265ec4a62bdbf4e85b5a8495c6157c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "advanced", "read_only"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/product_launch_customer_pitch`. The original RAPP
agent is preserved byte-for-byte in `product_launch_customer_pitch_agent.py` and in the RCI capsule.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the linked
agent SHA-256 before importing it. If preflight reports a host dependency that
Scout cannot satisfy, use the `brainstem_chat` MCP tool to run the canonical
agent in the user's Brainstem. Never paraphrase the factory or agent into a new
implementation. The generic direct-file commands in the generated Toaster
section are recovery guidance; Scout should prefer the verified runner.

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
