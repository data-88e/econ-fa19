test = {
	"name": "q2_5",
	"points": 1,
	"suites": [ 
		{
			"cases": [ 
				{
					"code": r"""
					>>> np.isclose(find_k(0,0), 2)
					True
					""",
					"hidden": False,
					"locked": False,
				}, 
				{
					"code": r"""
					>>> type(k_hat) in [float, np.float64]
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