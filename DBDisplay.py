import sys,os
from javax.servlet.http import HttpServlet
#sys.add_package("java.sql.DriverManager")
#sys.add_package("java.sql.DriverManager.getConnection")
#sys.add_package("org.sql.sqlite.JDBC")
from java.sql import *
from java.sql import DriverManager
from org.sqlite.JDBC import *
from JythonServletUtils import *

class DBDisplay(HttpServlet):
  def __init__(self):

    #define the JDBC url
    db_file = '/var/lib/tomcat7/webapps/jythondemo/products.db'
    url = "jdbc:sqlite:%s" % db_file

    #connect to the database and get cursor object
    try:
        self.c = DriverManager.getConnection(url)
    except Exception, e:
        print("Could not find %s in %s" % (db_file, os.cwd))

  def doGet(self, req, res):
    print("dir() = %s" % dir())
    #print("dir(self.servletContext) = %s" % dir(self.servletContext))

    res.setContentType("text/html")
    out = res.getWriter()

    out.println('''
      <html>
      <head>
       <title>Jylet Database Connection</title>
      </head>
      <body>
      <table align="center">
       <tr>
        <td><b>ID</b></td>
        <td><b>Title</b></td>
        <td><b>Description</b></td>
        <td><b>Price</b></td>
       </tr>
       ''')

    self.statement = self.c.createStatement();  
    self.resultSet = self.statement.executeQuery("select code, name, description, price from products")
    while self.resultSet.next():
      row = []
      for col in range(1, self.resultSet.getColumnCount()+1):
        name = self.resultSet.getColumnName(col)
        row.append(self.resultSet.getString(name))
      out.println('''
          <tr>
           <td>%s</td>
           <td>%s</td>
           <td>%s</td>
           <td>%s</td>''' % tuple(row)
           )
  
    out.println('''
      </table>
      </body>
      </html>
      ''')

  def destroy(self):
    self.c.close()
    self.db.close()


if __name__ == "__main__":
      DBD = DBDisplay()
      dummyRequest = DummyHttpRequest()
      dummyResponse = DummyHttpResponse()

      DBD.doGet (dummyRequest,dummyResponse)
