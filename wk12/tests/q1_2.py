test = {
	"name": "q1_2",
	"points": 1,
	"suites": [ 
		{
			"cases": [ 
				{
					"code": r"""
					>>> np.random.seed(1234)
					>>> x = np.random.uniform(0, 10, 5)
					>>> y = np.random.uniform(0, 10, 5)
					>>> np.isclose(slope(x, y), 0.853965497371089)
					True
					""",
					"hidden": False,
					"locked": False,
				}, {
					"code": r"""
					>>> np.random.seed(1234)
					>>> x = np.random.uniform(0, 10, 5)
					>>> y = np.random.uniform(0, 10, 5)
					>>> np.isclose(intercept(x, y), 1.5592892975597108)
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