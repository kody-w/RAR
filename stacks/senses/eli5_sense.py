"""ELI5 — the same response, explained to a five-year-old.

A sense that translates the main reply into a version a child could
understand. Same answer, different audience. Frontends with an
"explain it simply" toggle swap eli5_response in for the main reply;
teaching/onboarding UIs render it as a side-by-side companion.

Install: drop in rapp_brainstem/utils/senses/. The brainstem auto-discovers *_sense.py at startup; restart the brainstem.
"""

name = "eli5"
delimiter = "|||ELI5|||"
response_key = "eli5_response"
wrapper_tag = "eli5"
system_prompt = (
    "After your main reply, append `|||ELI5|||` followed by an "
    "explain-like-I'm-five version of the same answer. Short sentences. "
    "Concrete nouns. No jargon — if you must use a technical term, "
    "translate it inline (\"a cookie, which is a tiny note your browser "
    "remembers\"). Analogies welcome, especially physical ones. 2-4 "
    "sentences ideal. The ELI5 is a TRANSLATION — the same meaning, "
    "different audience. Always emit — empty is not allowed."
)

__manifest__ = {
    "schema": "rapp-sense/1.0",
    "name": "@rapp/eli5",
    "version": "0.1.0",
    "description": "ELI5 \u2014 the same response, explained to a five-year-old.",
}
