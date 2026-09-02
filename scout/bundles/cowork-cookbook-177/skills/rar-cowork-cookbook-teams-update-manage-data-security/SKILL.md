---
name: "rar-cowork-cookbook-teams-update-manage-data-security"
description: "Drafts a Teams channel post on manage data security status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_manage_data_security", "rar_sha256": "e06fb55f5be5f8488822c2ea9944713a26f31d55a64d1623c0b7f3a9336ce299", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_manage_data_security_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-manage-data-security:64cc616ddc5b993d5b122ac03b571ec5bc54eee5077430b561bf37f2407ca39b", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_manage_data_security`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_manage_data_security_agent.py` is
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

Manage data security Teams Channel Update — Drafts a Teams channel post on manage data security status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-manage-data-security
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_manage_data_security_agent.py` and embedded as the fenced Python below (sha256 e06fb55f5be5f848…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_manage_data_security_agent.py` first:

```bash
python3 teams_update_manage_data_security_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_manage_data_security_agent.py   # or on stdin
python3 teams_update_manage_data_security_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage data security Teams Channel Update — Drafts a Teams channel post on manage data security status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-manage-data-security
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_manage_data_security',
    "version": '2.0.0',
    "display_name": 'Manage data security Teams Channel Update',
    "description": 'Drafts a Teams channel post on manage data security status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-manage-data-security',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-manage-data-security',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9681baadfe006e8d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-access-and-security/manage-data-security'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/teams-update-manage-data-security', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateManageDataSecurity(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateManageDataSecurity'
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
    print(TeamsUpdateManageDataSecurity().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/715eXOrxrbvV+H5/pHkytvMIHzqVD0kIQGSAIEQSNmnHGYQ8yzIy3d/jWR779zkDKl69XDZZuhe8/qt1d2/PlltE+bV0+uT5lkZtLGSJAq9CrIyF1rmfV7F4F8e2+AXcvKsqSK7bfKqfnp+cr3aqaKiifIMTF9Vlt/UkAUdPSutISe0ssxLoCKvGyjPoNTKrMCDXKuxoNpz2ipqBqhurKatoT5qQsAQirLGqyyniToPYl2ruN8srcqF/LyCyjZyYggIAOi8APbezUqLxKufXn/+x/NTBO6fXn99chKrBq+e7lLoBeDn7e+sV4Cz9s4YzE6sLADDigFon4HnwqsAkxS8cj0fen/6sfYS/xn67/+Oe6sK6p9ev2bQ+/X1afpR2wxqQg9qcqtuPBdyrMKyowSweIHYpLeGGqq8pq2yyTA1kD0LXh4zv1HKC+jv07cfH0xeAq/58etTDkSwJtN+ffoJAtp/fara6f5lolL8+NNLkvde9eNP3+jUrX31nGYiBqR+eXt/ficLBn4bGvl3rn8HVB9OtL2vT98pN10PuSc9wcynl2seZT8+CBdV3nmZlTnejz/9M7JO6DlxEtXNf0T35wfh0LNcoNO74D893438D2j2rtAnzX/OtgBu/SuagOEf7J6hd0P9M9p3+/8P0kmUefWnxf+U3J9NmP0d+vmf6vavJjxD/tenlZeAxKgsO/FeoV/fNIVb/vyD++3lD//4DZD+t2S0vK2cO4U3kJyR79XN29vPP9T31z/84+cf2gLEGkijt7ZK/ozmn9n1zud3Fnwf9ePv5wL+ehZneZ9Bn5EO/ZoX/6v67QU6WUnkfntfv0Lf58t0zaBJiQ+mDxN8lzM1kPU7O/709BsAiAxo0zr3zyDL/+u/oH3kVHmd+w2kOXnbQMDBTZR6k/DHMKqh43tS/6Jthd3uJXV/gcDbKd0BRFht0kCbyooAxFX55PFJg9yHfvnfzh02vzjvsAk3ExS9tXcsenvg4NuEg28fOPjLC3QMAd+8ioIosxJIZRUFAsOyZuJ4j426Tb90E1MgUPQAHXUpTIBTt4n3N+iXf8vl7U7wpRgmNb5mwC8WcJYLNV5a5JVVRckAWRNO2UPjfQHoCrCkypPEtgDsTn/a4mWyjRF62bvFHADa3g3QbzwoyR0guR8BRH4GTq/zBIB3M9mxjqMkgdyoAkbKq+FeWoCtXydiv/zyi23V4dfsAcQ49CgpNQwGfAoMfflSVJ6fREHYfM08J8yhH3797Qfo/0D/atad+MRDARXhbjAQzAkkarIEgcxsUzCshqawALBz99yvvz08MUmXgRoI8inyI+8+GVD7FgaTBg/3fPgG6DyJ6FXvnH5vN6gPgV2gqAHWAjleP3/NJhI5GFr1Ue19GPEx+WH6D2c/+Ew+qd9tCPzkV3l6H3uPwMmZTl65L5DgQ5+WAuoCv95LcjgVYdcrvMz1MmcAM63mmwuzvIFqkDe1PzxDbQ1UnSj/YgPSk3FSAE5W8wu0XyqgzuUJ+DMZ6M4ezM6zaHL8e7Q+XgMi1Q8gxhYfJF4gyQPWhAqrsoqwsmrvPs63HhEB6tvHfEDcgjKvh6aC7k0+umf0PfL2f9ZDPNqN5Xu78aj40NcWQ1AC+v/bk0wispuNym3YI7eCOOmonh/xNDVOk3qPXmviMk2+J8e3juEDXD5g92uWRMAH1fC3x0j/HkKPMQ8oaysQHyqr3ulPyVzd6UYNCITJs1U1Ba/1NfvA92dgCuCGeoIqkK/xlP35J8Pp64ekIUjK6flbrYceMTbFPoheqGjtJHIg3/Pce6A3YTWl0bvhQVR4U0qBuHfC32kFAerA44D+5IEIeAfUgLvpJJAOoD96xPbn8GjqoIAUbusAaUG+eC+QMYUvCMEasj3QBk1jgBV+uJOCUg/YGIj4aeE6tIqHMFMz+y6gNfkiT6dY+c4D7x9BKE6FBPD7zDNA1Zri5GvWAyeANLo9PPsp57uvgLDpFPP3Sb9397uu0PeF6G9TrgEZv2E96L+nGv6dcQBAVyB4J8AA1TWuQTan3nsAgUi4l+uXR8V9lPRPWV7/0MH/+Nea/HsN1X/vuVcobJqifoXhR537KHMvTp7CIEaiwqsfJe/Loxh9eaTZl8l8Xz7S7HeEH3Z6hf6acL8j8R7VrxD6grwg06dd5HhT2L5fwBbLL4vzF2L6+jVTvW9Ofo+ECcYAtNrDZzX5GAJKSlB5wTT4UV3qqSj1oA7eQe1eHT4D4T1NJqwJplJY59+l76TT5NaH1z7BF3zKJlh3pxbusbpJJvFr7+k1a5Pk+SmzUu8/WNVM+ApCFRhjWguBtAEdURN596fP7mh6+P3a7Z5QAAnc/HXKK1DLQCf7DH02pc/QxzLhvvDKWrBO+nlqiCeWYCj49zn2c2Foe09gXdYMxST4Y+0z9WHv/fEfhZjSCUjseFO1zj/zc+L4ByLgJgi86o9E5PuNlbyDBADzqQKCwvue2jWQ0wUN0zMEXAdSDmQRCM8WTPgjG8Cn8gDCA5Sd1P1mv29q5Q9dfruboXksIH99+gCL6f7RADzCBkz4z7u0yaYf1fVtomxN8++91N3E9w70DagXTVX0u0/B1BK8PcLw6RVAjff8NBkSFKkkGu/r5aeHOECPb70roABA40s9dQUwyCJACdTqYtIhBoD3HYPpdeTex083r3/e8P6r7H+lCMehUMp1HdJmGNwlbRTDLAfBbZJGPfDSIQnP80iEpgkcsUkKtX2c9jECoR0LZ2wgxeTJ1HqXAkYnHwD5Pw3917vwpwcBUC4wkgIUPITybZL0Sdsj/Tkxn88xzME8i2EIgkZxC6N8HHVJ0qIIF6Uw3EFs2sctBscpx8MYZqL33gY+pHr7aLk/vPJAgTcAnGk0yYxZljN3aJRwGdoCRIDmuOOhGOrSuIeQDO7P5x4B5n9OfffM5LiH4lPQgg4Q9F/dxOfXd09PgUgRYCRP1AL7uJYwc7Jog7bV0GYqyjtfTFiwI72kPMIwTYMp5ZrADgtp01yLda5XNScNIodKjhrIlu5WGzlcMWxGi3zXZt6G3+5PYssE602pSTcxJfewX+G8zC9zMWC4XeqUJ24b1UXFVaWeuPb8VIlX9ZRZZJZtQ8Vfh+GJaDzfv60VDZS8SlzM1FbM1vuL0bdq5CDRuTLUk4FvqpI2Dq27IAu9vJyUYhO5kr7uxvAoWoUhFlq3TVAnwko9lmR5UbpK1mCOT9eMYpIczs/mnblmqDXRnc7R/rJUT8jOQN2q5ysNMdLW0RbnAQ1jpqedbTzrlqfoJMvzAjH3xTAjDLuVtItVXoJDgequlWiOuaZ6b5uMiSmeM/0Utc5pIXrJKVkwi6WJ6k1SslfFKSWx3IrUhVyU1ZaRWpVSJNn1tapNaP2S24lTz3VL1KMzMGfM8N6a5lOd5vQyRpLyONuEoiZlYetE5l5vhta1dx6iu6xTxQlmqOTKmp2xW596WBqYNKENjFi3dXZo1sezQiHHjJcbLTS2NGMNXGq4xm1TjdKo8dsAvsTrKMdWtisdLLQkE0InoyGtZ2l0pNMeW6s1XEo7UdsvKK+YEQd3Uwrx7WDkaHNWdPhkzHyRyUZPPl7jRXnB7SZBK8Y5lCRGn3mbvp2vSphEi8TNaEO7XOWdNUbcEhFOYmjJg2qi7U0Ku4ToDU/CjYu+ZUXHiUHWK/vbJQlPzmzfnulbNkbUib36FyZc9jhRO8doza/pcrM5F/RxHftVB+IjOZ/QU0jS0qUP6mM3kPtxY20iabmuK3m7TxuQa6Rk6qI0mLujWPKUU2Ai2W5x3kK6Xvd7c9XLPGEoe2WLHkN1XSrzlUzepA4uZrPQ2V8jUifRqvM5BMOJ/OxdKL0tryBuY21wjfK0bC1+t+HtdVhzTnC+lZcYTvjKL+ZyuHSqi+b3wEE7TcWHItsbmThmRSgYBzxdV6c9q3FJzh1WsprwOrlx9EiVbtIgJGzR1tzpujBZLdkJecFjzuZ6lsXNHE7UdI3A29M47o63qyJtyF2vygbDkQKWzx37rMELTFxu/DgyAKqmmKpZuG4rq8VMarYIS/Z4FcLonLMDOiTyEYMxTEXLoSP3RcS4+rk9wSuS6YS07NPMOR/3Z7Ja0hEqBSIr+pGZtfy1KK+5zszXzBpLN8BAyxsWDbGWEpvllXUvVY7u3BlNL3NpnuCOwMsVr2YjDCDvuD1XYx8ide9j5nZnZQCF9h4cI83SLSMtqjHWFlF95jA46WzVqD1dT+rsgOat0TinZRKZ4hA4zGok4lLs1nFbcaSjBReYis3rCc0vB1gOdiqplhdOQQVGYK0TZ4g6hRuMOieycWGd9XjuCFgs6DUWJcjl4tHYhqNU/RyjN7ZxvUt8q0xZz8uwkY67baeJ/ZjyPd1wTs0fyKvhgVirJC/b4MpNKObkQZ7HCF7A5mWvB2FA76t9uxevBJsr6PpqIlHK6JXRud5phRGzDrP966LkyaPPEjivuKtAU7Ow5k3DUldEv7qKCNcww8IprIhytDlhS7S8yDb5PlbdOV1YobCi5bFWTbxv6j5O3VTUrmRtjuiwOebluXfgjZdeR3sM112wsFY960rboyvE2ey6u2qnrDaFIeYWyVbtVaHHDsbVZhvEsHWH3NQEazfbrdAeBgmg1Na2OfsynkA6CNoyVjs+tbZqo4Guguqz7pp1rsGtdzy90nfcuiFXYuvSZoiuUyfNik1bUzM/IzG4W/VZ7C3kW1rlbYcyepjx5Lo9pnPMC1lJVfVKSbssPN7OrNswI70k5rpwnNO2ovBzVyviDqWkdUZ1ir4gCn+90/Jh6PxT2GuHpX+OXeFc4HG5p2pBVE5DedlTB5DOzI1D4yGqjs5iLUsnp2PVxc2JUrCaKMxFQxNBGWfUpdj5hRzY5PGQzPj54YjrRrK/OK4Oor3O0EuKpSsa6Gxu65QGPp9TTdwsrpdj6i6trba9jY5y6T3VqYV5UW636Sbv+XLFt0VytINCzkt03aihNxiNciBciWG5gk1y3aVtU94nO8QuRtY1ziNZ5dHtujiNSum3WqlLu9P2yrtla54Ma3aD3aNnjGJ2WSNqoK8lbb0dtttbXTC7JU1HfsSqG+vagfpAzvYLS9ub/kA4iCen3aIWrhcp5WEOP2wEvT9t62rDbwpmG3TaQifKrK2OJ4lb13JRwUViJ0mwSNgkLLepsJ/3W8flqODsmg6q2/NOM4LhonUlFVZpKKyDtm9mHM722NIhqky4iEhmDXMlNdaHKijd4Fx4p8wor5cAPW2CdBcq7Om4utmXpttjsCmW+0ZUhMsGD8WRlYWN6TYXqo91UFWSNFS3i+18rI8KV4z+MeyO8S6M6XODWsMsNaI5cjyaO61ezehT5nLnjMYFZiP0kTtH843pwJoH3ziKQ8MhLubqmZEpJxE6HdVB2pvWUh9Dwx7LA49khZNg4dIgF6O6u0R4KxplcQ6igjXy2WV9wlRBPnSY36xCGN9jiTIekmKRBXP/qMDpwhY4ilpke8Sp18fNmT2ZEo0WuWwgZKajsaHqhqTwHVhZUV4H+whLIKiV9FW0uh43XS5xjtwjt0Ly6FvT1f5xZ5FSW9DOyKS7eExUCpsR6K3fSXtD4GD5lrgkFyx3i9uCDWxXWTkW2iYZO2IhEkpBauSxx+VtdkP9+Nwg68gQ+FqyVidJnumlg7B8MXMFbZbrJ44vqeS4mHuUttCyU8QQVIFzVTKUV7tCh9K5oMyQnRfBsJmv8d2mxy0VlHt3ryLbfMnueHzJFm67zQVnPkrHYhiD9Srtt5fl3t0aS5cLUB8Vu/iybxsq44txXzXEat5aR2Q9J3pFxGRvWTc6Jh1o4kah6umWzPOL1trBfL4zY3IRcqFspnlAGYdwf2XLcCijTpRNwSqdWEo9C7lqM2xfoKctJu+Vfqvw6HKI6UuyJpVm4wTiqdPMy/VcdtuNeEqZITXT3XJnz7E8m1HcqN/wIK53h+OMXlHqSAzVDbVZa3Q8ZcUbx5qiglo/y0QtBRQcx8naynhLbmNkOBncAKoA422LDF/Z1nUPS4ja79o62kekttfStbA/Bj7hBec953iOXJpR4FZbNS/Aco5IRRC9zurSa6WMj2NVynsKT+GjJUvL1artYnPOH08yndmrbF1Q7HZV8eUujwsxsG8n+7xQAokUF3Wwialjcl6tBBfTt2MxM+ytSFDCYYgO9KBsdQpA68CmM1W66rJqIPmxkxl9n0iboclXO+6iz7wtTYXIKpeUQQyDnW+kYx4qc5foyJ2uLZT9THE7h+RrjbK3/aDn/pFfjIXKDQl707tUKJXdeZPc9j15qToTZs/jPOKVAvMCiWKZCMbnVSjiVWZbiLheGhYXMs5QIuJtMJ0brYs+zah2s5sZSzau6YUwPx5mabBjlHE/bHdtrOMXk5L7rjTbuJKtfbjSaEtTZEKSnNJGliJ/OK83vb+JroMTnA7VDfS4bK3vsWMwzpxSa7qOBGlNyOV+MWeXSFuX+K5hXdOnZbYINVDPuKuSXdB6Ix6pXrDP+FZZc07R2Oe9tTn31olUI/MCGpUZbnLmwaM3FJuVPXXKIt11XV9P9n20VPOoIgoZg6tse8yumitjKy68Dp2bLUC9rQYFjRSe7l1ZUVusQnCdWNsD7Rp1esQ9YNRTBp9bpnRx9mbukvFyvJyxRW1XqVSfuHDT4kqInMnj0tJpda+0K82m97NFToK0pbOulQvWawmrwi/lfAyX24i7StlSJA7ZwYSxGahGgkXINgCplJkZ6AFH1bnaB+dw1Qn42MnBcApMVDTXoLzCLlE6xvI66/cYU7nN1p3ljXr25EoG/iR2w6I6Xgl6lWkLvLYdu9o713FOwjBAfZg13aFaabOSgaPdjEmUi8eQIz0LLTeeYYmU8BcLY920lK/9nlnTt13eyWwqZstmnTHLNclxLEnOBFq2zuxalvHd8oD0cFCHVyedH3jBj8fZLvc23sWsytN8REwWu1b7zLvmc37FWzdrS2bLXCc6H955hBrClLFoQ5YaVwolC9nIA1OWrKTtZtTZ1pS5ulJcd1Ejkdria+Ww9ROw7F/Njt2JIRPrMJzO23NmybpiuExDbFbCIu9IZN0jtKdyzYq2mtvYVLBkwQbMEMxBuOi8iSFev+I0VTGvlG+y80bEbHzcH8+u16I9cY7IgMVAU17DBsrAYoRTYWu2++UOg3V97ku4ZPK0L4hNEOf9HnaoLO05cSaUmB7cFghyjnw1QurufF1TN1g0j64jsAc/rVc3hidy+pxIXlWQhBn4Rc+HKRc7s7V4rdim4giSBgs11Q9Wya7jWtf32Lm+Wxq91kQblNaHA4zmCFi7h+Um90GyaCvjyO9o/rgxFzfO4Tbn3Z67HhreSY1VQPSYcN5m48yPBRQ1cEGFx3k5Y5HcrwUftBpYk3o0RXOHpk/wmhR3c9MZN8sbxbrJrL+kV7jVl45YJYhPrAd5B5usS7tVbKe+23KMs+Q3sh2cj/CqXlwXiHJdnRBCcEA/yS8v5sroAFLOiIakaL6tgiW/7O3dtQIN6Qk/UCSKX5nhUlQdj9F61KOrDs2rkNrkGSJ1CxbjPXa96A82E+a8f84cS2D3FT9fetc5JRmDwt+oFSbW6awk4eOyh6W8me9dItiEuI0vglakB/ziww5sX3wU1/pZa6F0E4FK18o+rRFOtppFzcqeNYTTNrgLg5qKbCULsduOv55GHvi93tkpg8EqPU9oWFsK/tDlvO0tcUaIFWHDJ3wqiHm/lq4nYDoym/nOcVky4eZaGF1rAWPTQ3cLqXUhiIFe7IjW78abGa+5jLEdbzFQ+GqU7NY0vEo622BFIhQrq0UsbutfyIPArOSRYhcgJxebdWrn8ciMESKgktQBf15OUgcyeYeRCAKfonqRa8nZPMDkilQyh/VW4dxfS74RKr4oz3uHZRtHON5ci+32hIMJZTYG7SXTV/J1f7gkMcFJSTvyxUHPussS4V0zZYlhWIkM7l4Cfw4fGiXYd9HhkLU3dDcKR4t0F0jHpOt2brNrw6SVUwZiWGWd+ax1kK0hGfw6i66zk7A+wnGRyO3MxZR66fjXrOe3SxsEBeXNuIOA4KbAHmtmsY9mQqujfKx7ln+jx6XMV1QoHyjb3VC4bG5E9zhSq76gWl3EtweWfXp+uh/dPr2iCIWSz0/TMcD7Zv5f2gsOxqh4eyeF0zj2/PT/bqPysWn4cdB339r3LPf1zv31L0j5j+enyomARI/t4zppg/fNyf+xGfvl3+4QT9OHx+HzdCJ5az4OQhoruO9gR5nb1k01vNV50t73r4GlQT+VeXX99n6M8HRXKy2mM4nv1QCPlptGWQQYVG9N/vbY2p/e3497U8+Nvj0G77v+z0/uADwXOfUbTpFvAConhd8Pnqbd2+nk6em3/wvnn6wsUicAAA== -->
