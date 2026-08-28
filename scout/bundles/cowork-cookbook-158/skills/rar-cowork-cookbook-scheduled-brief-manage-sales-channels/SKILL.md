---
name: "rar-cowork-cookbook-scheduled-brief-manage-sales-channels"
description: "Schedulable morning-brief email summarizing manage sales channels for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_manage_sales_channels", "rar_sha256": "f7862a1d6b76f23a909e6b010ea8c25a8afdebce6e2a68a96cb16c3aa1b54377", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_manage_sales_channels`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_manage_sales_channels_agent.py` and in the RCI capsule.

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

Manage sales channels Scheduled Email Brief — Schedulable morning-brief email summarizing manage sales channels for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-manage-sales-channels
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_manage_sales_channels_agent.py` and embedded as the fenced Python below (sha256 f7862a1d6b76f23a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_manage_sales_channels_agent.py` first:

```bash
python3 scheduled_brief_manage_sales_channels_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_manage_sales_channels_agent.py   # or on stdin
python3 scheduled_brief_manage_sales_channels_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage sales channels Scheduled Email Brief — Schedulable morning-brief email summarizing manage sales channels for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-manage-sales-channels
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_manage_sales_channels',
    "version": '2.0.0',
    "display_name": 'Manage sales channels Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing manage sales channels for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-manage-sales-channels',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-manage-sales-channels',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '456c784f560dc125',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/develop-sales-policies/manage-sales-channels'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/scheduled-brief-manage-sales-channels', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefManageSalesChannels(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefManageSalesChannels'
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
    print(ScheduledBriefManageSalesChannels().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6eZOjxrbnV+HV+6Pbj+6SQCyibzhiWMQmIZCENtyONkuyiH2VwOPvPomkqravfd+7npiIUXdFCTh59vM7J5P69cVumzCvXr687ICdIZKdJFEIKsTOPITPr3kVw1957MAfxM2zpoqctsmr+uXTiwdqt4qKJsqzcbkbAq9NbCcBSJpXWZQFn50qAj4CUjtKkLpNU7uKBngfSe3MDgBS2wmoETe0swwkNeLnFdKEAKlAXeRZHY2c8msGqn8gUFQUZMBDmhyp2gzxIMcegfRXAOKkf4XagJudFpDfy5effv70EsHvL19+fXETu66/awc8blRJu8vfjeL5p3TIIbGzAJIWPXRIBq8LUEGVUnjLg1Y8rz7WIPE/If/1X/HVroL6hy9fM+T5+foy/ttC9UYrmtyuG6ixaxe2EyVR078ibHK1+xoa2LRVViM2UkN/ZsHrY+V3TnmB/Dg++/gQ8hqA5uPXlxyqYI/e/vryw2j71xfoCvj9deRSfPzhNcmvoPr4w3c+detcgNuMzKDWr9+e10+2kPA7aeTfpf4IuT7i6oCvL78zbvw89B7thCtfXi95lH18MC6qvAOZnbng4w//ii2MgBsnUd38W3x/ejAOge1Bm56K//Dp7uSfEfRp0DvPfy22gGH9O5ZA8jdxn5Cno/4V77v//4l1EmUwqd88/pfs/moB+iPy07+07b9b8Anxv74IIIk6mB2wZL4gv37bGQv+pw/e95sffv4Nsv4f2ezytnLvHL7BEo18UDffvv30ob7f/vDzTx/aAuYasNNvbZX8Fc+/8utdzh88+KT6+Me1UP4+izNY8ch7piO/5sV/VL+9Igc7ibzv9+svyO/rZfygyGjEm9CHC35XMzXU9Xd+/OHlNwgSGbSmde+PYZX/538iWuRWeZ37DbJz87YZsaaJUjAqb4ZRjcD/D4SCfn0A1IMO5v8Y4VHj3Ed++V/uHTk/u0/knNRv8PPtDonfHgD47Q6A394A8JdXxITM8yoKosxOkC1rGF9HuqwZBRcQF0HVQUhx+gZ8hmD0efyCRBnyy7/F/9ud1WvR/3JH9+iBU1teGTGqhqtfRzuPIcieVrmwIYAbcFsoJcldqJIfQYafRoTOkw5i3OiTOo6SBPGiCjogr/o7b+i3LyOzX375xbHr8Gv2ANUZ8ugY9QQSvKuDfP4MbfOTKAibrxlwwxz58OtvH5D/jfx3q+7MRxkGRPhnVKCG6k5fI7DK2hSSwYDBEEMIuUfl19+eHoZsYFdBYAwjPwKPxTBLY+C9uXsns59xkkIcAN0MXZwWedWMnStqXhHFR971hULHRyOWh3ndwEZVgMwDmdtDrjY0592TWd7AhtdEtd9/Qtoa3KX+4lT2XcV0jFLzC6LxBuwcefLW6EYiuDjPIuj+92R43IdMqg81wr2xeEXWY14ihV3ZRVjZTxm+/YgL7BhvyyFzG8nA9Ws29kkwuupeJA/3QCLoGfcZ0s9jzGHrh9078+o32Xcae+xv5r3PVV+z+lkAdjWGwoUNAQoN2sgb28I/nilVh3mbeHf/gUe3f0bBe0blnoPaX84H7z0cWdwninsrR762+BQjkP+v48eoMytJ24XEmgsBWazN7fnhy3FkGn3+mLLgEPAUA+vm+2DwBitv6Po1SyKYGFX/jwflPQJPmgditRVUZstu7/xh+KEvR7737ByzrarGvLa/Zm8w/gkG/I5ZMECwlOOHLW8Cx6dvmoawXsfr7y39Hs3KGwsbZiBStE4Cs8MHwHNsN4ZaVWOFPeMAUxWM1XYNIzf8g1UI5A4zAvJHoBIRrBno3bvr1jk0E8bFr/L0O3k0DkpQC691obZwJgWvyBEWyRiBGlYmnHZGGuiFD3dWSAqgj6GK7x6uQ7t4KDOOsU8F7TEWeQpz9/cReD78ntZ3XUb1IVfbsxvoy+uItR64PSL7ruczVlDZdCzE+6I/hvtpK/L7fvOPr9ldx3d4h/X9yN7vzkFgXaX1HVBHeKohxKTgPU8fXfn10Vgfnftdly9/mt0//r3x/t4q93+M3BckbJqi/jKZPNrbW3d7heAwgTkSFaD+3uke1ff5UWuf77X2+a3W/sD84asvyN9T8A8snpn9BcFep6/T8dEqcsGYus8P9Af/mTt/JsanX7Mt+B7oZzaM+Apr2unfm80bCew4QQWCkfjRfOqxZ11hm7yjLQzF1+w9GZ6lMhoajJ2yzn9XwveuC0P7iNx7U4CPsgbK9sZpLQDjZiYZ1a/By5esTZJPL5mdgn9zEzOCP0xZ6JBx+wPLBw5ATQTuV+/D0Hjxx93bvbAgInj5l7G+PiHj4PoJeZ9BPyFvu4L7Xitr4bbop3H+HUVCUvjrnfZ9a+iAF7gVa/piVP6x1RnHruc4/GclxrKCGrtgbOj5e52OEv/EBH4JAlD9mYl+/2InT7CoG3tsz1HzVuJvCfoJgeGDpQerCeZoCxf8WQyUU4GyhX3QG8397r/vZuUPW367u6F57Bd/fXkDjWcMnrMhJIfV+bkeO+EEpioUCK8fSQWf/d9NjU8mEOvgwAK5+PScwm3Moxya8vGZzUwZQDlTbArsuYuT9tz2PeC4gAK4Tc1thnIdjHJnto05JDGjacjvkZ/fxp4fjYrhtu3OXRojPIa2KRfMps7MBRiOefQMTElm5s/ngIA+el8aQ6B8WvuwbnTl+wA7euVp9K8vDkVASpmoFfbx4SfMwaaPtLMNHaaiwNk6TRQn2pe96Xiho1qYLHmOwqYCGGox31eu4sc7tbSJC+tqOVlKeigwbEarctdmQJKX2kFtk6CWLpE6qCnpoh6awWf7xWJzEWnltKT2taCah2hbpcAta1SJjnY7HZJNOVysnYWqaukddhPDWVVzXLkIWrIuHc1zKPt26UuwtJv1rbGoYnI7SVe9Tyh7n2wrdV8kPLl2TGuleTa93Pbq4VAyPS3m1t6zyR0v3paDMDmWaeVwrb6NfCMrcN8wG9L37bUudyTa9fJ+1UulZsYJhBYFNKWzLzzHn6ZS0y039ZnKcZ+4+HbDY+1hl5JSeiZXxyPht+dkJZizubjo85jK29zNyN5MV8kNjmxJ6IVAJTl3kVxSXJR16QzKpF5vxV0nHhNsdz6l+7SdCSmMRTSdnrSGtgp0Na2GQ7vvzXlgR7vEVPz1NNQ9LNOTxUo9LM9k4m52nrJbZ2jrJmFVHolT28TdSQOsmyVJulktl2y1w2yxPxB2xk7AUbXS6XQm7fatOPE0KrDI6mAXG3+FHkUv86IkTMiiSgkjvIjRBucra72lsJA+5EczXJunSizj9tatK3Xn253ZLyoOyBHQo4NiE5FZ2kNMccVxwAxsyNIec+c0N82jSl5BhWYzNFxHzUk7DRLhXw7BbMvh9bCmjdMyxMVQOiwv4CgoU2Ye1RWW2he85KdFRJicXauuu/CP01NKNOZ1v0fX7bm6HW43b6mmK4sJ+euMqF0zEmWRLiXpXNCmGE8y43SY6beqrPghBUPIuamf4OdUm2oLe7GyjgDv98eThemnw8HQyzQ1D6eZNcS3YX7MSmZ3IpYqtUJRiZlzpNQ1RzWPLpiP86spmpoyZfnnjJtWl2qGBsLGMkATrXxeLfft8tJURbztm111iCJLpvm9Iyb1QiPs29JJAkyxWfMaU0RcWfxpMHtsQwlZttc3vT5ka5M/t2GnrY7l2SbE7dVi9bW098zY5nbqDVXTreIq/Yp1JPcm7rUySlcKpZFXIl1dYG0Q+23t+TrqaRLKTOU8OyukPOy0DYi2pXFZTffOtN4xCl/j5s1odtO+PeP2ySS4SKy3fZGdogk62WT6Jb7W6KEF5rVkrNM8PdxAtdL2fLiNuFrB2z7NCSLLw9tJ7IJ6td/GfMdNJhtNHjxxa80lvxRlnucO2+KoLmK2NTyWJB1mud4vr+gJF3tj4xRiR2x6F0e79Uno1wex1UWsh3xgYTezXT8riiM9AExdRatlOSMY7RKY1uyyM/XwIDGl4K6lZcasOKyfmtF1P+cZY78YcuCz2BZodZKcs1W8543JfpjbZSNSMtH083Rvl1vZO07iraXEtJLnHtbmvq4yysUUFtklPE4DHkux/WRYrgpwu97Ma14oVaTYA9x4EliSLG21PIIkFY1iQXCUNN/11xOH44CYZFWd2KYDM/wyM0thdTRPusGAPS4J2iq7aj01QKCUbcE+MeZZpVWrs1VMJo5Trj/Mgb42Np0ugMmOJWXC2MnhbtuFdWbtbUsgruYYxHDS784FJfDAXMz9tcPzpRQbsQ4bbh36ix6kBTCWwpW3XYxIVP0EL+W5p6ViGV3OJ6bM1Bqduu7Gsy2LZXNBSLg667U5H583i3qbnHXhxCl83C3sUNeaaAacvTjzlma4QNmmssPqYi1sTpvuj4RCWbMsPGvKztIOWFavXGV3mLuYRbjrYSDYgqeKgLEI8bK8Mpea0bxhTkeDthn0tqtxFGRWP++GOIiBerxJqe9NLlShLvUdPb2166zeCfHmKJ+q48Aykzrge5wkLx4u8UprrkJsnvjQ58m8lU8MtoJN3ZC7gp2fW17MQphz7XJzVXLObHZ6rDvFsByimtutSJcqTZ2dyVf/aOqq29SLE7tryFZJer6R1tlBNHNMmZMUwaZpbh/K1TXRg7m63eDaYq6cyL2UGNDkvXLrrMKybY0+d0Dm8wjF1il0lWQFpe8oR46+SlQ914pW4ox9Gy4E3zaYQYxmGl42wSHbYcDAm01jrY5pfsAwI1SWiubzR8NaWrfUo1LbvQpMqqHniC2lNOrS68Bx+QT2NeOcdnulRZ0d092KJak1tSXk4WaNKfviXFYiOQudxHfNeuMpl22BRg4dK1exUG6eIwSNQrSbkp8Zq/bY2/GK0FBiuVE3pavCRPTM64FTF8Jw2xnrY1LZZ5Wo6S0Ka3JZuQsxXLNmYmBEWOJcdtL4LV+nVUeFJFOxhaihXqni5b7gd4JyynWUE65aEqUgmg5H4KzweShgXHQsplyWk9PDoWBK5eiup1bLdcFSDYimxmYYCaopJh2nl3h5ca5xdTkubl2L19h5B4LLdndbucJ+ycpMqqS5yizcPWD0TSuZDT9TqxVu7VbDdr12m+XVoJoqJkXiAmY5s1A2LZgngXzQJhrgbiK1J6N+EU/y6SZm4D5pFu3ycu6qG2FpqL6UsyXuJZFnw0kmkT22S1dwb5Avt9tCk/S8vShlelU5SpZMLNcMlE6nIWovGkVzZZ9yZuiV8yfy6aiRUpUF5aZneZ7uQKNyJZpodttG/TIK1SvDTAjUxCYkCIRFUu1r0d249rlGrcX2Sgu+FGMTQzr2A4PWZYyjGQYh4axb2NJhWqYIo1hKsYILaLyuGnbBmtKelXmumNIMEx6XOyBMduIuxlmLSuZEFJGwALEdPuhHdcdnVztNj7bnWhadKYam2ZukOizLgECL/dWXWzfYF9i5AQzLTfmePy1Lre1Oy+J2OWHLE6twsUFU7cERjoWkoeLU9DEhcIKU2mrHVt6aC7A7Z2RMWZtF1iviOjju4vK2izdURcazUs7kHWk6U4ayB5ftVlncqL6uGVdPXN2OSZl2lHDCFqYq+tKuD5Ml2Qr1tQFaLC12CxLYvRBaPN+vIljopQriKykfzDish3AX2yf7Jp4WOiklwzYMUW5HoLm71nHLRDNluRoKR1/Ft/rgp0f1IFaquc4WXlaW5KxuZ5sU5Zn9lCg3KMV7LIZaDUGvz4LVOlXoX9Rjxa+WewnzDIebTSCALS+1l1PU1iwYf8Hrk9icnsyu1dM97qBDcAlOB2sxTa4xWuX4wo5mPHeNo7VGF/qSc+tEitJlW/T71C3EYZ3x8sbAgcdYmC8FGE17pccqfaU2EyFmToY787xm50/LvXj0jxTG7RPOV4/NBiL2Kc+kHeusVOkYkNNgRu4LXWZsJc8i1l6yJq+KWentSdJyTi3bTEtHyu1gfdunqNiXpH3UxGE7x89Y4c49fD+k8pXfJqYap8xmv/aBTVObhCg2ptBNaWNtOoQT74hVSg3T62YzO9wgIM0Tltx1KV0RknnTrqRVdSeDPQ/zSDYKHGVtjSsOk5Y8SWYn6zOM2C0X9VURKCY55KcoaBkfz4/orExmtrxo6jyoaU6Zmxs0DVaMPGj9ctW6+5m1oM416y07bDmkoRIQNa5niZtG7WFNCQuh1jjp6kvRpXcDk61uaXMMjkvJUXvLl05FY3SkeiwJvdS4OctP63k5U82A1rvU40w+UZY7RfKNwsg3F4w/HEPVEi2LcIRkXdFqCJuasDPG3qUXGbjKi/UwaeM24iV9WahEKJ/OJ8wyNSWI7U2J7swmsCkqps7TzMyCQTnPs5l13a285bxigsuA5opzmfpNybiYrh7n7UyE4yUzC69nzJpgq87NvKt26EkXW+DHdeBIFHm5iFtlVzVD60n6vk8TdGoITkCk6GAErr7VSEDizqW8ylWblg1udxqziepQGaxrBPbLqThB8YVAbIUzN7DLdj6DqEAK4DC7LQSu1XS08/eto+3pRVeWtQ6KNeOsNmTtyR1768h0BU5OzTj8BvfxQ0Pi7CG5oI14azkjX3UWHkwOBClmcAM9QYNwsqmCa1X5E0yYyOYO7zrPReG+lN5uvASAUE+6zSrN9zHFdzeXEXhuCJrWClYnt1tkHrdWNV2oHPxwXAwma+89HSiXYnvjSFMn1kGrbyZi7MpgXk+n7cyt6OwccO0JWK0nbIlWWZ/s/rQ9+80AXIzuLws9xtU2VLcWlzGC5pDhJbuSrD6IjqcdCnluhF3dBvh5m0/8SMxlo8dpmu9iOjE8S4q1RNKLi2cs5Uqf467AxcH8MLd5yma66GbL+NQZMvuEAgxtJtTtNr0k7MGzthNOCzmRaYWimcu3qWy1PhyWQhGnT5cmWEnKwuE7fVg7J4hGK9/W4c59uupWty09hC3ZkuSMJ/2z2rJsN+wri5D5iSS24lXaNEOw1a8xyOQC9kuJxjK0bGOgAIGVVTtzpuvbhhqWPbM3B3QeyNuLcdFXSnhVh1PMO+16TmsLml/RqKt65CyTZ4Eh8le4ranOIQYwXfOpWTeTL1flynBMLuQbu7fpiUude0JThCAaOCuIqXVBL/qrS63YcxhU1WyK5kWVr/Vz6vu31FXlTXfdTQ6nQ+fMGTw5KpFzW9ckZR/P6S2uxQ4PnDWK04bka7FI0L6iTG5qXG/RNsdwZ6b3tTQBKt/L+tTrOE6edBdavsCqkITuRpwv63PL3vT25uO+Mr85w+w42yZse+Sv9DKs0jUUsSWpA3rS12uMmZXEQTpbVIO52pZ06cAjdBkWJZfzvDvJdZbGJ3RMafySmwvyvNcvTBlur/5loDZLo01BTHRrsz95l85VOGKDNzNnGd7mDpO15YQhW2qYCG2mey5W+aakCBNv7qPJZk4IYDDgHg+OaniHtcIaNl9Dp3KrnvjNLKIrF7hWO1ATP+gm/XF7ifbMbebe0q6Qbgl/qwP6Gm4XLEnYJZ07WjdhLsp625zn59UBGw6zq+iLqGpcb2t2LsWKccDmvmEw1zwC1SklW2OjAk/1InyGFZ3oRt1aJFZ74rKPzJVssLPcxbsFt+YCT90EgzvF3dYFoWwlJZViwqpoKHzOALwlb1NiItoxd5ZiZ3ZG6QFjs5rwhdvmJDamH206zdBYR2BFd2WGjsPKa0ortUKmajy2Yi4T6jxmb/MSJzBVmBbUCq9JoJ5pXSN6dGnTBNqz3Wxy40+cNeMzzj8kpVFv0oSiLzeT1laAwhWt63C3MHSu5M8z6rCgy+li17SmIWWL3CxPw8q0fd8dAlhR/VzOgvU0JtYi3JfkmqdOxf0KzrlzP6gmeSyUhtLOp5OaFqdnr7NzWlDLk1NtKZoUcjDZ+Mfd2ScufMyy7I8/vnx6GY+mnwfMf+818njc9//s1PFxQPj2yul+uAxs78td1pe/qdfPn14qN4JaPc5Y66QNnoeR/3TC+vnfelsxsugf72jHd2S35u1YvrGD8c+NXqLMa+um6r/VedLeD3o/vThtPf7dQ/3teaD9cjcvLcbT8X8yB97JKw9U35r8m2vX4cv4lwnjqx/gRXYDnpfB8+j504vXw3BFbv1tRpHfQFWM9j7fgIyHteMrkJff/g9+hSAl2SUAAA== -->
