from logic_utils import check_guess, get_range_for_difficulty, parse_guess, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# --- Bug 1: Hard difficulty range was easier than Normal (1-50 vs 1-100) ---

def test_hard_range_harder_than_normal():
    _, normal_high = get_range_for_difficulty("Normal")
    _, hard_high = get_range_for_difficulty("Hard")
    assert hard_high > normal_high, (
        f"Hard range (1-{hard_high}) should be wider than Normal (1-{normal_high})"
    )

def test_easy_range_easier_than_normal():
    _, easy_high = get_range_for_difficulty("Easy")
    _, normal_high = get_range_for_difficulty("Normal")
    assert easy_high < normal_high, (
        f"Easy range (1-{easy_high}) should be narrower than Normal (1-{normal_high})"
    )


# --- Bug 2: Invalid guesses still incremented the attempt counter ---
# The fix lives in app.py (only call attempts += 1 when parse_guess returns ok=True).
# These tests verify parse_guess correctly signals invalid input so the caller can gate on it.

def test_parse_guess_empty_string_returns_not_ok():
    ok, _, _ = parse_guess("")
    assert not ok

def test_parse_guess_non_numeric_returns_not_ok():
    ok, _, _ = parse_guess("abc")
    assert not ok

def test_parse_guess_none_returns_not_ok():
    ok, _, _ = parse_guess(None)
    assert not ok

def test_parse_guess_valid_integer_returns_ok():
    ok, value, err = parse_guess("42")
    assert ok
    assert value == 42
    assert err is None

def test_parse_guess_float_string_truncates_to_int():
    ok, value, _ = parse_guess("7.9")
    assert ok
    assert value == 7


# --- Bug 3: "Too High" guesses awarded +5 points on even attempt numbers ---

def test_too_high_never_awards_points():
    score = 50
    # Even attempt — previously gave +5, should now always deduct
    new_score = update_score(score, "Too High", attempt_number=2)
    assert new_score < score, "A wrong guess should never increase the score"

def test_too_high_odd_attempt_deducts_points():
    score = 50
    new_score = update_score(score, "Too High", attempt_number=1)
    assert new_score == score - 5

def test_too_high_even_attempt_deducts_points():
    score = 50
    new_score = update_score(score, "Too High", attempt_number=2)
    assert new_score == score - 5

def test_too_low_always_deducts_points():
    score = 50
    new_score = update_score(score, "Too Low", attempt_number=1)
    assert new_score == score - 5

def test_win_first_attempt_scores_100():
    new_score = update_score(0, "Win", attempt_number=1)
    assert new_score == 100

def test_win_score_decreases_with_more_attempts():
    score_attempt_1 = update_score(0, "Win", attempt_number=1)
    score_attempt_3 = update_score(0, "Win", attempt_number=3)
    assert score_attempt_1 > score_attempt_3

def test_win_score_never_below_10_points():
    # At attempt 10+, the minimum bonus should be 10
    new_score = update_score(0, "Win", attempt_number=20)
    assert new_score == 10
