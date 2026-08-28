---
name: "rar-cowork-cookbook-wrap-up-projects-and-organize-related-work"
description: "Close out a project with a clean, shareable archive - not a scattered trail of files."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/wrap_up_projects_and_organize_related_work", "rar_sha256": "3345136cb1f9680638dbcd2159d9cd206ddd7e9c4f18cb06a7027e4d418f04ab", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "work_management", "beginner", "read_only"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/wrap_up_projects_and_organize_related_work`. The original RAPP
agent is preserved byte-for-byte in `wrap_up_projects_and_organize_related_work_agent.py` and in the RCI capsule.

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

Wrap up projects and organize all related work — Close out a project with a clean, shareable archive - not a scattered trail of files.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a general capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/wrap-up-projects-and-organize-related-work
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `wrap_up_projects_and_organize_related_work_agent.py` and embedded as the fenced Python below (sha256 3345136cb1f96806…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `wrap_up_projects_and_organize_related_work_agent.py` first:

```bash
python3 wrap_up_projects_and_organize_related_work_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 wrap_up_projects_and_organize_related_work_agent.py   # or on stdin
python3 wrap_up_projects_and_organize_related_work_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Wrap up projects and organize all related work — Close out a project with a clean, shareable archive - not a scattered trail of files.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a general capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/wrap-up-projects-and-organize-related-work
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/wrap_up_projects_and_organize_related_work',
    "version": '2.0.1',
    "display_name": 'Wrap up projects and organize all related work',
    "description": 'Close out a project with a clean, shareable archive - not a scattered trail of files.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'work_management', 'beginner', 'read_only'],
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
        "upstream_slug": 'wrap-up-projects-and-organize-related-work',
        "upstream_url": 'https://coworkcookbook.com/recipes/wrap-up-projects-and-organize-related-work',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f351da4abc366491',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'beginner', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'none', 'process_roots': ['work-management'], 'process_tags': ['work-management/organize-information/archive-completed-work'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'work-management/wrap-up-projects-and-organize-related-work', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': []}, 'verification_status': 'draft'},
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


class WrapUpProjectsAndOrganizeRelatedWork(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'WrapUpProjectsAndOrganizeRelatedWork'
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
    print(WrapUpProjectsAndOrganizeRelatedWork().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/7V6+bebyJLmv0Lf/sGuxr7si/xOnTNsEgKBJJBAUK5js4PEJhaBVFP/+ySS7nXV61fd7/XMqOySgMyIyC8ivohM/NuL13dp1bx8eTEjr4QWXp5nadRAXhlCQjVUzQl8VScf/IWCquyazO+7qmlfPr2EURs0Wd1lVQmmC3nVRlDVd5AH1U11jIIOGrIuBZdBDkR/gtrUayLPzyPIa4I0u0TQZ6ispvFt4HVd1EQh1DVelkNVDMVZHrWvQEs0ekUNfr98+eXXTy8Z+P3y5beXIPdacOvFbrx6X28e+lquDNdN4pXZLTKi3Oui0AYLAEJyr0zA6PoK1lqC6zpq4qopwK0wiqHn1cc2yuNP0H/8x2nwmqT96cvXEnp+vr5M/xl9CXVpBHWV1wLZUODVnp/lWXd9hbh88K4t1ERd35TttCYAVZm8Pmb+kFTV0M/Ts48PJa9J1H38+lIBE7wJyK8vP0FVA/Q1/fT7dZJSf/zpNa+GqPn40w85be/fIQbCgNWv357XT7Fg4I+hWXzX+jOQ+nCZH319+cPips/D7mmdYObL67HKyo8PwcCXl6j0yiD6+NNfiQ3SKDjlWdv9U3J/eQhOIy8Ea3oa/tOnO8i/QvBzQe8y/1ptDdz6r6wEDH9T9wl6AvVXsu/4/53oPCuj9h3xfyjuH02Af4Z++cu1/VcTPkHx1xcxykGqNFPefIF++2ZuJOGXD+GPmx9+/R2I/m/FmFXfBHcJ3wqQIHHUdt++/fKhvd/+8OsvH/oaxFrkFd/6Jv9HMv8Rrnc9f0LwOerjn+cC/fvyVFZDCb1HOvRbVf9b8/srZHl5Fv64336B/pgv0weGpkW8KX1A8IecaYGtf8Dxp5ffAU+UYDV9cH8Msvzf/x3SsqCp2iruIDOYWAo4uMuKaDJ+l2YtBP5Mud1EANc2m1jqMe7JZZPFgJa+/6/gToqfgycpIgNgoG99/e05rv0GmPNb9WShb82Dhr5Nc76/QjugoWqyJCu9HDK4zeZr6SVR2U3a6yZqo+YCeMW/dtFnwEifpx9QVkLf/3kl3+7yXuvr9zuFZw/GMoTlxFZtn0ev04rtNCqf6wsA60djFPRAVV4FwK479X4CSLRVDki6m9BpT1meQ2HWAO1Vc73LBgh+mYR9//7d99r0a/mgVwJ6lIUWAQPezYE+fwYLjPMsSbuvZRSkFfTht98/QP8b+q9m3YVPOjaA7p/+ARYq5loHRSTpCzAMuA44G5DJ3T+//f6EGYgpQR0D3sziLHpMBvF6isI3zE2Z+4xTNORHAGuAc1FXTQc4G8q6V2gZQ+/2AqXTo4nV06rtoDCqozKMyuAKpHpgOe9ITuWsBUHZxtdPUN9Gd63ffVDUJhMLkPhe9x3ShA2oIVUO/jeZeR8EJldlBuB/j4jHfSCk+dBC/JuIV0ifIhSqPRASaeM9dcTewy+gdrxNB8I9qIyGr+VUNKMJqnu6POABgwAywdOlnyefg/peAG4I2zfd9zFTZEG7e8VrvpbtMxVAJQeoBKA0AKVJn4VTgfjbM6TatOrz8I4fsHSS9PRC+PTKIwbBAqC+fkuw9h5TbzENgT4EesY1dO9CvvY4ipHQ/5c2YzKHWywMacHtJBGS9J3hPGCaWp4JzkeXBCo9BGLlkRI/qv8bd7xR6Ncyz4DPm+vfHiPv4D7HPGipn4wwOOMuH3gWwDTJvQfeFEhNM4Ws97V84+pPwPw7MQHsQZaepjVU7wqnp2+WpiAVPz3Aedbtu6OacMIXBBdU934OHB9HUeh7wQlY1UzJ88QXRGE0ATOkWZD+aVUQkA6cDeRDwIgMOAzw+R06vQLLBHkTN1XxY3g2dUPAirAPgLWgp4xeIRvE/xQDLUg60NJMYwAKH+6ioCICGAMT3xEGnqwfxvwhALxnWOZ/dMDz2Y+AvZsyWQ+EeqHXASiHiUrDaHw49t3Mp6uArcWUYvdJf/b2c6nQH2vK376WdxPf2Rtkbn4Puh/YQCDWikdYT8TTAvIoomf8gEC4V97XR/F8VOd3W778p9b747/Wnd/L4f7PjvsCpV1Xt18Q5FHC3irYK0h7BIRIVkftvZp97uvPb0n5GWj6/JaUn58J+Xma/icND8C+QP+alX8S8YzuLxD2ir6i06NVFkRT+D4/ABThM+98JqenX0sj+uFtoL4qALlNTriC8vleS96GgIKSNFFyr5J3l7VTSRpAFbyTKfDH1/I9Ip7pAri6TKZC2FZ/SON7UQX+fbjvnfPBo7IDusOpLUuiaeOST+a30cuXss/zTy+lV0T//IZloncQugCTabcDvAGanS6L7lfvjc908edN2D2/ADGE1ZcpzT5BU5P6CXrvNz9BbzuA+9aq7MEW6Jep151UgqHg633s+w7Pj17Azqu71pP9j23N1GI9W9+/NsKr6/z6n7iyqybVfycNiGuicw9qUTgZ9GOFPxRXD22/3w3tHru3317e0vuJ0rNTA8NBHn1up2qEgHgCCsH1w/Pg2f9FD/eUBJgJdA5AFEGQFEbQgY/FM5pFaYIN/SDEMWoWzsA3SodhyESzgIwxNvBR2mNQnInIkMTYGCU9H8h7RNK3qfhmk3URGkfEDMODkKBxiiJnGIN7s9AjGc8LUZZlUCYOAXn/mHoCvPZc8mOJE57v7eQEzXPlv734NAlGymS75B4fAZlZHnNY+Xrqzxo65toje+pG1ZotuiKPrfUhjHX37Ooa4zGFQzektTwp6qIQeCdpgNwbsk3hypidjgTBnY2leaJ3RFRs3Hp0lpWwypBuZJo8STLOuYjuuPRqYS75iKJszOyYbtKd16znEWLy87LYcdcM7d3sjOIdvCIOBLujqALf99l5Li9mu8Vo9YF/UBR93KQuLhutu7otl5qWe8T+NEp+UcA7T7liSy8TOr0R1TTH1VorSnGIxBaON6sMDktsDOPM6Q8YFSDpWqFXeztjsVVhz8+Wh2P73tBX/t6krNw5BYZ0sSR/w6qERKnnQdn5kSiqmLaS3c1B23lOSAuZuzetwuDrsMyvA2w1J3Q196zqkBrbhhvNdrlPBkJrFROXpQ22xosWbcplKCsruO+K9XjuZtZNDo8YnjbFLnKHUkpcrZNKpeU0thk912wN81puDYWJt4KhmF3R9wF6WuAeZbU9HRiocMXdectt9/uLahLr/Q3gprPwvmqPIdMq8PpkFCukk84JNTa22B6a0BrUPWzZq4VZdLetPI7wdblaGO0CRCo3rGajtT7Nmry1UmUhlGv85JVcHDlDpWNLdZ+u9sxRS6nWibdsbsPBcrxglwWckINnhxhTR10QS2ofdjiPwfiNO7f7RjsumQ3bksPFWUjbrD1uL8lubRPW+YYZl3pIIh1zjaVSDfk4Gqxv2H522OjKjbHhQyRcFnM0PWrWzVfnyab2nRJdwXpRG3nYOBJ7ZC99fy6s7ODa8xLFS0EY18jqdEPd6sztlzaKXrGrjy2t060hFFC19n0cjes4TBWP0AkBL8BeBGWkbtjH15046CVpbLSNqpuZMT9fWBGAt7lcxpTNTgueCq8MrrfNLhzPwZFcM7KzdHFdPVVM44USa9c5tawKAx7Oi9FheNFctGZJOaEoJXt45fJEqeInftGcreawDYLz5bZorqFEUI643ufdieZV25n7g8e1krTHDifPiJQ9wSGVtJzrWJUNjuAIxapwWrHelWLi9IjEEqdME5vZINfNflWohDHfG5hNK5U07vvr4epXeXULhRWbOLlnIGItIQ1FF1fD8C9VeQYzN75R1ah7cRhEKAcbRvKk6vHIR4ZzFx3YoM5mAbotLIRH/cuSPg8Z5oTALeN+nqfNyj3hgz2j0wr2q7Ox4US9pjm9217p+fXmDoszvFepQ+nXCafNFKpLL2vEI8ncGuv2up5tLNESLlgwbg17751O8nChOjq/btRTudjkt9q5oqfgdjE3OuUglsA1xJVXbK5MwnjPp/qcmVuZc+kGCZltV+N5EMk9giyspVRZQ9Ow4nDVYNGb74NssTqfGVE+LmBnXs3YJX5aWig93/YtOhMYUXCXK3Nnk9lCpAjN8OxrvuIG3a7d9EiKa7lILlq7pGCu2MYyi+fG9cLPbux1DRJHx9pCIdcqvKZzKpCV3C2cobgkexMnuzOMbvEz5qFMh43sOXM2M2aGbGWKlpxuseBP/h5RhYXatVigN6d4YTqudy42kWnND6RNXSlGiI7e1d6SGUtxGqpwWyMgyB7EJu/w+prYm6UsxfGlSdZFHO9HN1jNlqbpOc6SFy+mydlcGp4S/0Dyu25nldqe24jHNNgn6l4yOtn1cDVQdOfggTIDwOFhXZWWzXCeSfNbn61Yhh0yia/5TAookrb5lW5H8sIJel0dsnreD7BAp17kmaBHioM1hp2i4yJvURqJDnOYjVcgaubLyiME+xAjBWaa+8C9hCpJ8KO6TvkgjPJmIxLwldPWcl6smUSSjPZyO7V0WCOLgjVFhkI2+gbBmIPEsJW3EiyLIes1WJ3FcEfezFB416wbsO6zVfWWpeTJqnPnqHlb6PZVPHqJGrhxUs4yd762KF1YdgtaUWtBy86OnnkhTQnO9kje7NpATVrUs27JM0Rdz/NIdupFsTtc63jfjUYoYTNyu2L9Za3p+Ylw4dDopC1G1fpiFx0GB7Z7crVzMMopDLInD7q+PZAXwjzgy/YmbC+W5RpFRMtXf0hnpNYfRk620B5Wk4M/qu7avOyxpnc3sNBoxE1wSbRl5rhRLuZnsrDckXXknXLhZbS6ZjfClpTtaPIcmV9Sb2F1a+l4tALnHKt4judL66hexohQFcEadC+31oW9y2/K1kFstl7betklsZqoqyq5LigDTrSIT7TdCt3aFlFcZxdli4rG9oJxbq9Zlu1ZaoaXunT2M/W0WPP4Jr5djrjHXOyFjRrLoRgSN5Yo13TIhgxtNnNgZe4kWrXsmi2iITLFbxrftFFPAtuQOMAaRtu31Lyb7xH7OldmLJIXxzO2NnBtIzqiwKF8cXG93bVZWRZVHby5ft6Tp44OJXfDpwq82jfjyjq3O3WpwFglNlda40ysNAMS0LF9U7p81xuGUUs8VxXpyfU9KcH4xTigZNnfSjSFPalbauy8ocPd0anWTX25aJ44vw05X7tiHV8Kxo1WsKt5oHW9qsdU2cIzpIvdLoL99cHazbRqG9JGOlNRKzlvdtqS8nfRPEtpKybWNarP8jXu9AbK5iQ+Uuhxq4RLfCnp6zi/tJKdysqWCxS6NFGislxVITezpaWGDn9SzVu2bHIqLOf6ShMM7rQD1Z4fDH0ZOTmnFW0yCvp50e/90qSFJAmNoXeuRd4LWWhbXVcoy6Opyos56ES2/MhUt0UphFFgGv5WZdwKJ04+feZtS3ZXVhroqxvHb2JLHbFyqS1l8nCtstLbFgvO4HvtWuHeIjTj/Q3dC5kqHNVic96tleW1KVBlRo4zvdbWDurMmcbws/Mmcajk3HS6O4e3+KJQmGJZK+vb8uxfrxZnnBcNf8AUDjQEAoqzgcNXHmrzCnxSLUB3gswVxQJBKkw/B5uUu2o4LEpndKnyhMYjBG85naPk/hKvMuUoqAdrPnonakXS4ulmgX1uJq9y6WSmfguKgtnOZrgYHRzaOW/ghFiTB26zY7f0pdQ65QbzVdrlq91il+5NDaUtw5cqVQVxkR98QF78cr9yW6YCLUUdCrBmz3zlEFNJsugAH9mBo2wN2IjMWxgEO66UZZ5rEaUVsDJ01NMm21uCW6wPBlICbP32qA4yEom4TPAKDwhHUCQlKg5NSxS91eKCi9g3E+O1ODh4PeNiRUKrgDajnSZUoE0P2sYJLoRYGLG2HqUsVaU1q2YzxKdIyrxUtkvBFHwpa7OPG1JaVzf0HJ1TURjYUSyPsmhvKU315dBHzC2Nb20EPhZ6I6CiC4vdbH6B5UQ7mDMG5y/xgdj6otiLl9BDEAdUf4wIdCrG7ZKIhs53EAxEy4HjbY2RLfa263m5uy682DhrIh5wtiNxtd2RDBIOmrxj266gyxCvy24xI+tsKYCyv10sW686JqpiUN3hhOzVYsRPEuWw++jAUxZFLIa1ubqSTqIjsgU2EBjikAu4tdpGRhx+j8s0LezaUVVXR5scyu3AMkg56zBkTFDQXXkH7ICw5oYmNBZjRn/t4gJKne0xX9LyEoT9ppM5C17lSVrUmUDbcmIKI8IdZ6skJcW+6m9Zszzs0pYizUVxvIrXVGzmSzFRri4yp0Gm7gQivHYFn5Ho6Sqbx2TGiOJ5y1VzjcQUYuXNKPN4WhhzWTvW2nCFpagfd/jtWLdR1JKxV9MWctxUDNNq9MnWmo0mp2JyifCkofR+Nl6v+tLRVcDvZhTcaD/RZOnmOTekKcC2sqzp1Yh6cu7JsGUhq83MYRmjSjUjO4XDbrk1Yj+htwhvhjPcL5kVuNUdPDbULHcxp+YnlWW0sYujK6KLFVMDp/TsRZKb9YIqZrexz0l42O05Pu4p+0aqFCwdgxWnpUwpZWGqzlREyqhKl/MGPsO7RJKVUmQ7Q1TXtLIqC0o4+Rzo5Nbiwo02FzUd1EFFBS/qElo7IbzVMxvJYQOK18gjb+/di6B4pGSHoCudRfFqHHHJ6ZOZpo+7HVp6l8FM+iTbCP5S7uWcuFXDyZ6VpjND1/OZzZbWHJvBzY6/MaxyS1fn2SbByr7d2w3NSAd9LImEUWh0H9zWIuwPYa6hFrudz7VtKZyxS4kERIeIfMBjuE/IsS2GFylJ+TLUI5/UTufxRNFjXzGsjisGjqTa8RhbGNOLi0gfETdcKNtV1HYLGKZLO+TP2ao6Myh+u1zl2q7n6Vnex4PMo+hQgh6cXxZ6wBlrc78+Gy7NmktOa2RWiDo2l47U2jixXKQEBdgjEzuE7oseBwHEOuKWyOGRhDn5ytSXBR7r7cULZ9jlgJmsYZgsTGw2Yn0gdI6pJartjpejX6EZBkf7UFc7vO3dLsWoJUxSXkEjcYIQwyhv/DzeRgRr1bQAilB68EPxvOR3cGnZh01JzllFJvHzljUqWjkzulAmMLZiXTvxBMGZnz14JRMUuef52QJz4KDA0LwgjmVsFZXTUjFrCQcr6bZpJG9UcV4ZaLzl1kM9GGndxFJhtQFeL+q+Y2xqpfYdTLR1hK1pgqqXh16qbRfdwA68owhuntCxzB8O2HKLnMooWG85u5cUsu+4fbFe+xJoHQwGd7HNrrrNF6675o+u3+K0NVeOjGpXeEgJbOjyOdKt6Bs+6DA8blXyprPnISaQ4/wUF9iVFvtI1sQQ6QfLjdvOjlu1EkmmH08OKpmXPowlgkNXGHNLd3RMU2W8H2oMXW+42NkNTBERHZ85iwwfKiG8NBvhwh1ka5XvIzMcM1g14BmaH5YmlpchI/tntu9O7JyNOm5QCGHPcdzPP798epkOKJ/HjP+DF4bTedL/s2OtxwnU2xuI+yFj5IVf7rq+/E+M+/XTSxNkwLTHcV6b98nzyOvvDvM+//NH2JOc6+O93PTyZOzezmo7L5n+vclLVoZ92zXXb22V9/eDxU8vft9Ob73byfoAfL/cF1rU03lp1aVRA77vphfe9CZveu02zYqSbHrzNZ0fAiC+VWV+X9Pz1BssBX9FX7GX3/8PF2QRs5EjAAA= -->
