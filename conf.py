import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def process(df,options):
    
    def mapping(feature):
        return feature.map({'Yes':1,'No':0})
    
    cat_cols=['SeniorCitizen', 'Dependents', 'PhoneService', 'PaperlessBilling']
    
    df['cat_cols']=df[cat_cols].apply(mapping)
    if ( options=='Online'):
        columns=['SeniorCitizen', 'Dependents', 'tenure', 'PhoneService', 'PaperlessBilling', 'MonthlyCharges', 'TotalCharges',
                 'MultipleLines_No_phone_service', 'MultipleLines_Yes', 'InternetService_Fiber_optic', 'InternetService_No', 
                 'OnlineSecurity_No_internet_service', 'OnlineSecurity_Yes', 'OnlineBackup_No_internet_service', 
                 'TechSupport_No_internet_service', 'TechSupport_Yes', 'StreamingTV_No_internet_service', 'StreamingTV_Yes', 
                 'StreamingMovies_No_internet_service', 'StreamingMovies_Yes', 'Contract_One_year', 'Contract_Two_year', 'PaymentMethod_Electronic_check']
        df=pd.get_dummies(df).reindex(columns=columns,fill_value=0)
    elif (options=='Batch'):
        columns=['SeniorCitizen', 'Dependents', 'tenure', 'PhoneService', 'PaperlessBilling', 'MonthlyCharges', 'TotalCharges',
                 'MultipleLines_No_phone_service', 'MultipleLines_Yes', 'InternetService_Fiber_optic', 'InternetService_No',
                 'OnlineSecurity_No_internet_service', 'OnlineSecurity_Yes', 'OnlineBackup_No_internet_service',
                 'TechSupport_No_internet_service', 'TechSupport_Yes', 'StreamingTV_No_internet_service', 'StreamingTV_Yes',
                 'StreamingMovies_No_internet_service', 'StreamingMovies_Yes', 'Contract_One_year', 'Contract_Two_year', 'PaymentMethod_Electronic_check']
        df=pd.get_dummies(df).reindex(columns=columns, fill_value=0)
        
    else:
        print("Invalid Information")
        
    #Feature Scaling
    ms=MinMaxScaler()
    df['tenure']=ms.fit_transform(df[['tenure']])
    df['TotalCharges']=ms.fit_transform(df[['TotalCharges']])
    df['MonthlyCharges']=ms.fit_transform(df[['MonthlyCharges']])
    
    return df
        
        
    
    
    