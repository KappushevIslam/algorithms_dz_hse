import pytest

from solution import group_anagrams, normalize


@pytest.mark.parametrize("strs,expected", [
    (
        ["eat", "tea", "tan", "ate", "nat", "bat"],
        [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
    ),
    ([], []),
    (["a"], [["a"]]),
    (["ab", "ba", "ab"], [["ab", "ab", "ba"]]),
    (["abc", "def", "ghi"], [["abc"], ["def"], ["ghi"]]),
    (["", ""], [["", ""]]),
    (["listen", "silent", "enlist", "hello"], [["hello"], ["enlist", "listen", "silent"]]),
    (["aab", "aba", "baa", "abb"], [["abb"], ["aab", "aba", "baa"]]),
])
def test_group_anagrams(strs, expected):
    assert normalize(group_anagrams(strs)) == normalize(expected)


def test_group_anagrams_does_not_mutate_input():
    strs = ["eat", "tea", "tan"]
    group_anagrams(strs)
    assert strs == ["eat", "tea", "tan"]


def test_group_anagrams_covers_all_words():
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    groups = group_anagrams(strs)
    flat = sorted([word for group in groups for word in group])
    assert flat == sorted(strs)
    assert len(groups) == 3
