import base64, sys, os
from concurrent.futures import ThreadPoolExecutor
from openai import OpenAI
client = OpenAI()
OUT = "C:/Repos/sites/buildingyourown/assets"
STYLE = ("Style contract: clean editorial line-art illustration on an off-white (#f7f8fa) background, deep-navy (#0f172a) outlines, "
 "brand-blue (#2563eb) for arrows, accents and icons, gold (#b88a1b) used sparingly for one small highlight only. Generous whitespace, "
 "ONE clear concept, landscape 3:2. Minimal, confident, warm. Simple line figures of people (diverse, no faces detail). "
 "NO text, NO letters, NO words, NO numbers, NO logos anywhere in the image. No photorealism, no 3D render, no heavy gradients, no green accents.")
P = {
 "home-hero": "A small group of five people around one long table in a bright room, each with a laptop, building something together. "
   "Above the table, light blue line drawings of the small tools they are building float up: a simple dashboard, a checklist, a flow of connected boxes. "
   "Underneath the floating tools, a clean grid of tidy structured blocks acts as a foundation, with one small gold diamond spark where structure meets the tools. "
   "The mood: hands-on, collaborative, capable. ",
 "home-prepare": "Preparation before a workshop: on the left a single clipboard questionnaire with blank lines and checkboxes, "
   "in the middle a simple video-call window with two line figures talking, on the right one tidy one-page canvas divided into a few blank panels. "
   "Blue arrows connect the three from left to right. Calm, organised, personal. ",
 "home-build": "The build day itself: in the foreground one person at a laptop building, a coach leaning in beside them pointing at the screen, helping. "
   "On the laptop screen, a simple line-drawn app made of connected blocks. Behind them, the rest of a small group builds in pairs. "
   "Energetic but focused. ",
 "home-demo": "The demo moment and taking it home: one person stands proudly next to a large screen showing a simple working app (connected blocks, a small chart), "
   "a small seated group listens and one raises a hand with a question. On the right edge, a line-drawn path leads from the room to a small office building, "
   "carrying a laptop: the result goes home. One small gold spark on the screen. ",
}
def gen(name):
    r = client.images.generate(model="gpt-image-1", prompt=P[name]+STYLE, size="1536x1024", quality="high", n=1)
    open(f"{OUT}/{name}.png","wb").write(base64.b64decode(r.data[0].b64_json))
    return name
names = sys.argv[1:] or list(P)
with ThreadPoolExecutor(4) as ex:
    for n in ex.map(gen, names): print("ok", n)
