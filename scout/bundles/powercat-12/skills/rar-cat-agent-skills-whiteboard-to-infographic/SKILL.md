---
name: "rar-cat-agent-skills-whiteboard-to-infographic"
description: "Turn a photo of a hand-drawn whiteboard or process sketch into a polished, client-ready infographic slide (.pptx), generated natively in the agent's Python container."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/whiteboard_to_infographic", "rar_sha256": "11818cb6790bb3fa12ce584fccfe160c66297eecba69ae252c3de296a25c47a8", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Andy Zehr", "tags": ["infographic", "whiteboard", "powerpoint", "presentations", "diagrams", "design", "consulting"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/whiteboard_to_infographic`. The original RAPP
agent is preserved byte-for-byte in `whiteboard_to_infographic_agent.py` and in the RCI capsule.

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

Whiteboard to Infographic — Turn a photo of a hand-drawn whiteboard or process sketch into a polished, client-ready infographic slide (.pptx), generated natively in the agent's Python container.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#whiteboard-to-infographic
  Upstream author: Andy Zehr
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
    "audience": {
      "description": "Optional. Who reads it \u2014 this drives register, length and what can be assumed.",
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
      "description": "What to produce, and about what.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `whiteboard_to_infographic_agent.py` and embedded as the fenced Python below (sha256 11818cb6790bb3fa…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `whiteboard_to_infographic_agent.py` first:

```bash
python3 whiteboard_to_infographic_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 whiteboard_to_infographic_agent.py   # or on stdin
python3 whiteboard_to_infographic_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Whiteboard to Infographic — Turn a photo of a hand-drawn whiteboard or process sketch into a polished, client-ready infographic slide (.pptx), generated natively in the agent's Python container.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#whiteboard-to-infographic
  Upstream author: Andy Zehr
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/whiteboard_to_infographic',
    "version": '3.0.2',
    "display_name": 'Whiteboard to Infographic',
    "description": "Turn a photo of a hand-drawn whiteboard or process sketch into a polished, client-ready infographic slide (.pptx), generated natively in the agent's Python container.",
    "author": 'Andy Zehr',
    "tags": ['infographic', 'whiteboard', 'powerpoint', 'presentations', 'diagrams', 'design', 'consulting'],
    "category": 'productivity',
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
        "upstream_slug": 'whiteboard-to-infographic',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#whiteboard-to-infographic',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '8ba98fb5f2eb84f8',
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.571, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:powerpoint', 'tag:presentations'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class WhiteboardToInfographic(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'WhiteboardToInfographic'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'audience': {'description': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What to produce, and about what.', 'type': 'string'}},
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
    print(WhiteboardToInfographic().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/9V6abPixprmX9Gc+8HlpupISCBE3eiIAYQW0ALakctR1r4vaBce//dJAeeccrd9uztivgxVYYMy883nfd41U/X7i9U2YVG9fH3Z5O4ImV5YvXx+cb3aqaKyiYocjChtlUMWVIZFU0CFD76GVu5+cSurz6E+jBrPLqzKhYoKKqvC8eoaqhOvcUIoysEKsLJIozr03M+Qk0Ze3nypPAtsFuV+EVRWGUYOVKeR60GfXsuyGX7+DAVe7lVW47lQbjVR56XTbKgJPcgCQ81PNXQaAe4ccoq8sSIw+RXA9gYrK1Ovfvn6y6+fXyLw/eXr7y9OatXg0Yv+jlQp2I+twbrUygMwobyLBL9Lr/KLKgOPXM+Hnr8+1V7qf4b+7d+S3qqC+uev33Lo+fn2Mv2R2gfCprDqCbljlZYdpVEzvkKbtLfGGqq8BnBZA0rqpory4PWx8kNSUUL/Po19emzyGnjNp28vRTmRAYzx7eXnieVvL1U7fX+dpJSffn5Ni96rPv38Iadu7dhzmkkYQP36/fn7KRZM/Jga+dB3+bTfPfeqPCcqPSD8B/2mzwP6U9yTku+PyZ+K8jP015Inff4d4H04lA3k/rVYwAFY+fIaF1H+6blHVXRebuWO9+nnvxPrhJ6TAN9q/ltyf3kIDoHzAbaelABnm0zwKzR76vYu8++3LYHD/E80AdPftnsn6u9k3y37H0SnwMHrd1v+pbi/WjD7d+iXv9XtXy34DPnfXkgvBYFXWXbqfYV+v7vILz+5Hw9/+vUPIPq/FCMXbeXcJXzPrDzyvbr5/v2Xn+r7459+/eWntgRe7FnZ97ZK/0rmX/F63+dPDD5nffrzWrC/mid5AfLUewxBvxfl/6r+eIU0C+Scj+f1V+jHSJw+M2hS4m3TBwU/RGMNsP7A488vf4CkkwNtWuc+DPLHP/4B8ZFTFXXhN5DsFG0DAQM3UeZN4JUwqiHwd8oalQd4rSNA7HMe8P/JwhNikHN/+9+O1Xy5J78vdRKlaQ1/ZN7vTfH9h2T62yukAIlFFQVRbqWQtDmdvuX3tdNuZeXVXtWBDGWPjfcFBPKX6cuUYH/7W5nf78tfy/E3COT+t2Qs7dgpzdVt6r1OCumhlz/hO1YOeYPntEByWjgAhh+B1PwZKFoXaQfS5KT8XRXIjUAiaYpqvMsGBH2dhP3222+2VYff8kdexqBHTaphMOEdDvTlC9DHT6MgbL7lnhMW0E+///ET9H+gf7XqLnza4wRKw5N+gPAgiwIEwqnNwDRgGWBLkCvu9P/+x5NVIAZUGwgYK/Ij77EYuGPiuW8Uy8zmC7rEIdsD1AJas7KoGpDsoah5hVgfescLNp2GpnIQFnUDuV7p5a6XOyOQagF13pnMiwaqgc/V/vgZamvvvutvdmXdIWYgrq3mN4jfnUDxKVLwnwnmfRJYXOQRoP/dAR7PgZAKVNHtm4hXSJgcECqtyd6V9dzDtx52AUXnbfm9oude/y2fCqw3UXWPhgc998IN6vnDpF8mm4ManYHQd+u3vT+Ku3IvldW3vH56ulVNpnBA5gebBm3kTvn/n0+XqsOiTd07fwDpJOlpBfdplacPvjckAOoPhR761qLIfAH9/9HOTKpsaFra0xtlT0J7QZEuD4qnOZMpHp0baC8g4GePcPpoOd7Sylt2/ZanEfCXavznY+bdMM85j4zVVgCetJE+MNzl3p12csKqmtzd+pa/pfHPgIp7zgK4QYSDCJgIf9twGn1DGoIwnn5/lPS7kQHHgHjgmFDZ2ilgzfc817acBKCaKH0zGPBgbzIUsA0wwo9aQUA6cBQgHwIgIhBKINXfqRMKoCaIOb8qso/p0dSCARRu6wC0oVd5r5AOYmfynxoELOijpjmAhZ/uoqDMAxwDiO8M16FVPsAUVfIG0Hra4kf+n0Mflr8jmcADmZZrNYDJfkq6rjc87PqO8mkpADWbovPhJ38y9lNT6Mdq889v+R3he54HQZ9OhfoHaiAQbFl9z7JTzqpB3sm8p/sAP7jX5NdHWX3U7XcsX6HdRoE2jwR3rz/Qp+ytst2LoPpnm3yFwqYp668w/D7tNYiasLVfowL+T8XsHx+B96UpvvwQS3+S/aDhK/R+WPnT6NMbv0LzV+QVmYa4yPEmd3t+vkJt/p4zPv3w/WmtuzWmwM7vyRD4yuSYU6zfmw3J+zAnQFJkIJgnlkdQSd/rzNsUUGyCygumyY+6U0/lqgcV8i4bEP4tfzf5MxxAHs+DqUjWxQ9hei+4wIAP+7zXAzCUN2Bvd+rIAm86AKWTurX38jVv0/TzS25l3r88+EzZHrgjoG06KIHAAK1NE3n3X1brRhN30/c/nwfF+xcrnWKnmCrnlNqbNw7vuN0KgJqCLYimBP8ZAliDJryr0k8BN7UHNlCtrkGxdSfszVhOYB8Ho6mVeu+z/jOCe8yCZOMWX6fQ/QxNPTFIx2/t7Wfo7cBxPxbmLTjL/TK11pPOYCr43/vc9+Ou7b38+hcwnp3234N45pPPd+Use6pUk4p/oROQVnnXFpRGd8LzoeDHvsVjsz/uOJvHKfT3l7eU8bTSsy8E00Fsfqmn4ggDlwcbgt8PZwNj/4OO8bkSJDfQuICl8zkxJxwbX60R28Z8a4463pJY+I7je3MccXAcXa88z7EtfG156BJ1MNdD1zhY7ixWFgHkPZz1+1T7ownNlC8BCV+Av3sfw+CR+1TjAXvi6L1BvbvhQ5vfX2x8AWYyi5rdPD47eK1ZOLqypdCe3XDvYhpr1soQ/Kbjg67rtyvpGWy9belRMamqbQt2xSaObrFNZhY6tuWFHYNvT6jsX1bmwjRU21aKZGNv2XR/K/ulM678mYPzfbzhuyZLtCtyvEpCuIP3uDH4uQ6SvbC9wDAcKR4Fl8Y+lOzgSnCCvWgP1NIph8Izde6KmddC1ctoHpgsMVJ1R9ElmWYX2pJK3YqTiJdMPD+ubErnmzy07VYc3cM+0lM17UzcjRQRaIo0u0JqbaUsnbJouI19kCUPvSSSjZmoOjtHXM5Waj+KQUsi0Qh7XXeL1ieMo2Zcms5gH44deXWjt1K2OyZbNcMFpR221yOazK/SbuBatbh5hdkdOOQaX7QRHbecNq+umMZjzmGeXUN8t9G0+thjLlbiM1vSgtrKhIGuuV675mMQmDate1WpD9KNJEuXzUJnae41omhyec1waLN2B7bGmY4X9XTMVO+IU5rB72Y8c90s1+o1IBhdjtSK1tabw4rNxLHonEQVg2QdwOJytt0pFeMkurrbzWcicQ2JbMZxOximxtq1qWaLirmeMeuSvYZLxCypS9oJDXs0PI2uKEk3hP3FZuBdUEt6b5sHZBvrNq2Uwi5HtladdT66Eq5+XlmCuXVZs8/OUXUe28uJJ1TXF+PFHMVi7eycO1LEfQQkcyxc56Ku7HBPuvZm2M+CHPVNg6WalY3uKbus5P3tssCIvgiFWlNnektiRXMcghrde7zj04iRLbq89DDmmACGSirNBka2h6roB7cS+dMC9mWYH0C8IfVwAh4gIUZ6FQBfoEwrulDG84671MdRideFKgJHcmS3aq9Hd+vZkbB3M1hdN+7JS+PVuJyREk6R2C7DZmltcSyRwxko0MMhRXOHlxFimToDiQdLHtHyVEjUjSSf6tlucZxfT+dAiyJMTtVxtcdbl+coUUYbEY8ozjPwdq4kgtGxuqIp7f6IHeWLpQWEzZ1aMz7z6JJPnN4fHW1UjUQQHWVGcqfdWPNGq+ry6G5IBhGNhbFpst2yOgh9KymnYT/fiP1S6PYMETK81JcWSGbB4bblvdb3ltjuSuTGOFsuYJ1RG5sjuzY7RSXWFMiMmPXr2Qn3zKPFl+LKlDGcFQt0v5RvxZbX4ZjqW9IKdkhsmYMor228PpHuwlHsklbXPBpj52Z1XKhTC0M2MEKUgeTkB2UzkzWau87zuX6IsRMunRCe0rJAz5RQIwQyVfLQxaVjsFLrrbCRLEwgl2oiUpWlHWicvWyKJQHPOu0Ca7tUN/CKSCrJE4RFSWlsHC8YZE3eiHzHleZOE+iq68kOO8eEbG/rPibMOTPLdJmtuMbtwzLkglYwbKtC2NnOXI5RRAadvWnM3T72Su3QYBlLXfDT3sWGrapwAsOP2ly3DmcJ3WmcLcWLg8jMgm5fH5crJ5Nghuislar6nRhrs2xNF6PC3g5wvcGRwl+I5BFBwkyAd9tkxV5L274guqGJSYBHyzaqjRVHSMMMlTaOTrPWKrhxuwsholZDYSa/G/3CkypUytp6VYaDfvCqo+xj7WjkKOpfB12B8dFvWQprTEnWVS2iJWlRmVm8W192UkDJRWNcFRsVeTxxfGMIkapkTO2ksXoU140GXCTb7HZnM7EF46JEq0EDc25LfG8i5cVKxnUf9IjBVgsmXFQGax4Mhh5nJ9Vrlqp1MfsT6lbmEdnv3EV/VCKJG7mIuNLSctV4jIk2cjLqCWuFXMV3soTSa91Kr2iTsueZeh0TKUPyEC7W6grJl8suRuNzwjWrRUrn9XAm9fliESxvF3ZTRCaBxpnArWTX2G5LoR0RyiaSYTkYgXIVUyulfII+0eqxEgdN9YyDjM8lJM1kHkNWF3e1OGlUVatnU04Zr0zMFLC9twxfJY6hKS7tGXLYsdJ1oyM5vOJm7YEWtn0tb/uFznKWFTgNKbf6KJ2J2ww+HjiXcNVDhillmLXYSo2cXQgzO+e8xahjL9H+PIv3p8VlTbOiaQCemoxahPRFR7QraKeDakuS+53sNJg9X8xOfecSDDlQNN5QCgHOKnINhyWJtUXJFMezJ9d7r71YkeEeRXV19EPqsFf5+aEeL2oj1GTHFpcdyl72Y7LtbpZhJZm8PxjbVYLuZcveOaogjJapHNKKJjqaWGhzZZpzTdKgT/LsuBPsuaxLOyU/nPudc9UvKHsF5RPEwbzlliTla02tEXuzd8nTzumIYJGUlRPoAivrSStvtDmjHm64rA9IoCtC4rLWcVlel8oxl5Ec8SUTg9fpvmmlaOSkZt8qeHbk7XQTgK6jvDHE4uTT0ZWuxrM2Uq1keUZdxdqRHnM7oerFKioDTqvY4mhbC/xwChF239NEmGBloJa8iVPBDpB3rIVt2svYKSBbOZtjq5Gy+TLTKFKdb6PD6kwQ8wE9HIvY8s693CZxT5kzJW63XjAXKydsy6a4Lvu1Utk4iH6Tx5XN/taRQrKG9V3ZZajLJFQrzoPrfBNoziq7spK+H6KIZzdIntmXfXw7dXB4uCGixLX7+KrbhHxdr9vguic2dqU2/n523msSdjyp587d2EQtosqmaxOUYVV6hV+HldU5rYFrjCpY8NbDlnvYUGZ7gY+sI2vGC02R4649pupxt2ExKUlpdGRu+SwZqQSUNk9F0G7kePOsHzkP5Y9n5Khey6iMFSQKkisHDxqjeK58ILi5WlOhGZNYMtf21The8MSWOMEQvbnv0GFEzOqjhXUGqKJyMFd2Y36sEEVZLvfZXuSv8dWXrCZtqiYtTouN7mkrW0d2ZMWdywGBrVXEeYiFSN2iunDLpA+5Y7ybsbi+EuTkNF8VGLO7BcuA8T1J40vJSNG9kwwofFmrx9OOKBdcU5UH43RC0hQdPfRMLptWQCNpHRtuUbfzq46TMzXVM1FTDRnlXX4v6Okm2Y8dam2Ua561Z05tbn4bIestjxJceh32OD8jeC+PgVuA1sqijB5hmXynRHmGIwSjHg3bZ5XzohDOiajZqG0kaK0TFL1MGXht7Rp8ZdkmjBrRjOGNnMAyIVwKyxuDHi8bBTcZzOwwjbkWyZhfMo+R4CBa7Kvwani+fCYiW9b9FOuLAV9XRRRl5KU43S63Sq0PheqArly8HpyeI4RZODvQXWN2/LUCiUyLBprS0zN85ZfbdDuTPLKLtu7aPDT9Wggul7aqb8TqIqDniixXYpH2m1bsuvC0qYktvFqWAzD+Ykul+zOPCQ48CGuxzdvcO4CKdjFmA6PIeRqbocfeoiwHAA/kThCJJXUJ3Q0i+P3hFhP8Vljhqq7q543lCrm/YXvcOYuWcNwX1i06DaaSeeDUk1s389a1WlDJCweFycvlJN5ClLVDdAZz1nopxR19oRihkw/pfHbyiD3pibMe34A+j5OULSnC1snh4la89jl/KTo7ZMKTiKLXYYsla4fhLnODTowUdBR2TOU+jx2YvuYonw5aurPrTA+JhiaWegwLR9iwZ7XbsEsWVAGNv0gZy+ZdTwhNL1SyS6+JYY9QHIbW8RBxUV/Z0Y0eCNCiEijpXem5t+r5mhObZmDhbgXOjkSQabtdR+Z2dyEMNjwNQoJTIkuLKJsjdoZTqz1LJgN8Hj0W1OTzlh35i5GXtiy1EXvAWzkfSE0f3f2mF0BgM33FaxuqWTQnMaz2yqkK52kcIbmBBcwuLXF4I+ylTYc3GTa3BCYe1ozqnWd76tqprb0/UmnaKf52wLkwIrdKEIwdAodBkKgkI9mkSjPrtk81akmEGszEN4JTMn6xmfE201wKF1uih9CODp2JxQpIhYlHRcgZOy4raYgHv6RFRjOHarZndgODL7fYeAHZIVO4Sg1Bc+yRgblYFA1WL+ghDJaEeFJNhQLZad2tDuLKWy4wBo0WzljopOWK6FVHMvdUOV19Bcf3SqmrhUZfLriJ8LyEeuszvfbiQlqSKhnqqzIoFq3l1h674SsGZxokaAR6pHsdO/DFDDfxlbwcM1pcUfriTPZxs642Or2e2fNqts5iX5leW7gEXlW4DQyzIkYn9uZHJmNd9NamdVFj7jDO3S06sC59QEfHOiVKrntO2qlrrFscR0IqcJqoZhs0T2ojTM5bbkiV/Wa+kJO55eBdWfVrpkALn5eu+DxOks088+MlemIUlTH3MomfcUXJ2NpwF/6SotplRJRErJLXS6PenJCOmnNRbYjKjhH27Kkz1+ra85BTqwVheBuejGw/PfvN9VwyMxSM78T2huyTMCbhDbWxW5jS94VOi+6h4qQRGcel1FoNAw5Ft+h8ym/H/CLa2Fqy7YozKb9Qlut5T7ErjTFLTN+M8Nr1B22trdp5qG9InyjKm6MSYSlcLk3Vbk9ZkAy3LdoN41L1l0jOl6cls055jjBso9UMNLmS65V1avEjEQig6oiqP2t4fL+odzrtUvq6bVeUlvK31DcV9ILfWtdeCZ0mgMDvlH5sGELSxuyk0q4qgNTa2PS2J5hN0yyveRcx4dgKq7iJWEOAy1ot3YtV9LgQp6x/65wGWRPrMyOLaKFz8NWgrV2YFl69P60URqvaqKhEZU7aYSOPZbflsTAdqcNazITzFUFUr1txJ85QhTzp4eUYXOURQ+3t+rgd41tQ4wdcWa7iDBaIilydtwo1o9dlDVeL5YI85NxGTFy8YvjgABpkizwhcklyV7hDux6FC+TgzmaIipWkd3Ziu5SF2Hdzp3Rl9IBHt4NgKIw3c0ccJlWDCcBZ3zFuBkseDacbVSdfBrToe/PTWkzpyGP5HebtSEqNT2a30A7dLZ3hIXrlRDZYwEcq67wbOWqlHq4dVJZhjiQ5IpZR0KJmIb8MB8QHZTi2s8HbHyzGsYLtcOblullvdxwZFi5/pj1hXJ9b3K4yO+CDwmhJCm6iFmNuYUaZyr7GE8w3iI24NnMxRxWykQJmvRfzgon3iDmc/e21wqoTWYntdRVaMEnNEM0SmrnbrqkVTPsHPQIxF3rHPO24fO3Co9wdArYNmHocQoeIDvVpo/awp1T1yj9y+eEaL5uthW2VNL9JxHpl8MgVdATxrXKW81aY1QIWLERqhh37hVCBMDutcSYiMSFY+dnlgLK+vxqYngC9db7KUB9Y7xKD88AldQlz1ftbQC+SEzvtwoHjhyXES5deKMbG3RPCGTlrFK0RrZvkpq+ufaodFo0psgsa14iu4NCdnjFRcDlxRMHItIyJxewoEjK3bmWBIW7o3lqsu6HxbVammOZo3xY9UxJ6zAeEkSp1wni3QeocGaPUkVkc+uhWp8J+znf9EXezaETFdcWkJuwP8IKiNriz1XNjsEljpRwEimg797Q4LDHljPlRjYd0iFpbc1yeTIKBN9IMOYVXjT9vNi+fX6a78+cN+H/9Wnu6kvx/dvv5uMR8e9d1v3r2LPfrfa+v/w0sv35+qZxoQnK/1K3TNnhekv7HK90vf/vaZFo3Pl4OT2/hhubtpUBjBdM/kHr589wPOdMV+fTPicoiyqfL8ftt7PMdbz1dlkcWWJbVj3vzKLhfpoOhNp1eck/Yn69hAGTsFXlFX/74vx6DH8pmJgAA -->
