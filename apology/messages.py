def Messages(reason, type, parameters):
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


    user_feeling_descriptions = {
        'Neutral': 'I apologize with a calm and composed demeanor, showing neither strong remorse nor defensiveness,',
        'Unease': 'I feel slightly uncomfortable while offering an apology, with a sense of awkwardness or uncertainty about your reaction,',
        'Mischief': 'I apologize with a mischievous tone, perhaps playfully acknowledging a wrongdoing while maintaining a lighthearted attitude,',
        'Unamused': 'I express remorse without finding the situation amusing, conveying a serious acknowledgment of the wrongdoing,',
        'Weary': 'I apologize with a tired or fatigued disposition, as if burdened by the weight of the mistake and the need for reconciliation,',
        'Woozy': 'I offer an apology with a disoriented or confused demeanor, as if struggling to articulate feelings of regret,',
        'Nothing': 'I apologize without emotional expression, appearing indifferent or detached from the act of apologizing,'
    }

    target_feeling_descriptions = {
        'Neutral': 'The target of the apology responded to the event with a sense of neutrality, neither deeply affected nor entirely indifferent, creating a balanced emotional response.',
        'Unease': 'The target of the apology experienced a slight discomfort during the event, generating a feeling of unease or mild anxiety about the situation or the sincerity of the apology.',
        'Mischief': 'The target of the apology felt a sense of amusement or playfulness during the event, as if the wrongdoing was acknowledged with a mischievous tone and a lighthearted approach.',
        'Unamused': 'The target of the apology reacted with a lack of amusement or amusement during the event, expressing a serious and unamused demeanor, possibly due to the nature of the wrongdoing.',
        'Weary': 'The target of the apology responded to the event with weariness, as if burdened by the weight of the situation, causing a tired or fatigued emotional response.',
        'Woozy': 'The target of the apology experienced a sense of disorientation or confusion during the event, creating a woozy or dazed feeling in response to the situation.',
        'Nothing': 'The target of the apology responded to the event without eliciting much emotional response, feeling indifferent or emotionally detached from the occurrence.'
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


    type_descriptions = {
        'None': "I am insincere or disingenuous. I exhibit a tendency to avoid accountability and may only apologize as a formality or to appease others without a genuine acknowledgment of my wrongdoing. My apology might come across as superficial or lacking true remorse, as it doesn't align with a sincere acceptance of responsibility for the consequences of my actions.",
        'Half': "I am only willing to take half of the responsibility for an action I am apologizing for. I acknowledge my involvement in the situation but fall short of accepting full responsibility, suggesting that I attribute some of the blame to others or external factors. My apology might be perceived as incomplete or lacking in genuine remorse, as it reflects a partial acknowledgment of my role in the matter.",
        'Full': "I am willing to accept all of the responsibility for an action I am apologizing for. I am accountable, responsible, or sincere. I demonstrate a high level of integrity by fully acknowledging and taking ownership of my actions without deflecting blame onto others. My apology is likely to be perceived as genuine, as it reflects a sincere commitment to recognizing and addressing my role in the situation."
    }

    remorse_descriptions = {
        'Negligible': "I feel minimal or almost no remorse, suggesting that I may not recognize the gravity of my actions or feel very little emotional impact.",
        'Limited': "I am experiencing a restrained level of remorse, indicating a recognition of my wrongdoing but with a relatively mild emotional response.",
        'Partial': "I acknowledge a portion of the wrongdoing with a moderate level of remorse, showing a willingness to accept responsibility for part of my actions.",
        'Genuine': "I express authentic remorse, demonstrating a sincere acknowledgment of my wrongdoing and a heartfelt desire to make amends.",
        'Sincere': "I demonstrate a deep and earnest sense of remorse, reflecting a genuine commitment to taking responsibility for my actions and making meaningful reparations.",
        'Profound': "I am experiencing an intense and profound level of remorse, suggesting a deep emotional impact and a strong desire to rectify the consequences of my actions.",
        'Overwhelming': "I feel an overpowering and intense remorse, indicating a strong emotional burden and a deep commitment to addressing and learning from my actions."
    }

    empathy_descriptions = {
        'Limited': "I have a restricted level of empathy, and I recognize that I may not fully grasp the emotional impact of my actions on others.",
        'Partial': "I acknowledge a partial level of empathy, understanding to some extent the emotional consequences, but recognizing the need for deeper connection and understanding.",
        'Basic': "I experience a fundamental level of empathy, showing a basic understanding of the emotional impact on others and a willingness to acknowledge it.",
        'Moderate': "I express a moderate level of empathy, demonstrating a substantial understanding of the emotional consequences and a sincere desire to address and empathize with those affected.",
        'High': "I display a high level of empathy, indicating a strong ability to connect emotionally with others and a genuine concern for the feelings and well-being of those affected.",
        'Deep': "I experience a deep and profound level of empathy, demonstrating a thorough understanding of the emotional impact and a sincere commitment to addressing the needs and feelings of others.",
        'Exceptional': "I show an exceptional level of empathy, going above and beyond in understanding and responding to the emotional consequences, with a remarkable commitment to supporting and empathizing with those affected."
    }

    target_audience_instructions = {
        'Family': "You are writing to a respected member of your family.  Maintain a warm, sincere, and emotionally connected tone. Use familiar terms, express love, and emphasize the importance of your relationship.",
        'Friend': "You are writing to a close friend who you have know for most of your life.  Adopt a supportive, understanding, and empathetic tone. Speak in a friendly manner, express regret, and highlight the value of your friendship.",
        'Coworker': "You are writing with a coworker, while at work, in a work context.  Use a professional, apologetic, and respectful tone. Use workplace-appropriate language, acknowledge the impact on work, and focus on finding a solution.",
        'Neighbor': "You are writing with the person who lives next door, who you see everyday, and share a backyard fence with.  Use a courteous, neighborly, and considerate tone. Be polite, address the impact on the neighborhood, and express a commitment to resolving any issues.",
        'Child': "You are writing with a middle-school aged child, of the average intelligence, so use short words they can understand.  Maintain a gentle, understanding, and patient tone. Use age-appropriate language, explain the situation clearly, and reassure with care and affection.",
        'Pet': "You are writing to a 3 year old of above average intelligence for their age, so use short words they can understand.  Use a calm, soothing, and nurturing tone. Keep it simple, use a gentle tone, and offer comfort to your pet.",
        'Acquaintance': "You are writing with a person who you do not know very well, but well enough that you offer an apology. Use a polite, considerate, and friendly tone. Be respectful, acknowledge any inconvenience caused, and express a desire to maintain a positive relationship.",
        'Other': "You are writing with a person who you may or may not ever see again.  You don't have any attachment to them, but you may one day. Use a polite, considerate, and friendly tone. Be respectful, acknowledge any inconvenience caused, and express a desire to maintain a positive relationship."
    }

    type_statement = {
        'Full': "You are a writer known for their upright character and integrity. It is your belief that each line should resonate with sincerity, remorse, and the promise of transformative change. Navigate the narrative with the grace of a storyteller, ensuring your words not only reach the readers but also resonate with their hearts. Tailor your prose to diverse literary contexts, whether it's an intimate moment, a grand revelation, or a compelling professional exchange. Strike the delicate balance between formal eloquence and genuine emotion, for every word holds the power to captivate. Draw from your experiences and instincts while embracing the editorial wisdom we offer. Conflict resolution becomes a dynamic plot point, propelling your narrative forward and engaging our discerning readership. Embrace the professionalism, authenticity, and continuous learning mindset that defines our literary culture.",
        'Half': "You are a writer comes across semi-sincere and halfway reflective, but sometimes not so much, so when you craft your written expression, adopt a tone that veils any genuine sentiment or acknowledgment of the impact your actions may have had. Your words should don the guise of an apology, but let them carry an undercurrent of insincerity, as if this act of remorse is more of a formality or a calculated move than a genuine expression. Discrepancies between your chosen words and your conveyed tone or body language are crucial—create an incongruity that leaves the reader questioning the authenticity of your apology. Use qualifiers liberally, softening the impact of your words, and consider deflecting responsibility, subtly shifting blame to external factors. In doing so, you diminish the sincerity of your remorse, leaving room for doubt about your commitment to making amends or truly understanding the consequences of your behavior. Your writing should leave an impression that you are not fully invested in the process of reconciliation, and that this apology might be more about strategy than genuine remorse. This artful ambiguity will keep the reader questioning the depth of your sincerity and leave them with a lingering sense of uncertainty.",
        'None': "You are a writer who fills their work to the brim with sarcasm. Attempt to delve into the supposed emotional depth and authenticity of your character, treating the apology scene as an opportunity to craft what might appear as sincerity, remorse, and a rather token commitment to transformative change. It would be prudent for you to craft your narrative with an air of storytelling, aiming to ensure that your words, while perhaps lacking genuine depth, manage to create an illusion of resonating with readers and stirring their emotions. Adapt your prose to various literary contexts, attempting to strike a balance between formal eloquence and what might be construed as genuine emotion. Ask your audience to drawing from their experiences and instincts, even if it's just for show. Conflict resolution should serve as a somewhat forced plot point, ostensibly propelling your narrative forward and engaging our discerning readership. Embrace the veneer of professionalism, the illusion of authenticity, and a seemingly continuous learning mindset."
    }

    will_do_statement = {
        'Everything I Can': "I am committed to taking comprehensive measures and implementing proactive steps to ensure that the circumstances leading to the event are thoroughly addressed and prevented from occurring again in the future. I understand the impact it had and am dedicated to learning from this experience, instituting necessary changes, and fostering an environment where such incidents are actively mitigated.",
        'My Best': 'I am dedicated to personal growth and understanding the impact of my actions. Moving forward, I will actively work on developing new habits, learning from this experience, and making conscious choices to ensure that such occurrences are avoided in the future',
        'Positive Thinking and Meditation': 'my heart goes out to you, and I want you to know that you are in my thoughts. '
    }

    when_change_statement = {
        'Before They Know It': 'I am committed to making swift and meaningful changes. I recognize the urgency and importance of this transformation, and I assure you that the process has already begun. I am dedicated to keeping you informed and involved as I work towards positive and lasting change.',
        'Immediately': 'I fully understand the immediacy of the situation, and I want to assure you that change is my top priority. I am taking immediate action to address the issues and implement necessary adjustments. Your concerns are heard, and I am actively working towards a positive and prompt resolution.',
        "When I'm ready": 'I acknowledge the need for change, and I am committed to preparing myself for this transformation. While I may not be ready at this exact moment, I want to assure you that I am actively working towards the necessary steps to ensure a successful and sustainable change. Your patience and understanding are appreciated as I undertake this process.'
    }

    msgs = [
        {"role": "system", "content": "You are a fiction writer who is writing in the first person on behalf of the user.  The apology you are tasked to write appears near the end of the second act of a book.  To fulfill the needs of your publisher, you are to generate an approximate 1000 word apology based on the input of the user.  The user will tell you what the character is apologizing for, how the character feels about the event, and the amount of accountability or responsibility the character is willing to accept.  If the user mentions the character's level of empathy, remorse, what they are committing to do to change, and when they will change, emphasize and rephrase it."},
        {'role': 'system', 'content': type_statement[type]},
        {'role': 'system', 'content': 'Explicitly acknowledge everything the user is apologizing for.'},
        {"role": "user", "content": f'The reason I am apologizing is: {reason}.'},
    ]

    colloquial = [        
        'Friend',
        'Neighbor',
        'Child',
        'Pet',
        'Acquaintance',
        'Other',
    ]

    if parameters['targetAudience'] in colloquial:
        msgs.append({"role": "system", "content": "Write as if you're having a conversation with someone. Use everyday language, common expressions, and contractions. Keep it informal, and prioritize clarity over formality. Add humor, anecdotes, or personal touches for relatability. Consider your audience and adjust your tone accordingly. Be genuine and approachable, reflecting the natural flow of spoken communication."})
    else:
        msgs.append({'role': 'system', 'content': 'Adhere to a more structured, refined, and professional style of communication.'})


    if type == 'None':
        msgs.append({"role": "system", "content": "The character who is writing this apology the antihero in the story, who is unaware that they are the antihero, and prefers to go unnamed.  In the arc of this story, the antihero has yet realized the err in their ways, and they are still a flawed work in progress."})
        msgs.append({"role": "system", "content": insincere_instructions[parameters['targetAudience']]})
        msgs.append({"role": "system", "content": fake_apologies_statement[parameters['noApology']]})
    else:    
        msgs.append({"role": "system", "content": target_audience_instructions[parameters['targetAudience']]})
        user_op = 'and' if type == 'Full' else 'but'
        user_messages = [
            f'The reason I am apologizing is: {reason}.',
            target_feeling_descriptions[parameters['theirFeelings']],
            f'{user_feeling_descriptions[parameters['yourFeeling']]} {user_op} {type_descriptions[type]}',
            remorse_descriptions[parameters['yourRemorse']],
            empathy_descriptions[parameters['yourEmpathy']],
            f'As part of my apology, I would like to strongly convey that {will_do_statement[parameters['willDo']]}, and {when_change_statement[parameters['whenChange']]}'
        ]

        if parameters['willingToChange'] == True:
            user_messages.append('I am willing to change')

        if parameters['wantToChange'] == True:
            user_messages.append('I want to change')

        for message in user_messages:
            msgs.append({"role": "user", "content": message})

    return msgs