#!/usr/bin/env python3
############################################################ IDENT(1)
#
# $Title: Generate sample condy wallpaper PNGs $
# $Copyright: 2026 The FrauBSD Project. All rights reserved. $
# $FrauBSD: condy/tools/mk-sample-wallpapers.py 2026-09-19 10:29:22 -0700 Devin Teske $
#
############################################################ DOCSTRING

"""Writes theme/wallpaper and theme/tallpaper samples. Run from the
repository root. Images are original FrauBSD work (no third-party art)."""

############################################################ INCLUDES

import os
import struct
import sys
import zlib

############################################################ GLOBALS

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

############################################################ FUNCTIONS

def _chunk(tag, data):
	crc = zlib.crc32(tag)
	crc = zlib.crc32(data, crc) & 0xFFFFFFFF
	return struct.pack(">I", len(data)) + tag + data + struct.pack(">I", crc)


def write_png(path, width, height, pixel_at):
	rows = []
	for y in range(height):
		row = bytearray([0])
		for x in range(width):
			r, g, b = pixel_at(x, y, width, height)
			row.extend((r & 255, g & 255, b & 255))
		rows.append(bytes(row))
	raw = b"".join(rows)
	ihdr = struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0)
	body = (
		b"\x89PNG\r\n\x1a\n"
		+ _chunk(b"IHDR", ihdr)
		+ _chunk(b"IDAT", zlib.compress(raw, 9))
		+ _chunk(b"IEND", b"")
	)
	tmp = path + ".tmp"
	with open(tmp, "wb") as f:
		f.write(body)
	os.rename(tmp, path)
	print("%s (%ux%u, %u bytes)" % (path, width, height, len(body)))


def _lerp(a, b, t):
	return int(a + (b - a) * t + 0.5)


def dusk(x, y, width, height):
	# Dark forest floor to a slightly lighter horizon
	t = float(y) / float(height - 1)
	r = _lerp(6, 18, t)
	g = _lerp(14, 48, t)
	b = _lerp(10, 22, t)
	# Soft left/right vignette so -fill is not a flat slab
	edge = min(x, width - 1 - x) / float(width)
	v = 0.72 + 0.28 * min(1.0, edge * 6.0)
	return (int(r * v), int(g * v), int(b * v))


def field(x, y, width, height):
	# Deeper green, ident.conkyrc graph colors (004F00 / 2AC12A family)
	t = float(y) / float(height - 1)
	r = _lerp(4, 8, t)
	g = _lerp(22, 79, t)
	b = _lerp(8, 16, t)
	band = abs((float(x) / float(width - 1)) - 0.5)
	v = 0.85 + 0.15 * (1.0 - band)
	return (int(r * v), int(g * v), int(b * v))


def night(x, y, width, height):
	t = float(y) / float(height - 1)
	r = _lerp(4, 10, t)
	g = _lerp(8, 18, t)
	b = _lerp(12, 28, t)
	return (r, g, b)


def main():
	land_w, land_h = 1280, 720
	port_w, port_h = 720, 1280
	wall = os.path.join(ROOT, "theme", "wallpaper")
	tall = os.path.join(ROOT, "theme", "tallpaper")
	if not os.path.isdir(wall):
		os.makedirs(wall)
	if not os.path.isdir(tall):
		os.makedirs(tall)
	write_png(os.path.join(wall, "sample-dusk.png"), land_w, land_h, dusk)
	write_png(os.path.join(wall, "sample-field.png"), land_w, land_h, field)
	write_png(os.path.join(wall, "sample-night.png"), land_w, land_h, night)
	write_png(os.path.join(tall, "sample-dusk.png"), port_w, port_h, dusk)
	write_png(os.path.join(tall, "sample-field.png"), port_w, port_h, field)
	write_png(os.path.join(tall, "sample-night.png"), port_w, port_h, night)
	return 0


############################################################ MAIN

if __name__ == "__main__":
	sys.exit(main())

################################################################################
# END
################################################################################
