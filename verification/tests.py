"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": ['VI'],
            "answer": 6
        },
        {
            "input": ['LXXVI'],
            "answer": 76
        },
        {
            "input": ['CDXCIX'],
            "answer": 499
        },
        {
            "input": ['MMMDCCCLXXXVIII'],
            "answer": 3888
        }
    ],
    "Extra": [
        {
            "input": ['I'],
            "answer": 1
        },
        {
            "input": ['II'],
            "answer": 2
        }
    ]
}
