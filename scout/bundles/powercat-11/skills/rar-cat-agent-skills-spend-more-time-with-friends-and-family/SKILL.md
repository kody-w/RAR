---
name: "rar-cat-agent-skills-spend-more-time-with-friends-and-family"
description: "While you're out of office, watches a group chat and answers questions from your local knowledge docs (clearly marked AI-generated), logs anything it can't answer for later, and pings you on Teams if its setup is incomplete."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/spend_more_time_with_friends_and_family", "rar_sha256": "ae5c4e43c1e54091d9c0fba127f9b7f077a61289feb638570df2aaab146c313c", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Adi Leibowitz", "tags": ["automation", "teams", "out_of_office", "knowledge"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/spend_more_time_with_friends_and_family`. The original RAPP
agent is preserved byte-for-byte in `spend_more_time_with_friends_and_family_agent.py` and in the RCI capsule.

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

Spend More Time With Friends & Family — While you're out of office, watches a group chat and answers questions from your local knowledge docs (clearly marked AI-generated), logs anything it can't answer for later, and pings you on Teams if its setup is incomplete.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#spend-more-time-with-friends-and-family
  Upstream author: Adi Leibowitz
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `spend_more_time_with_friends_and_family_agent.py` and embedded as the fenced Python below (sha256 ae5c4e43c1e54091…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `spend_more_time_with_friends_and_family_agent.py` first:

```bash
python3 spend_more_time_with_friends_and_family_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 spend_more_time_with_friends_and_family_agent.py   # or on stdin
python3 spend_more_time_with_friends_and_family_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Spend More Time With Friends & Family — While you're out of office, watches a group chat and answers questions from your local knowledge docs (clearly marked AI-generated), logs anything it can't answer for later, and pings you on Teams if its setup is incomplete.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#spend-more-time-with-friends-and-family
  Upstream author: Adi Leibowitz
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/spend_more_time_with_friends_and_family',
    "version": '3.0.2',
    "display_name": 'Spend More Time With Friends & Family',
    "description": "While you're out of office, watches a group chat and answers questions from your local knowledge docs (clearly marked AI-generated), logs anything it can't answer for later, and pings you on Teams if its setup is incomplete.",
    "author": 'Adi Leibowitz',
    "tags": ['automation', 'teams', 'out_of_office', 'knowledge'],
    "category": 'integrations',
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
        "upstream_slug": 'spend-more-time-with-friends-and-family',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#spend-more-time-with-friends-and-family',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'bd12abb4ba09a5e5',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Scout'],
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'kind:automation'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class SpendMoreTimeWithFriendsAndFamily(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'SpendMoreTimeWithFriendsAndFamily'
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
    print(SpendMoreTimeWithFriendsAndFamily().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916Z5OjWJb2X2FzIraql6oU3tTERCyScAJkkEHQ1VGNN8IbIejt/74XSZnVPd2zO/PG+2lVJgVcjj/Pcy7kLy9210ZF/fLlhfNiSPVjp+jjdnz59OL5jVvHZRsXObhqRHHqQ0PRfah9qOhaqAjA3yB2/U9Qb7du5DeQDYV10ZWQG9ktZOce+Nf0ft1AVec3k5wGCuoim6TUUFq4dgpd8qJPfS/0Ia9wG+ijm/p2nQ5QZtcX34M4+XPo535tt773wydwTwi05EMbxXkIxS3k2vmH9qkGCgogFaysP92Vl2BNM+mCihw6+HbWQHEAbmqgxm+BlTE4zt0iK1O/9V+Bw/7Nng6aly8//vTpJQbfX7788uKmdgNOvexLP/e0ovYPceYbcRsJdQzONFzuCXYWpwOQkNp5CJaWwEAQtE8vpV8DozJwyvMD6Hn0sfHT4BP0H/9x6e06bH748jWHnp+vL9MfvcuhNvKhtrAb4DdwsrSdOI3b4RXi0t4eGqgGHtT5FPGmrYGfr487v0sqSuhv07WPDyWvod9+/PpSlFMoQSK+vvwAgWh9fam76fvrJKX8+MNrWoBAfvzhu5ymcxLfbSdhwOrXb8/jp1iw8PtSENxv+y2/eOqqfTcufSD8N/5Nn4fpT3HPkHx7LP5YlJ+gP5c8+fM3YO+jKB0g98/FghiAO19ekyLOPz511MXVz+3c9T/+8I/EgvJ1L2nctP+U3B8fgiPf9kC0niEB5Tml4CcIfvr2LvMfqy1BwfwrnoDlb+reA/WPZN8z+3ei0zgHbfqWyz8V92c3wH+DfvyHvv1PN3yCgq8vSz+Nr6DunNT/Av1yL5EfP3jfT3746Vcg+n8Vsweg4d4lfMvsPA4Aonz79uOH5n76w08/fuhKUMWgzb91dfpnMv8srnc9v4vgc9XH398L9B/zCaty6L2HoF+K8t/qX1+hk53G3vfzzRfot504fWBocuJN6SMEv+nGBtj6mzj+8PIrgJ8ceNO598sAP/7yF0iL3bpoiqCF9u4EwCDBLYCiyfhDNIFZc0eN2gdxbWIQ2Oc6UP9ThieLAWb//J+u3X62Aaq2n5tLnKbNrJmQ7VsGoO3bJPAbwP/oW/BAt28ASb8Fd3z7+RU6APlFHYdxDqBb57bbr/ld0qS7rP3Gr68Ar5yh9T+Dtv48fQEYC/38T2r4dhf2Wg4/3wE8fsCgvpAnCGy61H+dnDUiP3+6BuAf8m++2wE9Dz4JAEs1n0AQmiK9AgidAnN3E/JiADJtUQ932SB4XyZhP//8s2M30df8gdk49OC8ZgYWvJsDff4MvAvSOIzar7nvRgX04ZdfP0D/Bf1Pd92FTzq2gECeqQEWrvabNQRarcvAsomCAMbb3j01v/z6jDEQA0gPAomMg9h/3AxKFTDiW8D3EvcZIynI8UGgQZCzsqjbBym+QnIAvdsLlE6XJqqIiqaFPH/KhZ+7A5BqA3feI5kXLdSAemyC4RPUNf5d689Obd9NzL5NrP4zpC22gJiKFPw3mXlfBG4u8hiE/70cHueBkPpDA83fRLxC66k4odKu7TKq7aeOwH7kBRDS2+1AuA3lfv81n2jYn0J175RHeO4jQew+U/p5yjkEiBzAgte86X4fG6DDnUbrr3nz7AK7nlLhAlYASsMu9iZu+OuzpJqo6FLvHj9g6STpmQXvmZV7Dd6HAWiaBqBpHICmeQB6DgTQv0OPgQD62mEISkD/10enKSCcKOq8yB34JcSvD7r5SJRb5O2U0MeMCQaYu6J7U34fat6A6w2/v+ZpDKquHv76WHlP73PNAxO7Gvinc/pdPqitpwP30p8cq+upaeyv+RtRAK+gOyoCd0DwpvCACntTOF19szQCYDAdfx8a7qVSTwmZmg8qOycFpRf4vufY7gVYVU/t+0w16AN/Sm8fxW70O68gIB2UG5A/xXQKJSCTe+jWxSMn9/y+L4+nIQ9Y4XUusDbya/8VFJJ9h/0GtD2Y1KY1IAof7qKgzAcxBia+R7iJ7PJhTFFf3gy0p1wUGUj1bzPwvPi9Z+62TOYDqbZntyCW/QTlnn97ZPbdzmeugLHZ1OX3m36f7qev0G8Z7a9f87uN7+wBCjqdhoHfBAcC5Zg193qcsK8B+AU67eEeqIQ7778+qPsxG7zb8gVacAeIewDlneOgj9kbe96J9vj7rHyBorYtmy+z2fuy1xC0dOe8xsXsD4T5lzuffZ747PPEZ58nPvv85LPPwODPDz77naZHUL5Av9tm/W7Fs0K/QOgr8opMl1SAEVMJPj9foC5/R6OPv/n+zN89P773CSDnBLOgfqZibSIAAFOcdP97gp9VMIE2gAxneGewtyWAxsLaD6fFD0ZrJiLsAffeZYMUfM3fi+DZIgC88nCi36b4TeveqXyCjkeS3pgGXMpboNub5sDwvgFLJ3cb/+VL3qXpp5fczvx/cuM1MQooVRDAacsG2gaMVm3s34/ex6zp4O83taChABJ4xZeprz5B00j8CXqfbj9Bb/uN+/4w78BW7sdpsp5UgqXgx/va9x2z47+A7WM7lJPxj+3ZNNA9B+0/GjG1E7DY9acpoXjvz0njH4SAL2Ho138Usrl/sdMnSDStPXE+gPlnaTTATg9MUJ8gkD7QFqCLADh24IY/qgF6ar/qALl6k7vf4/fdreLhy6/3MLSPPe4vL29g8czBc+oEy0FXfm4mep2B0gYKwfGjqMC1/+d59CkHwBwYhIAg2yddwidwF/VJAmFRj3WRwLFRjA5Yhw4QmrYpFGPYwHconCFpxAsw27YdlKBcHMVdIO9Rot+mWSKebCNZcB/LYgGBYogH9vAY4XkMxVAuSWOIzTo26ZCs7Xy/9QJ68Onww8Epmu+j8RSYp9+/vDgUAVZKRCNzj89ixqI2RdDOOnJgmgrCqlnaToausxaHDdEfqeX+LF+4627vOGbCoyehip2zdTnujXSzpuechMnbTAwslV0e61WXl5eLsp53mhE1VLDYbVfBNZA9hOf2SYzeLougtW1X8AcSDXGmjQeSrGPbF2fWkSXHzpLa6Hqdjcq1nSkndbFUGn93Ms5zdF7O7Fumit51lFtC6cfEsYVzpq7pIcz5gixza4Hh5kgd++i0t0yja71KFxr0IGzF0znzqlxuL3JaJWbDZ+6iIm6kSdcKKfbMLRgTN+bJ4iSXyUbDjIVBC/PGcqyoybjbyNhCTtit4OiLI6gVcplelhounDTLX9DEeFCI27DkkkV12xN5Y1Qo5scXhS9YiUxRGPavTgr7bX5gs9FBqRl8mcnnjBFi9GTEQHyqnQz7dHHppW6GmnTZnGardEVHRi9FWuILt8uQnBQC9JQnHfL5urxqMb9IkqI9mLhyHU+oyaZkGlz3twVbrLDS5xe0tEcIMnV73DH5c7PcM4poLcPhYEsV5QPqcYl2jV6pPLuierZj4v58kFPbzleixqg3tzysMnsQ94IJX5uFVeyVQdXI4wrse2AFXrf2yGjZ1Zh7K60dTL3KGeGCD0m+8K8nIwppdKeOK8zQPIMShFhazAcx2iMHbl/p1WFUzVkbVmbSzLHBTrB6ng34Bucr40qvZQI7zVpiPWSon64lnex4R6+qjbZSZ1GxpNo8Pif1Vsiu49hIMTvOWY1onSCgJENB3Jsv0NVGP+vX4LIyWpbdHGt4aRbI0TQzNne2i1Srm8FRut0RIx1mOcTbyuJMeFwEVX9usvl2TOHRpa4kcakyRV9FK2zTJkJxPjLJrIMxae41hm4QhoX56EmN5iSggqNSjdncGzumIhun3mwT5UgGmtfkN1/WrrnPJBt0oFUSTdpAxMfrMtMbxl/ke38f7M+XfSZpAdkstlFxptfbfheEnEMTC0FYIHDAGLXWhzLr7uvygmzL7aEWPF7LNlYvbRShKJUGMfYJYl9vazHHu26fSGhY9drYWBZpukR1MaPrOi2b/TIestGKggvHLyjX8qLZKbh6JCcdlHWjasRqLvqlelCXJoH2c1NLj32IelZoXw6L89HxFwxnF1Rc8bWmiMoWCwzZi3oz3Cw2874x7BWdj6GXazzTuzAzXqM1sZlRDDlIdSGHrrASl3K+2pFzkBDD0F12aSozBVuh6CycHYNTwxzsQDlK1Koq8i7yR9TcrBvq5kqzDUueD7k4P7RWFZ3LNDVX16VA+knVyqd1StwaU6hsd9vwwwUtxXG5xIr1GPl+dO7bNiwCmyNX/JwqKMQ+IvjNZS6r0Z+TO7+RTVXVgqtzbYOYTIXK3Iv61V7kKpZJl3O3c/fhkV2OVN4sW8fdr5O07+bCDJOv9lDv3AhmlWO8jw/7YhvqjMkyiJqLRFumoxhoMtluG0U/t4XWlTxct5s0QTJFhPXxxp/Y+dryS4S+VJZV7aybGu7mEpWo0ipqDHopyZtK1+wRndXHZtjQ5I1ZbfJTt2oFgibDdBd5/hzZqeeTcukYvuYRNHWR+EKaDpLrW2SOH5kDpcJ+tFxlfRg357FM50ovUo1kMv025nYnnwlha8jLLiO8Jtar9DxQxw1sXFH2ps8YANTZ9qopDlXJpVmstUW3I5fNqPOmskx6EVe3+REMA1IVuN1aVpk1L1VNX6hUpWAno6yCRE7kWOd3zfkaJA6Pm3Pe6914eSv3aidl2gKed1UvEAtbKzr8HLGD7vC5Urpl1ejCcW/tm4PGNPKYJgLOc7IVklV2LHGaro9lucio3TwZx6zqD5URepU/VxhZ3XmuMb96Nhs0MO/Pd4qVUlbUHgSDZDetgzRme0F5rvYS3kwSgTTl3VW+pjJWyOrqbJNI71ChPlonHQRb3coLcq+Vx17MWHQ4GcFKs1luUTGpNVtG4dFpaN4AuHBQDorMHGRWRreyoOXrs+ZI1bEMWHm12K1QQaXKGTyIYTzPWmytx6SyaI5r1zwmmtWjxoInetg7K0mugSHAuJT8AYwTjnxo820O/OO2/v4w31rwoERnV7/sdzsq7kJYJteK1phqX7Sn4TyHo33EHXH95gLeGYjl6kY0EiM6qKvmymU7t5mZTrqKv16omDr3xV0DizvcjCJxQ6IxjCXiapA73jymAi6y12hQqMVCq0x7mA+umwiimp5dI6tON7sYrXBBRik2N63TQnBrnhB3ropsm6rQe/Ek0j0KukqXvY04qHu9HQkJp0Rk15+usJ6qVjQcFpwhrrkC3606rDsrsKdsZJepLhVPXcN8e1EOFrLRYkVnyzUR0zpCHfFjxpoNzi2UcHmMOEnzopuRr3yKbIKjyh74dFVfojplCGTGa2vLFW+aYvLLy2JDRY1qZ/alMLjwHB/jlW5KGLapJWtjJ2sVNtlLuMxnKN7xymg6Znww6fVgIx18IHfV3KsWrEYfh10N37JidK3lDRU6CfWr8yHwOjs+Xy9FJe/JJdUkJbGYq6oNgPd086IuchNv38YtmfYHH5FOktUOrLWRFyyo2tOQ5+daVS5Oc5DI82prt5YZMuwe87jduNTseXbbdCvutD6OUWKue1ni/dyQTPJa8CYtI0bNYfmeV3fu0Oacs1sxNitmRuoVQlltbc67GItgtiiJToxbHBn4TgiOsbU+sl1SKjy8Nypuzejprp8bReJgIbFJmWVK5a5V6qiSCz7KMdaOMW1iZ8QFuazDGx6qJyW/pcsjlw7DuYouVUGc5M5f9c3haJ+WtbLUzIB3RFISXPpSxC1Dn84zre7nyg6vvDy3OiyG+W5BdQ2r8fz65u7l43a1m58a3TlL6fKqJerSwjpCTmaiFmySA7W/cMpNQJE5PXZ87UdWW+v5cQUmFakdeyFJafNQXXyK73yfa/dmORcsUTwT/GXIOAUed0FSsqSFzHkRTY1jkqn7Ey6LhmqPpYlg2DVVqqHTT/b8Ipnm+hSS7iJY9VW0Q4V+Lnf9XhGd1a1quR4RaRo2z1lrceV1x524OXPSJa8U68hs+4BL5WFnZkf1kJe9u5EPClKT+2p3pHebUje6aJep8/JcijevPJ3ajj0Ga/Gqd6hTk+OGYfYona6T+nwW0B1Sksf4BK9z73xCPIvpS1s9S0f5hDUk1kg9PuTGeJJn1/NGIDylUs60VwXro42yZU57vnerHStIYQwgPC2jrecYXkigKJ5rJwBZud2q1QFOsNMxq41UOo3aplX7jSRnroxarCeBxiEwMravIhwBLtcr7iQwxWCqMzLYzWLttJt3HBpdSJ/2ZBWuZjJRGUsO3uXsdeP4RlhTmYmfC/tcB3bC94iLcckZrfN1grU0AEAyW18OgRQu+mhbZmJ9nOON527QLpf52TkIrogQYH2NlONmsx7PW+YUyBTGoiNSX9kqicEYwy7Mjb87azuSQRZO32BlxFl13lq9eva8dGtLdFxo2ws+WyArMeaQwQLrk9vipG8GB51rHL7KZ+kFi4oMYO+l6LyYE6lSm3kYKuVmX3UtwV3AiOikJ5Y0Qewio4zoHdFa8xnLaw6JHVRkiWmNsyg5RndnRE1xND1WxTzNkXNLhMwG6zPYXjjalWarfcocq2VxILOUaSJqdoX7k4iaal5kxZWXEjZrzRmVVlvSOtkKzrozJ2qikbocDyJnVYsVbWxFx1xXaG6tr5mc9RWMoZyh6TK9wJoytWC2pH3vglflpj5vlmii145rqS0QZIGBCeF2oDVGj+L3o7WCb4N0mGOJjlorVmTD1L9JK8SclTK35vhzWMhz0W63eHFosjQ+oQBs8padb8alrxXVatmfVX8ntGCOFaOaBzg3tqokVBscD6VFZFIwlzY76kpd+S1patLyBoumH8LHOWrujy22c7aDncHYVp2Hu1W+6vf6HEWIzFhHVk/LjpI77Gjuqyrtzhc8IQeYY8pIU304SLG2EumBti4pLuENeZMZA7g5d9fFZtjGdMvojCfTo73VlMCMaZo4lBUG76m1QburBcVvVhou7YSZUng4QlC3LqSYLS2VS6GXDgSN24HdmCeBpqUoC7WjkBviwWTW7hJLEGSDpBKCjtv1qjZYaXHcaNzAqLq1v+4o0l2aJ2J+3C6UOkpKo6sIE9lxpLElLqRqlYI55Cbd7Vd7uDpRhD1c1dJDNJQIpWjr3Nr5xQE8WuMs0VKZtCZY0rmhxtm1+4MEk2SARTi5k7y12tBrdkN3tZUr7Z6hu0hD1tS5W24KHWzz7aBhYW2uouqiptGOGE0qXaBgh8yEdB/pPEcSlUxQeHelKW+5qOAi0hH6LF50qoBFtViLrCHBrj7i9nojciImGbZOZzqNApLurb1gZ8plhxyro2DSKBiVQ7A/OhBoBZOs6B6D5OYRXL9ZebN0BWPl4hJYK/sG86xxDtv5UswxTpHOHsyLYpHtN97W60bZorJd66O2REjJGOmza78XkWBNo4bjJFsrqK49G8YGVonDHm7sC4zM6FPOrIzyumSRBazVm06c4wK/qpaZSNtUL8384+52ddSLtR2sWXoMLupMIa4gn4lTXW+LI5736NW6lbMVniyR9SmgWo3iaXi/572TzVyzXEybok1nno4VFOCBgJSD9cbeGc2hh2cbGRglW9aeCi2t3ZaIdggJTdjZAuCji8QjhFNLBnkQnauRwpvqJqwSVF2u9kHtECrZElW7vazJeYMnJxrzuSyt/Oai9tEpOYxDUqD9GatUqTg2ndKn18GJBQlbayu5b6OsSRJrZpP6zr9oAUro1lFoveSwLXXsuDHL2bFS1W53hgVru6Rb/CSI2owksIqhzocy0RQDdOeJTnc8QYjsPCsuK6HUBZzGGS/gGakJDvWarsWraRsDLix3+MwZ7Zw3EPK4GtQzwp+R2tu0Ib4eSfuiSenshOAGgi+pdHsobiy+bGJCbSm7OpuoomjI6C6Wq+PyfCHZKsMaAbYtDFeVogVTqaijTp/LGHsSyzrQVfOCM7N+Tqv8shLnt0yPQopqSYe4rW/6dq9cD6K034YXocSObqhlt34IdaTTZyu5WqnZulmHst4t9jPaLtsbw6oLrbxevK3TBfF1Z3geQpwc4+C0892SFTZlKS23R+vmdHMqQsZAiKTAuQ5esER8TaDoZeW0FInDChPaiyzOVEafaaQ7q2iKM1bCXOi5Ft9pBzzcr2FmmUl0X66vgIT1pXbUG89I1nUKUtHjQeB6h0wfApmZ2WclsMZztZQIY0mepYxuRBRmTvMk5wWY1VxDamCyyM3bbYbbAtgyro+eu4UlecHTh1nAgI3AOVHRY7lpeJ9NT9We46jchBOv4dGe17drMESu4mrrIT6udqUNr7z4ZtlEEnqlNMBhba5sc6MkHRmkPLwbRAuVUh2PowBlOSQYVVOn8whej6PFcQ3bGiRttT2p6vTRd6oCV9TSkhm8WwW6sz+P2zDGr8Jpibt7RKHmdcQ4apCy43VW0zdmkfO2sax9FdlgNRGPZtkMyXCoN7O9hbuBzsPLfedWigfivcI21yIwxTZDNu7AcdzfXj69TE/9n8/u/9UX/9OD1P9vz3Mfj17f3uPdn9z7tvflruvLv2zZT59eajcGdj0eYTdpFz4f9P79A+zP/+TroUnK8Hi1Pr19vLVvLz5aO5x+Ce3l7SXN/XfJ2uk1LPhZdO23Ivj2eIEMjt9fA08WPl8hAcPwV+QVe/n1vwFvrOpH4CcAAA== -->
