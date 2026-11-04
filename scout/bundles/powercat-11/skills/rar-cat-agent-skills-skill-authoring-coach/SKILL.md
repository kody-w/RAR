---
name: "rar-cat-agent-skills-skill-authoring-coach"
description: "Help makers design concise, reusable Agent Skills with clear triggers, instructions, resources, and packaging."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/skill_authoring_coach", "rar_sha256": "d87d562cb6ff69f03c5fbe70ec218c4a216e2f3a22cb4aa2055fdc360addc454", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "2.1.2", "author": "Simon Owen", "tags": ["skills", "authoring", "documentation", "productivity", "agent"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/skill_authoring_coach`. The original RAPP
agent is preserved byte-for-byte in `skill_authoring_coach_agent.py` and in the RCI capsule.

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

Skill Authoring Coach — Help makers design concise, reusable Agent Skills with clear triggers, instructions, resources, and packaging.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a design capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#skill-authoring-coach
  Upstream author: Simon Owen
  Upstream version: 0.1.0
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `skill_authoring_coach_agent.py` and embedded as the fenced Python below (sha256 d87d562cb6ff69f0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `skill_authoring_coach_agent.py` first:

```bash
python3 skill_authoring_coach_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 skill_authoring_coach_agent.py   # or on stdin
python3 skill_authoring_coach_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/skill_authoring_coach_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/skill_authoring_coach_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/skill_authoring_coach/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""
Skill Authoring Coach — Help makers design concise, reusable Agent Skills with clear triggers, instructions, resources, and packaging.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a design capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#skill-authoring-coach
  Upstream author: Simon Owen
  Upstream version: 0.1.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/skill_authoring_coach',
    "version": '2.1.2',
    "display_name": 'Skill Authoring Coach',
    "description": 'Help makers design concise, reusable Agent Skills with clear triggers, instructions, resources, and packaging.',
    "author": 'Simon Owen',
    "tags": ['skills', 'authoring', 'documentation', 'productivity', 'agent'],
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
        "upstream_slug": 'skill-authoring-coach',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#skill-authoring-coach',
        "upstream_version": '0.1.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'dd0ed10e586119e5',
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
_SPEC = {'archetype': 'design', 'checks': ['Constraints are written down and the design respects them.', 'At least two options were genuinely considered.', 'The trade-off accepted is stated explicitly.', 'The riskiest assumption has a cheap test attached.'], 'confidence': 1.0, 'deliverable': 'A design record: constraints, options considered, the choice, the trade-off accepted, and the first thing to de-risk.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'constraints': 'Optional. Hard constraints — budget, platform, deadline, compliance.', 'subject': 'What is being designed.'}, 'refined_by': 'rules', 'signals': ['word:design'], 'steps': ['Write the constraints down first. A design produced before the constraints are known is a preference.', 'State the success condition in terms someone else could measure without you present.', 'Produce at least two genuinely different approaches; a single option is a decision already made, not a design.', 'Compare them against the constraints, and name what each one gives up. Every design gives something up.', 'Choose, and record why the rejected options were rejected — that record is what survives the next reorganisation.', 'Identify the riskiest assumption and the cheapest way to test it before committing.'], 'subject_label': 'thing being designed', 'verb': 'Design'}


class SkillAuthoringCoach(BasicAgent):
    """Design agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'SkillAuthoringCoach'
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
    print(SkillAuthoringCoach().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/716aZOjVpPuX9HU+8HtobsAsfcbjrhCgEAgkAAJgdvRZl/EJlYhj//7HFTqanvGfmduxI2r7qiSRJ7M5+TyZB6o317cvkuq5uXzi5EWVbnQxrB8+fgShK3fpHWXViW4JIZ5vSjcS9i0C3AljcuFX5V+2oYfF03Yt66Xh4tVHJbdwriked4uxrRLFn4eus2ia9I4Bis/LtKy7Zren5W288K26hs/BG/dMljUrn9x47SMX4H58OYWdR62L59//uXjSwrev3z+7cXP3badkc42Vg/cQH5duX4C1uRuGYOL9QS+n7dQh01UNQX4KgijxfPThzbMo4+Lf//3y+g2cfvj5y/l4vn68jL/0/ty0SXhoqvctguDhe/WrpfmaTe9Llb56E4tAN71Tdku3AXYzgz4beV3TVW9+Gm+9uHNyGscdh++vFQAgjvv/cvLj4uqAfaafn7/OmupP/z4mldj2Hz48buetvey0O9mZQD169fn56daIPhdNI0WX409v37aakI/rUOg/A/7m19v0J/qni75+ib8oao/Lv5a87yfnwDet6TwgN6/Vgt8AFa+vGZVWn542miqISzd0g8//Ph3av0k9C952nb/K70/vylOQjcA3nq65MePj/D9soCee3vX+fdma5Aw/zc7AeLfzL076u90PyL7X1TnaRm277H8S3V/tQD6afHz3+7tXy34uIi+vHBhng4g70CBfl789kiRn38Ivn/5wy+/A9X/oxrjUamzhq+FW6ZR2HZfv/78w1sB//DLzz/0Ncji0C2+9k3+Vzr/yq8PO3/y4FPqw5/XAvvH8lJWY7l4r6HFb1X9b83vr4uTm6fB9+/bz4s/VuL8ghbzJr4ZfXPBH6qxBVj/4McfX34HhPMHogL88Y9/LHap31RtFQGC86u+W4AAd2kRzuDNJG0X4P/MGk0I/NqmMx2+yYH8nyM8I66ixa//x3e7T+5MlJ/aB1HCj19f3W9k9tWf2ezX14UJtIFvACG6+UJf7fdfyse62VINqDNsBsBO3tSFn0ARf5rfAH5d/PqX+r4+lr7W068Pqk3fKE5fSzO9tX0evs4bsZKwfML23XIR3kK/B1rzygcQojQPn6SdD4Ae500/bC2CFBBIVzXTQzdwzOdZ2a+//uq5bfKlfONjbPHWT1oYCLzDWXz6BPYS5WmcdF/K0E+qxQ+//f7D4j8W/2rVQ/lsYw/awdPtAOHW0NQFKKO+AGLto9kAjni4/bffnx4FasqwWYAgpVEavi0GaXgJg2/uNcTVpyVBLrwQuBW4tKirpgOOXKTd60KKFu94gdH50twGkqrtQF+swzIIS38CWl2wnXdPllW3aEGutdH0cdG34cPqr17jPiAWoJ7d7tfFbr0HTafKwY8Z5kMILK7KFLj/Pfhv3wMlzQ/tgv2m4nWhzokHemjj1knjPm1E7ltcQLP5thwodxdlOH4p56Yazq56VMGbe4AQ8Iz/DOmnOeag0Reg5IP2m+2HjDu3RvPRIpsvZfvMcLeZQ+EDxgdG4z4NZt7/5zOl2qTq8+DhP4B01vSMQvCMyiMHH6198d7bF4/mvvjSLxEUX/z/HUNmOKvNRuc3K5PnFrxq6vabm4DRbjbyrLJuWoBceSuJ7+PCN0r4xoxfyjwFMW+mf75JPpz7lHnD0zfAF/pKf+gHkQVumvU+Em9OpKaZU9b9Un6jYIB48eAb4HtQpSCL5+T5ZnC++g1pAkpx/vy9HT8C1QTznkFyLerey0HgozAMPOABgKqZi+fpeJCF4VxIY5KCaPxxVwugHQQb6F8AECkoB0DTD9epFdgmiGDUVMV38XQenwCKoPcB2iRswteFBfJ/zoEWFB2YgWYZ4IUfHqoWRQh8DCC+e7hN3PoNTNVcvgF03/Phu/+fl77n6wPJDB7odAO3A54cZ9IMwttbXN9RPiMFoBZzhT0W/TnYz53+KZf++aV8IHznaVC4+SMnv7tmAQqmaB+ZNvNOC7ijCJ/pA/LgkYmvby3xree+Y/m8WK/MP2f3h+JbV3o0sOOfY/J5kXRd3X6G4Xex1xjUQ++9phX83xrRPx6/P713jk+PzvEnvW/XPi++nxT+dPmZip8XyCv6isyXlNQP51x7vj4v+vK96D/84f0zVI9QhMFHQFAzm4FEmbOyTcLgMSXo4fdYAihVAZhrdvEE2uB7o/gmArpF3ITxLPzWONq534ygxT10A29/Kd/j/awFQMRlPBNBW/2hRh8dE0TvLTjvhA4ulR2wHcyjVBzOp5Z83m4bvnwu+zz/+FK6Rfi3p5WZqkEeApfNJxtQEWAe6dLw8QlULQAGMq97fPzzWUx7vHHz14Xozpi/y35zo9cH4BTwcQFGzG4e8D+C4nCDedr6OLN5naczAcyAu6meEb4dY+bB530q+u92H1UK6CWoPs/F+lAPfr4Po7OVt+PB4wBX9uDk9fM8CM+bBaLg17vs+wHTC19++QsYz7n4b0CkM1HM1PJW82HwF1sBSprw2oM+Fswwvu/ru7nqzcbvD3jd21Hxt5dv3PCMynN4A+KgCD+1cyeDQXIDg+DzW2KBa//Lse65CjAYmDDmcylNBQS59D0yikgmQjCfiLyQQkJ/idI+7i5RMlxGmLsEIrjrLhGCiAIfIxE3CHycwIG+t6T8OjfpdEbi+UiEkgxKAyZnvOUSCNMhEmEMSUUuGWLLMKARBPG+L72Aqntu7207s+/eJ8zZDc9d/vbikfh8MwBvpdXbaw1DJxfGJG86i5CI0DcrQthxZZ8vuazxUyJn18jE3PJqNwK/dKtjZktiP6rpfXfusXbsJd3kchZem1BcToHPtHfoJskFpW1O59N61LEtVpNhCUH90G/M0Yzg8l7Cq2xf36KzlKz1e3i9svjJWmKCngYyrgSIBBko4E5hEqSc6dpdQ1PR+txnF8Ss8i0TilLd5YOMIKuOZDYRYip3L+VVa1PzjX0XgmXSnpCbqjtrZeusb8hO3037gCUv5OiqN0s3NyESKDxqxLl3VcEeNEKQFXx5vAZ4y2omF1CqtHaN6Xhvnb0J+QPJme2wb+hDWfqeg6UUX9NtVKdC3RpLOeI2EQ2xnVMNQkPAMNSe6OtSNzze8mVjMBppVQRXetf4Jlx10gUvbpmCwTGk22uvUXBfsfcNZt2UIEzuvbMhhovjGoapbwsCvpluE8VD6zjLNXoZDrDAnOq7HhWBrSepsDt4RTdsrS5Y6mPaCKfsRInCUG4Od+kyxIoadSNciL3TQnBa6LdbDe+Xcre8N4zVVvo5O5LDCeWLClrKCW4SB+eW4w1c4l5j2EtCvXFdoNoQTUq+oJ0R2L5ANZRPkrtulfa0t/AMI6ztwVpOxJrbD+JxP1nwuJJ94qhpy7GItxuFIfzo5twE7HA82IJN3v02taQ45nb7GE7OHiLHtKZz69iVVkIL3VH5ujqVVYZgfGJuC1lWh85ha2/nCGnDONoQqRiC0WdsmeN1hfqpcghTeYPH+6uij3f4tB32VcCbOFTCBE1Xa0nRt+e9HlpHkrad3RampvoOKRRqGRKcDPja1mWyHyYXrev1shrdzJgy67bxcrZlVw1Tro8pK+WZke6GhtqYmuRaRDzJmR4fkl0XsXRtQIdjit42Kiy5JO5mSJRjGIbiEIMRNyqKUiWEoShL9oi6UQm7dVflgGnyKuaOfbfWnIk6aSRbQlKRWlrgGH4WyOpO2YoCgcpOsQH1JK8omy/ymMYvuCNU/YoP6YOpSjYXyoaEs7aHrK6I4Pl2Ntisyqe+gdj16aphuUN6rbBjxKBv8/40gY3E0mXiGRXSMTDCJbsgtVGD1q+ec8M3FrFnj0glLg8OcWh3AhUhksHZ4qVaHlcGdnMJeO0o8LblaNyztOls7mwNsXZFCmoJSonTwd0S+k6Q1oqZNie5zZbqGHmiskrpVTBsKuY6Bml3r5G88PIYREGLW/PCJHB4uhwsy9ZPkjOmZmvcLy4P0Rty2N8rCA06HD2Kggjg3vuWQiGojQnGktRQqwToTm03/Eod7ENiStREsXIg1tnN9DzZpi1oiyYs0W59/xK5yNHCWxCXiTxs721Q+LeiWMoy7cFdeBWTGquPKSlrvXZx4DvZTGGxm9xLhzaom/I9My6pkELPbgSaQ3fj9uMtSnzqThyOoWxrZ1g5Go5d3UNXTBJkqHdwwYsyf9XWLb0V4gPco+dbwJlkxTbYwQ7aLSpqo4yLrYlLm1sRSGN3OhAs3lRLsm75nkVL2Rn6zq+3CZ6LnR0z+EUkSNMR+ha1/UsJSzaNJ7ncV/uGxXPdsQF0aKcGo7AVTVexrlK5RvkrLGB2shTVpFrD7MHqJTcOLGe8Z+xdQffEkUqoKN2mltLWWK4g9HRu92eFLIvWcyhpJCtDQ1KHsbhc0XwBDiDDlS1+OXGNVWjXMI8kFzj2tFTLyyDssk1HISxzE+ojRa7Vendu4kI2Dx2e7MUL5mZ1EIr81DaZeq92R/9Ub6+1zijG0bjJzSE9H7YHfXeNYMD9UTqiTLM1SAOtO/mmppwEitNjx+hAQ1Lj7/lIrSdNHPzVPjLs3q0r9abTNEsyKRfEp2jkwpiDTHsZCOqdwROFSOGVrJ67WGsLzjRbfDQdNk683f2whsjYSmt+Cu7nsLpsk6vMn8HkwN7WS5M5YKloae5Rk7g77PIV6jIkQRud2tAOg0rknkWdA8Xtz6PAHdu7OaX3tFFcd1qCJk+Yp+2mN+6jfoGdMC/NG+CGPCpugxsnfGa0FeIayWi3chPaoYHtGqGrMTPRZSWFlEI+32/nAW7KCGtueA4fG+q+gsarmmvJSjhYxr3FNefMIlvGl9F1AaG+bTkonzZ+Z+8JTxaleHeVoJpW4p7TeYIs7nzFn5L7LuPvBDmFrkRfK/7qHQvSpbb8KEP1+hyXfF4U5QaVxCZgPWrrb5ecP5HyLjC8ItyxdZTifTXeBbi9n0WKAGMi0nQtGzh9laMhujveoS43popEUaXCJpGEnd3GiX2Ppq8IscZdreNqD8wdxNZMirS4Tj5jR0sp1AixuvEXBY1Xwg2HJOpYHfokKOt8HfHLvcbrG7LULvRFoVkobo9GGgwtJqsi0XCiNBiYErprwLdpxruparmSjSAdx1+LA6dM/NoBfXe3xDZIRrt8J0nE+k4G0TQVVcwGPo9ssgsvOAWSbzXPKgZLboxDQTFT5oh7pyBx2lkmGuuHy0zk49BHjKwsU/naUuYuyY4ru9mJOLlHCJiO170VBMf4aq8y99ApVzrcD4VcclwMHZtQqQ14fVMuXkq5sKEYKCSunMA/83KsTAznu8VRvt0dZVQIlqxvJ7utTyA9+hUjNqvjaVWo9bgzBekUZOll0BrpoNeFTwX5Oq3XhQOvCjO8GXa68duWpwmiSPSS0OrsZOkpGQSGpGiyz8aWILY72FRLsdSni6TdhXFNHwoOgyr7vpTDscHvu9wpl5adObxeVTArNCdtJBmzFBVKl8X9lT56XGqtzqswPWkouZmwERGENvcZA2FkvOLXEDLV8rKQj54ZFnoXU25FTB2fXr2UgyVRi9QuzVTllOgeXjuDk2+gW+FJXV2sJIqKlEm1wMTBnTZnX0JEaGVmLqvR1TSWl+0WYWKO5Aw85rsSZ7tTOVrHDYrkze00yLXDU0W5w7xrLltYuZ/a6iKojCKnube/nskgxza4qjqmV92vazXL97CtE2Znb/CesxLWIil4zYbmcUNuAMB1twpKmVL6vW07iVuxakiRh/VO5XeXnI9RNuzZjvKLQizly95hAnrb7eNtzPlop7PJzctcxexJr78ztpwmzF5qzbBWx41l4SV6cPtr5twNm52iI7IFfWDpXEdn3zTXBOSpuKxqIZBcrParI+auAr64xeuVWEQyKx11z45JI4Q2CN/IKhx7YxuQo1CxlyxGDvIaucX2MbjqwR3aWIJ9Wwkd3U7VwcPitYQHbdF5qcPpsEadlYbhcey+OWXRZkVQdxmcb9KEotWyVk/sMFpWEq4GXJwar2/BYcUODE5b512ebwLT39ITJkflMMqOMa4sBpEaFDJyNqMHxbwmh53FUJN1OaFcERydK6W3eaytUGopWjKKsD2M8Gv6hIsCf4QHZtiuLr51a/BWls5GwcZeppWwsxKvwj6Pc1ZwsaUBGtVBTIOygTN71zpH6Ew2SdHsW9srdoUZNXftgDLFdqgu/QRGD7qnAyW7XqnuZLZJh605yNNOCtMTfjbFyDlB5FIMg2B7RaPziS68AKWQvulQ51yeImVo79qEBt5Sac5nOmyJeq2otSaha7iGbkJ0EjdRfCtu0+5gL7njOJzYyCLpDeVbMAPnU3od+ou5G4TEhBhONuX0uKYkQTSV22ZI4W15c0F1MOkYRpSCt4fDWKF7jmi5ioM5PCZFakU2+JB5JdbsoyBYMg1RIhyiK9yW0cYV5oq3lKDrSY2MqG8ACcskd6cpqFz1ydkFIyCkKpRT0f2t0dfloSc2ohHfzYMECyW6wTf42SkPxcFC9AhRTuJoMf5QW9v0rK+Icen7Ww4YWhFbo1fsbbypJZimC2SHoAO2uwsXu1fly9XsmzDD2p3m4Bv9aIhEdC5Vi65ujLNNqRip27GEVB/jS6M/h7eJGdbhSlLZI7xh2IhB1SOPpkNOhSsmpimP7Ph9eCkRxt2As9W1jc54URGOiEY3pZtkNO6h3k1tl4lSphZvhJsx55N7baA+AhPcITk4coWU7Qo0FxPM6SIyUsGgZRbkpHqak9SRtW8i2roIviu6KJzoIcOx6y0/9vR+u2nCJX4JMKYXTlBqHderIfZUrNWV3XG4BceC1yRw/pFK5FwQAsX7pZNqqxgVJKTC12xsj7CCREbWX9cZ6g/WrmECW6vTM0Sn22RUzs11taRdGbXDib8vjWB7JDqCiHEWBR5u0thoNSUcMIoeyns+wdxOPETyJmxVx4crrafBGZjJU8nmeScoOqoiN8YqMZEgL5dVu6e6WK4nswF5H2pDXO77eB8XN8w6KwETpK6Fp9QUgMlG6h2R9bvLxjmjVng6cMUhG8nctuA4uYWH+/kY+EVAoASO2fUBH+99iKj0LihCLuo27gCKPjxrzXJbQKzqIzDPRVDK5JnZ8xpRcUGHZAbG2Lo1MN2pNwXVhzyrMxTzqPV8GpbVNd4jUH9c3dftep1Rh5teBqN5oNhYquZO5WTXAOXlAmH4LD5v22sZ9VnlNa4XrcVotXK5QByCDEc8kH6BkZadDUVndDyX524rNri/g/Y1bKMclEGogIxLd6dYHpUfjss6GMZ8TTWjfwhYKmv5s0eLe1iddtpdCRE48sk1EbB8RXBXyjni7GZYHfcWe7egYmAPgR74ox14paXlAed7uK3lsodawfW0Rw0dJw2E9eKmU9F8OxBHYkufbOFouNfrtHINdL3umLvaq4c09mvYtaKwFvxzdM6xmDuMhd4zzNSQG0vWKUzMd2NvX31BlnCEOYKUwuDrtK5c3AfNyDbHAXdRAVWymqolHL9EJJ1esTtWQ8fihk/LM+nhFsrlrXtr46Ep6j1xwvxThHdEJwXQariv5IniJbw4hNCa66UdRLKQqO1tXPRyHb6sA+QCV8N9OYZbvdOIPNocqz3WVWGAllASxHdeO0daopEtUqfWJhJ6uF12jey7WLFHUmpzzamSIXPMiMNxn020XxlDvBGtTWBs7uKB7Dj2Sm9W0jKfynOuJNMZHCw2qCP31A71ErkNDnZn3aZ2uHWoRwVjF/qyWIn3cCvA9wOHyudcNkAMqd7cm1ehtmCVdLeRldv5no0GkwMnkylslVrvdjgTLf3Qgur7fQyPV3nsrq0biSe1zgoL9gVUP/UtoKRIHkOEPtrRNLhgekC1kJ+caTylApNzlwNP45tum58uLipfb1QETx6uqzRfaQyCmFgjurqfnVoja6LgfKmZPDevzS5GA2FP46Ls4eo9hARpky3hK3GuDTEnjQyhWv52p5qEpfqqP1lbfUyqkyfxewsRggzMBAp8VZm8cduqyhJ2sprgSKceirpWB/Xa+gjfo5XYtgcN4dkMnH0OgXukhbPKhfzWLkM33k6H3brtMjZVgNeD3YHzORldtqQy7Llbu1oFiDNwo7WkPZUNtKnQdATu8Z7GOtLUA63FKJvTFfLqylnk64cSFeiNe4HaVtmTZBwJDb4dikt/IPq+xUDpVRm8vsqWnZy31nSMsvAcnQJoeR0rloXWWqbxggkrxXHMTJOgkJAajme9tBLGS5V2gEefxQZC22b1UKaKCup83zsNxha0yLZ5QUQY1zUDer+vBx6jl2znwiJgh2WK0n5uCeyBW8L9WMFQ5mzkHWkO5s2mRjDpnc3z+nxPTvYlXvU1tr9iHmAxljexk3la247Yk/tzMh2ZqOgRwpmkcxYo3IW+FYhFrJdGJ+oIsZ9SQ55KBxFvzvKa4tQFDFW7ICl6zaO9czHF62yZqwQ4PCKkwi6t0EyrvcE1Dj5ivRPph6kc5XFColxYYbsA2ZHqNaEjGW+w3IUHzMNlX08OaulHjbHb34SCMWsXHDZuOS2Vh1sQXWAuTfIr7jJBxhMiPKorbzoLkHlcrVY//fTy8WV+TvJ82vGv//5gvu38/+zu99uN6m8PNB9PG0I3+Pyw9fl/wPHLx5fGTwGKt5v5bd7Hz5vg//VW/qe/fC42r5nent7Pj1hv3beHPp0bz3+19uaHFoi9L5wfelR+//7I/eWBPpgfHg5pN7vm7UY7gPZ8kgYQLV/R1+XL7/8JeWtdr6cnAAA= -->
