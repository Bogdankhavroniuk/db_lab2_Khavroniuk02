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
        print(conect_parametrs)
        dat = conect_parametrs

        conn = ps.connect("dbname=Khavroniuk_lr_1 user=user1 password=123321 ")





        return  conn





    def get_column(self ,  query ):

        conn  =  self.create_conection()
        cursor = conn.cursor()
        sql =  query
        cursor.execute(sql)
        column  =  cursor.fetchall()
        column_date = []

        conn.close()


        return column



    def get_column_gistogram(self , query ):
            column1 =  self.get_column(query)
            try:
              column  = get_column_data(column1 )
            
              p = float(1.322)

              diapazon = max(column) - min(column)

              n = m.ceil(1 + (p * m.log10(50)))

              h = diapazon / n

              list_of_intervals = []
              patches = []
              x = 1
              i = 1

              patches.append(x)

              while i <= n:
                  list_of_intervals.append(x)
                  i += 1
                  x += h
                  list_of_intervals.append(x)
                  patches.append(x)
            




              plt.hist(column, bins=list_of_intervals, edgecolor='black')
              plt.xticks(patches)
              #plt.savefig('Gistogram.png')
              plt.show()
              plt.close()
            except:
                print("Wrong data input")
            return column





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
               column1  =  get_column_data(column1)
               column2  =  get_column_data(column2)
               fig, ax = plt.subplots()

               ax.plot(column1 , column2 , linewidth=2.0)
               plt.xlabel(column_of_values1 , column_of_values2 )
               plt.ylabel('values')
               ax.set(xlim=(0, 8), xticks=np.arange(1, 8),ylim=(0, 8), yticks=np.arange(1, 8))
               #plt.savefig('dependency_diagram.png')
               plt.show()
               plt.close()
        except:
            print("cant build graph from this query")
            

        return  data_values  ,  data_names







