---
name: "rar-cat-agent-skills-sharepoint-list-formatter"
description: "Turns any SharePoint list data into a clean, consistent markdown table. Dynamic columns based on list type and query, plus a one-click Open link for every row."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/sharepoint_list_formatter", "rar_sha256": "9d5aac2ba3712657aade17d943de5d4935e122c800e3919e3c9202506154441b", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Mathias Salomonsen", "tags": ["sharepoint", "microsoft_365", "productivity", "tables", "data"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/sharepoint_list_formatter`. The original RAPP
agent is preserved byte-for-byte in `sharepoint_list_formatter_agent.py` and in the RCI capsule.

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

SharePoint List Formatter — Turns any SharePoint list data into a clean, consistent markdown table. Dynamic columns based on list type and query, plus a one-click Open link for every row.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a analyze capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#sharepoint-list-formatter
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
    "data_source": {
      "description": "Optional. Where the evidence comes from.",
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
      "description": "The question to answer, stated as a question.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `sharepoint_list_formatter_agent.py` and embedded as the fenced Python below (sha256 9d5aac2ba3712657…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `sharepoint_list_formatter_agent.py` first:

```bash
python3 sharepoint_list_formatter_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 sharepoint_list_formatter_agent.py   # or on stdin
python3 sharepoint_list_formatter_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
SharePoint List Formatter — Turns any SharePoint list data into a clean, consistent markdown table. Dynamic columns based on list type and query, plus a one-click Open link for every row.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a analyze capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#sharepoint-list-formatter
  Upstream author: Mathias Salomonsen
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/sharepoint_list_formatter',
    "version": '3.0.2',
    "display_name": 'SharePoint List Formatter',
    "description": 'Turns any SharePoint list data into a clean, consistent markdown table. Dynamic columns based on list type and query, plus a one-click Open link for every row.',
    "author": 'Mathias Salomonsen',
    "tags": ['sharepoint', 'microsoft_365', 'productivity', 'tables', 'data'],
    "category": 'pipeline',
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
        "upstream_slug": 'sharepoint-list-formatter',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#sharepoint-list-formatter',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '081ee2e4c6d01a36',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Cowork', 'Copilot Studio', 'Scout'],
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
_SPEC = {'archetype': 'analyze', 'checks': ['The question is falsifiable and answered directly.', 'The decision threshold was stated before the result.', 'Missing evidence is named rather than silently excluded.', 'Uncertainty is quantified.'], 'confidence': 0.667, 'deliverable': 'A decision-grade answer: one-sentence verdict, method, evidence, uncertainty, and what would change the conclusion.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'data_source': 'Optional. Where the evidence comes from.', 'subject': 'The question to answer, stated as a question.'}, 'refined_by': 'rules', 'signals': ['tag:data'], 'steps': ["Restate the question so it is falsifiable. 'Is X better?' becomes 'Does X reduce Y by more than Z?'", 'Declare in advance what result would change the decision — this is what separates analysis from justification.', 'Identify the evidence available and, explicitly, the evidence that is missing.', 'Compute the comparison, holding the method constant across every option.', 'Quantify uncertainty. A point estimate with no interval invites false confidence.', 'Answer the original question in one sentence, then show the working beneath it.'], 'subject_label': 'question under analysis', 'verb': 'Analyze'}


class SharepointListFormatter(BasicAgent):
    """Analyze agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'SharepointListFormatter'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'data_source': {'description': 'Optional. Where the evidence comes from.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'The question to answer, stated as a question.', 'type': 'string'}},
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
    print(SharepointListFormatter().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816abObWLblX6FvfUjnwzYzCFdUREsggcQgJklAusLJKBCjGCQgO/97H6R7r52vMuu9F9EfWulwSrDPPntcax/wby9e3yVV8/LlRfG6JPVayPTyqqjKNipfPr6EURs0ad2lVQlErL4pW8grR8hMvCbSqrTsoDxtOyj0Og8CvyrIg4I88sqPUAB0gFsRECm8Jgurewl1np9HnyF+LL0iDYBI3hdAo++1UQhV5VNXN9YR2CSErn3UjB+hOu/BpuB29CnI0yCD9nU0i5YZFFcNFN2AFNRU98/A3mjwijqP2pcvv/zz40sKvr98+e0lyL0WXHp5WF3PVstgo03VFF7XRQ1Yl3vlGQjUIwjG7HcdNUB3AS6FUQy9/vrQRnn8EfqP/8juXnNuf/7ytYReP19f5v+MHriYRFBXecDxEAq82vPTPO3Gz9Ayv3tjCzVR9wwi1HZNWp4/P1d+11TV0D/mex+em3w+R92Hry8VMMGbs/D15WcIOP31penn759nLfWHnz/n1T1qPvz8XU/b+5co6GZlwOrP315/v6oFgt9F0xj6Zmpr7nWvJgrSOgLKf/Bv/jxNf1X3GpJvT+EPVf0R+nPNsz//APY+K8kHev9cLYgBWPny+QLS8+F1j6a6RaVXBtGHn/9KbZBEQTaXzX9L7y9PxUnkhSBaryH5+eMjff+E4Fff3nX+9bY1KJj/iSdA/G2790D9le5HZv+TalDtUfueyz9V92cL4H9Av/ylb/9uwUco/vrCR3kKmmvu2S/Qb48S+eWn8PvFn/75O1D9X6oxq74JHhq+FV6ZxlHbffv2y0/t4/JP//zlp74GVRx5xbe+yf9M55/F9bHPHyL4KvXhj2vB/ocyK2fwee8h6Leq/l/N75+ho5en4ffr7Rfox06cPzA0O/G26TMEP3RjC2z9IY4/v/wOQKcE3vTB4zbAj7/9DVLSoKnaKu4gM6j6DgIJ7tIimo23krSFwJ8ZNZoZydoUBPZVDtT/nOHZ4iqGfv3fgdd98s4AUD+1WZrnLdK+49m3OaXf4jdE+/UzZAGNVZOe09LLIWOpaV/Lx9p5t7qJ2qi5AYTyxy76BJZ9mr8AAId+/Uud3x7LP9fjrw9wTp9QZ3DbGebaHuD67NApAdj8ND/wSigaoqAHmvMqAGbEKYDmj8DRtspvACZn5x+uQGEKgKSrAJDPukGAvszKfv31V0ANydfyicsE9CSjFgEC7+ZAnz4Bf+I8PSfd1zIKkgr66bfff4L+D/TvVj2Uz3togBpeww8s3Jl7FQLt1BdADGQG5BJgxSP8v/3+GlWgpowaCCQrjdPouXhmoyh8C7EpLj/hFA35EYgeCGtRV00HwB5Ku8/QNobe7YXmUDfdTAdJNdNoBKgtjMpgBFo94M57JMuqg1pQc20MGLFvo8euv/qN9zCxAH3tdb9CCqcB8qly8Nds5kMILK7KFIT/vQCe14GS5qcWWr2p+AypcwFCtdd4ddJ4r3vE3jMvgHTelj9YvozuX8uZYKM5VI9ueIYHCIHIBK8p/TTnHBB9AVo/bN/2fsh4M0VaD6psvoJ541npoPpAVILqwernPg1n/P/7a0m1SdXn4SN+wNJZ02sWwtesPGrwh+Fk5nnoneihrz2OYiT0//kcM/uwFARjLSytNQ+tVctwnrEFtjwMeQ5tYK54rHz00fdZ4w1P3mD1a5mnoFCa8e9PyUdGXmWeUNU3wGxjaTz0g3IAkZr1Pqp1rr6mmevc+1q+4fdH4McDrGZfqwCU/lxxbxvOd98sTUD/zr+/c/kju004RwZUJFT3PggGFEdR6HsgKF3SzB33milQutHcffckDZI/eAUB7SBeQP8c8BT0EEjMI3RqBdwEzRY3VfFdPJ1nL2BF2AfA2iRqQP5OoGnmwgGZi8AANcuAKPz0UAUVEYgxMPE9wgAZ66cxVZO9GegBP7x8nKIfE/B673uVP0yZrQdKvbnGvpb3GW7DaHgm9t3M11QBW4u5Lx+L/pjtV1ehH3nm71/Lh4nvCA/aPZ9r9IfYQKABivZRkHPNtQBxiui1fkAhPNj485NQn4z9bssXiFta0PIJbQ/mgT4Ub5z2oL/DH5PyBUq6rm6/IMi72Odz2iW9/zmtkH+hsb9955xPc+d8euecP+h+huEL9K8HlT+IvdblFwj7jH5G51tyGkRz4b1+vkB9+Q4bH374/pq2R1qi8COAuBkPgWVzibZJFD7mDSP6nldgUgUsndE1HwGZvlPNmwjgm3MTnWfhJ/W0M2PdAUk+dIPIfy3fc//aGADKy/PMk231Q8M+OBdk8pmod0oAt8oO7B3OQ9k5ms9A+exuG718Kfs8//gCICr6t2efGfBBXYKwzWcl0CJguunS6PFrrtVvzy0fP/9wHNw/vnj53Eignx51FN3S8BFsAPkAM+bCn22asRCseJ555inpfYT6V7WPrgRwElZf5uacgfOBw2+T60fo7SzxOPGVPTim/TJPzbMvQBT87132/QjrRy///BMzXofofzVibkqA2+2Dk2Y6KFtwwAI56Z6Jn5H87f6fOAhUN9G1BxQYzsZ99/a7EdVz598fRnfP0+ZvL28A8ZqK1/kPiINO/NTOJIiAugYbgt/PigL3/geT4etKcB8MKGApG1KeF+C+RzAYTlOMB05GGBOyJBFGVEiyBBVhOB4sUDQiWIyNiIDFUZxCaYwiSRLzgb5neXybOT6drZnhEQThEyjq6PttcCl8deNp9hyj90F0dvfVm99efJoEkiLZbpfPD4ewR4/GGd9IfHiiI8e12a1XHGjTjiYOP02N28lrj7ObHY7jxGETZuZeVp3DGND6sTGFs0WtS2altd2CUmhjmzZSuDnb3n29zILeVwpbo6YyLCith0PGM08Nsc/o+6EcT8WGY6eb6+ZX3yIpL4oHt5Nc1N/6XOeR2NbbLDqTKyc5MQzjWuj45ihEgj+Ygiyd4Iu8V6msoszd8Wyn8BTpdGotsyb09H63EgZT1hppGE/juV1XbSzRJ+KACdnG8DcecTjUhxyVfLLdLAlVbg8jhu5Cx7V02PTvt52qaRPGLqJyVwyxNjjtjagHWCDPhISevHZ1HaU8oqy26qaxs1NDMOS9nppR5t7qg2OvTgW2vvY3y3A9qSAseFq6rnSNzmfhuNm4XpQA1bJEFifzfnAyNc34hXddOxJqrXyc7YLRrC0534j98pp6SRz5xu7k87Z2HFnZPwWjraYNae8b1iyCe7rzTSlIcOto3RfN4N3P2Pm6MRcZsxH6LbcpePx0z9rUdhpVqvJjqd0l0zHj7S5Tyl3M+C7Pu5upxHMM39YBY/cL0bkeXUejyZSWc1PIGcZNj3Jl3sYcbSbeIVZsFrSmdD/6q465nETVTNxThg1xW1Qm3nYoPCFH9XJl+w13L81x4PtuaWZ7r97xo3pZ0ZtrT2C1oEYtSaDiWh2x/hbKRKNWFxfL+zuYOdP21IznalKmjLW4Nj3pusHFJ5SE08vysrnkHmxzK4fRpAGthTW+VRDGkfitNaFMlK72p1j03FrKDAc1ySnDYZkLHASzbd7aD1J746YtrRWYuDKOUn/NTjqlRIa8ZZ1x1Pi2YmKFMm6ryPbXkb1FfXk/Mm7lkYILb4a0RPipOEyTGntde3OqDalMC2tFrvlpWSxg09wISm8vpsMJJHi8W5FgBXA2wk4RVRFXjeall9ZOvWkxeRg0dY8F9BHlTmJyLt2Ia08nfJ2WhpnvPVpMNDnVr60sJNNoZ5jurwRizK5C7xMCYTJ0RdmKXJvu/Qx3NWfEGRgkA5g/yEonO/HyKjEbtFzzwcqdiiVLLxRpshR92hwIsUMdil3TqG5qlAJvqlNi2awSTBcLxphqZ3M4K4oRybiwechupKnaqNtfGwWfYlJnS+qgkQvrQBujwHopf9/dFHTjclOdxMSyapoTvj1kEnMPc83zDpu7c5mygHFIunA6PTNul4RkEGN570TXljaiFN9uS5Uv8YtcMZm1GuA6xYabF65TyTDRA3I0NcwzHS5o1+hRgnUuuPAww2INe+KOXnFc5UfaMm/8GmaT7GLe+ZpVJ6RYyrmguNI26dlbcqPL8hJWonO+lZEuts5u2cQLMRFkTvU2Q0IzVOBv4JW2XyrmtGY8QV4ai/pu1bZbJ4mnXFYCi3LhejQ9QjFA2TOK4hTHVpBbh9I8bnGxy6Y0nc0iHtWmM1B2Qe/5QaXVqBGRU4I4K2IbG/dA2DR1vvbg9V3Ch1DHORTzbJfLzvCZ3O9vtqwhUT8SxljWAh5753zPn1oJw0m+um+lKXZAuRbuFQ+YOjG8bYTs98mhQg42rYkLZy8uWk20+pUquseDdl6TuygHc16ykhzBXArioHSiY1OG5BBebdGZgCrgIL8ZDkVWc1my2SmnutgOBiKM293Vlo1LlHKtuQrdwuGPWkyp5sq7raS6kXcVFemDfSHkdNQ3YQ0fj+6UkclZK3g0SBmlatAaoYtUrXDBP7qMue62Z0ywi50s+ted1Xpqzo3u7gyIw+ZKr8InNdlcylhUT8XWFo3xelSckRV2dKvcD5htEQ0HJ2uOsNNotcimTbtCh+6Eb3Jz626IrE/MGOXU/eYAs5ejYaTtYhVIGbcleveIlQu96A4B5WY3X/AVoeO2R1deO+4uv3Lni4NJObI0lVL0DtJl56cTW43r1eXAYxWC4DbrWIrHJY5LlVv6otSeeL0V6h0dXFanbATmJa1DI99h3NHbhk0PY8tyebbxi7heRovl1JKGerz121FS9VXV6px1cpphFZ+rrDyQp01or7hgK2StNGEjHJVxh/c8iywzxE4TJBfMZBmSKOwSdsuX4q5cHTjx1KrDLjfzih5t1AwMjFNHSyqwlemTE3M/Lft0w+3rc5Ac9od4ay5CSjqcnXqBb50qb1P/PnbLVqJGexSYcu/ujHG6OrK1ul6E7HRW9PWu2mRD2GbdareBz/dxO+gglK51Wt6vnuSGdJ3VcnkLKec81I1Hm8Uui46pFQ/3HXyaRFfPHPyyLFfFxhnS801F9OaiRieDcVe6vlnfOffAJfwNz4VQlgaLiZLlIr4NhNRGVR8vPcZxlUDdVrEN2MabAqZwle1iyZuds1vD20y6xnuJVQV8LElP0vhcIXhJlndXxioSebjQS3njGcRJ4xaVvC2JdlEaPc/tTME+7bd7vdQyPqD7DZmix0PbYpOfF3YielV28GFXdnN0rDdHeT9tMXU76VKS76PjFB/Jc0heri5WrnH0IgdIY6MF5zZXdiFWq3qPLbPFUsao1vPpXlTQYdSPp45tV55bUXil2LXZkK0NX0/ctcGu911fj4ebtZSHfXpcx+xq2CwNGE/XPOGIFRxRVRJttZsBk/lNopuDKp2tXTwtvKXjitNw0M2jetsVxmIw0Cu80AXCp5rimuYiaDSpuqcRFR+k474oFMs7aIMuONfJ3HmYhiGrqUxRxq1DuxJxTCz4Ssz9paCYiSage5K0REW21STgUlhrqrRpyE3OZ7qZu1xVXccktrlQEtZrpa8NNGl57H4Rw5uQojATqhcBZU7Lcij47RZMDx6ibPW8Px4YyoSzNIPPCnmlh2rvuOFe1qz1MSPMJUV0hr6Vu9PyUt11M9TlIe7FZmPVU1NRS0Vt1ssbp8hSOHFG24DZggezQL7Z0Kq+0wOQceYcOiW9PyhhuhKwAD9VzV7gc4FAL3pDYvguKA+i7Ua+b96STsqS7lKl5xWYY65KtrTD9oye+mNoeasThuoSboT0hbPt+GqzRKVaUgkGera+EqG1owh7wTDKdAtPOJvSGIaI1d64J66SMBnB0KVy4PZWi2ksHZPbBa8snVPm5xOd2Q4gUAaMb+ohnzp3vbqSQkCG2QLJjAWH7F3CVAwVzVQ6wNYZu7kESmsX9hHucD1CuUTUp9s1VvuWv5+Rwl/iV3p1kfOdL01GiHcN1aK9yrWKiMKcdeV9aQ/aPDCmoxbZJYFwJZbWG36vwsi1hIU+7+K9TtK0LTB6Utd2NMh6j7m+7vcj03rJMq63R2Ilkl2BJBbN51mIXPoF76TX5cpKOp/UBeEybsZldt9oa5RbFMFQlgASDi0TMH7pXAnJLGK8CUMGV4Qm12UbPVGxddufgmpE6l3C6ouqRWw4VTeDr3UtT98ydaWnUkE2CBXHIAUNtlv7LawTgDLisFvZaX0TO/1wu+QHX9cGu1yMYrOn3A5310iJ2KoR7CMtOakXxOkMuC1P3hG2EcTxdXOsVntfAUPD4aRrYslcLOSKt7Dqu6kU0Hbd3TcJelVMnGyHNt7jC01dENcEA/Myv1tgjd+aewZmhCbervJ42dxdwsenHSzzC4tCkzgVLv24w5Fsm3Ypk+AOkjfl+pCGx2R5V7Z+vrOiVc85NB3pRbKNrs6+XDo4gw4peSjEA4e3FiAgb1hPFNy5DtntMJZc3Sv7cEPU41rdwU0dsid+RS6i1WFz1oZVJg9bdIney5Sob5e9xYnDquDqla4oV54zfDTcXQidtDF/DA82aJNSMVUNCbVt3zSFgfjMFcl7Qhk2bGS0hHYwL2sGULmGo6Irck2/MBbh1h8BC0ohGxDEnbUbvDdpBUcO9YVb7/f7hjiviKY6EhlFD/CZXmgLu7aOEz0Rvq2zozENV42x6kbax0RdYQQFphpUqLV+bG6WrDCbfedlJ6EKdWsdiFbExVZBHTgHu/NZyUob4YgTjOgpnLRa8CK5PBgooaeOxZDUGrfio0S04Z2alKbk1Gi9qpgFlbUxmFhDQr5usqmxsXXU9wv46u7YvcxrHRzjXRzURGeBo3rGplQKH3al7RlXywzLWA4vPbMsrXXExLcQISnsjO7AqDJUaI4vMGq5owwq5TyFt0Qe8wK0rP2zIlZ4FSvGlcYuDblMi5h3McpyO16G5XXIHXbm+ZwKVclrSrNH+OPmVjjn0BWuQpgvM+O6Zm1m0+hBct2PZdidWJnWSBJZcy6+PC/8ivQ2rCqpW/bC3sFgR/SnsVgv9MjRWzi8kdldVUCsS5ls1/viGu5U2brSZzQIJJHdD6G3YiT4avmR68uatLAdMe+uaZsRzarWqBtMXpmOGvw7wi7LiyQtmLXonPTLFTv3+K0609TICRoxUuuQOtCLa3xfM1nAt9PN6HKNyj1/JKWpI1PyRlxEXF2bVMd6a7ZKjbXqeov4WojHjrofp8g4ZcTQ1xHF3JS9d7BajmRLcXuwJ1o8nUJ9j+tFRgubeyCyVbgqSjAfDzuNZ3WaqHwBwfro0reG6bDmOB5EGocl2I6khqf4SPcVEvWR/XKJY5qgb5BBZTAZUaWpVvQT0RwWvXe/qJS7SIyYrxNaHoeLNfSuG/p0ipHKDa22NCt5zbqEMd7TqbIMlwPoRGeKhf6UsODclF6EGIV97BSuwFRaJP5py26YXF9TjsCuivtlq0m01hM3xERIZ2/3BWGLuhGd0Zqi96dEw7qOCk1/PBqluwp0LKK6kSbYNQJmTWWMxMmV1cgKbr0Zi0bK9KJzpG0HFU71IG0PLpaSm5NZCW1JjZLtXWQYtdhLERruAK/FXdThfOZHFS9hNz1lduykLfJ0SHiiVC/bfS/BJ1ixgoOFps19SNALuVt5fqHpguEgoLjpdZVZSnWfukPIZzsuvPsauzjhJAxaktk6G8LC/QLxI6JW3dyb4q5Sl7cqQbs1OP9e9pJKqsc965B+iGFyINtIo4VTZPc0PcWgJxKElc61M1725jEr42LRxRgPd9dtseR7Tr1EisD3YhbfRdMaECKSmxtAs/zKX4lNeGQWRqACHm7R1I617BSGTaf1bk2sQlJj4ROTI62A3dyIUHEDKc5qMyyCYG3fEMRCPep2OywmTSNuMGVwqz1aEYHQB5u+2N+xe77Ajyd5u+Sv4UR3+N3yl8Z6oR4wPds7fn/ByRDT7KFp9/LJSverIoslmgvPeZ2SNc2OiLRCk6yfKi293NYp4me8gShhsulDgiRu6nnJTXimUguXRWl5hR8iOb0SJt845J3oB7/vXJUUycgjzCL1CoHchGIkLRAcpkoGkAG8sgY6X2LhAJfoHVmffEve3sM1c7FxcAZlMdgit57oVpuyqxalfUFW+JY6B8dI0ZfLl48v8wPx18fa//Xr6vkR5P+zp53Ph5Zvr7Iez50jL/zy2OvLf8OWf358aYIUWPJ8iNvm/fn1oeh/foT76S9fiszrxudL3/kl29C9PenvvPP8D59+iAkQfX8D842gqZeH9eH81uiWdnNoHm8y2/kx+fzQGZj3+voEWEV8Rj/jL7//X4ofY/ojJgAA -->
