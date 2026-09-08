---
name: "rar-cat-agent-skills-idea-refiner"
description: "Refines an existing plan, decision, or draft through relentless, branch-by-branch questioning. Grouped in batches of 2-5 with recommended answers, pulling facts from Work IQ where possible, until every part has been fully thought through."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/idea_refiner", "rar_sha256": "e738ccce46e81b957aee2b02fb6e92e0c6f7a007f8d264a0539158190464d5d4", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Mathias Salomonsen", "tags": ["productivity", "planning", "decision_making", "refinement", "brainstorming"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/idea_refiner`. The original RAPP
agent is preserved byte-for-byte in `idea_refiner_agent.py` and in the RCI capsule.

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

Idea Refiner — Refines an existing plan, decision, or draft through relentless, branch-by-branch questioning. Grouped in batches of 2-5 with recommended answers, pulling facts from Work IQ where possible, until every part has been fully thought through.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a design capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#idea-refiner
  Upstream author: Mathias Salomonsen
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "constraints": {
      "description": "Optional. Hard constraints \u2014 budget, platform, deadline, compliance.",
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
      "description": "What is being designed.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `idea_refiner_agent.py` and embedded as the fenced Python below (sha256 e738ccce46e81b95…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `idea_refiner_agent.py` first:

```bash
python3 idea_refiner_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 idea_refiner_agent.py   # or on stdin
python3 idea_refiner_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Idea Refiner — Refines an existing plan, decision, or draft through relentless, branch-by-branch questioning. Grouped in batches of 2-5 with recommended answers, pulling facts from Work IQ where possible, until every part has been fully thought through.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a design capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#idea-refiner
  Upstream author: Mathias Salomonsen
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/idea_refiner',
    "version": '3.0.2',
    "display_name": 'Idea Refiner',
    "description": 'Refines an existing plan, decision, or draft through relentless, branch-by-branch questioning. Grouped in batches of 2-5 with recommended answers, pulling facts from Work IQ where possible, until every part has been fully thought through.',
    "author": 'Mathias Salomonsen',
    "tags": ['productivity', 'planning', 'decision_making', 'refinement', 'brainstorming'],
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
        "upstream_slug": 'idea-refiner',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#idea-refiner',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'f0afbd6c6948a24e',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Copilot Studio'],
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
_SPEC = {'archetype': 'design', 'checks': ['Constraints are written down and the design respects them.', 'At least two options were genuinely considered.', 'The trade-off accepted is stated explicitly.', 'The riskiest assumption has a cheap test attached.'], 'confidence': 0.5, 'deliverable': 'A design record: constraints, options considered, the choice, the trade-off accepted, and the first thing to de-risk.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'constraints': 'Optional. Hard constraints — budget, platform, deadline, compliance.', 'subject': 'What is being designed.'}, 'refined_by': 'rules', 'signals': ['tag:planning', 'word:plan'], 'steps': ['Write the constraints down first. A design produced before the constraints are known is a preference.', 'State the success condition in terms someone else could measure without you present.', 'Produce at least two genuinely different approaches; a single option is a decision already made, not a design.', 'Compare them against the constraints, and name what each one gives up. Every design gives something up.', 'Choose, and record why the rejected options were rejected — that record is what survives the next reorganisation.', 'Identify the riskiest assumption and the cheapest way to test it before committing.'], 'subject_label': 'thing being designed', 'verb': 'Design'}


class IdeaRefiner(BasicAgent):
    """Design agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'IdeaRefiner'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'constraints': {'description': 'Optional. Hard constraints — budget, platform, deadline, compliance.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What is being designed.', 'type': 'string'}},
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
    print(IdeaRefiner().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/+V6abOb5rbmX+Hu8yHOZXuLQUw+lapGgEaQEKNEnHKYQWKeUW7++32R5G3nHud0d1V/a8XlMCzWu8bnWS/4jxe7baK8evn0ItlNFNs1pNpJnuZZ7Wcvry+eX7tVXDRxngERxQ/izK8hO4P8Ia6bOAuhIrGzV8jz3bgGQq9QXkFeZQcN1ERV3oYRVPmJnzWJX9evkFPZmRt9dMaPjyOobP16Ug40vUEr8EDhe1CcQY7duBFYKQ8g7CMB9XEzKXLzNPUzD4jYWd37FdBYtEkymRHYblNDQZWnkJlXV2hzhPrIr3yoyOs6dhL/FWqzJk4gv/OrESrsqoEi4K3j+xkUACUjMHiy993wN+C+P9hpAUx/+fTrb68vMTh++fTHi5vYNbj0svF8+xGSCsiCOITgYjECPVPoCr8K8ioFlzw/gJ5nH2o/CV6h//zPa29XYf3zp88Z9Px9fpn+U9oMGOBDTW7XDXDUtQvbiZO4Gd8gNuntsQZxaNoqA1mA6qaaAvd48pumvIB+me59eCzyFvrNh88vOTDBnmL9+eXnKUufX6p2On6btBQffn5LchDSDz9/01O3zsV3m0kZsPrty/P8qRYIfhONA+iLKgvccy2QqrjwgfLv/Jt+D9Of6p4h+fIQ/pAXr9CPNU/+/ALsfRSjA/T+WC2IAXjy5e2Sx9mH5xpV3vkZKDX/w89/pxYUmntNQDn/H+n99aE48m0PROsZkp9f7+n7DYKfvr3r/Ptlp8b5v/EEiH9d7j1Qf6f7ntn/oTq5t+7XXP5Q3Y8egH+Bfv1b3/7dA69Q8PmF95MYNJwNGvAT9Me9RH79yft28aff/gSq/7dq1Lyt3LuGL6mdxQEAjS9ffv2pvl/+6bdff2oLUMW+nX5pq+RHOn8U1/s6f4ngU+rDX58F6+vZNcv7DHrvIeiPvPiP6s83yLCT2Pt2vf4Efd+J0w+GJie+LvoIwXfdWANbv4vjzy9/AqDJgDete78N8OMf/4Ck2K3yOgewqrp520DVBGapPxmvRXENgT8TalQTut3h7ikH6n/K8GQxgNLf/5drNx/tEODxx/oaJ0k9iwGGgQ68g9jvb5AGlORVHMaZnUAKK8ufs7v4tEBR+bVfdQCUnLHxP4Le/TgdTHD9+/dqvtyfeCvG3wFM39F8Mk3hNhOY1W3iv01mmxEA3oeR7p1PfLcFypLcBSsHMQDdV+BOnScdAMPJxbvBkBcDuGhyAOGTbhCGT5Oy33//3bHr6HP2QF8cerBWPQMC7+ZAHz8CF4IkBiD/OfPdKId++uPPn6D/gv7dU3fl0xoyAP1nkIGFW/Wwh0DTtICQAPFMGQOIcA/yH38+AwnUgHBAICVxEPuPh0HRXX3va1TVNfsRI0jAQiCaIJJpkVd3Vo2bN2gTQO/2gkWnWxPoR3ndAL4tJiLM3Im2bODOeySzvIFqUFl1MALKq/37qr8Dur2bmILutZvfIYmTAcXkCfhrMvMuBB4GRAzC/57zx3WgpPqphhZfVbxB+6nMJg61i6iyn2tMDDzlBVDL18eBchvK/P5zNlGnP4XqXvOP8AAhEBn3mdKPU86hieFBYuuva99l7IkItTshVp/BYPKoZ7vy7yPBnc/DNvYmlP/ns6RqwOWJd48fsHTS9MyC98zKvQYnAoeeDA59bjEEnUP/f804UxTY1UoRVqwm8JCw15TzIztunjVTFh/zIZg/IFCij078NpN8xZ2v8Ps5S2LgdTX+8yF5z+lT5gFpbQU8U1jlrt++B37Se6/3qX6rauoU+3P2FedfQQndQQ2kHIADaJ6pZr8uON39ailwNZrOv3H+PZzVFMmp40AcnQTUW+D7nmO71ykIU88+Ew+K359y0UcxSNr3XkFAO4jnFEpgRAxyALjgHrp9DtycMjPl5F08nmY0YIXXusDaKUNvkAnabiq9KRtg0JpkQBR+uquCUh/EGJj4HuE6souHMVOenwbaoALrOMy+j//z1rc2uVsyGQ902p7dgEj2E0R7/vDI67uVz0wBU9Opse8P/TXZT0+h7+non5+zu4XvrADwIpmY/LvQQKBP0/oO0BPc1QCyUv9ZPqAO7qT99uDdB7G/2/IJ4lgNYh/YeCco6EP6lfruLKn/NSefoKhpivrTbPYu9haCRmqdtzif/Qvb/WPiqY9PnvqLuofnn6B/3QX9RexZiZ8g9A15Q6ZbYuz6U6k9f59AC75DzYfvjp+ZumfC914BLE4YCupkKso68r37JKL431IJTMpTgJdThEfAue/09FUEcFRY+eEk/KCremI5AAkP3SDYn7P3dD9bAcB/Fk7cWuffteidp0HyHrl5p5H4jmojQGigL/SnHVEyuVv7L58ygCevL5md+v+yE5qIAZQfCNW0WwKNAGadJvbvZ6BZgUGg4Jr76V/3l4f7gZ28QWt7svWb7NfwOa0HdhivEyI30+ZhQmXbmya514k7iiSe+n4ytBmLybLHFmkaqt4nrn9d996cAFW8/NPUo69PwH8fdKdVHluP+6Ywa8Gu7tdpyJ6cBaLgf++y75tmx3/57QdmPGfuvzEinvBhQpRHq/veD1wBSiq/bAFrepMZ3/z6tlz+WOPPu3nNYxv6x8tXSHhm5TkYAnHQex/riTdnoKzBguD8UVDg3r8fGZ/CAK/AGAOkfQqnXdf156RPow5DULbvYw6CBQ7pM5iPuGRA2QhCBbSHkXMbIXAGJWiUQebk3CO8OdD3qMEvEw/GkwEEQwUIw2DBHMUQD+ylsbnn0SRNugSFITbj2IRDMLbz7dEraLKnVw8vppC9T6+T90/n/nhxyDmQXM/rDfv4cTPYsKkz5ewjh6HIICwvTN0MxD5NMfFk+jeSV7Z1v8IczdYchzuv4nmjm3vMEq5JoV1W5w0LK1u41ygxOyW7cSu1lurkSzPt++Nq3HYHjTl0notcheNlSy3VPD/tmpUltbtThlNYRmLH1Fh0DYeiXpzujNX5JtjNxiTwi44RgrNS1DjbNnRbjOJ52BmGnY5NaZmL1FL8VkN9SgiUzcwIi5gOR/XYCbrQ5wZHYNtEHS97w9kJ+HpGLA8DqurbuBP3SqoPUX2RnMJcDLvtTmeK1aaU1bjWrquZUO7RIMacmeCVmCRcjbYyyMSO7bLaq4W+gw3snHBpsqsLRa8KbaccpfCwIh1mH9WyQh5uBcIE8johmU7cnmfrK0m43Sw67BKsTvJLX+XW6rg0z+eTTwhseRIb5xxfc8MlLdWfG+22N4xIJeWrVShluRownrmxys4v1/lmYRgKcL1kDutuMY9NJ5O0Uoo0WQ1DTCnkRBlaizwqq7S/FjmbWydbIbzNybK8ea1gsyrQxf3+hHSaTNiWxlHnRLLrdEP33b5M/GKzFarlbki8a0DshvbWixKtwyZHodnCNAd6MTrsJVVYBxEXTFejYV0yN1II4I1AIyG5KnQjnFWxWF9nvRonXmUeC83yVX6/n6mrXTizrss4x3jH3x/PaEkk85PF3UqzUV3VRS3PwmAHmS3FhSeKglT1S+xyEEYjNt1KXd4UAXaIPkhBE6EYJ66Gi3+wT9VpRwfWpQHMf8H6c4Rv49kW2E7tt/qm2Z4ZZZdJUbNJhqiyEuVUBbs93Uh855t6vLDqrevOg3SOS4N9uCXwTtpaTEBqKnquROXqJk1WKNpFZnC0b261Sol9Tcga0Shz1VCLpFweLvDeWmdcexsH8dAh7BwX5IvQ1l6nZvvtjbZMwe74utVvN95QDPPU6heqJGA+ppcMxaf4rFSXSx0+MTdrUa1IQeM5SzYtfCNj6GwpEUtlk2x1Xdas5lxmOSOITeD6TLHtrF22rfh2wMKrszIwnamOfl2opwSxPKRlkxIL+PPV21KjxvelvOpvlJ9TJ0mMjGMP282e0/CrdHBlmF+LUiOetROPXilh1W7aue2yVz6yxbYWThy1POICs8kRnqN4e1yxLRsfxD7JqOXhvLVagtle3J1D+8F6FnMncY1U0YVCPIrdH9ayJK8ZOEtr0VtgDTkmTbAiVvbBzYIbPRtnQpXj4by4IPL8dvWvfSGO6Oq06T1xeyL31paRF/uLFDKFQjDVhl4XxoxU6MHUd+3VuQi783Vb7zuDmGMBN7b1bX/JnLC/mE0yw4ZrqBgjuqmwlGVnmgxTe9phzENycbZi4mAppSJ2N1jXYRy4pc2DOnJ123Yr+3S69pdZf7zRx9vQhjx9wrswr89zfCNSzHrkpKW2EhChtEWSI7brjN1t1BVds+i1N1uvTE+Yf84N7UqF8CHc5aVxyNzBKLzDOeQXK7LwIw1UjIjd/O0ZvxlbmfdlSjVWIGtwsBJvJrPqXM3C+3ktkKKcnQ/8DpXUWA447eSc09IRTdQ+Wbvrvtwc+GwMlho8N8xc3CmxhM336jE9icsmudASx1oBcthQsF6aGJUvanrLlcSW2BuzZYZgBj2Dzy09m2cjm85KbCdzcdiXun/EvDwcksU25MrePGHFZSSkPPEsQ2U5EdOzgw9z3ZLyy8vamYcXFbVbKhbWjHMO4YK+rKQVu5sfnYJfKeveHjnC5yzVPK7wjh+EQJ37xNk4sME6s0Bvnra3mPUOOx0XfMLQrRt/C+hgqFua0Mzr1l6ImtRxGrZcmq5sMM7unDGqwEb6ZmDItZnG1xkMhi/U1iO3ke0t4sUibcfUgd7pKbPMF/zytq4xlvQbbzdrl3h0JAR5I/q1psjottskpj6PO9YkK3akKKkcB/gM4iALYNZoGDnlPfiC6nFybT1bUYnYMAq2cMPWPO+vRNUOzGa2ikSVWwKwame9pSEKO+TYPioJl0tuNtjnUfPMraRTrMvXWUdXF9zNsETASE867PVbrVu0uHaPwxDy7D5r4/qUyalcXxROOtJcAQYm9nraJamplHRZpo02sOFVdOFAxhNEcC5R728W+LLoZpwm6+uWtGeqVY4ewQnbtIr4vDXr/FYYY7XVmE0LsL+x55vVdqc5R2KUJIWab/MhCe1wNRI7RplrqblNuZmxRiz/gFvDEVZ0qSQ0dkUtTsWKNlec455FJS/mt5xm9V0mgpkh2SKLJBH6vhpTpHXbs6zym3K4LW5RsDgcvE2zYdM9d2UifLhaJSHR6lmVdvs8N+jVVc1sz09kdj/k1zJKuv223+wWwqYzK37EF4pC+aNRbdizbeHWObvmS90sVjt/a+XlmkxgcTbqI77dFZsbG9bD0CS+uAObiz1c7CWz1TGfgYfS3qCXKzfgCGysZDPl+ihb7NqyX87Pi77olSpZHPVCBaWWb9OC08HAg/MOchG281SvBrVcjHS4vzlXv6GsXZnd+JQwip08j2KHwwKhqn3jtGQlxgqphTDHjtIh1JmjaIROSZHNjmuMy4wdVFU/jOj+tkkQVzzHJDNHPM7yq+yMIDEbi+5sJeyPnBE2ku3NU8VoR0lttm3Mnrhb0C6P4iE6WRQ2DLAjyDvDh/MiMtydHQ2HTRYzY3W51M1IkLl62BEmZd24kTKOS29IMMcfiJRXPW+fIGahMGRxRAIOZqOZtZHYagyH/SAKekv1MWJZfXQ4wh5Vq3WBiPCMkz13Rx03rKlvFhy62LTmPgacPT/dnFuUAj5IjU3XKZIzLIJTY1sdoehBbwYqqcPhLRlHp+9P8XlsT3szd9mLSi02xHmzrPPTheP3mYNekJQxcOkcsl3jEspxi/R4TzTorQlkNVHnG/SAXzx5F7DnsRuRtqu4pGQI0doppeYiG94/2Ru63vZ6Fw/z5Yx3Bq5HwXiDppk8Q5y4wZOVLy3Est7Mjzbns5anIC21HOYisxxLQuHQMXP409pmOYHpTrNa2u7LUm1olMcJIk1Hcb6D63J9coe9W1oIqrilccILV2Bcvz+mhKaMdV5iJWaT5zljHYZyf7GCA6mjWnWpdooEtzBVmTvKptC8a0bEmlm2uqAEtOvgTjojgzLe8PM56A6+HbmozGeUaIXe5bo4sDojojCPXIMliS8rOpi3umcYqGVFSn1cY7mlW1p5VYm1RHZERURVufDRahdqmLjAiRovEZpfDfkFdnhsSFimXy72/d5kejS7CWiS40HQ2Zi1n9VHxWe6bXPoBfjYrqouAhM1gXQ38XabRRo5GHGRmcEM5WeioWJdxwnwAUxQuY0hRZNny5N99Q0A4PPaDAFmIga+rIUqlGON5EndYy8IySRmJIDtxlXb3m4CzSaC1qb5NozTTZDeUqGnEFyLrXoun1aDblqZ1Ck4us7sngtDKQDbAfrSdM6ZjAC5p3izSK/tojNVsl0bWXsOxDgKN0JsO3HXB4xnHcKs1uadGC3O8gFJZ/aqlVHaZTTVX53YtQLvYto8MoBuPOxYmdKNIsptxA/wbrj666SUUc+wC5w5z7QcORbCNqGPqhmq8bjoQXfYFoNR2QAoS8kzldmnXJ1I9OKsdoeb5JzwuhWP5IF0HV3sxEFRBwSvy1Y2Yf0iLvbHkGfGGg4Wx6y/isWWjVdNPghkDEal7nwRSCnCBJ47KgmLcIva7uU1osVpHecG2UbRur/YOu87qZjJ0fG8m+/shRQ0g7raZjefHIdB26L8fNHnZz3rs228XM5OfQtXfhd0eH9bIGsySite09buAtX9ZnUhQZfninIhz9paQfe1yOERogNiuMyos1raCBlcZpdhSQsWc2No1VfIkXA6sVa4kxD4t0SoBu+2OYuAhzHjxoGBKdBHgT7kI4fTWMuHEoquT9vG93xfwhJ1LaTOreUDNrPWIU4paUXRHKUTuD9wyrwRYW6eWTM8i2qcsi4usuywVAuwy1kzG7T16IZC4FFGqcK0FlG5Vs/DeokibIUSB4VP90d2KcLR4dKCfXmUX9g4DPqBGTMdsTeeXJBbSzhomiHhway/3ezqxO19YZFTNNPnwWXRHMglSo0WeiGCwG9pOC1E5iDysga7WMMQx6V/ozpxt25uKB0i6oEzAg6NYW0tro8sPG/8jJSD2GDmRHRi5ri76ORCa1YbI9gc6I2usHvvuuMpRyW42Rm/nJdHb3O1eBQtMzvmM5oU+MZIbvnVqZNb0evC1mGr9kCPIU7j2C6QUJaMt4ZE7Rabi74hZ9jO7BlOFxOZsgvKQJwBhqUlXi/Yc6fZAzxUnGCSEYGtN6sezPf+UpLnGx2OCRp1lSg/g34XuqynNnuwwy91PWtm3GYDn2SHWqJY1/iNnzTbpm1d6uaFpDGUh5va1svrrISpuIJv8p6LTv0ioDfFzdXriFgQ8y1JDuuZKh+HiDI3lLtbw67W6hnDM1K6h3dNge+qfjQWGNOscY+gz+Rgjfyuw/UUX8L0IW58UByX3Qifx1mdU651xv2GTvA081jRLOZBsJaMU79amyvveEj9BLFXy55esXmzTbMskgdizTGDiRLbktoPTgj2bsdzYw5jIpNYu4JP8Da/FOvgKC5BSQ1pmFvOulos6LlOjeReM4y1xuM739yfjYyuyWM+i5C+LVRMc0Z4CwbV8gqmFgY0+qEsFhblh3EiWwqhSX7mSQgzUF7qezGznRfxTPQR84SXLq1ctSQW1QWj860KgFEo6vF2s8yTQQV51qstOS/9IGZWBnkxr6fN4AghZTgxnODXOD5cm5E3EBAnk9jy8c0gqN1cXho1Oshj056InaT5fbCW426ZlIS3VezkIMlcpS541GNPZ4Ip3RmlytfGQZeZMD97e7St/YszGJaZMC2sqgEf8BQdqqv5cbUqJGKBoqcxQS9OHPvXpbOW/PAAwFWlI24xivxCUuSj5i7UhK7nBuXOOTbzVk4/X+7bQwq70ohtVURMqZYKOsqsSe/WVQWDhPmCvqx95BK1tjRvUJaxzkaQoOvZyYnUYDEPBpOkbpXDkAcc3tFXm0tP19PYEDuMmK1wRqVImxNDlqrD86ljc6eZg9rGr6oD4yPTG+fTPhdt6ja/0quua8ziUvkyMn06SQ4t0aGLhpb5yKGSoF6jMKV2NEfr3RDxZc+sZ3uBkiSZx6KzsORlaqQ4HidF4VzePK7B0axdOJfA847bwNvrMbfhyUyfVft6iR5ZRdYUSS+61HTCWYvvVZS2CZ4jrnMtdIuMhMOTLtp5ubu0Q5BsRnU8Wch6UPCLcgzGKGTSto9xmaKdUzqykUI5e4K2GIQUF5jui2PRXU8qMgydbgUqds2up2jZ0oYuasP6WOWrdj3kHd+1VssEAR7q9EUN/Xbeqbwlx2Ky1yy3Tb2hmiGZeOxa0osux3iPbNx2T/pgd7zBjUYCeC+wLPvLLy+vL9Mr9ueL8h9+J5/eXP4/e4H6eNf59QvY/T21b3uf7mt9+vHyv72+VG4MFn+8/a2TNny+Pv2f734/fv/9ZBIdH9+Upy9wQ/P1o0Bjh9O/mHp5fAJr4i5uxueb8ukj6P0N+eNT6pfUvj6uPHROX4jByfNrdV6l001g3vOzC7AKf0PesJc//xsxyLv/uCYAAA== -->
