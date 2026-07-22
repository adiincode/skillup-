import pandas as pd
import random
import os

# -------------------------------
# Create data folder
# -------------------------------
os.makedirs("data", exist_ok=True)

# -------------------------------
# Skills Dataset
# -------------------------------
skills = [
    ("Python","Programming"),("Java","Programming"),("C++","Programming"),
    ("C","Programming"),("JavaScript","Programming"),
    ("SQL","Database"),("MongoDB","Database"),("MySQL","Database"),
    ("PostgreSQL","Database"),("HTML","Web"),("CSS","Web"),
    ("React","Web"),("Node.js","Web"),("Express.js","Web"),
    ("Django","Backend"),("Flask","Backend"),
    ("Git","Tools"),("GitHub","Tools"),
    ("Docker","DevOps"),("Kubernetes","DevOps"),
    ("AWS","Cloud"),("Azure","Cloud"),("GCP","Cloud"),
    ("Linux","OS"),("Bash","OS"),
    ("Machine Learning","AI"),("Deep Learning","AI"),
    ("NLP","AI"),("Computer Vision","AI"),
    ("TensorFlow","AI"),("PyTorch","AI"),
    ("Scikit-learn","AI"),
    ("Pandas","Data"),("NumPy","Data"),
    ("Matplotlib","Data"),("Seaborn","Data"),
    ("Power BI","Analytics"),("Excel","Analytics"),
    ("Data Analysis","Analytics"),
    ("DSA","Core"),("OOP","Core"),
    ("System Design","Core"),
    ("Operating Systems","Core"),
    ("DBMS","Core"),
    ("Computer Networks","Core"),
    ("Cyber Security","Security"),
    ("Android","Mobile"),
    ("Kotlin","Mobile"),
    ("Communication","Soft Skill"),
    ("Problem Solving","Soft Skill")
]

skills_df = pd.DataFrame(
    [(i+1, s[0], s[1]) for i, s in enumerate(skills)],
    columns=["skill_id","skill_name","category"]
)

skills_df.to_csv("data/skills.csv", index=False)

# -------------------------------
# Career Roles
# -------------------------------

career_roles = {

"Software Engineer":[
("Python",1.0),("DSA",1.0),("OOP",0.9),
("DBMS",0.8),("SQL",0.8),
("System Design",0.8),("Git",0.7)
],

"Data Scientist":[
("Python",1.0),("Pandas",1.0),
("NumPy",1.0),("Machine Learning",1.0),
("Scikit-learn",0.9),
("SQL",0.8),("Power BI",0.7)
],

"ML Engineer":[
("Python",1.0),
("Machine Learning",1.0),
("Deep Learning",1.0),
("TensorFlow",0.9),
("PyTorch",0.9),
("NLP",0.8),
("Computer Vision",0.8)
],

"Web Developer":[
("HTML",1.0),("CSS",1.0),
("JavaScript",1.0),
("React",0.9),
("Node.js",0.8),
("Express.js",0.7),
("Git",0.7)
],

"Android Developer":[
("Kotlin",1.0),
("Android",1.0),
("Git",0.8),
("Java",0.8)
],

"DevOps Engineer":[
("Docker",1.0),
("Kubernetes",1.0),
("AWS",1.0),
("Linux",0.9),
("Bash",0.8)
],

"Cyber Security Analyst":[
("Linux",1.0),
("Cyber Security",1.0),
("Python",0.8),
("Computer Networks",0.8)
]

}

career_data=[]

for role,skills_required in career_roles.items():
    for skill,importance in skills_required:
        career_data.append([role,skill,importance])

career_df=pd.DataFrame(
career_data,
columns=["role","required_skill","importance"]
)

career_df.to_csv("data/career_roles.csv",index=False)

# -------------------------------
# Learning Resources
# -------------------------------

resource_data=[]

for skill in skills_df["skill_name"]:

    resource_data.append([
        skill,
        "YouTube",
        f"{skill} Full Course",
        "Beginner"
    ])

    resource_data.append([
        skill,
        "Official Docs",
        f"{skill} Documentation",
        "Intermediate"
    ])

learning_df=pd.DataFrame(
resource_data,
columns=["skill","platform","resource","difficulty"]
)

learning_df.to_csv("data/learning_resources.csv",index=False)

# -------------------------------
# Users Dataset
# -------------------------------

colleges=[
"RRGI Lucknow",
"NIT Trichy",
"NIT Surat",
"IIT Kanpur",
"AKGEC",
"IIIT Lucknow"
]

branches=[
"CSE",
"AIML",
"IT",
"ECE"
]

roles=list(career_roles.keys())

users=[]

for i in range(1,501):

    users.append([
        i,
        f"Student_{i}",
        random.choice(colleges),
        random.choice(branches),
        random.randint(1,4),
        random.choice(roles)
    ])

users_df=pd.DataFrame(
users,
columns=[
"user_id",
"name",
"college",
"branch",
"year",
"target_role"
]
)

users_df.to_csv("data/users.csv",index=False)

# -------------------------------
# User Skills Dataset
# -------------------------------

levels=["Beginner","Intermediate","Advanced"]

user_skill_data=[]

all_skills=list(skills_df["skill_name"])

for uid in users_df["user_id"]:

    selected=random.sample(all_skills,random.randint(5,10))

    for skill in selected:

        user_skill_data.append([
            uid,
            skill,
            random.choice(levels)
        ])

user_skill_df=pd.DataFrame(
user_skill_data,
columns=[
"user_id",
"skill",
"level"
]
)

user_skill_df.to_csv(
"data/user_skills.csv",
index=False
)

# -------------------------------
# Peer Dataset
# -------------------------------

peer=[]

for i in range(1000):

    peer.append([
        random.choice(colleges),
        random.choice(branches),
        random.randint(1,4),
        random.choice(all_skills)
    ])

peer_df=pd.DataFrame(
peer,
columns=[
"college",
"branch",
"year",
"skill"
]
)

peer_df.to_csv(
"data/peer_data.csv",
index=False
)

print("="*50)
print("🎉 Dataset Generated Successfully!")
print("="*50)

print("Files Created:")

print("✔ skills.csv")
print("✔ career_roles.csv")
print("✔ learning_resources.csv")
print("✔ users.csv")
print("✔ user_skills.csv")
print("✔ peer_data.csv")
print("="*50)