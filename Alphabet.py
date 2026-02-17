from js import document, speakFromJS

class AlphabetCard:
    def __init__(self):
        self.letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        self.index = 0

    def tap(self, event=None):
        speakFromJS(self.letters[self.index])
        self.next()   # ✅ เพิ่มบรรทัดนี้


    def next(self):
        self.index = (self.index + 1) % len(self.letters)
        self.update()

    def prev(self):
        self.index = (self.index - 1) % len(self.letters)
        self.update()
        speakFromJS(self.letters[self.index])

    def update(self):
        document.getElementById("letter").textContent = self.letters[self.index]
        document.getElementById("count").textContent = self.index + 1
        document.getElementById("star").textContent = self.index

card = AlphabetCard()

# ---------- expose functions ----------

def pyNext():
    card.next()

def pyPrev():
    card.prev()

# ---------- bind events ----------

def prev_click(e):
    e.stopPropagation()
    pyPrev()

def next_click(e):
    e.stopPropagation()
    pyNext()

document.getElementById("card").onclick = card.tap

prev_btn = document.getElementById("prevBtn")
if prev_btn:
    prev_btn.onclick = prev_click

next_btn = document.getElementById("nextBtn")
if next_btn:
    next_btn.onclick = next_click
