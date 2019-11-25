test = {
	"name": "q2_5",
	"points": 1,
	"suites": [ 
		{
			"cases": [ 
				{
					"code": r"""
					>>> len(new_features) == 6
					True
					""",
					"hidden": False,
					"locked": False,
				}, 
				{
					"code": r"""
					>>> new_X.shape[1] == 6
					True
					""",
					"hidden": False,
					"locked": False,
				}, 
				{
					"code": r"""
					>>> len(new_Y_hat) == defaults.num_rows
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