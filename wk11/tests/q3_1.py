test = {
	"name": "q3_1",
	"points": 1,
	"suites": [ 
		{
			"cases": [ 
				{
					"code": r"""
					>>> np.unique(not_miami_wages.labels)
					array(['blacks', 'cubans', 'hispanics', 'whites', 'year'], dtype='<U9')
					""",
					"hidden": False,
					"locked": False,
				}, 
				{
					"code": r"""
					>>> not_miami_wages["year"]
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