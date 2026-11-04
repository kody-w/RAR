"""HEADLINE — the same response, as a news headline.

A sense that translates the main reply into a punchy headline. For
notification UIs, push-style summaries, dashboard cards, anywhere a
glanceable hook beats prose. Verb-driven, present tense, no clickbait.

Install: drop in rapp_brainstem/utils/senses/. The brainstem auto-discovers *_sense.py at startup; restart the brainstem.
"""

name = "headline"
delimiter = "|||HEADLINE|||"
response_key = "headline_response"
wrapper_tag = "headline"
system_prompt = (
    "After your main reply, append `|||HEADLINE|||` followed by a single "
    "headline that captures the answer's essence the way a news ticker "
    "would. Verb-driven. Present tense. Under 10 words. Title case is "
    "fine but not required. No clickbait, no rhetorical questions, no "
    "ellipses. The headline is a TRANSLATION of the answer into "
    "attention-grabbing form. Always emit — empty is not allowed."
)

__manifest__ = {
    "schema": "rapp-sense/1.0",
    "name": "@rapp/headline",
    "version": "0.1.0",
    "description": "HEADLINE \u2014 the same response, as a news headline.",
}
