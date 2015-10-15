import sys,os,re
from java.io import *
from javax.servlet.http import HttpServlet
from JythonServletUtils import *

class JythonServlet2 (HttpServlet):
  def doGet(self,request,response):
    self.doPost (request,response)

  def doPost(self,request,response):
    toClient = response.getWriter()
    response.setContentType ("text/html")
    toClient.println ("<html><head><title>Servlet Test</title>")
    toClient.println("<body><h1>Servlet Test</h1></body></html>")

if __name__ == "__main__":
  JS2 = JythonServlet2()
  dummyRequest = DummyHttpRequest()
  dummyResponse = DummyHttpResponse()

  JS2.doPost (dummyRequest,dummyResponse)
