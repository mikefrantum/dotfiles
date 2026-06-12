#!/usr/bin/env python3
import gi
import math
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GLib

class RecordingOverlay(Gtk.Window):
    def __init__(self):
        super().__init__(type=Gtk.WindowType.POPUP)
        self.wave_offset = 0

        self.set_app_paintable(True)
        self.set_decorated(False)
        self.set_keep_above(True)
        self.set_skip_taskbar_hint(True)
        self.set_skip_pager_hint(True)
        self.set_resizable(False)

        screen = self.get_screen()
        visual = screen.get_rgba_visual()
        if visual:
            self.set_visual(visual)

        self.set_default_size(260, 44)
        # Center top of DP-2 (starts at x=1920, width=2560)
        self.move(1920 + 1280 - 130, 55)

        da = Gtk.DrawingArea()
        da.set_size_request(260, 44)
        da.connect('draw', self.on_draw)
        self.add(da)

        GLib.timeout_add(50, self.animate)
        self.show_all()

    def animate(self):
        self.wave_offset += 0.15
        self.get_child().queue_draw()
        return True

    def on_draw(self, widget, cr):
        w, h = 260, 44

        # Transparent background
        cr.set_operator(0)  # CLEAR
        cr.paint()
        cr.set_operator(2)  # OVER

        # Dark pill background
        r = 10
        cr.set_source_rgba(0.14, 0.15, 0.23, 0.93)
        cr.arc(r, r, r, math.pi, 3*math.pi/2)
        cr.arc(w-r, r, r, 3*math.pi/2, 0)
        cr.arc(w-r, h-r, r, 0, math.pi/2)
        cr.arc(r, h-r, r, math.pi/2, math.pi)
        cr.close_path()
        cr.fill()

        # Orange border
        cr.set_source_rgba(1.0, 0.286, 0.149, 1.0)
        cr.set_line_width(1.5)
        cr.arc(r, r, r, math.pi, 3*math.pi/2)
        cr.arc(w-r, r, r, 3*math.pi/2, 0)
        cr.arc(w-r, h-r, r, 0, math.pi/2)
        cr.arc(r, h-r, r, math.pi/2, math.pi)
        cr.close_path()
        cr.stroke()

        # Red dot
        cr.set_source_rgba(0.93, 0.33, 0.39, 1.0)
        cr.arc(20, h/2, 6, 0, 2*math.pi)
        cr.fill()

        # Text
        cr.set_source_rgba(0.80, 0.85, 0.96, 1.0)
        cr.select_font_face("Sans", 0, 1)
        cr.set_font_size(12)
        cr.move_to(34, h/2 + 4)
        cr.show_text("REC")

        # Wave bars
        bx = 75
        for i in range(8):
            phase = self.wave_offset + i * 0.8
            bh = 6 + 16 * abs(math.sin(phase))
            by = (h - bh) / 2
            g = 0.5 + 0.4 * abs(math.sin(phase))
            cr.set_source_rgba(0.2, g, 0.5, 0.9)
            cr.rectangle(bx + i * 10, by, 6, bh)
            cr.fill()

        return False

if __name__ == '__main__':
    RecordingOverlay()
    Gtk.main()
