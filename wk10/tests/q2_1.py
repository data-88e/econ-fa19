test = {
	"name": "q2_1",
	"points": 1,
	"suites": [ 
		{
			"cases": [ 
				{
					"code": r"""
					>>> len(cum_income_share)
					5
					""",
					"hidden": False,
					"locked": False,
				}, 
				{
					"code": r"""
					>>> for i in range(4):
					...     assert cum_income_share[i] < cum_income_share[i+1], "cum_income_share must be increasing"
					""",
					"hidden": False,
					"locked": False,
				}, 
			],
			"scored": False,
			"setup": "",
			"teardown": "",
			"type": "doctest"
		}, 
	]
}