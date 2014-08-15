import textwrap
import moviepy.editor as moviepy

def make_element(quote, author, size):
    signature = (moviepy.TextClip("- %s"%author, fontsize=30,
                               color='gray',)
                               #font="Amiri-Slanted")
                  .margin(right=30, bottom=30, opacity=0)
                  .set_pos(("right","bottom")))
    quote = '\n'.join(textwrap.wrap(quote))
    quote_clip = (moviepy.TextClip(quote, fontsize=23,
                          font="Amiri-Bold", align="center")
                            .set_duration(len(quote)*.065)
                            .set_pos("center")
                            .crossfadein(.2)
                            .crossfadeout(.2))
    element = (moviepy.CompositeVideoClip(
                   [signature, quote_clip], size=size, bg_color=(233,229,90))
                    .set_duration(quote_clip.duration))
    return element
