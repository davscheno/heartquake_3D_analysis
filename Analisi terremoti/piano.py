
# coding: utf-8

# In[ ]:


def piano(A,B,C_,D):

    #calcolo E
    E=np.sqrt(A**2 + B**2 + 1)

    #calcolo i coseni
    cos_a = A/E

    cos_b = B/E

    cos_cp = C_/E  #gamma_p


    cos_c = np.cos((np.pi/2) + np.arccos(C_/E))   #controllare se è corretto 

    #calcolo la direzione teta del vettore, il coseni direttori danno la direzione del vettore occorrre aggiungere 90°
    teta_primo = np.arctan(cos_a/cos_b)   #espresso in radianti
    teta_deg = (teta_primo*180)/np.pi 

    #calcolo della direzione della massima pendenza sul piano
    #dip_direction = teta_deg 

    #calcolo l'immersione dip angolo tra la verticale e il piano
    dip_vert = np.arcsin(-1*cos_c)
    dip_deg = (dip_vert*180)/np.pi

    #calcolo l'immersione dip
    dip = dip_deg
    #occorre orientare correttamente il dip_direction
    #cond_1 = dip_direction = teta_deg
    #cond_2 = dip_direction = teta_deg + 180
    #cond_3 = dip_direction =  teta_deg + 360

    #def orientation(cos_a,cos_b):

    if cos_a > 0 and cos_b > 0:                
        dip_direction = teta_deg
        if cos_cp <0:
            dip_direction =  dip_direction + 180

    if  cos_a > 0 and cos_b < 0:
        dip_direction = teta_deg + 180
        if cos_cp <0:
            dip_direction =  dip_direction + 180


    if  cos_a < 0 and cos_b < 0:
        dip_direction = teta_deg + 180
        if cos_cp <0:
            dip_direction =  dip_direction - 180


    if  cos_a < 0 and cos_b > 0:
        dip_direction =  teta_deg + 360
        if cos_cp <0:
            dip_direction =  dip_direction - 180








    #creo l'array per il plotaggio su stereogramma
    plot_dip_direction = 0
    plot_dip = 0
    plot_dip_direction = np.append(plot_dip_direction, dip_direction)
    plot_dip = np.append(plot_dip, dip)
    print("dip_direction= %f ; dip= %f" % (dip_direction, dip))
    print(cos_a, cos_b)
    print('##################################################')
    print(teta_deg)
    output = "teta= %f ; dip= %f" % (dip_direction, dip)
    file = open("giacitura_cluster_xx_plane.txt","w")
    file.write(output)
    file.close()

    daframe_cluster_xx = pd.DataFrame.to_csv(df_cluster_2)
    file = open("daframe_cluster_xx_plane.csv","w")
    file.write(daframe_cluster_xx)
    file.close()

    #salva i risultati su di un file shape
    geometry = [Point(xy) for xy in zip(df_cluster_2.x , df_cluster_2.y)]
    df_shape = df_cluster_2.drop(['x', 'y','Ora', 'Data', 'Sec'], axis=1)
    crs = {'init': 'epsg:3003'}
    gdf = GeoDataFrame( df_shape, crs=crs, geometry=geometry)   #df_shape,
    gdf.to_file(driver = 'ESRI Shapefile', filename= "result_xx_plane.shp" )



    strike = plot_dip_direction - 90 
    dip =  plot_dip
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='stereonet')
    ax.plane(strike, dip)
    ax.pole(strike, dip ,markersize=5)
    ax.grid()
    plt.show()

