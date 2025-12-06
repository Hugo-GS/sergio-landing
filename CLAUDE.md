# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Flask-based landing page server for Sergio's audiovisual production portfolio. The application serves multiple landing page variants through a dynamic routing system.

## Running the Application

### Development Server
```bash
python main.py
```
The server runs on `http://localhost:5000` with debug mode enabled.

### Virtual Environment
```bash
# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Architecture

### Multi-Landing System
The application uses a numeric routing pattern to serve different landing page variants:
- URL pattern: `/landing/<id>` (e.g., `/landing/1`, `/landing/2`)
- Each landing has its own folder in `templates/landing-{id}/`
- Template naming convention: `landing-{id}.html` inside `landing-{id}/` folder
- If a landing ID doesn't exist, returns 404

**Example structure:**
```
templates/
  landing-1/
    landing-1.html
  landing-2/
    landing-2.html
```

### Static Assets Organization
Static files are served from the `/static` directory:
- `static/images/` - Image assets (PNG, JPG)
- `static/videos/` - Video files (MP4)

Note: The static route in `main.py:24-34` has a `send_from_directory` import missing - this needs to be added to the Flask imports.

### Frontend Stack
Landing pages use:
- Tailwind CSS via CDN
- Font Awesome icons
- Google Fonts (Montserrat, Open Sans)
- Custom brand colors defined in Tailwind config:
  - `brand-gold`: #D4AF37
  - `brand-dark`: #0a0a0a
  - `brand-gray`: #1f1f1f
  - `brand-light`: #f3f4f6

## Content Guidelines

The `context.md` file contains the complete structure and content requirements for landing pages, including:
- Video reel on homepage (10-20 seconds, autoplay, muted)
- Service sections (editing, production, post-production)
- Portfolio with 3-6 featured projects
- Work process explanation (brief, proposal, production, reviews, delivery)
- Contact form fields
- Testimonials structure

When creating or modifying landing pages, reference this file for the expected sections and content flow.

## Known Issues

- `main.py:33` - Missing import: `from flask import send_from_directory` is needed for the static file serving route to work.
