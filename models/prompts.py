def build_prompt(profile, context, tone):
    return f"""
You are a college admissions expert.

Student Profile:
- Interests: {profile['interests']}
- Achievements: {profile['achievements']}
- Challenges: {profile['challenges']}
- Goals: {profile['goals']}

Context:
{context}

Instructions:
1. Generate 3 story ideas
2. Create an outline
3. Write a 500-word essay

Tone: {tone}
"""