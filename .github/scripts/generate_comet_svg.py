import svgwrite
import math

def generate_comet_svg(filename="github-contribution-grid-comet.svg"):
    dwg = svgwrite.Drawing(filename, profile='tiny', size=("800px", "200px"))
    comet_color = "#ff0000"
    trail_length = 8

    for frame in range(50):
        frame_group = dwg.g(id=f'frame-{frame}', visibility="hidden")
        for i in range(trail_length):
            offset = frame - i
            if 0 <= offset < 40:
                x = 20 * offset
                y = 100 + int(30 * math.sin(offset / 4.0))
                opacity = 1.0 - (i / trail_length)
                frame_group.add(dwg.circle(center=(x, y), r=6,
                                           fill=comet_color, opacity=opacity))
        dwg.add(frame_group)

    animate_script = """\
let frame = 0;
setInterval(function () {
    for (let i = 0; i < 50; i++) {
        let el = document.getElementById('frame-' + i);
        if (el) el.setAttribute('visibility', i === frame ? 'visible' : 'hidden');
    }
    frame = (frame + 1) % 50;
}, 80);
"""
    dwg.add(dwg.script(type="text/javascript", content=animate_script))
    dwg.save()

generate_comet_svg()
