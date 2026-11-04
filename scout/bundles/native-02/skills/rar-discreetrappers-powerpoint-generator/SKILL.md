---
name: "rar-discreetrappers-powerpoint-generator"
description: "Generate professional PowerPoint presentations using Microsoft templates.\n\nTemplates available:\n- BaseTemplateBlue: Microsoft corporate template (recommended)\n- ZavaTemplate: Modern business template\n- BaseTemplateDynamics: Dynamics-style template\n\nActions:\n- create_presentation: Create multi-slide presentation\n- list_templates: List available templates and their layouts\n- list_layouts: List layouts for a specific template\n\nSlide types: title, section, content, two_column, comparison, quote, stats, pipeline, blank\n\nExample:\n{\n  \"action\": \"create_presentation\",\n  \"customer\": \"Contoso\",\n  \"template\": \"BaseTemplateBlue\",\n  \"output_filename\": \"my_presentation\",\n  \"slides\": [\n    {\"type\": \"title\", \"title\": \"My Presentation\", \"subtitle\": \"Subtitle here\"},\n    {\"type\": \"content\", \"title\": \"Key Points\", \"bullets\": [\"Point 1\", \"Point 2\"]},\n    {\"type\": \"comparison\", \"title\": \"Before vs After\", \"left_label\": \"Before\", \"right_label\": \"After\", \"left_items\": [\"Old way\"], \"right_items\": [\"New way\"]}\n  ]\n}"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@discreetRappers/powerpoint_generator_agent", "rar_sha256": "e1c71838845673ea756b0fea8afa04d3c9014964423cdaf354547df96af9a7e6", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "1.0.2", "author": "Bill Whalen", "tags": ["productivity", "powerpoint", "presentations", "templates", "microsoft"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@discreetRappers/powerpoint_generator_agent`. The original RAPP
agent is preserved byte-for-byte in `powerpoint_generator_agent.py` and in the RCI capsule.

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

PowerPoint Generator Agent V2 - Template-Based Microsoft Design
Purpose: Generate professional PowerPoint presentations using Microsoft templates

Design principles:
- Template-based generation for consistent branding
- Supports multiple templates (BaseTemplateBlue, ZavaTemplate, etc.)
- Smart layout selection based on content type
- Proper placeholder population
- Fallback to programmatic generation if template not available

Templates supported:
- BaseTemplateBlue.pptx: Microsoft corporate template (113 layouts)
- ZavaTemplate.pptx: Modern business template (62 layouts)
- BaseTemplateDynamics.pptx: Dynamics-style template

Usage:
1. With template: action="create_presentation", template="BaseTemplateBlue", slides=[...]
2. Without template: action="create_presentation", slides=[...] (uses default styling)

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "action": {
      "enum": [
        "create_presentation",
        "list_templates",
        "list_layouts"
      ],
      "type": "string"
    },
    "customer": {
      "description": "Customer name - creates a subfolder in docs/ppt for this customer",
      "type": "string"
    },
    "output_filename": {
      "type": "string"
    },
    "slides": {
      "items": {
        "type": "object"
      },
      "type": "array"
    },
    "template": {
      "description": "Template name (BaseTemplateBlue, ZavaTemplate, BaseTemplateDynamics)",
      "type": "string"
    }
  },
  "required": [
    "action"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `powerpoint_generator_agent.py` and embedded as the fenced Python below (sha256 e1c71838845673ea…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `powerpoint_generator_agent.py` first:

```bash
python3 powerpoint_generator_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 powerpoint_generator_agent.py   # or on stdin
python3 powerpoint_generator_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@discreetRappers/powerpoint_generator_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/powerpoint_generator_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@discreetRappers/powerpoint_generator_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""
PowerPoint Generator Agent V2 - Template-Based Microsoft Design
Purpose: Generate professional PowerPoint presentations using Microsoft templates

Design principles:
- Template-based generation for consistent branding
- Supports multiple templates (BaseTemplateBlue, ZavaTemplate, etc.)
- Smart layout selection based on content type
- Proper placeholder population
- Fallback to programmatic generation if template not available

Templates supported:
- BaseTemplateBlue.pptx: Microsoft corporate template (113 layouts)
- ZavaTemplate.pptx: Modern business template (62 layouts)
- BaseTemplateDynamics.pptx: Dynamics-style template

Usage:
1. With template: action="create_presentation", template="BaseTemplateBlue", slides=[...]
2. Without template: action="create_presentation", slides=[...] (uses default styling)
"""

from __future__ import annotations

# ═══════════════════════════════════════════════════════════════
# RAPP AGENT MANIFEST — Do not remove. Used by registry builder.
# ═══════════════════════════════════════════════════════════════
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@discreetRappers/powerpoint_generator_agent",
    "version": "1.0.2",
    "display_name": "PowerPointGeneratorV2",
    "description": "Generates PowerPoint decks from slide specs with python-pptx, using Microsoft templates and smart layout selection.",
    "author": "Bill Whalen",
    "tags": ["productivity", "powerpoint", "presentations", "templates", "microsoft"],
    "category": "productivity",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}
# ═══════════════════════════════════════════════════════════════


import json
import logging
import os
from datetime import datetime
from typing import Dict, Any, List, Optional, Tuple
from agents.basic_agent import BasicAgent
from utils.storage_factory import get_storage_manager

# Import python-pptx
try:
    from pptx import Presentation
    from pptx.util import Inches, Pt, Emu
    from pptx.dml.color import RGBColor
    from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
    from pptx.enum.shapes import MSO_SHAPE, MSO_CONNECTOR
    from pptx.oxml.ns import nsmap
    PPTX_AVAILABLE = True
except ImportError as e:
    PPTX_AVAILABLE = False
    PPTX_IMPORT_ERROR = str(e)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class PowerPointGeneratorAgentV2(BasicAgent):
    """
    Agent for generating professional presentations using Microsoft templates.
    """

    # Template configurations - maps template names to layout indexes
    TEMPLATE_CONFIGS = {
        "PowerpointTemplateBlue": {
            "file": "docs/ppt/ppt_templates/PowerpointTemplateBlue.pptx",
            "layouts": {
                "title": 2,  # "Title Slide"
                "title_photo": 0,  # "Title square photo"
                "section": 102,  # "Section Divider"
                "content": 9,  # "Title and Content"
                "two_column": 11,  # "Two Column Bullet text"
                "three_column": 15,  # "Three Column Bullet with Subtitles"
                "four_column": 16,  # "Four Column Bullet with Subtitles"
                "comparison": 11,  # "Two Column Bullet text"
                "quote": 64,  # "Quote slide 1b"
                "code": 94,  # "Developer Code Layout full page"
                "demo": 100,  # "Demo slide"
                "blank": 108,  # "Blank 12 Column"
                "closing": 111,  # "Closing logo slide"
                "title_only": 18,  # "Title Only"
            }
        },
        "BaseTemplateBlueV2": {
            "file": "docs/ppt/BaseTemplateBlueV2.pptx",
            "layouts": {
                "title": 2,  # "Title Slide"
                "title_photo": 0,  # "Title square photo"
                "section": 102,  # "Section Divider"
                "content": 9,  # "Title and Content"
                "two_column": 11,  # "Two Column Bullet text"
                "three_column": 15,  # "Three Column Bullet with Subtitles"
                "four_column": 16,  # "Four Column Bullet with Subtitles"
                "comparison": 11,  # "Two Column Bullet text"
                "quote": 64,  # "Quote slide 1b"
                "code": 94,  # "Developer Code Layout full page"
                "demo": 100,  # "Demo slide"
                "blank": 108,  # "Blank 12 Column"
                "closing": 111,  # "Closing logo slide"
                "title_only": 18,  # "Title Only"
            }
        },
        "BaseTemplateBlue": {
            "file": "docs/ppt/BaseTemplateBlue.pptx",
            "layouts": {
                "title": 2,  # "Title Slide"
                "title_photo": 0,  # "Title square photo"
                "section": 102,  # "Section Divider"
                "content": 9,  # "Title and Content"
                "two_column": 11,  # "Two Column Bullet text"
                "three_column": 15,  # "Three Column Bullet with Subtitles"
                "four_column": 16,  # "Four Column Bullet with Subtitles"
                "comparison": 11,  # "Two Column Bullet text"
                "quote": 64,  # "Quote slide 1b"
                "code": 94,  # "Developer Code Layout full page"
                "demo": 100,  # "Demo slide"
                "blank": 108,  # "Blank 12 Column"
                "closing": 111,  # "Closing logo slide"
                "title_only": 18,  # "Title Only"
            }
        },
        "ZavaTemplate": {
            "file": "docs/ppt/ZavaTemplate.pptx",
            "layouts": {
                "title": 0,  # "Title 1"
                "title_photo": 10,  # "Title Photo 1"
                "section": 14,  # "Section Header 1"
                "content": 24,  # "Content 1"
                "two_column": 41,  # "Two Content"
                "comparison": 43,  # "Comparison"
                "quote": 59,  # "Quote"
                "statement": 56,  # "Statement"
                "number": 53,  # "Number Large"
                "conclusion": 48,  # "Conclusion 1"
                "blank": 45,  # "Blank"
                "title_only": 44,  # "Title Only"
                "agenda": 20,  # "Agenda"
            }
        },
        "BaseTemplateDynamics": {
            "file": "docs/ppt/BaseTemplateDynamics.pptx",
            "layouts": {
                "title": 0,
                "content": 1,
                "blank": 6,
            }
        }
    }

    # Microsoft color palette
    COLORS = {
        "ms_blue": "0078D4",
        "ms_dark_blue": "004578",
        "ms_light_blue": "50E6FF",
        "ms_green": "107C10",
        "ms_red": "D13438",
        "ms_orange": "FF8C00",
        "ms_purple": "5C2D91",
        "black": "000000",
        "dark_gray": "323130",
        "medium_gray": "605E5C",
        "light_gray": "A19F9D",
        "white": "FFFFFF",
    }

    # Segoe UI fonts (Microsoft standard)
    FONTS = {
        "title": {"name": "Segoe UI Semibold", "size": 44, "bold": False},
        "subtitle": {"name": "Segoe UI", "size": 24, "bold": False},
        "heading": {"name": "Segoe UI Semibold", "size": 28, "bold": False},
        "body": {"name": "Segoe UI", "size": 18, "bold": False},
        "caption": {"name": "Segoe UI", "size": 14, "bold": False},
    }

    def __init__(self):
        self.name = 'PowerPointGeneratorV2'
        self.metadata = {
            "name": self.name,
            "description": """Generate professional PowerPoint presentations using Microsoft templates.

Templates available:
- BaseTemplateBlue: Microsoft corporate template (recommended)
- ZavaTemplate: Modern business template
- BaseTemplateDynamics: Dynamics-style template

Actions:
- create_presentation: Create multi-slide presentation
- list_templates: List available templates and their layouts
- list_layouts: List layouts for a specific template

Slide types: title, section, content, two_column, comparison, quote, stats, pipeline, blank

Example:
{
  "action": "create_presentation",
  "customer": "Contoso",
  "template": "BaseTemplateBlue",
  "output_filename": "my_presentation",
  "slides": [
    {"type": "title", "title": "My Presentation", "subtitle": "Subtitle here"},
    {"type": "content", "title": "Key Points", "bullets": ["Point 1", "Point 2"]},
    {"type": "comparison", "title": "Before vs After", "left_label": "Before", "right_label": "After", "left_items": ["Old way"], "right_items": ["New way"]}
  ]
}""",
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {
                        "type": "string",
                        "enum": ["create_presentation", "list_templates", "list_layouts"]
                    },
                    "customer": {
                        "type": "string",
                        "description": "Customer name - creates a subfolder in docs/ppt for this customer"
                    },
                    "template": {
                        "type": "string",
                        "description": "Template name (BaseTemplateBlue, ZavaTemplate, BaseTemplateDynamics)"
                    },
                    "slides": {
                        "type": "array",
                        "items": {"type": "object"}
                    },
                    "output_filename": {"type": "string"},
                },
                "required": ["action"]
            }
        }
        super().__init__(self.name, self.metadata)

        try:
            self.storage = get_storage_manager()
        except Exception as e:
            logger.warning(f"Storage not available: {e}")
            self.storage = None

        # Find base path for templates
        self.base_path = self._find_base_path()

    def _find_base_path(self) -> str:
        """Find the base path for the RAPP project."""
        # Try common locations
        possible_paths = [
            os.getcwd(),
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            "c:/Users/billwhalen/OneDrive - Microsoft/Documents/GitHub/RAPP/CommunityRAPP-main",
        ]
        for path in possible_paths:
            if os.path.exists(os.path.join(path, "docs", "ppt")):
                return path
        return os.getcwd()

    def perform(self, **kwargs) -> str:
        """Execute the requested action."""
        if not PPTX_AVAILABLE:
            return json.dumps({
                "status": "error",
                "error": f"python-pptx library not available: {PPTX_IMPORT_ERROR}",
                "suggestion": "Install with: pip install python-pptx"
            })

        action = kwargs.get('action', 'create_presentation')

        try:
            if action == 'list_templates':
                return self._list_templates()
            elif action == 'list_layouts':
                return self._list_layouts(kwargs.get('template', 'BaseTemplateBlue'))
            elif action == 'create_presentation':
                return self._create_presentation(**kwargs)
            else:
                return json.dumps({
                    "status": "error",
                    "error": f"Unknown action: {action}",
                    "available_actions": ["create_presentation", "list_templates", "list_layouts"]
                })
        except Exception as e:
            logger.error(f"PowerPoint generation error: {e}")
            import traceback
            return json.dumps({
                "status": "error",
                "error": str(e),
                "traceback": traceback.format_exc()
            })

    def _list_templates(self) -> str:
        """List available templates."""
        templates = {}
        for name, config in self.TEMPLATE_CONFIGS.items():
            # Normalize path separators for Windows
            template_rel_path = config["file"].replace("/", os.sep)
            template_path = os.path.join(self.base_path, template_rel_path)
            templates[name] = {
                "file": config["file"],
                "exists": os.path.exists(template_path),
                "layouts": list(config["layouts"].keys())
            }
        return json.dumps({"status": "success", "templates": templates}, indent=2)

    def _list_layouts(self, template_name: str) -> str:
        """List layouts for a specific template."""
        if template_name not in self.TEMPLATE_CONFIGS:
            return json.dumps({
                "status": "error",
                "error": f"Unknown template: {template_name}",
                "available": list(self.TEMPLATE_CONFIGS.keys())
            })

        config = self.TEMPLATE_CONFIGS[template_name]
        # Normalize path separators for Windows
        template_rel_path = config["file"].replace("/", os.sep)
        template_path = os.path.join(self.base_path, template_rel_path)

        if not os.path.exists(template_path):
            return json.dumps({
                "status": "error",
                "error": f"Template file not found: {template_path}"
            })

        # Handle .potx files by converting to .pptx in temp location
        import tempfile
        import shutil
        
        actual_path = template_path
        if template_path.lower().endswith('.potx'):
            temp_dir = tempfile.gettempdir()
            temp_pptx = os.path.join(temp_dir, f"temp_template_{template_name}.pptx")
            shutil.copy2(template_path, temp_pptx)
            actual_path = temp_pptx

        prs = Presentation(actual_path)
        layouts = []
        for i, layout in enumerate(prs.slide_layouts):
            layouts.append({"index": i, "name": layout.name})

        return json.dumps({
            "status": "success",
            "template": template_name,
            "layout_count": len(layouts),
            "mapped_layouts": config["layouts"],
            "all_layouts": layouts
        }, indent=2)

    def _hex_to_rgb(self, hex_color: str) -> RGBColor:
        """Convert hex color to RGBColor."""
        hex_color = hex_color.lstrip('#')
        return RGBColor(
            int(hex_color[0:2], 16),
            int(hex_color[2:4], 16),
            int(hex_color[4:6], 16)
        )

    def _create_presentation(self, **kwargs) -> str:
        """Create a presentation using templates."""
        template_name = kwargs.get('template', 'BaseTemplateBlue')
        slides = kwargs.get('slides', [])
        output_filename = kwargs.get('output_filename', 'presentation')

        if not slides:
            return json.dumps({
                "status": "error",
                "error": "No slides provided. Use 'slides' parameter with array of slide configs."
            })

        # Load template or create blank presentation
        prs = self._load_template(template_name)
        if prs is None:
            return json.dumps({
                "status": "error",
                "error": f"Could not load template: {template_name}"
            })

        config = self.TEMPLATE_CONFIGS.get(template_name, {})
        layout_map = config.get("layouts", {})

        # Process each slide
        for i, slide_config in enumerate(slides):
            slide_type = slide_config.get('type', 'content')
            self._add_slide(prs, slide_config, slide_type, layout_map, i + 1)

        return self._save_presentation(prs, output_filename, kwargs)

    def _remove_placeholder_shapes(self, slide) -> None:
        """Remove placeholder shapes from a slide to avoid template artifacts."""
        shapes_to_remove = []
        for shape in slide.shapes:
            # Check if it's a placeholder shape
            if hasattr(shape, 'placeholder_format') and shape.placeholder_format is not None:
                shapes_to_remove.append(shape)
        
        # Remove the placeholder shapes
        for shape in shapes_to_remove:
            sp = shape._element
            sp.getparent().remove(sp)

    def _load_template(self, template_name: str) -> Optional[Presentation]:
        """Load a PowerPoint template."""
        if template_name not in self.TEMPLATE_CONFIGS:
            logger.warning(f"Unknown template {template_name}, using blank presentation")
            prs = Presentation()
            prs.slide_width = Inches(13.333)
            prs.slide_height = Inches(7.5)
            return prs

        config = self.TEMPLATE_CONFIGS[template_name]
        # Normalize path separators for Windows
        template_rel_path = config["file"].replace("/", os.sep)
        template_path = os.path.join(self.base_path, template_rel_path)

        if not os.path.exists(template_path):
            logger.warning(f"Template file not found: {template_path}")
            prs = Presentation()
            prs.slide_width = Inches(13.333)
            prs.slide_height = Inches(7.5)
            return prs

        try:
            # Handle .potx files by converting to .pptx in temp location
            import tempfile
            import shutil
            
            if template_path.lower().endswith('.potx'):
                # Copy .potx to temp .pptx file (python-pptx doesn't support .potx directly)
                temp_dir = tempfile.gettempdir()
                temp_pptx = os.path.join(temp_dir, f"temp_template_{template_name}.pptx")
                shutil.copy2(template_path, temp_pptx)
                template_path = temp_pptx
            
            prs = Presentation(template_path)
            # Remove any existing slides from template
            while len(prs.slides) > 0:
                rId = prs.slides._sldIdLst[0].rId
                prs.part.drop_rel(rId)
                del prs.slides._sldIdLst[0]
            return prs
        except Exception as e:
            logger.error(f"Error loading template: {e}")
            return None

    def _add_slide(self, prs: Presentation, config: Dict, slide_type: str, 
                   layout_map: Dict, page_num: int) -> None:
        """Add a slide based on type and configuration."""
        # Get the appropriate layout
        layout_idx = layout_map.get(slide_type, layout_map.get('content', 0))

        # Ensure layout index is valid
        if layout_idx >= len(prs.slide_layouts):
            layout_idx = 0

        layout = prs.slide_layouts[layout_idx]
        slide = prs.slides.add_slide(layout)

        # Populate the slide based on type
        if slide_type == 'title':
            self._populate_title_slide(slide, config)
        elif slide_type == 'section':
            self._populate_section_slide(slide, config)
        elif slide_type == 'content':
            self._populate_content_slide(slide, config)
        elif slide_type in ['two_column', 'comparison']:
            self._populate_comparison_slide(slide, config)
        elif slide_type == 'quote':
            self._populate_quote_slide(slide, config)
        elif slide_type == 'stats':
            self._populate_stats_slide(slide, prs, config)
        elif slide_type == 'pipeline':
            self._populate_pipeline_slide(slide, prs, config)
        elif slide_type == 'image':
            self._populate_image_slide(slide, config)
        elif slide_type == 'title_image':
            self._populate_title_image_slide(slide, config)
        elif slide_type == 'value_cards':
            self._populate_value_cards_slide(slide, config)
        elif slide_type == 'before_after':
            self._populate_before_after_slide(slide, config)
        elif slide_type == 'agent_cards':
            self._populate_agent_cards_slide(slide, config)
        elif slide_type == 'metric_boxes':
            self._populate_metric_boxes_slide(slide, config)
        elif slide_type == 'process_flow':
            self._populate_process_flow_slide(slide, config)
        else:
            # Default content slide
            self._populate_content_slide(slide, config)

    def _populate_image_slide(self, slide, config: Dict) -> None:
        """Populate a slide with an image."""
        title = config.get('title', '')
        image_path = config.get('image_path', '')
        caption = config.get('caption', '')
        
        # Remove non-title placeholders to avoid artifacts
        shapes_to_remove = []
        title_shape = None
        for shape in slide.shapes:
            if hasattr(shape, 'placeholder_format') and shape.placeholder_format is not None:
                if shape.placeholder_format.type == 1:  # Title placeholder
                    title_shape = shape
                else:
                    shapes_to_remove.append(shape)
        
        for shape in shapes_to_remove:
            sp = shape._element
            sp.getparent().remove(sp)
        
        # Set title
        if title_shape and title:
            title_shape.text_frame.paragraphs[0].text = title
            self._style_text(title_shape.text_frame.paragraphs[0], "heading")
        elif title:
            self._add_title_textbox(slide, title, 0.5, 0.3, 12.333, size=28)
        
        # Add image if path exists
        if image_path and os.path.exists(image_path):
            # Calculate centered position
            img_width = Inches(10)
            img_left = Inches(1.667)  # Center on 13.333" wide slide
            img_top = Inches(1.3)
            img_height = Inches(5.5)
            
            slide.shapes.add_picture(image_path, img_left, img_top, width=img_width)
        
        # Add caption if provided
        if caption:
            caption_box = slide.shapes.add_textbox(Inches(0.5), Inches(6.9), Inches(12.333), Inches(0.4))
            tf = caption_box.text_frame
            p = tf.paragraphs[0]
            p.text = caption
            p.font.size = Pt(12)
            p.font.italic = True
            p.font.color.rgb = self._hex_to_rgb(self.COLORS["medium_gray"])
            p.alignment = PP_ALIGN.CENTER

    def _populate_title_image_slide(self, slide, config: Dict) -> None:
        """Populate a slide with title, content bullets, and an image side by side."""
        title = config.get('title', '')
        content = config.get('content', [])
        image_path = config.get('image_path', '')
        
        # Set title
        title_set = False
        for shape in slide.shapes:
            if shape.has_text_frame and shape.placeholder_format:
                if shape.placeholder_format.type == 1:
                    shape.text_frame.paragraphs[0].text = title
                    self._style_text(shape.text_frame.paragraphs[0], "heading")
                    title_set = True
                    break
        
        if not title_set and title:
            self._add_title_textbox(slide, title, 0.5, 0.3, 12.333, size=28)
        
        # Add content on left side
        if content:
            self._add_bullet_textbox(slide, content, 0.5, 1.3, 5.5, 5.5)
        
        # Add image on right side
        if image_path and os.path.exists(image_path):
            img_left = Inches(6.5)
            img_top = Inches(1.3)
            img_width = Inches(6.3)
            slide.shapes.add_picture(image_path, img_left, img_top, width=img_width)

    def _populate_title_slide(self, slide, config: Dict) -> None:
        """Populate a title slide."""
        # Remove all placeholder shapes to avoid template artifacts
        self._remove_placeholder_shapes(slide)
        
        title = config.get('title', '')
        subtitle = config.get('subtitle', '')

        # Title slides have dark background - use white text
        self._add_title_textbox(slide, title, 0.5, 2.5, 12.333, color="#FFFFFF")
        if subtitle:
            self._add_subtitle_textbox(slide, subtitle, 0.5, 3.5, 12.333, color="#CCCCCC")

    def _populate_section_slide(self, slide, config: Dict) -> None:
        """Populate a section divider slide."""
        # Remove all placeholder shapes to avoid template artifacts
        self._remove_placeholder_shapes(slide)
        
        title = config.get('title', '')

        # Section slides have dark background - use white text
        self._add_title_textbox(slide, title, 0.5, 3.0, 12.333, size=36, color="#FFFFFF")

    def _populate_content_slide(self, slide, config: Dict) -> None:
        """Populate a content slide with bullets."""
        # Remove all placeholder shapes to avoid template artifacts
        self._remove_placeholder_shapes(slide)
        
        title = config.get('title', '')
        bullets = config.get('bullets', config.get('content', []))

        # Add title and content as textboxes (placeholders removed)
        if title:
            self._add_title_textbox(slide, title, 0.5, 0.5, 12.333, size=28)
        if bullets:
            self._add_bullet_textbox(slide, bullets, 0.5, 1.5, 12.333, 5.5)

    def _populate_comparison_slide(self, slide, config: Dict) -> None:
        """Populate a comparison/two-column slide."""
        # Remove all placeholder shapes to avoid template artifacts
        self._remove_placeholder_shapes(slide)
        
        title = config.get('title', '')
        
        # Support both old format (left_label/right_label) and new format (left/right objects)
        left_data = config.get('left', {})
        right_data = config.get('right', {})
        
        if isinstance(left_data, dict):
            # New format with nested title/content
            left_label = left_data.get('title', config.get('left_label', 'Left'))
            left_items = left_data.get('content', config.get('left_items', []))
        else:
            left_label = config.get('left_label', 'Before')
            left_items = config.get('left_items', [])
            
        if isinstance(right_data, dict):
            right_label = right_data.get('title', config.get('right_label', 'Right'))
            right_items = right_data.get('content', config.get('right_items', []))
        else:
            right_label = config.get('right_label', 'After')
            right_items = config.get('right_items', [])

        # Add title as textbox (placeholders removed)
        if title:
            self._add_title_textbox(slide, title, 0.5, 0.3, 12.333, size=28)

        # Add comparison content via text boxes
        self._add_two_column_content(slide, left_label, right_label, left_items, right_items)

    def _populate_quote_slide(self, slide, config: Dict) -> None:
        """Populate a quote slide."""
        # Remove all placeholder shapes to avoid template artifacts
        self._remove_placeholder_shapes(slide)
        
        quote = config.get('quote', '')
        author = config.get('author', config.get('quote_author', ''))

        # Add quote box directly (placeholders removed)
        self._add_quote_box(slide, quote, author)

    def _populate_stats_slide(self, slide, prs, config: Dict) -> None:
        """Populate a stats/metrics slide."""
        # Remove all placeholder shapes to avoid template artifacts
        self._remove_placeholder_shapes(slide)
        
        title = config.get('title', '')
        stats = config.get('stats', config.get('metrics', []))

        # Add title as textbox (placeholders removed)
        if title:
            self._add_title_textbox(slide, title, 0.5, 0.3, 12.333, size=28)

        # Add stats boxes
        self._add_stats_boxes(slide, prs, stats)

    def _populate_pipeline_slide(self, slide, prs, config: Dict) -> None:
        """Populate a pipeline/process slide."""
        # Remove all placeholder shapes to avoid template artifacts
        self._remove_placeholder_shapes(slide)
        
        title = config.get('title', '')
        steps = config.get('steps', [])

        # Add title as textbox (placeholders removed)
        if title:
            self._add_title_textbox(slide, title, 0.5, 0.3, 12.333, size=28)

        # Add pipeline visualization
        self._add_pipeline_boxes(slide, prs, steps)

    def _populate_value_cards_slide(self, slide, config: Dict) -> None:
        """Populate a slide with value proposition cards (like the HTML demo)."""
        # Remove template placeholders first
        self._remove_placeholder_shapes(slide)
        
        title = config.get('title', '')
        cards = config.get('cards', [])
        
        # Set title
        self._add_title_textbox(slide, title, 0.5, 0.3, 12.333, size=28)
        
        # Calculate card positions (up to 4 cards per row)
        num_cards = len(cards)
        card_width = 3.8
        card_height = 2.8
        gap = 0.3
        
        if num_cards <= 3:
            start_x = (13.333 - (num_cards * card_width + (num_cards - 1) * gap)) / 2
            cards_per_row = num_cards
        else:
            start_x = (13.333 - (3 * card_width + 2 * gap)) / 2
            cards_per_row = 3
        
        for i, card in enumerate(cards):
            row = i // cards_per_row
            col = i % cards_per_row
            x = start_x + col * (card_width + gap)
            y = 1.3 + row * (card_height + 0.3)
            
            self._add_value_card(slide, card, x, y, card_width, card_height)

    def _add_value_card(self, slide, card: Dict, x: float, y: float, 
                        width: float, height: float) -> None:
        """Add a single value card with icon, title, description, and before/after."""
        icon = card.get('icon', '📊')
        title = card.get('title', '')
        description = card.get('description', '')
        before = card.get('before', '')
        after = card.get('after', '')
        
        # Card background
        shape = slide.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE,
            Inches(x), Inches(y), Inches(width), Inches(height)
        )
        shape.fill.solid()
        shape.fill.fore_color.rgb = RGBColor(255, 255, 255)
        shape.line.color.rgb = self._hex_to_rgb(self.COLORS["light_gray"])
        shape.line.width = Pt(1)
        shape.shadow.inherit = False
        
        # Icon
        icon_box = slide.shapes.add_textbox(Inches(x), Inches(y + 0.15), Inches(width), Inches(0.5))
        tf = icon_box.text_frame
        p = tf.paragraphs[0]
        p.text = icon
        p.font.size = Pt(32)
        p.alignment = PP_ALIGN.CENTER
        
        # Title
        title_box = slide.shapes.add_textbox(Inches(x + 0.1), Inches(y + 0.65), Inches(width - 0.2), Inches(0.4))
        tf = title_box.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(14)
        p.font.bold = True
        p.font.color.rgb = self._hex_to_rgb(self.COLORS["ms_blue"])
        p.alignment = PP_ALIGN.CENTER
        
        # Description
        if description:
            desc_box = slide.shapes.add_textbox(Inches(x + 0.1), Inches(y + 1.05), Inches(width - 0.2), Inches(0.6))
            tf = desc_box.text_frame
            tf.word_wrap = True
            p = tf.paragraphs[0]
            p.text = description
            p.font.size = Pt(10)
            p.font.color.rgb = self._hex_to_rgb(self.COLORS["medium_gray"])
            p.alignment = PP_ALIGN.CENTER
        
        # Before/After if provided
        if before and after:
            ba_y = y + height - 0.6
            
            # Before (red, strikethrough)
            before_box = slide.shapes.add_textbox(Inches(x + 0.15), Inches(ba_y), Inches(1.2), Inches(0.35))
            tf = before_box.text_frame
            p = tf.paragraphs[0]
            p.text = before
            p.font.size = Pt(11)
            p.font.color.rgb = self._hex_to_rgb(self.COLORS["ms_red"])
            p.alignment = PP_ALIGN.CENTER
            
            # Arrow
            arrow_box = slide.shapes.add_textbox(Inches(x + 1.4), Inches(ba_y), Inches(0.6), Inches(0.35))
            tf = arrow_box.text_frame
            p = tf.paragraphs[0]
            p.text = "→"
            p.font.size = Pt(14)
            p.font.bold = True
            p.font.color.rgb = self._hex_to_rgb(self.COLORS["ms_green"])
            p.alignment = PP_ALIGN.CENTER
            
            # After (green)
            after_box = slide.shapes.add_textbox(Inches(x + 2.0), Inches(ba_y), Inches(1.5), Inches(0.35))
            tf = after_box.text_frame
            p = tf.paragraphs[0]
            p.text = after
            p.font.size = Pt(11)
            p.font.bold = True
            p.font.color.rgb = self._hex_to_rgb(self.COLORS["ms_green"])
            p.alignment = PP_ALIGN.CENTER

    def _populate_before_after_slide(self, slide, config: Dict) -> None:
        """Populate a slide showing before/after transformation."""
        # Remove template placeholders first
        self._remove_placeholder_shapes(slide)
        
        title = config.get('title', '')
        items = config.get('items', [])
        
        # Set title
        self._add_title_textbox(slide, title, 0.5, 0.3, 12.333, size=28)
        
        # Create table-like layout with before/after
        y_start = 1.3
        row_height = 0.7
        
        # Headers
        self._add_ba_header(slide, "Challenge", 0.5, y_start, 4.5, "ms_red")
        self._add_ba_header(slide, "", 5.1, y_start, 1.0, "ms_green")  # Arrow column
        self._add_ba_header(slide, "Solution", 6.2, y_start, 6.5, "ms_green")
        
        for i, item in enumerate(items):
            row_y = y_start + 0.5 + (i * row_height)
            before = item.get('before', '')
            after = item.get('after', '')
            
            # Before text
            self._add_ba_item(slide, before, 0.5, row_y, 4.5, "dark_gray")
            
            # Arrow
            arrow = slide.shapes.add_textbox(Inches(5.1), Inches(row_y), Inches(1.0), Inches(0.5))
            tf = arrow.text_frame
            p = tf.paragraphs[0]
            p.text = "→"
            p.font.size = Pt(24)
            p.font.bold = True
            p.font.color.rgb = self._hex_to_rgb(self.COLORS["ms_green"])
            p.alignment = PP_ALIGN.CENTER
            
            # After text
            self._add_ba_item(slide, after, 6.2, row_y, 6.5, "ms_green", bold=True)

    def _add_ba_header(self, slide, text: str, x: float, y: float, 
                       width: float, color: str) -> None:
        """Add a before/after header."""
        box = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(width), Inches(0.45))
        tf = box.text_frame
        p = tf.paragraphs[0]
        p.text = text
        p.font.size = Pt(16)
        p.font.bold = True
        p.font.color.rgb = self._hex_to_rgb(self.COLORS[color])

    def _add_ba_item(self, slide, text: str, x: float, y: float, 
                     width: float, color: str, bold: bool = False) -> None:
        """Add a before/after item."""
        box = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(width), Inches(0.5))
        tf = box.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = f"• {text}"
        p.font.size = Pt(14)
        p.font.bold = bold
        p.font.color.rgb = self._hex_to_rgb(self.COLORS[color])

    def _populate_agent_cards_slide(self, slide, config: Dict) -> None:
        """Populate a slide with agent cards (colored boxes like HTML demo)."""
        # Remove template placeholders first
        self._remove_placeholder_shapes(slide)
        
        title = config.get('title', '')
        agents = config.get('agents', [])
        
        # Set title
        self._add_title_textbox(slide, title, 0.5, 0.3, 12.333, size=28)
        
        # Layout agents in a grid
        num_agents = len(agents)
        cols = min(3, num_agents)
        card_width = 3.9
        card_height = 2.0
        gap = 0.2
        
        start_x = (13.333 - (cols * card_width + (cols - 1) * gap)) / 2
        
        for i, agent in enumerate(agents):
            row = i // cols
            col = i % cols
            x = start_x + col * (card_width + gap)
            y = 1.3 + row * (card_height + 0.2)
            
            self._add_agent_card(slide, agent, x, y, card_width, card_height)

    def _add_agent_card(self, slide, agent: Dict, x: float, y: float, 
                        width: float, height: float) -> None:
        """Add a single agent card with gradient-like appearance."""
        name = agent.get('name', '')
        level = agent.get('level', 1)
        description = agent.get('description', '')
        competitors = agent.get('competitors', [])
        
        # Color based on level
        if level == 0:
            bg_color = "#11998e"  # Green for orchestrator
        elif level == 2:
            bg_color = "#667eea"  # Purple for synthesizer
        else:
            bg_color = "#0078d4"  # Blue for Level 1
        
        # Card background
        shape = slide.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE,
            Inches(x), Inches(y), Inches(width), Inches(height)
        )
        shape.fill.solid()
        shape.fill.fore_color.rgb = self._hex_to_rgb(bg_color)
        shape.line.fill.background()
        
        # Level badge
        badge = slide.shapes.add_textbox(Inches(x + 0.1), Inches(y + 0.1), Inches(1.0), Inches(0.25))
        tf = badge.text_frame
        p = tf.paragraphs[0]
        p.text = f"LEVEL {level}"
        p.font.size = Pt(9)
        p.font.bold = True
        p.font.color.rgb = RGBColor(255, 255, 255)
        
        # Agent name
        name_box = slide.shapes.add_textbox(Inches(x + 0.1), Inches(y + 0.4), Inches(width - 0.2), Inches(0.4))
        tf = name_box.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = name
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = RGBColor(255, 255, 255)
        
        # Description
        if description:
            desc_box = slide.shapes.add_textbox(Inches(x + 0.1), Inches(y + 0.85), Inches(width - 0.2), Inches(0.6))
            tf = desc_box.text_frame
            tf.word_wrap = True
            p = tf.paragraphs[0]
            p.text = description
            p.font.size = Pt(10)
            p.font.color.rgb = RGBColor(230, 230, 230)
        
        # Competitors (if any)
        if competitors:
            comp_box = slide.shapes.add_textbox(Inches(x + 0.1), Inches(y + height - 0.4), Inches(width - 0.2), Inches(0.3))
            tf = comp_box.text_frame
            tf.word_wrap = True
            p = tf.paragraphs[0]
            p.text = " | ".join(competitors[:4])  # Max 4 competitors
            p.font.size = Pt(8)
            p.font.color.rgb = RGBColor(200, 200, 200)

    def _populate_metric_boxes_slide(self, slide, config: Dict) -> None:
        """Populate a slide with large metric/stat boxes."""
        # Remove template placeholders first
        self._remove_placeholder_shapes(slide)
        
        title = config.get('title', '')
        metrics = config.get('metrics', [])
        
        # Set title
        self._add_title_textbox(slide, title, 0.5, 0.3, 12.333, size=28)
        
        # Calculate positions
        num_metrics = len(metrics)
        box_width = 3.5
        box_height = 2.5
        gap = 0.4
        
        total_width = num_metrics * box_width + (num_metrics - 1) * gap
        start_x = (13.333 - total_width) / 2
        
        for i, metric in enumerate(metrics):
            x = start_x + i * (box_width + gap)
            self._add_metric_box(slide, metric, x, 2.0, box_width, box_height)

    def _add_metric_box(self, slide, metric: Dict, x: float, y: float,
                        width: float, height: float) -> None:
        """Add a single metric box with large number and label."""
        value = metric.get('value', '')
        label = metric.get('label', '')
        description = metric.get('description', '')
        color = metric.get('color', 'ms_blue')
        
        # Box background
        shape = slide.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE,
            Inches(x), Inches(y), Inches(width), Inches(height)
        )
        shape.fill.solid()
        shape.fill.fore_color.rgb = self._hex_to_rgb(self.COLORS.get(color, self.COLORS["ms_blue"]))
        shape.line.fill.background()
        
        # Large value
        val_box = slide.shapes.add_textbox(Inches(x), Inches(y + 0.3), Inches(width), Inches(1.0))
        tf = val_box.text_frame
        p = tf.paragraphs[0]
        p.text = str(value)
        p.font.size = Pt(48)
        p.font.bold = True
        p.font.color.rgb = RGBColor(255, 255, 255)
        p.alignment = PP_ALIGN.CENTER
        
        # Label
        label_box = slide.shapes.add_textbox(Inches(x), Inches(y + 1.4), Inches(width), Inches(0.5))
        tf = label_box.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = label
        p.font.size = Pt(14)
        p.font.bold = True
        p.font.color.rgb = RGBColor(255, 255, 255)
        p.alignment = PP_ALIGN.CENTER
        
        # Description
        if description:
            desc_box = slide.shapes.add_textbox(Inches(x + 0.1), Inches(y + 1.9), Inches(width - 0.2), Inches(0.5))
            tf = desc_box.text_frame
            tf.word_wrap = True
            p = tf.paragraphs[0]
            p.text = description
            p.font.size = Pt(10)
            p.font.color.rgb = RGBColor(220, 220, 220)
            p.alignment = PP_ALIGN.CENTER

    def _populate_process_flow_slide(self, slide, config: Dict) -> None:
        """Populate a slide with a horizontal process flow."""
        # Remove template placeholders first
        self._remove_placeholder_shapes(slide)
        
        title = config.get('title', '')
        steps = config.get('steps', [])
        
        # Set title
        self._add_title_textbox(slide, title, 0.5, 0.3, 12.333, size=28)
        
        num_steps = len(steps)
        if num_steps == 0:
            return
            
        # Calculate positions
        step_width = 2.0
        arrow_width = 0.8
        total_width = num_steps * step_width + (num_steps - 1) * arrow_width
        start_x = (13.333 - total_width) / 2
        
        for i, step in enumerate(steps):
            x = start_x + i * (step_width + arrow_width)
            self._add_process_step(slide, step, x, 2.5, step_width, i + 1)
            
            # Add arrow between steps
            if i < num_steps - 1:
                arrow_x = x + step_width + 0.1
                self._add_flow_arrow(slide, arrow_x, 3.5, arrow_width - 0.2)

    def _add_process_step(self, slide, step: Dict, x: float, y: float,
                          width: float, number: int) -> None:
        """Add a single process step with number circle and description."""
        title = step.get('title', step) if isinstance(step, dict) else step
        description = step.get('description', '') if isinstance(step, dict) else ''
        duration = step.get('duration', '') if isinstance(step, dict) else ''
        
        # Number circle
        circle = slide.shapes.add_shape(
            MSO_SHAPE.OVAL,
            Inches(x + width/2 - 0.3), Inches(y), Inches(0.6), Inches(0.6)
        )
        circle.fill.solid()
        circle.fill.fore_color.rgb = self._hex_to_rgb(self.COLORS["ms_blue"])
        circle.line.fill.background()
        
        # Number text
        num_box = slide.shapes.add_textbox(Inches(x + width/2 - 0.3), Inches(y + 0.08), Inches(0.6), Inches(0.5))
        tf = num_box.text_frame
        p = tf.paragraphs[0]
        p.text = str(number)
        p.font.size = Pt(18)
        p.font.bold = True
        p.font.color.rgb = RGBColor(255, 255, 255)
        p.alignment = PP_ALIGN.CENTER
        
        # Title
        title_box = slide.shapes.add_textbox(Inches(x), Inches(y + 0.8), Inches(width), Inches(0.6))
        tf = title_box.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = self._hex_to_rgb(self.COLORS["ms_blue"])
        p.alignment = PP_ALIGN.CENTER
        
        # Description
        if description:
            desc_box = slide.shapes.add_textbox(Inches(x), Inches(y + 1.4), Inches(width), Inches(0.8))
            tf = desc_box.text_frame
            tf.word_wrap = True
            p = tf.paragraphs[0]
            p.text = description
            p.font.size = Pt(9)
            p.font.color.rgb = self._hex_to_rgb(self.COLORS["medium_gray"])
            p.alignment = PP_ALIGN.CENTER
        
        # Duration badge
        if duration:
            dur_box = slide.shapes.add_textbox(Inches(x + width/2 - 0.4), Inches(y + 2.2), Inches(0.8), Inches(0.3))
            tf = dur_box.text_frame
            p = tf.paragraphs[0]
            p.text = duration
            p.font.size = Pt(9)
            p.font.bold = True
            p.font.color.rgb = self._hex_to_rgb(self.COLORS["ms_orange"])
            p.alignment = PP_ALIGN.CENTER

    def _add_flow_arrow(self, slide, x: float, y: float, width: float) -> None:
        """Add a flow arrow between process steps."""
        arrow = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(width), Inches(0.5))
        tf = arrow.text_frame
        p = tf.paragraphs[0]
        p.text = "→"
        p.font.size = Pt(28)
        p.font.bold = True
        p.font.color.rgb = self._hex_to_rgb(self.COLORS["ms_blue"])
        p.alignment = PP_ALIGN.CENTER

    def _populate_bullets(self, text_frame, bullets: List[str]) -> None:
        """Populate a text frame with bullet points."""
        # Clear existing paragraphs except first
        while len(text_frame.paragraphs) > 1:
            p = text_frame.paragraphs[-1]._p
            text_frame._txBody.remove(p)

        for i, bullet in enumerate(bullets):
            if i == 0:
                p = text_frame.paragraphs[0]
            else:
                p = text_frame.paragraphs[-1]._p.addnext(text_frame.paragraphs[0]._p.makeelement('{http://schemas.openxmlformats.org/drawingml/2006/main}p', {}))
                p = text_frame.paragraphs[-1]

            p.text = bullet
            self._style_text(p, "body")

    def _style_text(self, paragraph, style: str) -> None:
        """Apply font styling to a paragraph."""
        font_config = self.FONTS.get(style, self.FONTS["body"])
        if paragraph.runs:
            for run in paragraph.runs:
                run.font.name = font_config["name"]
                run.font.size = Pt(font_config["size"])
        else:
            paragraph.font.name = font_config["name"]
            paragraph.font.size = Pt(font_config["size"])

    # ==================== HELPER METHODS FOR CONTENT ====================

    def _add_title_textbox(self, slide, text: str, x: float, y: float, width: float, 
                            size: int = 44, color: str = None) -> None:
        """Add a title text box."""
        textbox = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(width), Inches(1))
        tf = textbox.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = text
        p.font.name = self.FONTS["title"]["name"]
        p.font.size = Pt(size)
        # Use provided color or default to dark_gray
        text_color = color if color else self.COLORS["dark_gray"]
        p.font.color.rgb = self._hex_to_rgb(text_color)

    def _add_subtitle_textbox(self, slide, text: str, x: float, y: float, width: float,
                              color: str = None) -> None:
        """Add a subtitle text box."""
        textbox = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(width), Inches(0.6))
        tf = textbox.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = text
        p.font.name = self.FONTS["subtitle"]["name"]
        p.font.size = Pt(self.FONTS["subtitle"]["size"])
        # Use provided color or default to medium_gray
        text_color = color if color else self.COLORS["medium_gray"]
        p.font.color.rgb = self._hex_to_rgb(text_color)

    def _add_bullet_textbox(self, slide, bullets: List[str], x: float, y: float, 
                            width: float, height: float, color: str = None) -> None:
        """Add a text box with bullet points."""
        textbox = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(width), Inches(height))
        tf = textbox.text_frame
        tf.word_wrap = True
        # Use provided color or default to dark_gray
        text_color = color if color else self.COLORS["dark_gray"]

        for i, bullet in enumerate(bullets):
            if i == 0:
                p = tf.paragraphs[0]
            else:
                p = tf.add_paragraph()
            p.text = f"• {bullet}"
            p.font.name = self.FONTS["body"]["name"]
            p.font.size = Pt(self.FONTS["body"]["size"])
            p.font.color.rgb = self._hex_to_rgb(text_color)
            p.space_after = Pt(12)

    def _add_two_column_content(self, slide, left_title: str, right_title: str,
                                left_items: List[str], right_items: List[str]) -> None:
        """Add two-column content with titles and bullet points."""
        # Left column title
        left_header = slide.shapes.add_textbox(Inches(0.5), Inches(1.3), Inches(5.8), Inches(0.5))
        tf = left_header.text_frame
        p = tf.paragraphs[0]
        p.text = left_title
        p.font.name = self.FONTS["body"]["name"]
        p.font.size = Pt(18)
        p.font.bold = True
        p.font.color.rgb = self._hex_to_rgb(self.COLORS["ms_blue"])
        
        # Right column title
        right_header = slide.shapes.add_textbox(Inches(6.8), Inches(1.3), Inches(5.8), Inches(0.5))
        tf = right_header.text_frame
        p = tf.paragraphs[0]
        p.text = right_title
        p.font.name = self.FONTS["body"]["name"]
        p.font.size = Pt(18)
        p.font.bold = True
        p.font.color.rgb = self._hex_to_rgb(self.COLORS["ms_blue"])
        
        # Left column bullets
        if left_items:
            left_content = slide.shapes.add_textbox(Inches(0.5), Inches(1.9), Inches(5.8), Inches(4.5))
            tf = left_content.text_frame
            tf.word_wrap = True
            for i, item in enumerate(left_items):
                if i == 0:
                    p = tf.paragraphs[0]
                else:
                    p = tf.add_paragraph()
                p.text = f"• {item}"
                p.font.name = self.FONTS["body"]["name"]
                p.font.size = Pt(16)
                p.font.color.rgb = self._hex_to_rgb(self.COLORS["dark_gray"])
                p.space_after = Pt(10)
        
        # Right column bullets
        if right_items:
            right_content = slide.shapes.add_textbox(Inches(6.8), Inches(1.9), Inches(5.8), Inches(4.5))
            tf = right_content.text_frame
            tf.word_wrap = True
            for i, item in enumerate(right_items):
                if i == 0:
                    p = tf.paragraphs[0]
                else:
                    p = tf.add_paragraph()
                p.text = f"• {item}"
                p.font.name = self.FONTS["body"]["name"]
                p.font.size = Pt(16)
                p.font.color.rgb = self._hex_to_rgb(self.COLORS["dark_gray"])
                p.space_after = Pt(10)

    def _add_comparison_content(self, slide, left_label: str, right_label: str,
                                left_items: List[str], right_items: List[str]) -> None:
        """Add comparison content to a slide."""
        # Left column header
        self._add_column_header(slide, left_label, 0.5, 1.8, 5.5, "ms_red")
        # Right column header
        self._add_column_header(slide, right_label, 7.0, 1.8, 5.5, "ms_blue")

        # Left items
        y_start = 2.5
        for i, item in enumerate(left_items):
            self._add_comparison_item(slide, item, 0.5, y_start + (i * 0.7), 5.5, "ms_red")

        # Right items
        for i, item in enumerate(right_items):
            self._add_comparison_item(slide, item, 7.0, y_start + (i * 0.7), 5.5, "ms_blue")

        # Arrow in the middle
        self._add_arrow(slide, 6.0, 3.5)

    def _add_column_header(self, slide, text: str, x: float, y: float, 
                           width: float, color: str) -> None:
        """Add a column header."""
        textbox = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(width), Inches(0.5))
        tf = textbox.text_frame
        p = tf.paragraphs[0]
        p.text = text.upper()
        p.font.name = self.FONTS["body"]["name"]
        p.font.size = Pt(14)
        p.font.bold = True
        p.font.color.rgb = self._hex_to_rgb(self.COLORS[color])

    def _add_comparison_item(self, slide, text: str, x: float, y: float,
                             width: float, color: str) -> None:
        """Add a comparison item with bullet."""
        # Bullet circle
        bullet = slide.shapes.add_shape(
            MSO_SHAPE.OVAL,
            Inches(x), Inches(y + 0.1),
            Inches(0.15), Inches(0.15)
        )
        bullet.fill.solid()
        bullet.fill.fore_color.rgb = self._hex_to_rgb(self.COLORS[color])
        bullet.line.fill.background()

        # Text
        textbox = slide.shapes.add_textbox(Inches(x + 0.25), Inches(y), Inches(width - 0.25), Inches(0.6))
        tf = textbox.text_frame
        p = tf.paragraphs[0]
        p.text = text
        p.font.name = self.FONTS["body"]["name"]
        p.font.size = Pt(16)
        p.font.color.rgb = self._hex_to_rgb(self.COLORS["dark_gray"])

    def _add_arrow(self, slide, x: float, y: float) -> None:
        """Add an arrow shape."""
        textbox = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(1), Inches(0.5))
        tf = textbox.text_frame
        p = tf.paragraphs[0]
        p.text = "→"
        p.font.size = Pt(36)
        p.font.color.rgb = self._hex_to_rgb(self.COLORS["ms_blue"])
        p.alignment = PP_ALIGN.CENTER

    def _add_quote_box(self, slide, quote: str, author: str) -> None:
        """Add a quote box."""
        # Quote background
        box = slide.shapes.add_shape(
            MSO_SHAPE.RECTANGLE,
            Inches(1), Inches(2),
            Inches(11.333), Inches(3)
        )
        box.fill.solid()
        box.fill.fore_color.rgb = self._hex_to_rgb(self.COLORS["ms_blue"])
        box.line.fill.background()

        # Quote text
        textbox = slide.shapes.add_textbox(Inches(1.5), Inches(2.5), Inches(10.333), Inches(2))
        tf = textbox.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = f'"{quote}"'
        p.font.name = "Segoe UI Light"
        p.font.size = Pt(28)
        p.font.italic = True
        p.font.color.rgb = self._hex_to_rgb(self.COLORS["white"])
        p.alignment = PP_ALIGN.CENTER

        # Author
        if author:
            author_box = slide.shapes.add_textbox(Inches(1), Inches(5.2), Inches(11.333), Inches(0.5))
            tf = author_box.text_frame
            p = tf.paragraphs[0]
            p.text = f"— {author}"
            p.font.name = self.FONTS["caption"]["name"]
            p.font.size = Pt(16)
            p.font.color.rgb = self._hex_to_rgb(self.COLORS["medium_gray"])
            p.alignment = PP_ALIGN.RIGHT

    def _add_stats_boxes(self, slide, prs, stats: List[Dict]) -> None:
        """Add statistics/metric boxes."""
        num_stats = len(stats)
        if num_stats == 0:
            return

        box_width = min(3.5, 11.0 / num_stats)
        spacing = (12.333 - (box_width * num_stats)) / (num_stats + 1)
        y_start = 2.0

        for i, stat in enumerate(stats):
            x = 0.5 + spacing + (i * (box_width + spacing))
            value = stat.get('value', '')
            label = stat.get('label', '')
            sublabel = stat.get('sublabel', '')

            # Box background
            box = slide.shapes.add_shape(
                MSO_SHAPE.ROUNDED_RECTANGLE,
                Inches(x), Inches(y_start),
                Inches(box_width), Inches(2.5)
            )
            box.fill.solid()
            box.fill.fore_color.rgb = self._hex_to_rgb(self.COLORS["white"])
            box.line.color.rgb = self._hex_to_rgb(self.COLORS["light_gray"])
            box.line.width = Pt(1)

            # Value
            value_box = slide.shapes.add_textbox(
                Inches(x), Inches(y_start + 0.4),
                Inches(box_width), Inches(0.8)
            )
            tf = value_box.text_frame
            p = tf.paragraphs[0]
            p.text = str(value)
            p.font.name = "Segoe UI Light"
            p.font.size = Pt(48)
            p.font.color.rgb = self._hex_to_rgb(self.COLORS["ms_blue"])
            p.alignment = PP_ALIGN.CENTER

            # Label
            label_box = slide.shapes.add_textbox(
                Inches(x), Inches(y_start + 1.4),
                Inches(box_width), Inches(0.5)
            )
            tf = label_box.text_frame
            p = tf.paragraphs[0]
            p.text = label
            p.font.name = self.FONTS["body"]["name"]
            p.font.size = Pt(16)
            p.font.bold = True
            p.font.color.rgb = self._hex_to_rgb(self.COLORS["dark_gray"])
            p.alignment = PP_ALIGN.CENTER

            # Sublabel
            if sublabel:
                sub_box = slide.shapes.add_textbox(
                    Inches(x), Inches(y_start + 1.9),
                    Inches(box_width), Inches(0.5)
                )
                tf = sub_box.text_frame
                tf.word_wrap = True
                p = tf.paragraphs[0]
                p.text = sublabel
                p.font.name = self.FONTS["caption"]["name"]
                p.font.size = Pt(12)
                p.font.color.rgb = self._hex_to_rgb(self.COLORS["medium_gray"])
                p.alignment = PP_ALIGN.CENTER

    def _add_pipeline_boxes(self, slide, prs, steps: List[Dict]) -> None:
        """Add pipeline/process flow boxes."""
        num_steps = len(steps)
        if num_steps == 0:
            return

        # Calculate dimensions
        total_width = 12.333
        step_width = (total_width - 1) / num_steps
        y_start = 2.5

        for i, step in enumerate(steps):
            x = 0.5 + (i * step_width)
            label = step.get('label', f'Step {i+1}')
            description = step.get('description', '')
            number = step.get('number', i + 1)

            # Circle with number
            circle = slide.shapes.add_shape(
                MSO_SHAPE.OVAL,
                Inches(x + (step_width/2) - 0.3), Inches(y_start),
                Inches(0.6), Inches(0.6)
            )
            circle.fill.solid()
            circle.fill.fore_color.rgb = self._hex_to_rgb(self.COLORS["ms_blue"])
            circle.line.fill.background()

            # Number in circle
            tf = circle.text_frame
            p = tf.paragraphs[0]
            p.text = str(number)
            p.font.name = self.FONTS["body"]["name"]
            p.font.size = Pt(18)
            p.font.bold = True
            p.font.color.rgb = self._hex_to_rgb(self.COLORS["white"])
            p.alignment = PP_ALIGN.CENTER

            # Label below circle
            label_box = slide.shapes.add_textbox(
                Inches(x), Inches(y_start + 0.8),
                Inches(step_width), Inches(0.5)
            )
            tf = label_box.text_frame
            p = tf.paragraphs[0]
            p.text = label
            p.font.name = self.FONTS["body"]["name"]
            p.font.size = Pt(14)
            p.font.bold = True
            p.font.color.rgb = self._hex_to_rgb(self.COLORS["dark_gray"])
            p.alignment = PP_ALIGN.CENTER

            # Description
            if description:
                desc_box = slide.shapes.add_textbox(
                    Inches(x), Inches(y_start + 1.3),
                    Inches(step_width), Inches(0.5)
                )
                tf = desc_box.text_frame
                tf.word_wrap = True
                p = tf.paragraphs[0]
                p.text = description
                p.font.name = self.FONTS["caption"]["name"]
                p.font.size = Pt(12)
                p.font.color.rgb = self._hex_to_rgb(self.COLORS["medium_gray"])
                p.alignment = PP_ALIGN.CENTER

            # Arrow to next step
            if i < num_steps - 1:
                arrow_x = x + step_width - 0.3
                arrow_box = slide.shapes.add_textbox(
                    Inches(arrow_x), Inches(y_start + 0.1),
                    Inches(0.5), Inches(0.5)
                )
                tf = arrow_box.text_frame
                p = tf.paragraphs[0]
                p.text = "→"
                p.font.size = Pt(24)
                p.font.color.rgb = self._hex_to_rgb(self.COLORS["light_gray"])
                p.alignment = PP_ALIGN.CENTER

    def _save_presentation(self, prs: Presentation, filename: str, kwargs: Dict) -> str:
        """Save the presentation to file."""
        if not filename.endswith('.pptx'):
            filename = f"{filename}.pptx"

        # Get customer name for subfolder organization
        customer = kwargs.get('customer', '')
        
        # Build output directory - create customer subfolder if specified
        base_output_dir = kwargs.get('output_dir', os.path.join(self.base_path, 'docs', 'ppt'))
        if customer:
            # Sanitize customer name for folder (lowercase, replace spaces with underscores)
            customer_folder = customer.lower().replace(' ', '_').replace('-', '_')
            customer_folder = ''.join(c for c in customer_folder if c.isalnum() or c == '_')
            output_dir = os.path.join(base_output_dir, customer_folder)
        else:
            output_dir = base_output_dir
            
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        local_path = os.path.join(output_dir, filename)

        try:
            prs.save(local_path)
        except Exception as e:
            # Fallback to temp directory
            import tempfile
            local_path = os.path.join(tempfile.gettempdir(), filename)
            prs.save(local_path)

        result = {
            "status": "success",
            "filename": filename,
            "local_path": os.path.abspath(local_path),
            "customer": customer if customer else "none",
            "customer_folder": output_dir,
            "template_used": kwargs.get('template', 'BaseTemplateBlue')
        }

        return json.dumps(result, indent=2)
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
