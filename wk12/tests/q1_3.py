test = {
	"name": "q1_3",
	"points": 1,
	"suites": [ 
		{
			"cases": [ 
				{
					"code": r"""
					>>> np.random.seed(1234)
					>>> y = np.random.uniform(0, 10, 5)
					>>> y_hat = np.random.uniform(0, 10, 5)
					>>> np.isclose(rmse(y, y_hat), 2.440102731334708)
					True
					""",
					"hidden": False,
					"locked": False,
				}
			],
			"scored": False,
			"setup": "",
			"teardown": "",
			"type": "doctest"
		}, 
	]
}