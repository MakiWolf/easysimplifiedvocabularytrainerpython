import sqlite3

def test(txt, r1, r2, mistake, vocabulary_id):
  global erg #result
  global upperlowercase
  if(str(r1.lower()) == str(txt.lower())) :
    if(str(r1) == str(txt)) :
      print("Right! " + str(r1) + " = " + str(r2))
      erg = erg + 1
      if(mistake > 0) :
        mistake = mistake - 1
        sql_command = "UPDATE vocabulary SET mistakes = %i WHERE ID= %i " % (mistake, vocabulary_id)
        c.execute(sql_command)
        conn.commit()
    else :
     print(txt + " upper und lowercase mistake! correct is: " + str(r1) + " = " + str(r2))
     mistake = mistake + 1
     sql_command = "UPDATE vocabulary SET mistakes = %i WHERE ID=%i" % (mistake, vocabulary_id)
     c.execute(sql_command)
     conn.commit()
     upperlowercase = upperlowercase + 1
  else :
    print(txt + " is not correct! Right is: " + str(r1) + " = " + str(r2))
    mistake = mistake + 5
    sql_command = "UPDATE vocabulary SET mistakes = %i WHERE ID=%i" % (mistake, vocabulary_id)
    c.execute(sql_command)
    conn.commit()

conn = sqlite3.connect('vocabulary.db')
c = conn.cursor()
mistake = 10
print("Please enter 1 (language1 - languege2) or 2 (language2 - languege1) ")
choice = input()
print("Begin ID: ")
beginid = int(input())
print("End ID: ")
endid = int(input())
print("only where mistakes enter 1: ")
mistakes_round = input()
erg = 0
upperlowercase = 0
if mistakes_round == "1" :
  sql_command = "SELECT * FROM vocabulary WHERE mistakes > 1 AND ID BETWEEN %i AND %i" % (beginid, endid)
  c.execute(sql_command)
  result = c.fetchall()
  lenfalsch = int(len(result))
  for r in result:
    #print(r)
    if choice == "1" :
      print(str(r[1]))
      vocabulary_id = int(r[0])
      r2 = r[1]
      r1 = str(r[2])
      mistake = int(r[3])
    else :
      print(str(r[2]))
      vocabulary_id = int(r[0])
      r2 = r[2]
      r1 = str(r[1])
      mistake = int(r[3])
    txt = input()
    test(txt, r1, r2, mistake, vocabulary_id)
  if(lenfalsch > 0) :
    print("result: " + str(erg) + "/" + str(len(result)) + " and " + str(upperlowercase) + " uppercase und lowercase mistakes")
  else :
    print("no vocabulary found!")
else :
  sql_command = "SELECT * FROM vocabulary WHERE ID BETWEEN %i AND %i" % (beginid, endid)
  c.execute(sql_command)
  result = c.fetchall()
  for r in result:
    #print(r)
    if choice == "1" :
      print(str(r[1]))
      vocabulary_id = int(r[0])
      r2 = r[1]
      r1 = str(r[2])
      mistake = r[3]
    else :
      print(str(r[2]))
      vocabulary_id = int(r[0])
      r2 = r[2]
      r1 = str(r[1])
      mistake = r[3]
    txt = input()
    test(txt, r1, r2, mistake, vocabulary_id)
  print("result: " + str(erg) + "/" + str(len(result)) + " and " + str(upperlowercase) + " uppercase und lowercase mistakes")

conn.close()
input()