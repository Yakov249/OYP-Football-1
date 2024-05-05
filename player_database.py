import streamlit as st
import pandas as pd
def player_database_page():
    st.title("Player database")
    st.header("Data source: https://www.fbref.com/")
    st.sidebar.header("Choose your features:")
    selected_year = st.sidebar.selectbox("Season", list(f"{i-1}-{i}" for i in range(2022, 2010, -1)))
    years = {
        "2021": "https://fbref.com/en/share/AqYHp",
        "2020": "https://fbref.com/en/share/9oKEZ",
        "2019": "https://fbref.com/en/share/rPWzg",
        "2018": "https://fbref.com/en/share/U0Nlp",
        "2017": "https://fbref.com/en/share/2D44U",
        "2016": "https://fbref.com/en/share/1Dif9",
        "2015": "https://fbref.com/en/share/HGohy",
        "2014": "https://fbref.com/en/share/JYfNm",
        "2013": "https://fbref.com/en/share/SVvhs",
        "2012": "https://fbref.com/en/share/0Eo8N",
        "2011": "https://fbref.com/en/share/I5iuO",
        "2010": "https://fbref.com/en/share/ued5k"
    }
    @st.cache_data
    def load_data(year):
        url = years[year.split("-")[0]]
        html = pd.read_html(url)
        df = html[0]
        df = df.drop(["Per 90 Minutes"], axis = 1, level = 0)
        df = df.drop(["Progression"], axis = 1, level = 0)
        df.columns = df.columns.droplevel(0)
        index_names = df[df["Player"] == "Player"].index
        raw = df.drop(labels = index_names, axis = 0)
        raw = raw.reset_index(drop = True)
        raw["Nation"] = raw["Nation"].apply(lambda x: (x.split(' '))[-1])
        raw = raw.drop(["Matches"], axis = 1)
        playerstats = raw.drop(["Rk"], axis = 1)
        return playerstats
    playerstats = load_data(selected_year)
    sorted_unique_team = sorted(playerstats["Squad"].unique())
    selected_team = st.sidebar.multiselect("Club", sorted_unique_team, sorted_unique_team, help = "Select the clubs to display player's stats")
    unique_pos = sorted(playerstats["Pos"].unique())
    selected_pos = st.sidebar.multiselect("Position", unique_pos, unique_pos, help = "Select positions to display player's stats")
    df_selected_team = playerstats[(playerstats["Squad"].isin(selected_team)) & (playerstats["Pos"].isin(selected_pos))]
    st.header("Player stats of selected team/s")
    st.write("Data Dimension: " + str(df_selected_team.shape[0]) + " rows and " + str(df_selected_team.shape[1]) + " columns.")
    st.dataframe(df_selected_team)
    with st.expander("Glossary"):
        st.info('''
        **Pos:**\n
        GK - Goalkeepers\n
        DF - Defenders\n
        MF - Midfielders\n
        FW - Forwards\n
        FB - Fullbacks\n
        LB - Left Backs\n
        RB - Right Backs\n
        CB - Center Backs\n
        DM - Defensive Midfielders\n
        CM - Central Midfielders\n
        LM - Left Midfielders\n
        RM - Right Midfielders\n
        WM - Wide Midfielders\n
        LW - Left Wingers\n
        RW - Right Wingers\n
        AM - Attacking Midfielders\n
        **MP:** Matches Played. Matches Played by the player or squad\n
        **Starts:** Starts. Game or games started by player\n
        **Min:** Minutes played.\n
        **90s:** Number of 90s played. Minutes played divided by 90\n
        **Gls:** Goals. Goals scored or allowed\n
        **Ast:** Assists.\n
        **G-PK:** Non-Penalty Goals.\n
        **PK:** Penalty Kicks Made.\n
        **PKatt:** Penalty Kicks Attempted.\n
        **CrdY:** Yellow Cards.\n
        **CrdR:** Red Cards.\n
        **xG:** Expected Goals. xG totals include penalty kicks, but do not include penalty shootouts (unless otherwise noted).\n
        **npxG:** Non-Penalty Expected Goals.\n
        **xA:** xG Assisted. xG which follows a pass that assists a shot\n
        **npxG+xA:** Non-Penalty Expected Goals plus xG Assisted. xG totals include penalty kicks, but do not include penalty shootouts (unless otherwise noted).
        ''')
    if st.button("Head back to the home page", on_click = lambda: st.session_state.update(page = "main")):
        pass
    return False if not st.session_state.get("page") == "main" else True
