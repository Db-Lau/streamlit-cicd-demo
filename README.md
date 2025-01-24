# Streamlit demo

## Step 1: API
- sign up for openweathermap.org
- generate an API key
- identify the API url

## Step 2: app.py
- create your streamlit app, i.e. app.py
- in your uv environment, install streamlit and requests
- in app.py, retrieve the API key that is stored in Streamlit Cloud. But DON't put the API key in the script
    ```python
    api_key = st.secrets["openweather_api_key"]
    ```
- use the API url and API key to get data
    ```python
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    ```
## Step 3: Streamlit Cloud
- sign up Streamlit Cloud
- create an app by connecting to a public repo in your github acc
- a webhook will be created automatically in github repo so that Streamlit Cloud will listen to all changes to the repo's main branch and redeploy the app
- this means that the deployment step in cd.yml is redundant