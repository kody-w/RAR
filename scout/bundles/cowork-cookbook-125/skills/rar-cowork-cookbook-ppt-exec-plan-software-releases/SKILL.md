---
name: "rar-cowork-cookbook-ppt-exec-plan-software-releases"
description: "Generates an executive-ready PowerPoint deck on plan software releases status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_plan_software_releases", "rar_sha256": "963bec39f48ae64906fc9d830220e402b45f1d5a22255c09fef5b9b1708d6d84", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_plan_software_releases`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_plan_software_releases_agent.py` and in the RCI capsule.

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

Plan software releases Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on plan software releases status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-plan-software-releases
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_plan_software_releases_agent.py` and embedded as the fenced Python below (sha256 963bec39f48ae649…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_plan_software_releases_agent.py` first:

```bash
python3 ppt_exec_plan_software_releases_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_plan_software_releases_agent.py   # or on stdin
python3 ppt_exec_plan_software_releases_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan software releases Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on plan software releases status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-plan-software-releases
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_plan_software_releases',
    "version": '2.0.0',
    "display_name": 'Plan software releases Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on plan software releases status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-plan-software-releases',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-plan-software-releases',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ffa5523311f4c1b0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/uptake-software-releases/plan-software-releases'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/ppt-exec-plan-software-releases', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.5, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class PptExecPlanSoftwareReleases(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecPlanSoftwareReleases'
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
    print(PptExecPlanSoftwareReleases().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6+7ObSJLuv6I9+0N3r2yDAIHwxERcQAgJgcRLvNoTbt4P8X4IUN/+328h6djd2zM7MxEbcWUfW0BVVuaXmV9mFefXN6fv4rJ5+/ymBk6x4JwsS+KgWTiFv2DKoWyu4L/y6oKfhVcWXZO4fVc27duHNz9ovSapuqQswHQuKILG6YIWTF0EY+D1XXILPjaB408LqRyCRiqTolv4gXddlMWiysC4tgy7wWmCRRNkgdOCyW3ndH37AayVV1nQBYsh6eKFFztN1z6U6pzsmhTRx+ohrSjBip+AMsHozBPat88//+3DWwK+v33+9c3LnBbcepOqjgUqSWBN9bWk8loRzAV3IzComgASBbiugiYsmxzc8oNw8br6sQ2y8MPiv/7rCmZH7U+fvxSL1+fL2/xH6YtFFweLrnTaLvAXnlM5bpIl3fRpQWWDM7XAyq5vCmAHMLMBRnx6zvwuqawWf52f/fhc5FMUdD9+eSurGVkA85e3nxZlA9Zr+vn7p1lK9eNPn7IZ3h9/+i6n7d008LpZGND609fX9UssGPh9aBI+Vv0rkPp0qBt8efudcfPnqfdsJ5j59ikF0P/4FFw15S0onMILfvzpH4n1YuDyLGm7f0nuz0/BMYgbYNNL8Z8+PED+22L5MuibzH+87Bxg/44lYPj7ch8WL6D+kewH/v9NdJYUIH7fEf+74v7ehOVfFz//Q9v+pwkfFuGXt22QgSxrHDcLPi9+/apKLPPzD/73mz/87Tcg+p+KUcu+8R4SvuZOkYRB2339+vMP7eP2D3/7+Ye+ArEWOPnXvsn+nsy/h+tjnT8g+Br14x/ngvUvxbUoh2LxLdIXv5bVfzS/fVroTpb43++3nxe/z5f5s1zMRrwv+oTgdznTAl1/h+NPb78BeiiANb33eAyy/D//cyEmXlPObLRQvbLvFsDBXZIHs/JanLQL8HfO7SYAuLYJAPY1DsT/7OFZ4zJc/PJ/vAdlfvRelAlVVfd1JsNHPHx9p7uv73T3y6eFBsSWTRIlhZMtFEqSvhROFABqA0tWTdAGzQ2QiTt1wUdAQx/nL4ukWPzyTyR/fQj5VE2/PFgzeXKTwhxmXmr7LPg022bEQfGyxPtG28EiKz2gTJgAPv0AbG7L7AZ4bcahvSZZtvCTBhhdNtNDNsDq8yzsl19+cZ02/lI8iRRdPMtDC4EB39RZfPwIrAqzJIq7L0XgxeXih19/+2Hxfxf/06yH8HkNCfD5yxNAQ149nxYgs/ocDANOAm4FtPHwxK+/vbAFYkBhWgC/JWESPCeDyLwG/jvQ6p76iKzxhRsAgAG4eVU2HWDnRdJ9WhzCxTd9waLzo5m/47KdS1kVFH5QeBOQ6gBzviEJytKiBeHXhtOHRd8Gj1V/cRvnoWIOUtzpflmIjASqRZmBf2Y1H4PA5LJIAPzfwuB5HwhpfmgX9LuIT4vTHIuLymmcKm6c1xqh8/QLqBLv04FwZ1EEw5dirorBDNUjMZ7wRHPZTryXSz/OPp9rL2ABv31fO3qVdn+hPWpb86VoX0H/rN0eKAJg0ahP/LkU/OUVUm1c9pn/wA9oOkt6ecF/eeURg9LfbwTY9xbi983Ddm4evvQIvMIW/z8bjllviuMUlqM0drtgT5piPfGce6QZ92dbBYr/AgTVM3e+NwTvdPLOql+KLAHB0Ux/eY58eOE15slUfQNAUyjlIR+EAMBzlvuI0DnimmaObedL8U7fH4DTH1wFLAfpDMJ9jrL3Been75rGIGfn6++l/OHRxp+tB1G4qHo3AxESBoHvOgDLLp4xfncDCNdgzrghTrz4D1YtgHQQFUD+DH8C4AQU/4DuVAIzQYKFTZl/H57MDRLQwu89oC1oQoNPCwMkyhwsLchO0OXMYwAKPzxELfIAYAxU/IZwGzvVU5m5b30p6My+KHMQKb/3wOvh99B+6DKrD6Q6vtMBLIeZaf1gfHr2m54vXwFl8zkZH5P+6O6XrYvf15m/fCkeOn4jd5Dj2VyifwfOAuRW/oy6maJaQDN58AogEAmPavzpWVCfFfubLp//1Kz/+O/1848Sefmj5z4v4q6r2s8Q9Cxr71XtE8gVCMRIUgXtXOE+ztn3cc6vj+/59fE9v/4g9onS58W/p9ofRLxi+vNi9Qn+BM+PhMQL5qB9fQASzEfa+ojNT78USvDdxa84mNk1m0BJ/VZq3oeAehM1QTQPfpaedq5YAyiSD64FTvhSfAuDV5IApiiiuU625e+S91FzgVOfPvtWEsCjogNr+3N/FgXzxiWb1W+Dt89Fn2Uf3gonD/7phmUmfRCmAIp5kwNSBjQ7XRI8rr41PvPFH7doj2QCLOCXn+ec+vCgRMB87/3mh8X7DuCxoyp6sAX6ee515yXBUPDft7Hf9n9u8AY2XN1UzWo/tzVzi/Vqff+sxJxKQGMvmAt5+S035xX/JAR8iaKg+bOQ8+OLk70IAnD4zNZJ957WLdDTB03OhwVwHEg3kEGAGHsw4c/LgHWaoO5B/fNnc7/j992s8mnLbw8Yuufe8Ne3d6J4+eDVB4LhICM/tnMFhECQggXB9TOcwLN/t0N8TQfMBloUMJ/EUTfwUDLENk6AYySMhx7pb1AYQeAAgxEXW4crf+0gCLJeezAZBuHaJd0VAW983N9gQN4zJr/OVT6ZVUIcx9t4xArzScLBvQCFXdQLVsjKJ9AAXpNouNkEGEDn21RQD/2XnU+7ZhC/NaszHi9zf31zcQyM3GPtgXp+GIjUHcIgXCV2yQYPLNuEDm5yqVX7RpbGYPgKXHA4zVP3nlAC9kjwlKfqJ21/sO7dUVxtJTlelgp5TVeodE2Ol2rKk42RRLIkFPyV8JfEvg+88+5iKjiL0iru6nB3H4yGdnYHHtSXwg7W7ErJMIG8un4i1adrrcd3WEFGkyDWeojIlZqsI/fe7hK29k/OZn93zfVWozJjwm9UjhRbDacKYXW06pjet0pVribS2ZwSeW1jlqkTvKepbdPomiUq+EnL8M15SxJeKCAEfSUCCEWgQ2DddFhgmPw0MPcgF4y68vOpcmrbuNxOYkaMOu3C2/3G1jisdp1tZ2faoTu7K7LM3Z5Xd8xOHEovEy9Y7xX20jOgnYd1sdFs5TFArlF/xDLD4GDM0T0mh/NUODUXo+cvo1f3G74uyaZztlrZBzaumaTZuaXBq5u7eJ1yvBrPUivc+WR1HSubWTP5nvMQ587dTiZeqaKgX09IbzdmeB4mZo1WfCs2Pcv5+omxz6SexmFvCIKRI/ikxZXg0hCaa7I3rWrWlW4rchr65LpSYSN28+icpksk6mJuENx1vTVa8yYdHYevd2PuEccNkhyQ5crIrmtDzH24llfxdu8hBIZTtiGg0ogW+bTyNgQNV721b4osQ9FlfEo6UzTvRzxMj2MfsrrRddiNqQimtVe7nN6vxlK3Dl7b3H27PqDTZpDOda2JdH3fIZa2RJL2btcuv5d0sz62OuQXcsyeylt7MFjIubOYokwBs9Lyo2mM6+36vlqFdx/wONtINiGJQnvf9HFsi5cTO7FNaeiGfQxMO9vyFZfOP8dKIC+2I2JLzeWWNL2EPMgawpiCBjFBxVi8FBAWNnsKhwJnj+uetecR4d7sA9I+tLfcrLI+b7PKVNo7lWFOpwu6BZ/d/RI2uZWixCnH9+rmEnSAJyaKQo+ZTB+ckylctPK89I9rJsF6Sl6LFh7ByLbcc92l6bcUM5SIynNKcW2YgtjbbIzFcHe1LcUUjZU71YCzfO6CeZo/YpPmMeXyfCv0Ph9U6JpgyuZqU7drzwi8FCfEySeO6+NBQbT9ZjuZXNSjqr2FannrTfH+3Be4BE3elV7rHs6zSDHaG8tF4yOG6hlypmRLHBDxiCsXsdizkHXmYHizCxv6kOiY5pHDxj/ZwVAQo4nfpfNJOOrcNfE53qmnuGbp+nBnd0TRQi7KlKdNjG4OldhJfIaSZHFIcC5Zbqy4yJuVSlaOtFo16vGGtBimj0klbPcxdEE061pYl0OHpsa0S0tlrRm+d2LxVjlQt5Tf7px9AfveJRXOF2edr7eHYrMSISsnbHk8D4UJG6rJHNZ3FjowucKbvim7TcgstRG3GlE8B+edq1KC2+Fga2mYYEscn68GY+88+W6YsX10TsL+cCyayVBHiZCEQ8Wcdd9sMso5id6dhIzUjmELWS8PxamoedTjekhikOuU8JutuO7x8lCgJZdBF5eWyrLLlaBdUg27X6HrzURueIwKMnLcXi2ZpImjyhx2V2Ia5EFK6bPYK+r+xm/T/iCMayEdcxapQtE6tMtulax02Zi8ouFvYb61Rsa+V8XBFR0yuJVwdx5KHcncsVZrgVCmkU4VhdnXkSKs6Og2uLx6vIRMz3GDR58ZdXfo+fvK4a36pHSk6XqHNbW/8oqxY7mL0245Xbhk1/7U3uMBkdkacCh6H6KD7mw2RxRbEbeso1X+5BRITq02VbpajvCIB/dut61SEcOXkJvhftEkd1FllGPWiYrdoaR4bK8DJMD1yrCloeSs8ipJw+2O2QM69H279mPPObJHQ4UIUIPF2w29Y6BR08mUOkXBwVRU1EEq85bKMH+gpVZlrqJrE3c5ahlVyLypHiqKu99DTe7OTNUyQsQaLWo7d1pPucGR4fVJlc5BT9UVj2ROQoza4by8XE9+fN7sNpeky0g+Pcpl2Fzwc075nnlzs4usYRvfty9xtuShUHVDlWp2pLPesSv+SO3TfaaKPcLdG+Oe+5RRacH5mN8vp73uVuWGotQw8XGms3d7FUFQlnPx4oTwlnIq7dWluF2bNtXKRkJzNfFc66gLCLRHd/zVQTnscN3r045T0+PK9w8CUZgH1AqDw/WoZf2ST8XYkcXCVq7dtc7T9GwZoRlyGSPuyTwfOGu0GMuF1Fhq/aHdTrIq2d6qq0QRViNrKm5ctrsxmpUrO27TCwrdDm5g0AfY2e7QlbyBToNcWNuu367kXg2ulKyUhm2zPt3qV2FV0PmddwM0HzqWp+tcpokii/NsqE9RxwKW6cWSVk/Szs/7Te2STl0yMNbGlhuwOQLHok40jajv6cRkhgzs+nxiQ4rmpeSg8ALnB5e1jS5Ms44wVGGldvyFpo0tpHd+YTWs26+5cuTYe79yGBwJsptnMfzZVTuDCy9nSetTXmUY7NiegtIUW3rfCOuhpIKVa+LbvuXPwcFtuY3i+J6wy9UDBVGjtYSPvD2wTLOpWPOOIVgPOWIlejDlOX64xE4dZ6YOaZ/Tq9wG5UDz3r4wkwjDNc5XUV3RZRPeBEFKhOtpQ/oevcvMqYot2ccpiYzgNMrPxXZNwEa3ghNcD00825wJxDbUTa7VoYOgzm2HuGWssKnFMbcebbdKQ4k7lW5hYeuuslLADMUKCdqz9YRT40S6liDQ8fCywUCl1ErzwjQwzqtN1l/W8HYEVf/gKJkCm/xVOJ8Iv1a2I4Ef0aOReRv8UtbbKyp0euub8FmLuO3BvJvQrgYd1E480/BYaCeqqC7LVj6ablIze1B+V4FiDGxWSkHE0UEuq1DH31j/3HdTnlVreJdj9NI88bi39KxghC83jnPgbik7mOBc1+a4Y0RxlG+Dn9jNWI/xJRNNtk6wXI1paJceiyApWUfdXn3jPHFjpV7S0pd2emPTWA/bVhjpuZSwgDRX1U0rbP7CkH6qInZ27Jzk1qhyp0+XW8HqWI2TcNtDWu5sQ9DfuAm/JUoe3porHEmTVXTqbg7CYSPpG+oKvadOmfVwRe7sPsZ2OeL7Qn1n0l3iQ8eizIsQsR1tB+E1c6ZPjbo/FOWKddlyPHO7EqdZTKWZwofvO2pjqlyS8a6Sd6LPGmfO2/pDfNnsc0hQT+RkjT1Jj8uTBpOFSbOlIxCMK8SaCp8qmZl0QYslamfYw4Xi+knOyrN+EPpdnU9IR8lqdeHzbBtcV2Lv1V01OSPYvxAB7zExZ6G2SkQ6V/vNQT6e93d18E83i1ErayAwRRyJc4to8u60xtNbxAuWrNVSXLiaoJmH0z0zRdCB36uhrtgDS1XkMbOqTCn8iN+M+Z7vmlU4cCIEdg/rdVFyZCSWN5I4INW58QjNiNlIvg8V2ZhVYpl+0mSFEzcIkUh+ZWu2Z7QCLazvA8RJ22Xb0PKRqGkWlRU8Tyji4lYaynMlFfVdn14dB+kV+hpN21Kkh+GsUfq6p2hlFzt+I5cXEdFSubo0mhP698k1htNlt3W2dYle9FuM0ojPrYhpoo5KEct5qdy6CN9IdJUdaZ21zCICzQaX3gCQZcl4y5ISunrpWJN/9rcrmAUDjCAYeWy101VzxNMjVSagVQs6wTzr5p5JO2a73VS+y0C7beym5m3f7UhilFxQZcdlPQJIOq3xKkKfeOK2jZB+hCrUXwdEZDXxtJ74thUo9JSNxUWnIjY0z+vLhdBaQ22iQPcNGEbsDc1PJykVeqIP0Cg4D069t5tNE+1UWNk2vXW5KSeC0vxYuMSScaBLjlATd+uEdF/HXXNT3SWHUBDY2AbYbomu+H1I3NSwTslgSymFt3fP4+1e8MSZtJ3gnIpoWxNCQrnadoOnhc+gohm4DRWk90GClqhpQtTWyvSoCm0ISrJlEBXdLSBsUjFU39GJ5IJcSbnE4rtbHiX+Djs629Zj24/HddVWS7lZyop84sIWEeIrRWtpNw35SZQw4WCh/G1Ho/u1CNX4HjSQ+oRnoUjuhtM1Jyq4xCV6GJGrEfXBgO97c0fci+JgBPB1PMHCUTieoVLehkZsb87ythp1NILCIiyX3HKaorYtE7JnpQhBdDS0zE3o5XvhgMQc2LEewwaWSRvl7pEFd7tESmVTM294JlyWSON5hAoJym28QcH5zIbnY1PXkkXnh0Nxs3AzVDY+jbgFIWkHxe9XGGExY0L5tnFKT66JtjcBck54b+12aLwuyfWIind/Q8T+raUQVjaxWm/JdHRbBnXWKQ06FStvr8vkVNHByO1X0dK+yXtYoCItM0DPKiAqPB5V0tTSqYhQJbpxF0W5YxdB3Ow6gdvfZCnlJdfPGgnsNfD7dj3smc6agutJHLAOX+bSHRO5VEFZrx/IC73iK8bAIZIws+hy2YNm+UjQ7IWwRH4XkbBBjdsxaEINj2XUsttRXEIpi019kQ/upvMxsrmjqu62p5uI3IumshOXAxtSyKFbFHdb0d7gMpp2myiFrvl53ON4ato3j6gHl8SuwsEjFNJgmNtS2iPSnjJYcQ8V60RcJVjK4sQJ2iNVLgRBPRE7i55gY2tffE/thg7Af+ynalX1cU+Yaudw58bXVles7wae3LuDzEd76tCcca8F1zV+vrNJJB1GKCv4TR3pXjFsltckIfhbzbsotWHuDmEyQsDSpY8sU09iSNu93chz2LU33C2Lmxm7IeLSFMimYgnX+5x1kV1rkCGxNQ2i8gPiCIOOeXABmd2blQuKgKUhZNMuUxQXCHLJylAWygGKuCasy8B7S9m35DqhLkt918F+LkHJ6HElcg3ErMbX6v2OyrdKkskTJTLZIdTRDSSdyaiMesEfkb3QcBIDWsSdTbRI6kpd20hI00dRrBPhmdoDS0KKOilXj8dKPjjc1FJWaa30Mc6Li9rVSMJx+6JUSAH0kAPNuqi1LO4rqmixcDvK5q7TwsS6iZJIuXR0xNSCQRD67A72xTbD2vWykyzi3orKuTCWERnLJTWtIvyeYbuix7RUwHcZmpBXOoTIml0yU78LmOXoXsJDfBIydJ+giGWQ401We8ieWggzokPa67oapKqSTITu66ETM3UI7Zh1t7pLChlpzcYLKELWLMwoXCQa2VTl5Yg+ozDBSHgib8pJde8asffqtMeJQsvP8v2I5vdx5ZiXzTLacESjF9Z0pSjqr399+/A2Hzu/Do//1VfD84He/9q54vMI8P0V0uPgOHD8z4+1Pv/LGv3tw1vjJUCf58lpm/XR66Dxv52bfvwn7x3mydPzXev8nmvs3g/YOyeaf0noLSn8vu2aCWiT9Y+D2w9vbt/Ov7PQfn0dUL89TMqr+bT73QTw1fHzpEjmF6Ffu/Lr88A4eJt/rWB+fxP4yffL6HWW/OHNn4B3Eq/9iuLrr0FTzaa+XmbMZ7Dz24y33/4fvH32Bo8lAAA= -->
