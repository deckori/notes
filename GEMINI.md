# GEMINI context

## Directory Overview
Personal academic notes repository for UDST (University of Doha for Science and Technology) Engineering courses. Managed as a [Quarto](https://quarto.org/) website. Uses `git-annex` for binary files (PDFs, images) to keep repo size small, though remote data may be unavailable.

## Key Files
- `_quarto.yml`: Main configuration. Defines website structure, sidebar sections (e.g., "4th Semester"), themes, and rendering rules.
- `sems/`: Organized by semester (`sem1` through `sem4`). Contains course-specific notes in `.qmd` and `.ipynb` formats.
- `class-enroll/`: Course planning and availability trackers for various semesters.
- `replace.sh`: Maintenance script to fix broken `git-annex` pointers by linking to local object storage.
- `templates/`: Custom Quarto templates for PDF and HTML output.

## Usage
- **Rendering:** Use `quarto render` to build the website. Output is stored in `.site/`.
- **Note Taking:** Add or edit `.qmd` files within the appropriate `sems/semN/` directory.
- **Data Management:** Binary files (PDFs) are tracked via `git-annex`. If pointers are broken, use `replace.sh` (requires local annex object store at `/inc/annex/`).
- **Styles:** Custom CSS for enrollment lists in `class-enroll/styles.css`.
