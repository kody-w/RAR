---
name: "rar-discreetrappers-powerpoint-generator"
description: "Generate professional PowerPoint presentations using Microsoft templates.\n\nTemplates available:\n- BaseTemplateBlue: Microsoft corporate template (recommended)\n- ZavaTemplate: Modern business template\n- BaseTemplateDynamics: Dynamics-style template\n\nActions:\n- create_presentation: Create multi-slide presentation\n- list_templates: List available templates and their layouts\n- list_layouts: List layouts for a specific template\n\nSlide types: title, section, content, two_column, comparison, quote, stats, pipeline, blank\n\nExample:\n{\n  \"action\": \"create_presentation\",\n  \"customer\": \"Contoso\",\n  \"template\": \"BaseTemplateBlue\",\n  \"output_filename\": \"my_presentation\",\n  \"slides\": [\n    {\"type\": \"title\", \"title\": \"My Presentation\", \"subtitle\": \"Subtitle here\"},\n    {\"type\": \"content\", \"title\": \"Key Points\", \"bullets\": [\"Point 1\", \"Point 2\"]},\n    {\"type\": \"comparison\", \"title\": \"Before vs After\", \"left_label\": \"Before\", \"right_label\": \"After\", \"left_items\": [\"Old way\"], \"right_items\": [\"New way\"]}\n  ]\n}"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@discreetRappers/powerpoint_generator_agent", "rar_sha256": "e1c71838845673ea756b0fea8afa04d3c9014964423cdaf354547df96af9a7e6", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "1.0.2", "author": "Bill Whalen", "tags": ["productivity", "powerpoint", "presentations", "templates", "microsoft"]}
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
