---
name: "rar-cowork-cookbook-scheduled-brief-track-project-expenses"
description: "Schedulable morning-brief email summarizing track project expenses for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_track_project_expenses", "rar_sha256": "361cf831759605a496cee6d7a3badb675f54b7b5b6d4fafd24f433c588460862", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_track_project_expenses`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_track_project_expenses_agent.py` and in the RCI capsule.

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

Track project expenses Scheduled Email Brief — Schedulable morning-brief email summarizing track project expenses for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-track-project-expenses
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
      "description": "The process to automate.",
      "type": "string"
    },
    "trigger": {
      "description": "Optional. What starts it \u2014 schedule, event or manual.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_track_project_expenses_agent.py` and embedded as the fenced Python below (sha256 361cf831759605a4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_track_project_expenses_agent.py` first:

```bash
python3 scheduled_brief_track_project_expenses_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_track_project_expenses_agent.py   # or on stdin
python3 scheduled_brief_track_project_expenses_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Track project expenses Scheduled Email Brief — Schedulable morning-brief email summarizing track project expenses for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-track-project-expenses
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_track_project_expenses',
    "version": '2.0.0',
    "display_name": 'Track project expenses Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing track project expenses for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
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
        "upstream_slug": 'scheduled-brief-track-project-expenses',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-track-project-expenses',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd7fcf107e421f4a6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-delivery/track-project-expenses'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/scheduled-brief-track-project-expenses', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ScheduledBriefTrackProjectExpenses(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefTrackProjectExpenses'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'The process to automate.', 'type': 'string'}, 'trigger': {'description': 'Optional. What starts it — schedule, event or manual.', 'type': 'string'}},
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
    print(ScheduledBriefTrackProjectExpenses().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6+ZOi2Jb/v8Lk/FDVQ1WCsteLFzGKiqKiAoLQ1VHNctk3WWTpb//v34uaWd2v+828npiIsSojBc49+/mccy/5y4vV1EFevnx5UYCVIYKVJGEASsTKXITP27yM4a88tuEP4uRZXYZ2U+dl9fLpxQWVU4ZFHebZuNwJgNsklp0AJM3LLMz8z3YZAg8BqRUmSNWkqVWGA7yP1KXlxEhR5hFwagR0BcgqUCFeXiJ1AJASVEWeVeHIKm8zUP4NgbJCPwMuUudI2WSIC1n2CKRvAYiT/hWqAzorLRJQvXz58adPLyH8/vLllxcnsarqu3rAnY86qaMCx4f85VM8ZJFYmQ9pix66JIPXBSihTim85UI7nlcfK5B4n5D/+I+4tUq/+uHL1wx5fr6+jP9kqN9oRp1bVQ1VdqzCssMkrPtXZJa0Vl9BC+umzCrEQiro0cx/faz8zikvkL+Pzz4+hLz6oP749SWHKlijv7++/DAa//UF+gJ+fx25FB9/eE3yFpQff/jOp2rsu48hM6j167fn9ZMtJPxOGnp3qX+HXB+RtcHXl98YN34eeo92wpUvr1EeZh8fjGEwbyCzMgd8/OGfsYUhcOIkrOp/ie+PD8YBsFxo01PxHz7dnfwTgj4Neuf5z8UWMKx/xRJI/ibuE/J01D/jfff/P7BOwgwm85vH/5Tdny1A/478+E9t+68WfEK8ry8LkIQ3mB2wZr4gv3xTjkv+xw/u95sffvoVsv5v2Sh5Uzp3Dt9SKws9UNXfvv34obrf/vDTjx+aAuYasNJvTZn8Gc8/8+tdzu88+KT6+Pu1UP45izNY8sh7piO/5MW/lb++IpqVhO73+9UX5Lf1Mn5QZDTiTejDBb+pmQrq+hs//vDyK0SJDFrTOPfHsMr//d+RfeiUeZV7NaI4eVOPYFOHKRiVV4OwQuD/B0RBvz4Q6kH3BLNR49xDfv5P546dn50ndmLVG/58u4PitzsEfnuu+vYGgT+/IirknpehH2ZWgsiz4/FrZvkgq0fJBURGUN4gpth9DT5DNPo8fkHCDPn5XxPw7c7rteh/viN8+EAqmd+MKFXB5a+jpXoAsqddDmwKoANOA8UkuQN18kIIsp9GkM6TG0S50StVHCYJ4oYllJWX/Z039NyXkdnPP/9sW1XwNXvAKoE8ukaFQYJ3dZDPn6FxXhL6Qf01A06QIx9++fUD8v+Q/2rVnfko4whB/hkXqKGoHCQE1lmTQjIYMhhkCCL3uPzy69PFkA1sLAiMYuiF4LEY5mkM3Dd/K+vZ5ylFIzaAfoY+Tou8rMfuFdavyMZD3vWFQsdHI5oHeVXDXgV97YLM6SFXC5rz7sksr5EKJmPl9Z+QpgJ3qT/bpXVXMYUFb9U/I3v+CHtHnrz1upEILs6zELr/PRse9yGT8kOFzN9YvCLSmJlIYZVWEZTWU4ZnPeICe8bbcsjcQjLQfs3GVglGV93L5OEeSAQ94zxD+nmMOWz/sINnbvUm+05jjR1OvXe68ivMsEcJWOUYCge2BCjUb0J3bAx/e6ZUFeRN4t79Bx4N/xkF9xmVew6qfz4jvPdxZHkfK+7tHPnaTPEJifzfziCj1jNBkJfCTF0ukKWkysbDm+PgNHr9MWvBQeApBlbO9+HgDVreEPZrloQwNcr+bw/KewyeNA/UakqojDyT7/xhAkBvjnzv+TnmW1mOmW19zd6g/BMM+R23YIhgMccPW94Ejk/fNA1gxY7X39v6PZ6lO5Y2zEGkaOwE5ocHgGuPjqyDcqyxZyBgsoKx3togdILfWYVA7jAnIH8EKhHCqoHevbtOyqGZMDBemaffycNxWIJauI0DtYWTKXhFdFgmYwQqWJtw4hlpoBc+3FkhKYA+hiq+e7gKrOKhzDjMPhW0xljkKcze30bg+fB7Yt91GdWHXC3XqqEv2xFuXdA9Ivuu5zNWUNl0LMX7ot+H+2kr8tue87ev2V3Hd4SHFf5I3+/OQWBlpdUdUkeAqiDIpOA9Tx+d+fXRXB/d+12XL3+Y4D/+tSH/3i7Pv4/cFySo66L6gmGPFvfW4V4hPGAwR8ICVN+73aP8Pt+L7fOz2D6/FdvvuD+c9QX5axr+jsUztb8gk1f8FR8f7UIHjLn7/ECH8J/nxmdyfPo1k8H3SD/TYYRYWNR2/95v3khg0/FL4I/Ej/5TjW2rhZ3yDrgwFl+z92x41grE88wfm2WV/6aG740XxvYRuve+AB9lNZTtjiObD8YtTTKqX4GXL1mTJJ9eMisF/+pWZmwAMGmhR8ZdEPQ8HIPqENyv3kei8eL3u7h7aUFMcPMvY4V9Qsbx9RPyPol+Qt72BvctV9bAzdGP4xQ8ioSk8Nc77fsW0QYvcEdW98Wo/WPDMw5fz6H4j0qMhQU1dsDY1PP3Sh0l/oEJ/OL7oPwjk8P9i5U84aKqrbFFh/Vbkb+l6CcExg8WH6wnCJMNXPBHMVBOCa4N7IXuaO53/303K3/Y8uvdDfVj1/jLyxtsPGPwnBAhOazPz9XYDTGYq1AgvH5kFXz2P5wdn1wg3MGpBbIh6InjscSEoTgapyySox0AaJexCNtybZqhPIq0GZuyaZf0LM+dkh5JEA7FsiSNs/QU8ntk6Lex8YejZlPLcliHmZAux1iQHYHbhAMm04nLEACnOMJjWUBCJ70vjSFWPs19mDf68n2MHd3ytPqXF5smIeWarDazx4fHOM3CSMaWgh1K4Nj8jGGtndZlPKFvc3PY5e6tLgLgq8Y+dnFdFsI8wVWLqa7h9hzZjZEvUVlEW5XYeYtlIibFRMKrY4ALC5szIHQtfOx2SwUnkFdxBybDllpqZuNpkrHh7EIpNE0/7tnpNmV3iXHbla6yQrc73Qo1FMN0Ys/v1FOe1tdz7UJEL6L+CnvgrdZqm14N7WW4rIPt5LAzr9Ky1LtEudZisosbzZvMqH15dY2kFvrjtQ5OlHwgl1TClq52qcgqi7Ftc8uSCep6TMjGdYcCdVWhXMSetuE+2U+vab+0xUa6XvSBpep8O4hmr50u3KzDcJuqTbO2ejCNcSGuaQ5fSISQ5AbwfD+pJ+VpIq2TKZYPK6XFJd3qGuMmkD6YWRRj8hBS+glfJymVnshCv5aqlWyX3ZRySLm+HuX84ApTn+AWbsOer+dqz4iC2RROv9h65Dq1V1GubulLnwiDYfOzwGzBucgVSmtEOmeOEpHFS1FymDic+r5AVrp8TsFUbI9lEGlmXR+7OCvly3Tgqj1IqXOp7zribEzNtVOeE92wqOuCxDkzlvzrdAFTd2NNhElMqeeO66xCrErM7GNDKs9kZLWXiLxA/OT5enNm0qoQVGsScoOklRSbHI4o62w3KbktJjZXE6VKRtqQ4G1D4K3hEnF6HfZEyDnl0dCXxvRaU8Y+Uonttq+m5rWh852Slup+dW2zLltw0zAclgEQoksQDAnYYI4nOr0msoGC48zeUbrJcUPa2sEwbSuLd+kNM7la5u3imlVk01YkqZuXzs3MrBFCideq1JmKW2lXL9Js4vbZRO3jicaTFSfxN5FDT22MRnMv9LL2dsuBXBJ6ul0O3LGLIuPGrDhMOu4XAVVkJYb60ck8hq6y9niz1Bshq/QilPubxWhpaGQMb9jaUC/3pNVtvcTHK302kEm1YZtJFe1Jk+Kv7rzrr97eOK6mehEs9dNUX5SXveToNbn3d3vV3MSikCrhxgvNeLsO92Gvd3Etr9TdtbgOh9QhHVUeSPribPPucCQ8kJ48guMpccqfxaZXu12c8gptgmjhpIp3NYZ5Ciiu0AO3TQzzRsyAdAiyjcDddtgNmznJetd12JXVWkXgjImj0x16OJ3behOuLroo4e7GLIZ9p2rVbrezdEYkAmkgFt2U0PAtkC2s9VH63NWCkgCTbPiTey4DQSQBO5nV8i1uMH9lEia1RT0snMiuqrmgxvthhdogBplAD4V7RKnkJDOKtdf0ljdvwmR3nMWqddOG63TtyKJ+o8XFbiik9rQh49NECChuna1EObvaJ9qhYgW1Yi/cui5hRKuIoXNxlwhxdMI2UXPaXTTtxNw4v/EG+rTKBGK35rmaXxViWbaR7p2LKMBiR66mzWYOK3TYqVrgULleAHpyVlFiCLWN2u9Kztmt1SJqnBud2BIaLYkjJ1B7TgZRjB8p8swKxuUUm0l9cRfLAzufNHxkiMxq1dDmhCEtUsZ11gMe4WN6lLbtjPLI2XkdKKfzvM5MnJfnrCl2CV0YHCWe3SQobmLk7luB469FsKAi8XIDszakgMh7R4FrecshzEw8XGgUeG1oNvm5j8AF3cVFyOF8fAK8ac74zeI4WTVZz/ezhJ0t9U3XrHnVj+eKFUqGEjFOQWpc7u5P2X7m9+mS0Ou9u4VCk6tMRpnKs46+8vmyPNUsvjPT1QbN5ucmm1FOs7FOUnq56NbCnOZHc+rowGIxpb3KmStZQ9lx3mVBUV4ch63N7ydqVDI5J4pyKnnCZFsN05PDKzgtzTPjwrBxq5+JE+k0LXte8WvKpOvK9TBgolc1QtHbsRA8NF50Ib05eFmW0KS5mEX+6jAR+RNVr6uS35Kr7U2LipJnFw4ZzG2eTGmh3TS+ZuzY0wlfhUe7DoVMvKrUadWvZOmEl84xOFzmpBpFFSt27ZFOJQv0ZzpWN2ll74/O5jbHDnk27715DjRfMhqaELWlQBiZjQeC6VXn9hqKkjKnlRVQj7U5WEx4O2TlmfKWid5OvTSMJ7sqnJFq4E63N3e1Ps10NBXcLqmTQ7NNN1uWllnYgSXpiPEr67hPaIiq0ulm05aiqIq99qjNeRn02jYV+i52KYE5EntmuVY2uOUVA6sapoLDVEjmnR5C7HVFK0uInSbvQ9SXmhXLe0LA66VK6Lx6VubzBXuOBqXWCdjQdyfWoz0dC41K2AvzWZHshUlgrxbb+LaYX/NzGR5DSozbIuHRdCvAucbf8sziTKqOujBELKyUINanhr1rOdFY8dE2mc6SiLpNk9Z2ZDsfusRYm7MivcXoAEeZSVer+NxQrkYl3fhTg1WKgg4krsk7WhHXWyHCd3Njhu0ZgVgcSxuoMyl0quktFgkuFWnOmKZX3dZ4KcRwTi+UjZq50dY8HUIeDiYoqAx0w2u83deqhG52IJMPam9fXcuCGdpF200keyrZn6Rs18Tmri22zgbLV2FLwy34QhMlwVfwpDcSvfNz6cQJjluI2NRBY081kmIe+Rym5g4jlPOWYaJs2Tns4iQ0M+XCscT1OnMnYqnVmnw50+ZhfbvdMvRUY4azaOMSTPzSjzJ7k+F+eLidKUpKQwHvprqXwammJlg077l0EbpWitn+lDTV+Y2z/JXCXRVMl/nloM3mbWzUR9XztDDOfAwPnEIKBKcIjssUHJkpm6/NfJvWvgpLGN9rahntOgcNKMUJN/0Vvx6uzGElDzc7mZ7O+TGXdWk2aaW+OBVXomsuVtKF61ZYGwt+yeAWijfzqzSXDhNOPmuboIwjKvKVilidhQNqaIXTmW0UDIYWB0KTSvNDo1hHOrv0y/Qy5VQ8ZpntTpljZRhxgbrfq72jlbSWHP0eVa2pdplLkmX2gTmLlR0xUOE8TvcXIQnNqRqcefp6sCgjFtYbunFjLlSEc5L75VI7y4vYUv1osWOFg4nJBnArJeMOZzlro27qXszofL3lmkKLqNLZh00JsX64mS6a7NkVWuBic0Jp3p1NONPNydpY2I1bhjtV1Et+t9X1iXu0xVoZrHW0d3OadlU0kKMg8/rCkq4EsSm3bcKmM3uAE1loh7jsTQWDv6kkP2+zkNvQBdjOx1lKSTb1NTIShxJbieBXpz4AnCvDDA5R4SY3rj8bSipCFwXVzKmUZKykLPb5oQIJUQbFhgdWQ89Edn6z93y8nNRsbjZRx28SdaNROLbeTpasu7RMeZOzwzU7lBeLbVdNrJCT6Cw3Oxbb+NqyVLvTlT7pg7DbZYHS127bzIb91d5XmbWTSgyOXWcbWOdla3fHoScJ1KGWTdjudZAueJ1qpOVWiPP1VmPz2mtvlpgutgsXW5ELAcQnjjtkuKj7B+E2lBuS4lme8S7RJleGmX+0p6rcHTYUwdY4T0w5Z9IK+vmkuz6cW3BXbVdQ5dSUasLa7mLW3QNeTzwyNltVIbdbSS0YnYqv2sxUDUMNfEfgr/1+v0J3UngTDG0r2JsuPxcTyjwAKvDyHMaxy2cLfI5dif7il4eodjl7ttpvT/n1vDfZRlED/qJvElqYn0kt8w87PY38NFnwDMR4LdYGlLF6AV2gWyanwWGTUHSQRUoyCTyJ3ud8ITpbk4PDDq+57RbOSShsJYv9apqsr5jib322ZG9qvY3JzKZLXSKayXE1rFwgZih7iK4M7A0utsOcdQIOFzB3i5zU59VtQ8nncFkzLsXJg3voTLlZ+ThzKHJ3yBe7WNWlBqUpGqxourxWdnrrj+S+MMI9wZNlIsgrD9uxC9aMN3BQDcp9MUUJ2l9Pr1jeGvtuIMg1HQzmsCQTSb0ErSR6jAzWUpZzeShhumYPgXuFTXo9BH11O+CLqrrgMSeRO050mQO+ptFsyWIQiLBKO/ZzMNdMC4OTCZmC04RjyiybeBfrsK7yIysmIjN35UVKnBTUznIjFF2tHg7ylinIGMtFRsw7KfB6a5PYm4WqFkMrwK64OW7PxLxeFcOaqoacIrQm1aZMQlaLlS/1011N5OZRbhfMbKo0ZntdNJcJ0ftrft9tgSkoYqJxa3AmuzrtFW4d76bs4jKZY9DK24G98nll3ChA8OsOuFF97lfo9bbPFGFbzs8yGiYDl3o2mPtwG7mT3cjhBDxouRVFS4ueW6NNOmgYZ2BMEHblIZiiraL7StjPcRSLzsy6zo7DfGqEjFQS02AVLRXX14lV6pbM9JKQQKgvEt8zLRtaC5IJTRR1u4aAwhQ4G8waAgTLujt7IaXkCukbmRF68gHHb0aUUC22zfILuvR5adBFGo2cs8Qq+U1jWbYlJdxYdEMY7D2+6uiZToRYs5gdZim2yg46kKRuka8HZb+y5DMqukQgLwguZziCQQ97Mqrx9dU/FGaZM8xmSh03UR4u5rZ/bvhqh3ct2MqLqu6uuwXakqftRJ/sldvAJtA1cuSo2I5xJdtYEAx+VghBBWqd+Z087Olj4gQhnPkaY9aKZ7MNb57MBARZVQtWmlQpqqbMZIL3q27jnCig6ha5YpfGocPNbd/NONSdblq9vG53WIKjxPRUHXJsUrfmaRfk9QFNbCpl5vnmBjQmJtQLGtVTbhVc13NMvixwp+FOB1aISJmabRe5ADuU71IV17vCfDVDu4g1LyaFn2LqKE45MVlK6tGyiLVI7Ztu0ixn7IbxyNXKp9BKGDC9FXZ2nbWlu3VpdrPzBmG7wDzWOSQGSwZg4s1KoWTS6Q2zFhJ6PR8burArzLthoV36wNkeBgbz8hvW8vLQ61xPOF16K/qu4IvKZ9pAXs4o0oJVy+xvmBZZkuwavrHWJkNCtJoHh5xjO5FmrBBvjtqEdfbHRZuHaam1HLGuUpjkjWgwNDsJGzNLtzCsrLHZnDtYJDNh7WbtbHE2jzzY8bAPZ+tsnsu0yd9ORLyvVdvwbJix3OJIWdelvhSjA73GG1Ash2hGuoeILK8WuzCpjooXxmZZBltndzGW1C1I5OTinVM8k8I96STnWDgm1tTH06OS5ZE1JHQSVeQQlnRVYgmzWWHgeBadVQa2zoqLpnnXhdalrI/JxmlrhjH8vsOMPmZJwZAioJ2VJjvJ2ynckpmOFRxKr6rnFMa1jVz4w24GwAxT1Hyq3Xa93+GX0+VUzQ+XvudvaHhq4lZhBhUVKls8cIOW7Y2gYBpuXZbVoSDY+VDqhWtdt6fZ7OXTy3gg/TxW/osvkMczvv+1o8bHqeDbq6b7kTKw3C93WV/+qmI/fXopnRCq9TharZLGfx5B/sPB6ud/7TXFyKN/vJ8d34519dt5fG35418bvYSZ21R12X+r8qS5H/B+erGbavyrh+rb8yD75W5gWoyn4v9g0OPR3Zg6H+m9cKQKs/HFD3BDqwbPS/957Pzpxe1h1OD+4RtBU99AWYxGP19/jOe04/uPl1//P9Vc577dJQAA -->
