test = {
	"name": "q1_1",
	"points": 1,
	"suites": [ 
		{
			"cases": [ 
				{
					"code": r"""
					>>> np.random.seed(1234)
					>>> x = np.random.uniform(0, 10, 5)
					>>> su_x = np.array([-1.65063375,  0.26090383, -0.55762848,  0.98562722,  0.96173118])
					>>> np.allclose(su_x, su(x))
					True
					""",
					"hidden": False,
					"locked": False,
				}, {
					"code": r"""
					>>> np.random.seed(1234)
					>>> x = np.random.uniform(0, 10, 5)
					>>> y = np.random.uniform(0, 10, 5)
					>>> np.isclose(corr(x, y), 0.6410799722591175)
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