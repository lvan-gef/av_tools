import argparse
import sys
from pathlib import Path
from collections import namedtuple
import shutil

import pymupdf
from pptx import Presentation
from pptx.util import Inches

RESOLUTION = namedtuple('resolution', ['width', 'height'])


def main(pdf: Path, reso: namedtuple, out: Path) -> None:
    outdir = pdf.parent.joinpath('.converted')
    outdir.mkdir(parents=True, exist_ok=True)

    pngs = _pdf_to_png(pdf=pdf, reso=reso, outdir=outdir)
    pptx = _png_to_pptx(pngs_list=pngs, pptx=out)

    shutil.move(pptx, out)
    print(f'Powerpoint is saved at location: "{out}"')
    shutil.rmtree(str(outdir))


def _pdf_to_png(pdf: Path, reso: namedtuple, outdir: Path) -> list[Path]:
    outlist_pngs = []

    print('Start parsing pdf')
    doc = pymupdf.open(pdf)

    for i, page in enumerate(doc, start=1):
        rect = page.rect
        page_width, page_height = rect.width, rect.height

        scale_width = reso.width / page_width
        scale_height = reso.height / page_height
        scale = min(scale_width, scale_height)

        matrix = pymupdf.Matrix(scale, scale)
        pix = page.get_pixmap(matrix=matrix)

        png_path = outdir.joinpath(f'page_{i}.png')
        pix.save(png_path)
        outlist_pngs.append(png_path)

    doc.close()

    return outlist_pngs


def _png_to_pptx(pngs_list: list[Path], pptx: Path) -> Path:
    print('Creating powerpoint')
    prs = Presentation()

    prs.slide_width = Inches(20)
    prs.slide_height = Inches(11.25)
    slide_width = prs.slide_width
    slide_height = prs.slide_height

    for img_path in pngs_list:
        blank_slide_layout = prs.slide_layouts[6]
        slide = prs.slides.add_slide(blank_slide_layout)

        pic = slide.shapes.add_picture(str(img_path), 0, 0)

        width_ratio = slide_width / pic.width
        height_ratio = slide_height / pic.height
        scaling_factor = min(width_ratio, height_ratio, 1)

        pic.width = int(pic.width * scaling_factor)
        pic.height = int(pic.height * scaling_factor)

        pic.left = int((slide_width - pic.width) / 2)
        pic.top = int((slide_height - pic.height) / 2)

    prs.save(pptx.name)
    return Path(pptx.name).resolve()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='pdf2pptx',
        description='Convert pdf to pptx')
    parser.add_argument('filename', type=Path, help='The path to the pdf file')
    parser.add_argument('-r', '--resolution',
                        type=str,
                        default='1920x1080',
                        help='The target resolution of the presention (default 1920x1080)')
    args = parser.parse_args()

    args.filename = Path(str(args.filename).lower()).resolve()
    if not args.filename.exists():
        print(f'The pdf: "{args.filename}" does not exists')
        exit(1)

    res = args.resolution.split('x')
    if len(res) != 2:
        print('Not engough arguments for resolution, use format: "<width>x<height>"',
              file=sys.stderr)
        exit(2)

    if not res[0].isdigit() or not res[1].isdigit():
        print(f'argument for resolution have a non digit in side it: {res}',
              file=sys.stderr)
        exit(3)

    RES = RESOLUTION(width=int(res[0]), height=int(res[1]))
    outname = Path(str(args.filename).replace('pdf', 'pptx'))

    main(pdf=args.filename.resolve(), reso=RES, out=outname)
