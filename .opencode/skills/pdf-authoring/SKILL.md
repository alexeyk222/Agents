---
name: pdf-authoring
description: Create or revise polished PDF documents and verify their rendered layout. Use for reports, manuals, handouts, forms, or other authored PDFs where typography, pagination, tables, images, and final visual QA matter. Use the existing scientific `pdf` skill instead for specialized scientific-agent PDF processing.
license: Apache-2.0
metadata:
  source: https://github.com/openai/skills/tree/main/skills/.curated/pdf
  upstream-skill: pdf
  adapted-for: OpenAgents Control OpenCode project
  runtime: Existing project document toolchain or explicitly approved dependencies
---

# PDF authoring

> Adaptation notice: this project-local derivative has a conflict-free ID, project output
> conventions, Cyrillic font checks, and approval-aware dependency handling.

Create a maintainable source document and a visually verified PDF. Do not treat successful
file generation as proof that the document renders correctly.

## Select the source format

Prefer the repository's existing document toolchain. If none exists, choose based on the task:

- Typst or LaTeX for structured, text-heavy documents with pagination and references.
- ReportLab for data-driven programmatic generation.
- HTML/CSS plus an available print renderer for web-native layouts.
- An existing editable source when revising a PDF that originated in the project.

Do not add a new package manager, global dependency, or lock-file change merely to create one
document. Inspect available tools first and obtain approval before installing dependencies.

## Workflow

1. Confirm the audience, page size, language, required sections, branding, citations, and final
   output path.
2. Keep the editable source beside the project artifact or in the requested documentation area.
3. Generate the PDF with deterministic inputs and stable filenames.
4. Render every page to images with Poppler when available:

   ```bash
   pdftoppm -png input.pdf .tmp/pdf-runs/task-slug/page
   ```

5. Visually inspect the rendered pages. Check margins, wrapping, clipping, table continuation,
   image resolution, headings, page breaks, headers, footers, and page numbers.
6. Extract text with `pdftotext`, `pdfplumber`, or `pypdf` as a secondary check for missing or
   reordered content. Text extraction does not validate layout.
7. Regenerate and repeat the visual check after every material layout change.

## Fonts and languages

- Use fonts that cover every required script and embed them when the renderer supports it.
- For Russian or other Cyrillic text, do not rely on ReportLab's built-in Helvetica/Times fonts;
  select and register a font with Cyrillic coverage.
- Check rendered output for tofu, black boxes, missing glyphs, broken ligatures, and incorrect
  fallback fonts.
- Preserve typographic punctuation unless the chosen renderer demonstrably mishandles it.

## Quality requirements

- Keep typography, spacing, hierarchy, and color use consistent.
- Keep tables, charts, and figures sharp, aligned, labeled, and legible at normal zoom.
- Avoid orphaned headings, nearly empty pages, accidental blank pages, and clipped footnotes.
- Ensure citations are human-readable and no tool placeholders remain.
- Do not claim PDF/A, accessibility, tagged-PDF, or print-production compliance unless it was
  explicitly requested and validated with an appropriate tool.

## Files and dependencies

- Put disposable renderings in `.tmp/pdf-runs/<task-slug>/`.
- Put the final PDF at the requested path, or under `output/pdf/` if no destination is given.
- Keep the editable source unless the user explicitly requested only the binary artifact.
- Typical optional tools are Poppler, Typst, ReportLab, `pdfplumber`, and `pypdf`; use only the
  subset the chosen workflow needs.
- Never overwrite the only copy of a source PDF. Write a new output and replace only after the
  result has been validated and the user requested replacement.
