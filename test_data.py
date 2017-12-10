import textwrap

day1 = (
	[
		("1122", 3),
		("1111", 4),
		("1234", 0),
		("91212129", 9)
	],
	[
    	("1212", 6),
    	("1221", 0),
    	("123425", 4),
    	("123123", 12),
    	("12131415", 4)
	]
)

day2 = (
	[
		(textwrap.dedent("""\
		5 1 9 5
		7 5 3
		2 4 6 8"""), 18)
	],
	[
		(textwrap.dedent("""\
		5 9 2 8
		9 4 7 3
		3 8 6 5"""), 9)
	]
)

day3 = (
	[
		(1, 0),
		(12, 3),
		(23, 2),
		(1024, 31)
	],
	[]
)

day4 = (
	[
		("aa bb cc dd ee", 1),
		("aa bb cc dd aa", 0),
		("aa bb cc dd aaa", 1)
	],
	[
		("abcde fghij", 1),
		("abcde xyz ecdab", 0),
		("a ab abc abd abf abj", 1),
		("iiii oiii ooii oooi oooo", 1),
		("oiii ioii iioi iiio", 0)
	]
)

day8 = (
	[
		(textwrap.dedent("""\
		b inc 5 if a > 1
		a inc 1 if b < 5
		c dec -10 if a >= 1
		c inc -20 if c == 10"""), 1)
	],
	[
		(textwrap.dedent("""\
		b inc 5 if a > 1
		a inc 1 if b < 5
		c dec -10 if a >= 1
		c inc -20 if c == 10"""), 10)
	]
)