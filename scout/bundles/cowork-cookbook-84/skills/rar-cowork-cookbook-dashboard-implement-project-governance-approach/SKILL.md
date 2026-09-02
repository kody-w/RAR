---
name: "rar-cowork-cookbook-dashboard-implement-project-governance-approach"
description: "Produces a self-contained interactive HTML dashboard for implement project governance approach - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_implement_project_governance_approach", "rar_sha256": "751d973b017d6c97c2a59abc7b0021edec3018a1133a4a18f7cb5cc620b839f9", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_implement_project_governance_approach_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-implement-project-governance-approach:9687b3b55ce328422566507bbee10947220619ed91fd9104c09b5c60ef3b5c0d", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_implement_project_governance_approach`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_implement_project_governance_approach_agent.py` is
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

Implement project governance approach Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for implement project governance approach - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-implement-project-governance-approach
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_implement_project_governance_approach_agent.py` and embedded as the fenced Python below (sha256 751d973b017d6c97…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_implement_project_governance_approach_agent.py` first:

```bash
python3 dashboard_implement_project_governance_approach_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_implement_project_governance_approach_agent.py   # or on stdin
python3 dashboard_implement_project_governance_approach_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Implement project governance approach Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for implement project governance approach - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-implement-project-governance-approach
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_implement_project_governance_approach',
    "version": '2.0.0',
    "display_name": 'Implement project governance approach Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for implement project governance approach - opens in any browser, no D365 access needed by the viewer.',
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
        "upstream_slug": 'dashboard-implement-project-governance-approach',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-implement-project-governance-approach',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9451820fa3df0809',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/implement-project-governance-approach'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/dashboard-implement-project-governance-approach', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardImplementProjectGovernanceApproach(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardImplementProjectGovernanceApproach'
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
    print(DashboardImplementProjectGovernanceApproach().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816aZei2JruX6GjP1RVGxnMIHHWWesiIKIIKihgZa1I5kEmGcXq+u+9USMi69Spvqe674drrogQ2Psdnndm569PdttERfX0+qT5dg6JdprGkV9Bdu5BXNEX1Qn8KU4O+IHcIm+q2Gmboqqfnp88v3aruGziIgfbN1Xhta5fQzZU+2nwZVxsx7nvQXHe+JXtNnHnQwt9LUOeXUdOYVceFBQVFGdl6md+3kBlVSS+20Bh0flVbueuD9kluGm7EfQFKko/rwExINoAOVXR1371DOUFxOMUCdku4F1Due97gKUzQE3kQ13s9371AmT1L/bIpn56/fmX56eR5dPrr09uatfg1hP/LpD0LsvmLor4IQn7EATQSu08BJvKAQCXg+vSr4AeGbjl+QH0uPpxBOEZ+o//OPV2FdY/vX7Nocfn69P4b9fmNxmbwq4bILJrl7YTp3EzvEBs2ttDDVV+01b5DVGAex6+3Hd+UipK6O/jsx/vTF5Cv/nx6xMAqrJHq3x9+gkCAH99qtrx+8tIpfzxp5e0AKj8+NMnnbp1bsD//Wa6l7fH9YMsWPi5NA5uXP8OqN7t7/hfn75Tbvzc5R71BDufXpIizn+8EwYYdv4Nzx9/+jOybuS7pzSum3+J7s93wpFve0Cnh+A/Pd9A/gWaPBT6oPnnbEtg1r+iCVj+zu4ZegD1Z7Rv+P8D6RTERv2B+D8l9882TP4O/fynuv13G56h4OsT76cgCivbSf1X6Nc3bSNwP//gfd784ZffAOn/KxmtaCv3RuEts/M48Ovm7e3nH+rb7R9++fmHtgS+5tvZW1ul/4zmP8P1xud3CD5W/fj7vYD/Pj/lRZ9DH54O/VqU/1b99gId7DT2Pu/Xr9D38TJ+JtCoxDvTOwTfxUwNZP0Ox5+efgPpIgfatO7tMYjyf/93aB27VVEXQQNpbtE2EDBwE2f+KLwexTWkP4L6m7aSZPkl875B4O4Y7iBF2G3aQGJlx+l7xhs1KALo2/9xbxkX5M57xoU/MuXbR5Z8e+x5+8ySb+9Z8tsLpEdAiqKKwzi3U2jHbjaQHY7JFfC/eUrdZl+6UYRbZr7JtOOkMf3Uber/Dfr2F3m+3ci/lMOo4tcc2Oye9Rs/K4vKruJ0gOwxhzlD438BeRjkmapIU8d2T9D4qy1fRtyMyM8faLqgEPkX320bH0oLF+gRxCB3PwOHqIsUVJFmxLg+xWkKeXEFBCuq4VaxgB1eR2Lfvn1zgBpf83uSxqF7paphsOBDYOjLl7LygzQOo+Zr7rtRAf3w628/QP8J/Xe7bsRHHhtQO27wAUdPoaWmKhCI2nbEayxTwP62d7Pqr7/d7TJKl4PSCiCMg9i/bQbUPl1k1OBurHdLAZ1HEf3qwen3uEF9BHCB4gagBeK/fv6ajyQKsLTq49p/B/G++Q79u+nvfEab1A8MgZ2Cqshua2/eORrTLSrvBZIC6AMpoC6wazNaNCrqBjg0qMuen7tjybWbTxPmRQPVIKbqYHiG2hqoOlL+5gDSIzgZSFx28w1acxtQA4sU/BoBurEHu4s8Hg3/8N37bUCk+gH42OydxAuk+ABNqLQru4wqu/Zv6wL77hGg9r3vB8Rt0Bz0n93GLdpvnif9Sw2I9I9dzEfTAH1tMQQloP+PO6BRTVYUd4LI6gIPCYq+s+4+OQo5cr63gaD7uEl0C7DPjuQ9eb2n9a95GgM7VsPf7iuDmxve19xTZVsBGXbsDnoHobpr2gBnGr2jqsYAsL/m7/XjGaAGdK7HVAhi/jRmkOKD4fj0XdIIYDdef/YS0N1Px/gBEQCVrZPGLhQAIG7B0kTVGIoPKwHP8sewBLEDQP1eKwhQB14D6ENAiBi4OKgxN+gUEFKg/7rHx8fyeOzQyrvRPQjEnP8CGWMIADeuIccHbda4BqDww40UlPkAYyDiB8J1ZJd3YcY++yGgPdqiyOzG/94Cj4fAncdCBfh9xCqgant2A7DsgRFAKF7ulv2Q82ErIGw2xs1t0+/N/dAV+r7Q/W2MVyDjZ/UAo8HYI3wHDkjyVVbf8hao3qcaZITMfzgQ8IRbO/Byr+j3luFDltc/DBc//rX541aj97+33CsUNU1Zv8LwvY6+l9EXt8hg4CNx6defJfXLR9h9eYTdl8+w+/Iedr9jc0ftFfprov6OxMPHXyH0BXlBxkdy7PqjEz8+ABnuy8z6QoxPv+Y7/9PkD78YEyNI1iDC3+vT+xJQpMLKD8fF93pVj2WuB5X1liZv9ebDLR5BA7JwHo7FtS6+C+ZRp9HIdxt+pHPwKB8LhTc2jKE/TlbpKH7tP73mbZo+P+V25v/liWrM38CNATTjVAZug26sif3b1UdnNl78fuS8BRvIEl7xOsYcqJWgi36GPhriZ+h9RLmNgHkLZrSfx2Z8ZAmWgj8faz/mWcd/AhNiM5SjGve5a+wBH735H4UYQw1IfMu9Y5V5xO7I8Q9EwJcw9Ks/ElFvX+z0kUDqxh4rLCjsj7CvgZweaM+eIWBIEI4gwkDibMGGP7IBfCr/3IKa7o3qfuL3qVZx1+W3GwzNfXj99ek9kYzf7w3G3YnGwfZ/2BOOCL/X8reRjz1Su3VuN8BvvfAbUDYea/Z3j8KxAXm7u+jTK0hK/vPTCGsVgwb/epvjn+7CAa0+u2hAAaSXL/XYg8AgwgAl0BmUo0YnkBq/YzDejr3b+vHL65+33v9annhlqCnt4A5Juj6OTQkMIymKRGjH8X0UYQgawxAKZXyPQQPwgxAuwjikSyF+ADa5iAdkGq2c2Q+ZYHS0D9Dmwwj/2+ng6U4OFB0gG6BHk6jH0LiDoLRHuQztYjbJ2I5LOwiCoaCLcHEEndooiuM2YaPTgHaBpC6FIc4UZwJmpPdoSO8yvr03/+8Wu2ePN5B+s3jUALNtd+rSKAH42hQACnFw10cx1KNxHyEZPJhOfcK/YXHf+rDaaNQ7DKN7g14UdD7dyOfXhxeMLksRYOWCqCX2/uFg5mDTBu3sIoepKN86mrDkxPuz5jXzM9Wb3g7JeY87bY+yV+Ts3DvFark6lXyi8Fgj2LOu2AauNBmOBL0YdvPVntatYt6ceAs7Thw1D5oLXaX8LhUQvzqXXCXsji5yrkzCMFzUoE5VcSr9oyVfuS1JNZinDvOyzBun1+hlZ15pMk3o6FgSVZVvcGyg4Do6HMlTn/Mqr8aGQFwP3tFN42XuVmHvXNw2NZzBmyCTo11opSX0l7puNNqglNNyY6xyq0BgGE7yRAwsrJpt4wvplGlzqHqbOrUzi1oUqJpfL6Qf0CdmY5IS7kzgjSkvMBkTa/Uktbic4eemWQ34oWQoeYvL/vqgGx57hQV7yOpqb3S8cl5yJZlXNCKg7nBaCatjsj0ujKRweRkh3doQONpirIuPlnyt2FrF6/Z0LrWRfcrrWaLa1PZs2OKgUUN7cGov2VoMSrMOvKV0k03zxYAMM70b1hEc+ce1sc4UGeP4FNMOSBjqeX5YHcLzKW1RUhZlBV6EztI/tYO407ZKQJFyJg5kX+Ur1KvPnpFlxKDbqUAeJl4tO5qEBV5lJhuv57NypWzRq7u4XFBri/WJpUQTNEoO4HmqpDKFnHNx6JiqNzqt0eN1xfqbyPepvbRCoqT1p+RZqQwZX18OXT4cLJi+9EVrLcr80GC432xixVRNnaN9PR7aTjgYXkp1Q0RwtYfNM1EiLCTaYupm2qz6xiukxQD3nVgiy4xFLyl9XKDNnGwva8xW/ZVpHImEwRih6k8JPptHMlZfVov9NImMs9XHV2dx2mSdeYAVzDm3q6saXPUVvd5sKuJ0aY5FKBnb09UmlRqLHQvlAqsR2t7exz0c06q12GCWVWHLICLyakNPHZxYnOxJesxCf3OAraVxpTwX1nmYJ9Q4pWbXZouI2oy295fY0etzpcjCZTkRz+nFKrIlcwyWZwrjxHptocpwOYfKrJy62PFsrjAhAz7RHScngpx3uVrFU3luKrzkrMS0y7dcy4SnOmHVbaHtV9gyPNGW7ibqaQfumpy8PF+1tbreU53Kc766zKgpOWtnSDA3rydcJ1aBqiB5lU11etmm01OvB4mMTB10r00svhZLOkfS7RwfjlF3ncgkhbqEfe0YuId3XRzWVuPuO4e3Er+u4Hxlbcy5qCSaJJ2x+DCfb3vL0pmQcLaDavdXMs616AhHlz1jInuGOiYESnalmCr8TN6fa2FGbaxyO6/OBS4dfRifbx1m3p0MvdSOmsnHOzU6dxvOPh5jeJ+X8nHSNrZ+gBGc5662ZvQlEezlWakl/VKgdwSChI3OyavVtQK1bz9USyJRD+KBWuTIfGteZXBxjGleSmBUoqpL1/ECzXlBely6UpWfc3J2GPilZxsxblznzCKhEMM6u9OphJ0k44Svsrgt1hzNc55Ug1glkqzO2QFBLEN150PVGkOSIz4WaeI0JjpT05C1tMgrfJ8sG8zKSFjCZ+l5eQ0WE1jhjBDhqDW/3kUuMt2C4hhPV8wpXSP2pcC3Hsec5kcaDSL+Yksh3aGCmk54clGXkhTi10SeOSy8FoiBnEv+NFVVK4QXJ2yzsPQjaxR9ND3vmd2+VQS+yY+Ta7W4hFjtZf7Zu4iorOYVtpEvoZTUq0t0rstYRdw6rNblkj2wu2yy3W6mszrUVpZr9lgmCPwpi+IuVFijtI8NN8xcD2XT02xllHNz364VcQafm0I7m9LEYompJOyTet1OBc7KBDbKIw1ebA6TVlrtltV2qiAinvYGijXtJjEO58ITjnlu4jSjXqcTu7kKYa6VxVUwHA/WuWp53qTOwa6UvNjy6729yAuTnLpTkVg4jjvpW2/OCcEmP5KwD/uLWTfosJLC/qTd+Cl/0eCVWEXYipwaTLtlF/IsKfUYUa2LTPQhuzTl0h1stmZxHAmc8KxyETGTC8VwN1v3eqnj7OxmJWfkPkjxkaIdFJuck1ym+UIi0dOVS53EOLUTNWubRQRXOwMheDpmSHeVLLo8qSo3me8XyYYOgoysRSprhZKrd8lmhpnLhAmcIT7uDvTVTlYk0dl21DMlsxaPbF3MD1d7X3NJhV31mJeYQ+Zw9VacKv3ZMcUY8YHWGddrTHtphsHFfSmL3WLNZ+cDhsuLJR46HezqTehJ8a5k7CORE/28lC5eL2oYwVmi60mWinbX4w6PJ/HGAdlYRA12KuJqcbELkuNMYpWD4mpnuWjJO2W368SziEfcTPBOS1KfdUi81xqOA6VJbrjYgc2IG+ZTYW/s9qR2PHFbdqfEpx0iZthhY7iigyRL+lR4+/0q8lLtwroofNA14pD1B00R1W7dznRlIyhFxhQV458LDiGEKHR8ITPmM76io8o9gPzgi4uVciwit7LgNSPC/Obs2DqrxG5ndPkKZ6rViSKz09koj+vJkt4e/FyKxAhj5sVsNb+2jB1X6pT1M20+rBxNCVp7UeLaiZwTGZGdjzXMmmE7azr7wja2bxOIcUHKIWlDkCbacKgNbbnNB1bW4ZgPuwW7HdZiNoOd2NFwptBO/RXhNtsN3PLOfk9Qh+qIuOFcpzBWz2ck2u83Wdrk+0bZH/Zzk1O1iKanZOCjnRRfWVJCDGHhh7PAZ1bFMil7I2DkqvakNjVR7BzwLZOnp255InLawEA/aV0bVZSEI4eSDHaYaSqArdgqVVjVc1AqXXlZb8iwdc89L+wvi9jozHII9maNklG1lqnZvp1RoSkbAqIuctWTNPQczXeuf2gtPsHNvbo/F2a3R5cEYXW7/QJnq4OsHJpiQSh+L7ISfjVg0GD1ykxRGwRRpDWzytF4pl3dw9aiycgoh9WEBYRmrLaOWOo4kyekQsTkBWn3GM7ZYCXbSTnSrIKJtbYo0C00gWssifUiJbcLuo/rVKK3sKCRS5pko6WTrXWh1HRDjyyOseXVsq/Ohp/2R/mgC2ljm9HKtrPLfMfuSLEmpJ5iDFTUo3quVFrOqIc4608c5uX2aR948SE19NO51eZ1H3XM8aAyKUIJjO6I2ZKe51LQLDbhMO2Memuuj1UdYnicdflsuOp+65VhVh6W/IVWCorSde+QSYLT6pvLQZlMSayir32DblkHRXQXV3exgJSz2Fub80UoCaKLJ8KBv+xk0BeeGvOwtyi5mSx7BefmW9DCMHxBI0tdpZBj0NsMriN9uphzlTNZr0QUrYyUlaV9I4rTfmfluz1rz2ZzI6S4sO2NcyUfkXy5TNnzce9R2/2JuZ6zUkYvOj2l/aXLRaKFH2063ItGi2xFP1zWxzS9VAYzIaX0ytcRQGLnXI/K1tSXdIetzb4UC5XSaxcV/MmGM11qvthowLCBIYRzrtjD89V5P1iXcqtsj3rVogof0Ylo5uvldJrUM7+ftAcfLY773GmZZapxluAQ7hST1czu6BWqtszMVGDRoKOuuIK2zWszl+xdHm8YfZ6V8xSfcHTGerzDKSsYXV3DcN+7eyPXrwcqXe1Za1X3OM8S69n+JLmyKx4jxMvOW37OKzG5b/UlgnVobYWoa3ose04oylQFWiB7jw9olS1jTdCo07wV5Wq73uSItWyj486fEYS+0i7EFSujo9wn7Lk/kw4w25xGQeVCXDaXt/WU0fT+vGrrLr2I+91OaMNiYhttcJ6chaUN+g1SgzGFXiy0q9oZsitP9YRnZuhmUZqNQx/PvhnZZ9g70hK9keMdBWZQs+1VubAqb0K7s7ChramCzuP9XGjMGpdUhEB3a8o+aobnLU4wcqxZfjgvHHPLu54pMV7FHFp9N4/6nb47nWtyF/hCzMETnJCJiN1LDSI0Q+ZcLZsN7GqSzCJbVWE+2E8C1arY7mzXG5+UJ7aMELWyaNhdR2t04pqVhs4jgqrpYGjCTpo16iZpVe+08C/Npa0vw2aD4DDN7ILpLBDOtSITJjzVArxe0hXeYkGQKmZRIEiDSJVh9oKIaHt/lxN1uyyX6dFrjwN/8Jg4ACPXCbHUi9mJobRUOUQa3Oml2yYx32cM4uzc/XVSSZTqkc6yPNQkDkaTrZzsyl3t8Tu6lRTPns561fODIev8fc1E67g67faZdYS36/mktgdSqmcxBxoHdLKFr2ubrtp1H69kSmqcmUx6XtOYw3zSdOtOExU5PHNBgfXMEcfw0FpHQgznW5PXGxKk0k1zxhcq0g2IM3VgPEmixTXOKCbB2GPMLWlMzUALsth6GTm5IoNgOo2vYizwy9w4JNbVQBlaHmAs8atstvMI3974rndd44FKmDo9UyJhPlmmzsaaGuAKq63eaqfislpuiqN9MutdzFhwJiM8w/USmAFLapp4J2WtId0BIaYkoSCWfEnFvTuZc/1mVmmXCY3wYGTElGN7vcitWvcTd9ZXxjovZ/pak9Uuu7Rm0PXWmkgaZHNgPc3epn139THSms9nhHbk2l6bq5TH7ayNNw/X26l5xpFJsVcwkV7rm46I1DUNyu0KnpnixpkyyNygOeeq1CRFGVZ2OTXzDgudObymeSHKQZvt5ZkQoJMBY2ETAUOckztGEnRCtONzSiz63pmqvZJc+nnEz2ByYiWK1UpXtS2mILBxsdscLA+rWdKWZ/VZbY8GYYLaWpjHPY3gW9yvGqPh+X1LTwZ3oV2ESdIQktDzPbvvbL0DCUDxTS/esXxqwcP11B52q4lO+BvN3yknHD0oFDqZHxuvi2adyCIq6TvqIvSnDba5+lYz7SiZzFtz5k4kkeMnC34DWkZVseAislBmb6hda9rwhRbxVbFYtrTb04VTFcAJvA7xYffUbSerqFPhUAEDSBcuo41g+oJthWI324vewjsFabcNSRHVybhZ6IoZLA/TBa7AiYTwW00HU5N5saYwHrcSpVSc48aRPaV1oiy7RPdl2OVZc5tq9cUTzuI5mMFbolHXvM2zFMjwJlUWhEswvHqVDlSGhCm18JlKNZukXsKH8DwrtulaLgKNnOR6xm4iYrqJs6bqu+60MCw1ZA+OpF88m+3WhItJ5+6idhpWih53DK/yspeClZfw5Xafd0cOWVxxaXFBUzGhS+ca0sQE9QN2GczznezO0Ooq6TbpzZCOyeat67jzKhh88CMUg0CkpZsW+9qp/Yt4MGFdmuswWZjrduJlm5pzgyTvFyvOWXAI5SPi8mTvZGG7xCYpu4TPS35IlstO2dTkJV0s8CXtXoYFKRI4GIVLL7lSMsa6Uw1hViHLPj0/3Q6Un15RZIriz0/jUcLjQOB/8QY5vMbl24MwThPo89P/u1eY99eJ7weJt+MB3/Zeb9xf/8cy//L8VLkxkO/+CrpO2/DxEvMfXuF++YtvmUdiw/3wfDwNvTTvxy6NHd7eice519ZNNbzVRdre3ogDm7T1+F9r6rfHMcXTTeWsvJ15vPMH320vi/MYUK/emuLtfm7gP43//WU85vO9+PMyfBwpAAIDMHDs1m84Rb75VTnq/jjjGl/4jodcT7/9F1iOqQdmKAAA -->
