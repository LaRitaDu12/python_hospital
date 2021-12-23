def read_data():

    #read the file
    d = os.getcwd() #chemin du projet
    data_path = d+'/model/static/data/diabetic_data.csv'
    mapping_path = d+'/model/static/data/IDs_mapping.csv'

    #convert to pandas dataframe
    df = pd.read_csv(data_path, header ="infer")

    #drop the dead people 
    df = df.drop(df[df["discharge_disposition_id"] == 11 ].index)
    df = df.drop(df[df["discharge_disposition_id"] == 13 ].index)
    df = df.drop(df[df["discharge_disposition_id"] == 14 ].index)
    df = df.drop(df[df["discharge_disposition_id"] == 19 ].index)
    df = df.drop(df[df["discharge_disposition_id"] == 20 ].index)
    df = df.drop(df[df["discharge_disposition_id"] == 21 ].index)
    #11,Expired
    #13,Hospice / home
    #14,Hospice / medical facility
    #19,"Expired at home. Medicaid only, hospice."
    #20,"Expired in a medical facility. Medicaid only, hospice."
    #21,"Expired, place unknown. Medicaid only, hospice."

    #drop the identification data
    df.drop(['race','encounter_id','patient_nbr'],axis=1,inplace=True)

    
    url="https://en.wikipedia.org/wiki/List_of_ICD-9_codes_001%E2%80%93139:_infectious_and_parasitic_diseases"
    page=requests.get(url)
    html_soup=BeautifulSoup(page.content,'html.parser')
    table = html_soup.find_all('table',{"class":"wikitable"})
    df_list = pd.read_html(str(table),header=None)[0]
    df_list.drop(labels="Chapter",inplace=True,axis=1)