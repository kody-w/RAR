---
name: "rar-cowork-cookbook-product-launch-customer-pitch"
description: "Turn a competitor announcement into a sharp, differentiated customer pitch - built and ready before tomorrow's meeting."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/product_launch_customer_pitch", "rar_sha256": "8a3d0dbbbcbf0c3a3fa8435b26cbc0a94c74f13ca340bec01e1fdfab3a28c921", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "advanced", "read_only"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `product_launch_customer_pitch_agent.py` and embedded as the fenced Python below (sha256 8a3d0dbbbcbf0c3a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `product_launch_customer_pitch_agent.py` first:

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
    "version": '2.0.1',
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
