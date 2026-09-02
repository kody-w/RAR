---
name: "rar-discreetrappers-powerpoint-generator"
description: "Generate professional PowerPoint presentations using Microsoft templates.\n\nTemplates available:\n- BaseTemplateBlue: Microsoft corporate template (recommended)\n- ZavaTemplate: Modern business template\n- BaseTemplateDynamics: Dynamics-style template\n\nActions:\n- create_presentation: Create multi-slide presentation\n- list_templates: List available templates and their layouts\n- list_layouts: List layouts for a specific template\n\nSlide types: title, section, content, two_column, comparison, quote, stats, pipeline, blank\n\nExample:\n{\n  \"action\": \"create_presentation\",\n  \"customer\": \"Contoso\",\n  \"template\": \"BaseTemplateBlue\",\n  \"output_filename\": \"my_presentation\",\n  \"slides\": [\n    {\"type\": \"title\", \"title\": \"My Presentation\", \"subtitle\": \"Subtitle here\"},\n    {\"type\": \"content\", \"title\": \"Key Points\", \"bullets\": [\"Point 1\", \"Point 2\"]},\n    {\"type\": \"comparison\", \"title\": \"Before vs After\", \"left_label\": \"Before\", \"right_label\": \"After\", \"left_items\": [\"Old way\"], \"right_items\": [\"New way\"]}\n  ]\n}"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@discreetRappers/powerpoint_generator_agent", "rar_sha256": "5a9fc79dfbf2038ba411e2789dc988713389b2219ff5ce721b02d684d88a23f5", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "powerpoint_generator_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@discreetrappers/powerpoint-generator:8ea151a306b1714dbe02a37c4a9cbbf5e7c9e2d18676cdce14e2e2256231b0ed", "kind": "skill"}, "version": "1.0.2", "author": "Bill Whalen", "tags": ["productivity", "powerpoint", "presentations", "templates", "microsoft"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@discreetRappers/powerpoint_generator_agent`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `powerpoint_generator_agent.py` is
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `powerpoint_generator_agent.py` and embedded as the fenced Python below (sha256 5a9fc79dfbf2038b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `powerpoint_generator_agent.py` first:

```bash
python3 powerpoint_generator_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 powerpoint_generator_agent.py   # or on stdin
python3 powerpoint_generator_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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
