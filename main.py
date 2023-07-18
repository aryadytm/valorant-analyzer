import streamlit as st
import os
import time


agents = ["[NONE]", "Astra", "Breach", "Brimstone", "Chamber", "Cypher", "Deadlock", "Fade", "Gekko", "Harbor", "Jett", "KAY/O", "Killjoy", "Neon", "Omen", "Phoenix", "Raze", "Reyna", "Sage", "Skye", "Sova", "Viper", "Yoru"]

abilities = ["Traps", "Smoke", "Soft Recon", "Hard Recon", "Drone", "Pop Flash", "Nearsight", "Stun", "Wall", "Quick Reposition"]

agent_abilities = {
    "[NONE]": [],
    "Astra": ["Smoke", "Stun"],
    "Breach": ["Stun", "Pop Flash"],
    "Brimstone": ["Smoke"],
    "Chamber": ["Traps", "Quick Reposition"],
    "Cypher": ["Traps", "Soft Recon"],
    "Deadlock": ["Traps", "Wall"],
    "Fade": ["Hard Recon", "Soft Recon", "Stun"],
    "Gekko": ["Soft Recon", "Stun", "Nearsight"],
    "Harbor": ["Smoke"],
    "Jett": ["Quick Reposition"],
    "KAY/O": ["Pop Flash", "Hard Recon"],
    "Killjoy": ["Traps", "Soft Recon"],
    "Neon": ["Quick Reposition", "Stun"],
    "Omen": ["Nearsight", "Smoke", "Quick Reposition"],
    "Phoenix": ["Pop Flash"],
    "Raze": ["Quick Reposition", "Soft Recon"],
    "Reyna": ["Nearsight"],
    "Sage": ["Wall"],
    "Skye": ["Soft Recon", "Pop Flash", "Drone", "Stun"],
    "Sova": ["Hard Recon", "Drone"],
    "Viper": ["Smoke"],
    "Yoru": ["Pop Flash", "Quick Reposition"]
}


def analyze(agents: list[str]) -> str:
    strengths = {}
    weaknesses = set(abilities)
    
    for agent in agents:
        for ability in agent_abilities[agent]:
            if ability in strengths:
                strengths[ability].append(agent)
            else:
                strengths[ability] = [agent]
            
            weaknesses.discard(ability)
    
    result = "Strength:\n"
    
    for ability, agents in strengths.items():
        result += f"- {ability} ({', '.join(agents)})\n"
    
    result += "\nWeakness:\n"
    
    for weakness in weaknesses:
        result += f"- {weakness}\n"
    
    return result



def main():
    
    # result = analyze(["Reyna", "Jett", "Brimstone", "Sage", "Chamber"])
    # print(result)
    # return

    st.write("# VALORANT Analyzer")
    
    st.write("## Enemy Team")
    enemy_1 = st.selectbox("Enemy 1", options=agents)
    enemy_2 = st.selectbox("Enemy 2", options=agents)
    enemy_3 = st.selectbox("Enemy 3", options=agents)
    enemy_4 = st.selectbox("Enemy 4", options=agents)
    enemy_5 = st.selectbox("Enemy 5", options=agents)
    
    st.write("## Your Team")
    you_1 = st.selectbox("You 1", options=agents)
    you_2 = st.selectbox("You 2", options=agents)
    you_3 = st.selectbox("You 3", options=agents)
    you_4 = st.selectbox("You 4", options=agents)
    you_5 = st.selectbox("You 5", options=agents)
    
    agents_enemy = [enemy_1, enemy_2, enemy_3, enemy_4, enemy_5]
    agents_you =  [you_1, you_2, you_3, you_4, you_5]
    
    if st.button("Analyze"):
        result_enemy = analyze(agents_enemy)
        result_you = analyze(agents_you)
        
        st.write("## Analysis Result")
        
        st.write("### Enemy Team")
        st.write(result_enemy)
        
        st.write("### Your Team")
        st.write(result_you)


if __name__ == "__main__":
    main()

