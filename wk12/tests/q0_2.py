test = {
	"name": "q0_2",
	"points": 1,
	"suites": [ 
		{
			"cases": [ 
				{
					"code": r"""
					>>> "sex" in defaults.labels
					False
					""",
					"hidden": False,
					"locked": False,
				}, 
				{
					"code": r"""
					>>> "education" in defaults.labels
					False
					""",
					"hidden": False,
					"locked": False,
				}, 
				{
					"code": r"""
					>>> "marital_status" in defaults.labels
					False
					""",
					"hidden": False,
					"locked": False,
				}, 
				{
					"code": r"""
					>>> "sex_male" in defaults.labels
					True
					""",
					"hidden": False,
					"locked": False,
				}, 
				{
					"code": r"""
					>>> "sex_female" in defaults.labels
					True
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