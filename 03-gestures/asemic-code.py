#!/usr/bin/env python3
import vsketch
import bezmerizing
import math

from numpy.random import normal

paper_width = 210
paper_height = 297
paper_padding = 10
character_width = 5
character_height = 8
character_padding = 1
curve_tightness = 8
max_character_num_per_line = math.floor(
    (paper_width - paper_padding * 2) / character_width
)
max_line_num_per_page = math.floor(
    (paper_height - paper_padding * 2) / character_height
)
layout_offset_x = paper_padding + character_width * 0.5
layout_offset_y = paper_padding + character_height * 0.5
vsk = vsketch.Vsketch()
vsk.size(str(paper_width) + "mm", str(paper_height) + "mm", center=False)
vsk.scale("1mm")

text = open(__file__)
line_index = 0
for line in text:
    if line_index < max_line_num_per_page:
        for c in range(len(line)):
            character = line[c]
            if (
                character != " "
                and character != "\n"
                and c < max_character_num_per_line
            ):
                x = c * character_width + layout_offset_x
                y = line_index * character_height + layout_offset_y
                w = character_width - character_padding
                h = character_height - character_padding
                points = []
                if character.isalpha():
                    glyph_complexity = 8
                    stroke_color = 1
                elif character.isdigit():
                    glyph_complexity = 7
                    stroke_color = 2
                else:
                    glyph_complexity = 5
                    stroke_color = 3
                for i in range(glyph_complexity):
                    if character.isupper() or character.isdigit():
                        glyph_point = [normal(0, 0.4), normal(-0.1, 0.2)]
                    elif character.islower():
                        glyph_point = [normal(0, 0.3), normal(0, 0.3)]
                    else:
                        glyph_point = [normal(0, 0.2), normal(0, 0.2)]
                    points.append(glyph_point)

                curve_points = (
                    bezmerizing.Polyline(points)
                    .catmull_spline()
                    .to_polyline(curve_tightness)
                )

                vsk.stroke(stroke_color)
                with vsk.pushMatrix():
                    vsk.translate(x, y)
                    vsk.scale(w, h)
                    vsk.polygon(curve_points)
    line_index += 1

vsk.display()
