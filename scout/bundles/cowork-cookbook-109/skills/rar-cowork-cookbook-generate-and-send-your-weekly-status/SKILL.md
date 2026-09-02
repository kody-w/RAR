---
name: "rar-cowork-cookbook-generate-and-send-your-weekly-status"
description: "Replace the Monday-morning scramble with a status update that writes itself."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/generate_and_send_your_weekly_status", "rar_sha256": "db94ab2c81b668d9e81704c23a28d8401cd9b63203dd54d595c2f1186ea5f0bc", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "generate_and_send_your_weekly_status_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/generate-and-send-your-weekly-status:0a9fa133416655686e68acd394a8bcbb09903c3465f40dce4d89c668f7cf08b9", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "work_management", "intermediate", "integration", "fabric_iq"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/generate_and_send_your_weekly_status`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `generate_and_send_your_weekly_status_agent.py` is
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

Generate and send your weekly status automatically — Replace the Monday-morning scramble with a status update that writes itself.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/generate-and-send-your-weekly-status
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
    "audience": {
      "description": "Optional. Who reads it \u2014 this drives register, length and what can be assumed.",
      "type": "string"
    },
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
      "description": "What to produce, and about what.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `generate_and_send_your_weekly_status_agent.py` and embedded as the fenced Python below (sha256 db94ab2c81b668d9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `generate_and_send_your_weekly_status_agent.py` first:

```bash
python3 generate_and_send_your_weekly_status_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 generate_and_send_your_weekly_status_agent.py   # or on stdin
python3 generate_and_send_your_weekly_status_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Generate and send your weekly status automatically — Replace the Monday-morning scramble with a status update that writes itself.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/generate-and-send-your-weekly-status
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/generate_and_send_your_weekly_status',
    "version": '2.0.0',
    "display_name": 'Generate and send your weekly status automatically',
    "description": 'Replace the Monday-morning scramble with a status update that writes itself.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'work_management', 'intermediate', 'integration', 'fabric_iq'],
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
        "upstream_slug": 'generate-and-send-your-weekly-status',
        "upstream_url": 'https://coworkcookbook.com/recipes/generate-and-send-your-weekly-status',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3ec977d736fa8623',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'fabric-iq', 'process_roots': ['work-management'], 'process_tags': ['work-management/manage-communications/produce-recurring-status-updates'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'work-management/generate-and-send-your-weekly-status', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Scheduling', 'Meetings'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.429, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:report', 'word:generate'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class GenerateAndSendYourWeeklyStatus(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'GenerateAndSendYourWeeklyStatus'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'audience': {'description': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What to produce, and about what.', 'type': 'string'}},
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
    print(GenerateAndSendYourWeeklyStatus().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/616aXOjyLrmX2F8P3T3lctiEQh84kQMAoQASUggENDVUcW+L2IRoJ7+75NItqvq3u4zpyeuHLYlyHzzXZ/3yUS/P9ldG5X10+uT6tsFxNtZFkd+DdmFBzFlX9Yp+FemDviF3LJo69jp2rJunp6fPL9x67hq47IA0xW/ymzXh9rIh3Zl4dnjp7ysi7gIITDMzp3Mh/q4jSAbalq77Rqoqzy7nSbYLdTXces3UNw2fha8AOH+YOdV5jdPr7/+9vwUg/dPr78/uZndgEtPvF/4NZhMF57qF55ZdvXZ99NsVO+iwfzMLkIwsBqBdQX4XPl1UNY5uOT5AfT26edptWfoP/8z7e06bH55/VxAb6/PT9OP0hV3g9rSblrfg1y7sp04i9vxBaKz3h4bqPbbri6au1k1sPblMfObpLKC/jnd+/mxyEvotz9/fiqryQDgus9Pv0BlDdaru+n9yySl+vmXl6zs/frnX77JaTon8d12Ejb56Mvb5zexYOC3oXFwX/WfQOojSI7/+ek746bXQ+/JTjDz6SUp4+Lnh+CqLq9+YReu//MvfyXWjXw3zeKm/bfk/voQHPm2B2x6U/yX57uTf4NmbwZ9yPzrZUGKFX/HEjD8fbln6M1RfyX77v//IjqLC5CV7x7/U3F/NmH2T+jXv7TtX014hoLPT6yfxVeQHaBiXqHfv6gHjvn1J+/bxZ9++wOI/n+KUUFRuHcJX3K7iAO/ab98+fWn5n75p99+/amrQK75dv6lq7M/k/lnfr2v84MH30b9/ONcsL5WpEXZF9BHpkO/l9X/qv94gXQ7i71v15tX6Pt6mV4zaDLifdGHC76rmQbo+p0ff3n6A0BEAazp3PttUOX/8R/QLnbrsimDFlLdsmshEOA2zv1J+VMUN9Dprai/qpKw3b7k3lcIXJ3KHUCE3WUtxNd2nEGgHqaITxaUAfT1f7t3WPzkvsHiPHwDoy8AM780AI6+jMDHX/o7IH15gN3XF+gUgaXLOg7jws4ghT4cIBtMbadF7+nRdPmn67Qu0Cl+4I7CCBPmNF3m/wP6+u8s9OUu86UaJ2M+FyA6NgiZB7V+XpW1XcfZCNkTWjlj638CKAsQpS6zzLHdFJr+dNXL5KFz5BdvfnNBX/AH3+0AWGelC5QPYoDMzyD0TZldJwQHJjRpnGWQF9fAVWU93hsI8PjrJOzr16+O3USfiwccY9CjcTRzMOBDYejTp6r2gywOo/Zz4btRCf30+x8/Qf8H+lez7sKnNQ6gM9x9BlI6g0RV3kOgPrscDAN9BSQHAJ97/H7/4xGMSTvgTwhUVRzE/n0ykPYtGSYLHhF6Dw+weVLRr99W+tFvUB8Bv4AeBrwFKr15/lxMIkowtO7jxn934mPyw/Xv8X6sM8WkefMhiFNQl/l97D0Pp2C6Ze29QEIAfXgKmAvi2k4RjcqmBalbgcTwC3d8NNaPEBZlCzWgeppgfIa6Bpg6Sf7qANGTc3IAUXb7FdoxB9Dtygz8mRx0Xx7MLot4Cvxbwj4uAyH1TyDHVu8iXqC9D7wJVXZtV1FtNw82ENiPjABd7n0+EG5Dhd9DU2P3pxjd6/qeee+9/e7/KcuhKcuhR5a/cwfAWsoczAFKgYufOxRGFtD/JAWZNKF5XuF4+sSxELc/KeYjbSYWNFnxIE6ACkCASjxq4Bs9eEeSd4z9XGQxcHU9/uMxMrhnymPMA7e6GqSBQit3+VPN1ne5cQviPQWwrqcctT8X72D+DMwA3m4mXAJlmU5FXn4sON191zQCtTd9/tbYoUcqTS4GSQpVnZPFLhT4vnfP5zaqp2p5cysIvj9VDkhvN/rBKghIB4EF8iGgBPAcBAD/7ro9yPrJ7/cU/hgeT3QJaOF1LtAWlIX/Ap0n34NMayDHB5xnGgO88NNdFJT7wMdAxQ8PN5FdPZSZmOmbgvZbLL73/9utd8j0vhUTkGmDqANP9iAEoFaGR1w/tHyLFFA1nxL7PunHYL9ZCn3fc/4xFRTQ8Bumg9Sc2vV3rgEoXOfNPbFBI00bULK5/5Y+IA/unfnl0Vwf3ftDl9f/RsZ//nt8/d4utR/j9gpFbVs1r/P5o6W9d7QXt8znIEPiym8+utsnsMKnqRw/TeX46VGOnx519IPsh6teob+n3w8i3tL6FUJe4Bd4urWNXX/K27cXcAfzaWV+Wkx3PxeK/y3OPyKDM350jW/dMwxrP5wGP7pIMzWfHvS7O3jdu8BHLrzVCcDGIpxaXlN+V7+TTVNkH4H7AFlwq5jg25sIW+hPu5lsUr/xn16LLsuenwo79/+tXcyEpCBfgTum3Q+oHMCA2ti/f7I7L558Mr3/cSsm39/Y2VRc5dQPvQnW3kvirr9XA+WmagxBp/LrZwjoHE7ICEzqp4qcmr4DTGxA2/O9yYZ2rCalH7uciXF90LH/rsG9qAEaeeXrVNugbQLq/Ax9sOBn6H1fct/rFR3YmP06MfDJZjAU/PsY+7HTdPyn3/5EjTdC/tdKvAHO86OhO1M/nEz8E5uAtNq/dKD/epM+3wz8tm75WOyPu57tY0v5+9M7pkzvH2TgkVpgwt8ibZPd7832yyTcnkTcqdXdDXda+sUGOTA11e9uhRND+PLI1qdXAEr+8xOYDKgN4Nq3+zb66aERMOUboQUSALx8aiaSMAfFBiSB1l1NZqQAGr9bYLoce/fx05vXv2TB/wonXmGbCmwEwxYIQeA4QRI+Qdquh1ELm3Rcx4EpCsZcbEHgwQL2XH/hkZRLEGSwdAOYdCigSAMSI7ffFJkjUySACR/u/v9i508PGaC5oDgxHRE4QCEHdUnEAYt7lE8iS3jhopiNkh65gBHXoxwCQ2HM8/CFh1O4iwYIAsyx8QB23EneGzd8KPblnYe/x+YBGV8A0ObxpDZq2y7pLpGFRy1twvUx2MFcH0ERb4n5ME5hAUn6CzD/Y+pbfKbwPWyfshfQQkDKrtM6v7/Fe8pIYgFGbhaNQD9ezJzSbQLbOkNkzG5EYAoJWYrqqUT5QoXXWhHH0rIoUy+ZaegC4RYELZpp1K1ooV8rW86++ceILBU8LZbFUhYlUBvozOJ3Jn4wMWdf3GbaEkOKI7m8KRp+vhwrSxrZ41np+Kuhm7p5uWq6I5yqSsksU23GvE/UARNXNDWfzXSD1OosNkdN2nvSYTdXzzKR58QgeE6pinGdiumooXI1bs/HtiSrBL1Y7oiIDYPAFwFTKn27hRXicKpgKihOJBUY2Axs+uZkUOs8MiOjti9VuNOz+rSUG1kq9ChfHZVSGCVrROiCom+BKqSXPXqOcN7WiC1zHHxiKJxE03bKvjePF+nSMoO/1Qm1OW9vunxDRYQw20I8Ho3ItC5urSoXfXHRYLyP+FbnRTQTmjyWiL5rUHPJXzDE4Lpb1VF4qqO1Lpn9ieDjWkjENt6RNSlyCipV+uomEXRJHLXtDk/Hmy5kjeRY9cZGlvjAHw15ENqSZhoxEdo421Hxlp2d2day1i3apAvb5vsAGdbwRm6Z7rzdkEWsWJrN2WWKUoK72cx3YaPwveMMF5Zvzu4V8ChB14nR9g7OFa1Gv0Zu4bA213BUMKLYNwpyNQ8CpieBnpQ4cmP1k9sf2LNkYEV33UetoZ0TfuEnSHjrVMFpZrOTshbJNjCPlVqiUbpbwH6uc37blMgI9zIpEFyyslLRJXcenzrpYpzHoYVk6NoX566hRhZz8c2w2RPLDbdQlNEj1mzFKVESb24bDDnc3DOx3exuBQnHRhTjnkFoztkWVjhc74huvyc1XiMvhHQ2PIR3wK+105cqAmcDWWwsj1EJDp+Jt/liM6eZQ0DAkRJv67kpXG6E412rjArdgyK13rLFMWJRzm9n38t9wWJq3V6f92wWikM6x0Ze3ZnDfjzKiRiK7iFVAI4TWu7SSHFSswW+YmtnHuK3017NuT4THVNuzWO7EIKDC3xIJ5cVDTOuKnYKdhRusFIPoomtkUVEYiAXmqE3cyoeEBnXlNAL0D21I1APvmU7PgzSVKBdLos3q70ZmWPA5dY2PTBKgjRU4hwZqSNYH5flqLX4tBY33vZKHRoJxZrVeg0nZFd1NVLpvVVvF65AcbW/8vixkqT9Cj8MbNywIqvn9Mpcy+vAL+1DvhzT04Ipa3l1aGkS58ql3a8NWJV87cbUZ5ljqeCo3eQm2/KKSTDXk0O6YsXlm1iKW9QTHRnnnFOLaylMV1IdxOS42+8zXxQP9voINsWetJJLSrzILR+T6W5fqStBW23qLtD2q/2xy8Kj4J4rwpmV2QI9M7PtfJkxqXC0ewWfqRS3JyRqpFuQatR5G5G+u3ToI7w0V7V03GxhRq+PVaygudYrhEcbihZ7ZytLKpGxdgndUdsNarD4IGn7ZR7NdTIl8MW8vpSIdPSa+Y7d6C1LGWJ6ZWfX5Kqs+tVonhVNPBn9Zr8xDSQwxdNaau09ulnI+or25wGF7sKZT583p2RxpXebA5NGKWucleRMbqKw4I1LxWJpqqToOibz9QIrUXPN73nFEyjTmgtcLd8aFXP6I7o4jXJTRQk+z2/IDT8Vdd27YCdt5fmYj4cLvSqtPiLTah+GerDYwxJZy2anVC4y24gSw1Vr0NpKeOWE1VhZR0TsaXIvC0J5kqSMabZ7UvHWBcv0zTZdC2G03y00wFQO0vzAhL4s97h71EK96XY7l79mJt+iSHFottw4upxVFAY2X8o3cnB1nD21/IIYl3N4cRnVJDtZQMsbLK56acsmaI3Pmzk/Yw3D9YfAYkJmk6flZTafxfWMaHlDnefGdiBnbrmJ10W6hw9bKcdFlo7CtYwI4xFvil3CSWpjEZ2nKNmRjfFrR+dpot3YOqTzEFmPFH248eNFq0Y7ZWyPPGUqJ+7h4bY4hfxs3ZAiWu7iES5vVbal3f16RcJ6sW7P2yO+z6nuoJUg3o1xzYHxWkRc6XEv6yPJVPV55C2vEZiuZI6rC1q52j4Du0SXOLeHFIvxWnRhanUse4qlw3BsxDMOpxkjLhtPwUANRdltpayTM2OkNE4mbCTbQb/ZJXFzRFY65RO4FptzVBRQcTt42Iy/UCaKKGlPlnzkjWfPWlF0drMHhuWSATP7BcLaGmf0gsfBFGy6VbXaUU56HVGtOctwcWYqaVafwEaN7DlWHdMssWpQS7v5Ga4TZVvYkXeJpGMfjfyw4tneX2Xp6QYf48tNsWUsF7q+zwTPFc/7YX12NYJbyvaZvHHK8diTjN3hBteihQ1KXQX8wQrp0RftEVXG2soY/MwdMolrQnYlDrPFbjhUCcHMc8/OBWOjoJHBDdlyZ1h4nVdlq8435XgjsS4r9Vifu4lmJoyI3c6lCSsYDboDW7Lm2Z2JJmB70il1LqK+JphLs3GYErPT/kZ72UIzD3Qzni6xcVpdNWZ9VgeO47s+ZQRCqMn16rLlT6v0fECXBbxBdkQectLpMG/Ym9P7lIRahKyw1mKkhxONn5FijyZmzWUAt1xx7xppqcznwbW2Kc920WRD2Ga4hNcqMQ+vK/jcXEQck3feEBEnzzg7o+PkQTO47EVnE2dZn8/mjiqXkdiXK6/lxoXAXjgmolHCmOFa4mw13z3MuA13NpVMvQ3kej3ODzciWvK7hhn1LIl8g8+k066Jh440EU5INAy11NM+8wRS3KrqDERaZvyZdTnFzdU7p+tTWshyIpjR2vBhM97fjrgrWCqq4sux3Md8GcmMYLWmho6lTEunRXXL04hVjEqQiFDfxTpPdrA6mru2Kg4cD5iIrui3+kDPZ9sIoU5nnRZbnYZjGMfVetB4lFFNnq3aiNbW0slc7YU1Gakh7pRiuajq+tqcOmxja67iNpZo1XkpnUqzlmKnG7cjvDunDLPKb2p7KqPdhRHocdHo9CVULHk25w4YHYgRvxh3aZ3nW6u4YYIZdjNViWxDZ7mVLmm1HBaavaQrcdtZTH4+6idFn7Gye/S3uB+eZECQkiTSVI3Y6PNrLMd91kTn0kJjid3JgmQejqCNZUnZsHt/gewPEskWGrnBDGFJLvKZq4UXk/IGsJ8xV2YnVAwlS5pZX1LjjBcbfikNcHDak/qOaiNEzLaEo7H2jbaWfekcO8HmpF6EMbi/rHuxq+wxQOYXkSniuuXMXBsxL9+KphEvF22hLrdIdmX0tUYrK91I8fC0VohOAF7ew+cMvR64g+cMsFD0nc6AnOGFvTV6ZegaZmmcKHNgW/16vcqMMsz48/pqIVu7L8VdCqy6IiuXaDebVCnLQbUvWSJRebLX/Ea87taW7pk2nx+XMmdY2OFgqcy8QoTERtnEHgmuvoCIiimC2q3g07B+4U88RmC2sZIMzYqcjdkEV3SrM8NgFeQe3sNNkRX2UV0qoi1s6nMgeEyCMd1NM88yfo235ZGF+eVa36r7XLXNAbe2HD0bVhFyUpxDVi0JT+awhMEYdw/o1AYvIoNlA5mvtynR4EXn4hXFsipwvLNGuSBFAlkNw0M2NzfMcC2M7Xl7NhJqDLFNixgLFF+uHWa2RAH4zWs2HDpnWWGqZVD9Tr9ZHcFZW3ncsZ47DHFBZ3KK4C68yFSGuDa12Xl4GvSWy2B9u7QQjh2z64CjXjDO05rv0q3N7ZIQ8zeUFEWtu8ipXUYJykhjJKaf6ZiIanqR6bZzIjo7Go4XzsB86oyvZ/BB3fbLBa1j1nC6XfVVEkr8Uh6vgLsz7e4AiINMZmGJyUESBslwm899zDDm9CZiHDFWWbPGZsIBR2EPxof6YF1iasl5eykYZUlHszUuX7eusTluiE11c6IdiZK3Xpyz8Lhq+sW5s3T66Ln7i7L28WQWrbkNgEHSGZJiPlqbAcOyLs+MUxG4GB9pa0WVb4A4yrcIteoIE7Gt7eFKcuWt9XaXVLubOkM7O9bbvMBdVljPXcTol/OqwbBNUCFmYyKKhwGG63utp4+AAWC8V7ErDXTsoNwfKQtD8TB0q0U8L44GIBw4d4QP7QXbyOgVhmvqeiWGYb7KTpUPK0t6p4gc5R8unncb4cLCArDFW6kUVa8Ww1oBiAdS0prtK9x31led7a5eyZ/2s9IdyGVTkEFHRjlKqgl9m90uneMei0WxrdSA22pL7nQRDBtecmZxOpCVB0wxV6uZ3R82WBEjXVxxRCdeicitTJmRndifKUxopXXJISSWpP0JlJdF9NkyucqHgvYlPtsuR03h4uCCS8GlN+UNi2FBO5BCrR32m23huJSYSE7P9mkvu/VNgx1YxEMKPtMDGwXGVcwULxBsd3DROcUtEuKa4JlNtfypm3XDcesqDS7Dvgficbu655jHTwDbjlSQKRwjkTMYY43Z4kq5KwxxjK1zvgWdFrVMIR3q/qhsInaNHlj2DAtccCpgnsED/xy0AF5JAS+xDZov3LHIWUvzWpdqGuKgLgNLd+DlEbMMsF8LB2RZgsYe48vQW+w2YXLjS4bU5ypf6ETfxh6/WtOzWUIVcoJcolUfJBRxkg5d7qemQZV4jQ5Ixx1JYRmYgGgRs5a4ze2i9rdyN9sUBdinXqhmSLho2USo3hDIfkzafkm2JX9N5pc5JrPY1WrIhd4a6C2xcgJEjHGQub+kkiUZk0IwBiXr+AxGmSVdLlg9YS7C6kRklT0jfEwmN2zq6IdcgL0d4hed0QdqMduxx/1KlBlkb6xPt7knLcAWWmErR/RYZOEXo+50CStvF16TXvNLsq7pc+oby4PEsqUKB/SBukomH1jra3xbwbLjZppxpmo3KwwUXaJwYRae654v4Tq6KIV3IoqtNnZ9SB42K1JD9v6aIsPFbUXSjN5HmzVeMi4W3sq4DC6sf8pD3pPV+MRuxtLZu/lBTSqjtQC1vV0XbLRdLq/ovgZV2S100V1lpLYQqcYlyZFDUePobecAza/rjlluyeSCuZG0i2TJMiR7veWWm3jfXOe6sDrO9V0u50SQz1PaXdZZv+Fpr5YwW4bXombbdVoKqFxg24A2NrpUHH3GHWoylzd1ILrEYIwe3FC8eLKxBDZIGu4txpgvCpqm//n0/HR/lvr0isAoRj4/Tef1b6fuf/dANrzF1Zc3aaBhoc9P/3PnhI8zu/encvczcN/2Xu+rv/49RX97fqrdGCj1OMZtsi58Ox78Lyein/6dk9pJwvh4LDw9RBza90cXrR3eD5PjwuuatgZ6lFl3P0oGLu+a6eshzfQNIhf8f7obl1fTEf7jMTV4M+kyfSEFKD49932avrkxPRbzvRjo9PYxfDt3B4GznTp2v8SXycC350LTeen0YOjpj/8LUT5hw78mAAA= -->
