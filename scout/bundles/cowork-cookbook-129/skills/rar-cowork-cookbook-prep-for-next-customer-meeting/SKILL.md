---
name: "rar-cowork-cookbook-prep-for-next-customer-meeting"
description: "Walk into your next call already knowing the account cold - no scramble through CRM tabs and email."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/prep_for_next_customer_meeting", "rar_sha256": "39769fdbab6ded7312db55e5d89a3b4fc099a6b7154a77bc691ce95e9c9d6e96", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "beginner", "integration", "dynamics_365_sales"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/prep_for_next_customer_meeting`. The original RAPP
agent is preserved byte-for-byte in `prep_for_next_customer_meeting_agent.py` and in the RCI capsule.

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

Prep for my next customer meeting — Walk into your next call already knowing the account cold - no scramble through CRM tabs and email.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/prep-for-next-customer-meeting
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `prep_for_next_customer_meeting_agent.py` and embedded as the fenced Python below (sha256 39769fdbab6ded73…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `prep_for_next_customer_meeting_agent.py` first:

```bash
python3 prep_for_next_customer_meeting_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 prep_for_next_customer_meeting_agent.py   # or on stdin
python3 prep_for_next_customer_meeting_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Prep for my next customer meeting — Walk into your next call already knowing the account cold - no scramble through CRM tabs and email.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/prep-for-next-customer-meeting
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/prep_for_next_customer_meeting',
    "version": '2.0.0',
    "display_name": 'Prep for my next customer meeting',
    "description": 'Walk into your next call already knowing the account cold - no scramble through CRM tabs and email.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'prospect_to_quote', 'beginner', 'integration', 'dynamics_365_sales'],
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
        "upstream_slug": 'prep-for-next-customer-meeting',
        "upstream_url": 'https://coworkcookbook.com/recipes/prep-for-next-customer-meeting',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2438ecf80198b98a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'beginner', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-sales', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/manage-customer-relationships/maintain-contacts-and-accounts'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/prep-for-next-customer-meeting', 'uses_skills': {'custom': [], 'ootb': ['Word', 'Email', 'Calendar Management', 'Meetings'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class PrepForNextCustomerMeeting(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PrepForNextCustomerMeeting'
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
    print(PrepForNextCustomerMeeting().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/716+deiSNLuv8J9vx+6+7OqQFapOXPORUFQERUUhK451SzJIvsmS9/+32+i1lvdMz3zzZxzz7UWRTIjI56IeCIy8dc3u23CvHr7/KYBO0NEO0miEFSInXnIKu/yKoZveezAf4ibZ00VOW2TV/XbhzcP1G4VFU2UZ3C6YScxEmVNjgx5WyEZ6BvEhdIQO6mA7Q1InOVdlAVIEwLEdt28zeCAPPGQj0iWI1CUnToJgLervA1CZKXukcZ26ocmILWj5BNcE/R2WiSgfvv8898+vEXw89vnX9/cxK7hV2/HChTrvFLg2qu2bvIUVHsAGrgqnJrY8O3zWzFAezN4XYDKz6sUfuUBH3ld/ViDxP+A/Pd/x51dBfVPn79kyOv15W36o7bZw4Imt+sGeNDEwnaiJGqGTwiXdPZQIxVo2iqDiiM1hCsLPj1nfpeUF8hfp3s/Phf5FIDmxy9vOVTBnsD88vYTkldwvaqdPn+apBQ//vQpyTtQ/fjTdzl169yA20zCoNafvr6uX2LhwO9DI/+x6l+h1KfbHPDl7XfGTa+n3pOdcObbp1seZT8+BRdVfgeZnbngx5/+mVg3BG6cRHXzb8n9+Sk4hJEBbXop/tOHB8h/Q2Yvg95l/vNlC+jW/8QSOPzbch+QF1D/TPYD/78TnUQZqN8R/1NxfzZh9lfk539q27+a8AHxv7zxIInuMDpgfnxGfv2qHYXVzz9437/84W+/QdH/oxgNJqb7kPA1tbPIB3Xz9evPP9SPr3/4288/tAWMNWCnX9sq+TOZf4brY50/IPga9eMf58L1L9nEARnyHunIr3nxv6rfPiG6nUTe9+/rz8jv82V6zZDJiG+LPiH4Xc7UUNff4fjT22+QHTJoTes+bsMs/6//QvaRW+V17jeIBvmnQaCDmygFk/LnMKoR+HfK7QpAXOtoYqPnOBj/k4cnjXMf+eV/uw9i/Oi+iBEtIO98hfTxdWK9r+6Ler6mT+755RNyhlLzKgqizE4QlTsev2R2ACABwhXh5BpUd8glztCAj1DMx+kD5FLkl38t+OtDxqdi+OVBktGTmdTVZmKluk3Ap8kyIwTZyw4XMjzogdtC8UkO2RnxI0imH6DFdZ7cJ/KFCtVxBGnbiypocl4ND9kQqc+TsF9++cWx6/BL9qRRAnmWgBqFA97VQT5+hIr7SRSEzZcMuGGO/PDrbz8g/wf5V7Mewqc1jpDMX36AGm61g4LAvGpTOAy6CDoVksbDD7/+9oIWislgzYJei/wIPCfDuIyB9w1nTeI+4hSNOACiCbFNi7yaIESi5hOy8ZF3feGi062JvcO8bhAPFCDzQOYOUKoNzXlHMssbpIbBV/vDB6StwWPVX5zKfqiYwgS3m1+Q/eoIa0WewP8mNR+D4OQ8iyD871Hw/B4KqX6okeU3EZ8QZYpEpLAruwgr+7WGbz/9AmvEt+lQuA1Lbvclm0oimKB6pMUTHjgIIuO+XPpx8jmsvCnkAK/+tvZjjD1VtPOjslVfsvoV8nY1ucKFJQAuGrSRNxWCv7xCqg7zFtbwCT+o6STp5QXv5ZVHDE6FGYHII+nw6gxeoYy8Qhn50uLYnET+P3QRkz6cKKqCyJ0FHhGUs2o+cZr6mwnPZ0sES/pD5UdOfC/z30jiG1d+yZIIOr0a/vIc+UD3NebJP20FwVA59SEfuhZaPcl9RN5kXVVNMWt/yb6R8gfozAcDQfBhmsIwnqLn24LT3W+ahjAXp+vvBfrhqcqb7IXRhRStk0DP+wB4ju3GEy5T9rzQhmEIpkzqwsgN/2AVAqVDb0P5CFQigvkAifsBnZJDM6ED/CpPvw+PprYHauG1LtQWNpDgE2LABJiCoIZZB3uXaQxE4YeHKOh3iDFU8R3hOrSLpzJTz/lS0J58kacwLn/vgdfN7yH70GVSH0q1PbuBWHYTgXqgf3r2Xc+Xr6Cy6ZRkzzD6g7tftiK/rx5/+ZI9dHzn7Ckkp8L7O3AQmDPpM84m6qkhfaTgFUAwEh419tOzTD7r8Lsun/+h0f7xP+vFH4Xv8kfPfUbCpinqzyj6LFbfatUnmPgojJGoAPWjbj0KzpRnH7/l5MdXTv5B6hOkz8h/ptkfRLxC+jMy/4R9wqZbcuSCKWZfLwjE6uPS/EhOd79kKvju4VcYTKSZDLBQvleQb0NgGQkqEEyDnxWlngpRB2vfg0KhD75k71HwyhHI0Fkwlb86/13uPkop9OnTZe9MD29lDVzbm5quAEybkWRSvwZvn7M2ST68ZXYK/qdNyETlMEghEtO+BSYMbGCaCDyu3puZ6eLvNldTKkEO8PLPU0Z9QKbG8wPy3kN+QL519Y9NUtbCbc3PU/86LQmHwrf3se87Nwe8wT1UMxST1s+tytQ2vdrZf1RiSiSosQum8py/Z+a04j8IgR+CAFT/KOTw+GAnL3qoG3sqtlHzLalrqKcHW5cPCPQbTLapZthZayd/sgxcpwJlC6uaN5n7Hb/vZuVPW357wNA893u/vn2jiZcPXr0dHA7z8WM91TUUxihcEF4/owne+w+7vtdsSGuw74DTCZahWR+ysEN7wGOIOe45FAUob8HahEP6LsayNu0wc4q0GcZxaXbuApYCrMt6NGBpKO8ZkV+n0h1NGuG27S5cZk56LGPTLiAwh3DBHJ9D8QCjWMJfLAAJwXmfGkNOfJn5NGvC8L0BneB4Wfvrm0OTcKRE1hvu+VqhrG7ThOz04XU20r65uS3yrabGWzwrMemSRdGOyfLYu81GI54LJM1tzThsl8YyYup9XyrbgzQsj6nml94dLEUjZjTb8KOLttm1xB1n5GRBjbWsJgIGdFGOyvlldExGzwsiTA1FSfNqIXCbzaKez2ZGlrFJdU263lCrtVeWBXpRwXrTXRvAU7cE1+kCAkXOg+O+uVzw3WqXbXCL1qNDeaeUCBPC9K5XvF8zh421H0f9tnUpYV63EREMhysxUAd5MYC0WuCoOfOV65pFJWZpxJadY1yzJc3RLpPUyprzxSnt9bLXFQvjjwtVr4nkbJ1svi6sdTWCu3866/2WOeCZKezOqW0aB6cm7w4ftVrfX8NNdXYHgDVSaQRFrrDZcClpQbkdRVxvVJtOdnp5q1dlE95kzrudTFaZ93f6MCv1lF0PbrOv10Vc1kxRLfcLh92urLRL1C0zMJtizwWNvaNAuRaGBj/qolXcl0AN4vnYaqO94pRjOL+623jsr4clc7jb1bXZtod4IZbNIrL5LGzUiIpYIuN5unQu8tJYt6VJHY7MZZXvKtNrFlhYGA5xS5S1NE90Q4lRQk/Cu9qMpVJxxj6cAepC7rDwFgF3sc/mzJJOzYYYi0PjNyR1We6ATM2dsGXm24VaUgNtXs8z11AIMi37+q4vLtlmV9ZdMOYNTeerIgb21VoWUk12BlBnYcol1o3ZXVl8VQ6m6O+ku74v7fqCMuItIXdXhkvxWF75yTkCp4C+W6dynB9zc39f9KxirBxzKNiDHG/lvbxnFu3YnPHlUgh39Pq4u4cFfyfSZC2NsVSMGVGwuUvOVqjjsIdCXhxExjz6N4AK7E3qqj0mhbSPLleiP1bMzPdJZjmY1xw95Ky8yIID5bS77TyxfHWbbuWOdXLDpkrXOPp5q+RhdBP3ZzfDY9YhjiEYeA29nmC1S9b0DsukTeJS54W0tHb1Hgvjkq+u+61rNOSe23ZnaxNvRaDVgl9b8U6KJA0/6ep61Tv6fVeleoGdMz6yW1/UnE4Xi/mCqhYDb9BdJVRBtNHduFONrbe4XmTUE7dc6sdhxi/mY1m2K2a7uaGb3YCvSGMsQp/2O96u5YO8UyqsWegXQ0RJIz3OKfVU3Oqj3mJalZcifxa9Or2Zdrkr5lw47hbbFrLTAd/fT9t6pZcoFl43t8P24qaOGibhnCznslATnGOe7E6z1tT9boqiRQNtlFHatdfk5qjPaf8sC8S80g9joTpzo2KoVhTwIFGDgrHbcwjZuN8KQ95bjTiPN7Dp7eXlvMXlMhcuu3F/Wco58E966FnbAQJ5lXvJbwuJEQx5dpOYZFhsNY1U6dbyI0kS/DWhYyJlVllvHOUTFXRj11X2KVRPViKvaA0b6/12cSPkfRVtrAzuHbHYDERT3IKBMra+7pjhRh7kuHVRto17yC2epqSEFTnZ4uaKRnnaeUcWaFKp4uvRFK3zejz3fHqr5a7CtetZrcTMI64h5R5SyUP7uSn1J8AtDszdDzqBLFdrel5jNQfZ77YVDi21Eu7ULrq5q5Zy1CJNqNNNkJIwMShrOcg3ZtOz6Jngtzeb31NXB0gZzq71OrqQeVOZwTjXLWZpbxSFC0OLk7xGdYo9QDkfhCCpe0KOFv0gFMJS9DZ+jxnE2Tm1fa4euCW5bJtSbLexaZ/KJlfBLT3vO3cTrzc3Z1+7uNqf4xyMXXY9Z+3dEJRdPE8vdiRf8UDSByXjC00vc3ZzPoC73GDMcaQG9KhpqlsyZ8G4AvQ8VNv9cfB2jY6fF7tlvNvyGXmmFubCJqWr4866kyh2/cwfxuWwdY5OSKCLWqIt99hyi8t9CMuNN6WEV2vc6moK3s4Ub2O69GxB4HfzS5GeT2vT6Aa1OazyZCWZQhph5p5dHnhxcE4dpazEBtCbcrvFY1sjyjEXaZcENF/VW9xS7J19yHQuXqX1TIGuxK6ok15cgTxyRLsLxPjqwlKX8cHdEvWmJuP4RhMWj40gZ07Z8V4WMwzI5Uq7cMqGdhxxxotjiY+ptzbyMzjsUhLzxSjDN5eBEzhCprXGWksamdKps2eucw6DXQubj/fOnmGoOpa1hJGnPpUlBdS4jzPru8CN8xkVacyFuYB2PQIyRrP7vre3jdQZ9qHx8HK2j8TZsdpexPkonA5tc2zUtciR2tJkRAk2dOSc2/B790jctIhIhHQkOSk/RQmv5yEm77Q6MeRQa6SZnKb8aibI+CXfWptovZExRQ8Fa+MvSSU86/dVOvIWyKILYdGltrRvnsYe40slnk98eMCFmpxfTiPRHamsndM5TMIgOqj1RrxaQn3fu3gbYvU6HGm3cDqRGEA24/fntdsGd4qUMGpFOodjZeL1XcMjoFllqedmSCSNl5mFoOBkFnepILe9HRE2YH0z56yjozWG6F/w47nNtqo8yqp4NfeomoQXPmPDW5hS6FUxIjYBJxfT5mazWalRr8tCkA5xpEpGeKoOXJB4rLliJIFIUEZNtmEaLP1zhRJLWMp9zyNs67Bb9UMQLPURKNfyhta4pfOeruur63lJ0ajvn3WGsZo2BflCFFtO8YoUlYTlwMvZ0bCH81myrJlnXwfCH+leynv3XOlEZTGZZvEFGZucptNEdk1uW07bxbxZLnH8ZtdGV6cdmq6ooeL2peod48K9j/UsL6zbIN67khP8PFgligzmgy3BwNic5jwXoNuL2ZJSSJikeKFj/X5hdyQVNerl0FTXXWUFd9dMuRW/uXYEusNiMp9ZLl9Eh9TVyaKMR3qEZbzdbfb+4nQzqPV1tZOU0NAEm84wjqaU7UxoZ6d4oInSENLM1J3TkXIvfj5afcBkuragmnK4OLwXZCWqWIJIduNamy9zqhUWTRCtI63ZEtug9lbojMxb9MJh2vKqlx4/DPgAy38051dQNyVSdoHQKQV5LuYDL+3HqiWW1TmjVH2V9YFKe9muMSI/rRPbiVsA1nWXtEphKWzCmsJQXDb3k0AJSmW5idPVmd5w7tHy6wPsQ+O7tRy95KJQhH1C84Q/LbQRHNoE2/Za1B+Y+Ixdz/dqz0oRutBPY9COjpDrXW0mh10XJnxPjqfcdVQ6nB8dHFvXmLW7JHeTrs2rKbq81wWXOWag+rBlB7NvWW4HlDPGZldeyO2NzMly6GmYsj1Jgy6flseTYlvdJcDhfijn7huHFsp0WDQldujjZZLwUTZfK+uAEotsjd7Ghk66nVDcvKRqlyeLxlXOKreyOUowCgaWtLhsHOsQyzleaaJ0c1ciNkOFqoOO9c8l3hq3u+jc5LZYrY/ZOdBXe3WzPC/0HaXtbhqNG9sslbY3ZkA7cY9uzJFi74GYcDILGKA3mmKvcbwR1VOYhvyCuPNcD3BIV025vlf01psFnXLdifKh0w714risBvS2ul/SlCaXaww7RNtAxM50THUq3ILI8rmgjLKuLifzVAcMz5l7/oIJQK6XIHT1rOzkNa+k5GXH3TylYh1RDq7MLuA8lfW2xxXbBeShr4rutIP7HqEtls4tonCep1hx5efS5RqISkzHpbGflaahLTb9rt61V085DoZyPQa+nmUFRfHZ9ZLoW1+i9/kq3LqDRc97l9Zdc3fAlsaRTua1TGEHvVUAC+ZXos0Y3WoORAIUp7Pnh6S/NhC7biapjX5EtbYfDnLgVv3oHkjMYGtHpIdOXJVaKDVd2hyUi3zI8LOeSWp1ZMUr19e1Rg6U5vD5kFWlVzSDhRp0KMgHtTw5ArPBdzLKuKejsV/mIrGJKtlCb9aGZ65eciXlJsQxhk7GLXu+a7Pq5GOoxtCYuBxt+mgsbz5l6PisLef19mahlkFk5hI3eBq7CotI4q5goQRHC5L0nZHHEQ2XC63shKpB0Z5Hj+cBv969etZWNqpu2sK/quvyHkjbPCDJ6Nh73iqsxqEyq9hoS2blY6t5jJmtCje5Amw2l4WKUeTtkEiwB9ozOR6R1G1hqJjHU8420VsKl/b9RrYLbXRp8Yy5nKKLi2V38IA/pHdwqRehHFWxeklNHVWvCbuwB3Jfq+qKvXMz9Ij2tsLO52vTktb07NJwzaJtZ1hF7RYdkXoFr1yDfIOeFj093Js711mrQ5K3PcwJuLsENeuJM8oIUePsRP6s9j1yMHVCJXzuDDP1bHUYjd5MRmqy4whwM2KWBc2Yqz7iFNNgs70jEc3dGV0FbtjW8zGgLnO6J4QxnHl9SwwrBwb8gj8QIBQaXPNrN7z0Xr4/G5qvzkbybt4SakQ31/w8EwJOGSu+p0Rm75DJGlRFT6mBX3TSTd6Y1GK3jowVHt5Yopb6OKtL2LFFvutZ/YLke63WfW0FNuaVBZFENTR7HmcKyYZszpcnLW7uMwa/y6dFfYhWe7mINrmMER3YqXzd9OX6xs66WC+b1rwdb1TCrgv15h7ZBMfsec/cqybWCPsMzk12V9VxTx+TOpxdGNAqR7CFQEX3jYl2To8bs5lAi14VW9WyxSO3DflQcjD3jMoXps8pqQ9zZqG455SVVvr1bNwBwJXekOfp0atOq0uEOfKtKo12TZxoaiftMpDSBlOHiY3tFY3JmG3n8fGGlZzutA0kbpO3tHJB7z7RnPNuk0vD3p9rw1Es19KSPR4LLp/RFq21i8txk+AHSCBSyNsEqENJ6u+4v1Jm9tabZyzhzgC9WO/cG5D5o8f6h8Zc5KF7Y3NjA0uq7ZdXgSiKU4sV13pGNSED9/hp4KS05OcoOgwd0Ruw1LjbxtPmbGzy/ZoIxXSzrOAOMFMJU6Kq8eLedgXbi7cire5COVsyHUp2CocJMSlf5gvjeGTJKhJvWpcQUm7c99hsZzPMiYgYR6kZYshZso3WvH4M0Nw1btDMZeBtT4HcnOYuMEFIwB1pA/cGK4q/g3km4wSxO6q3Ug3UpOZzPwrZ7FYuj2o3O0ZRW51iP86AeThxhgObBm8nNPuNS2zoatihBl6IlmB1zG7L7f1dc18WnJvcLTCX+FGW1D5bX4kzYazxTpmhOKeR8mF2IWXq1izDW4zdr/R141OFRRgsv2PYbHceAzvAle21FwpDbXtGsHSfLpblkdmuqIQYUT0KYZvnthx14l3KyBw8CDdn7eoGy8OIUeqdjDqyGIZzf64U371FNIkz6QG2LsSB6Qfxqi/ACY290F1RQc5x3F/fPrxNB8+v4+N/85HvdKb3/+xo8XkK+O0R0uPoGNje58dan/9dhf724a1yI6jO8+i0TtrgddT4dwenH//1Y4dp7vB8gjo95eqbb+frjR1Mv/t5izIPTqmGr3WetI+D2w9vTltPv0Oov74OqN8eBqXFdNqdNyGonl/UBXCbr03+tWzzBkzzQBBNTynfpp8LNCB4HSB/ePMG6I/Irb8SNPW1tqefHEEDX48wprPX6RnG22//Fyh7KzJAJQAA -->
