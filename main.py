from  Data_analis import Vizualization


if __name__ == '__main__':

   data1 = Vizualization.Get_visualisation(user_name="user1", database_name="lr2", password  ="123321", host  ="localhost", port ="5432")
   print(data1.get_column_gistogram( "SELECT   total_points FROM statistic"  ,"SELECT trim(player_name) FROM player"))
   print(data1.get_circle_gistogram("SELECT total_points  FROM statistic "  ,  "SELECT trim(player_name) FROM player"))
   print(data1.dependency_graphick("SELECT field_goals  FROM statistic " , "SELECT total_points  FROM statistic "))
