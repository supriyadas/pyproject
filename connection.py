class DBConnection:
	def getDbConnction():  
		db = pymysql.connect("127.0.0.1","root","","test" )
		return db