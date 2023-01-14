import select
import re
import psycopg2 as  ps
import matplotlib as mpl
import matplotlib.pyplot as plt
import math as  m
import numpy  as np
import psycopg2.extras



def get_column_data(column1):

    column = []

    for i in range(len(column1)):
        column.append(int(column1[i][0]))

    return column



def get_string_data(column1):
    column = []

    for i in range(len(column1)):
        column.append((str(column1[i][0])).replace(" " , ""))

    return column



class Get_visualisation():



    def __init__(self , database_name  ,  user_name ,  password  , host  , port  ):

       self.database_name =  database_name

       self.user_name =  user_name

       self.user_name = password

       self.password  = password

       self.host  =  host

       self.port  = port



    def create_conection(self):
        d_n  = self.database_name
        u_n = self.user_name
        p_w = self.password

        conect_parametrs = "dbname="+  d_n +" user="+  u_n +" password=" +p_w

        dat = conect_parametrs

        conn = ps.connect("dbname=lr2 user=user1 password=123321 ")





        return  conn





    def get_column(self ,  query ):

        conn  =  self.create_conection()
        cursor = conn.cursor()
        sql =  query
        cursor.execute(sql)
        column  =  cursor.fetchall()
        column_date = []

        conn.close()


        return column1 , column2



    def get_column_gistogram(self , query , query1 ):
              column1 =  self.get_column(query)
              column2 = self.get_column(query1)
              column  = get_column_data(column1 )

              values = get_string_data(column2)
              fig = plt.figure(figsize=(10, 10))
              plt.bar( values, column, color='maroon' , width = 0.4)

              plt.xlabel("name of scorer")
              plt.ylabel("sccorer points")
              plt.title("The geatest scorer")



              plt.show()
              plt.close()

              return column1





    def get_circle_gistogram(self , query , query1  ):

            column1 =  self.get_column(query)
            column2 =  self.get_column( query1  )
           
            
            
            try :
                data_values = get_column_data(column1)
                data_names = get_string_data(column2)
                if  len(column1) != len(column2):
                  raise Exception("Dimention_exeption")
                if isinstance(data_names[0] , str) == False or isinstance(data_values[1] , int ) == False:
                   raise Exception("Data_typpe_exeption")
                else:

                   fig, ax = plt.subplots()
                   ax.pie(data_values, labels=data_names)
                   ax.axis("equal")
                   #plt.savefig('circle_diagram.png')
                   plt.title("The geatest scorer")
                   plt.show()
                   plt.close()
            except:
                print("Cant print diagram from this query")
                    
                
                
           
            return column1  , column2



    def  dependency_graphick(self , query1 , query2  ):
   
        column1 = self.get_column(query1 )
        column2 = self.get_column(query2 )
       
        try:
            column1 = get_column_data(column1)
            column2 = get_column_data(column2)
            if len(column1) != len(column2):
                raise Exception("Dimention_exeption")

            if isinstance(column2[0], int ) == False or isinstance(column1[0], int) == False:
                    raise Exception("Data_typpe_exeption")
            else:

               fig, ax = plt.subplots()

               ax.plot(column1 , column2 , linewidth=2.0)

               plt.title("Dependensy bbetwen field goals and total points")
               #plt.savefig('dependency_diagram.png')
               plt.show()
               plt.close()
        except:
            print("cant build graph from this query")
            

        return  column1  ,  column2







