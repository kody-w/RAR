---
name: "rar-cowork-cookbook-teams-update-identify-common-issues"
description: "Drafts a Teams channel post on identify common issues status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_identify_common_issues", "rar_sha256": "5151242d789b06fb90e47c4ea2cbae3ce66330bfc2061c86a78da1a824054fdc", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_identify_common_issues`. The original RAPP
agent is preserved byte-for-byte in `teams_update_identify_common_issues_agent.py` and in the RCI capsule.

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

Identify common issues Teams Channel Update — Drafts a Teams channel post on identify common issues status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-identify-common-issues
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_identify_common_issues_agent.py` and embedded as the fenced Python below (sha256 5151242d789b06fb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_identify_common_issues_agent.py` first:

```bash
python3 teams_update_identify_common_issues_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_identify_common_issues_agent.py   # or on stdin
python3 teams_update_identify_common_issues_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Identify common issues Teams Channel Update — Drafts a Teams channel post on identify common issues status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-identify-common-issues
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_identify_common_issues',
    "version": '2.0.1',
    "display_name": 'Identify common issues Teams Channel Update',
    "description": 'Drafts a Teams channel post on identify common issues status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-identify-common-issues',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-identify-common-issues',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '96e509eb4a1ede2a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/establish-a-knowledge-base/identify-common-issues'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/teams-update-identify-common-issues', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateIdentifyCommonIssues(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateIdentifyCommonIssues'
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
    print(TeamsUpdateIdentifyCommonIssues().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/716eZObyLbnV2Hq/WH3k11iR/jGjRhAC4tYJARCane4WZJN7Isk1NPffRJJVXa/7vvm9sTEyFEuAZlnP79zTlK/vbh9F5fNy5cXE7gFsnKzLIlBg7hFgAjlpWxO8Fd58uAP4pdF1yRe35VN+/LpJQCt3yRVl5QF3D5v3LBrERfZATdvET92iwJkSFW2HVIWSBKAokvCARLJ8/G6bXvQIm3ndn2LXJIuhiyRpOhA4/pdcgYIF7jV/YvgNgESlg1S94l/QqAIbgReoQDg6uZVBtqXLz//8uklgd9fvvz24mduC2+93OWwqsDtgPRkLtx5S3fWcH/mFhFcWA3QAgW8rkAD2eTwVgBC5Hn1sQVZ+An5z/88Xdwman/68rVAnp+vL+O/bV8gXQyQrnTbDgSI71aul2RJN7wiXHZxhxZpQNc3xWicFkpfRK+Pnd8plRXyz/HZxweT1wh0H7++lFAEdzTv15efEKj/15emH7+/jlSqjz+9ZuUFNB9/+k6n7b0U+N1IDEr9+u15/SQLF35fmoR3rv+EVB+O9MDXlx+UGz8PuUc94c6X17RMio8PwlVTnkHhFj74+NO/IuvHwD9lSdv9W3R/fhCOgRtAnZ6C//TpbuRfkMlToXea/5ptBd36dzSBy9/YfUKehvpXtO/2/y+ks6SAgfxm8b8k91cbJv9Efv6Xuv13Gz4h4deXOchgajSul4EvyG/fTGMh/Pwh+H7zwy+/Q9L/RzJm2Tf+ncK33C2SELTdt28/f2jvtz/88vOHvoKxBhPpW99kf0Xzr+x65/MHCz5XffzjXsjfKk5FeSmQ90hHfiur/9H8/orYbpYE3++3X5Af82X8TJBRiTemDxP8kDMtlPUHO/708juEiAJq0/v3xzDL/+M/EDXxm7Itww4x/bLvEOjgLsnBKPwuTloIU/fcbgC0a5tAwz7XwfgfPTxKXIbIr//Tv0PlZ/8JldNuBJ9v/R19vr1h37cH9n17YN+vr8gOki6bJEoKN0O2nGF8LSC0Fd3ItmpAC5ozBBRv6MBnCEWfxy8QIpFf/w3q3+6EXqvh1zuUJw+M2grSiE9tn4HXUcd9DIqnRj6EX3AFfg95ZKUPBQoTiK2foO5tmUEY7kZ7tKcky5AgaaDyZTPcaUObfRmJ/frrr57bxl+LB6ASyKM8tFO44F0c5PNnqFmYJVHcfS2AH5fIh99+/4D8L+S/23UnPvIwILY/PQIllE1dQ2CG9TlcBp0F3Qvh4+6R335/2heSKWA9g/5LwgQ8NsMIPYHgzdimyH3GKRrxADQyNHBelU0HURpJuldECpF3eSHT8dGI4/FY1gJQgQJa3x8gVReq827JouyQFoZhGw6fkL4Fd66/eo17FzGHqe52vyKqYMCqUWbwv1HM+yK4uSwSaP73UHjch0SaDy3Cv5F4RbQxJpHKbdwqbtwnj9B9+AVWi7ftkLiLFODytRgrJBhNdU+Qh3ngImgZ/+nSz6PP7yUaOrZ9431f4461bXevcc3Xon0Gv9uMrvBhMYBMoz4JxpLwj2dItXHZZ8HdflDSkdLTC8HTK/cYlP66M3i0EcKzjXjUceRrj6MYifz/7jVGMbnVartYcbvFHFlou+3hYb6xJRrN/OiiYM2/b76nyvc+4A1F3sD0a5ElMBaa4R+PlXejP9c8AKpvoI223PZOH3ocmm+kew/IMcCaZgxl92vxhtqfoDHuEAXVhdkLo3sMqjeG49M3SWOYouP19wp+dyBUG7ocBh1S9V4GAyIEIPDc0QZxMybV0/QwOsGYYJc48eM/aIVA6jAIIP27D6B/ILLfTaeVUE2YT2FT5t+XJ2NfBKUIeh9KC3tO8IrsYV6MsdHCZITNzbgGWuHDnRSSA2hjKOK7hdvYrR7CjG3qU0B39EWZj9HygweeD79H8l2WUXxI1YWxBW15GcE1ANeHZ9/lfPoKCpuPuXff9Ed3P3VFfiwv//ha3GV8x3OY0tlYmX8wDgIDEIbviKEjIrUQVXLwDCAYCfci/Pqoo49C/S7Llz/15h//Xvt+r4zWHz33BYm7rmq/TKePavZWzF5hGk1hjCQVaB+F7fOj9Hx+S7TPj0T7/Ei0P5B+WOoL8vfE+wOJZ1x/QbBX9BUdH60TH4yB+/xAawif+cNncnz6tdiC725+xsIIqNkAK+l7dXlbAktM1IBoXPyoNu1YpC6wLt7hFTria/EeCs9EGfEmGktjW/6QwPcyCx378Nt7FYCPig7yDsbW7DG3ZKP4LXj5UvRZ9umlcHPwb80rI9bDcIXmGOccmDqw1+kScL9673vGiz9OZvekgmgQlF/G3PqEjD3qJ+S93fyEvA0A96Gq6OEE9PPY6o4s4VL4633t+9jngRc4c3VDNYr+mGrGDuvZ+f5ZiDGloMQ+GOt3+Z6jI8c/EYFfogg0fyai37+42RMoIKCP1Tjp3tK7hXIGsLf5hEDnwbSDmQQBsocb/swG8mkARHmItKO63+33Xa3yocvvdzN0j9Hwt5c3wHj64NkGwuUwMz+3Y+GbwkCFDOH1I6Tgs/+bBvFJAqIc7E4gDQqjMJzEA2bGeigdeiwKSMYngYv7ngsIH9A0QaBe6OMojfkz2mVmgYu5M5xEKTIMfEjvEZt3NskoFkBDQLAY7gcEjVMUyWIM7rKBSzKuG6CzGYMyYQALwfetJwiRT10fuo2GfO9VR5s8Vf7txaNJuFIkW4l7fIQpa7vefupt4/WkySbXK0FvCKuyTnm7ttcnn04rfX0SdvyJordgoTCy7Jt2t3Ok4xrvFkf+XKaT6MyYE/qIg/1a0TLotmi+PkVesmsZfTK93ZYyv5CuoBLqMytKzaIxjvnyWrp4l13tNtMw12/yPajR68yhzcHq14RDzHY7tKcaZdgUyfq6lPbXzJ13MVsczczFlgGg91EvV0SemVVmTU61fMI2+6m+tLI6O+SZMqsJe1DcyhwoS9nS+o6aTY0bRYfnOcYoLQXOO2Kqbrdn7NLMLqZ+jpWh6cwM68C+w+xqLmeFtF+F6Fyb1QsNLBurkfRZhTpqNUzYaLsu9vkqljbYIrOzobSpISxuS6Z2ZEe1MxCD5Yr37ax2BU1cUUVTeWubl1zSqh3bmlu3wbRxmz6waXbw9CA0mz5jrGPZZH47s1zZSg6iop5YESwZMbeYhVWf0KzeTVbx1dSKrPcTR7Wy4Rx4a4BagPOZU0bkV2ai2j51mx+Vi8HOKvuQ5d5uYRk7qxdn3YKMKKy2lXgzbVZwd1oTUuYee/Pg1nM23+ZKetA6FOObfZM7sTwXM/nQ5kNI5ZuZuG1vddfwphpPQLUglROf9rIuK6mLReyOtRlqlu2NfuYL65ynj5gXdESj+dueGugDsSNBux+kpZ0cz0c2U8tjqsNY3PJdsjx4q1WYZ8t9f7N2FCDFbJddTss85s+TldoMy8FfZR6Gyel6ZUzk8uYrZNj6Wzw9pLeTbvppXB2oOOskEE1ComdoNyFse+kcJvmwn6mhyGySnTrnV7GA28USOPtOd9v8dqg0x7r/YCBs0/nGEYfAL0jdIL2MXM1JScTn2Z5CyyQTpzx1IAuHuZHT7W0tMboNAp8hKM3uJgoQutbq66Rt9JUsKw0cmPdbfrim+PXg8aKyV92Ykvjt6sJNJDfJG9kMLnOdNQQbG+Sp7jj8rag6ZS/csuWB0i1LVurY5xM4kSRVqabm+rrVBtWUCk7O+4Wdcs7GzNeHtkluCn9VRbHpAwhqEj0NavqoNdR1Wia+Qa9XIiXetpMdtMNhdhb28s00DrNcvBnaHh/0De62DJmsG6/N5novM+yUKU0NV0hXUGUjYUB+xm1nWbTnOEn5bneZzt1Brju5ni4XqW64ZX91V/RyI4eJU/RiWtVpabGzLTvHt/ZpbydWY1OzpeLZZm1sbdYZFoepo9DxVkMPtT4Nz9myUqvkbAim7PJh7sjr/uzgnaxM68GxOzo1k7NVDOyBKtLNojqsl9KiP82SzvSDJd1kXAnEXGBOohHRs4pbgWs3r6777ZJET9MFzRz5WJcL4oYntqDGdTXZCn6itnCKJPZUMWOKWz5X1wAoR8/n1om32zGwcoSOKARSfTIFht/3jTo7XJvCtaxNDic3zCl9MtzNW4VxRGWLKge8aGade3MqLL6wp9Y6ugkIr+cO3dmlyvURd7SxfCvGxhJgZ7e/7HD3ClCPnFrL0mDO00u7ZbdnbgJQpfUdyWG2fG4fJm2L8buEm5wXm2GKSc7k5K6pizrPLsRSSCOlvO5l+kYJmLU5DH5RVucw3pDxWqVVMxNvbet4qLbaorhIJeREc3K8MI3cWrZqFLNkFVwiK6SXbCeg4eqQKpi/LgVzKesKKlg7L+hrHNzOLXrgxEg298uj1VsXXcv38lpSw6PjRQlnkhmXxoaK23PzfFzZ0/hMGEYonG51bmC55dt7WCq0XRHO9LK9LWashLE5sUYZw2lQSqIOnOUfa3rdsD42UCe1IOQUeMaGFMmytorUQUlztt+CAafYNFicFttZt3foshUduiD9abapQL1lJTHRLnYHa1HADK0u2JsSl5fmKpBmJyqzbSHF/Drf6Sedzyesg1lD0t8O/BJd1b0TLSuptnc2vrUG3TyroN9wVS3lbTPjNzZYlDbO21R9Draudc2u7Cas17Gh3IxuGQbLlJrTA4+hKhYJlrvrQFIXGZNTt8ykrcyw9rc9Iw2qwywTpVLiiptofL+NCRnmIKneKj3TvWu5b7Fmi26UcmrzBTe0Ms5mcrECGaGiTLRu1KN/m20PVFQcG9twwkDOYzK7pq1GKIWFn2/JMbkc1bXBksdIOpumZnJe7So7Y2rSdHGImf0qMic2gUtbcu3zOZOLy2F7oQ117sS56aLGRNxyUlJxEXPE4WS9G/Y8e+GK604L8Lx2JZ4MrgXr1IS83u5Nweq26KVJVzR3WOS2HrerpgfJeuJk2nU47s7VJC7ySpqn+gXbLAhuuAgeWcIOQkYLdzYz8P18U0V1wB32kxpU1uq2bGYqq54X2aYsFblgi1kq5qwWnwLpKM51lb+RZ8ooYZbqezVbBcWybbezTSVGgXncZCd+ouOYupkMZrefmo2HHhyGsLarep8d5uwey4NE2lLeCaQLWIKAOXP20XQDmHhBL7B4OFWzDcnqtJpJZ4u1rEPu5IJ6iy2IEdaKMsxuvRPm6rDLE/zGn11sX2eJomg8v1vy2DEziVgydqxpn7301rmTk3qS7AV36dTphOw6i0jN3RGkp00PhprnLsAJDvP6oFGY7NmotbIIjFIW4bQQByyb6b6cyTSm8MRhVeHSxBAkOqid1FwRt3TtHSfhvjCZcEtfM1otFkPWTQhwFC6XlamtIhWOUZ4vRWWJbjnhdglTHbrVHs7LKCRTS9aSFcR0HTbN5xtKja5aLxLhXNuFdlUZMveEsKblwlx0hxKTlvXhXPMqYFZX92QLLO1eyyyW7XUWrEqnySwSY5g5F835k0E2/d7ms0tqplGgHnGFK5YaIYSqr2fSApjRDR0CtVR3q+ygyIIRVAMXWC0eYuL5VKldtzrz8rG38NMchpLBCKuDJ5v+tnG3J5Mj5EJT3F5QWOuWcQNPks65xBeOcOR7xRQKWVhGa7qcuLm6PVVmWl/xTX69xYmn3aQ+JfjUpqN03pBzQ6Z3bbYgKtbfWnwiDHKALxMXrRsq2WFu5x9bMmkr29FZhhisK1su5xpYrPuIMPuJWs8C8+JKhp9rt3Q1FNZi70prf69fg3BYmwnkTfcdiZLEfoGrs0UGlGHNpHVg5GG+lq67c5usLxQMyBiT1F20XYHLRl+0O1m017eN3p0k1Lpq7MGMtQEtONxf5Gk1m9H0PAEddSau6W4TXW4N7RMJTZ+KPj1p/qqpGUnpQMbUSbWYgzr1OJlOAWzzzHm4lXBy6Z70qbKUL1MIAhCOOfm4lWS0ZZpOXXrVAtdgY+sllTZbY9sBnR0U/iT510KgyKitC9+IFjcl38kybeEQGcO0zaayKZjNzUgJj9A3zaLPh1bNFBG9Xnza2qrVRsXWVOKmA84X5E7V926DMZd+uWs3FKvvyGXPGXsHEIUv61O/2O3jKtrcLq3W5PY+BqrhqDq2IiZTC5ADm0WcvNYvprFAjaoUpjv1piY5Uy6XuDUpWyXPmkq55Sm3QXv8lN76ueko+URZpK0qpAc9hViuc/oGNu/n/cZUVp58PZ4VW94TxAw9W75or4QZx6/ElS1iINJpjyk26KVyeWXhGNqNcfvCSBdJOldq9ZZeV8s63aJm0uSkpk5K2TtPhqNPM2e6EDxsx5fleSX4IAgJW5uhkcCXeFOyBh4xJUg7O1sdgXiDo5Yw1eaNVzqnc99NjCs/2XjphKnRm8843kD5eEftCNfh2SCfOj2bsMTy6swhOBHHw0o7e15i0LQmbLo6GEgKL4KydMyFGxSLC+4CrqUW58w7Q5A+KWwQafue2FLiqS/JRMHUS5Uk/gKE4rQrrsZ2qc90J7adfDZpugvhBBOeS5iFExThYhICrZkbNWhVQN0mnuKTvjbvuO2ZyRnX8ljNFS6TAA86Cr/Yp3mopCTBwRmJaJmN18z8KGU1djq52lPOOw3Mejehp9MlRD8T0DDZRIxKQSGzleKR+iWjY3RVKQaH4vJEcLZgJnC7XlytDXxlmpLE283E3Fv4krPgEN5e57AM8NRuRWmXRN9M5cJ3zFmLomfCZ6ii7Lae3g4B3acXXw/cxt6rpT0vbArMKuriSJqsrgPhkgzzM73YEjfYfcWRRc/sTr2uTuFlsoIzzfwYaw7TWh1XTQgiPCxnZ78OsJNrDs6G3urqDI48zIW6HP1olUyLjbPY4ZSUlaG3Peu7KqQYh2amjVhvRSWqaTzFuWMryIxqZJ0/h/nuGuf8kNUYzTjzOFmj3NxLUv3GenBCztdhLdG9fxALbVJX5BATrLMqQumYclFzsZiAEZPb4jiRk9UmvnIkcTDDXY422iHVmcO0qY+iKkYcR9xQBsS9sFxQYVEnfoCTEune8DQZJF8gMdzSzqtLdeNQMgzCWywTtaeFOjdDm5VzyWNBPE6dUzVt+AgFxiXlUZGOjKtc814xq6nzIYoiQ/W4hSW4MX4klSV3Pe0vGB9PwlbGHJOQ4GzD8iFvWjKxOF/3xAFHjYCFdXpPmt4QnDBa0f0qakEkHsMzftxM2YwrBPcaiBPZT5IpdhEB4VKrY0EwkeEoaSIuUU0wBoZTLsGcvGCBzoX8zZ2n/jnqxC69Ef5hxh5TwkH5mGtXOEnTB68IULkPA9Tpd5oRUABzT363YSauMrDiclcLRHIJhbOQcZddwSbSEhwc35UuUinOtDBVaWOfeOKVVg1ZrSe1DcdO2FtVGiprZCTGokewUa0wOOGFoT/1mBAjhiboaZZqh9lqBlaAwWFJiZkNfq0m5kx1nHU7TXuRWfKVrxG75kqzEaER+8OVugZnFEwlf4peEnG6puc4EZ2n5nY+8DG1vVlL9CAU1xqOhe1tutG1yNYxJ+Xdvgc9yzX0+WrMtB1ncJUwx8JQ3O2mUJfExajOS1HOKUzn0HWs611D6XA7Al7TOWy9gDPtRaNXWhNzm8tBNDeSSmhavs7Fcosf3HPVcQPthd3ZcNKmN3e6cd2X3J6vFixm9DN2c2U0JyZJo8Ur5iI5tHjaGLA/8KX5NXT5wiBVSapDjO/51Jrror6RrwVpaV2/E+sNSuEl5XI9iwv+MRTQnp22QjGdonCsOjqLMz8NmjrML1qToaI5xQf2loRRO0wpujNUcdvO05xdHM5LnFgkcbebKtaiNOriJu5cwwtvG5+ouotucLsmOWjiUUAVVVviC2u1KpzrnHdoE041hqST2DQiRLS0e5dkeJk23EgeaCw9hVM+d6WuO06UDce9fHoZj6Ofh8p/503xeMj3/+ys8XEs+PaK6X6gDNzgy53Xl78l1S+fXho/gTI9TlXbrI+eB5D/5Uz187/xbmIkMDxewY7vw67d2yF850bj3xG9JEXQt10zfGvLrL8f7H568fp2/JOG9tvzAPvlrlpejafhP6oyHpS7LfjWld/uL83f9t/fNOYgSB5rxsvoedj86SUYoKsSv/1G0NQ30FSjvs83HlBN/BV9xV5+/98Bo/rbpyUAAA== -->
