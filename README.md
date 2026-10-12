# Chapter 7 Exercises - Iteration and Search

This project contains my solutions to the Chapter 7 exercises from *Think Python*, covering loops, strings, searching, and doctests. I completed Exercises 7.9.1 through 7.9.8 in `chapter7_exercises.py`.

## Exercises

- **7.9.1:** Explained why putting `return False` inside the loop makes `uses_any()` stop checking after the first nonmatching letter.
- **7.9.2:** Created `uses_none()` to check whether a word avoids forbidden letters.
- **7.9.3:** Created `uses_only()` to check whether a word contains only allowed letters.
- **7.9.4:** Created `uses_all()` to check whether a word contains every required letter.
- **7.9.5:** Built a word checker and scoring functions using the *Spelling Bee* rules.
- **7.9.6:** Rewrote `uses_none()` by calling `uses_any()` and using `not`.
- **7.9.7:** Rewrote `uses_all()` using `uses_only()` with the arguments reversed.
- **7.9.8:** Rewrote `uses_all()` by calling `uses_any()` for each required letter.

## Testing

I used Python's `doctest` module to test the functions and added examples for different results, uppercase letters, and empty strings.

```text
Doctests run: 34
Doctests failed: 0
```

I also tested the *Spelling Bee* checker and scoring functions:

```text
color: accepted, 5 point(s)
ratatat: accepted, 7 point(s)
rat: not accepted
told: not accepted
bee: not accepted
card: accepted, 1 point(s)
cartload: accepted, 15 point(s)
```

In the last example, `cartload` earns 8 points for its eight letters and 7 bonus points for using every available letter.

## Comparison with the Instructor's Work

The instructor's GitHub README demonstrates an important mistake in `uses_any()`: placing `return False` inside the loop means the function can stop after checking only the first letter. My solution puts `return False` after the loop, so the function checks all the letters unless it finds a match first. I agree with the instructor's corrected approach because the placement of `return` is important for making the search work correctly.

The instructor organized the remaining exercises into separate Python files, while I kept mine in one file with labeled sections. Separate files make it easier to look at one exercise at a time, but I like having all of mine together because I can run the doctests and examples in one place.

I also tried multiple approaches in my own code. For example, my first `uses_none()` uses a loop, but the later version simply returns `not uses_any(word, forbidden)`. I think the loop is easier to understand when first learning how searches work, while the shorter version is better for reusing code and avoiding repetition. The same idea applies to using `uses_only()` to build `uses_all()`.

## Reflection and Possible Improvements

Loops were one of my favorite parts of this chapter because I already remember using repeat and forever loops in Scratch for movement, music, and animations. Python takes that same idea and lets me search through strings and check letters one at a time.

I also enjoyed learning more about doctests. I like that the examples inside a function's documentation can also be used to check whether the function works. Having all 34 tests pass was a useful way to check my work, although passing those tests does not guarantee that every possible input has been covered.

One improvement I could make is adding even more tests for unusual inputs, such as repeated required letters or different combinations of uppercase and lowercase letters. I could also split the exercises into separate files if I wanted to match the instructor's organization. Overall, I think the best solution is one that works correctly, is easy to read, and uses functions without repeating unnecessary code.

## Running the Program

Run `chapter7_exercises.py` in PyCharm, or run the following command from the project folder:

```bash
python chapter7_exercises.py
```

The file uses only Python's built-in `doctest` module, so no extra packages are needed.