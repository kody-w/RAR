---
name: "rar-cowork-cookbook-adaptive-card-identify-strategic-initiatives"
description: "Produces a reusable Adaptive Card JSON snapshot of identify strategic initiatives status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_identify_strategic_initiatives", "rar_sha256": "69057dd60e40ccbb810b1f5ad7761bdba169a94697d40ae81056f5615415419b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_identify_strategic_initiatives`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_identify_strategic_initiatives_agent.py` and in the RCI capsule.

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

Identify strategic initiatives Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of identify strategic initiatives status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-identify-strategic-initiatives
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_identify_strategic_initiatives_agent.py` and embedded as the fenced Python below (sha256 69057dd60e40ccbb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_identify_strategic_initiatives_agent.py` first:

```bash
python3 adaptive_card_identify_strategic_initiatives_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_identify_strategic_initiatives_agent.py   # or on stdin
python3 adaptive_card_identify_strategic_initiatives_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Identify strategic initiatives Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of identify strategic initiatives status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-identify-strategic-initiatives
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_identify_strategic_initiatives',
    "version": '2.0.0',
    "display_name": 'Identify strategic initiatives Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of identify strategic initiatives status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-identify-strategic-initiatives',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-identify-strategic-initiatives',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '81e43e4f7032681f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/develop-business-strategy/identify-strategic-initiatives'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/adaptive-card-identify-strategic-initiatives', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardIdentifyStrategicInitiatives(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardIdentifyStrategicInitiatives'
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
    print(AdaptiveCardIdentifyStrategicInitiatives().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816a7uiyJLuX3HWfOjqoWrJHan97Oc5gAqIgAqo2NVPFZdEkKvcsaf/+yTqWtU1vfc+p+ecD8e6LIHMiMg3It6ITNZvL05Th3n58vnFAE42EZ0kiUJQTpzMnwh5l5cx/JHHLvw38fKsLiO3qfOyevn44oPKK6OijvIMTt+Uud94oJo4kxI0leMmYML5DnzcgonglP5kZejapMqcogrzepIHk8gHWR0Fw6SqS6cG58ibRFlUR844p4J3nbqpJkFeTkDqAt+PsjMcMPGdKnRzKLH6CB84UQJ/wjEmcNLqFdoFeictElC9fP7l148vEfz+8vm3Fy9xKnjr5c2m0ST5aYDxpl/+rh4KSpzsDGcUA0Qog9cFKKExKbzlg2DyvPpQgST4OPmP/4g7pzxXP3/+kk2eny8v459dk03qEEzq3Klq4E88p3DcKInq4XXCJZ0zVBCwuimzETqIBFzl62Pmd0l5Mfn7+OzDQ8nrGdQfvrzk0ARnhP/Ly88jAl9eymb8/jpKKT78/JrkHSg//PxdTtW4F+DVozBo9evX5/VTLBz4fWgU3LX+HUp9ONoFX17+sLjx87B7XCec+fJ6yaPsw0NwUeYtyJzMAx9+/mdivRB4cRJV9f+R3F8egkPg+HBNT8N//ngH+dcJ8lzQu8x/rraAbv0rK4HD39R9nDyB+mey7/j/N9FJlMFgfkP8H4r7RxOQv09++adr+1cTPk6CLy9zkMAgLscs/Dz57auxWQi//OR/v/nTr79D0f9bMUbelN5dwtfUyaIAVPXXr7/8VN1v//TrLz81BYw1mHhfmzL5RzL/Ea53PT8g+Bz14ce5UL+VxVneZZP3SJ/8lhf/Vv7+Otk7SeR/v199nvwxX8YPMhkX8ab0AcEfcqaCtv4Bx59ffodckcHVNN79Mczyf//3iRp5ZV7lQT0xvLypJ9DBdZSC0XgzjKoJ/DvmdgkgrlU0ct5jHIz/0cOjxZDovv0v706ln7wnlU6dJwt99SANfX0jwq/vRPj1D0T47XViQh15GZ2jzEkmO26z+ZI5Zzhn1F+UoAJlC5nFHWrwCXLSp/HLyJTf/oqar3eJr8Xw7U7+0YO1doI8MlbVJOB1XPUhBNlzjR6sF6AHXgOVJbkHLQsiSLsfIRpVnkDWr0eEqjhKkokflRCOvBzusiGKn0dh3759cyGZf8keFEtMHgWlmsIB7+ZMPn2CSwyS6BzWXzLghfnkp99+/2nyn5N/NesufNSxgbT/9BG08F6DYM41KRwG3QcdDgnl7qPffn8CDcVksAJCj0ZBBB6TYczGwH9D3ZC4TzhFT1wA0YZIp0Ve1vfqVL9O5GDybi9UOj4amT3Mq3rigwJk0AveAKU6cDnvSGawJFbQEVUwfJw0Fbhr/eaWzt3EFCa/U3+bqMIG1pE8gf+NZt4Hwcl5FkH432PicR8KKX+qJvybiNeJNkbppHBKpwhL56kjcB5+gfXjbToU7kwy0H3JxuIJRqjuKfOABw6CyHhPl34afQ47gxTyg1+96b6PccZqZ96rXvklq57p4JSjKzxYHqDScxP5Y5H42zOkYGfQJP4dP2jpKOnpBf/plXsMyv+6bzAefcOPzceXBkcxcvL/SZcyroITxd1C5MzFfLLQzJ39QHfssUYvPNoy2CTcJd8z6Xvj8EY7b+z7JUsiGCrl8LfHyLtPnmMejNaUEMIdt7vLhwEB0R3l3uN1jL+yHCPd+ZK90fxHiNCd06DLYHLD4B9j7k3h+PTN0hAudLz+XvLv/oVQwoiAMTkpGjeBoAUA+K7jxdCqcsy5p0dg8IIR5i6MvPCHVU2gdBgjUP4EGhHBLIKl4A6dlsNlQpiDMk+/D4/GRqp4ONifwCYWvE4OMG3G0KlgrsJuaBwDUfjpLmqSAogxNPEd4Sp0iocxY9/7NNAZfZGn0PV/9MDz4fdAv9symg+lQtqtIZbdSMI+6B+efbfz6StobDqm5n3Sj+5+rnXyx3r0ty/Z3cZ33ocZn9zj9zs4E5hpaXWn2JGwKkg6KXgGEIyEe9V+fRTeR2V/t+Xzn5r9D39tP3AvpdaPnvs8Ceu6qD5Pp4/y91b9XiFdTGGMRAWo3ivhp7FEfXpLtk/vyfbpD8n2g44HZJ8nf83OH0Q8A/zzBHtFX9Hx0TrywBjBzw+ERfjE25/I8emXbAe++/sZFCPxJgMsve9V6G0ILEXnEpzHwY+qVI3FrIP1807D0CNfsveYeGYMZPnsPJbQKv9DJt/LMfTww4Hv1QI+ymqo2x+bujMYtz7JaH4FXj5nTZJ8fMmcFPy1Lc9YHGAAQ1zGPRNMJtgu1RG4X723TuPFj5u/e5pBfvDzz2O2fZyMbe7HyXvH+nHytoe4b9CyBm6ifhm75VElHAp/vI9931m64AXu3+qhGNfw2BiNTdqzef6zEWOSQYshu1ejLW9ZO2r8kxD45XwG5Z+F6PcvTvKkDsjuY/mO6reEr6CdPmyGIKm3YyLC3IKU2cAJf1YD9ZTg2sA66Y/L/Y7f92Xlj7X8foehfuwuf3t5o5CnD56dJBwOc/VTNVbKKYxYqBBeP2ILPvu/6jGfsiABwr4GCqNZlGJ8n0YBiXqe684w1MUCyvEZhsZcyOMYzTosSbOMT6IOgI8pOqBojCLHv6wL5T2i9evYGkSjfbjjeDOPwUifZRzaAwTqEh7AcMxnCIBSLBHMZoCEUL1PjSF7Phf9WOSI6Hu7O4LzXPtvLy5NwpESWcnc4yNM2b1D44y7C12kpIF9OrKyG1lXw239bRK3dFnoWl6lc3CrlrlVVgttWC0wzduddcfyS1EP5yyXMatN4zcBl/ZuXC3rs+hG2O1U0Z5+CtpABLnMheINU3Z7QsFsJr8C43hQ08WQUMc4cbtDmmBWq+SYjibUdju1FYM12bZpW0Y8FlZZ8nOVVNBDDU7DqnP66VG6TWF76i2J60W5ng6mRk8T9+SWe3PVz+2DY5Q3zXC6RK+1UuB35k3iTrYbpBtNmSmovqN1s0CnmxtFg3ZeMkmBs0A6IvYsBO52t94vqVCbQda/asoB4Coh5hfNqsnuoJ9QczPbH5bD0eIuEV8nakRRzbGuVjQZ3xojtReKv5eswspOiJcyC49K12ge7fdeBPY73ksKuVIh8x8VelFene5WWnm931IDthtC/7CH5HKxnGnG5yBuydo42o1HkSl32KlLdSrPJLCkpAPoMPQqa7q7Wh4Ngdeb1VE/CDepucVemvo9KQ4AGjtXc1loZ02VhFXoKRSp9Xv66NSF1qOJbGFXtMDJ0Aj1QZo7rH0AwOmNlandtlLfz9ztoSttrUYxPjy4RBhqeylJ9qIWT4n9smKaQ4GJ2HktdtONpcRLZ9v3G+DtJY3h6SzPCQyGT1CRlMWv+HjZEKxGlGZ+2WMJ2jUEOVPLstf22QnMp2tzLeDLVNwra+DMZZSdRa2mpXl5XN+4GZ03i04s1eMp3FwcZa1FhRp77B7k1z5jKy9akreCioQuY0Q7myvA7KzK7gw63cgbPQj2sxpXnKtQ4vat12+qJJVdvKsp8iwftmeWGpjNKY9IX3dNSCkx5gzmvkbrcm0dGFVHmUXRdW5/ns9UidzqaiB45taTrtNqEReM1gZFz549adccIpbRV1zcJsSas8WVYlXKhSCsQUGOhR+ZJ/VCDp2/vLQLTXZ65ZhE2MIQBrKPu6mOcXyRY1Zi62eSwtpcm1bUrZOnogXjke53ouIH3ambdyJ62JmsldtVUPmxIQmSMWztbin0jtUKYborUMoMe5U5XvS6Uy4kjdQX3AWGjV3kbKVSPGpqNr3Sc/Kk45JeCGa72GX7DYok64uCRNM+lTrJuhgh7ENxHDER3r0i/sUqDEbdROgVaZFlcWGBZefL5XzDhu7JtHz/0ickczl0YlrLA+ferrdCNKkmInOE3fXinOAW8VFYbGkrSjVEjucxHy7C/tBI02Olqm7uo3wfrHYLEATTLIOhuAR6bBmz0LjWtx1qFqVY7QMMwqIq11hVfSlK2fIgHbMVZUa+ga1zQ98dWXWVkOhU6ETuxmuWSOQgWGC9niPULo9ODkd42ALJzbIRFqUSHN3DysrT2fVIiV0k8MNVWfgtptDLdVVZCVesVLPOrapZ80fJq/CBkeau7HqGQ57Tsq9PqoPdloqAM4Z1HQpUOTjDYla6yVrnUYHjsnJ2dW7Lukf6WbHaYnthWvdtews0WSUhcd7WperoMnvVap/SUZN2eoAy+eYMlPm5ptnpDJynlVjr8eVWySp6SlairtD1zRwEqT9n4lFO5kSc74JUHGZpYt9m7iC04kJKmkstbCULMqSRMVQMRNManNWQY1VgznCn3c6EOiA7dJMq8Qwf0G3ocadC8URySAljhU1zmiLRdL6YqVeB66jV1i5l1hGLFCsDTJquj5cby6lYsdMw+aKZZ48u7cWJP/E3YS0WObdWmJvGqwvb6Sil7yjmEg5zY4m5/JBzh7oM8fIGC+OcIsSUvKS+HzB+xeq3Ze9nK15GTTFdVQiJmFG5um7ObuK0dZZv55zlSFnbUqQxcyrJPXqHLtCEUGgh8bRt6AVriR7IzUYiCArz9L3QG4Qihh2u9DOLSrecaO+qSKFyDzWzNIF+So4KlVmiwbeVjdxEIHZzBvJDRNgCwfsX8QY7oM6Jge1724Nh1QrKF1rW6VtYWlbLwMihSYlVeL6lzm/2DWKs4sKUWQyXKlt12KVbyrPEUgM96Z3g7La0Xiw7h8DkbueS+EX2bDVlsv26FU4L1i2LwlpnEZY7C5YwSXUF61hH3mhYYU5ScMIzlb85lwrvbUeznczGFV6aIz0vplpAjE6D5Xm24eVwrRi7cntbmh7db3CkOTUDQHey1fIYG5EnAz2fcJxfmatUWwtxX6ENcs16NcAVWgij8tyKOJLM53tp0e14fsvGxqEScWG7NusO9mDJvBYuQ9wNfLBsFu4x6df+2dHRg3YZohWsIcVebTRFQSO7UAZeJsg54EXbZldb1u7TdoabF0pYaEuhOMim1pVkczWv+8ibIQuq6SLOtJcWGzRN4KKnqzrguXwBrsjHOARck/I6wTXeQWREPcx2Yj0PMhg3DX3YSjN2Rtuh52UiBlrxmJ+KzclD9w56hR4mmiTfRwHjXSz7Iixxu96eQsk5tha/TWvSuipTW9uY13A1bPpVuFz2J3qepbZggtzkTx2roC26XjiGbxmMrYncHtq/nq8rPc/TQ7otde5s2dqVQ5IFk0yZXbLi0/PGNMspwRdh7tUkUTiiMS+wlay70Yw5xFLp5NjVodfyVV1zwXo7J2ZTAI7NcnsTCthTyDrFbRGUNrudVNIi8LMyBTJIjhhS+HPApLuq3cGtAgpBKekkdZR8J9N8vmbztbBw8zlvnV1tTqU95cNqm4gS0u2FvR3msn25KusEBxkmIBrYpghFSoo2bawraYuHM8duscKgBk7RI7ITbJpIbpp8tRgUu6Saw5CGeDxSiYViFm4E52XJ2dwlmLvIwRZJdIFSkqmAarscTFaJd816ZS5gNcromNa2Kz3mNi5XJfL+tpRDzHBMRNa8ep3C1kOLVUZYR/y0jC5sasK20SKvRMbX+FyyfdTRmNNVNlJL64/aFjT21RDD8yLUjryqrg7bCI3oKxiU86rw9B1mUbIrkmQEEKPaHXYL3Sg2g6q23WmfsavwNHMsphgqS+TO+i1nLGZxoNzDrtAtmqJSTBCnaLJ38cDMTToMBH8o400aZp3v49vZSRa9PgXh1Dx4rrA/72B3MrudLPM4M2bRFYQkn+K1vy5ns8sy8jMly9MsSKeOdUIYXQC8v69MxxV2kUUWvL+Sjst5KC+UmjBUa876sq3YhaYbaI/6W9zpNEZYmred67cyQawukotKEl3rWeGQdijsjp57UnXXShyLq0IDtc3bEqo9rWEnksbQlelwoC+Qa9q5jC2up8WK2qI55ppd7el+u4BRd5HdaqXN1pdlh8X2Ul+sqtM+GU7pMJw6pjfVENvEWeGeUGN/05gNctqfeT1vxFOtaksvJ3THu6GLo55xV2SxSrcFouytPtnBvZWzhQVmFZWieRPVqWIbFNVuD3OOXvrMAdSmf5CINJFXSjX4nXzK9t65uc33WsXye226EKcOmSLnxRondjpKqjyDk77KHNLrrec1ukTceJVSMTuEV0/WSjenJLEoY7ORvTM55wJ0nndLYJ7nx94WMxtVlnMtJtFb4qB4RnizdF9t9uIWP9NXnVg6ZNn52Q5rYZVZGaonLHBhNa3XUkRqcrmt7ItqectQztGaIWMt2YTZXubrOjDVix25FwZd3zonqA+7Di1O+/3QzOXNfHA3KdDy4ybJtsKiRvo5XgSOyBzniZua0bHZN1KPDDktlXht1lP8WkbT4lDhaeBI/NQviVPLDVPmDPfmg0+h+EE7n0SavCFCtM3LgmBYUbX6NDFQP8l4SmXxgJt60XlIGIZYn2DW2f6+VLHeVnjL262uoW1hmB61m3DKsaxJwcIarjcyjeBS5+ItUtiWKPCNfWQ32bFdd2s6ri/ryghK28iW55yp5lrmHN1rSh3EqtpIu/SE7H2R4rAiRvQuoWc4eyl5pN0NcwkliCmzNJHzkU8OThtkEqJkMUvoNEkRRxY/A1bx14JHg85a7GDfI/i9xwoIf+Nac+AMnDCVAF3EcWcL5XGqV6vc4NDhdADypViQ55ncemK3X8rTqEt3DJZ46f64bk/efBPVAzvol7O9AYyALcxhuUVwKtNtn9p21xhf4eFqd+KP7NJxSWy6CQdOm651drYrpNk6bJuGK6eyvcmGeb5skxrDlkf5qKQIZMWTUmnaRdMRCVZgopoL8RnZR45AO352U8VwWh9IBk+IuJ6WAVJ5ngxgh0rwms1f17KUuvTxyKH1CveJ28K090HgdEDdBTcOV4v41GglhRyTNpHqjT4TVvjU0m3ax01kQwDr5vLa9ryaOphdnweTuiR0w1X7xhvWJCnv/NPCa3cHypmyK/TC84NtI+aqoeb+ovIHrzlalYnJ/Axuli/LPj9wtqoI2gZ0nih4vTsbqpVP4ZlEnDdLodtXyzUZ8Tq2WW5YW5UuPb20D+epxeMyLG4I4TB2wnkHiRdSYcor8RoQq+RMouKCmvOHS3ADYSBZrhWqxPQmkwYI9a4ctvWA1T0Bjq6aNAs8yIqVFvmp0x0lZ15l8a5CwXw4myEGvB3TErJ3Yb0dgbvExj1c3HYR7vjMu+A2uSQFW+9zWxlCjkUCnOsOZb422fQwbTzN1niqZLrmfJzztpamLnU48QUxba7s4BQlsaaxdtct5xlVlRx6sFp01fIcLjWccSYLZDZFF23LVobMqaU0g1v7GRpfKD3MWZla4GawV4lyThoRRoDFYWbPt27CxiTgmWFaBHDjjA5M2SaA8ilmtu44t7dP03bdY1ep5kux1eg+6TvWZY82QpnX1dFHr3gAAj9iGBuktJMx0+DcTgdxd4ss9kZ4p9o16ltsX6glEQqpzF/6/aE0CBuhGWkLLk4468WySMuppyBrKgr6yOHz1WoLyit5BQET7he1eEOkxtzywF/5lUbgRbJMZ65z5E5GgfjLq6gEPLEla92aO3PeMUI+pXOb9Eh/fritE5pGM0gvwC/1Y31p8en+XPG5uVSZa+AVINunnBSSMz1K62tXtrF0gNtdbm/Ku953uFIlPVy+lkNG5K411y/q9pTE5EJLcKpFc8UgqsKZn5hUIulBcNmWgQWQbCgAuFWQtLt1taTRwxYfBtosAFNtvFlGrsU29g9MvIqHBUklHgW3cmYF+sPyOLtunQvSm/qprqaYnXOQeNZnfcEx+j7C2Vw2ZDQm5LNZjfmCyJWuBGruxeTtOAN2uwHsbS/lKtOeZv4lxWE/usHnpCmUobLluJePL+Ph9POI+X/0onk86ft/duD4OBt8ewV1P14Gjv/5ruvz/8y8Xz++lF4EjXsctlZJc34eR/63o9ZPf+UlxihpeLzTHd+g9fXbaX3tnMffWXqJMr+BM6F5edLcD34/vrhNNf7WRPX1ecD9cl9sWoyn5T8sbnRLXgLPqeqvdf71ebgeZeObIeBDE8Dz8vw8i/744g/QiZFXfSVo6isoi3Hdzzcj47Ht+Grk5ff/AsyzSg0pJgAA -->
