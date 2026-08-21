import streamlit as st
import random 
import time

def main():
  st.title("Hangman Game")
  words = [
    "apple", "brave", "cloud", "dance", "eagle", "flame", "grape", "house",
    "ivory", "jewel", "kneel", "lemon", "mango", "night", "ocean", "piano",
    "queen", "river", "storm", "tiger", "umbrella", "violet", "whale", "xenon",
    "yacht", "zebra", "anchor", "basket", "castle", "dragon", "engine", "falcon",
    "garden", "hammer", "island", "jungle", "kitten", "lantern", "mountain", "nature",
    "orange", "pencil", "quality", "rocket", "sunset", "tent", "uniform", "valley",
    "window", "yellow", "bridge", "castle", "desert", "forest", "guitar", "hospital",
    "internet", "jacket", "kitchen", "library", "market", "network", "oxygen", "paradise",
    "question", "rainbow", "safari", "teacher", "universe", "village", "weather", "xylophone",
    "yogurt", "zephyr", "adventure", "butterfly", "chocolate", "dinosaur", "elephant", "firework",
    "galaxy", "horizon", "iceberg", "jigsaw", "kangaroo", "lighthouse", "magnificent", "nebula",
    "orchestra", "penguin", "quartz", "rainforest", "squirrel", "telescope", "unicorn", "volcano",
    "wonderful", "yesterday", "zucchini", "algorithm", "backpack", "cactus", "diamond", "echo",
    "flamingo", "gratitude", "helicopter", "illusion", "jubilee", "keyboard", "landscape", "mystery",
    "navigation", "orchid", "puzzle", "quintessential", "relic", "sunset", "tornado", "utopia",
    "victory", "whisper", "xray", "yawn", "zodiac", "adventure", "breeze", "candle", "dream",
    "echo", "frost", "ghost", "honey", "ivy", "jade", "kite", "lace", "moon", "ninja",
    "owl", "pearl", "quill", "rose", "star", "tulip", "unity", "vase", "wave", "xmas",
    "yard", "zest", "atlas", "beacon", "copper", "dew", "ember", "fable", "glow", "haze",
    "iron", "jewel", "karma", "lunar", "magic", "noble", "oasis", "palm", "quartz", "rust",
    "silk", "tide", "urban", "vivid", "wind", "xeric", "yolk", "zinc"
]
  if "random_word" not in st.session_state:
    st.session_state.random_word = random.choice(words)
    st.session_state.guesses = list("_"*len(st.session_state.random_word))

    if "tracker" not in st.session_state:
      st.session_state.tracker = list(st.session_state.random_word)
  guess = st.text_input("Guess a character: ", value="---")

  if guess in st.session_state.tracker:
    while True:
      pos = "".join(st.session_state.tracker).find(guess)
      st.session_state.tracker[pos] = "_"
      st.session_state.guesses[pos] = guess
      if pos == -1:
        break
      
        
    if "_" in st.session_state.guesses:
      st.write(",".join(st.session_state.guesses))
    else:
      st.write("CONGRATULATIONS!")
      st.write("The word is:  {st.session_state.random_word}")
      time.sleep(3)
      st.session_state.decision = st.text_input("Do you want to play again?", value="---")
      if st.session_state.decision == "Yes":
        st.rerun()
      elif st.session_state.decision == "No":
        st.write("Thank You for playing.")
  else:
    st.write("Try Again!")

if __name__ == "__main__":
  main()
