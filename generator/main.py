import pyodbc
import ConfigParser

config = ConfigParser.RawConfigParser()
config.read('../resources/env.properties')
list = []
login = 'myFancyLogin'

def addTestData(db, schema, Name, LastName, Level, Area, Salary, Grade):
    try:
        dbAddress = "Driver={SQL Server};Server=localhost\SQLEXPRESS;Database="+db+";Trusted_Connection=yes;uid="+login+";pwd="
        cnx = pyodbc.connect(dbAddress)
        cursor = cnx.cursor()

        id = "SELECT top 1 ID FROM ["+schema+"].[candidates] ORDER BY ID DESC"
        id = returnValue(cnx, cursor, id)
        Id = str(id + 1)

        schema = str(schema)

        testQuery = 'SELECT DB_NAME() AS [Current Database];'
        candidates = "INSERT INTO ["+schema+"].[candidates] VALUES("+Id+",'"+Name+"','"+LastName+"','"+Level+"','"+Area+"',"+Salary+","+Grade+")"
        returnDBName(cnx, cursor, testQuery)

        list = [candidates]
        executeQuery(cnx, cursor, list)

    except pyodbc.Error as e:
        print(e)
        print 'errors in addTestData function'
    else:
        cnx.close()


def deleteTestData(db, schema):
    try:
        dbAddress = "Driver={SQL Server};Server=localhost\SQLEXPRESS;Database="+db+";Trusted_Connection=yes;uid="+login+";pwd="
        cnx = pyodbc.connect(dbAddress)
        cursor = cnx.cursor()

        schema = str(schema)

        testQuery = 'SELECT DB_NAME() AS [Current Database];'
        candidates = "DELETE FROM ["+schema+"].[candidates]"
        candidatesProcessed = "DELETE FROM ["+schema+"].[candidatesProcessed]"

        returnDBName(cnx, cursor, testQuery)

        list = [candidates, candidatesProcessed]
        executeQuery(cnx, cursor, list)

    except:
        print 'errors in deleteTestData function'
    else:
        cnx.close()

def createStructure(db):
    try:
        dbAddress = "Driver={SQL Server};Server=localhost\SQLEXPRESS;Database="+db+";Trusted_Connection=yes;uid="+login+";pwd="
        cnx = pyodbc.connect(dbAddress)
        cursor = cnx.cursor()

        testQuery = 'SELECT DB_NAME() AS [Current Database];'

        dropCandidates = 'IF EXISTS (SELECT schema_name FROM information_schema.schemata WHERE schema_name = \'Test\' ) BEGIN EXEC sp_executesql N\'DROP TABLE [Test].[candidates]\' END'
        dropCandidatesProcessed = 'IF EXISTS (SELECT schema_name FROM information_schema.schemata WHERE schema_name = \'Test\' ) BEGIN EXEC sp_executesql N\'DROP TABLE [Test].[candidatesProcessed]\' END'

        createSchema = 'IF NOT EXISTS (SELECT schema_name FROM information_schema.schemata WHERE schema_name = \'Test\' ) BEGIN EXEC sp_executesql N\'CREATE SCHEMA [Test]\' END'
        candidates = 'SELECT  * INTO [Test].[Candidates] FROM  [dbo].[Candidates]'
        candidatesProcessed = 'SELECT  * INTO [Test].[CandidatesProcessed] FROM  [dbo].[CandidatesProcessed]'

        returnDBName(cnx, cursor, testQuery)

        list = [dropCandidates, dropCandidatesProcessed]
        executeQuery(cnx, cursor, list)

        list = [createSchema, candidates, candidatesProcessed]
        executeQuery(cnx, cursor, list)

    except:
        print 'errors in createStructure function'
    else:
        cnx.close()
#-----------------------------------------------------------------------------------------------------------------------
def executeQuery(cnx, cursor, list):
    for i in list:
        cursor.execute(i)
        cnx.commit()

def returnDBName(cnx, cursor, dbQuery):
    cursor.execute(dbQuery)
    Value = cursor.fetchone()
    Value = Value[0]
    Value = str(Value)
    print Value


def returnValue(cnx, cursor, list):
    cursor.execute(list)
    Value = cursor.fetchone()
    if(Value is None):
        value = 0
    else:
        value = Value[0]
    return value

