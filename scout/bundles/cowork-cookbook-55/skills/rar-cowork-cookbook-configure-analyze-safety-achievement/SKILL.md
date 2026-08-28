---
name: "rar-cowork-cookbook-configure-analyze-safety-achievement"
description: "Applies a bulk configuration change to analyze safety achievement from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_analyze_safety_achievement", "rar_sha256": "296036988eae31f6e4debc99df2499eb95e6166a1417e265a846d775a299a833", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_analyze_safety_achievement`. The original RAPP
agent is preserved byte-for-byte in `configure_analyze_safety_achievement_agent.py` and in the RCI capsule.

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

Analyze safety achievement Configuration Bulk Setup — Applies a bulk configuration change to analyze safety achievement from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-analyze-safety-achievement
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_analyze_safety_achievement_agent.py` and embedded as the fenced Python below (sha256 296036988eae31f6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_analyze_safety_achievement_agent.py` first:

```bash
python3 configure_analyze_safety_achievement_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_analyze_safety_achievement_agent.py   # or on stdin
python3 configure_analyze_safety_achievement_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze safety achievement Configuration Bulk Setup — Applies a bulk configuration change to analyze safety achievement from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-analyze-safety-achievement
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_analyze_safety_achievement',
    "version": '2.0.0',
    "display_name": 'Analyze safety achievement Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to analyze safety achievement from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-analyze-safety-achievement',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-analyze-safety-achievement',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'cdedf87341d7b1fa',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/analyze-hr-programs/analyze-safety-achievement'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/configure-analyze-safety-achievement', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ConfigureAnalyzeSafetyAchievement(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureAnalyzeSafetyAchievement'
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
    print(ConfigureAnalyzeSafetyAchievement().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6eZObyLbnV2Hq/dHuJ7vELuEbN2JYtCEkkNjV7rBZkkXsmyTo6e8+iaQqu1/ffnN7YiIGu6KAzDz7+Z2TSf324nRtVNQvn19U4OTIyknTOAI14uQ+whfXok7gryJx4Q/iFXlbx27XFnXz8vHFB41Xx2UbFzlczpZlGoMGcRC3S+9zgzjsamccRrzIyUOAtAWk66T9AJDGCUDbI44XxeACMpC3SFAXGRxH4rzsWmRx80CKBHEKPiLXuI2Qi5PG/oPcKFxdpKnreAnSdGVZ1O0rlAjcnKxMQfPy+ZdfP77E8P7l828vXuo08NUL/xQJsA8Z1LsI7HcJIIUUygmnlj00Sg6fS1AHRZ3BVz4IkOfThwakwUfkP/8zuTp12Pz8+UuOPK8vL+O/Y5cjbTTq6zQt8BHPKR03TuO2f0XY9Or0DVKDtqvz0VwNtGkevj5WfqdUlMg/x7EPDyavIWg/fHkpoAh3G3x5+Rkpasiv7sb715FK+eHn17S4gvrDz9/pNJ17Bl47EoNSv359Pj/Jwonfp8bBnes/IdWHb13w5eUH5cbrIfeoJ1z58nou4vzDg3BZFxeQO7kHPvz8V2S9CHhJGjftv0X3lwfhCDg+1Okp+M8f70b+FZk8FXqn+ddsS+jWv6MJnP7G7iPyNNRf0b7b/7+QTuMcZsKbxf8luX+1YPJP5Je/1O2/W/ARCb68CCCNLzA63BR8Rn77qioL/pef/O8vf/r1d0j6/0hGLbrau1P4mjl5HICm/fr1l5+a++uffv3lp66EsQac7GtXp/+K5r+y653PHyz4nPXhj2shfz1P8uKaI++RjvxWlP+j/v0VMUYA+P6++Yz8mC/jNUFGJd6YPkzwQ840UNYf7Pjzy+8QJHKoTefdh2GW/8d/ILvYq4umCFpE9QoIRNDBbZyBUXgtihsE/h9zu4agUTcxNOxzHoz/0cOjxEWAfPuf3h09P3lP9Jy+ISL4+sTArw8M/PoDBn57RTRIu6jjMIaTkCOrKF9yJxzhEfIta9CA+gIRxe1b8Ali0afxBiIm8u3fIf/1Tum17L/dITR+oNSR34wI1XQpeB21NCOQP3XyIByDG/A6yCQtPOcByM1HqH1TpBeIcKNFmiROU8SPa6h+UfcPeO7yzyOxb9++uU4TfckfkEogj5rRTOGEd3GQT5+gakEah1H7JQdeVCA//fb7T8j/Qv67VXfiIw8F4vvTJ1BCUZX3CMyxbtQYugs6GALI3Se//f40MCSTwyIHPRgHY9EaF8MYTYD/Zm11zX7CKRpxAbQytHA21hiI00jcviKbAHmXFzIdh0Ykj4qmRXxQgtwHuddDqg5U592SedHCstfGTdB/RLoG3Ll+c2vnLmIGk91pvyE7XoF1o0jHYlk/6whcXOQxNP97LDzeQyL1Tw3CvZF4RfZjVCKlUztlVDtPHoHz8AusF2/Lx0qM5OD6JR+r5D047inyMA+cBC3jPV36afQ5LOgZxAO/eeN9n+OM1U27V7n6S948w9+pR1d4sBxApmEHqzYsCv94hlQTFV3q3+0HJR0pPb3gP71yj0H2r9sE/g+dBTc2GyoEkxL50uEoRiL/3xuRu/yr1XGxYrWFgCz22tF+2HVsoEYGj54LtgMIDK5HDn1vEd4A5g1nv+RpDIOk7v/xmHn3xnPOA7tg0vsQKo53+jAUoF1HuvdIHSOvru/2+JK/AfpHaJw7ekEVYFrDsB8t8sZwHH2TNIK5Oz5/L+53z9b+qDqMRqTs3BRGSgCAfzdCG9Vjtj19AcMWjJl3jWIv+oNWCKQOowPSR6AQMcwfCPp30+0LqCZMtLsX3qfHY8sEpfA7D0oLO1TwipgwYcagaWCWwr5nnAOt8NOdFJIBaGMo4ruFm8gpH8KMTe1TQGf0RZHBOP7RA8/B7yF+l2UUH1J1oO+hLa8j7Prg9vDsu5xPX0FhszEp74v+6O6nrsiPlecfX/K7jO9ID3M9HYv2D8ZBYI5lzT3kRqhqINxk4BlAMBLu9fn1UWIfNfxdls9/6uQ//L1m/1409T967jMStW3ZfJ5OH4Xurc69QqCYwhiJS9B8r3mfnun26ZFun35Itz/QfpjqM/L35PsDiWdgf0awV/QVHYek2ANj5D4vaA7+E2d/IsfRL/kRfPfzMxhGqE17WGTf687bFFh8whqE4+RHHWrG8nWFFfMOvNATX/L3WHhmygNzYNFsih8y+F6AoWcfjnuvD3AobyFvf2zbQjDuatJR/Aa8fM67NP34kjsZ+Dd3M2MdgBELDTLug2D2wE6ojcH96b0rGh/+uJW75xUEBL/4PKbXR2TsYD8i783oR+Rte3DfdOUd3B/9MjbCI0s4Ff56n/u+T3TBC9yTtX05Cv/Y84z917Mv/rMQY1ZBiT0w1vbiPU1Hjn8iAm/CENR/JiLfb5z0iRVN64yVOm7fMryBcvrdiOzQaDDzYDJBjOzggj+zgXxqUHWwJPqjut/t912t4qHL73cztI+N428vb5jx9MGzSYTTYXJ+asaiOIWhChnC50dQwbH/q/bxSQMiHWxdIBGcoVGCZuZz4AACC2hA+sD1GMYPcJJhgMtQgMZo2sFIbAZwmnLmJO3PZpSDM4wzJwhI7xGeX8fqH49y4Y7jzb0ZRvrMzKE9QKAu4QEMx/wZAVCKIQLIjYQmel+aQJh8KvtQbrTkeyc7GuWp828vLk3CmWuy2bCPi58yhuOaU/cYSZM6ndxuBH0g9FJHL04XWRsKW698a8NmAhi8pa3XzaLtRRPbe0bSObqHCcpxzXABnjLXoZk3lm7XGrVmyf2aqzOtmclDdxnIq83t1oUoBicm8tJ62VdO3CZN61ZmhulWkWpJP8WqmEohZ7gd0E6pGx0MA98QxJTRTlf96DjG0pAWrSg0KH+qM2eiV5v+4OJgKu3QFY1K+dHAxWYAYt8c1RNexG6uYsvW61E6PYvTvZ7yrmSXqccbjRWpWe0JBxoEbjOVh1MPuqGeW6eeCXKCDGLGqI4iZ95SAipbWatCb7U4q9paj5KNKfuopswNe0VK2c3Y1snppBXdyU0Zio3E88ZecGtDxRxjewtyUXZlS069tGEMYytSlr3szXozHI/dia7MKxaa284wU3G6uyYGE+5dTVujZnGmsNrZB5ifyieH0kQl5SPDbiq9PhP8fKhln9+aamXMp3ixF+Lc3QiAWmR26bY2bYKpdyS5oVMtwIZSwddM51XnpvTWzLy0tEDvdhllbynax9hzblWpGk1WZLvF1mZ3NG99c92jQKBt3E72YUVrOmjtDnOWCanqGH1zRAl1B6fXc7xF5+X2YKVkfi4idVVdk4HH1nuMpYmsIs6R1F5EikSFjWBol0ESaytnhNnazcK2bovbWhJTkJzc0yRtEjvqUHQTl4YbDzODdodtfzFPlTy/zIW+jEmNc1DR8xaBia6zmMUndJXcjGE9WaCexVezubDwC3ozp4Qk35BbUy5OrroulPxCnNr9MairuG4C4SSBlRIzpCni3hAu3PLgt84iO9X0VazgT42z1UXBs7SUWkrpzuR6Nj8Oc42bL4QZ2589WgdqMo0Y3dNKZn4hUK/v5SE1cstkpppZBxDRancpVUW9HaJYVSvMLI3k4DWnZWOuhqjHzqvCVDkdNJwSi55VL7Rsa1vV+uDvqnhYTnqPom11mbRU5Ow1wbJrXFiyXdQu9aMc6+oBxExztNTttT9Wk6V3W+pwYSZtyB1zJTPpjFkrUjcaP5D9drea7FGuyOYHVcyTbZQn0jInU0MMBDI9aa6i47ikregzVbKKukva7cREZ5spdemD8hjP8qjX1AkBC85som7Ji5/ichLdiklj401vFrQ/XI/kLMb73dk8NlHEWzNtR0DM4AzGSbBFQF8xbQlduVQNP2FQLUnZ8ljJuNIzXlzFCrNrh+1GWxEE3s6YFTTBiu8Zlb1Uxtb10cqngdGpgYMmlERXKFk057PgY+fY2x+cdFLHK+FsHCea5butYDdLUQzzhusZYSDj/NYvk66GG40iVANGlW5VjNpFcDkYol5gdqXRC8vhA6+Lo7U6wzx6jfY7eV+o8mlmc9JcM7VQbzryvOL9XUnGKsVmXbmbe0Odm6aelHu4amFYbnQTFxvSwEj56BfFjVAsCmBZfqzP5xlMVUXXinjPTDLnwKXkEK63XdNv5uJsh7dTneZBb7pYX9TXGXGkkrlMDUQPzuuhj1MUBUy9ERe4qRc0oekn2RfoqybMCD3qe7WINeG20nhPl/f1tl7Z61wuao/lUqoHcQUCnrnyrI/aqYTnx0CxSLDLThU9uNA/F7GRycBijeTUCcxBk1KuUno+axcsa9rnLeWtvEXaq3lUkWSF1z7TahbYlJuFHvIQM+alxtVJvfNMs9gw2mUtUKxx23ZrHpyaarWUZ3vLXLOeN2G3A1/ag+MdD6I7Ca6YzKC3GT/ImtCfuzk9ARZFMxcpPi9D3owgRvtBGxGLdF0ac5vYDjjYX6/SukBreaVcBnFTED5z6GdZr9m9IRtSPZ2TtaKs6VNwYycWeu62xE1FVyefuFS5LZ74c7HwtqfkPBirk6k7td7ThkyH19Kt6cAYZDFpG9Ji1ZLqNumcb819biyPBbaZ12viyB+vty2bVWd7qVErvqRU3rKqXOMmxi094ppocrtLh+5SOcCPHrOpCsDhUaZ5atv36SbxWMLPT8qSn9mZfGD0kzK/TfdcEKxrzHVDXc4qneuIyBlMdyf6ZkDZ65ANeJQ4bSks9beW6x2kc7bDbZr07MOtuRHUoW6NPV/MAwmfLZPT7kpHDnlebkIdc4J4l+gqQU/xjsxtG1tYW31BnQqRZizSY6UDkegrLCb4mdxuDTy/sizdVEyCs+drRJYKGW6dfm5ESwa0AeAsR8mPTW4p7JmfTFrJkC0vTTA0sI/MwLJ+ZN5aO3AatODTq4TD0KPbvY4e7Jg8dVoOUdDts0Y77UCm7DwMJNeQON36FDMGgz7fPFShpFSe9Ftl4xSltZM2RLgMOem60+OJFyeECWoBnXLbiJupN5Srj3PdN8t9JpmFtDp1i/iwt2XR7SlmR/TDPkr8jYqelWYiHg4Zx9AkdS7NZrUOtos6Vom9FcA8qDlFch1n59hwV6VYYsF4RjEj9UyvZQjQWtB35ULkOXx/q/bXtSaDG6b70JhCfxUv6qLYlrNDcdvTu3SzOVcbVWKE6yks2rkhC3zOmWkX65m4G46SHxGVqxg8tlyucrbjQ7qJS/easOyGknGCuxGtoirqYhsfti13mdoWPtRYt+qEY6/kimhwQ6GJ3ZWiUS6cpUfJPpWRsrzA7UEPLtOjKqDYZJuyIs4xJUFMAl62XIdBs8uBnBC4UhupnhEo1ZzMYdnvSgO0RNNeFqwk3OacuR5OZ61ZYAd8w64cQT7sFW57U89h4B7oQ3bVHJ3OWd1yr7RM652r3qTNbp5Vg3PmdJfgFpHvnxnBXGzcVK2L7lwaO+nqcuoqAS3lUrOjTGvmOdOl9FAQ0hST2XUc7mZ1Z2K3wk7iKPKVCN2GNbm3VsFuJ6cbEsLvQA6+V+y0iBWyq8T1HG72hrLPmYN726qSeyoXyW7Yuio3k+J8Hhm7XULJmz2z6bXEC5LlYnZRNxtDS5f9EYZFIKQSOKDD1BS60FXRjXJV6Xq9rRQz7am1eW6i9pydS8cmbtjauzU5fk6FOZ8QQsSTs5NhwW6/5lmubWkw429Lx8Dmg0hH1jb15Q1s+YxLbM6PuF0ZhVGB2O7X9HHojSCrzcVQbfDZTqZqG5uaomFUdU7j55xRVd2ySOjwbr1XaAJfaNMtsanFS6dlZnZirhsrs5ZgCRuqhEzXt+sm5W6kFm4WvE+oC124nXBjuTM8Bm0OXpXe5Jy32L1qC0O5AYnKtd6wE7xWcXJLp2bcgJ0Ud31wLnvhGG1OBEi38ZZn00Vt1j4gJS83jxt8ww8th175dtVpu/UR7UWQsrSvc/1xuWO0ql1Lkjm9TrJQIClBibpNQhCyTkgqCCPSiGA3UxOxXMKSBNBtlS5S1Z1UuwOHB1NdBFt9KRKhn69gyevFRceVnc1sycUG8xwhkaPDTq/LWjw7V27L+mYHdH5xI6LV8qJxjGAdlkSlUAap7+nFzMf9fcUfubMrXKDBjC1Pkeb+2DF7Q74cFnhjhxFas9JsODArlptQZXZaHlB16WHDWh2u15sk3rIwDKc7rMtTL4s7Y99nomDb0j50dksjIdmZaOVb7MQpmxOaL7N5aab4hFqndBTRxdUMIaj66iVQhqzo3B1XRaou4pI82eemeNwFEEvpLWVQa6HZ1dJaOGirPO3s09I8WsqpFdNA0mq2XTW952cCUdFVc8mSxWG/uXnr0wRduuzpQBhCtFgchXVG+jNuwaBlf7n1CtHnEVBUXM3xmT4HLm0KUuBuZ4p4vjAqOKSzToonazm31sBe7S+uGys7+sjr+8pf6f1MK0w9KvHVcLztmDgNvd1xR+mnQ4vh1bq+dPWAO/VuIi5F+pidU2peHFlpOgvECy86+w0hD3w47VxmkVMac0Mbcql5YkAyHiBbTum8rq2ut0kqOHOTCyekTO9DhV3uwLzWnXVUDe1U7rx56FCLYE3a9Flmpq7vu2eYwsVlOsW3BMl2Z6lplZkCd2CKRPcMphH9pS65KX6EkI2zTFhQQk+oOuBK1FssFKnPBHoWkcm0EE9iGO4dCqBH8opH63OebOaxfFV4d+Ca5U1V7OZcUETbZSk+5MFuWKhuSmRurqNAirWaOW3LM190FLAuvOdR+EIdtvhht7uEs/68asn+IF09ERBri2E1WD6lCGod4p52AsRifZv4rU/g3FQScvdUr/QwnU/SyJNCqiRuRIiW7H55kaOuODdzUzniWRR4hDoZsgt2mZlKB/tWnqrINboY7IVF28p2Rq7jQkaDQL8paZ3i9dpgzc1BMpe6nzl4e6E8c6JHmG9fJcVl1Nm5UryLPZ9Rx523oHghn9X+HGcjJVpZPcpvTKbfnPVj0OSFGTNLt62ZCiTeVV4IwlQ5+tsVKRpWNgGddFu74fk2yLGsbLurGFqVjs5nS9TeT5YXurxmRO74cCdKFSu2DTGwkM99fRumEKio+SQb93ukgNlLe8ecW2ZueOvkeA1hBxbyBw5jSMeWl2zUWAfDOE+ChMUwE9+o2sCcLF5Fl7D3unJXzSQUv/TjjUlq9QQkS3wr79KwmSSzUxBnaERMt5xMY3GvzP3BlALL82egTvwsCDqW8eBszzrMN1PO002hAdtVW1yFueyytpvOlyVDbDhtWMNm1KTjw2rBX133XJd45xMHmuaII6B0FCUGv7Y2jhMS3UREfSk/0zIRs5p/WaRQxo5xUTFoCZuI2KOqkDqzolCvTSbKGdUa/mQwxjDJ3SU5SYlDRsxZQPoXkK5ietLiBLG3DaqjianlAwaCFrHYaazCDMPUwYT+oNB8kcHM2RyxCTVThNuxAI7BSpeZ1UT79kbdstm+Zib8NNjukrUizZaZe74EGh6L7I0sqJ6vr5xGYgZhDbsL2vbo9oLvUFvCmJ6tSaHdTld5aCZsJqvJJaYmU2UJDrp6wZLrRChQUptt3M41gHQ6uc6RXOvFxWoEYamEs8I24zXHcKEvsuGwu+5tYIMoP4VVlRGCGzV0hk5Bl5E3FJ0uq4azV8mBOEyoM6asGxGsz9dJ7+AXvpuG/jGkNjx2hQ3PreDnQ3S9xtV0saJW/mFH7m5cXmnhATdnOkg5LWOW0iG4eOF0ZR5OgX9TZOmyJm4UtZGKdia7odVNXIGQNd53B1sjZGkyWJvpuqPn4XF9nai2NTF1y6iUpQuyyaIRD4pxAZWcAXyWh9SgwVwHLKEtro6kLcmD7Ryrpb7a5j6FhdKsSoZK2axILBC0lGZoLZNXN747E1Vz6DqSWU5ZPtJvzG2xDVn25ePLeHL9PH/+W9+bx9PA/2eHko/zw7fvUfejZ+D4n++8Pv89sX79+FJ7MRTqcQDbpF34PKr8L8evn/6dLxkjhf7xKXf8fHZr347sWycc/ybpJc79rmnr/mtTpN39EPjji9s14x9HNF+fh90vd+WycqT2zhTeRzHUqS2+1qCN7y/ifPwgBPzYad8ew+eJ9McXv4duir3mK0FTX0Fdjpo+P4yMLhi/jLz8/r8BZJNr7v0lAAA= -->
