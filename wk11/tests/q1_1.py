test = {
	"name": "q1_1",
	"points": 1,
	"suites": [ 
		{
			"cases": [ 
				{
					"code": r"""
					>>> ".id" in mariel.labels
					False
					""",
					"hidden": False,
					"locked": False,
				}, 
				{
					"code": r"""
					>>> "year" in mariel.labels
					True
					""",
					"hidden": False,
					"locked": False,
				}, 
				{
					"code": r"""
					>>> np.unique(mariel["year"])
					array([1979, 1980, 1981, 1982, 1983, 1984, 1985])
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