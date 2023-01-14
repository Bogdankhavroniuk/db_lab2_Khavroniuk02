CREate TABLE player(
   player_id integer ,
   player_name text,
   player_position text  



);
CREate TABLE team_year (
 t_name text ,
 year_period text ,

 player_id int,
 
 Primary Key(t_name , year_period  )

) ;



CREate TABLE statistic(
 stat_id integer , 
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


