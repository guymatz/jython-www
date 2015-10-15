import sys,os,re
from javax.servlet.http import HttpServlet
from java.io import File
#sys.add_package("jxl")
sys.add_package("org.apache.commons.fileupload")
#sys.add_package("org.apache.commons.fileupload.disk")
#sys.add_package("org.apache.commons.fileupload.servlet")
#os.path.append("/usr/share/java/jxl-2.6.12.jar")
from jxl import Workbook
from org.apache.commons.fileupload import *
from org.apache.commons.fileupload.disk import DiskFileItemFactory
from org.apache.commons.fileupload.servlet import ServletFileUpload
from JythonServletUtils import *

class upload (HttpServlet):
  UPLOAD_DIRECTORY="/tmp/uploads"
  def doGet(self,request,response):
    self.doPost (request,response)

  def doPost(self,request,response):
      print("request = %s" % request)
      print("__name__ = %s" % __name__)
      request.setAttribute("message", 'hello')
      request.setAttribute("env", os.environ)
      dispatcher = request.getRequestDispatcher('result.jsp')
      dispatcher.forward(request, response)
#      factory = DiskFileItemFactory()
#      upload = ServletFileUpload(factory)
#      print("dir(upload) = %s" % dir(upload))
#      items = upload.parseRequest(request)
#      if ServletFileUpload.isMultipartContent(request):
#              print("yes")
#
#
#
#if __name__ == "__main__":
#	J = upload()
#	dummyRequest = DummyHttpRequest()
#	dummyResponse = DummyHttpResponse()
#
#	J.doPost (dummyRequest,dummyResponse)
