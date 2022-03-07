
### Homework

```SQL
sql_query_string = """
SELECT s.First, s.Last, s.studentID, s.grade, scanTime, status, date, courseSection, attendance, period,teacher
FROM Scan AS s
INNER JOIN periodAtt AS p
ON s.studentID=p.studentID AND substr(s.scanTime, 1, 9)=p.date
WHERE Attendance = 'A'
ORDER BY s.last ASC
"""

#Exectue the SQL query
result_df = sql_query_to_pd(sql_query_string, db_name='default.db')
result_df
```

### ASYNC

**SQL CHallenge 2**

```SQL
sql_query_string = """

SELECT * FROM (SELECT s.First, s.Last, s.studentID, s.grade, scanTime, status, date, courseSection, attendance, period,teacher
FROM Scan AS s
INNER JOIN periodAtt AS p
ON s.studentID=p.studentID AND substr(s.scanTime, 1, 9)=p.date
WHERE Attendance = 'A') AS allCuts
LEFT JOIN bio AS b
ON allCuts.First=b.First AND allCuts.Last=b.Last AND allCuts.studentID=b.studentID
ORDER BY allCuts.teacher ASC


"""

#Exectue the SQL query
result_df = sql_query_to_pd(sql_query_string, db_name='default.db')
result_df
```
