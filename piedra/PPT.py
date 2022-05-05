import random
import pandas as pd

jugada = 0
df = pd.DataFrame( columns= ["jugador" , "cpu", "estado"])
bol = True
maquina_2 = ""


contador_u = 0
contador_m = 0


while(bol):

    
    usuario = input("Escoge una opción: \n")

    if jugada == 0 :
        maquina = random.choice(["piedra", "papel", "tijera"])
        maquina_2 = maquina
        
    df = df.append({"jugador":usuario, "cpu":maquina}, ignore_index=True)


    if (df.loc[jugada,"jugador"] == df.loc[jugada,"cpu"]):
            df.loc[jugada,"estado"] = "empate"

    if ( (df.loc[jugada,"jugador"] == "piedra" and df.loc[jugada,"cpu"] == "tijera") or (df.loc[jugada,"jugador"] == "papel" and df.loc[jugada,"cpu"] == "piedra") or (df.loc[jugada,"jugador"] == "tijera" and df.loc[jugada,"cpu"] == "papel") ):
            df.loc[jugada,"estado"] = "pierde"
        
    if ( (df.loc[jugada,"jugador"] == "piedra" and df.loc[jugada,"cpu"] == "papel") or (df.loc[jugada,"jugador"] == "papel" and df.loc[jugada,"cpu"] == "tijera") or (df.loc[jugada,"jugador"] == "tijera" and df.loc[jugada,"cpu"] == "piedra") ):
            df.loc[jugada,"estado"] = "gane"

    
    if (df.loc[jugada,"estado"] == "gane"):
        dff = df[ df["estado"] == "gane"]
    
    if (df.loc[jugada,"estado"] == "pierde"):
        dff = df[ df["estado"] == "pierde"]

    if (df.loc[jugada,"estado"] == "empate"):
        dff = df[ df["estado"] == "empate"]

    final = dff["jugador"].value_counts()
    final = final.reset_index()
    maquina_2 = final.loc[0,"index"]

    """if resultado == "piedra":
        maquina_2 = "tijera"
    if resultado == "papel":
        maquina_2 = "piedra"
    if resultado == "tijera":
        maquina_2 = "papel" """
 
    print("\n")  

    if usuario == maquina:
            print("maquina: " +maquina)   
            print("usuario: " +usuario)   
            print("")
            print("empate") 
            print("")  
            print("contador CPU = " + str(contador_m))  
            print("jugador = " + str(contador_u)) 
            print("")  
            print("\n")

    if (usuario == "piedra" and maquina == "tijera") or (usuario == "papel" and maquina == "piedra") or (usuario == "tijera" and maquina == "papel"):
            contador_u = contador_u + 1
            
            print("maquina: " +maquina)   
            print("usuario: " +usuario)   
            print("")
            print("ganaste") 
            print("")  
            print("contador CPU = " + str(contador_m))  
            print("jugador = " + str(contador_u)) 
            print("")  
            print("\n")


    if (usuario == "piedra" and maquina == "papel") or (usuario == "papel" and maquina == "tijera") or (usuario == "tijera" and maquina == "piedra"):

            contador_m = contador_m + 1
            
            print("maquina: " +maquina)   
            print("usuario: " +usuario)   
            print("")
            print("perdiste ") 
            print("")  
            print("contador CPU = " + str(contador_m))  
            print("jugador = " + str(contador_u)) 
            print("")  
            print("\n") 
    
    jugada = jugada + 1
    maquina = maquina_2
    if contador_u == 7 or contador_m == 7:
        bol = False

if contador_m == 7:
    print("maquina gana")
if contador_u == 7:
    print("usuario gana")

#df.to_csv("salida.csv")
#print(df)
