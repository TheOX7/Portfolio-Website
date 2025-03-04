import streamlit as st
import base64
from streamlit_extras.colored_header import colored_header

st.set_page_config(
    page_title='Marselius Agus Dhion - Portfolio',
    layout='wide'
)

def enter():
    st.markdown('<br>', unsafe_allow_html=True)
    
def horizontal_line():
    st.markdown('<hr>', unsafe_allow_html=True)
    
def logo_link(link, path_img, width):
    st.markdown(
        """<div style="display: grid; place-items: center;">
        <a href="{}">
        <img src="data:image/png;base64,{}" width="{}">
        </a></div>""".format(
            link,
            base64.b64encode(open(path_img, "rb").read()).decode(),
            width,
        ),
        unsafe_allow_html=True,
    )

horizontal_line()
st.markdown("""
    <div style='text-align: center; font-size:36px'>
        <b>Marselius Agus Dhion - Portfolio</b>
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <div style='text-align: center; font-size:20px;'>|
        <a href="#internship-experiences" style='text-decoration: none;'>Internship Experiences</a> | 
        <a href="#projects" style='text-decoration: none;'>Projects</a> | 
        <a href="#thesis" style='text-decoration: none;'>Thesis</a> |
    </div>
""", unsafe_allow_html=True)

horizontal_line()

with st.container():
    enter()
    enter()

    col_img, col_exp = st.columns([1, 5])
    
    with col_img:
        st.image('image/img-bg.png', width=270)
        
        st.markdown("""
            <div style='text-align: center; font-size:20px'>
                <b>Marselius Agus Dhion</b> 
                <br>
                Data Enthusiast
            </div>
        """, unsafe_allow_html=True)
                 
    with col_exp:
        # st.markdown("""<div style='font-size:36px'>About Me</div>""", unsafe_allow_html=True)
        colored_header(
            label="About Me",
            description="",
            color_name="orange-70",
        )
        st.markdown("""
            <div style='font-size:16px'>
                <b>Related Links: </b>
                <a href="https://linkedin.com/in/marselius-agus-dhion/" style="text-decoration: none;">LinkedIn Profile</a> ||
                <a href="https://github.com/TheOX7" style="text-decoration: none;">Github Repository</a> ||
                <a href="https://medium.com/@thismad07" style="text-decoration: none;">Medium</a> ||
                <a href="https://public.tableau.com/app/profile/mad27/vizzes" style="text-decoration: none;">Tableau Profile</a>
            </div>
        """, unsafe_allow_html=True)   
        col_exp_left_1, col_exp_mid_1, col_exp_right_1 = st.columns([2,3,5])

        style = """
            <style>
                .rounded-box {
                    border: 1px solid white;
                    border-radius: 10px;
                    padding: 12px;
                    background-color: #0E1117;
                    text-align: center; /* Memposisikan teks ke tengah */
                }
            </style>
        """
                
        with col_exp_left_1:
            st.markdown(style, unsafe_allow_html=True)
            st.markdown("""<div class="rounded-box">
                        <b>Work Experiences</b> 💼 
                        <br>
                        6 months experience<br>
                        Data Analyst & Data Scientist Intern
                        </div>""", 
                        unsafe_allow_html=True)
            
        with col_exp_mid_1:
            st.markdown(style, unsafe_allow_html=True)
            st.markdown("""<div class="rounded-box">
                        <b>Education</b> 🎓 
                        <br>
                        Unofficial Undergraduate - Information Systems - <a href="https://drive.google.com/file/d/1RqODtLrZc3vFLELQfhP4mOs-ydSi3ib9/view?usp=sharing">GPA: 3.94</a>
                        <br>
                        Universitas Kristen Maranatha
                        </div>""", 
                        unsafe_allow_html=True)
            
        with col_exp_right_1:
            st.markdown(style, unsafe_allow_html=True)
            st.markdown("""<div class="rounded-box">
                        <b>Achievements</b> 🎖️ 
                        <br>
                        ○ Favourite Dashboard Winner - Pedas (Pesta Data Nasional 2023) -
                        <a href="https://public.tableau.com/app/profile/mad27/viz/Superstore_16986572902350/Final-Dashboard">Tableau Dashboard</a> |
                        <a href="https://drive.google.com/file/d/1ER6NIrTQ5TF7oXmdfJx73ZbYLeTkFGov/view?usp=sharing">Certificate</a>
                        <br>
                        ○ <b>Dean List:</b> Even Semester 21/22 | Odd Semester 22/23 | Even Semester 22/23 | Odd Semester 23/24
                        <br>
                        </div>""", 
                        unsafe_allow_html=True)
        
        enter()  
        col_exp_left_2, col_exp_right_2 = st.columns(2)
        
        with col_exp_left_2:  
            with st.expander('Hard Skills'):
                st.markdown("""
                <ul>
                    <li><b>SQL</b>
                        <ul>
                            <li>PostgreSQL</li>
                            <li>MySQL</li>
                            <li>Google BigQuery</li>
                        </ul>
                    </li>
                    <li><b>Programming Language</b>
                        <ul>
                            <li>Python</li>
                            <li>Java</li>
                        </ul>
                    </li>
                    <li><b>Data Visualization Tools</b>
                        <ul>
                            <li>Tableau</li>
                            <li>Streamlit (Python - Web App)</li>
                            <li>Google Data (Looker) Studio</li>
                            <li>Power BI</li>
                        </ul>
                    </li>
                </ul>
                """, unsafe_allow_html=True)
                
            with st.expander('Soft & Other Skills'):
                st.markdown("""
                <ul>
                    <li><b>Language Proficiencies</b>
                        <ul>
                            <li> English (Intermediate) </li>
                            <li> Indonesia (Native) </li>
                        </ul>
                    </li>
                    <li><b>Other Skills</b>
                        <ul>
                            <li> Git & GitHub </li>
                            <li> Web Scraping: Octoparse & Power Automate </li>
                        </ul>
                    </li>
                </ul>
                """, unsafe_allow_html=True)                
                                    
        with col_exp_right_2:
            with st.expander('Organization Experiences'):    
                st.markdown("""
                <ul>
                    <li><b>Event Division Member - Wiratha Fest (Jan - Jun 2022)</b>
                        <ul>
                            <li> Organized the entire Wiratha Fest event, from concept to execution. </li>
                            <li> Created quizzes and door prize giveaways for the audience during the event. </li>
                            <li> Collaborated withthe Public Relations division to identify and engage relevant audiences and speakers. </li>
                            <li> Collaborated with the Finance Division to calculate projected expenses and drafted a thorough 
                            proposal for submission to Maranatha Christian University. </li>
                        </ul>
                    </li>
                </ul>
                """, unsafe_allow_html=True)                
                
            with st.expander('Training and Courses'):    
                st.markdown("""
                <ul>
                    <li><b>MySkill: Data Analysis Bootcamp (Oct - Nov 2022)</b>
                        <ul>
                            <li> Skills Gained → Python, PostgreSQL, Looker Studio, Clustering, & Customer Segmentation </li>
                            <li> I become as one of the top ten students due to the excellence of my capstone project. </li>
                            <li> Project → <a href="https://lookerstudio.google.com/reporting/cd26e7aa-e114-4bcb-81b0-ca98ed97ec73">Looker Studio Dashboard</a> | 
                                           <a href="https://github.com/TheOX7/Data-Analytics-Bootcamp-MySkill-">Github Repository</a> 
                            </li>
                            <li> Excellent Student Certificate → <a href="https://drive.google.com/drive/folders/1uPC0nFJ3rnft3mX9R-RzHpCUAdS64nvo?usp=sharing">Certificate Link</a> </li>
                        </ul>
                    </li>
                    <li><b>DQLab: Tetris Batch 3 (May - Jun 2023)</b>
                        <ul>
                            <li> Skills Gained → Python, PostgreSQL, Pentaho for ETL (Extract, Transform, & Load), & Streamlit </li>
                            <li> Project → <a href="https://pl-2022-2023.streamlit.app">Streamlit App Link</a> | 
                                           <a href="https://github.com/TheOX7/Premier-League-Streamlit-Web-App">Github Repository</a> 
                            </li>
                            <li> Certificate → <a href="https://academy.dqlab.id/Certificate_check/result/DQLABTSB3IBEIQN#mycertificate">Certificate Link</a> </li>
                        </ul>
                    </li>
                    <li><b>Kelas.com: Data Science Bootcamp</b>
                        <ul>
                            <li> Skills Gained → Python, MySQL, Tensorflow, Deep Learning, & Git </li>
                            <li> Project → <a href="https://github.com/TheOX7/Final-Proyek-Data-Science-Kelas.com">Github Repository</a> | 
                                           <a href="https://drive.google.com/file/d/1Bfs3rl_KDR3ZoICGrBOzH_q3L3hpsUnt/view?usp=sharing">Report Card</a> 
                            </li>
                            <li> Certificate → <a href="https://academy.dqlab.id/Certificate_check/result/DQLABTSB3IBEIQN#mycertificate">Certificate Link</a> </li>
                        </ul>
                    </li>
                </ul>
                """, unsafe_allow_html=True)                

enter(); enter(); enter()
     
with st.container():
    st.markdown("<a id='thesis'></a>", unsafe_allow_html=True)
    horizontal_line()
    st.markdown("""
        <div style='text-align: center; font-size:36px'>
            <b>Thesis</b>: 
            <b style='font-size: 30px'>Fantasy Premier League Rec. Starting Lineup using Regression Function Optimization</b> 
        </div>
    """, unsafe_allow_html=True)
    horizontal_line()
    
    col_vid, col_exp = st.columns([1,2])
    with col_vid:
        st.markdown(f'<iframe width="550" height="350" src="https://www.youtube.com/embed/XtqkC0qYQXA" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)
        enter()
    with col_exp:
        st.subheader('Explanation', divider='gray')
        st.markdown("""
                    <li>
                        Scraped FPL player stats datasets from the official Premier League website using Power Automate for every single gameweek.  
                    </li>
                    <li>
                        Predicted the FPL player's expected total points for the upcoming gmeweek in 2024/25 using Random Forest (created for each player's 
                        position and a general (all positions) model), with the per-position model achieving better performance, showing a Mean Absolute Error of 1.27 and an R-Squared of 81.15.
                    </li>
                    <li>
                        Optimized FPL recommended starting lineup using PuLP to find the best solution based on several constraints from 
                        <a href="https://fantasy.premierleague.com/help/rules" target="_blank" style="text-decoration: none">
                            FPL rules
                        </a> 
                        , such as a maximum starting lineup cost of £100.
                    </li>
                    <li>
                        Created a website using Streamlit to display stats and the FPL recommended starting lineup for the upcoming gameweek.
                    </li>
                    <li>
                        Implement a paired t-test to validate the starting lineup recommendation for the 2024/25 season for each gameweek to 
                        determine whether the differences between predicted and actual total points are statistically significant.
                    </li>
                    <li>
                        Currently in the process of creating a paper for publication in 
                        <a href="https://journals.sagepub.com" target="_blank" style="text-decoration: none">
                            Sage Journals
                        </a> 
                        and 
                        <a href="https://journal.maranatha.edu/index.php/jutisi" target="_blank" style="text-decoration: none">
                            JuTiSi Maranatha
                        </a>.
                    </li>

                    <li>
                        <b>Related Links: </b>
                        <a href="https://fpl-rec-selection-lineup.streamlit.app">Streamlit App</a> | 
                        <a href="https://github.com/theox7/best-team-selection-fpl">Github Repository</a> | 
                        <a href="https://drive.google.com/file/d/1Vcv9yHmfX8p-k5TAurNOaBR252LpOYwT/view?usp=sharing">Thesis Paper</a>
                        <a href="https://drive.google.com/file/d/1Aizz9Rxt1L6BxP0hu3gha7YAdomyDWTo/view?usp=sharing">Journal Publication (Ongoing)</a>
                    </li>
                    """, unsafe_allow_html=True)
    
    enter(); enter(); enter()


     
     
with st.container():
    st.markdown("<a id='internship-experiences'></a>", unsafe_allow_html=True)
    horizontal_line()
    st.markdown("""
        <div style='text-align: center; font-size:36px'>
            <b>Internship Experiences</b> 
        </div>
    """, unsafe_allow_html=True)
    horizontal_line()
    
    enter()
    
    col_left, col_mid, col_right = st.columns(3)
    style_intern = """
        <style>
            .rounded-box {
                border: 2px solid white;
                border-radius: 10px;
                padding: 15px;
                background-color: #0E1117;
                text-align: left; /* Memposisikan teks ke tengah */
            }
        </style>
    """
    
    with col_left:
        with st.expander('Data Analyst Intern - PT Kimia Farma (Nov 2022 - Jan 2023)', expanded=True):
            enter()

            st.subheader('Main Task', divider='gray')
            st.markdown("""
                        ○ Analyzed and created a Looker Studio dashboard to visualize PT Kimia Farma's overall revenue, revenue generated by each branch of the organization, and the number of items sold from January to June 2022.  
                        ○ Designed and implemented a database using PostgreSQL to store the organization's product, customer, and sales data, utilizing a snowflake schema.
                        """, unsafe_allow_html=True)

            enter()
            st.subheader('Dashboard (Looker Studio)', divider='gray')
            logo_link("https://lookerstudio.google.com/s/r50X6KE_Ook", "image/kimia-farma.png", 500)
            enter()
            
            enter()
            st.subheader('Other Information', divider='gray')        
            st.markdown("""
                        → Dashboard: <a href="https://lookerstudio.google.com/s/r50X6KE_Ook">Dashboard Link</a> <br>
                        → Github Repository: <a href="https://github.com/TheOX7/VIX-Big-Data-Analytics---Kimia-Farma">Repository Link</a> <br>
                        → Certificate: <a href="https://drive.google.com/file/d/1dHRnzdhVPgMYSwgU1S0qDjUHKWDRjlVr/view?usp=sharing">e-Certificate</a>
                        """, unsafe_allow_html=True)
            enter()
            
    with col_mid:
        with st.expander('Data Analyst Intern - Ditusi Gaming (Jun - Aug 2023)', expanded=True):
            enter()

            st.subheader('Main Task', divider='gray')
            st.markdown("""
                        ○ Analyzed top 10 popular content and their effectiveness content on their social media platforms based on Engagement Rate Reach (ERR) 
                        and Engagement Rate Post (ERP), reach, likes, new followers, total profile visits, shares, and comments                        
                        ○ Analyzed type of content (such as video, post, vlog, meme, and branding content) on TikTok & Instagram
                        based by reach, likes, new followers, total profile visits, shares, and comments        
                        """, unsafe_allow_html=True)

            enter()

            st.subheader('Other Information', divider='gray')        
            st.markdown("""
                        <b>Certificate</b>
                        → <a href="https://academy.dqlab.id/Certificate_check/result/DQLABCADITUSIDRTGRP#mycertificate">e-Certificate</a> <br>
                        """, unsafe_allow_html=True)
            enter()
            
    with col_right:
        with st.expander('Data Scientist Intern - Kalbe Nutritional (Jun - Aug 2023)', expanded=True):
            enter()

            st.subheader('Main Task', divider='gray')
            st.markdown("""
                        ○ Developed an ARIMA Time Series analysis modelto predict daily total product sales. <br>
                        ○ Designed and created a Tableau dashboard to visualize monthly total quantity, daily total revenue, the number of 
                        products sold per product, and total revenue per Kalbe's store/branch. <br>
                        ○ Created a clustering model to categorize customers into three clusters based on total transactions, 
                        number of products purchased, and expenditure.
                        """, unsafe_allow_html=True)

            enter()
            st.subheader('Dashboard (Tableau)', divider='gray')
            logo_link("https://public.tableau.com/app/profile/marselius.agus.dhion/viz/FinalTask-Kalbe/Dashboard1", "image/kalbe.png", 500)
            enter()
            
            enter()
            st.subheader('Other Information', divider='gray')        
            st.markdown("""
                        → Dashboard: <a href="https://public.tableau.com/app/profile/marselius.agus.dhion/viz/FinalTask-Kalbe/Dashboard1">Dashboard Link</a> <br>
                        → Github Repository: <a href="https://github.com/TheOX7/Final-Task-Kalbe">Repository Link</a> <br>
                        → Certificate: <a href="https://drive.google.com/file/d/14rW6nK_Jpk1o3RPsAxqj5EMm8lvc-xIc/view?usp=sharing">e-Certificate</a>
                        """, unsafe_allow_html=True)
            enter()

enter(); enter(); enter()

with st.container():
    st.markdown("<a id='projects'></a>", unsafe_allow_html=True)
    horizontal_line()
    st.markdown("""
        <div style='text-align: center; font-size:36px'>
            <b>Projects</b> 
        </div>
    """, unsafe_allow_html=True)
    horizontal_line()
    
    enter(); enter()
    with st.expander('Analysis Premier League 2022/23 and Predict Match Result Premier League 2023/24 (Streamlit)', expanded=True):
        col_vid, col_exp = st.columns([1,2])
        with col_vid:
            st.markdown(f'<iframe width="500" height="300" src="https://www.youtube.com/embed/7BpAbtECcPs" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)
            enter()
        with col_exp:
            st.subheader('Explanation', divider='gray')
            st.markdown("""
                        <li>
                            Analyzed Premier League 2022/2023 season statistics, including player stats, club performance, and individual match performance.  
                        </li>
                        <li>
                            Predicted match results for the upcoming 2023/2024 season using a LightGBM model with 83% balanced accuracy.
                        </li>
                        <li>
                            Dataset: Web scraped the data match result from season 2006/07 until 2022/23 from the official Premier League website using Power Automate app
                        </li>
                        <li>
                            <b>Related Links: </b>
                            <a href="https://pl-2022-2023.streamlit.app">Streamlit App</a> | 
                            <a href="https://github.com/TheOX7/Premier-League-Streamlit-Web-App">Github Repository</a>
                        </li>
                        """, unsafe_allow_html=True)
    
    enter()
    
    with st.expander('Dashboard Tingkat Kemiskinan Jawa Barat (Streamlit)', expanded=True):
        col_vid, col_exp = st.columns([1,2])
        with col_vid:
            st.markdown(f'<iframe width="500" height="300" src="https://www.youtube.com/embed/4LMHZzDGklw" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)
            enter()
        with col_exp:
            st.subheader('Explanation', divider='gray')
            st.markdown("""
                        <li>
                            Analyzed and provided recommendations on the "Tingkat Kemiskinan" (poverty rate) in Jawa Barat from 2017 to 2022, including comparisons of poverty levels across cities and regencies, 
                            as well as analyses of the "Indeks Pendidikan" (Education Index) and "Indeks Pembangunan Manusia" (Human Development Index).  
                        </li>
                        <li>
                            Analyzed and provided insights into the Human Development Index (IPM) components, such as "Usia Harapan Hidup" (Life Expectancy), "Harapan Lama Sekolah" (Expected Years of Schooling), 
                            and "Rata-Rata Lama Sekolah" (Average Years of Schooling).
                        </li>
                        <li>
                            Collected and cleaned datasets from BPS Jabar's official website.
                        </li>
                        <li>
                            <b>Related Links: </b>
                            <a href="https://mof-2024-jabar.streamlit.app">Streamlit App</a> | 
                            <a href="https://github.com/TheOX7/MoF-2024">Github Repository</a>
                        </li>
            """, unsafe_allow_html=True)
    
    enter()
    
    with st.expander('Sentiment Analysis on Hotel X\'s user Reviews (Tableau)', expanded=True):
        col_img, col_exp  = st.columns([2,3])
        with col_exp:
            st.subheader('Explanation', divider='gray')
            st.markdown("""
                        <li>
                            Scraped and visualized user reviews from the Play Store & App Store about the hotel's app.
                        </li>
                        <li>
                            Analyzed total number of negative, neutral, and positive reviews for each hotel type to determine which types
                            have more positive reviews than negative and neutral ones, indicating good business for those hotels.            
                        </li>
                        <li>
                            Visualized the top and bottom 10 comments based on the compound score. The VADER model assigned this
                            score, where scores above 0 indicate positive reviews, scores below 0 indicate negative reviews, and a score
                            of 0 indicates neutral reviews.            
                        </li>
                        <li>
                            <b>Related Links: </b>
                            <a href="https://public.tableau.com/app/profile/marselius.agus.dhion/viz/BoboboxSentimentAnalysis/Dashboard">Tableau Dashboard</a> | 
                            <a href="https://github.com/TheOX7/Sentiment-Analysis-Hotel-X">Github Repository</a>
                        </li>
                        """, unsafe_allow_html=True)
            enter()
        with col_img:
            logo_link("https://public.tableau.com/app/profile/marselius.agus.dhion/viz/BoboboxSentimentAnalysis/Dashboard", "image/sentiment-analysis.png", 600)
            enter()
    
    enter()  
    with st.expander('Superstore Sales Dashboard (Tableau)', expanded=True):
        col_img, col_exp = st.columns([1,2])
        with col_img:
            logo_link("https://public.tableau.com/app/profile/mad27/viz/Superstore_16986572902350/Final-Dashboard", "image/superstore.png", 500)
            enter()
        with col_exp:
            st.subheader('Explanation', divider='gray')
            st.markdown("""
                        <li>
                            Analyzed profit & sales per category products, average completion shipment days, total order per
                            weekdays. Also analyzed total profit, sales, & profit ratio for each state.
                        </li>
                        <li>
                            Conducted trend sales, profit, and profit ratio per year.
                        </li>
                        <li>
                            <b>Tableau Dashboard: </b>
                            <a href="https://public.tableau.com/app/profile/mad27/viz/Superstore_16986572902350/Final-Dashboard">Dashboard Link</a>
                        </li>
                        """, unsafe_allow_html=True)
            
    enter()
    with st.expander('Analysis & Prediction of Telco Customer Churn (Tableau)', expanded=True):
        col_img, col_exp = st.columns([1,2])
        with col_img:
            logo_link("https://public.tableau.com/app/profile/mad27/viz/Telco-DataScienceIndonesia/Final-Dashboard", "image/telco.png", 500)
            enter()
            
        with col_exp:
            st.subheader('Explanation', divider='gray')
            st.markdown("""
                        <li>
                            Analyzed the total CLTV (Customer Lifetime Value),number of customers, & total purchases.
                        </li>
                        <li>
                            Visualized incorrectly predicted churn for old customers and incorrectly predicted no churn for new
                            customers based on patterns from a classification model.
                        </li>
                        <li>
                            Explored total payment methods per device class &the total number of customers for each Telco product.
                        </li>
                        
                        <li>
                            <b>Related Links:</b>
                            <a href="https://public.tableau.com/app/profile/mad27/viz/Telco-DataScienceIndonesia/Final-Dashboard">Tableau Dashboard</a> |
                            <a href="https://github.com/sntdshrly/dsw2023">Github Repository</a>
                        </li>
                        """, unsafe_allow_html=True)
