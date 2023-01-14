CREate TABLE statistic(
 stati_id integer , 
 player_id integer,
 total_games integer , 
 total_points integer, 
 field_goals integer
);

ALTer TABLE player
ADD CONSTRAINT player_id   primary KEY (player_id);

ALTer TABLE team_year
ADD CONSTRAINT player_id FOREIGN KEY(player_id )  REFERENCES player(player_id);

ALTer TABLE statistic
ADD CONSTRAINT stat_id primary KEY  (stat_id) , 
ADD CONstraint player_id FOREIGN KEY(player_id )  REFERENCES player(player_id);


INSERT INTO player
VALUES (1, 'Kareem Abdul-Jabbar', 'C' ),
       (2, 'LeBron James', 'SF' ),
       (3, 'Karl Malone', 'PF' ),
       (4, 'Kobe Bryant', 'SG' ),
	    (5, 'Michael Jordan', 'SG' ),
		(6, 'Dirk Nowitzki', 'PF/C'),
		(7, 'Wilt Chamberlain', 'C');


INSERT INTO team_year
VALUES ( 'Milwaukee Bucks ', '(1969–1975)', 1),
       ( 'Los Angeles Lakers ', '(1975–1989)', 1),
       ( 'Cleveland Cavaliers', '(2003–2010, 2014–2018)', 2),
       ( ' Miami Heat ', '(2010–2014)', 2),
	   ( 'Los Angeles Lakers ', '(2018–present)', 2),
       ( 'Utah Jazz  ', '(1985–2003)', 3 ),
       ( 'Los Angeles Lakers ', '(2003–2004)', 3),
	   ( 'Los Angeles Lakers ', '(1996–2016)', 4 ),
	    ( 'Chicago Bulls ', '(1984–1993, 1995–1998)', 5 ),
		( 'Washington Wizards  ', '(2001–2003)', 5 ),
		( 'Dallas Mavericks ', '(1998–2019)', 6 ),
		( 'Philadelphia/San Francisco Warriors ', '(1959–1965) ', 7 ),
		( 'Philadelphia 76ers ', '(1965–1968) ', 7 ),
		( 'Los Angeles Lakers ', '(1965–1973) ', 7 )
		;

INSERT INTO statistic
VALUES ( 101, 1, 1560, 38387 , 15837),
       ( 102 , 2 , 1397, 37965  ,13896 ),
       ( 103 ,3, 1476, 36928,13528 ),
       ( 104,4, 1346, 33643 ,11719 ),
	   ( 105,5,1072 , 32292 ,12192 ),
	   ( 106,6,1522,31560  ,11169 ),
       ( 1077 ,7, 1045  ,  31419, 12681  );
