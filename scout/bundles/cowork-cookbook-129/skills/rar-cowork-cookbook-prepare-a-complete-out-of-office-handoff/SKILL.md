---
name: "rar-cowork-cookbook-prepare-a-complete-out-of-office-handoff"
description: "Step away from your laptop knowing nothing in flight will stall while you are out."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/prepare_a_complete_out_of_office_handoff", "rar_sha256": "6d9f56b07253ba06fef4da66d4c4caf1204fe4e4f9b92328b4b18cd24c251842", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "prepare_a_complete_out_of_office_handoff_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/prepare-a-complete-out-of-office-handoff:cd2a65a64d073587cea2da5ef596fb0e81d596e9264462bed036667f504f6b37", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "work_management", "advanced", "read_only"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/prepare_a_complete_out_of_office_handoff`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `prepare_a_complete_out_of_office_handoff_agent.py` is
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

Prepare a complete out-of-office handoff — Step away from your laptop knowing nothing in flight will stall while you are out.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a general capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/prepare-a-complete-out-of-office-handoff
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
      "description": "What to apply this capability to.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `prepare_a_complete_out_of_office_handoff_agent.py` and embedded as the fenced Python below (sha256 6d9f56b07253ba06…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `prepare_a_complete_out_of_office_handoff_agent.py` first:

```bash
python3 prepare_a_complete_out_of_office_handoff_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 prepare_a_complete_out_of_office_handoff_agent.py   # or on stdin
python3 prepare_a_complete_out_of_office_handoff_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Prepare a complete out-of-office handoff — Step away from your laptop knowing nothing in flight will stall while you are out.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a general capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/prepare-a-complete-out-of-office-handoff
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/prepare_a_complete_out_of_office_handoff',
    "version": '2.0.0',
    "display_name": 'Prepare a complete out-of-office handoff',
    "description": 'Step away from your laptop knowing nothing in flight will stall while you are out.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'work_management', 'advanced', 'read_only'],
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
        "upstream_slug": 'prepare-a-complete-out-of-office-handoff',
        "upstream_url": 'https://coworkcookbook.com/recipes/prepare-a-complete-out-of-office-handoff',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f3c59d4f41c70cbd',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'advanced', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'none', 'process_roots': ['work-management'], 'process_tags': ['work-management/coordinate-team-work/hand-off-work-during-absence'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'work-management/prepare-a-complete-out-of-office-handoff', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Calendar Management', 'Meetings', 'Communications'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'general', 'checks': ['The outcome is independently verifiable.', 'Assumptions are written down.', 'The result was checked against the original goal.'], 'confidence': 0.0, 'deliverable': 'A completed pass with the goal, the method, the result, and the assumptions it rests on.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'What to apply this capability to.'}, 'refined_by': 'rules', 'signals': [], 'steps': ['State the goal as an outcome someone else could verify without you.', 'List what you have and what is missing before starting.', 'Do the smallest version end to end, so unknowns surface while they are cheap.', 'Check the result against the goal as stated, not against what turned out to be convenient.', 'Record what would have to be true for this to be wrong.'], 'subject_label': 'task', 'verb': 'Run'}


class PrepareACompleteOutOfOfficeHandoff(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PrepareACompleteOutOfOfficeHandoff'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What to apply this capability to.', 'type': 'string'}},
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
    print(PrepareACompleteOutOfOfficeHandoff().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/616eZeiyJr3V2Fy/qjqMStZBMG8554zCIiCgIKK0tUniyXYZJNFwH77u7+BmllVd27P3J4zVmWqEPHsv2cJ8vcnu6nDvHx6fTKAnSGinSRRCErEzjyEy9u8PMG3/OTAH8TNs7qMnKbOy+rp+ckDlVtGRR3l2bC9BgVit3aP+GWeIn3elEhiF3VeIKcsb6MsQLK8Dof3KEP8JArCGmmjJEGqGjJF2jBKwLANsUuA5E39AlmAzk6LBFRPr7/+9vwUwc9Pr78/uYldwUtP6xIUcDHL5cOiGmhNrfma70cuWED5c9+HJBI7C+DaoodqZvB7AUo/L1N4yQM+8vj2uQKJ/4z8x3+cWrsMql9ev2bI4/X1afinNxlShwCpc7uqgYe4dmE7URLV/QvCJlDrCilB3ZRZhdhQoRKq+XLf+Z0StMTfh3uf70xeAlB//vqUQxHswYZfn35B8hLyK5vh88tApfj8y0uSt6D8/Mt3OlXjxMCtB2JQ6pe3x/cHWbjw+9LIv3H9O6R695YDvj79oNzwuss96Al3Pr3EeZR9vhMuyvwCMjtzwedf/oysGwL3lERV/S/R/fVOOAS2B3V6CP7L883IvyGjh0IfNP+cbQHd+lc0gcvf2T0jD0P9Ge2b/f+BdBJloPqw+D8l9882jP6O/Pqnuv13G54R/+sTD5LoAqPDScAr8vubsRa4Xz953y9++u0PSPp/JGNAKLo3Cm+pnUU+qOq3t18/VbfLn3779VNTwFgDdvrWlMk/o/nP7Hrj85MFH6s+/7wX8t9lQwLIkI9IR37Pi38r/3hB9nYSed+vV6/Ij3gZXiNkUOKd6d0EP2CmgrL+YMdfnv6AWSKD2jTu7TZE+b//O6JEbplXuV8jhgsTCwIdXEcpGITfhlGFbB+g/mbIy9XqJfW+IfDqAHeYIuwmqRGxtKMEgXgYPD5okPvIt/90b/nxi/vIj2hxz0dv9pv7yEhvkN1b7sP/Q1J6C+9Z6dsLsg0h+7yMgiizE0Rn12vEDkBWD4xvIVI16ZfLwBvKFd1zj84th7xTNQn4G/LtX2X2dqP7UvSDUl8z6CUbus5DapAWeWmXUdIj9pC1nL4GX2DChZmlzJPEsd0TMvxqipfBUmYIsof9XFgoQAfcpgZIkrtQAR/m7uoZhkCVJxeYJQerVqchuXtRCU2Wl/2tokDLvw7Evn375thV+DW7p+Uxcq8kFQoXfAiMfPkClbxXiq8ZcMMc+fT7H5+Q/4f8d7tuxAcea1gkbnaDoZ0gkqGpsLIETQqXVcgQJDAJ3fz4+x93hwzSZbD0QXRFfgRumyG170ExaHD30ruLoM6DiKB8cPrZbo+aFtXQWhDx1fPXbCABqyAo26gC70a8b76b/t3ndz6DT6qHDZNHZR3W3uJxcKabl94LsvSRD0tBdaFf68GjYV7VMIQLkHkgc3u4066/uxBWY6SCKKr8/hlpKqjqQPmbA0kPxklhqrLrb4jCrWHVyxP4azDQjT3cnWfR4PhH0N4vQyLlJxhjs3cSL4gKoDURGKh2EZZ2BW7rfPseEbDave+HxG0kAy0y1Hgw+OiG71vkPco8XPAe6UN78CX3v9wjHXlEOvK1ITCcRP7vO5FBClYUdUFktwKPCOpWP95DZmiJBg3uXRRsBxDYTtzj/3uL8J5N3vPs1yyJoJnL/m/3lf4tSu5r7rmrKWEI6Kx+oz/gtbzRjWro68F5ZTnEp/01e0/oz9A60NLVkJsgJE8DwPMPhs83290lDSHuhu/fiztyD6MhvGGAIkXjJJGL+AB4t1iuw3JAysO40PFgQA00khv+pBUCqUOnQvoIFCKCEQiT/s106sPaN3d8LI+GlglK4TUulBZCArwg5hChMMoqxAGw7xnWQCt8upFCUgBtDEX8sHAV2sVdmKFNfQhoIzCkYHlIfnTA4979zgCvDyRBorZn19CULfQBBEp3d+yHmA9XQVnTIapvm3729kNV5MfC87cBTVDE70kdRtZQs3+wDUzBZVrdsgqspqcK4jUFj/iBgXArzy/3Cnsv4R+yvP6X1vzzX+vebzVz97PjXpGwrovqFUXvde29rL1A1KEwRKICVO8l7ov95R2LX37C4pcHFn+ifzfXK/LXZPyJxCO2XxH8BXvBhlsryG0I3scLmoT7Mjt+IYe7XzMdfPc1ZJ+nMJ0MLuhhSv0oG+9LYO0IShAMi+9lpBqqTwsL3i173crARzw8wAKTYxYMNa/KfwDxoNPg3bvzPrIsvJUN+dsbOrcADJNNMohfgafXrEmS56fMTsG/OtEM2RSGLbTIMAxBBMFuqI7A7dtHZzR8+XlAu2ELJgUvfx0gBisX7GKfkY+G9Bl5HxFuk1fWwBnp16EZHljCpfDtY+3H9OeAJziY1X0xSH+fe4Ye7NEb/7kQdlEk/X/Jk3U+sP4HapBcCc4NrIHeINB3Db8zzu/c/rgJWt/Hu9+f3qE9fL4X5Lt3h2nwrzZPg/LvRe9tYGAPZG4tzs0WtzbxzYZ+GIrbD7eCoVK/3YPm6RXmB/D8BDfDFgP2vtfbZPt0lwqq873BhBQg0r9UQ7FGYcxDSrCEFoMqJ5ilfmAwXI682/rhw+ufdaX/I2RfXY+wJ5Q9IT2MHlMM7QKb8GwK+NR04jsYYHAPfgJTYkKSE8IBHjaeTCa0T2GkP3HGNBSmghGS2g9hUHzwCFTjw+z/64756U4HJnyCmkBCE2/qUxMHowlq7NjYxAc+6dmTiUe6pGv7OAFFAiQg/akzJcYE45AOzkD9SJegcIYkBnqPXu0u3Nt7X/zuozuCB7HSaBCdsG2XcWmc9Ka0PXHBGHPGLsAJ3KPHAKOmY59hIEfv6WPrw0+DG+/6D5EMFYZN0mXg8/vD70N0Tki4ckFWS/b+4tDp3ibGq1gNpSmOe0G68a3IIK8NuJp2bTmu3mVKYloGiWcqte/3bCdsQimOUpZ1ed1OJpde8DPOV1Lg5OzOcJMr4dZ8EfemznKqnky1jDy6urcIwr2YqEKxPIFQTY0mC2XaNTm0q5jWkDy7N9ZzE13TpTNayef9all6vVR4glN52l5wTlVm0POtLY5NRzDCgwU1xOTK7a+4d5Ycy8na+CyNpzUOIW5LabiiecXiFdJfjylq5McMDg4H8rKyzpSLbhWjrI/LPtxrc4GWepvA+rAjcEGf1bohrRo37EFurflCK7H4HFOivbHaKr6CiZ7R0enqLndbOTD2XbqPCj9b4SlzZYvEFK+p1MhSQMxiJTXnC7E7nQxi7xnakXJ2vVpr836x74PpXlOnjUqIIbjSJmajhStecHvuyCx57ORaOM2vvM8yxFm3yOQoF7vGWiz5zGBDy1bMJmfrJDVcS8WomJydqn5tsUFx4iPUYSOLnqdXZZsGKTnZtoU3L5Idv6630nlZUr7Re8p+H3W7VQawsHV9JuI6wZnVTRooduf1UwmOsZh67p25Uc2XSso42cZhjjAmTdYzxFo6yQXmOuICWyb7y4VTnOlRuuSaIiYXD0wO+Xgx48qL4wWeX+etXEpzPbUyC83cQETpAIsyfukYY0ihMtW52Ux3xtwlF7FgQ9OpnNiMRCLuhc61eboIveOYQ9uDhHvyvFl2dRUG68I5ZthqpNZp5NblccfEjD719go9J8rSuE622zDcJUcVm/dbXdiYNmya1ptCpZxYaw5iZm2ckNLLCAVmmp/WGM3WS3fbbfneXUsB0yrhmFiWkbruec2gxQOKtWjY8wHlnWliXpVb37DM7STbx1Uo4Mo+zunS9gW33PX2ydwex/YO8qBDXhMrI6GO3kzY7CJ5JniuvG04gJ8pA2axYnz2W8+dY4J+5Gc7zZy4ViePg76NSPUYx9rpEptSLxGt4C3LlSRehP11p5+seaqZFlZsw15FIbTU9hy3/WjqMzYeEOes4+Um01e87MxBV5OFe+BlhQ1kKtKtjJJmk5FXWFXt0o00yVF/jhP2lGmOanVBx9G8vlCcJk/RKEjl8qDRaW8usKm+kg6MRjZ1fL4YGhoabHtINiZjhhV/mskMFmvM2DK08WkeWyBQnZ06CiWGYGab6alJyqAa7cahKnZlufQYlSL4/SyRCYywFoC16nN4mBSSNt/S/GrekfJUxc2ZhO6EfDwplLNalcvyUKxTRjmkBTsP5+yFy6ipeJjzl23oQJgEyoRLFFSIGNuXRsusXZEdkYrm4oguj4GOy0dM3MsBN9qM6Nm020W8ENCsanHCQqsOMswXa428LiLNP83OUpJkjRX15WpHyigu6qv5nPWnRdvt1EkWHLz2RO1JtCp2drnxGXQdr9amODlvOWYxAwu3nzZ80FfXJbU9tCuuPB5w35ac/aS21TG9aVR9CVAwwhR9pAVE6XYooRRMVmy2RVJczl2hxmS/jcXeWviqEsVLeU8pZYjuK2sV2JtGX+1LNFwsIzNqLx2+Ybh0zNtSXCbiopxQqinYO8qz6ROI+1S38mC0WaqiGLDklT0WTD8N/DnBmMcOW9dJZ7CFpoutd4IFtdlh3jQyoiKYByJJ5M7R1rlSl5PrhZOIKUPuBXYXdFyzC6+WAXaTy94iXT3syVPJySeT5ttVOs/niVQAT2rpA9Anim1et+WUdrMFRWulkWMAIti+0hfyejYg6rZggkkVz+0AF7XkFDZha788sm3ZmEe6Dja62KPclSLPaEExl/Wit1BgsRUWsvlxv9iR3PniawopLWf7ilMS1dlSemOZG/eE5ZOodk+8V7JN0Ox0qlwqqrEsO2vCOaKa7OKwtU/TY70zdoZiq8VmIiess5NaUYtrR+XZrBOjzsqveHM9c7mbtgbPbrgrmzXawpHyraZujViVNZ/EtlEVUERezSmL5I4XXNHXh7MwnUAwxPEq8Xo37cqeUovCMUqYeUrmQhfXkWDqsTQ+cxFWJk3YJkwee/wqnG70spovUNdoLX+LspVUF5K8pCjiXBfbQm+1bnxo29BNF8v8WMae7/hOOdKxEchRitsKcmPXOUPMz5S62m/8nY4RdctvYJtLLxZi4GYby2e7ajNOnXmTcay9FtBRsZdSfXSil5fjpuPwwD+xM5vVFds7KHh/YBwurY+Gic6IQtZTQdocjqtLyHfKKrIBK6W78CBpVcjPvU0+N00zYHSvMUq1lmITF5fnMlwd17PzHM4SmO01+DU9rSJwnc1OgoETfJSsG8KxhdNUmkcbxxDH+lrbrlo08CniIDVixx3KHRc44DrHgVXq+xWOkaWC+tNFPkl2pz4TxiLbBp5ilSJYchcC71hqXhsp4Y6WOcg8bRscztuzKksFEc/dfJ/SeqXmqwqbBQaQDsmCnvmKWOhLfL8S3I1jCpWb7Zv9SmMj3JsawaRJRqsLEcu6ZrMbS1mRgOf13qe3Dda67CKeauyMDpnx9IqD2LrskmZv7SaqcsjyEYGuD+RhlGYKMOwqoE9hLO7zdibASU3v8bTy5/ypQS/qonDK3qtCLy4pRarjcb4KzInBbJaNKl59Q2m42QQiYItr6azZn3HjEDj0ZrKZtNvliSQ2mwNNkBeZT49GoEbzoyptiG7Gu9EIAiE2ev4kEHnDdMzWN5nTId9mtLjbJVf1eiZq9XSNVvoadkyFm/MooQfqWsCpDmbGoK4jOGN69Vn17J2DEyVH2keC5UAz2ieXVDhuVt2F6Qy9gihd7wJ67lL1zsSUSTIalxvrbARFfw7k6hoZyrmoOR8om9je8pEqzgC9NMkzL5vc0SgPB9PyT2p1rKocFKl2inOyFHdxGhzhbLzTwZXhWK2Udk5MTQjz0lfCCdhMvRMEVtqJqFOORy251jOguBG/l1Vspcc0718Xgni+zo0utrtQ7CQdnI3mbFc45eq9W65FuzNGE2cu5p4z2850WvXrCj+wpiqEKK5RV57sJvg2vVBEDDKUNWQnlsrIW1ZzUXZXBTgtD9us2E9Lf8SwdrBPDgcVLdjzaK0sVx6NQzxiTim2ZUUZEldgdtKQ5DGdaaazYrmrVMFI8JZysjZ2e67YXLPrNiwnfc6PKEGy1+68wjxMmZ1C+ZSgE73us7JOTuisQPftwinPKFiv1/XJ2RpeVo2LqkvlWQSBeLI8W1D60bHiJIETlCm53JujdRvpWnztY9xfN0AeTbBLw3n0lu3YED/6m/haxWHJMslMiUeVWZCeJdBkpC3P+Wqj1/nIb8ders5QN5wQ2MIb1avw5DBn/uI2vZQfCN31Wj9DLdPryQVoa+vod3i2VKiTI3tzRzlKIy3W9JWC5tNFyMvsuapRir8kBN/u+S12dkqvsTLYlI+3hBbJ28Brlc0SX/AsBgL5XKphO5djTwFdeMqm1awvr+WYZTD9dPAWzoxveFweLYmgwng4gI4O3jplz1ueobLDJsJcT1SpUJuRiyucQRxYWmeC23RYbq99MvL3NTkv203q0sp8QZs1yqmnZrMAwUEGuig0IidMMkoujmAjrVYMr2JNtLjU1MrXZDf0NA1dcBIVjthCzPA5JWIgFdB5CrKFbVq7BnUzJzieYWBcxnm+Bi3bByzVbbQpcOW0BLsjxp46v13KjqagiZW7bqOQ9HmRrWF3lmqJT6KTUT+JQSjGk0urLV16Rde5HOp0tz7VcS/P5Eyeu4tSG40Zng+X47Si4RSullZqhownwrIVM6V8OaDTI4N2gWHFvDRhq5qdqylfTKfzYjx2Rv6pVjqR8FY40c0DarzvjXIbXEWcWawYZh2DMsMNcskEdk2ikTX21+RhS8/UUJiPlnt/fbykZKh2l2MvNIopEUKG+bt8o+ioW6Hd/OruQlIJ3KTwva27qXf2LlBJRZ8szlbBanxqaX44nwV6sM+FdurMGEsaCStgjuQR2bUcRYlclXdA4HbLvKJG5YxkRuvttje30fjK73spMupLpeiZoC/0eWpQ+0037i7BCZ9o1ZXO3dWk7rRzGVNTLOTTAwaH28OeQuemT3eSfSkr0x2LMJyqrNS3V2Wypi4zYne1xj27EzrOlUtz5PN7gDLKvF0crIvr1UeVYAxOgH2lZ065pZwftRFmnUcoO+1dcDkeVhNR8oFzKjN+B4ixF+w4+rzaXizvSqtBcrzi8z3lULCB2sWHKOj40qnY8Lwut2d2HGA+d2GPQX52dgsXtyXsKOx4SvNry3K95VLbYt4FjuL8aYyHHFWz0wzXpm0EUWaPrjW1WHeB6btOv0+v5QJX0drCp3ug5qHro5csxEo6FTyMYUjseugSbKJbaLdzhbSnRXRh9g7m+u72sp0eLtgBztprLVuBdjJm9uUkT+Jl6Nsef17OtlfTbht7tDx0tc8bZx7Gam5eRu3ZEGhqTLZTFhOEVsYS9rBGaTLnOFGqrp5L7LEsRZNrYF8xee8280m4OLdm7tb8ouYjTCLXObs47khJKktfSPeVSxRa0dS0Sa3kph6NqwKMNQjQIofdWAEHp3V3DLf0mJ0HE38RHg74Uh/324u2YNnVgRO4gxnI1/VCjeQzU0wpxc4KjDqHinLhuiohnKkcnQCerTBHY0KgVPkEHSf4niZF1D+ysNiloz25HonHqbOQilHToqfwqox95ySaY1rapwvemGEeavaaHc3McXPpt6y9mMDG/OqtUfeanY8YTJTBZl1JmH+9OATsuLm4aXPOu5y3s0u04ovTfqhVXc1UGX1dqG5ZFApdWGfmmuFEFkCgW0QX7te7hGXZvz89P92e8z29Tmmcfn4aTpIf58H/m3PK4BoVbw+CY5KcPj/93x2b3Y+w3h8c3c6Hge293ri//nVhf3t+Kt0ICnY/4aySJnicmP3DQeGXf/UQc6DS359eDs+7uvr9gL22g9tZa5R5TVWX/VuVJ83tpBVav6mGv2aohj94ceH7003JtBiOuW8Pa+H7IM7w5xNQ9uHpJLxie5fBCMOJ32CEtzxLbho9HlUMZ4bDs4qnP/4/8vjE+GQlAAA= -->
