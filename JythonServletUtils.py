from java.lang import System
import javax

class DummyHttpRequest(javax.servlet.http.HttpServletRequest):
	pass

class DummyHttpResponse(javax.servlet.http.HttpServletResponse):
	def setContentType(self,t):
		System.out.println ("Content-Type:%s" % t)
		
 	def getWriter (self):
 		return System.out
