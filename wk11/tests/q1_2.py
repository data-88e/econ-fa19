test = {
	"name": "q1_2",
	"points": 1,
	"suites": [ 
		{
			"cases": [ 
				{
					"code": r"""
					>>> "ethrace" in mariel.labels
					True
					""",
					"hidden": False,
					"locked": False,
				}, 
				{
					"code": r"""
					>>> np.unique(mariel["ethrace"])
					array(['blacks', 'cubans', 'hispanics', 'whites'], dtype='<U9')
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