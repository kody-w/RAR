---
name: "rar-cowork-cookbook-dashboard-establish-support-procedures-and-policies"
description: "Produces a self-contained interactive HTML dashboard for establish support procedures and policies - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_establish_support_procedures_and_policies", "rar_sha256": "c9353a2bd73b351452ad841945bf33640bbd3508feca99b357d30a8e7702a99d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_establish_support_procedures_and_policies_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-establish-support-procedures-and-policies:082a24809b94e6a59f68c3ddb2f16e65fa147d92cdc13b17f6a9972e98d098c7", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_establish_support_procedures_and_policies`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_establish_support_procedures_and_policies_agent.py` is
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

Establish support procedures and policies Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for establish support procedures and policies - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-establish-support-procedures-and-policies
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_establish_support_procedures_and_policies_agent.py` and embedded as the fenced Python below (sha256 c9353a2bd73b3514…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_establish_support_procedures_and_policies_agent.py` first:

```bash
python3 dashboard_establish_support_procedures_and_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_establish_support_procedures_and_policies_agent.py   # or on stdin
python3 dashboard_establish_support_procedures_and_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Establish support procedures and policies Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for establish support procedures and policies - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-establish-support-procedures-and-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_establish_support_procedures_and_policies',
    "version": '2.0.0',
    "display_name": 'Establish support procedures and policies Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for establish support procedures and policies - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-establish-support-procedures-and-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-establish-support-procedures-and-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1874609b20a9d64b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/support-systems/establish-support-procedures-and-policies'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/dashboard-establish-support-procedures-and-policies', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DashboardEstablishSupportProceduresAndPolicies(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardEstablishSupportProceduresAndPolicies'
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
    print(DashboardEstablishSupportProceduresAndPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8166Zei2Jbvv0JHf6iqNjMYBY27aq0HiggiKoOilXdFMhwGZZ6hXv3v76ARkVm3bnXfoT88c2WEwDl73r+9Nyd+fbLqKkiLp5cnDVgJIlhRFAagQKzERRZpmxY3+Cu92fA/4qRJVYR2XaVF+fTpyQWlU4RZFaYJ3L4vUrd2QIlYSAki7/O42AoT4CJhUoHCcqqwAcha38qIa5WBnVqFi3hpgYCysuwoLAOkrLMsLSokK1IHuHUxEoNiZGkUOiG8+IykGUhKSBDe7xG7SNsSFJ+QJEWWJD1FLAfyL5EEABeytXukCgDShKAFxTOUF3RWnEWgfHr55a+fnkL4/enl1ycnskp462n5LhT/Lo/2EGf/IQ2buPs3WSC5yEp8uC/rof0SeJ2BAqoTw1su8JC3qx9HW3xC/uu/bq1V+OVPL18S5O3z5Wn8p9bJXcwqtcoKSu1YmWWHUVj1zwgbtVZfIgWo6iK5GxaaP/GfHzu/UUoz5Ofx2Y8PJs8+qH788gRtVVijc748/YRAO395Kurx+/NIJfvxp+cohYb58advdMravgKnGolBqZ9f367fyMKF35aG3p3rz5DqIwxs8OXpO+XGz0PuUU+48+n5mobJjw/C0MENSKzEAT/+9GdknQA4N+iG6h+i+8uDcAAsF+r0JvhPn+5G/isyeVPog+afs82gW/8ZTeDyd3afkDdD/Rntu/3/hnQEU6T8sPjfJff3Nkx+Rn75U93+uw2fEO/L0xJEMBkLGObgBfn1Vdvzi19+cL/d/OGvv0HS/yMZLa0L507hNbaS0IOZ/Pr6yw/l/fYPf/3lhzqDsQas+LUuor9H8+/Z9c7ndxZ8W/Xj7/dC/kZyS9I2QT4iHfk1zf6j+O0ZOVpR6H67X74g3+fL+JkgoxLvTB8m+C5nSijrd3b86ek3iBgJ1KZ27o9hlv/nfyLb0CnSMvUqRHPSukKgg6swBqPwehCWiP6W1F+1jSjLz7H7FYF3x3SHEGHVUYUIhRVGI+CNHh81SD3k6/9x7sALIfQBvOgHYL5+gOXrG1i+fgPLVwiWr+9g+fUZ0QMoSVqEfphYEaKy+z1i+SCpRhnu0VLW8edmFOMO0ne51IU4QlBZR+AvyNd/ge/rncVz1o+qfkmg7x5FoAIx3GYVYdQj1ohldl+BzxCSId4UaRTZlnNDxh919jza7xSA5M2qDqxLoANOXQEkSh2oixdCGP8EA6NMI1hUqtHW5S2MIsQNC2jItOjvlQP642Uk9vXrVxuq8iV5gDWJPApXicIFHwIjnz9nBfCi0A+qLwlwghT54dfffkD+L/Lf7boTH3nsYRm5mxAGfIRI2k5BYPbWMVw2ViwYB5Z79+6vvz18M0qXwEoLcy70xvJWjf76LlRGDR4Oe/cW1HkUERRvnH5vN6QNoF2QsILWgjhQfvqSjCRSuLRowxK8G/Gx+WH6d/c/+Iw+Kd9sCP3kFWl8X3uP0tGZTlq4z4joIR+WguqO4TB6NEjLCgY2LNEuSJyx+lrVNxcmaYWUMLdKr/+E1CVUdaT81YakR+PEEMCs6iuyXexhLUwj+GM00J093J0m4ej4t/h93IZEih9gjHHvJJ4RBUBrIplVWFlQWCW4r/OsR0TAGvi+HxK3YJ/QImMXAEYf3bP+Hnn8P9yPiH/b2Hz0EMiXmsBwCvn/vCka1WUFQeUFVueXCK/o6vkRm6Ogo6ke3SHsRu5S3RPtW4fyDmbvMP8liULoz6L/y2Oldw/Hx5oHdELxXYhEKvJuiOJON6xgUI1RUhSjStaX5L2efIKWgy4tR2iEuX8bkST9YDg+fZc0gPYbr7/1FsgjXkdzwUxAshoa1EE8aIh70lRBMabkm6dghIExPWEOOcHvtEIgdRg9kD4ChQhhqMOaczedAlML9mOPPPlYHo4dW/ZwvIvA3APPyGlMBRjOJWID2HaNa6AVfriTQmIAbQxF/LBwGVjZQ5ix/X4T0Bp9kcZWBb73wNtDGNZj4YL8PnIWUrVcq4K2bKETYEp2D89+yPnmKyhsPObPfdPv3f2mK/J94fvLmLdQxm+VBE4MY8/wnXEg2BfxI0xhNb+VEBli8BZAMBLu7cHzo8I/WogPWV7+MHP8+M+NJfeabfzecy9IUFVZ+YKij7r6XlafnTRGYYyEGSi/ldjPH6n3+S31Pn9Lvc+Q/+f31Psdq4flXpB/TtzfkXiL8xcEf8aesfGRHDpgDOS3D7TO4jN3/kyNT78kKvjm9rfYGEESAjfM8vda9b4EFiy/AP64+FG7yrHktbDK3iHzXns+QuMtcSAiJ/5YaMv0u4QedRod/fDjB7TDR8lYNNyxifTBOHBFo/gleHpJ6ij69JRYMfhXBq0RzmE0Q+uM8xp0BmzSqvERvPpo2MaL3w+k95yDYOGmL2PqwdIJm+tPyEef/Al5n1zuw2FSw9Htl7FHH1nCpfDXx9qPadcGT3B2rPps1OQxjo2t4VvL/kchxoy7h8/YHKQfKTxy/AMR+MX3QfFHIrv7Fyt6wxFotrHgwjr/lv0llNOFHdsnBPoSZiVMNIifNdzwRzaQTwHyGpZ4d1T3m/2+qZU+dPntbobqMdP++vSOJ+P3R7/xiKNx3v032sTRyu/l/XXkZY0U783c3ej3NvkVKhyOZfy7R/7Yk7w+IvXpBeIT+PQ0mrYIYe8/3Kf8p4eAULNvDTakAJHmczm2JShMNEgJNgvZqNUNouR3DMbboXtfP355+fOu/B+HjBdsRlgENcPm9pwCtDWde/TMIV3XJjycBvTUs3CKceeE4zo4aeOMR1vzOUOA+czF5jOHgXKN3o6tN7lQfPQT1OjDGf8bw8PTgySsQ8SUhjSdOTklLcJ2GdImpzg1JSx3RuFzamp7JElTmG275BSbecCB4sIljEti1gwwDEbAG+5I761Xfcj5+j4XvHvuASavEJHjcNSCsCwHqotT7pyxaAeQmE06ACdwKALApnPSm80ABUbKb1vfvDc692GKMdRhmwqboWbk8+tbNIzhS1Nw5ZoqRfbxWaDzo0VTjN0F5qSgwXl7nWAxFhoUfclSUpNt5VJ02LIUZNsWFV8cJNbRLrtot1STWqjw0mCBeJucpUlETm+SFsn9JGMNq6Vu0VD2F2dAvd3xYKiWMthmYGkyHtf5LT+q1QnXUh0ct/JghpcSS4/bbE/NCh9La+tyO4KF5+373vZK1vWK456nLww6n4UVc8zrWQ/8A0ZLZ/2qHIVwKt/07XQvhSQ3Bfml3ri7i98fz5Hm9wtg45GVE2VF+7diZTbtdIaibRIKk8EoAifobDuLLiF5jlTdTNPpOp0r6+uU9vZDNgcezSb6fD7x+nUsk/y24DOtVKjz3Mqj+FIAXSryYyJspszGz5hAmK/yTYznrQ6uh/yMF4zr1Skun85hy6m1NYhLMlliqOfQi1WcyccsP+/1s28qzm3ZzSuwiE1jy/KnotSqi5VfRHMjJ2sr35/pk4/PipxnJj7lmudYi6aRXzm+4bLR8eotZr5GDVV62BnZ1PVD9+Bw5/yoxedTIReVM5x2qNgaG5pUpZpjT0k7kIYU6fjxtpk75elUKRUea6tc7rMbcyEqNZwG82ZiCfiB2N6obGG6WxAuJ0SgBMJB9qb56lSazX7jWHKuzUpLQoliqYOwII/W6XBLl7P50LVqtzTF2ZSy9kW+xrcBaBLtaKNF17W7g5AnbkzopybqFklix77bkFG/l4UjrUYWSoT+arJJbuczur5ePXlzmFrH2GIMlYzmPnBNIz4vT8K6CvaMtR2U+FLmG7AxTxfqOifmvNzeruRipcp02Wnr0+zqV0YfRFHq+ZMz6sIaAvW8bq6EN+gSs93vE+rWVZeGFaH8c6tVKsK3LzjrXSq27jcW7QXhsiAnmqHEXtMRvec3XrbzSqwJPK+d5eQ22N9KlNor6y2BevmaPrnn9RIzE1uY77Cwb7PL4nQCeCH2INAwyaTxvLRkJbRPl2teVibXyLV02G7j1G19V6xg767VviQrJ/nUbdbMrtlyzM7MdGl7pm9YvczWeJ6ZW6HmL8tocwsWneZIO2JLiIEYYBXEP9XcnnC7z7PMcgVN20kxPZ9yNYd7K3OIdP28aXb7W1QkM92WJkl5o5YrSQkSRojoQZUvE1q3Z8vehLWTUvyIRK9eD7DK3i0aCqDofksyPpHcuq3XTbxg2AkMo+3WWKfm04xarW11U4eidtpKRO8oQRpaE7LMdGPezlzlAgKdzOPD1YwnN8s0DB4Pj6zM9eI8a62sEEnIn2EWaTELydnmvK22ksRPefMMbVpstxMc5GQmlY2+rab0zNKTG7Y9SufJhbeUGyFJxGopHyn8du220cq5UbmIK7IGRJwLWDIFnnHa7Y16GmWxXJVBg56veRPO+a3XSEf6dotaH5t123DJrczjcKIImvD3oYVWnCBP9nteyRcrViGyPDmZq2S5dMXM7/spF5fNAjNa+wQ0I2sUS76R5Xm+EbbTgNyCdJYa2AXs6d4utduJ3DP89MaogORpM0DNNmz8w9YllMTgTsRMxBty2ZpzSc7SY6LXLC5TBzNrLhOFXInEUkHPPb4B86VgkKvjQagUxd+w7BpPY8HcZst5mXJszbKXHdcRIsnLztmfuN0Gu4nxRFleBK+hOeoCsV5NNgUAc6B3/TwMK5E1ZCk/54V8HmpBb9ebzTbaZLSPLWgXFbfsij4tZadetZzoRBHleJxhnmRhlRqUzh3YJc9qPZFZVHzk8uBwPJaL04zaDQtDNTZJQAkQ5Dlc3/pjXjDX5IqborK54SllnU5MdJsPpb31diWjHuhzd0tMkpnshhl9rgbRv8EtGl8o5T7FUmy5nlRaYV5ScskO2DU9ub6H0r06FaZMUOGK6MLq0djmMNDoHDvSaMegYoPOyvmBCa8zozollyTpqoIvfR8T9qtd4U9Dvqk2HL/JXDnWjRVfc7P9pDytV8Z8t2oXRW2XG5UdjldLEa1t3K3jvSkah8jWqsHl9MvOzy6nwOQ2PpDko6amk8xL9KlHFIay01H1NGsiKLE9JVYbRbULYcAYhbw6xFrR1/Qx2Ihd4qPQIDOSmKWCcfR4Ig3repXoWLyu92HQ+HIuXJpTJLOphp4sp70E+Zaxj6FIBI0CM1CJlwE2PR7AzVQIpb7Zpd7tWb47XNj8qhFTiTfceZO6pVyLC0HKISgQhF8eBLNMFtbQ6YBjNrbqJp4S9TY1vwFCbXlsi3GsQBIpqovOgdtS0ZUwKt3WlyyTUcqiUCvV7kOR96D1dK7BbqyGb1ZKujXdFU9Omo1dGm3gOqtlJ2GH1ULIQ1E1z5eN5Mwv/rHp46GiNd5Z7bKzdGhYsgNxbx3Dsl0cLnW3CoL2qI/elBqXZoycZvOduD2vkkxcLURdqCdncuW2B/3WTa+GJV13eCRdQ1hoZ/OllQZOlVhHdHUyO4vdXwTsqGGKOGlNsDZKPgzp9RkXxGVOXgginl9wbsn4bW0L4oyoaJfP9mot4VJYLBN/qax8sWKw3cpbV7BRC+by4piEO4ZtePxUH8Ne4nmYgRgl+u2WbfmzrhQ3rxqqTJ9gknV2aY5ME5RcVWHuuAJZWzvN6frgtpHCGT1l11drrm+co3MAi4u81+cK7TToRQuvhnDYzRdgMlCnoVhD6JvTazOkO1do5Og0SY7MvuAMvcP3lWs3ZnrdYfSeVVkZJKQeLo3LWVj0LBEv9udrNJOpU3AGDOdc9FBog3B/C2ALVE5SRi0GIfTbyyZtdzl3rsDyMHW5IVicsLOhrqgyc9o9V+Pi7kAnUWPMN/T0VqnYdmDr1WLovHMgsmeDa1x31pfSnneYs6nb08WyOoFU18glHNhlqbTnB/1ESclCFJTgtLgdzsxCdB3ihoaw/GmdflGENEioA33YXxwDLdusi6lklU+mVeZfYrn30SRY+VuDUj1eO0joVAwgrImxokGwS64HfsKbR73TjX4qtbD70sUITgbcxrKP3erMqp0QazwVObCZ9n1G0XKsbLJTcah6Z2qEGVP2kaw5kdm3ccxXaLdR0bJOwuRIDFk46Zx+zQRDfwFmcVqpBt7ZF7VRcc7dm81OyTuC1szZKdbWnS1fcFyIjVUy8GStRWlMesSJPq1IehEA1RUwqRkCpdt4iR+It8IJWj7cbZms3nB+HB+jjUZElX222NrCKF5n/eOcrNE4XM21FK/my6K21tlkt5O7A3YOeXcduBq2DfyFfyz0an/b1APr36yzJOxY+uDX6Sm3ZQ0D3CZib8bJMZTt3qGzPMRdfzJEdrsPbiIqMLLuOG2PkQ4/YBwabtN6d70Qcq/KeXJZ5ph0IGP67PeC3nil2HDW7saku+5qQJwFfD29iVtQAc44E7w/XRYGs9rkzpByyUI5XI7FbrLmKDw7h2jigwPLs4SGkmJjQRgZ3DngtWBpLNZ1DU6rcF5KOzDPl02RS/igMil3ExRYXXbObL8reu+sXnL1rHAHT7lwrVLyWOX1qs+JsJUUy0Q/RcRmmx98a2BFge3Pi0JqWbct7bVFyNJyfxMp+WhRmGaXnm71XH6orINyXHd9NXNb+YKBoVmLbC5AYXDBps51rQXt5MpJhLxZtqc1a2vETgD4xtJmYrspN/WJAX2a6JM5BL72dC55fdbMYgdwKo53c9UYwlxicdXstGMzMQUhcbkNPTH41XVHpEzMzZnKvHohBppuwlBzwbYaW9Fvxt5nUCIvk3oWcye8m9Vm3dZyek7c/tL51A4OFvw07stVG5mNztuWq+WZsnUN3BfC3qN2NbsJe/vKYTxhVltQ00TeSMWk3ajG5EaX04kX8tQCnZC03S8OtUTKObGRGmVCmxOfZZ2DzEm1VnIQjJyTKhMb83g8p6gW4JbCdp67rhbdGpY7t9FPVhKkg8JIxIwKBKJFd+mUbBRmSub0sE5ns1ODVjiOtit0UbR8UjUoFaANnNBWjXtGl7JFqlodeAUnYM3tQKoyh6+8cE7HRniKTnguVi5NGGi6KaTUV+oGKKtDki7VazB0glLvD/vNeeCqVTesL+WQ0uT1FkcT5uZtUV7bHhXTLo4YWAZ6I1mLKbNMeaoeyHi/u9RBqAvkoWzLlJlcdWV+LtZtp+1OMjFn3el+IgaNU8MeRJw25kpWB29dNNV2oq1lAdUU6ZKLiqG7MMir3ax2hEhUqWZqrAiMARoP66eFd4MrzyoBFdCKmmkiMI7DbKGkXK6Ka9JmbPMwwyXSJvGtPrWmbt7hh1XMr/K+tGOLqJqLYU6wDJ9QorSXcRV2cqSDO8CdweBYnENumA/ZxFP9hFzI2Vk9D+DQy4QpqtspnzaqQNEkp/L8su67+U6tBoESbZjRTr1R17R/7fC6dCA+tZYUZEubsIy5rwmS114jpeFjB3XUaSqwVUoAXh3gJNlNbIB6NUmhV2JN+LuM2yyoPbO2xWrZt/SB78xW8lknnm3L9ZVtCTndZDbq3RYr+nrm4cSDqqZmYeawaOqMZGCz7AZu2Z6ovpiAckVI9YVRz3M4XHjH08BRdr7c0XjY72fCVF81Rb1zk2NfkkpNsk4drQXY2Z1tVCy5gsP20dLAKLlcxrM1dzH1E3oe2OG6jwvnRBMHAU7t9vpaFEKtkweaPpInMDWwGYm7xTHFcK4JY1PHnNMuZYDMwYlG2izTnUf0fkVf3U5esr0PqOnkKItzSyy9dco4fF/Q+bpS7GU7KckDRs5YQLkNyBeU3KzdZn5wNrO9e0Gnpp7U3nJgr3a7RN0ZOgkPMGUA6QamktjnyqvltV7ZqX0hDp3CTgZGGOx4UrHkoaiIK4km9s0MRGaoz8OFjkjq1iahXG82HiugnGG5K6Vv+kb1pzRuMoK1EywBhV26jAdeF565lJP0uiio0vGY7sgrwjSQEikl1pFl7nfVPM67/VDBCWmdz1tROgLy6nO04CY+uzTO6wWQFqaqxEy8Sjn6smgOpL+FQe41uuZqIFhjzYqVWV7du1ca7A0eDBEFdsupkluz5YUOpvwSSzcVz1F1xZrxTDD4o0urdlvlXLKMRR7XZhuhXx9V+qaItuFU3Akw7G7bpAfdKxhOQr12sZnKG+pGycwCth+xVDm1SJkTIqod2xFkjwBF0wspserlxVzuQ7rqGNE+ekTG5Ut61c9v5JU0Z9h6R1+c5bUV6MEVQqwDZ4GPrRDnwmw669ojdcsWvd5xjYLGyyu9xJPd1u3CHUqQwda0HHBF26Wd9jlrhSnLsj///PTp6X7u/PSCY7Pp7NPTeMrwdlbwb75Z9ocwe30jTjIUpP2/90rz8Xrx/azxfnQALPflzv3l35L7r5+eCieEMj5eT5dR7b+92PybV7uf/4U30CPB/nHePh6cdtX76Uxl+fd35mHi1mVV9K9lGtX3N+bQP3U5/lVO+fp2lPF0Vz3O7uci7zLA75Ybh0kIqRevVfr6OFsAT+NfzowngsANv136b8cOkEAPnR065StJT19BkY36vx2FjS+Cx7Owp9/+HwCKDTKoKAAA -->
