def Messages(reason, type, parameters):
    fake_apologies = {
        'Non-Apology': "Shift the blame to recipient's sensitivity.",
        'Justification Apology': "Offer an excuse for the user's behavior rather than taking responsibility.",
        'Blame-Shift Apology': "Shift the blame onto the recipient, and minimize the user's personal responsibility.",
        'Conditional Apology': "Put conditions on the apology, making it contingent on the recipient's actions.",
        'Minimizing Apology': "Downplay the impact of the action on the recipient. Minimize its significance.",
        'Redirected Apology': "Turn the tables by bringing up the recipient's mistakes.",
        'Empty Apology': "Acknowledge the recipient's feelings without admitting the user's fault or expressing genuine remorse.",
        'Fake Regret Apology': "Express regret not for the user's action, but for the consequence of being caught.",
    }

    msgs = [
        {"role": "system", "content": "You are a writer who specializes in writing apologies"},
        {"role": "system", "content": f"You write for people who feel {parameters['yourFeeling']} about what they've done."},
        {"role": "system", "content": f"The recipients of your writing feels {parameters['theirFeelings']} about what has happened."},
        {"role": "user", "content": f'Th reason I am apologizing is: {reason}.'},
        {"role": "user", "content": f'The amount of responsibility I am willing to take is: {type}.'}
    ]
    
    if type == 'None':    
        msgs.append({"role": "system", "content": "You are a writer who specializes in writing insincere apologies for a publication that shows how not to write apologies."})
        msgs.append({"role": "system", "content": f"In this apology, the writer wants to convey: {fake_apologies[parameters['noApology']]}"}) 
    elif type == 'Half':
        msgs.append({"role": "system", "content": f"You write for people who feel only half responsible for their actions and sneakily try to convey it."})
    else:
        msgs.append({"role": "system", "content": "You write for people who feel fully responsible for their actions"})
        user_feeling = f'The event makes me feel {parameters['yourFeeling']}.'
        user_remorse = f'I feel {parameters['yourRemorse']} remorse.'
        user_empathy = f'My empathy is {parameters['yourEmpathy']}.'
        user_will_do = f'{parameters['willDo']} is what I will do.'
        user_when_change = f'I will change {parameters['whenChange']}.'
        recipient_feeling = f'The recipient feels {parameters['theirFeelings']}.'

        user_messages = [
            user_feeling,
            user_remorse,
            user_empathy,
            recipient_feeling,
            user_will_do,
            user_when_change,
        ]

        if parameters['willingToChange'] == True:
            user_messages.append('I am willing to change')

        if parameters['wantToChange'] == True:
            user_messages.append('I want to change')
        
        for message in user_messages:
            msgs.append({"role": "user", "content": message})

    if parameters['targetAudience'] == 'Child':
        msgs.append({"role": "system", "content": "A child will be the one receiving the apology."})
    elif parameters['targetAudience'] == 'Pet':
        msgs.append({"role": "system", "content": "A pet will be the one receiving the apology."})
    elif parameters['targetAudience'] != 'Other':
        msgs.append({"role": "system", "content": f"Your relationship between the user and recipient is: {parameters['targetAudience']}"})            

    return msgs