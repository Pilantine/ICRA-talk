from manim import *

class EDiamThinking(Scene):
    def construct(self):
        self.camera.background_color = ManimColor("#0f111a")
        self.camera.background_color.opacity = 0

        tpl = TexTemplate()
        tpl.add_to_preamble(r"""
\usepackage{tikz}
\usetikzlibrary{shapes}
\definecolor{darkbg}{HTML}{1a1d2e}
\definecolor{textcol}{HTML}{e2e8f0}
""")

        def make_cloud(text_width, aspect, scale, pos, with_text=False):
            text_content = r"Interesting\ldots" if with_text else r"\phantom{x}"
            font_size = r"\itshape\LARGE" if with_text else r"\tiny"
            tw = f"{text_width}cm"
            obj = Tex(
                rf"""\begin{{tikzpicture}}
\node[cloud, cloud puffs=10, cloud puff arc=110, aspect={aspect},
      draw=white, line width=1.8pt,
      fill=darkbg,
      text=textcol, text width={tw}, align=center,
      font={font_size}]
  at (0,0) {{{text_content}}};
\end{{tikzpicture}}""",
                tex_template=tpl,
            )
            obj.scale(scale)
            obj.move_to(pos)
            return obj

        # E_diamond — bottom-left
        ediam = MathTex(r"\mathcal{E}_\diamond", font_size=130, color="#e2b96f")
        ediam.move_to(LEFT * 3.5 + DOWN * 1.8)

        # Progressive clouds: small → medium → large (with text)
        c1 = make_cloud(text_width=0.3, aspect=1.4, scale=0.15, pos=LEFT * 2.9 + DOWN * 1.2)
        c2 = make_cloud(text_width=0.3, aspect=1.4, scale=0.22, pos=LEFT * 2.2 + DOWN * 0.6)
        c3 = make_cloud(text_width=0.8, aspect=1.6, scale=0.32, pos=LEFT * 1.4 + UP * 0.1)
        c5 = make_cloud(text_width=5.0, aspect=2.5, scale=0.65, pos=RIGHT * 2.0 + UP * 1.6, with_text=True)

        # Animations
        self.play(FadeIn(ediam, run_time=1.8, rate_func=smooth))
        self.wait(0.4)
        self.play(FadeIn(c1, scale=0.5), run_time=0.35)
        self.play(FadeIn(c2, scale=0.5), run_time=0.35)
        self.play(FadeIn(c3, scale=0.5), run_time=0.35)
        self.play(FadeIn(c5, scale=0.5), run_time=0.7)
        self.wait(2.5)
