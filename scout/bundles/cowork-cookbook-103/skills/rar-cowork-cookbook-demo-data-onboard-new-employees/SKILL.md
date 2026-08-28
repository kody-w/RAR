---
name: "rar-cowork-cookbook-demo-data-onboard-new-employees"
description: "Generates and creates realistic demo records for onboard new employees in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_onboard_new_employees", "rar_sha256": "75db6608e059a9c117a663515f75a6da7115b7c6322223946a756ce00c0b4d6d", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_onboard_new_employees`. The original RAPP
agent is preserved byte-for-byte in `demo_data_onboard_new_employees_agent.py` and in the RCI capsule.

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

Onboard new employees Demo Data Generator — Generates and creates realistic demo records for onboard new employees in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-onboard-new-employees
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_onboard_new_employees_agent.py` and embedded as the fenced Python below (sha256 75db6608e059a9c1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_onboard_new_employees_agent.py` first:

```bash
python3 demo_data_onboard_new_employees_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_onboard_new_employees_agent.py   # or on stdin
python3 demo_data_onboard_new_employees_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Onboard new employees Demo Data Generator — Generates and creates realistic demo records for onboard new employees in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-onboard-new-employees
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_onboard_new_employees',
    "version": '2.0.1',
    "display_name": 'Onboard new employees Demo Data Generator',
    "description": 'Generates and creates realistic demo records for onboard new employees in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-onboard-new-employees',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-onboard-new-employees',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0263795c7214d6a5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/recruit-and-onboard-talent/onboard-new-employees'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/demo-data-onboard-new-employees', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DemoDataOnboardNewEmployees(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataOnboardNewEmployees'
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
    print(DemoDataOnboardNewEmployees().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8Va+bOiyJb+V5w7P1T1WHWRHepFRwwqioqggKB0dVSzJPu+KNDT//sk6r3VPd1v3nsREzF2dAmSefKc7yzfyeT++mK1TZBXL19eVGBlk7WVJGEAqomVuZNFfsurGH7lsQ3/nzh51lSh3TZ5Vb98enFB7VRh0YR5BqevQQYqqwH1fapTgfs1/ErCugmdiQvSHN46eeXWEy+vJnlm51blTjJwm4C0SPIewAlhNrEmNRRh592kAZmVNffRTWWFWZj5d+lFmOTNpHbg4yrM61eoDOgsKAPUL19++vnTSwivX778+uIkVg1/elnCxZdWY8mPNSVw499WhHMTK/PhoKKHSGTwvgAVXDKFP7nAmzzvPtYg8T5N/uM/4ptV+fUPX75mk+fn68v4n9JmkyYAkya36gZACKzCssMkbPrXCZfcrH5Eo2mrrB4thEBm/utj5ndJeTH5cXz28bHIqw+aj19f8mJEFsL89eWHCcTi60vVjtevo5Ti4w+vSX4D1ccfvsupWzsCTjMKg1q/fnveP8XCgd+Hht591R+h1IdDbfD15XfGjZ+H3qOdcObLa5SH2ceH4KLKr6OTHPDxh78n1gmAE49R8E/J/ekhOACWC216Kv7DpzvIP0+mT4PeZf79ZQvo1n/FEjj8bblPkydQf0/2Hf//IToJMxi/b4j/pbi/mjD9cfLT37Xtf5vwaeJ9hYGdhFcYHXYCvkx+/aYe+MVPH9zvP374+Tco+h+KUfO2cu4SvqVWFnqgbr59++lDff/5w88/fWgLGGvASr+1VfJXMv8K1/s6f0DwOerjH+fC9U9ZnOW3bPIe6ZNf8+Lfqt9eJzqsH+733+svk9/ny/iZTkYj3hZ9QPC7nKmhrr/D8YeX32B5yKA1rXN/DLP83/99sg+dKq9zr5moTt42E+jgJkzBqLwWhLAs1ffcrgDEtQ4hsM9xMP5HD48a597kl/907iXzs/MsmchY9b65sPJ8e5a7b7DcfXsvd7+8TjQoNq9CP8ysZKJwh8PXzPIBrHpwyaICNaiusJjYfQM+wzL0ebwYi+Qv/0Dyt7uQ16L/5V4xw0dtUhabsS7VbQJeR9uMAGRPSxxY/UEHnBbKT3IHKuOFsJ5+gjbXeXKFdW3EoY7DJJm4ISzkkAX6u2yI1ZdR2C+//GJbdfA1exRSfPKghxqBA97VmXz+DK3yktAPmq8ZcIJ88uHX3z5M/mvyv826Cx/XOMB6/vQE1HCrytIEZlabwmEjd8DCa7l3T/z62xNbKAYS0wT6LfRC8JgMIzMG7hvQqsB9xkhqYgMIMAQ3LfKqGakmbF4nG2/yri9cdHw01u8grxtIaQXIXJA5PZRqQXPekcxGeoLhV3v9p0lbg/uqv9gjh0EVU5jiVvPLZL84QLbIE/jPqOZ9EJycZyGE/z0MHr9DIdWHejJ/E/E6kcZYnBRWZRVBZT3X8KyHXyBLvE2Hwq2RZL9mIyuCEap7Yjzg8UfaHun57tLPo88hz6ewCrj129r+k9rdiXbntuprVj+D3qrAndShKv3Eb0N3pIK/PUOqDvI2ce/4QU1HSU8vuE+v3GNQ/ss+YGTsyUjZk2djMfJei81QYvL/2WmMCnPrtcKvOY1fTnhJUy4PIMfmaAT80U9B1n8IG5PmeyfwVkfeyunXLAlhVFT93x4j7/A/xzxKVFtBtBROucuHikEgR7n30BxDrarGoLa+Zm91+xO06l6koHdgHsM4H8PrbcHx6ZumAUzW8f47hz9RGy2H4TcpWjuBeHoAuLblxFCrakyvpxtgnIIx1W5B6AR/sGoCpcNwgPIh9FBV+HXL7tBJOTQTQutVefp9eDh6D2rhtg7UFnaf4HViwAwZo6SGaQnbm3EMROHDXdQkBRBjqOI7wnVgFQ9lxob1qaA1+iJPYXT83gPPh99j+q7LqD6Uao0F9Wt2G0usC7qHZ9/1fPoKKpuOWXif9Ed3P22d/J5g/vY1u+v4XtVhcicjN/8OHBh/VfqI57E21bC+pOAZQDAS7jT8+mDSB1W/6/LlT136x3+tkb9z4+mPnvsyCZqmqL8gyIPP3ujsFVYGBMZIWID6Tm2fR7w+P/PrM8yvz+/59QexD5S+TP411f4g4hnTXybo6+x1Nj4SQ5iWEIrnByKx+Dy/fCbGp18zBXx38TMOxrKa9JBL3znmbQgkGr8C/jj4wTn1SFU3yI73Igud8DV7D4NnksAanvkjQdb575L3TrbQqQ+fvXMBfJQ1cG13bMx8MO5YklH9Grx8ydok+fSSWSn4hzuVsdrDMIVQjLsbmDKwy2lCcL9773jGmz/uze7JBKuAm38Zc+rTZOxOP03eG81Pk7fW/76Vylq49/lpbHLHJeFQ+PU+9n3jZ4MXuNNq+mJU+7GfGXurZ8/7ZyXGVIIaO2Bk8Pw9N8cV/yQEXvg+qP4sRL5fWMmzQNSNNfJx2LyldQ31dGF382kCHQfTDWYQLIwtnPDnZeA6FShbSHzuaO53/L6blT9s+e0OQ/PYFP768lYonj54NoBwOMzIz/VIfQgMUrggvH+EE3z2r7aGz+mwssHeBM6nSdemqBkDZiRrsQ6K0hZF4SRKejRpUa5Foyhp0w6FY/CDswRl0STlgNnMmdmES7lQ3iMmv430Ho4qgZkHcBbFHBenMJIkWJTGLNa1CNqy3BnD0DPac2Hx/z41hmXxaefDrhHE9y51xONp7q8vNkXAkQJRb7jHZ4GwukURtC0F9pSmPL+MGGbGFn3cULchtRXKUNWlu4hvqkorGo/qfBnaZzM+qUYiS/ScE7DNIV17psguT4lTxbQqdpY4b+S90juHpYNkstv7wlFbklLO6GifiZ1Jbc/muvC7xfqgXOhOoYe4krMN3F8ms3LAcZpsPELc4zCL4qM47VJknya71F6c0DRVdtuZ1dSXUFILQOa3gevWHSTZXezJTCNK4mCcWobA9HMd7BPnFq8lU03PXC+frxR7EEPKzaqQ8WqiPlf9lF2yWV4Zu20fLnyzYspmVm0YebWyLT1aLDpajLZ0UHU7rWR2p5Pg4L2h1q1GMO78cN4HB3TF93lcieomNc4m6RoH8ahieambTggSZVE36rHShAuTYE3QB4nM8ma+Qc/yvtCdC24UaYvmjWQOPYMZSEjNQCwJGqHi6y1K+a2rZ/v1yeoFNV145xkXq6f0Oj3LxqLUzraNGT1tYsLR3kzjdX8RVlWIDpTQ60Seccz6bLSo1bsiE2SYRtU8SKnVKhRou27Eorw69SqIrZgdnENfrBwF4ypT2hJoMJiXsxbISUWhZSb3VzcPharRC1OWom2m72LpcuxQiUex46Gcwp5brhkMRFl23CfusGCd2dW7ehRvyLgzt2U76ORqzU6PiYXjNTEIzrqr+KNq41XmD4Yytd3AoC/qYYUHQNdypZ4XUTUdBKXgExn1sFJ2d2fHIyISY/ioyzR6vQoOWN3J/AmWImPv9OGgJjFSHa5lf7aTVA9gl7i6BE7qJdillGYLXuXFi2JBH+571O2yWdCb0prpS/Wqr41o6xVseD7GU6/wai/zr9cNUOxe7ZeYfUOwxYpBsjPOMMhtuoxPlSqzFnU2D/wyvCEbI8TEWTiUO0XwbFG7zGRtM60B3x1XQbRe1WptedKexntzXgObUEzfurrC7hTF8tTdUYsQkZ0jt12CS9qcbkm3pv0bJypSXkbyEAZhxEZSwBFKulbFmisNUVowO9k0sqMuC/vBAXsS58qDVpGdTVa6Vy2YkInPsacI8xUqRCGVeDSFbjYBzUVXryKpeKY4l8NJxRGfXOO8unAMG78hvWOgfUmmC6nxEuSEgka8RquLp51Wi0SDz/l+V17zQNqbKWPpnMdZ/G1d8tc+NZGQ2M1gxIjhEmmCnWhtVUUvT1NeOZg8RYrJZluzCmJj3FUcavbGMf3eXUNQb2Cho3sdpZL5YY+rAZKftjM0cnJEJ3tfVMuk5lyhaalS4JFyoVfMmecFnsiYpYk2qB1e+f2COvBCkMveXO8UJCR9O7XDeHEYThA7sYgsnuZdT95tT5sA2Qkkv1G5zrXW0VnEKoDd2OYSrqSryLkmLEsg1+WGTUUBmAPJK/3SXTlmTKbnfVxvgbJv9P6cnxg3xfUjXhrqguDTGhGYxqL5ao4OTC+bcnxAZ2lCHXaIHPFCHO372uUvGn1bHulStA6FsC19rAG3aRmVJIuQFy+U0mgWtf7FWeNyH0erpS3vo/M0ynttKabGBSc3JwMJDEF0mi0h4XNFC8V+ZkRePRdXnVdTU6QgA/7m1LvqpDDIYFIsp+ZVnmPMTtpglrA1NlLDxwHFrxSWI7ZMyp4Cu9oZw5px9+nhiG7yTUTgyzOtd3ZcYBuyRYXb/Lo7Ko3pXMrTktMF3neEDWbeCH3DnyLnsJ/xN0WplnHlLb1muiaWG12vPePCGV17MPLrkMXM2YEt/9xEUcbBBuZegMnNVgi1fbDNDt6tK1U1ItesXmWmwMdmGPoUW8pAOHQph2K4UJ/RPOdCkp0uRI1GGGrqbZMb0nqkOb1pCO6DzXl+xGWs0K9qV6vHhX2J9c0Fi4YgVXg+FnZsEqc654ZGh4WWo2i63M6Py0HI5o5fKJmpqycS7eVbxNsLadjuZ+VNAPJljmv1sjpu8dvB3e4Sw9yxl+XNW1Fl63iDbjgqeukV2VSmbSEmgiQY2xW9DRW/7q7SzXTRLaMc9Bxmhl/LM0FlDsEJM5prPkv1681JWxeTvPSqchx/NNN94/T91Gckds9nyZou1Zlpc4XWHazLCmO0WItFlLeYtkj6Hk+ba61szodE6NU4WRRylcgMNgV4uQpkZ9ptbTzcLCv0vB4akzm7psLCukq2XLPVovmQD6iwOAnEbRdcZtNYak/M0fAJ9bodtp46Z7J4re9C8aT3gXMqt66zMJSwcw1HPGTXDcPTVJxbyiZM9pt9Vh/DmpP9KdWZ/RDpJllftRtfxLvE4bRE19PkVK1WgzYz6NVp0XBBek0PveCS03IQLT+U3XqzPpt8fZu5O4wgmkDf9qtO7yO5nx+m2l47nkr/SmbnIlx1vWufe8cESVMzyaDo1aleTwdAyYGxdZtO3gb7zdkt0dV1zyiAPHK9iQfuJpmSOcjctRae5s5qodNRSLT8NBoy2OPixNmguHW9lcHGrde9f0GhyvHJd7H5imQusYUHm60GjKM8FFPUmcaudizyOR9jSOQ7tifQJzaztPDYgpPPV8Rhh4lKNwMMFRdhuYuEomSaOY4MAU3rzZAilwLL1pv1NNl6nrwm5AgtREnGutirD2plkSdAXtsVa4ixK4mgiV12d5K8MPDn0rlS2Otiz8w35VEKfWCbTRUIi95eTi+7ZFdzt2RXdHyFkiBbHZA9OFmH3XUdV4UHQwdl922A+WeVby65chKExFkoxyqjl5Zy2uJlle0v0plo9+v2rBZm3oAZe6TX/C2Qp8aVXPna8qhpsbv3mTyq4owauMJpqXjj1MNB3+oWZ3gbTl3om7Xqu3yYIKoGNqHr2olEa1ouNsSSaS17ZjLEzY3KopW9dZ3sbnh+s7ojqgTsxgxb4M/qAe7CfGUZHM5x5PfGMeB7SWSibQ593Zn0ZeDJ4pKgq1nWhFvLX/bNcIuW9myhmLh2aTUjOfROtVpGc9+hZX3d8166T9Z2tgXgUt+Chi1MiU0Yip8RRi7flF6glYHYX4euEk6xmMqBUhLY1hmqayZz9rQgCpY/NWInSjlFnRVE34MNDtuNsDRZi2647JpUa2KBi3kitKeILwJ1uSfsdJ2vl3NhRQWsZBvsro4t8aJHrRTapiPPW+JILXnR91g+wsJuVcBNKIJuaZnCTO/msJkC9xLrcqXM3BmH4UZjnuLct2YnDY8k3yU385oXImuZ5Ry9dcv9NtWYw+y0LOJjlvBG1Imls2uWuDVvZkBbr/ew19gNyCI4Oo3OLyDR2GuTtLD4GmBH2WGQTbLstmWC6byZdmBAMpTYKP3hGttLUTsnq1tCSKh2LY5+IYnhZRHou2W40g/mXjE2q41UNIhdcgTSRcshj6dxJ3MOwSJ5Hk6vp7NdsmaiqhceboiYdtin6pVe6puanZ9lhDc8y50vi/XqfC4zyvAX003LaGs8d+PhuLWMaA7jvVgi27WmJ464Wm+JKdoGJrk8ZcZFC3zamV9gNA77VRHM3LI8LldLqSZPsKeZYe2hvgS6k7k8Z3BzSpMFeh6DG/AbX40vBK9f+eFGyJrQWQqA3CDbJjYsuiInhE4xLSp1T/EKRwupvrT50LnD6dodqNDMuMw2ziipbTZ+UvLldDEUV4ssY/JyijzRRzZnzG+rGRCdnWO7x6iHSeUV5ArXp5Z5bqctXcV2Wy0ZphXFEi9dlz265xtpsC1VzW81fXG26Eq5rHhJRO0gtZwQ5hSuZhWWzrEDJ8lKQZ1oyENFfs5K0MzSEt8S3YXhj1hhJOJsyKOcuDKStYcs5saYxeuAPhNeLwEUT/j5gmYabD4tnN4jhFlTUsxaKZasJcwuGKwYXW0jodrOUD09BLm2p3cYYvu72w0Bxxm9MYiQRqf1lpQPCwShXddjODlMjHXCnJHp7kxQC4CxdJNhrEKwMCZiqRAu1pRzsHKn3fbsCiW22NVeNup0YYmHeouc9upyHlFrktTnXHHD8lgTUpFanFQQZ+2SWB5jr7tkBY0mTosaYs46y+2icWUSxoQsHCzNWhT0Igekc77KshOYtKrx+LEua5+eBpzEXvTshnJyptvuTCgEyM/XtvXxUlHAoItH0ROra7Nrj1epIRPr2BWOtBUsURQqyLXOch77sCm0FpTFtr5i4d3MXmbWeWrpUwmhum4WkdzZ3ZkItw/mK7ZaajZx0HKAO8iGMhfilToHdbeqeM7qWzu9YNer6Z67mYkyWH4GQqoNmeAMB5LEF5R32bYcdx2cSifWOwTeobkQSbivSOaWFe1jiAYSXgmM6c6ux3q5ERbNAc/tOijCU9I3WdZIczlagjr3NeFWGuRNtLADLvtnXp2y9NYAW7cb4vVQrBfNkQR8c7jlAc2eJIxmp/P5emO3HGvMjVW5wKbYyj4n/u3i304Ex/rljt0zwsI/UtXFCi6IXW91HeAb5drBhm1RE0q7aXvblryNm3V4p8MB1xWmRXlBppd1iZ7w3fZ6FmJvPETYVAN1YNZMBLvJQG4zm9xZuN3kiZgfYZQwax7pksPelOfMxZKvy2XooD6h5YTNTlWMbEUTyB1bXLjeN5am6jYhe6spQZM8U7dn9BEHwqwygqjEV64pi1U5P+eDPBdT6citEkRbcecChdlz4U9Lcn2gYlOg1cUyZjP7lp0uJIycAUiCb9BnizhqN7+RrmclioiZLU6niJnU1ECrrSe73sl2NWuzRDwGyMmRIeYgYaPz9mBaJTJdrYRWPPp4FbU0RS/ro0vB/YN4wTybEZCpft4wu+C6RgKpao2rb8/Bpmc2s24uyYtiDzHnkbEnCKUyPfCWHFote4S9R6siRpKvfT+dW+k17FjEWx2PM+usNx0aoWSRYSbhwVAQa4AN1+MuJktIgJciEpplMNsQh3y/ynen9aXU0I70KcFN1bKqHLS1hsrWXNqyG8HVGCO8rYJSydwlnR1OPbj5jJzl0x1clZsCcNhz9tzfEWq2mGHztTvdl/tcoFJ0O1yWcrTPY46Y6rRbxjkpgl4v1gO+ETo0FiK2sQfFJloUuNzW0zNFdCRSNY5Y11Na4QrOwaFSQjSusWsg8XY7k27Djh2OhZNemlTaXanwaEXTTpPNpkYkJ+dI/Cz68omDjUCIsvlG5WfpecNpNbufudNNLe+8fc7E1HDGCaIFDUZGah3TmUluV2LJHrbejUMBbdXThc9x3I8/vnx6GY+anwfG/+x74PEQ7//sLPFx7Pf22uh+WAws98t9rS//tEY/f3qpnBDq8zgtrZPWfx4u/o+z0s//4F3DOLl/vFgd3211zduhemP5418EvYSZ29ZN1X+r86S9H9Z+erHbevwDhfrb81D65W5SWjxOuJ8mwOsgrMC3Jv9WgQZevYx/PTC+rQFuaDVvt/7z5BjO7KFfQqf+hlPkN1AVo5HPVxfQNux19oq+/Pbf/+JZnnYlAAA= -->
