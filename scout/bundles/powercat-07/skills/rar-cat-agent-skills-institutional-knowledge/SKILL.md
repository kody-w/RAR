---
name: "rar-cat-agent-skills-institutional-knowledge"
description: "Preserve a departing senior leader's institutional knowledge \u2014 decisions, rationale, relationships, and tribal knowledge \u2014 by mining their M365 signals into a structured, multi-phase archive a successor can ground on."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/institutional_knowledge", "rar_sha256": "dea44d1c2bf0f7803a9848d3d09ce9e461afd0b5dad71a53f21c4e8f374a544b", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Srinivas Varukala", "tags": ["knowledge", "handoff", "leadership", "m365", "offboarding", "documentation", "productivity"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/institutional_knowledge`. The original RAPP
agent is preserved byte-for-byte in `institutional_knowledge_agent.py` and in the RCI capsule.

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

Institutional Knowledge Archivist — Preserve a departing senior leader's institutional knowledge — decisions, rationale, relationships, and tribal knowledge — by mining their M365 signals into a structured, multi-phase archive a successor can ground on.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a convert capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#institutional-knowledge
  Upstream author: Srinivas Varukala
  Upstream version: 1.0.1
  Licence        : unverified (unverified — indexed, never republished)

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `institutional_knowledge_agent.py` and embedded as the fenced Python below (sha256 dea44d1c2bf0f780…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `institutional_knowledge_agent.py` first:

```bash
python3 institutional_knowledge_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 institutional_knowledge_agent.py   # or on stdin
python3 institutional_knowledge_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Institutional Knowledge Archivist — Preserve a departing senior leader's institutional knowledge — decisions, rationale, relationships, and tribal knowledge — by mining their M365 signals into a structured, multi-phase archive a successor can ground on.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a convert capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#institutional-knowledge
  Upstream author: Srinivas Varukala
  Upstream version: 1.0.1
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/institutional_knowledge',
    "version": '3.0.3',
    "display_name": 'Institutional Knowledge Archivist',
    "description": "Preserve a departing senior leader's institutional knowledge — decisions, rationale, relationships, and tribal knowledge — by mining their M365 signals into a structured, multi-phase archive a successor can ground on.",
    "author": 'Srinivas Varukala',
    "tags": ['knowledge', 'handoff', 'leadership', 'm365', 'offboarding', 'documentation', 'productivity'],
    "category": 'general',
    "quality_tier": "frontier",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cat-agent-skills',
        "source_name": 'CAT Agent Skills',
        "source_url": 'https://microsoft.github.io/cat-agent-skills/',
        "upstream_slug": 'institutional-knowledge',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#institutional-knowledge',
        "upstream_version": '1.0.1',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '3ac7896e76455716',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Cowork', 'Scout'],
}


try:
    from agents.basic_agent import BasicAgent
except ModuleNotFoundError:
    class BasicAgent:
        def __init__(self, name, metadata):
            self.name = name
            self.metadata = metadata


# The toasted capability, generated by @kody-w/skill_toaster_agent. A licensed
# recipe entry carries the upstream recipe verbatim (with attribution) in
# _SPEC["recipe"]; a metadata-only entry carries RAR's own method for that shape
# of work. See the module docstring for which this is.
_SPEC = {'archetype': 'convert', 'checks': ['Record counts reconcile between input and output.', 'Every unmapped field is listed with its disposition.', 'A round-trip on the sample is lossless, or the loss is documented and intended.', 'The conversion is rerunnable and produces identical output.'], 'confidence': 1.0, 'deliverable': 'Converted output plus a mapping table, an unmapped-field list, and a reconciliation showing nothing was lost silently.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The input to convert — path, URL or payload.', 'target_format': 'Optional. The desired output format.'}, 'refined_by': 'rules', 'signals': ['word:into'], 'steps': ['Characterise the input completely before writing any mapping: schema, encoding, size, and every optional field actually present.', 'Define the target contract with the same rigour, including what the consumer requires versus merely accepts.', 'Map field by field, and write down the fields with no counterpart — silent drops are how conversions lose data.', 'Decide the policy for the unmappable: fail, default, or carry through as an extension. Never drop by accident.', 'Convert a representative sample first and diff it against the input on the fields that matter.', 'Run the whole set, then reconcile counts and checksums between input and output.'], 'subject_label': 'input to convert', 'verb': 'Convert'}


class InstitutionalKnowledge(BasicAgent):
    """Convert agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'InstitutionalKnowledge'
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

    # ── recipe entries: the upstream recipe, verbatim, deterministic ─────

    def _recipe_context(self, kwargs):
        extras = []
        subject = self._subject(kwargs)
        if subject:
            extras.append(f"subject: {subject}")
        for key in _SPEC["params"]:
            value = str(kwargs.get(key) or "").strip()
            if value:
                extras.append(f"{key}: {value}")
        return extras

    def _recipe_prompt(self, kwargs):
        r = _SPEC["recipe"]
        lines = [r["prompt"]]
        extras = self._recipe_context(kwargs)
        if extras:
            lines += ["", "Context supplied by the caller:"] + [f"- {e}" for e in extras]
        return lines

    def _recipe_attribution(self):
        src = __manifest__["source"]
        r = _SPEC["recipe"]
        who = ", ".join(r.get("authors") or []) or __manifest__["author"]
        return [
            f"Recipe: {__manifest__['display_name']} — by {who}, {src['source_name']} "
            f"({src['license']}). Source: {src['upstream_url']}",
        ]

    def _perform_recipe(self, op, kwargs):
        r = _SPEC["recipe"]
        ref = _SPEC.get("refinement") or {}
        if op == "prompt":
            return "\n".join(self._recipe_prompt(kwargs) + [""] + self._recipe_attribution())
        if op == "plan":
            lines = [f"Steps for {__manifest__['display_name']} on {r['platform']}:"]
            lines += [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "checklist":
            lines = ["Before you run it:"] + [f"  [ ] {p}" for p in r["prerequisites"]]
            if r.get("expected_output"):
                lines += ["", "Done when:", f"  [ ] {r['expected_output']}"]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "describe":
            lines = self._provenance()
            if ref.get("when_to_use"):
                lines += ["", f"When to use: {ref['when_to_use']}"]
            if ref.get("example_request"):
                lines += [f"Ask for it like: {ref['example_request']}"]
            if ref.get("inputs"):
                lines += ["", "It will ask you for:"] + [f"  - {i['name']}: {i['description']}" for i in ref["inputs"]]
            if r.get("business_value"):
                lines += ["", f"Why it matters: {r['business_value']}"]
            return "\n".join(lines)
        if op == "run":
            lines = [f"{__manifest__['display_name']} — run on {r['platform']}", ""]
            if r.get("what_it_does"):
                lines += [r["what_it_does"], ""]
            lines += [f"Prompt (paste into {r['platform']}):", ""] + self._recipe_prompt(kwargs) + [""]
            lines += ["Procedure:"] + [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)] + [""]
            lines += ["Acceptance checks:"] + [f"  [ ] {c}" for c in _SPEC["checks"]] + [""]
            lines += [f"Deliverable: {_SPEC['deliverable']}", ""]
            if r.get("tenant_caveat"):
                lines += [f"Verified upstream: {r['tenant_caveat']}", ""]
            return "\n".join(lines + self._recipe_attribution())
        return (
            f"Unknown operation {op!r}. Valid operations: "
            + ", ".join(_SPEC["operations"])
        )

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

        if _SPEC.get("recipe"):
            return self._perform_recipe(op, kwargs)

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
    print(InstitutionalKnowledge().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/+V6abOiWLruX/Hs/lBZx8yNjEp2dMQFEUFQRkWorMhiBpknAevUfz8Lde/MPF3VfW7E/XbdEamw3vUOzzsuyN9f7K6Nivrl84tWx3l8tZvZya67xE7tl48vnt+4dVy2cZEDCrn2G7+++jN75vmlXbdxHs4aP4+Lepb6tufXPzWzOG/auO2mLXY6S/KiT30v9GdfOmQBY2CjGzdgrfk4q+0HkQ9++un9ooniEqzYuTdr69j5MwbOOMuAokByG/lxPdujBD5r4hAwmoS3BdCuaevObbva9z7Osi5t409lZDdA79qN4rv+Tee6ftMAxV07n4V10QGRRf4KbPYHOytTv3n5/MuvH19i8Pvl8+8vbmo34NYL/715wptyYFtq5yFYL0cAZw6uS78OijoDtzw/mD2vPjR+Gnyc/ed/Jr1dh83Pn7/ks+fny8v0p3b5ZNesLeym9T2gXWk7cRq34+uMSnt7bABWwLK8eZgJcHh97PzGqShn/5jWPjyEvIZ+++HLSwFUuGP85eXnGbD7y0vdTb9fJy7lh59f06L36w8/f+PTdM7Fd9uJGdD69evz+skWEH4jjYPZV03erJ+yauDk0gfMv7Nv+jxUf7J7QvL1QfyhKD/O/pzzZM8/gL6PYHQA3z9nCzAAO19eL0Wcf3jKqIurn9u563/4+a/YupHvJmnctP8rvr88GEf3cP/whOTnj3f3/TqbP2175/nXYksQMP83lgDyN3HvQP0V77tn/wfrNM795t2Xf8ruzzbM/zH75S9t+1cbPs6CLy+Mn4J8q20n9T/Pfr+HyC8/ed9u/vTrH4D1v2WjFV3t3jl8zew8Dvym/fr1l5+a++2ffv3lp64EUezb2deuTv+M55/hepfzA4JPqg8/7gXyj/lUhvLZew7Nfi/K/6j/eAW1Mo29b/ebz7PvM3H6zGeTEW9CHxB8l40N0PU7HH9++QPUnPxRwKZlUD/+9rfZPnbroimCdqa5RdfOgIPbOPMn5fUoBnWvuVeN2ge4NjEA9kkH4n/y8KRxEcx++z+u3X6yQz9vPzVJnKYN9EO1/vpebH97nemAX1HHYTyVcZWS5S/5feckq3w2Ag9U49b/BNL40/QDlN/Zb3/B8et982s5/nav7vGjzKlrfipxTZf6r5MxRuTnT9WnuuwPvtsBvmnhAiWCGFTlqVc0RQqKeDsZfjdj5sWgiLRFPd55A3A+T8x+++03x26iL/mjJqOzRy9rIEDwrs7s0ydgTZDGYdR+yX03KmY//f7HT7P/mv2rXXfmkwwZdIUn9EDDnSYdQJMJuwyQPVohqBN36H//44kpYJP79Qw4Kg5i/7EZhGLie28Aaxz1CcGJmeMDYAGoWVk8Wm3cvs74YPauLxA6LU2tICqadmrKfu75uTsCrjYw5x3JvGhnDYi3Jhg/zrrGv0v9zantu4oZyGm7/W22X8ug8RQp+GdS804ENhd5DOB/d//jPmAydXv6jcXr7DAF3wyMBXYZ1fZTRmA//AIaztv2e4fO/f5LPvVWf4LqngkPeAARQMZ9uvTT5POZW2Qg7b3mTfadxp7ao35vk/WXvHlGuV1PrnBB1QdCwy72ptr/92dINVHRpd4dP6DpxOnpBe/plXsM/tDhZ+8tfkbdhwdQ994mkf8PxqEJD2q7VTdbSt8ws81BV82Hn9wibyd/PsZHMJ/MQLA+cvLbzPJWl97K85c8jUHQ1ePfH5R37z5pvikJqo165w9CC/hp4nuP/CmS63rKGftL/tYHADqze9EDzgdlAqTRFL1vAqfVN02BydF0/W0muEdK7U34guielZ2TgsgLfN9zbDcBWtVT9j6BBmngT5ncR7Eb/WDVDHAH0Qb4A8iAquCrf0B3KICZwDVBXWTfyONphgNaeJ0LtI382n+dGSABpyBsQNaDQWyiASj8dGc1y3yAMVDxHeEmssuHMkWdvCl4txRA0X7vgOfat4y5qzJpD5jant0CKPupcHv+8HDsu5pPVwFdsynH75t+9PbT1Nn3/ervX/K7iu+9ApSOdGr132EzAymbNfewnipfA6pX5j/jBwTCvau/Phrzo/O/6/J5tqb0GfUok/cONvuQvfXGexs9/uiUz7OobcvmMwS9k72GcRt1zmtcQP/UDv/2Q7p+es+2Hzg/QPg8+6cD0w9Uz6D8PINfF6/wtCTGrj9F3fPzedbl7/Xnw3e/nz67+2RK2fxeWEHITPHZRL53H1pU/5tTgUZFBirGhPU4lYS3nvVGAhpXWPvhRPzoYc3U+nrQbe+8Aexf8nfHP7MC9IQ8nBpuU3yXrffmDdz48NJ7bwFLeQtke9NkF/rTOSqdzG38l895l6YfX3I78//V+WlqHCAmAWrTcQukB5iQ2ti/X71PS9PFj2fSe+KAjPeKz1P+fJxNk+3H2fuQ+nH2dmy4n+3yDpzIfpkG5EkkIAVf77TvB17HfwFHv3YsJ40fp6xpLnvOy/+sxJQ3cV52d03esvDpxtJuQdk5quLUA0t7TAvbm1T5J+4tGBz89ut0JrL/RIZUPjB7ZClYi6dSCdraJPax6U/YAr61X3UT7WT3NyC/2Vc8jPrjjkf7OLP+/vJWHp7OeE6RgBzk4admaqcQCGwgEFw/Qgqs/a/ny+c+UMfAoHM/ItsY5sEu4gSLYLlaoDa5wlYe6i1I1yd9jIDtwFs4uGd7S9jG0QCBXcxfBegSs3EMcwC/R0B+nWaFeNJlKo0Agk8gpv1vy+CW9zTiofSE0Ps4Oxn7tOX3F4fAACWHNTz1+KwhEraX5vKi0g6ZE35x0OeacqgPPSUsM2txurkjpTZXruIaqraKwlhuas3bSo5dN7dMdcRgo8hrVm66wBcuHYKhOspshLWq7QkwnXWoUwQ4jjupRvF0TGrGPI5FTjPGRF8JKwSJzfKslaNlC8i11dBNfYMgPsVsyzLwUyIIhnTWWKb01nar5WqmCnRS75fqul2oHmzveEXoYyfg1nqhqU6hr1X83LPLqyF5S/5A2+zC7BjE7DxEio9wfDO06DrAphsEo9ack40gntpksW+MshiFRRVh/MVKj12sB+tFe5DsQyLZyGW9S8WTJlnr0tjF3XAu7W244iwWnrsyBMXLw/lmzUUcJiAJGhDhhDRpEfftiS14Q3XqmxTFO9w2DWKEI5N2xVxd3yDqoBXJGPU7wQnt3TmKSq+AvF44SSfmlNTEBpNvbb46CflY0+bZ1GNV4eghi9JIHRpLqM5jZPbxMjIi0H+SeCT67Na0cCWhqUWYdVvPS8JZslW6LxZHhh7SXewwzHW9Oq8VYpN0KVYY+7qi9N1ebTBGFVM3Nsz6aiycCuZ6bmcl/mhqZRHrpLNv8/M2MLloHA5tm8hDQhz6azlsj5zc6nzFHuZXS2P32akajpsMKXXOhEqKjU1k7fgH2jnFy7TO9R1zONd0fWV6s8gSO2fHhkVWyZpYUlLJaMl4Cg23XrML72Bez7ZUA2yvxVbawhfft8/t2SHpS3Ye2fCcY/223qVeYnHWPGlCFhILNF7HR+QUSthGy08wOMlg6IgpImcRxo7l+2ygTlBNG1ZceXm9UixtSWCLMF/7jq4mbgoy+7bdymSL9LDeaISAbnBZn7cqdizOBMqrRNcvkua4s9E0NjynlAjkKAuZXsW5uTyvKjHsxyVddlBC2KukyJpLztNz+ihTdcAMUHSzXOIYqSEEvCPsU86v8uiScpf9LRPkI1tmWrEq+3WkiGrNmisuRCWYHA/HUTcpmhH7Syn6auLkkY60UXNL7ex8jENH9u09cuNc3uiOSU/aDNK6c1KQYJ11BWwr3NTEBpwj+HaRNjSSGhS70ca9ru0Vhqml9UBRIZ7t5/V5d5MH9TDsCcqjb5bNY9W6UuL9jTvkJCyZOzzGSCJ3BbH3grwOU8vS8fqkRzkRt7fzAVIZAwBMcFnn7FAerXs9iMkbrErnhuCVLUR65jnNA1U3LEJbd8Jyf3Sz44BxorniKZNPb7EjZsllhZktDRFtsfVJ2r2yOEjTs0Wd5/tGuHi92M097nJZCPM1bYJKPneOCoVUp0xdlDjP45WnY5WlbOzgsBZIHqV2cQodMugwr/Jjc0hd/OQny+qGVB2uZEK6cQtWVlbzUg9XANGax103VCGCaUr0pLLrlUoGYmcPaoodoQW75jfsnrnsT8uTmB3n4bAbLtqgXB2FNl10XV6tEmINiUtoMVHPx+0C5jO90yJYCTFtb66jNbcQ3MCifcvTbjkLR52MC7BUjQHhbW/QmdzWpm5fI8ylquOyMJGbtDhQ2SFYHxaOWZUOY6Oak8Ta0VdaNJCQ8Ta/lU2z4KkjfWWygtcUVBQ8sr54e4T2r67M3/Btrbv+QsEqVVvYASShV45oZfm6rNWBJFdddBGhNRInYTUu1jcqPo0m1PDquKH7PY2unARpL/Fuk6VeECDlaWtxuBrAOwGMaenGri4msQt2F9hT2R2Et/G5T8bERfiww9ZSMran5njh6WCDCasNnzQL5NLi+kaSXXjMbao502paM4chDoO9lixZ1dJOqs4M3j7Xu/mC0JBwZ6tctr8aGrJNj2VgLRxQycgdG/MKglFOri/xHKPq3M9TLePPnIpUnuho5Fa03T2v4LUC0zdpCPf8NhB6PDnONdGiKCM6oMl2fz1asi8kW+FyTtxCXKmnXoC50LNWesZgKF2N1E7PneXo7e1VwIEjRObOqVroZL7KlF0+MvnuclS3c4hb5KvFTlBUQZAXOESnB3XD2Bce3YoRJui7MtacxvfXiaLs1NONIMdO9MbAPjp6ifYY6njxRYooKNlKAuXQxWqBZyTWDt5S2KtruWALbnFR02tSgBoL66rUXbZreidm7DgP5OVij8p0SEbRvFYVaDzt+jgw7bPv1JImxMkuudJc3W2xQizVsbScFc/SVTGUinMcq/iWbnwmDUUsthih3FaIdKo0+lJmzJ5da9LIncQk59qMZtxzmmx8VVFqkdWGk6kv7BNm5NuOF9B+bwf4bX2oaNyAFYuPRrs/roZ5EbqZSrYhNggZX2beKeEtHN3VIZIvGDiX18HcYVxcwLsddUFo7rTiL8OpDINFEVe1kFvuJaBSNd9EiYOhFV7E4gUqRFjMcEa3DyOlRHLNe6Loj8ZtfUpzLcOihmbGRKgwrcj7JPRvCHxIDyfVpE4749g4Km7FmBSACEqPrJRvOH5bLJfjoeqzKqGhXdvaxrLaEn6Lg5wxtOAqut0Jg3Xp5IF+hZWbsj7qG8JCSkZWu+IcyybHjQp66NTcdq/bSxzWNg3ngq8e+lN9UtX9bjRs+gTJzkpb7pZi7u12Jdxy/k1aG2YSQ2HmDeetd9qZR7wjDW/sXS4GxcamNX59FlFzcdPoRFTyxY3H0XAZS2WvtTUjxrs8kHOCiAJTdWHPZq+HPT7G0X6dGGS432khe1nYhrLMfKw6L0aWn/P6jq2OG61hYC+ATi4mxtUeWaHX/mh2qdZhvZuJ68q8Xi2in9dzvOl5+mDXuUnmGzE8uPWRN3ceP2r7zJKP18IQ47AtSsvm9oHVbck1LlHW8rjb0qJmwFAr4CnmUbQHuXSts3FutSN+mvMwLFSaNcKZcvBzktjyXLmuxY017ze80CRq45oWtd3LgnOhGUxkLjLF+8suOcHucYhk42wcYrZJCcbPd9nmfGkIcXUR2ONaWdesUuNbrd2ExbVzuhjXwpuxPuecvyqaVaKH3hXMj6hnLmiNqLurzJoi7lGbndLYDSKq0ZCIp31vrMXKpCwfc4b9dn4+V4VQCCe6uSCNT2xDNcLEdGgx2otGRyyCjJAPp32mEPAKi40yrZR+30apOj/bcNMaFmzdHDuF6YAlWR8O7XjAJWKo84pRcXUx30iKUuEHf9H2BRIj44j1KAFO6ocLHcTZySLqqDYNycigZa3lN9vBmys8wiVqEclquRmu1+66N1cYJQ+1ZcdyQZ6OXFUxImLpFM7x7Jpy+vZMeXAD2vnQcttFp6ZyY62pvW6lG+K2S9RgFaxscPS5cGv6ZgjVAhV7K2I9FoFP+NAqZErPi9XgKEEcQzFkctWt56Fzm6CQaSLYIb7t4coBJ7bT0NwcyFcNQ8RsekT6tmdNva2G/iB3KETiRrDaIN3JFBz4DK2O0FDulh56zYLziW2J8eIr2VLENQkMtmqxCWLCTDBxHTIrgoSorNVpdYHIMaxvijV9iVqc17gtQ6xHhmP1aL1XoF0uRxVadlma3RLSFVlVNVKNRB3F96J1dTOCWo5I310444WrkkzsGC27MTJBr/LggnAml2c+yq5pPAyXfb5gUdQ4KbohYHm7iMc8t53TPnIyOuCWx8U5So9XLYjd1soDb8VIFGbcBMtzyW2/W5CbpX1gRpIjpBg9LedN0GKIst429gWhrHi9W65kxjEPI5yr12BPS7RxaGvZtYRekM0TODO19pxMEZ9T8/NFiDzMN+Wt1954Ml+6QkdGmQnOd0LmyAqcYRd46JRx0+23ErLJNgm83DgcncyTTle1oruYApVfNo1OzkFbsPgK92tTUVfmPCkXOn4krI1M+zYSMs5QiWy05FUZnA/TS4bmGyZaCq07+ptk1WMtsUpkHLo2QUCvt0XQUjtjGxHK2pg30gopr2FDGqGKXw6KMp6lS2WbW5aL4AQ9sRfISnYny16KmnzDxvl6P+pMcLykBnxlvNKKd9nq4kgGcA3dWLetcyiEXj70kHnBEuWcwWvMXbkWFkRSdnFwwYQdMkpA48eK+VWiNnN8ZSzd/ck5hwqZSztkN86ZEgqr/a3vstYNkECfH9e3WlevndHiS4XgRQdgeWhu89CGO9W0o4Hbn3rvkAikXKY6Hp0pWnMXxDFEtbr1sJ4vuH4frIaFVFXsZe8z/iCmC1a5osJC3yMZ2odoTNlbUh6u2yGcZ60GuSU4duEZ1+aBVM1vuhorEApxdHWCJGpZOF5qJWS3vWXNQFe5FDWDLNDxDbSLpiePh+u1N+YrEhw9VjVBI2RfXo7ENWJ7EKWRXrHZVmQ0mzwazRXimotdMoNwKY3uYDLlsEJyNz4QmYzzUb9YHmthzRFZEro4zHZ42xznZkWfNkZlZgqp2sUZrptTO1SbghOCLD2jhXmLLytXvPJbethdVxW3OBTHy7KVFSXawykmKMoQkdE6glEodtZH5sBJdR7uh9Ha7etj618SLsKHUh5wVr1yg0Gesjk2ImcbBPXCF3mYsazAOGjOLYfMCsrqhUlBHghYSVgsWdk8K+g89xV6vki5henDsYSuI4hLoHQHKdBld/Hjpd2O1WqfKqDOqyRqBMS2MdxwrEl4lyt5Zmr9rSjQdoWaYy6CMMMF5MYapF5A5QEra5OBCX97KqBQkPaDHeJFtB+WqKj0EnfV2MNVPq5HweeEJdqtYXEwEZxjzTSNqkuUINKiXW1JZKGfUWlDyrY9mO1c6uUjLAsm6DQyus0HMb6WJWXD9bFphb6W8d0iUiGujA4G2yRostKuS5QVrr0ll+0YdJSgOzrkh1OBOqsnL19AQ33CfK+b80V0gWQDNjhd8fZWosMxo9H4kZF8tlF2ncWS2aqV6jmkzZnlPCnSnLiqpT8ecHqUjIGXDgPijjmcNXMenyt2l9pzd5mm7ta+yrszjREt0ZnEscODpBjkJbX358W2o3f0RothwTV9dpsIbEXsu0hfglEdSfx6j1SiJPYhLp66xL04MGsbLSR1mgLdZGrZFMpSED2dqSsk5YPtmV2teBuRTJJi1qGd4toGjDBbxhzt0MBtXOysoezwYUMLxOEcIYJoWodxZaXNsSjxA+pBcrAwmpVnlfCCwM4Lfq5eOlNVUHi7MuzQb1bClUAu1/SK7fMYuY6i5+HowScPS4h1lZbWbxqL1b6x6gI4IIOaiqmYoIybSLC3Ucj6Fa0zJA5LaHu8ljijCYhUK8YBzudsLweB5uqcPw/4FWSfhcC6nStmCaa4BkIF1DzUJNHRnLwXVraLN7K1utHS4JErstiy9IbVz57pQnh4YQ1HOEnzjjQP6JXiDAKruk4LFfooBjfb67OOInhMSLuw4ROEFNvelMCA4/itEUablTeI8/ONddSDRrdHT2b6Ih83KmPXLjHHzOWtUNgl1Bu9gwVO7kGISDqMYqL1LTtzeStGZ/y6jd3CT4ob7C9hbOvh5300Mu5yg+08VdbrYt1xai0x186OyHMg9+ac0UKv42v9RjCRSFaJ3nm35U2f035ejAeQBcKNKiwHGoRz6csUlF8Oa5N3R4qi/vHy8WV6Lv98uv7vXr5PD0L/nz1zfTw6fXuZdn+s7tve57usz/9Wk18/vtRuDPR4PEZugEueD2b/50PkT3/xUmbaNT5eX0+v+Ib27VVDa4fT/956+Z4ysnOvCILpvcT91ez0ahVcZCiBgy+w4hR27U3PzD++eIXbvb+Wfrkb6U2vt65xe9f7+WoHqIu+Ll7Rlz/+G2pcUgZGJwAA -->
