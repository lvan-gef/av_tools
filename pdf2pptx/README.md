# PDF to PPTX Converter

A command-line tool to convert PDF documents to PowerPoint presentations. Each page of the PDF is converted to a slide in the PowerPoint presentation.

## Features

- Convert PDF files to PPTX format
- Maintain aspect ratio during conversion
- Customize output resolution
- Clean temporary files automatically
- Simple command-line interface

## Installation

1. Clone this repository or download the source code
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Dependencies

The tool requires the following Python packages:
- pymupdf
- python-pptx

## Usage

### Basic Usage

```bash
python main.py path/to/your/file.pdf
```

This will convert `file.pdf` to `file.pptx` in the same directory.

### Custom Resolution

You can specify a custom resolution using the `-r` or `--resolution` flag:

```bash
python main.py path/to/your/file.pdf -r 1280x720
```

The default resolution is 1920x1080.

## Examples

Convert a PDF with default settings:
```bash
python main.py document.pdf
```

## How It Works

1. The PDF is parsed using PyMuPDF
2. Each page is converted to PNG images at the specified resolution
3. The PNG images are inserted into a PowerPoint presentation
4. Temporary files are cleaned up automatically
