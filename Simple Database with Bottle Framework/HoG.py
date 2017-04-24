import sqlite3
from bottle import route, run, template,request

@route('/insert/player', method="GET")
@route('/insert/player', method="POST")

def insert():
    con = sqlite3.connect("nba.db")

    pid=request.forms.get('pid')
    fname=request.forms.get('fname')
    lname=request.forms.get('lname')
    dob=request.forms.get('dob')
    height=request.forms.get('height')
    weight=request.forms.get('weight')
    tid=request.forms.get('tid')
    query=request.forms.get('query')
    cur = con.cursor()
    if(query):
        cur.execute("select fname,lname from player where t_id=(select t_id from team where teamname='Los Angeles Lakers') and p_id in(select p_id from position where p_name='SG' or p_name='PG');") #Enter Query here
        data = cur.fetchall()
        output = template('Query',rows=data)
    else:
        cur.execute("INSERT into player values(?,?,?,?,?,?,?)", (pid,fname,lname,dob,height,weight,tid))
        output = template('InsertionPlayer')
    con.commit()
    con.close()
    return output
@route('/insert/team', method="GET")
@route('/insert/team', method="POST")

def insert():
    con = sqlite3.connect("nba.db")

    teamname=request.forms.get('teamname')
    homecourt=request.forms.get('homecourt')
    tid=request.forms.get('tid')
    query=request.forms.get('query')
    cur = con.cursor()
    if(query):
        cur.execute("select * from player") #Enter Query here
        data = cur.fetchall()
        output = template('Query',rows=data)
    else:
        cur.execute("INSERT into team values(?,?,?)", (teamname,homecourt,tid))
        output = template('InsertionTeam')
    con.commit()
    con.close()
    return output
@route('/insert/contract', method="GET")
@route('/insert/contract', method="POST")

def insert():
    con = sqlite3.connect("nba.db")

    pid=request.forms.get('pid')
    year=request.forms.get('year')
    amount=request.forms.get('amount')
    query=request.forms.get('query')
    cur = con.cursor()
    if(query):
        cur.execute("select * from player") #Enter Query here
        data = cur.fetchall()
        output = template('Query',rows=data)
    else:
        cur.execute("INSERT into contract values(?,?,?)", (year,amount,pid))
        output = template('InsertionContract')
    con.commit()
    con.close()
    return output
@route('/insert/sponsor', method="GET")
@route('/insert/sponsor', method="POST")

def insert():
    con = sqlite3.connect("nba.db")

    name=request.forms.get('name')
    media=request.forms.get('media')
    shoe=request.forms.get('shoe')
    jersey=request.forms.get('jersey')
    equipment=request.forms.get('equipment')
    tid=request.forms.get('tid')
    query=request.forms.get('query')
    cur = con.cursor()
    if(query):
        cur.execute("select * from player") #Enter Query here
        data = cur.fetchall()
        output = template('Query',rows=data)
    else:
        cur.execute("INSERT into sponsor values(?,?,?,?,?,?)", (name,media,shoe,jersey,equipment,tid))
        output = template('InsertionSponsor')
    con.commit()
    con.close()
    return output
@route('/insert/hof', method="GET")
@route('/insert/hof', method="POST")

def insert():
    con = sqlite3.connect("nba.db")

    year=request.forms.get('year')
    votes=request.forms.get('votes')
    group=request.forms.get('group')
    pid=request.forms.get('pid')
    query=request.forms.get('query')
    cur = con.cursor()
    if(query):
        cur.execute("select * from player") #Enter Query here
        data = cur.fetchall()
        output = template('Query',rows=data)
    else:
        cur.execute("INSERT into hall_of_fame values(?,?,?,?)", (year,votes,group,pid))
        output = template('InsertionHoF')
    con.commit()
    con.close()
    return output
@route('/insert/star', method="GET")
@route('/insert/star', method="POST")

def insert():
    con = sqlite3.connect("nba.db")

    year=request.forms.get('year')
    team=request.forms.get('team')
    winner=request.forms.get('winner')
    query=request.forms.get('query')
    cur = con.cursor()
    if(query):
        cur.execute("select * from player") #Enter Query here
        data = cur.fetchall()
        output = template('Query',rows=data)
    else:
        cur.execute("INSERT into all_star_team values(?,?,?)", (year,team,winner))
        output = template('InsertionStar')
    con.commit()
    con.close()
    return output
@route('/insert/games', method="GET")
@route('/insert/games', method="POST")

def insert():
    con = sqlite3.connect("nba.db")

    gid=request.forms.get('gid')
    gdate=request.forms.get('gdate')
    location=request.forms.get('location')
    query=request.forms.get('query')
    cur = con.cursor()
    if(query):
        cur.execute("select * from player") #Enter Query here
        data = cur.fetchall()
        output = template('Query',rows=data)
    else:
        cur.execute("INSERT into games values(?,?,?)", (gid,gdate,location))
        output = template('InsertionGames')
    con.commit()
    con.close()
    return output
@route('/insert/performances', method="GET")
@route('/insert/performances', method="POST")

def insert():
    con = sqlite3.connect("nba.db")

    pid=request.forms.get('pid')
    gid=request.forms.get('gid')
    twos=request.forms.get('twos')
    threes=request.forms.get('threes')
    fgp=request.forms.get('fgp')
    turnovers=request.forms.get('turnovers')
    fouls=request.forms.get('fouls')
    query=request.forms.get('query')
    cur = con.cursor()
    if(query):
        cur.execute("select * from player") #Enter Query here
        data = cur.fetchall()
        output = template('Query',rows=data)
    else:
        cur.execute("INSERT into performances values(?,?,?,?,?,?,?)", (pid,gid,twos,threes,fgp,turnovers,fouls))
        output = template('InsertionPerformances')
    con.commit()
    con.close()
    return output


@route('/display')
def display():
    db = sqlite3.connect('nba.db')
    c = db.cursor()
    c.execute("SELECT p_id,fname,lname,DOB,height,weight,t_id FROM player")	#Insert what you want to display and change it in Display.tpl file
    data = c.fetchall()
    c.close()
    output = template('Display', rows=data)
    return output

from bottle import static_file

@route('/static/larry')
def server():
    return static_file(filename, root='/Users/Reddy/pyprojects/larry.jpg')
run(host='0.0.0.0', port=1033)
