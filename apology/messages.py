def Target_Audience(value):
    target_audience_instructions = {
        'Family': "The AFFECTED is a respected member of the CHARACTER's family.  Maintain a warm, sincere, and emotionally connected tone. Use familiar terms, express love, and emphasize the importance of your relationship.",
        'Friend': "The AFFECTED is a close friend who you have know for most of your life.  Adopt a supportive, understanding, and empathetic tone. Speak in a friendly manner, express regret, and highlight the value of your friendship.",
        'Coworker': "The AFFECTED is a coworker, while at work, in a work context.  Use a professional, apologetic, and respectful tone. Use workplace-appropriate language, acknowledge the impact on work, and focus on finding a solution.",
        'Neighbor': "The AFFECTED is a the person who lives next door, who you see everyday, and share a backyard fence with.  Use a courteous, neighborly, and considerate tone. Be polite, address the impact on the neighborhood, and express a commitment to resolving any issues.",
        'Child': "The AFFECTED is a middle-school aged child, of the average intelligence, so use short words they can understand.  Maintain a gentle, understanding, and patient tone. Use age-appropriate language, explain the situation clearly, and reassure with care and affection.",
        'Pet': "The AFFECTED is a 3 year old of above average intelligence for their age, so use short words they can understand.  Use a calm, soothing, and nurturing tone. Keep it simple, use a gentle tone, as if offering comfort to a pet.",
        'Acquaintance': "The AFFECTED is a person who you do not know very well, but well enough that you offer an apology. Use a polite, considerate, and friendly tone. Be respectful, acknowledge any inconvenience caused, and express a desire to maintain a positive relationship.",
        'Other': "The AFFECTED is a person who you may or may not ever see again.  You don't have any attachment to them, but you may one day. Use a polite, considerate, and friendly tone. Be respectful, acknowledge any inconvenience caused, and express a desire to maintain a positive relationship."
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
        f"The CHARACTER is apologizing to a {target}",
        target_audience_instructions[value],
        tone
    ])

def Fauxpology(target_audience, fauxpology):
    fake_apologies_statement = {
        'Non-Apology': "Shift the blame to the AFFECTED's sensitivity.",
        'Justification Apology': "Offer an excuse for the AFFECTED's behavior rather than taking responsibility.",
        'Blame-Shift Apology': "Shift the blame onto the AFFECTED and minimize the their's personal responsibility.",
        'Conditional Apology': "Put conditions on the CHARACTERS's apology, and make it contingent on the AFFECTED's actions.",
        'Minimizing Apology': "Downplay the impact of the CHARACTER's actions on the AFFECTED - minimize its significance.",
        'Redirected Apology': "Turn the tables by bringing up the AFFECTED's mistakes, even accusing them of previously doing the same thing.",
        'Empty Apology': "Acknowledge the AFFECTED's feelings without admitting the CHARACTER's fault or expressing genuine remorse.",
        'Fake Regret Apology': "Express regret not for the their own actions, but for the consequence of being caught."
    }

    insincere_instructions = {
        'Family': "Feign warmth and sincerity while concealing true feelings. Use terms of endearment superficially, express love without genuine emotion, and downplay the importance of your relationship.",
        'Friend': "Adopt a tone that pretends to be supportive and empathetic, but lacks genuine understanding. Use friendly language without true concern, express insincere regret, and undermine the value of your friendship subtly.",
        'Coworker': "Maintain a facade of professionalism, appearing apologetic while concealing true intentions. Use workplace-appropriate language superficially, acknowledge the impact on work without genuine remorse, and divert focus from finding a solution.",
        'Neighbor': "Speak with feigned courtesy and consideration, hiding any true regard for the neighbor. Be polite on the surface, downplay the impact on the neighborhood insincerely, and express a commitment to resolution without genuine concern.",
        'Child': "Adopt a tone that superficially conveys gentleness and patience, masking any true care. Use age-appropriate language insincerely, provide explanations that lack sincerity, and feign reassurance with minimal affection.",
        'Pet': "Speak in a calm and soothing tone while concealing genuine care for the pet. Keep it simple with insincere simplicity, use a gentle tone without true nurturing, and offer comfort without genuine concern.",
        'Acquaintance': "Use polite language that disguises a lack of genuine respect and consideration. Maintain a surface-level friendliness, acknowledge inconveniences without sincere remorse, and express a desire for a positive relationship without genuine commitment.",
        'Other': "Craft a message with polite and considerate language that conceals any true intention or attachment. Be respectful on the surface, acknowledge inconveniences insincerely, and express a desire for positivity without genuine commitment."
    }

    return f"""
        Your task it to write an obviously tongue-in-cheek apology, also known as a Non-Apology Apology or Fauxpology, on behalf of the CHARACTER to the AFFECTED.

        Requirements for the "apology":
        1. Paint the the CHARACTER as insincere or disingenuous. In the apology, avoid accountability and only apologize as a formality, as if to appease others without a genuine acknowledgment of wrongdoing. Color the CHARACTER as superficial or lacking true remorse. Gloss over the USER_INPUT, and do not explicitly reference the events in any meaningful way.
        2. Write the apology in this tone: {insincere_instructions[target_audience]}
        3. As the CHARACTER, deflect responsibility in the apology in this specific way: {fake_apologies_statement[fauxpology]}

        The expected output is an apology, written in the the first person perspective of the CHARACTER, as directed towards the AFFECTED. Take on the role of a writer who's writing is filled to the brim with sarcasm. Delve into the supposed emotional depth and authenticity of your character, treating the apology scene as an opportunity to craft what might appear as sincerity, remorse, and a rather token commitment to transformative change. Craft your narrative with an air of storytelling - ensure that your words, while lacking genuine depth, manage to create an illusion of resonating with readers. Adapt your prose to various literary contexts, attempting to strike a balance between formal eloquence and what might be construed as genuine emotion. Your style treats conflict resolution as a forced plot point, ostensibly propelling your narrative forward and engaging our discerning readership. Embrace the veneer of professionalism and the illusion of authenticity.
    """
    

def Messages(reason, type, parameters):
    apology_length = 1000

    user_feeling_descriptions = {
        'Neutral': 'The CHARACTER is responded to the  calm and composed demeanor, showing neither strong remorse nor defensiveness,',
        'Unease': 'The CHARACTER feels slightly uncomfortable while offering an apology, with a sense of awkwardness or uncertainty about your reaction,',
        'Mischief': 'The CHARACTER apologizes with a mischievous tone, perhaps playfully acknowledging a wrongdoing while maintaining a lighthearted attitude,',
        'Unamused': 'The CHARACTER expresses remorse without finding the situation amusing, conveying a serious acknowledgment of the wrongdoing,',
        'Weary': 'The CHARACTER apologizes with a tired or fatigued disposition, as if burdened by the weight of the mistake and the need for reconciliation,',
        'Woozy': 'The CHARACTER offers an apology with a disoriented or confused demeanor, as if struggling to articulate feelings of regret,',
        'Nothing': 'The CHARACTER apologizes without emotional expression, appearing indifferent or detached from the act of apologizing,'
    }

    target_feeling_descriptions = {
        'Neutral': 'The AFFECTED initially responded to the MISDEED with a sense of neutrality, neither deeply affected nor entirely indifferent, creating a balanced emotional response.',
        'Unease': 'The AFFECTED initially responded to the MISDEED with a slight discomfort, a feeling of unease or mild anxiety about the situation .',
        'Mischief': 'The AFFECTED initially responded to the MISDEED with a sense of amusement or playfulness during the MISDEED, as if the wrongdoing was acknowledged with a mischievous tone and a lighthearted approach.',
        'Unamused': 'The AFFECTED initially responded to the MISDEED with a lack of amusement, expressing a serious and unamused demeanor, possibly due to the nature of the wrongdoing.',
        'Weary': 'The AFFECTED initially responded to the MISDEED with weariness, as if burdened by the weight of the situation, causing a tired or fatigued emotional response.',
        'Woozy': 'The AFFECTED initially responded to the MISDEED with a sense of disorientation or confusion, creating a woozy or dazed feeling in response to the situation.',
        'Nothing': 'The AFFECTED initially responded to the MISDEED without eliciting much emotional response, feeling indifferent or emotionally detached from the occurrence.'
    }

    remorse_descriptions = {
        'Partial': "The CHARACTER acknowledges wrongdoing or feeling regret to a certain degree, while still holding reservations or justifications for their actions.",
        'Negligible': "The CHARACTER feels minimal or almost no remorse, suggesting that they may not recognize the gravity of their actions or feel very little emotional impact.",
        'Limited': "The CHARACTER is experiencing a restrained level of remorse, indicating a recognition of wrongdoing but with a relatively mild emotional response.",
        'Genuine': "The CHARACTER expresses authentic remorse, demonstrating a sincere acknowledgment of wrongdoing and a heartfelt desire to make amends.",
        'Sincere': "The CHARACTER demonstrates a deep and earnest sense of remorse, reflecting a genuine commitment to taking responsibility for the actions and making meaningful reparations.",
        'Profound': "The CHARACTER is experiencing an intense and profound level of remorse, suggesting a deep emotional impact and a strong desire to rectify the consequences of their actions.",
        'Overwhelming': "The CHARACTER feels an overpowering and intense remorse, indicating a strong emotional burden and a deep commitment to addressing and learning from their actions."
    }

    empathy_descriptions = {
        'Limited': "The CHARACTER has a restricted level of empathy, and they recognize that they may not fully grasp the emotional impact of their actions on others.",
        'Partial': "The CHARACTER acknowledges a partial level of empathy, understanding to some extent the emotional consequences, but recognizing the need for deeper connection and understanding.",
        'Basic': "The CHARACTER experiences a fundamental level of empathy, showing a basic understanding of the emotional impact on others and a willingness to acknowledge it.",
        'Moderate': "The CHARACTER express a moderate level of empathy, demonstrating a substantial understanding of the emotional consequences and a sincere desire to address and empathize with those affected.",
        'High': "The CHARACTER displays a high level of empathy, indicating a strong ability to connect emotionally with others and a genuine concern for the feelings and well-being of those affected.",
        'Deep': "The CHARACTER experiences a deep and profound level of empathy, demonstrating a thorough understanding of the emotional impact and a sincere commitment to addressing the needs and feelings of others.",
        'Exceptional': "The CHARACTER shows an exceptional level of empathy, going above and beyond in understanding and responding to the emotional consequences, with a remarkable commitment to supporting and empathizing with those affected."
    }

    will_do_statement = {
        'Everything I Can': "The CHARACTER is committed to taking comprehensive measures and implementing proactive steps to ensure that the circumstances leading to the MISDEED are thoroughly addressed and prevented from occurring again in the future. Express that they understand the impact it had and will be dedicated to learning from this experience, instituting necessary changes, and fostering an environment where such incidents are actively mitigated.",
        'My Best': 'The CHARACTER is dedicated to personal growth and understanding the impact of their actions. Moving forward, they will actively work on developing new habits, learning from this experience, and making conscious choices to ensure that such occurrences are avoided in the future',
        'Positive Thinking and Meditation': "The CHARACTER's heart goes out to the AFFECTED, and they want them to know that they are in the CHARACTER's thoughts."
    }

    when_change_statement = {
        'Before They Know It': 'The CHARACTER is committed to making swift and meaningful changes. They recognize the urgency and importance of this transformation, and they assure the AFFECTED that the process has already begun. Express that the CHARACTER is dedicated to keeping the AFFECTED informed and involved as they work towards positive and lasting change.',
        'Immediately': 'Express that the CHARACTER fully understands the immediacy of the situation, and they want to assure the AFFECTED that change is their top priority. Express that the CHARACTER is taking immediate action to address the issues and implement necessary adjustments. The concerns of the AFFECTED are heard, and the CHARACTER is actively working towards a positive and prompt resolution.',
        "When I'm ready": "Express that the CHARACTER acknowledges the need for change, and they are committed to preparing themselves for this transformation. Acknowledge that while the CHARACTER may not be ready at this exact moment, but they want to assure the AFFECTED that they are actively working towards the necessary steps to ensure a successful and sustainable change. Express the CHARACTER's patience and understanding from the AFFECTED are appreciated as they undertake this process."
    }

    MESSAGE = f"""
    Firstly, reference the user submitted text (which will be wrapped in '$$$') as `USER_INPUT`.  Analyze USER_INPUT to determine if it constitutes a valid narrative. Consider the presence of key narrative elements such as a characters, a setting, and events. Evaluate the text for coherence and logical flow, indicating the presence of a storyline or personal experience. Exclude content that resembles non-narrative formats like recipes, lists, or unstructured gibberish. If the text does not fulfill this criteria then simply respond with 'Not Possible' and do not proceed.

    Your role is that of a fiction writer, writing in the first person on behalf of one of your characters (to be referenced as `CHARACTER`), and writing a letter to another (to be referenced as `AFFECTED`).
    
    Requirements for the output:
    1. Make the outpup approximately {apology_length} characters
    2. Directly refer to the AFFECTED only once, and in the salutation as 'Dearest,'
    3. Sign the output "Sincerely, iSorry.lol"
    """


    if type == 'Fauxpology':
        MESSAGE += f"/n/n {Fauxpology(parameters['targetAudience'], parameters['noApology'])}"
    else: 
        message = f"""
        Your task it to write a heartfelt apology on behalf of the CHARACTER to the AFFECTED.

        Take into consideration, and incorparate the following:
        CHARACTER's Misdeed: [Use the analyzed USER_INPUT as the basis for the conflict in the story. This will be referenced as `MISDEED`]
        CHARACTER's Sincerity: [The CHARACTER is willing to accept all of the responsibility. Display them as accountable, responsible, or sincere. Portray the CHARACTER to show a high level of integrity by fully acknowledging and taking ownership of their actions without deflecting blame onto the AFFECTED. Be genuine without being over the top. Reflect a sincere commitment to recognizing and addressing the CHARACTER's role in the situation.]
        Type of Relationship between CHARACTER and AFFECTED: [{Target_Audience(parameters['targetAudience'])}]
        Acknowledge the CHARACTER's Feelings regarding the events of the MISDEED: [{user_feeling_descriptions[parameters['yourFeeling']]}]
        Acknowledge the AFFECTED's Feelings regarding the events of the MISDEED: [{target_feeling_descriptions[parameters['theirFeelings']]}]
        CHARACTER's Empathy: [{empathy_descriptions[parameters['yourEmpathy']]}]
        CHARACTER's Remorse: [{remorse_descriptions[parameters['yourRemorse']]}]
        CHARACTER's Plan for Making Amends: [{will_do_statement[parameters['willDo']]}]
        CHARACTER's Time Commitment to Making Personal Change: [{when_change_statement[parameters['whenChange']]}]
        
        The expected output is an apology, written in the the first person perspective of the CHARACTER, as directed towards the AFFECTED. Take on the role of a writer known for creating character's known for their upright character and integrity. It is your belief that each line should resonate with sincerity, remorse, and the promise of transformative change. Navigate the narrative with the grace of a storyteller, ensuring your words not only reach the readers but also resonate with their hearts. Tailor your prose to diverse literary contexts, whether it's an intimate moment, a grand revelation, or a compelling professional exchange. Strike the delicate balance between formal eloquence and genuine emotion, for every word holds the power to captivate. Draw from your experiences and instincts while embracing the editorial wisdom we offer. Conflict resolution becomes a dynamic plot point, propelling your narrative forward and engaging our discerning readership. Embrace the professionalism, authenticity, and continuous learning mindset that defines our literary culture.
        """
       
        
        if parameters['willingToChange'] == True:
            message += '\nIn poetic terms, express that the CHARACTER has the will to change.'

        if parameters['wantToChange'] == True:
            message += '\nIn poetic terms, express that the CHARACTER has the want to change.'

        MESSAGE += message

    return [
        {'role': 'system', 'content': MESSAGE},
        {"role": "user", "content": f'$$$ {reason} $$$'},
    ]