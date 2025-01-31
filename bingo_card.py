#!/usr/bin/env python3
"""
No cap, this lit AF bingo generator is straight fire! 🔥 It yeets random slang bro into each card's
squares - think "understood the assignment", "it's giving...", and "dope" vibes.
Slide into the app, and boom! You've got a savage bingo experience that's lowkey hilarious and
totally cringe-proof. Periodt! 💯

If your main character hits different, print some cards and score his talk for some dope fun
that slaps. True that.
"""
import random
from uuid import uuid4

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas



def generate_bingo_card(words, filename):
    # Define the size of the bingo card and its grid
    card_size = (595.27, 841.89)
    grid_size = 5  # 5x5 bingo card
    box_width = card_size[0] / grid_size
    box_height = card_size[1] / grid_size

    # Create a new PDF document
    c = canvas.Canvas(filename, pagesize=letter)

    # Draw the bingo card grid and fill with words
    for i in range(grid_size):
        y1 = (grid_size - 1 - i) * box_height  # Invert y-axis to align text correctly
        for j in range(grid_size):
            x1 = j * box_width

            # Draw the rectangle for each box
            c.rect(x1, y1, box_width, box_height)

            # Place the word in the center of the box
            word = words.pop(0)  # Get and remove the first word from the list
            text = c.beginText(x1 + 10, y1 + box_height // 2)
            text.setFont("Helvetica", 14)
            text.textLine(word)
            c.drawText(text)

    # Save the PDF document
    c.save()
    print(f"Wrote {filename}")


def main():
    # List of words to fill the bingo card
    words_list = (
        "GOAT IYKYK OG TFW boujee bro church clapback dank "
        "dope flex lit rizz salty sesh situation sus sweet yeet"
    ).split(" ")
    words_list.extend([
        "hits different", "just saying", "living rent-free", "no cap", "true that",
        "vibe check", "that slaps",
    ])

    # Shuffle the words to randomize them
    random.shuffle(words_list)

    u = uuid4().hex
    filename: str = f"bingo-{u[:8]}.pdf"

    generate_bingo_card(words_list, filename)


if __name__ == "__main__":
    main()
