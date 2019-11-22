import psycopg2 as dbapi
import os

url = os.getenv("url")

class FootballStats:

	def Team_add(self, TeamName, NickName, ShortName, FoundationDate, Capacity, ManagerID):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """ INSERT INTO Teams(TeamName, NickName, ShortName, FoundationDate, Capacity, ManagerID) VALUES(%s,%s,%s,%s,%s,%s);"""
				cursor.execute(statement,([TeamName, NickName, ShortName, FoundationDate, Capacity, ManagerID]))

	def Team_update(self, TeamID, TeamName, NickName, ShortName, FoundationDate, Capacity, ManagerID):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement="""Update Teams Set Teamname=%s, NickName=%s, ShortName=%s, FoundationDate=%s, Capacity=%s, ManagerID=%s  Where ID=%s;"""
				cursor.execute(statement,([TeamName, NickName, ShortName, FoundationDate, Capacity, ManagerID, TeamID]))
	
	def Team_delete(self, TeamID):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """ DELETE FROM Teams WHERE ID = %s;"""
				cursor.execute(statement,[TeamID])		
	
	def Stadium_add(self, TeamId, StadiumName, Capacity, Built, PitchSize, Surface):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """ INSERT INTO Stadium(Team_ID,Stadiumname,Capacity,Built,PitchSize,Surface) VALUES(%s,%s,%s,%s,%s,%s);"""
				cursor.execute(statement,([TeamId, StadiumName, Capacity, Built, PitchSize, Surface]))
	
	def Stadium_delete(self,StadiumId):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement="""Delete From Stadium Where ID = %s;"""
				cursor.execute(statement,([StadiumId]))

	def Stadium_update(self, StadiumId, TeamId, StadiumName, Capacity, Built, PitchSize, Surface):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement="""Update Stadium Set Team_ID=%s, Stadiumname=%s, Capacity=%s, Built=%s, PitchSize=%s, Surface=%s Where ID=%s;"""
				cursor.execute(statement,([TeamId, StadiumName, Capacity, Built, PitchSize, Surface, StadiumId]))
	def Stadium_update_info(self, ID):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """ Select * From Stadium where ID = %s;"""
				cursor.execute(statement,([ID]))
				cursor_list=cursor.fetchall()
				return cursor_list

	def Stadium(self):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """Select * FROM Stadium ORDER BY Stadiumname"""
				cursor.execute(statement)
				cursor_list=cursor.fetchall()
				return cursor_list
			
	def Assist_add(self, PlayerId, MatchId, Minute, LastTouch, Format, GoldenAssist, StadiumHA):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """ INSERT INTO Assist(PlayerId,MatchId,Minute,LastTouch,Format,GoldenAssist,StadiumHA) VALUES(%s,%s,%s,%s,%s,%s,%s);"""
				cursor.execute(statement,([PlayerId, MatchId,Minute,LastTouch,Format,GoldenAssist,StadiumHA]))

	def Assist_delete(self, AssistId):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement="""Delete From Assist Where ID = %s; """
				cursor.execute(statement,([AssistId]))

	def Assist_update(self, AssistId, PlayerId, MatchId, Minute, LastTouch, Format, GoldenAssist, StadiumHA):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement="""Update Assist Set PlayerID=%s, MatchID=%s, Minute=%s, LastTouch=%s, Format=%s,GoldenAssist=%s,StadiumHA=%s Where ID=%s;"""
				cursor.execute(statement,([PlayerId, MatchId, Minute, LastTouch, Format, GoldenAssist, StadiumHA, AssistId]))
	def Assist_update_info(self, ID):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """ Select * From Assist where ID = %s;"""
				cursor.execute(statement,([ID]))
				cursor_list=cursor.fetchall()
				return cursor_list

	def Admins_add(self, UserName, UserPassword):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """ INSERT INTO ADMINS(UserName,UserPassword) VALUES(%s,%s);"""
				cursor.execute(statement,([UserName, UserPassword]))
	
	def Goal_add(self, PlayerId, MatchId, Minute):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """ INSERT INTO Goal(PlayerId, MatchId, Minute) VALUES(%s,%s,%s);"""
				cursor.execute(statement,([PlayerId, MatchId,Minute]))
	
	def Goal_update(self, GoalID, PlayerId, MatchId, Minute):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement="""Update Goal Set PlayerId=%s, MatchId=%s, Minute=%s Where ID=%s;"""
				cursor.execute(statement,([PlayerId, MatchId, Minute, GoalID]))
	
	def Goal_delete(self, GoalID):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """ DELETE FROM Goal WHERE ID = %s;"""
				cursor.execute(statement,[GoalID])	
	
	def Statistic_add(self, MatchID, HScore, HPossesion, HCorner, HInjure, HFoul, HOffside, HShot, HShotOnTarget, HShotAccuracy, HPassAccuracy, AScore, APossesion, ACorner, AInjure, AFoul, AOffside, AShot, AShotOnTarget, AShotAccuracy, APassAccuracy, Referee_UserName):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """ INSERT INTO Statistic(MatchID, HScore, HPossesion, HCorner, HInjure, HFoul, HOffside, HShot, HShotOnTarget, HShotAccuracy, HPassAccuracy, AScore, APossesion, ACorner, AInjure, AFoul, AOffside, AShot, AShotOnTarget, AShotAccuracy, APassAccuracy, Referee_UserName) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"""
				cursor.execute(statement,([MatchID, HScore, HPossesion, HCorner, HInjure, HFoul, HOffside, HShot, HShotOnTarget, HShotAccuracy, HPassAccuracy, AScore, APossesion, ACorner, AInjure, AFoul, AOffside, AShot, AShotOnTarget, AShotAccuracy, APassAccuracy, Referee_UserName]))

	def Statistic_delete(self, StatisticId):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement="""Delete From Statistic Where ID = %s; """
				cursor.execute(statement,([StatisticId]))

	def Statistic_Update(self, StatisticId, MatchID, HScore, HPossesion, HCorner, HInjure, HFoul, HOffside, HShot, HShotOnTarget, HShotAccuracy, HPassAccuracy, AScore, APossesion, ACorner, AInjure, AFoul, AOffside, AShot, AShotOnTarget, AShotAccuracy, APassAccuracy, Referee_UserName):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement="""Update Statistic Set MatchID=%s, HScore=%s, HPossesion=%s, HCorner=%s, HInjure=%s, HFoul=%s, HOffside=%s, HShot=%s, HShotOnTarget=%s, HShotAccuracy=%s, HPassAccuracy=%s, AScore=%s, APossesion=%s, ACorner=%s, AInjure=%s, AFoul=%s, AOffside=%s, AShot=%s, AShotOnTarget=%s, AShotAccuracy=%s, APassAccuracy=%s, Referee_UserName=%s Where ID=%s;"""
				cursor.execute(statement,([MatchID, HScore, HPossesion, HCorner, HInjure, HFoul, HOffside, HShot, HShotOnTarget, HShotAccuracy, HPassAccuracy, AScore, APossesion, ACorner, AInjure, AFoul, AOffside, AShot, AShotOnTarget, AShotAccuracy, APassAccuracy, Referee_UserName,StatisticId]))

	def Player_add(self, PlayerName, PlayerAge, Position, PlayerNationalty, PlayerHeight, PlaceOfBirth, TeamID):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """
                                INSERT INTO Player(PlayerName, PlayerAge, Position, PlayerNationalty, PlayerHeight, PlaceOfBirth, TeamID) VALUES(%s,%s,%s,%s,%s,%s,%s);"""
				cursor.execute(statement,([PlayerName, PlayerAge, Position, PlayerNationalty, PlayerHeight, PlaceOfBirth, TeamID]))
	
	def Player_delete(self, PlayerID):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """ DELETE FROM Player WHERE ID = %s;"""
				cursor.execute(statement,[PlayerID])

	def Player_update(self, PlayerID, PlayerName, PlayerAge, Position, PlayerNationalty, PlayerHeight, PlaceOfBirth, TeamID):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement="""Update Player Set PlayerName=%s, PlayerAge=%s, Position=%s, PlayerNationalty=%s, PlayerHeight=%s, PlaceOfBirth=%s, TeamID=%s Where ID=%s;"""
				cursor.execute(statement,([PlayerName, PlayerAge, Position, PlayerNationalty, PlayerHeight, PlaceOfBirth, TeamID, PlayerID]))
	
	def Manager_add(self, Name, Age, Nationalty, Height, PlaceOfBirth):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """INSERT INTO Manager(Name, Age, Nationalty, Height, PlaceOfBirth) VALUES(%s,%s,%s,%s,%s);"""
				cursor.execute(statement,([Name, Age, Nationalty, Height, PlaceOfBirth]))			
	
	def Manager_update(self, ManagerID, Name, Age, Nationalty, Height, PlaceOfBirth):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement="""Update Manager Set Name=%s, Age=%s, Nationalty=%s, Height=%s, PlaceOfBirth=%s Where ID=%s;"""
				cursor.execute(statement,([Name, Age, Nationalty, Height, PlaceOfBirth, ManagerID]))
	
	def Manager_delete(self, ManagerID):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """ DELETE FROM Manager WHERE ID = %s;"""
				cursor.execute(statement,[ManagerID])	
	
	def Team(self):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """Select * FROM Teams ORDER BY Teamname"""
				cursor.execute(statement)
				cursor_list=cursor.fetchall()
				#cursor_tuple=()
				#cursor_list=list(cursor_tuple)
				#for id,Teamname in cursor:
					#cursor_list.append(Teamname)
					#print('%(tt)s: %(nm)s' % {'tt': id, 'nm': Teamname})
				return cursor_list

	def Player(self):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """Select * FROM Player ORDER BY PlayerName"""
				cursor.execute(statement)
				cursor_list=cursor.fetchall()
				return cursor_list
	
	def Goal(self):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """Select * FROM Goal ORDER BY PlayerID"""
				cursor.execute(statement)
				cursor_list=cursor.fetchall()
				return cursor_list
	
	def Assist(self):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """Select * FROM Assist ORDER BY PlayerID"""
				cursor.execute(statement)
				cursor_list=cursor.fetchall()
				return cursor_list
	
	def Statistic(self):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """Select * FROM Statistic ORDER BY MatchID"""
				cursor.execute(statement)
				cursor_list=cursor.fetchall()
				return cursor_list
	
	def Standings(self):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """Select Standings.ID,TeamName,Played,Won,Drawn,Lost,Goals_for,Goals_against,Goals_difference,Points FROM Standings,Teams WHERE Teams.ID=TeamID ORDER BY Points DESC,Goals_difference,TeamName;"""
				cursor.execute(statement)
				cursor_list=cursor.fetchall()
				return cursor_list
	
	def Fixtures(self,week):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """Select Fixtures.ID,T1.TeamName ,T2.TeamName,Week,MatchDate,Time,HomeScore,AwayScore,Status FROM Fixtures,Teams AS T1,Teams AS T2 WHERE Week = %s AND T1.ID=HomeTeam AND T2.ID=AwayTeam;"""
				cursor.execute(statement,([week]))
				cursor_list=cursor.fetchall()
				return cursor_list

	def Referee(self):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """Select * FROM Referee ORDER BY RefereeName"""
				cursor.execute(statement)
				cursor_list=cursor.fetchall()
				return cursor_list

	def Manager(self):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """Select * FROM Manager ORDER BY Name"""
				cursor.execute(statement)
				cursor_list=cursor.fetchall()
				return cursor_list
	
	def Referee_add(self, RefereeName,Age,TotalMatch,TotalRedCard,TotalYellowCard):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """ INSERT INTO Referee(RefereeName,Age,TotalMatch,TotalRedCard,TotalYellowCard) VALUES(%s,%s,%s,%s,%s);"""
				cursor.execute(statement,([RefereeName,Age,TotalMatch,TotalRedCard,TotalYellowCard]))
	
	def Referee_delete(self,RefereeId):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement="""Delete From Referee Where ID = %s;"""
				cursor.execute(statement,([RefereeId]))

	def Referee_update(self, RefereeID,RefereeName,Age,TotalMatch,TotalRedCard,TotalYellowCard):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement="""Update Referee Set RefereeName=%s, Age=%s, TotalMatch=%s, TotalRedCard=%s, TotalYellowCard=%s Where ID=%s;"""
				cursor.execute(statement,([RefereeName,Age,TotalMatch,TotalRedCard,TotalYellowCard,RefereeID]))
	def Referee_update_info(self, ID):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """ Select * From Referee where ID = %s;"""
				cursor.execute(statement,([ID]))
				cursor_list=cursor.fetchall()
				return cursor_list
	
	
	def Standing_add(self, TeamID,Played,Won,Drawn,Lost,Goals_for,Goals_against):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """ INSERT INTO Standings(TeamID,Played,Won,Drawn,Lost,Goals_for,Goals_against,Goals_difference,Points) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s);"""
				cursor.execute(statement,([TeamID,Played,Won,Drawn,Lost,Goals_for,Goals_against,(int(Goals_for)-int(Goals_against)),(3*int(Won)+int(Drawn))]))
	
	def Standing_delete(self,StandingId):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement="""Delete From Standings Where ID = %s;"""
				cursor.execute(statement,([StandingId]))

	def Standing_update(self, StandingId,TeamID,Played,Won,Drawn,Lost,Goals_for,Goals_against):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement="""Update Standings Set TeamID=%s, Played=%s, Won=%s, Drawn=%s, Lost=%s,Goals_for=%s,Goals_against=%s,Goals_difference=%s,Points=%s Where ID=%s;"""
				cursor.execute(statement,([TeamID,Played,Won,Drawn,Lost,Goals_for,Goals_against,(int(Goals_for)-int(Goals_against)),(3*int(Won)+int(Drawn)),StandingId]))
	def Standing_update_info(self, ID):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """ Select * From Standings where ID = %s;"""
				cursor.execute(statement,([ID]))
				cursor_list=cursor.fetchall()
				return cursor_list
				
	def Fixture_add(self, HomeTeam,AwayTeam,HomeScore,AwayScore,Week,MatchDate,Time,Status):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """ INSERT INTO Fixtures(HomeTeam,AwayTeam,HomeScore,AwayScore,Week,MatchDate,Time,Status) VALUES(%s,%s,%s,%s,%s,%s,%s,%s);"""
				cursor.execute(statement,([HomeTeam,AwayTeam,HomeScore,AwayScore,Week,MatchDate,Time,Status]))
	
	def Fixture_delete(self,FixtureId):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement="""Delete From Fixtures Where ID = %s;"""
				cursor.execute(statement,([FixtureId]))

	def Fixture_update(self, FixtureID,HomeTeam,AwayTeam,HomeScore,AwayScore,Week,MatchDate,Time,Status):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement="""Update Fixtures Set HomeTeam=%s, AwayTeam=%s, HomeScore=%s, AwayScore=%s, Week=%s,MatchDate=%s,Time=%s,Statuse=%s Where ID=%s;"""
				cursor.execute(statement,([HomeTeam,AwayTeam,HomeScore,AwayScore,Week,MatchDate,Time,Status,FixtureID]))
	def Fixture_update_info(self, ID):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """ Select * From Fixtures where ID = %s;"""
				cursor.execute(statement,([ID]))
				cursor_list=cursor.fetchall()
				return cursor_list
	
	def Goal_update_info(self, ID):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """ Select * From Goal where ID = %s;"""
				cursor.execute(statement,([ID]))
				cursor_list=cursor.fetchall()
				return cursor_list
	
	def Manager_update_info(self, ID):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """ Select * From Manager where ID = %s;"""
				cursor.execute(statement,([ID]))
				cursor_list=cursor.fetchall()
				return cursor_list

	def Team_update_info(self, ID):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """ Select * From Teams where ID = %s;"""
				cursor.execute(statement,([ID]))
				cursor_list=cursor.fetchall()
				return cursor_list

	def Player_update_info(self, ID):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """ Select * From Player where ID = %s;"""
				cursor.execute(statement,([ID]))
				cursor_list=cursor.fetchall()
				return cursor_list

	def Player_key(self,Key):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """Select * FROM Player WHERE ID=%s"""
				cursor.execute(statement, [Key])
				cursor_list=cursor.fetchall()
				return cursor_list
	
	def Team_key(self,Key):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """Select * FROM Teams WHERE ID=%s"""
				cursor.execute(statement, [Key])
				cursor_list=cursor.fetchall()
				return cursor_list
	
	def Goal_key(self,Key):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """Select * FROM Goal WHERE ID=%s"""
				cursor.execute(statement, [Key])
				cursor_list=cursor.fetchall()
				return cursor_list
	
	def Manager_key(self,Key):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """Select * FROM Manager WHERE ID=%s"""
				cursor.execute(statement, [Key])
				cursor_list=cursor.fetchall()
				return cursor_list