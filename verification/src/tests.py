"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": '12.04.2018',
            "answer": 1
        },
        {
            "input": '01.01.1999',
            "answer": 0
        }
    ],
    "Extra": [
        {
            "input": '20.11.1990',
            "answer": 3
        },
        {
            "input": '11.11.1111',
            "answer": 6
        },
        {
            "input": '09.07.0168',
            "answer": 6
        },
        {
            "input": '12.12.2112',
            "answer": 4
        },
        {
            "input": '31.12.2999',
            "answer": 3
        },
        {
            "input": '01.01.3000',
            "answer": 2
        }
    ]
}
