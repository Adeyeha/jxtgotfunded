import streamlit_authenticator as stauth 
import streamlit as st

import yaml
from yaml.loader import SafeLoader
with open('old/config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

print(config)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    # config['preauthorized']
)

name, authentication_status, username = authenticator.login('Login', 'main')

if authentication_status:
    authenticator.logout('Logout', 'main')
    if username == 'jsmith':
        st.write(f'Welcome *{name}*')
        st.title('Application 1')
    elif username == 'rbriggs':
        st.write(f'Welcome *{name}*')
        st.title('Application 2')
elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')

# if st.session_state["authentication_status"]:
#     authenticator.logout('Logout', 'main')
#     st.write(f'Welcome *{st.session_state["name"]}*')
#     st.title('Some content')
# elif st.session_state["authentication_status"] == False:
#     st.error('Username/password is incorrects')
# elif st.session_state["authentication_status"] == None:
#     st.warning('Please enter your username and password')