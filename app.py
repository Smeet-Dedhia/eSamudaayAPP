import streamlit as st
import requests
import pandas as pd


# def productsInfo(bizID):
#     total = df1.loc[df1.BusinessID==bizID, 'TotalSKU'].values[0]
#     img = df1.loc[df1.BusinessID==bizID, 'ImageMissing'].values[0]
#     prop = df1.loc[df1.BusinessID==bizID, 'skuPropMissing'].values[0]
#     name = df1.loc[df1.BusinessID==bizID, 'mfrNameMissing'].values[0]
#     addr = df1.loc[df1.BusinessID==bizID, 'mfrAddMissing'].values[0]
#     #if((img==0) and (prop==0) and (name==0) and (addr==0)):
#     #    return 'No failed products! All products have passed'
#     #else:
#     #x = {'TotalSKU':str(total),'ImageMissing':str(img), 'SKUpropMissing':str(prop), 'MFRnameMissing':str(name), 'MFRaddMissing': str(addr)}
#     return [total, img, prop, name, addr]



def main():
    df1 = pd.read_csv("data.csv")
    bID = 0
    data1 = ""
    data2 = ""
    data3 = ""

    QueryText = '<p style="font-family:Georgia; color:Black; font-size: 20px;">{resp}</p>'
    QueryText2 = '<p style="font-family:Georgia; color:Green; font-size: 24px;">{resp}</p>'
    ResponseText = '<p style="font-family:Georgia; color:Green; font-size: 17px;">{resp}</p>'
    ResponseText1 = '<p style="font-family:Georgia; color:MediumOrchid; font-size: 17px;">{resp}</p>'
    ResponseText2 = '<p style="font-family:Georgia; color:MediumSlateBlue; font-size: 17px;">{resp}</p>'
    ResponseText3 = '<p style="font-family:Georgia; color:Red; font-size: 17px;">{resp}</p>'
    ItemText1 = '<p style="font-family:Georgia; color:Black; font-size: 17px;">{resp}</p>'
    ItemText2 = '<p style="font-family:Georgia; color:Blue; font-size: 17px;">{resp}</p>'

    NameID = dict(zip(df1['Name'],df1['BusinessID']))

    menu = ["Home", "Business Report", "Overall Analytics"] 

    choice = st.sidebar.selectbox("Menu", menu)


    if choice == "Home":
        st.image('eSamudaayLogo.635d9bd5.svg', width=100000)
        #st.markdown('<img src="eSamudaayLogo.635d9bd5.svg"  width="500" >',unsafe_allow_html=True)
        st.header("Hackathon project by TEAM DOMIN8")
        st.subheader("Navigate to BUSINESS REPORT menu to see customized reports for each business.")
        st.subheader("Navigate to OVERALL ANALYTICS menu to see Cumulative Analytics for all businesses .")
    if choice == "Business Report":

        c1, c2 = st.columns([1,1])

        with c1: 
            name = st.selectbox('Enter Business Name', NameID.keys())
            bID = NameID.get(name)

            s1 = "https://api.test.esamudaay.com/api/v1/businesses/" + str(bID)
            response1 = requests.get(s1)
            data1 = response1.json()

            s2 = "https://esamudaay-api-smeet.herokuapp.com/productInfo/" + str(bID)
            response2 = requests.get(s2)
            data2 = response2.json()

            s3 = "https://api.test.esamudaay.com/api/v1/businesses/" + str(bID) + "/report"
            response3 = requests.get(s3)
            data3 = response3.json()
            
            st.markdown(QueryText.format(resp='Is Business Open?'), unsafe_allow_html=True)
            st.markdown(ResponseText1.format(resp=data1.get('is_open')), unsafe_allow_html=True)

            st.markdown(QueryText.format(resp='Address Location'), unsafe_allow_html=True)
            if(data1.get('address')):
                st.markdown(ResponseText1.format(resp=data1.get('address').get('address_name')), unsafe_allow_html=True)
                st.markdown(QueryText.format(resp='City'), unsafe_allow_html=True)
                st.markdown(ResponseText1.format(resp=data1.get('address').get('geo_addr').get('city')), unsafe_allow_html=True)
            else:
                st.markdown(ResponseText1.format(resp='Address Not Available'), unsafe_allow_html=True)
                st.markdown(QueryText.format(resp='City'), unsafe_allow_html=True)
                st.markdown(ResponseText1.format(resp='City Not Available'), unsafe_allow_html=True)

            st.markdown("""---""")

            st.markdown(QueryText.format(resp='Is Delivery Enabled?'), unsafe_allow_html=True)
            st.markdown(ResponseText2.format(resp=data1.get('has_delivery')), unsafe_allow_html=True)

            st.markdown(QueryText.format(resp='Is Self Pick-UP Available?'), unsafe_allow_html=True)
            st.markdown(ResponseText2.format(resp=data1.get('has_self_pick_up')), unsafe_allow_html=True)

            st.markdown(QueryText.format(resp='Is Slot Delivery Available?'), unsafe_allow_html=True)
            st.markdown(ResponseText2.format(resp=data1.get('has_slot_delivery')), unsafe_allow_html=True)

            st.markdown(QueryText.format(resp='Is SmartBox Delivery Available?'), unsafe_allow_html=True)
            st.markdown(ResponseText2.format(resp=data1.get('has_smartbox_delivery')), unsafe_allow_html=True)
           

        with c2:
            st.markdown('')
            st.markdown('')
            #st.markdown('')

            st.markdown(QueryText.format(resp='Business Category'), unsafe_allow_html=True)
            if(len(data1.get('bcats'))>0):
                st.markdown(ResponseText2.format(resp=data1.get('bcats')[0].get('name')), unsafe_allow_html=True)
            else:
                st.markdown(ResponseText2.format(resp='Category Not Available'), unsafe_allow_html=True)

            st.markdown(QueryText.format(resp='ONDC Enabled?'), unsafe_allow_html=True)
            st.markdown(ResponseText2.format(resp=data1.get('ondc_enabled')), unsafe_allow_html=True)

            st.markdown(QueryText.format(resp='ONDC Category'), unsafe_allow_html=True)
            st.markdown(ResponseText2.format(resp=data1.get('ondc_category')), unsafe_allow_html=True)

            st.markdown("""---""")

            st.markdown(QueryText.format(resp='Rating Count'), unsafe_allow_html=True)
            st.markdown(ResponseText1.format(resp=data1.get('ratings_info').get('ratings_count')), unsafe_allow_html=True)

            st.markdown(QueryText.format(resp='Average Ratings'), unsafe_allow_html=True)
            st.markdown(ResponseText1.format(resp=data1.get('ratings_info').get('ratings_avg')), unsafe_allow_html=True)

            st.markdown("""---""")

            #st.markdown(QueryText.format(resp='Phone No Registered?'), unsafe_allow_html=True)
            #st.markdown(ResponseText.format(resp=data1.get('ratings_info').get('ratings_count')), unsafe_allow_html=True)

            st.markdown(QueryText.format(resp='Is UPI Active?'), unsafe_allow_html=True)
            st.markdown(ResponseText2.format(resp=data1.get('payment_info').get('upi_active')), unsafe_allow_html=True)

            st.markdown(QueryText.format(resp='Is Chat Enabled?'), unsafe_allow_html=True)
            st.markdown(ResponseText2.format(resp=data1.get('chat_enabled')), unsafe_allow_html=True)


        st.subheader("Business Item Details")

        total = data2.get("TotalSKU")
        img = data2.get("ImageMissing")
        sku = data2.get("SKUpropMissing")
        mfrname = data2.get("MFRnameMissing")
        add = data2.get("MFRaddMissing")
        
        st.markdown(QueryText.format(resp='Total Products'), unsafe_allow_html=True)
        st.markdown(QueryText2.format(resp=total), unsafe_allow_html=True)

        if(img>0 and sku>0 and mfrname>0 and add >0): 
            st.warning("Some of your Products have FAILED! Check their failure reasons...")

            st.markdown(QueryText.format(resp='Products with Images Missing:'), unsafe_allow_html=True)
            st.markdown(ResponseText3.format(resp=img), unsafe_allow_html=True)

            st.markdown(QueryText.format(resp='Products with SKU Properties Missing'), unsafe_allow_html=True)
            st.markdown(ResponseText3.format(resp=sku), unsafe_allow_html=True)

            st.markdown(QueryText.format(resp='Products with Manufacturer Name Missing:'), unsafe_allow_html=True)
            st.markdown(ResponseText3.format(resp=mfrname), unsafe_allow_html=True)

            st.markdown(QueryText.format(resp='Products with Manufacturer Address Missing:'), unsafe_allow_html=True)
            st.markdown(ResponseText3.format(resp=add), unsafe_allow_html=True)
        else:
            st.markdown(QueryText2.format(resp='Great! All products are cleared...'), unsafe_allow_html=True)
        st.markdown("""---""")

        st.markdown(QueryText.format(resp='Individual Product Details'), unsafe_allow_html=True)

        for i in range(len(data3)):
            st.markdown(QueryText.format(resp="Product "+str(i+1)+":"), unsafe_allow_html=True)
            st.markdown(ItemText1.format(resp='SKU ID'), unsafe_allow_html=True)
            st.markdown(ItemText2.format(resp=data3[i].get('sku_id')), unsafe_allow_html=True)
            st.markdown(ItemText1.format(resp='Item Name'), unsafe_allow_html=True)
            st.markdown(ItemText2.format(resp=data3[i].get('product_name')), unsafe_allow_html=True)
            #st.write(data3[i].get('failure_reasons'))
            st.markdown("""---""")

    if choice == "Overall Analytics":
        st.header("Overall Business Analytics")
        d1, d2 = st.columns([1,1])

        with d1:
            st.image('delivery.png')
            st.image('chatEnabled.png')
            st.image('ONDCenabled.png')
            st.image('UPIactive.png')
        
        with d2:
            st.image('self-pickup.png')
            st.image('slotDelivery.png')
            st.image('smartboxDelivery.png')
            st.image('download.png')



if __name__ == '__main__':
    main()