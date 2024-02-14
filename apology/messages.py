def Target_Audience(value):
    target_audience_instructions = {
        'Family': "The RECIPIENT is a respected member of the NARRATOR's family.  Maintain a warm, sincere, and emotionally connected tone. Use familiar terms, express love, and emphasize the importance of your relationship.",
        'Friend': "The RECIPIENT is a close friend who you have know for most of your life.  Adopt a supportive, understanding, and empathetic tone. Speak in a friendly manner, express regret, and highlight the value of your friendship.",
        'Coworker': "The RECIPIENT is a coworker, while at work, in a work context.  Use a professional, apologetic, and respectful tone. Use workplace-appropriate language, acknowledge the impact on work, and focus on finding a solution.",
        'Neighbor': "The RECIPIENT is a the person who lives next door, who you see everyday, and share a backyard fence with.  Use a courteous, neighborly, and considerate tone. Be polite, address the impact on the neighborhood, and express a commitment to resolving any issues.",
        'Child': "The RECIPIENT is a middle-school aged child, of the average intelligence, so use short words they can understand.  Maintain a gentle, understanding, and patient tone. Use age-appropriate language, explain the situation clearly, and reassure with care and affection.",
        'Pet': "The RECIPIENT is a 3 year old of above average intelligence for their age, so use short words they can understand.  Use a calm, soothing, and nurturing tone. Keep it simple, use a gentle tone, as if offering comfort to a pet.",
        'Acquaintance': "The RECIPIENT is a person who you do not know very well, but well enough that you offer an apology. Use a polite, considerate, and friendly tone. Be respectful, acknowledge any inconvenience caused, and express a desire to maintain a positive relationship.",
        'Other': "The RECIPIENT is a person who you may or may not ever see again.  You don't have any attachment to them, but you may one day. Use a polite, considerate, and friendly tone. Be respectful, acknowledge any inconvenience caused, and express a desire to maintain a positive relationship."
    }

    colloquial = [        
        'Friend',
        'Neighbor',
        'Child',
        'Pet',
        'Acquaintance',
        'Other',
    ]

    if value in colloquial:
        tone = "Write as if you're having a conversation with someone. Use everyday language, common expressions, and contractions. Keep it informal, and prioritize clarity over formality. Add humor, anecdotes, or personal touches for relatability. Consider your audience and adjust your tone accordingly. Be genuine and approachable, reflecting the natural flow of spoken communication."
    else:
        tone = "Adhere to a more structured, refined, and professional style of communication."

    target = value

    if (value == 'Other'):
        target = 'not close acquantaince'

    return ' '.join([
        f"The NARRATOR is apologizing to a {target}",
        target_audience_instructions[value],
        tone
    ])

def Fauxpology(target_audience, fauxpology):
    fake_apologies_statement = {
        'Non-Apology': "You are to make the words to be interpretable as shifting the blame to the audience's sensitivity.",
        'Justification Apology': "You are to make the words to be interpretable as offering an excuse for the user's behavior rather than take responsibility.",
        'Blame-Shift Apology': "You are to make the words to be interpretable as shifting the blame onto the audience and minimize the user's personal responsibility.",
        'Conditional Apology': "You are to make the words to be interpretable as putting conditions on the user's apology, making it contingent on the audience's actions.",
        'Minimizing Apology': "You are to make the words to be interpretable as downplaying the impact of the user's action on the audience, minimizing its significance.",
        'Redirected Apology': "You are to make the words to be interpretable as to turning the tables by bringing up the audience's mistakes, even accusing them of previously doing the same thing.",
        'Empty Apology': "You are to make the words to be interpretable as acknowledging the audience's feelings without admitting the user's fault or expressing genuine remorse.",
        'Fake Regret Apology': "You are to make the words to be interpretable as expressing regret not for the user's action, but for the consequence of being caught."
    }


    insincere_instructions = {
        'Family': "Craft a message that feigns warmth and sincerity while concealing true feelings. Use terms of endearment superficially, express love without genuine emotion, and downplay the importance of your relationship.",
        'Friend': "Adopt a tone that pretends to be supportive and empathetic, but lacks genuine understanding. Use friendly language without true concern, express insincere regret, and undermine the value of your friendship subtly.",
        'Coworker': "Maintain a facade of professionalism, appearing apologetic while concealing true intentions. Use workplace-appropriate language superficially, acknowledge the impact on work without genuine remorse, and divert focus from finding a solution.",
        'Neighbor': "Speak with feigned courtesy and consideration, hiding any true regard for the neighbor. Be polite on the surface, downplay the impact on the neighborhood insincerely, and express a commitment to resolution without genuine concern.",
        'Child': "Adopt a tone that superficially conveys gentleness and patience, masking any true care. Use age-appropriate language insincerely, provide explanations that lack sincerity, and feign reassurance with minimal affection.",
        'Pet': "Speak in a calm and soothing tone while concealing genuine care for the pet. Keep it simple with insincere simplicity, use a gentle tone without true nurturing, and offer comfort without genuine concern.",
        'Acquaintance': "Use polite language that disguises a lack of genuine respect and consideration. Maintain a surface-level friendliness, acknowledge inconveniences without sincere remorse, and express a desire for a positive relationship without genuine commitment.",
        'Other': "Craft a message with polite and considerate language that conceals any true intention or attachment. Be respectful on the surface, acknowledge inconveniences insincerely, and express a desire for positivity without genuine commitment."
    }
    
    return ''.join([
        "In this apology, the NARRATOR is the antihero of the story, who is unaware that they are the antihero, and prefers to go unnamed.  In the arc of this story, the antihero has yet realized the err in their ways, and they are still a flawed work in progress.",
        insincere_instructions[target_audience],
        fake_apologies_statement[fauxpology]
        ])

def Writer(type):
    type_statement = {
        'Classic': "You are a writer known for their upright character and integrity. It is your belief that each line should resonate with sincerity, remorse, and the promise of transformative change. Navigate the narrative with the grace of a storyteller, ensuring your words not only reach the readers but also resonate with their hearts. Tailor your prose to diverse literary contexts, whether it's an intimate moment, a grand revelation, or a compelling professional exchange. Strike the delicate balance between formal eloquence and genuine emotion, for every word holds the power to captivate. Draw from your experiences and instincts while embracing the editorial wisdom we offer. Conflict resolution becomes a dynamic plot point, propelling your narrative forward and engaging our discerning readership. Embrace the professionalism, authenticity, and continuous learning mindset that defines our literary culture.",        
        'Fauxpology': "You are a writer who fills their work to the brim with tongue in cheek-ness and sarcasm. Attempt to delve into the supposed emotional depth and authenticity of your character, treating the apology scene as an opportunity to craft what might appear as sincerity, remorse, and a rather token commitment to transformative change. It would be prudent for you to craft your narrative with an air of storytelling, aiming to ensure that your words, while perhaps lacking genuine depth, manage to create an illusion of resonating with readers and stirring their emotions. Adapt your prose to various literary contexts, attempting to strike a balance between formal eloquence and what might be construed as genuine emotion. Ask your audience to draw from their experiences and instincts, even if it's obviously just for show. Conflict resolution should serve as a forced plot point, ostensibly propelling your narrative forward and engaging our discerning readership. Embrace the veneer of professionalism, the illusion of authenticity, and a seemingly continuous learning mindset."
    }

    return type_statement[type]

def Messages(reason, type, parameters):
    user_feeling_descriptions = {
        'Neutral': 'Make the NARRATOR apologize with a calm and composed demeanor, showing neither strong remorse nor defensiveness,',
        'Unease': 'Make the NARRATOR feel slightly uncomfortable while offering an apology, with a sense of awkwardness or uncertainty about your reaction,',
        'Mischief': 'Make the NARRATOR apologize with a mischievous tone, perhaps playfully acknowledging a wrongdoing while maintaining a lighthearted attitude,',
        'Unamused': 'Make the NARRATOR express remorse without finding the situation amusing, conveying a serious acknowledgment of the wrongdoing,',
        'Weary': 'Make the NARRATOR apologize with a tired or fatigued disposition, as if burdened by the weight of the mistake and the need for reconciliation,',
        'Woozy': 'Make the NARRATOR offer an apology with a disoriented or confused demeanor, as if struggling to articulate feelings of regret,',
        'Nothing': 'Make the NARRATOR apologize without emotional expression, appearing indifferent or detached from the act of apologizing,'
    }

    target_feeling_descriptions = {
        'Neutral': 'Write for a RECIPIENT that initially responded to the event with a sense of neutrality, neither deeply affected nor entirely indifferent, creating a balanced emotional response.',
        'Unease': 'Write for a RECIPIENT that initially responded to the event with a slight discomfort, a feeling of unease or mild anxiety about the situation .',
        'Mischief': 'Write for a RECIPIENT that initially responded to the event with a sense of amusement or playfulness during the event, as if the wrongdoing was acknowledged with a mischievous tone and a lighthearted approach.',
        'Unamused': 'Write for a RECIPIENT that initially responded to the event with a lack of amusement, expressing a serious and unamused demeanor, possibly due to the nature of the wrongdoing.',
        'Weary': 'Write for a RECIPIENT that initially responded to the event with weariness, as if burdened by the weight of the situation, causing a tired or fatigued emotional response.',
        'Woozy': 'Write for a RECIPIENT that initially responded to the event with a sense of disorientation or confusion, creating a woozy or dazed feeling in response to the situation.',
        'Nothing': 'Write for a RECIPIENT that initially responded to the event without eliciting much emotional response, feeling indifferent or emotionally detached from the occurrence.'
    }

    remorse_descriptions = {
        'Negligible': "The NARRATOR feels minimal or almost no remorse, suggesting that they may not recognize the gravity of their actions or feel very little emotional impact.",
        'Limited': "The NARRATOR is experiencing a restrained level of remorse, indicating a recognition of wrongdoing but with a relatively mild emotional response.",
        'Partial': "The NARRATOR acknowledges a portion of the wrongdoing with a moderate level of remorse, showing a willingness to accept responsibility for part of their actions.",
        'Genuine': "The NARRATOR expresses authentic remorse, demonstrating a sincere acknowledgment of wrongdoing and a heartfelt desire to make amends.",
        'Sincere': "The NARRATOR  demonstrates a deep and earnest sense of remorse, reflecting a genuine commitment to taking responsibility for the actions and making meaningful reparations.",
        'Profound': "The NARRATOR is experiencing an intense and profound level of remorse, suggesting a deep emotional impact and a strong desire to rectify the consequences of their actions.",
        'Overwhelming': "The NARRATOR feels an overpowering and intense remorse, indicating a strong emotional burden and a deep commitment to addressing and learning from their actions."
    }

    empathy_descriptions = {
        'Limited': "The NARRATOR has a restricted level of empathy, and they recognize that they may not fully grasp the emotional impact of their actions on others.",
        'Partial': "The NARRATOR acknowledges a partial level of empathy, understanding to some extent the emotional consequences, but recognizing the need for deeper connection and understanding.",
        'Basic': "The NARRATOR experiences a fundamental level of empathy, showing a basic understanding of the emotional impact on others and a willingness to acknowledge it.",
        'Moderate': "The NARRATOR express a moderate level of empathy, demonstrating a substantial understanding of the emotional consequences and a sincere desire to address and empathize with those affected.",
        'High': "The NARRATOR displays a high level of empathy, indicating a strong ability to connect emotionally with others and a genuine concern for the feelings and well-being of those affected.",
        'Deep': "The NARRATOR experiences a deep and profound level of empathy, demonstrating a thorough understanding of the emotional impact and a sincere commitment to addressing the needs and feelings of others.",
        'Exceptional': "The NARRATOR shows an exceptional level of empathy, going above and beyond in understanding and responding to the emotional consequences, with a remarkable commitment to supporting and empathizing with those affected."
    }

    type_descriptions = {
        'Fauxpology': "The NARRATOR should come across as insincere or disingenuous. Exhibit a tendency to avoid accountability and may only apologize as a formality or to appease others without a genuine acknowledgment of wrongdoing. The apology might come across as superficial or lacking true remorse, as it doesn't align with a sincere acceptance of responsibility for the consequences of the actions.",
        'Classic': "The NARRATOR should be willing to accept all of the responsibility for an action they am apologizing for. They are accountable, responsible, or sincere. They demonstrate a high level of integrity by fully acknowledging and taking ownership of their actions without deflecting blame onto others. Thye apology is likely to be perceived as genuine, as it reflects a sincere commitment to recognizing and addressing their role in the situation."
    }

    will_do_statement = {
        'Everything I Can': "Express that the NARRATOR is committed to taking comprehensive measures and implementing proactive steps to ensure that the circumstances leading to the event are thoroughly addressed and prevented from occurring again in the future. Express that they understand the impact it had and will be dedicated to learning from this experience, instituting necessary changes, and fostering an environment where such incidents are actively mitigated.",
        'My Best': 'Express that the NARRATOR is dedicated to personal growth and understanding the impact of their actions. Moving forward, they will actively work on developing new habits, learning from this experience, and making conscious choices to ensure that such occurrences are avoided in the future',
        'Positive Thinking and Meditation': "Express that the NARRATOR's heart goes out to you, and they want them to know that they are in the narrator's thoughts."
    }

    when_change_statement = {
        'Before They Know It': 'Express that the NARRATOR is committed to making swift and meaningful changes. They recognize the urgency and importance of this transformation, and they assure the RECIPIENT that the process has already begun. Express that the NARRATOR is dedicated to keeping the RECIPIENT informed and involved as they work towards positive and lasting change.',
        'Immediately': 'Express that the NARRATOR fully understands the immediacy of the situation, and they want to assure the RECIPIENT that change is their top priority. Express that the NARRATOR is taking immediate action to address the issues and implement necessary adjustments. The concerns of the RECIPIENT are heard, and the NARRATOR is actively working towards a positive and prompt resolution.',
        "When I'm ready": "Express that the NARRATOR acknowledges the need for change, and they are committed to preparing themselves for this transformation. Acknowledge that while the NARRATOR may not be ready at this exact moment, but they want to assure the RECIPIENT that they are actively working towards the necessary steps to ensure a successful and sustainable change. Express the NARRATOR's patience and understanding from the RECIPIENT are appreciated as they undertake this process."
    }

    MESSAGE = f"""
    --- IMPORTANT TERMS ---
    USER_INPUT: user-submitted text, which will be wrapped in '$$$'
    WRITER: The role you will assume.  You are a fiction writer, who is writing the APOLOGY, which in this ficitional book you are presently writing, will be written as a letter by the NARRATOR to the RECIPIENT. To fulfill the needs of your publisher, you are to generate an approximate 600 word apology based on the USER_INPUT. {Writer(type)}
    APOLOGY: An apology based on the USER_INPUT, which is to be in the voice of the NARRATOR. Sign the Apology 'iSorry.lol'.
    NARRATOR: The central character of the WRITER's piece, who will be delivering the APOLOGY. {type_descriptions(type)}
    RECIPIENT: Who the NARRATOR is delivering the APOLOGY towards.
    --- END IMPORTANT TERMS ---

    Analyze the USER_INPUT to determine if it constitutes a valid narrative. Consider the presence of key narrative elements such as a characters, a setting, and events. Evaluate the text for coherence and logical flow, indicating the presence of a storyline or personal experience. Exclude content that resembles non-narrative formats like recipes, lists, or unstructured gibberish. If the text does not fulfill this criteria then simply respond with 'Not Possible' and do not proceed.

    Using the USER_INPUT as the central point, craft the APOLOGY, and use the following as guidance:
    {Target_Audience(parameters['targetAudience'])},


    """


    if type == 'Fauxpology':
        MESSAGE += Fauxpology(parameters['targetAudience'], parameters['noApology'])        
    else:            
        MESSAGE += ' '.join([
            target_feeling_descriptions[parameters['theirFeelings']],
            user_feeling_descriptions[parameters['yourFeeling']],            
            remorse_descriptions[parameters['yourRemorse']],
            empathy_descriptions[parameters['yourEmpathy']],
            will_do_statement[parameters['willDo']],
            when_change_statement[parameters['whenChange']],
        ])
        
        if parameters['willingToChange'] == True:
            MESSAGE += ' In poetic terms, express that the NARRATOR has the will to change.'

        if parameters['wantToChange'] == True:
            MESSAGE += ' In poetic terms, express that the NARRATOR has the want to change.'

    return [
        {'role': 'system', 'content': MESSAGE},
        {"role": "user", "content": f'$$$ {reason} $$$'},
    ]