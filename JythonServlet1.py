import sys,os,re
from javax.servlet.http import HttpServlet
from java.io import File
sys.add_package("jxl")
#os.path.append("/usr/share/java/jxl-2.6.12.jar")
from jxl import Workbook
import calendar

class JythonServlet1 (HttpServlet):
  def doGet(self,request,response):
    self.doPost (request,response)

  def doPost(self,request,response):
    toClient = response.getWriter()
    response.setContentType ("text/html")
    toClient.println ("<html><head><title>Servlet Test</title>")
    toClient.println("<body><h1>Servlet Test</h1></body></html>")
    toClient.println("<P>request.getContextPath(): %s</P>" % request.getContextPath())
    toClient.println("<P>dir(request): %s</P>" % dir(request) )
    toClient.println("<P>sys.path: %s</P>" % sys.path)
    toClient.println("<P>dir(sys): %s</P>" % dir(sys) )
    toClient.println("<P>dir(os): %s</P>" % dir(os) )
    f = File('webapps/jythondemo/w.xlsx')
    w = Workbook.createWorkbook(f)
    toClient.println("<P>dir(f): %s</P>" % dir(f) )
    toClient.println("<P>f.getAbsolutePath(): %s</P>" % f.getAbsolutePath() )
    toClient.println("<P>dir(w): %s</P>" % dir(w) )
    toClient.println("<P>dir(): %s</P>" % dir() )
    toClient.println("<P>dir(__builtins__): %s</P>" % dir(__builtins__) )
    toClient.println("<P>sys.builtin_module_names: %s</P>" % str(sys.builtin_module_names) )
    toClient.println("<P>sys.argv: %s</P>" % str(sys.argv) )
    toClient.println ("<table>")
    for k in sorted(os.environ.keys()):
        toClient.println ("<tr>")
        toClient.println("<td>%s</td><td>%s</td>" % (k, os.environ[k]))
        toClient.println ("</tr>")
    toClient.println ("<table>")
    for e in sorted(dir(sys)):
        element = getattr(sys, e)
        toClient.println ("<tr>")
        toClient.println("<td>%s</td><td>%s</td><td>%s</td>" % (e, str(type(element))[1:-1], element.__doc__))
        toClient.println ("</tr>")
    toClient.println ("</table>")

    #cal = calendar.calendar(2019)
    #cal = re.sub(' 27 ','*27*', cal)
    #toClient.println("<pre>")
    #toClient.println(cal)
    #toClient.println("</pre>")
