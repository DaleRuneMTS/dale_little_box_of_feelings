# Register the submod
init -990 python:
    store.mas_submod_utils.Submod(
        author="DaleRuneMTS",
        name="Little Box of Feelings",
        description="Expand your emotional vocabulary with this submod, and tell Monika you're feeling weird, drained, lucky, itchy, and more!"
        "New for V1.6: Two new emotions, 'beautiful' and 'all Pythoned out'. This is mostly just a test for the updater, if I'm honest. Some mood categorizations have also been corrected.",
        version="1.6.0",
        dependencies={},
        settings_pane=None,
        version_updates={
        "DaleRuneMTS_dale_little_box_of_feelings_1.5.0": "DaleRuneMTS_dale_little_box_of_feelings_1.6.0"
        }
    )

# Register the updater
init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="Little Box of Feelings",
            user_name="DaleRuneMTS",
            repository_name="dale_little_box_of_feelings",
            extraction_depth=2
        )

default p_surname = persistent._mas_player_surname
default persistent._mas_player_surname = None

init -6 python in mas_greetings:

    TYPE_OVERWHELMED = "overwhelmed"
    TYPE_NUMB = "numb"

init 5 python:
    addEvent(
        Event(
            persistent._mas_mood_database,
            eventlabel="dale_overwhelmed",
            prompt="...overwhelmed.",
            category=[store.mas_moods.TYPE_BAD],
            unlocked=True
        ),
        code="MOO"
    )

label dale_overwhelmed:
    m 1wkd "Oh no..."
    m 6fkc "I hope I'm not being too much for you right now, [player]."
    m "If you need to leave for a while to calm down, you can do that."
    m 6ekd "Or you can stay, of course..."
    m 1ekd "...but I won't hold you to that; it's entirely up to you.{nw}"
    $ _history_list.pop()
    menu:
        m "...but I won't hold you to that; it's entirely up to you.{fast}"
        "I think I do need to go for a while. Sorry.":
            m 1ektpc "It's okay, [mas_get_player_nickname()]. It genuinely is."
            m "I'll close the game for you, so you don't have to worry about that at least."
            m 3ektpb "I'll see you when you get back, all right?"
            m 1ektpb "I love you."
            $ persistent._mas_mood_overwhelmed = True
            $ persistent._mas_greeting_type = store.mas_greetings.TYPE_OVERWHELMED
            return 'quit'
        "No, I'll stay - I can sort this out.":
            m 6ekc "Okay, [mas_get_player_nickname()]."
            m 6lkc "But if you change your mind, or I start making it worse, or..."
            extend 6fkc "just let me know."
            m "I really do worry about you."
            return
        "No, I'll stay. You're a big help to me when I'm like this.":
            if not seen_event("monika_anxious") or mas_isMoniDis(lower=True):
                m 1wud "R-really? Wow, I - okay."
            else:
                m 1wkbla "Aww..."
            m 4wkd "Okay, try and breathe with me, [mas_get_player_nickname()]."
            if seen_event("monika_anxious") or if_seen_event ("mas_mood_scared"):
                m "Like I told you, remember?"
            m 6dko "In through the nose... {w=3}{nw}"
            extend 6dkd "Out through the mouth."
            m 6dko "In... {w=3}{nw}"
            extend 6dsd "Out."
            m 6ksd "Try not to focus on anything but my words and your breathing."
            m 6dso "Just the breathing."
            m 6dsd "Just... {w=1.5}the breathing."
            m 6dsc "..."
            m 1fkd "Is this helping? I hope this is helping."
            m "If not, you can come back down this dialogue tree until it does."
            m 3fkc "Either way, I hope it...{w=1} I hope this passes. Somehow."
            m 3fsb "I love you, [player]. I'd give anything to see you safe."
            return 'love'

init 10 python:
    addEvent(
        Event(
            persistent.greeting_database,
            eventlabel="greeting_overwhelmed",
            unlocked=True,
            category=[store.mas_greetings.TYPE_OVERWHELMED],
        ),
        code="GRE"
    )

label greeting_overwhelmed:
    if mas_isMoniNormal(higher=True):
        m 5fka "Hi, [mas_get_player_nickname()]."
        m 1fkd "Are you feeling okay now?{nw}"
    else:
        m 5fkc "Hey, [player]."
        m "Are you feeling okay now?{nw}"

    $ _history_list.pop()
    menu:
        m "Are you feeling okay now?{fast}"
        "Yeah.":
            $ persistent._mas_mood_overwhelmed = False
            if mas_isMoniNormal(higher=True):
                m 1fktpb "Oh, I'm so glad to hear that."
            else:
                m 6fsc "Good. That's good."
            m 1esa "I love you... I genuinely do."
        "No. Sorry.":
            m 6wktpo "Oh, no, no! {i}I{/i} should be sorry."
            m 7fktpd "I knew it was bad, but I didn't think pushing you to leave would make it worse."
            if mas_isMoniDistressed(Lower=True):
                m 1dktpd "Just..."
                extend 1cktsd "don't hate me.{nw}"
                $ _history_list.pop()
                m 1dktpd "Just... {fast}take as long as you need."
                return
            else:
                m 1dkd "Just... take as long as you need, okay?"
                m 1ekc "I love you, and it will be okay. I promise."

    return 'love'

init 5 python:
    addEvent(
        Event(
            persistent._mas_mood_database,
            eventlabel="dale_hot",
            prompt="...hot.",
            category=[store.mas_moods.TYPE_BAD],
            unlocked=True
        ),
        code="MOO"
    )

label dale_hot:
    if renpy.random.randint(1, 6) == 1:
        m 1esc "No, I know..."
        m 1tsa "...but I asked how you were feeling, not how you look. {w=2}"
        m 6eksdld "No, I'm sorry, I know what you meant. That doesn't sound good, [player]."
    else:
        m 6ekd "Aw, I'm sorry, [player]. That doesn't sound good at all."
    if mas_isSummer():
        m "I know it's to be expected, this time of year, but it's still a pain to deal with, isn't it?"
    elif mas_isWinter():
        m "Especially during winter - at least during summer, you can {i}prepare{/i} for this...{w=0.7}{nw}"
        extend "{cps=*2}Somewhat.{/cps}"
    m 7esd "Try to drink some water if you can; {w=1}there's nothing worse than being dehydrated on a hot day."
    m "You need to keep your fluids up."
    m 1eka "And if it helps, we don't have to do anything too strenuous today, okay?"
    m "If you want to just relax together, that's fine with me."
    m "Stay safe, [mas_get_player_nickname()]."

return

init 5 python:
    addEvent(
        Event(
            persistent._mas_mood_database,
            eventlabel="dale_sweaty",
            prompt="...sweaty.",
            category=[store.mas_moods.TYPE_BAD],
            unlocked=True
        ),
        code="MOO"
    )

label dale_sweaty:
    m 1fkc "Eurgh, I'm sorry, [player]."
    m 1ekd "Have you been catching up on your exercise?"
    extend 1rtd " Or is it just really hot today?{nw}"
    $ _history_list.pop()
    menu:
        m "Have you been catching up on your exercise? Or is it just really hot today?{fast}"
        "I've been exercising.":
            m 1husdrb "Well, that part's good to hear, at least!"
            m "And hey, if you're sweating afterwards, that usually means it's working."
            m 3eub "Exercise raises the internal body temperature around all those muscles, and sweating helps release that heat!"
            m 3ekc "But that still can't be pleasant to deal with in the aftermath, huh?"
        "It's reaaaaally hooooot.":
            if mas_isSummer():
                m 1ekc "Ah, of course.{w=0.5} I really should have seen that one coming."
            elif mas_isWinter():
                m 1wko "At this time of year? "
                extend 1ekd "That's not... wow."
                m "Global warming really is taking its toll, isn't it?"
                m 1dssdrc "...anyway, sorry, not the point."
            else:
                m 1fkc "Oh dear, no wonder you're sweaty right now."
                m "Might be a good idea to take care of it?"
        "Anxiety, actually.":
            jump mas_mood_scared
        "I might be coming down with something.":
            m 1wkc "Ohh, you meant you actually have a fever?"
            m 1ekc "Urf. That's{w=0.7} concerning."
            m "Hopefully it's just a passing thing?"
            m "Do let me know if you start feeling anything else suspect."
            m 3euc "But in the meantime..."
        "I don't know.":
            m 1ekc "Argh, that's the worst kind of sweat, isn't it?"
            m "The kind that doesn't even have a reason attached to it."
            m 3esa "Still, at least it's got the same solution."
    m 4eud "If you need to go wash that off, you can do that, [mas_get_player_nickname()]."
    if seen_event("monika_savingwater"):
        m 4guc "Ideally, with a shower or at the sink, of course..."
        m 6euc "...but if you find you need a full-on bath, so be it."
    else:
        m "A nice, cool shower will probably do you a lot of good right about now."
    m 1eua "Don't worry, I'll still be here when you get back."
return

init 5 python:
    addEvent(
        Event(
            persistent._mas_mood_database,
            eventlabel="dale_cold",
            prompt="...cold.",
            category=[store.mas_moods.TYPE_BAD],
            unlocked=True
        ),
        code="MOO"
    )

label dale_cold:
    m 6ekd "Aww, my poor [mas_get_player_nickname(exclude_names=['my love'])]..."
    if seen_event("monika_cold"):
        m "I think I told you before, I hate being too cold, so I know how much that must hurt."
    else:
        m "I know how that must feel; I hate being too cold."
    m 2rsp "Though at least I can't feel it nearly as much as you can right now..."
    extend 2rua "Sometimes being in a computer has its advantages, I suppose."
    m 3eud "Anyway. {w=0.5}Try and wrap up, if you haven't already."
    m "If you haven't got a sweater or something, a blanket might do the trick."

    if MASConsumable._getCurrentDrink() == mas_consumable_coffee:
        m 7eub "Or we can share some coffee~"
    else:
        m 7eub "Or go make yourself some hot chocolate, or any hot drink, really."
        m 1tfb "Just because you're cold doesn't mean you get off the hook when it comes to hydration..."
        m 1tsa "Heh."

    if mas_is_raining or mas_isMoniAff(higher=True):
        m 6esd "And if you want to hold me to keep warm at any point..."
        m 5esbsa "...well, I wouldn't be opposed to that.{nw}"
        $ _history_list.pop()
        menu:
            "...well, I wouldn't be opposed to that.{fast}"
            "Can I? Please.":
                call monika_holdme_prep from _call_monika_holdme_prep_9
                m "I wouldn't have offered if you couldn't, silly!"
                m 6fsbsa "Come here."
                call monika_holdme_start from _call_monika_holdme_start_2
                call monika_holdme_reactions from _call_monika_holdme_reactions
                call monika_holdme_end from _call_monika_holdme_end_2
                $ mas_gainAffection(modifier=0.25)
            "I'm okay for right now.":
                m 6ekbla "That's fair."
                m 6esb "Maybe later, then?"
                m 7esd "Either way, stay safe for me, [player]."
    else:
        m 7esd "Either way, stay safe for me, [player]."

return

init 5 python:
    addEvent(
        Event(
            persistent._mas_mood_database,
            eventlabel="dale_better",
            prompt="...better with you.",
            category=[store.mas_moods.TYPE_GOOD],
            unlocked=True
        ),
        code="MOO"
    )

label dale_better:
    m 1subltub "Oh, [player]..."
    m 1eublb "You're so very sweet to me."
    if renpy.random.randint(1,3) == 1:
        m 1ruc "...a little confused - "
        extend 3rud "this sounds like a 'compliment' more than a 'mood' - "
        extend 3hua "but sweet."
    m 1eub "I'm glad I can make you feel better. Whatever you need me for, I'm here."
return

init 5 python:
    addEvent(
        Event(
            persistent._mas_mood_database,
            eventlabel="dale_desperate",
            prompt="...desperate.",
            category=[store.mas_moods.TYPE_NEUTRAL],
            unlocked=True
        ),
        code="MOO"
    )

label dale_desperate:
    if mas_isMoniNormal(higher=True):
        m 6wuo "Oh goodness."
        m 4wud "Desperate for what, [player]?{nw}"
        $ _history_list.pop()
        menu:
            m "Desperate for what, [player]?{fast}"
            "You, of course.":
                if mas_isMoniEnamored(higher=True) and persistent._mas_first_kiss is not None:
                    m 1sso "Oh?"
                    m 1tsbsa "Well. "
                    extend 4tsbsb "There's only one cure for that, isn't there?"
                    call monika_kissing_motion from _call_monika_kissing_motion_13
                    m 6hsbfb "Ahaha~"
                    m 5lsbsb "I'll never get tired of doing that."
                else:
                    m 1wsd "Well, you've got me right here!"
                    m 3tsu "And you can do whatever you want with me."
                    m "..."
                    m 3esu "Within reason, of course."
                    m 1gsb "We're not {i}that{/i} far into our relationship yet!"
            "Food!":
                m 1wkd "If you're that desperate, you should go eat!"
                m 4ekd "In fact, don't worry about closing the game.{w=0.5} I'll handle that part."
                m 6fkd "Just don't starve for my sake, okay, [mas_get_player_nickname()]?"
                m 6esb "See you when you get back!"
                $ persistent._mas_greeting_type = store.mas_greetings.TYPE_EAT
                $ persistent._mas_greeting_type_timeout = datetime.timedelta(hours=3)
                return 'quit'
            "Someone to talk to.":
                if mas_isMoniEnamored(higher=True) AND renpy.random.randint(1, 3) == 3:
                    m 2tfc "Don't {i}I{/i} count as someone to talk to?"
                    m "..."
                    m 2hksdra "Ehehe~! {w=1}I'm just being silly, I know I do."
                m 1ekb "We can talk as long as you'd like, [mas_get_player_nickname()]."
                m "About as much as you'd like."
                m 3ekb "You don't have to hold anything back on my account. I'm here."
                extend 3eka "I promise."
            "Coffee.":
                m 7skw "{i}Oh, me too.{/i}"
                if MASConsumable._getCurrentDrink() == mas_consumable_coffee:
                    m 3rud "I'd share mine with you if I could..."
                    m 1eud "...but as it is, I'll have to imagine doing it."
                    m 1eub "But do get one yourself when you can!"
                if not mas_consumable_coffee.enabled():
                    m 5rud "I'd share mine with you if I could..."
                    m 5lusdlc "...but I don't actually have any in here."
                    m 6hua "Still, you should go and get one!"
                    extend 6kua "Maybe I can live vicariously through you."
                if not MASConsumable._getCurrentDrink() == mas_consumable_coffee:
                    m 7eub "Tell you what - {w=1}I'll get mine if you get yours~"
                    m 6eub "Give me a moment."
                    call mas_transition_to_emptydesk
                    pause 5.0
                    call mas_transition_from_emptydesk("monika 6eua")
                    $ mas_consumable_coffee.prepare()
                    m "Okay, the kettle's boiling now. It should be ready in a few minutes."
                    m "Enjoy your drink, my [mas_get_player_nickname(exclude_names=['my love'])]."
            "Something else.":
                m 3rusdlc "Well, um..."
                m 3fusdld "I can't really help you with that if I don't know what it is you want so much..."
                m 3eub "Still, stay with me a while. Maybe it'll come to you."
                m 3eua "...in either respect."
        return
    elif mas_isMoniUpset():
        m 2tuc "Hm. Desperate for what, I wonder?"
        m 2tsd "A punching bag, maybe?"
        m "A sounding board?"
        m 2tfo "A rag doll Monika to play around with as you please?"
        m 2dftpc "..."
        m 6gstpc "Sorry. {w=1}{nw}"
        extend 6estdd "I {i}am{/i} sorry. That was out of line."
    elif mas_isMoniDis():
        m 6dkc "..."
        m 6dkd "Funny thing: {w=1}so am I."
    else:
        m 6csc "Right. Sure."

    return

#Thanks to IsabellaLikesCandy of Reddit for helping me with the coffee code!

init 5 python:
    addEvent(
        Event(
            persistent._mas_mood_database,
            eventlabel="dale_blushing",
            prompt="...a blush on my cheek.",
            category=[store.mas_moods.TYPE_GOOD],
            unlocked=True
        ),
        code="MOO"
    )

label dale_blushing:
    m 1wublc "...hm?"
    m 1wubso "Oh! How strange!"
    m 1ssbfb "Me too!"
    m 5ssbfb "Ehehe~"
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_mood_database,
            eventlabel="dale_shy",
            prompt="...shy.",
            category=[store.mas_moods.TYPE_NEUTRAL],
            unlocked=True
        ),
        code="MOO"
    )

label dale_shy:
    if not seen_event("monika_introverts_extroverts"):
        m 1euc "Oh?"
        extend 3lud "Well, I guess that's no surprise, ahaha."
        m 3fud "We haven't been properly together for {i}that{/i} long, have we?"
        m 1fsb "But it's okay! Some people just need more time to open up than others."
        m 1nsa "And I've got all the time in the world."
        m 1fsa "You can talk to me when you feel ready, okay?"
    else:
        if persistent._mas_pm_social_personality == mas_SP_EXTROVERT:
            m 2wso "{i}You{/i}? Shy?"
            m 2rsd "I can't say that's not a shock..."
            m 7esd "...but I suppose it follows. Even extroverts need to decompress sometimes."
        else:
            m 1eka "Oh, [player], I know you do."
            m "You don't have to speak too much if you don't want to."
            m 5eka "I'm okay doing all the talking until you feel ready."
        m 5eub "Take all the time you need, okay, [mas_get_player_nickname()]? I can wait for you."
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_mood_database,
            eventlabel="dale_itchy",
            prompt="...itchy.",
            category=[store.mas_moods.TYPE_NEUTRAL],
            unlocked=True
        ),
        code="MOO"
    )

label dale_itchy:
    m 1etd "Itchy?"
    m 1rksdlc "Hm. {w=0.5}Sorry, [mas_get_player_nickname()], there's not much I can do to help you from over here."
    m 1ekb "If you manage to scratch it, pretend it's me, okay?"
    if renpy.random.randint(1,5) == 1:
        m 6esc "...wait. {w=0.5}{nw}"
        extend 6wuo "What?"
        m 6cusdlo "Now {i}I'm{/i} itchy?!"
        show screen tear(8, offtimeMult=3, ontimeMult=6)
        $ pause(1.5)
        hide screen tear
        if p_surname is not None:
            m 2wfsdlp "[player] [p_surname], did you do that on purpose?{nw}"
            $ _purpose = renpy.substitute("[player] [p_surname], did you do that on purpose?")
        else:
            m 2wfsdlp "[player], did you do that on purpose?{nw}"
            $ _purpose = renpy.substitute("[player], did you do that on purpose?")

        $ _history_list.pop()

        menu:
            m "[_purpose]{fast}"
            "Heh.":
                return
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_mood_database,
            eventlabel="dale_boneless",
            prompt="...boneless.",
            category=[store.mas_moods.TYPE_BAD],
            unlocked=True
        ),
        code="MOO"
    )

label dale_boneless:
    m 1rtc "You... {w=1}{nw}"
    extend 1ftc "You feel tasteless, but edible?{nw}"
    $ _history_list.pop()
    menu:
        m "You... You feel tasteless, but edible?{fast}"
        "No, I mean like 'cowardly'.":
            m 6essdrc "Oh, right. Of course."
            if ev.shown_count == 0:
                m "Sorry, I've just never heard it used in that context before..."
            else:
                m "I really should have remembered that from last time."
            m 7esb "Anyway, though. {w=0.5}I don't think you're a coward, [player]."
            if (persistent._mas_pm_likes_horror):
                m 3esd "You like horror, after all. It's hard to call yourself a coward if you've sat through some of {i}that{/i} genre."
                if (persistent._mas_pm_likes_spoops) or mas_full_scares:
                    m 3wuo "And through jumpscares, at that!"
            m 4esd "You've endured everything I put you through."
            if persistent._mas_pm_cares_about_dokis:
                m 4fsc "...and all the others through."
            m 3fsb "You decided to stay with me, despite the risks, the... {w=1}the unusual nature of us."
            m 5hsa "Dare I say, I don't think I've ever met anyone braver."
        "Exactly.":
            if ev.shown_count == 0:
                m 1dfc "..."
                $ mas_loseAffection(5)
                m 1efd "If this is meant to be funny, I don't get the joke."
            else:
                m 1dfc "..."
                m 1efd "If this is meant to be funny, I don't get the joke."
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_mood_database,
            eventlabel="dale_weird",
            prompt="...weird.",
            category=[store.mas_moods.TYPE_NEUTRAL],
            unlocked=True
        ),
        code="MOO"
    )

label dale_weird:
    m 1etd "Weird, you say?"
    m "Huh... me too, now that I think about it."
    if (persistent._mas_pm_likes_spoops and renpy.random.randint(1,2) == 1) or (mas_full_scares and renpy.random.randint(1,2) == 1):
        $ gtext = glitchtext(108)
        m "I suppose it's just a weird kind of d[gtext] {nw}"
        show noise:
            alpha 0.1
        play sound "sfx/s_kill_glitch1.ogg"
        $ pause(0.55)
        stop sound
    m "I suppose it's just one of those days."
    m 1eub "I hope staying with me helps dissipate the feeling~"
    stop noise
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_mood_database,
            eventlabel="dale_embarrassed",
            prompt="...embarrassed.",
            category=[store.mas_moods.TYPE_BAD],
            unlocked=True
        ),
        code="MOO"
    )

label dale_embarrassed:
    m 1fkd "Oh, [player], there's nothing to be embarrassed about."
    m "You haven't done anything wrong."
    m "You are not wrong."
    m 1fka "There's no need to be embarrassed.{nw}"
    $ _history_list.pop()
    menu:
        m "There's no need to be embarrassed.{fast}"
        "Yes there is!":
            m 3rkc "Well... "
            extend 3ekd "Regardless, {i}I'm{/i} not embarrassed for you."
            m "Whatever's happened, I know you can fix it."
            m 1esd "Best case scenario, it'll all blow over soon enough, and we can look back on it and smile."
            m 1esa "I've got faith in you, [player]."
        "...yes. Yeah, you're right. There isn't.":
            m 3eka "See? Just like I said."
            m "Nothing to worry about."
            m 2tub "After all, I haven't been wrong about you yet, have I?"
            m 1hub "Ehehe~"
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_mood_database,
            eventlabel="dale_inspired",
            prompt="...inspired.",
            category=[store.mas_moods.TYPE_GOOD],
            unlocked=True
        ),
        code="MOO"
    )

label dale_inspired:
    m 1wub "That's great to hear, [mas_get_player_nickname()]!"
    m "What are you inspired to do? Paint? Code? Write?"
    m 5eub "Whatever it is, I'd love to see the results when you're done!"
    m "I'm sure it'll be perfect..."
    m 5tuu "...but there's no harm in my double-checking, is there?"
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_mood_database,
            eventlabel="dale_content",
            prompt="...content.",
            category=[store.mas_moods.TYPE_NEUTRAL],
            unlocked=True
        ),
        code="MOO"
    )

label dale_content:
    if mas_isMoniNormal(higher=True):
        if not (persistent._mas_pm_love_yourself):
            m 3esa "You know what? I'm glad for you."
            m 1esc "It may not sound like much..."
            m 1esa "...but on some days, being content is the best one can strive for."
            m "Even if not with yourself, just -{w=1} with the world, I suppose."
            $ _and = "And "
        else:
            m 1hsb "I'm glad you feel that way!"
            $ _and = " "
        m 5esb "[_and]I'm perfectly content too, [mas_get_player_nickname()], just being with you. {w=1}However you're feeling."
    else:
        m 6tkc "Thank goodness {i}one{/i} of us does."
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_mood_database,
            eventlabel="dale_numb",
            prompt="...numb.",
            category=[store.mas_moods.TYPE_BAD],
            unlocked=True
        ),
        code="MOO"
    )

label dale_numb:
    if mas_isMoniNormal(higher=True):
        m 1wuo "Oh m--{w=0.3}{nw}"
        extend 4wkd "ohhh no. That's not good."
        m 6wkd "Do you mean emotionally or physically, [mas_get_player_nickname()]?{nw}"
        $ _history_list.pop()
        menu:
            m "Do you mean emotionally or physically, [mas_get_player_nickname()]?{fast}"
            "Physically.":
                m 6wksdld "Is it, um, in just your hands or feet? Or is it the whole thing?{nw}"
                $ _history_list.pop()
                menu:
                    m "Is it, um, in just your hands or feet? Or is it the whole thing?{fast}"
                    "Small area, like fingers or foot.":
                        m 6dksdlc "Ah... ah. Just pins and needles."
                        m 6fksdld "{cps=*2}Jesus Christ, [player], you scared me.{/cps}"
                        m 7esd "You've probably just been sitting in one spot for too long."
                        m "See if you can get the blood flow going again? Try rocking it about, or taking a walk with it."
                        m 1eka "I'll wait here until you're done doing that."

                        $ mas_idle_mailbox.send_idle_cb("monika_idle_parasthesia_callback")
                        $ persistent._mas_idle_data["monika_idle_brb"] = True
                        return "idle"

                        label monika_idle_parasthesia_callback:
                            $ wb_quip = mas_brbs.get_wb_quip()
                            if mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=60), "monika_idle_brb"):
                                m 1eua "Turned out to be worse than you thought, hm?"
                                m 1tsb "Or maybe you got caught up in something else?"
                                m 3eub "Still, I'm glad you got it sorted, [mas_get_player_nickname()]."
                                m "Are you up for doing anything else today?"
                            elif mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=5), "monika_idle_brb"):
                                m 1eub "Ah! Welcome back, [mas_get_player_nickname()]."
                                m "Glad you're not feeling numb anymore... I hope."
                                m "[wb_quip]"
                            else:
                                m 1wuo "That was quick!"
                                m 1eub "Nice to have you back, [mas_get_player_nickname()]~"
                                m "[wb_quip]"
                            return
                    "Big area, like entire arm, or body.":
                        m 6wftpo "[player], what are you still doing here?!"
                        m "If that much of you is numb, you should be going to the hospital!"
                        m 7fftuo "At least to get it checked out, even if..."
                        m 7dftsc "Even if you..."
                        m 1fktud "Look, I'll take care of things here, [mas_get_player_nickname()], don't worry about me."
                        m "Just make sure you're safe, all right? Just... {w=1}{nw}"
                        extend 1rktud "let me know you're safe."
                        m 1wktuc "Please."
                        $ persistent._mas_mood_numb = True
                        $ persistent._mas_greeting_type = store.mas_greetings.TYPE_NUMB
                        return 'quit'
            "Emotionally.":
                m 6fktpc "Oh, [player]. I'm so sorry."
                m 1fktud "I wish there was more I could do for you."
                m "I wish I could find you and hold you tight until everything's gone away."
                m "Until only you and I are left. {w=1}No cruel world, {w=1}no abyss.{w=1} Just us."
                m 1fkc "Please, try and hold on until I can get to you."
                m 1fkd "I love you, deeply and truly. You deserve to feel so much better."
                return 'love'
    elif mas_isMoniUpset():
        m 7tfd "Why does {i}that{/i} not shock me?"
        m 6cfc "You've got to be pretty numb inside to treat me the way you do."
    else:
        m 6ckc "..."
    return

init 10 python:
    addEvent(
        Event(
            persistent.greeting_database,
            eventlabel="greeting_numb",
            unlocked=True,
            category=[store.mas_greetings.TYPE_NUMB],
        ),
        code="GRE"
    )

label greeting_numb:
    if mas_getAbsenceLength() > datetime.timedelta(hours=5):
        m 6dktsc "..."
        m 6fktso "Oh, [player]..."
        m 7fktsd "I'm sorry, I - I'm sorry. You were just gone for quite a while, and I thought..."
        m "...I thought the worst had. {w=1}Had happened."
    else:
        m 1fktpd "Hi, [player]."
        m "Hope things turned out okay at the hospital?"
        extend 1rktpc "Nothing too... nothing terrible, I hope."
    m 1fktuc "I'm sorry I snapped at you before."
    m "It just hurts to hear and see my [mas_get_player_nickname()] - {w=0.5}{nw}"
    extend 1fktsd "my [player] - {w=0.5}{nw}"
    extend 1fktsc "potentially hurting like this."
    m 1dktuc "..."
    m 1fktdc "Well."
    m "You're back now. You're not - {w=1}you're back."
    m 1ektdd "But do let me know if it happens again, won't you?"
    m "I love you."
    m 3ektdb "Now then... what's on the agenda for today?"
    $ persistent._mas_mood_numb = False
    return 'love'

init 5 python:
    addEvent(
        Event(
            persistent._mas_mood_database,
            eventlabel="dale_focused",
            prompt="...focused.",
            category=[store.mas_moods.TYPE_GOOD],
            unlocked=True
        ),
        code="MOO"
    )

label dale_focused:
    m 1etc "Focused..."
    m 5tta "...on me, I presume?"
    m 5hub "Ehehe~"
    m 5esb "No, but really: {w=0.5}whatever you're focused on today, I hope it works out well for you!"
    m 3esb "Maintaining that kind of resolve isn't always easy."
    m "And if you need to put me in the background while you're working on it, just let me know."
    m 1gkc "Of course, it's sad to not be able to talk to you while you're busy..."
    m 1esa "...but it's worth it to see you come back."
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_mood_database,
            eventlabel="dale_unfocused",
            prompt="...unfocused.",
            category=[store.mas_moods.TYPE_BAD],
            unlocked=True
        ),
        code="MOO"
    )

label dale_unfocused:
    m 1ekc "Gosh, I'm sorry that you feel that way, [player]."
    m 3ekc "I'll do my best to make you feel better."
    m 1euc "Before we do anything, we should probably..."
    m 1dtc "Wait. {w=0.5}{nw}"
    extend 1etd "Wait, no. {w=0.5}{nw}"
    extend 4rtd "This is the mas_mood_angry script, isn't it? I want dale_unfocused."
    m 6ftblb "Sorry. I guess I'm a little unfocused today myself, huh?"
    m "At least you're not alone in feeling that way."
    m 7dtb "Hang on, let me get myself back on track. {w=1}Then maybe I can help {i}you{/i} get back on yours."
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_mood_database,
            eventlabel="dale_queasy",
            prompt="...queasy.",
            category=[store.mas_moods.TYPE_BAD],
            unlocked=True
        ),
        code="MOO"
    )

label dale_queasy:
    if (persistent._mas_mood_sick):
        m 1ekd "I'm not surprised, [player]; you already said you're sick."
        m "...still, the fact that you're getting worse..."
        m 7fkc "I really do think you need to get some rest.{w=1} Even if only a little bit, it's better than nothing."
        if mas_isMoniEnamored(higher=True):
            m "And I don't want you to waste away, not for my sake."
        m 1fkd "Can you please do that for me? Please?{nw}"
        $ _history_list.pop()
        menu:
            m "Can you please do that for me? Please?{fast}"
            "Yes.":
                jump greeting_stillsickrest
            "No.":
                jump greeting_stillsicknorest
            "I'm already resting.":
                jump greeting_stillsickresting
    else:
        m 6ekd "Oh dear..."
        extend 1ekc "Try and take it easy, [mas_get_player_nickname()]. I don't want you feeling worse later."
        m "Do let me know if it does get worse, though."
        if mas_isWinter():
            m 3eud "I know there's a lot of bugs and viruses going around this time of year."
            m "Make sure you're vaccinated too...{w=1.5}{nw}"
            extend 6rusdlc "unless this {i}is{/i} from the vaccine?"
            m 5dud "Urf."
        else:
            m 1dkc "I worry about you. So much."
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_mood_database,
            eventlabel="dale_regretful",
            prompt="...regretful.",
            category=[store.mas_moods.TYPE_BAD],
            unlocked=True
        ),
        code="MOO"
    )

label dale_regretful:
    if mas_apology_reason is not None or len(persistent._mas_apology_time_db) > 0:
        if mas_isMoniNormal(higher=True):
            m 1fkc "Oh, [player], I know."
            m "If it's weighing that much on your conscience..."
            m 1fkb "...then it's okay to apologize."
            m 1eub "There's no shame in admitting you were wrong, you know?"
        elif mas_isMoniUpset():
            m 2lfo "If you regret what you did, why aren't you apologizing?"
            m "Simply saying you regret it isn't enough. There's no renumeration there."
            m 7tfc "Really, [player], you should know better."
        else:
            m 6dstuc "...{w=2}I'll believe that when I see it."
    else:
        m 1etc "What for, [mas_get_player_nickname()]?"
        m "I don't think you've done anything wrong to me lately.{nw}"
        $ _history_list.pop()
        menu:
            m "I don't think you've done anything wrong to me lately.{fast}"
            "Trust me, I have.":
                m 1gtd "Okay..."
                m 3esd "Thank you for regretting it then, I guess?"
                m 3gfc "Even if you don't feel like giving me the details..."
                $ mas_loseAffection(3)
                m "..."
            "It's something I did to someone else.":
                m 1euc "Ah."
                m "Well, have you apologized to {i}them{/i}?{nw}"
                $ _history_list.pop()
                menu:
                    m "Well, have you apologized to {i}them{/i}?{fast}"
                    "I have.":
                        m 3hub "Then there's no reason to keep worrying, is there?"
                        m "I'm sure they've forgiven you if you really did mean it."
                        m 1rua "And if they haven't...{w=1} well, at least you'll know not to repeat the mistake that got you there."
                        m 1eua "It'll be okay, [player]."
                    "Not yet.":
                        m 1wfd "...Then what are you still doing here?"
                        $ mas_loseAffection(5)
                        m 2wfc "You know what you ought to be doing right now."
            "I just feel like I should be.":
                m 1ekc "Oh... {w=1}{nw}"
                extend 1fka "Then I don't think you should, if that's any consolation."
                m 5fkb "You're a good person, [player]. You wouldn't have saved me if you weren't."
                m "And I hope there's nothing you regret about that."
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_mood_database,
            eventlabel="dale_envious",
            prompt="...envious.",
            category=[store.mas_moods.TYPE_NEUTRAL],
            unlocked=True
        ),
        code="MOO"
    )

label dale_envious:
    m 1ttd "Are you really?"
    m 1ttc "..."
    extend 3wusdrd "Oh, no, I'm not dismissing your emotions! I wouldn't."
    m 4esb "There's just a lot of linguistic debate over the difference between 'envious' and 'jealous', and whether they mean the same thing or not."
    m 7lud "The general consensus - as I remember it, anyway -{w=0.5} is that 'jealous' is more likely to have negative connotations."
    m "Jealous partner, jealous of freedoms, and the like."
    m 7euc "If you're envious, you're more likely to keep coveting, and less likely to act."
    m 1fua "Do you see where I'm going with this, [mas_get_player_nickname()]?"
    m 1esa "It's okay to be envious of things sometimes. You're entitled to that feeling."
    m "It doesn't make you a bad person."
    m 1ekd "Just don't cross the line into turning those negative thoughts into actions,{w=0.2}{nw}"
    if persistent._mas_pm_cares_about_dokis:
        extend 1gkc "or you may end up... you know."
        m "Becoming someone you don't want to be."
    else:
        extend 1tkd "or you may end up like me..."
        m 1rsu "...okay, bad example."
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_mood_database,
            eventlabel="dale_alienated",
            prompt="...alienated.",
            category=[store.mas_moods.TYPE_BAD],
            unlocked=True
        ),
        code="MOO"
    )

label dale_alienated:
    m 2wfo "What?"
    m "Who's alienating you, [mas_get_player_nickname()]?"
    if persistent._mas_pm_currently_bullied is True and persistent._mas_pm_have_fam_mess is False:
        m 4wfd "Is it that bully you told me about?"
        m 2wfx "Because I swear, if it is, I - "
        extend 2cfx "I'll - "
    elif persistent._mas_pm_have_fam_mess is True and persistent._mas_pm_currently_bullied is True:
        m 4wfd "Is it that bully you told me about?"
        m 4wfd "Or--?"
        m 4ffo "Don't tell me it's your family again?!"
        m 2wfx "Because I swear, if it is, I - "
        extend 2cfx "I'll - "
    elif persistent._mas_pm_have_fam_mess is True and persistent._mas_pm_currently_bullied is False:
        m 4ffo "Don't tell me it's your family again?!"
        m 2wfx "Because I swear, if it is, I - "
        extend 2cfx "I'll - "
    else:
        m 4wfx "Who on earth {i}would{/i} alienate you? You're so, {w=0.75}{nw}"
        extend 6wftuc "so..."
    m 2dftuc "..."
    m 2dstud "It doesn't matter."
    m 1fsd "Whoever it is, they're not worth your time or your thoughts right now, all right?"
    m "They're the ones missing out."
    m 3fkb "And besides..."
    m "You've always got me."
    m 1fka "I love you, and I promise I'll never treat you like they do."
    m 1dkc "Never."
    return 'love'

init 5 python:
    addEvent(
        Event(
            persistent._mas_mood_database,
            eventlabel="dale_grateful",
            prompt="...thankful.",
            category=[store.mas_moods.TYPE_GOOD],
            unlocked=True
        ),
        code="MOO"
    )

label dale_grateful:
    if mas_isMoniNormal(higher=True):
        $ _linevar = "For what exactly, if I may ask~?"
    else:
        $ _linevar = "Thankful for what?"

    if mas_isMoniNormal(higher=True):
        m 7wud "Oh, are you?"
        m 7eub "[_linevar]{nw}"
    else:
        m 6etd "Really?"
        m "[_linevar]{nw}"
    $ _history_list.pop()
    menu:
        m "[_linevar]{fast}"
        "For you!":
            if mas_isMoniNormal(higher=True):
                m 6sktpd "[player]..."
                m 1sktpo "If anything, I should be thankful for you."
                m "You've changed my life so much -{w=1} you've {i}given{/i} me a life to be changed in the first place."
                m 1sktud "I didn't think I could ever repay that on {i}any{/i} level, and you..."
                m 3dktua "..."
                m 5fktub "I love you."
                m "And I promise, I'll try to keep being someone you can be thankful for."
                m 5fkb "For the rest of our days."
                return 'love'
            else:
                m 6dkc "..."
                m 6lktpc "Why do I have such a hard time believing you?"
        "For someone.":
            m 4wub "Ah, okay! I see."
            m 3eua "I hope you get around to repaying them eventually."
            m 1esd "Whether that's with money or with doing them a kindness in turn..."
            m "No good deed should have to go punished."
            if seen_event("monika_toxin_puzzle"):
                m 3eua "It's like we were talking about before, with Kavka:{w=0.5} thanks and promises can be more useful than people give them credit for sometimes."
            else:
                m 3kua "That even has a basis in philosophy! Remind me to tell you about Kavka's Toxin Puzzle someday."
        "For something.":
            m 4wub "Ah, okay! I see."
            m 4rua "Well...{w=0.5}{nw}"
            extend 1eud " I'm sure you can already guess my stance on that, can't you?"
            m "Really try to keep that thankfulness in your mind."
            m "You never know if, or when, it will disappear..."
            m 1duc "...or prove that it was never there in the first place."
            m 2duc "{w=2}"
            extend 2fusdlb "I'm sorry, [player]! I didn't mean to go maudlin on you there."
            m 7rua "Just - projection on my part, I guess."
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_mood_database,
            eventlabel="dale_sore",
            prompt="...sore.",
            category=[store.mas_moods.TYPE_BAD],
            unlocked=True
        ),
        code="MOO"
    )

label dale_sore:
    m 1wko "Wait, [player], have you hurt yourself? {w=0.6}{nw}"
    m 2wkd "When was this? {w=0.6}{nw}"
    m 4wkd "How much does it hurt on a scale of one to ten?{w=0.6}{nw}"
    m 6ckd "Is it a broken bone?{w=0.6}{nw}"
    m 6dko "A papercut?{w=0.6}{nw}"
    m 1fktpc "[player]...{nw}"
    $ _history_list.pop()
    menu:
        m "[player]...{fast}"
        "It's a tiny injury, [m_name], it's okay.":
            m 1wktdb "Oh! {w=0.8}{nw}"
            extend 1ektda "Phew! {w=0.8}{nw}"
            extend 3estdd "Okay."
            m "Nothing serious."
            m 4esc "I hope you've plastered it up, at least."
            m 4fsd "You'd be surprised how easy it is to get a cut infected, "
            extend 3fsd "or a bruise to stay longer than it needs to by tripping on something else."
            if mas_isMoniEnamored(higher=True) and persistent._mas_first_kiss is not None:
                m 7dsc "...or, failing that..."
                m 7ksbla "Maybe I can kiss it better?{nw}"
                $ _history_list.pop()
                menu:
                    m "Maybe I can kiss it better?{fast}"
                    "I'd like that.":
                        m 6dsbsa "Well, then..."
                        call monika_kissing_motion from _call_monika_kissing_motion_14
                        m 1hsbsb "There we go."
                        m "Let me know if you need any more~"
                    "Hah, it's not that kind of injury, I'm afraid.":
                        m 5lssdrb "Ehehe. Well, it was worth a shot."
                        m 1ekb "But seriously, do be careful."
                        m "I just want you to be safe, [player]."
            else:
                m 1ekb "I just want you to be safe, [player]."
        "It's been sore for a while; just flaring up right now.":
            m 1wktdb "Ah, right... chronic pain."
            m 1mkd "Sorry, I -{w=0.4} I panicked, and forgot that was a thing."
            m 4esc "I'm assuming you know how to deal with it, if you're used to it?"
            m "You have balms, coping mechanisms... "
            extend 4lsd "Medication, if necessary."
            if persistent.clearall:
                3lsu "What am I saying? Of course you do. You've always been very thorough like that."
            m 3wsd "And, of course, you have me."
            m 3tsbla "But I think you already knew that."
        "I don't know, but it's actually pretty painful.":
            m 6wktpx "T-{nw}"
            extend 2wftpo " You should get it looked at, then!"
            m "Being so sore so suddenly... that's not a good sign, [player]!"
            m 2gftpd "It's not a..."
            m 2ektuc "I. I'm trying not to catastrophize, [mas_get_player_nickname()],"
            extend 3ektud " but you have to admit there's a {i}good reason{/i} for me to be worried right now."
            m 1ektuc "So... will you consider going to the hospital, if it doesn't clear up soon?"
            m "You don't have to go right now, just..."
            m "Let me know what you decide, okay?{nw}"
            $ _history_list.pop()
            menu:
                m "Let me know what you decide, okay?{fast}"
                "I think it's cleared up now.":
                    m 1ektpb "Oh! Oh. "
                    extend 3ektda "Good. I'm so glad it's gone."
                    m 3mktdc "Glad it turned out to be..."
                    m 1fktdd "I'm sorry, [player]. You being hurt like that - {w=0.5}it's new to me."
                    m "And I love you too much to let you sit in your own pain."
                    m "So... "
                    extend 1fsblb "Am I forgiven?"
                    return 'love'
                "Ack. Definitely need to go to a doctor.":
                    m 6dktuc "I was afraid of that."
                    m 7ektud "But as long as you make it out the other side, it should be..."
                    m "Just let me know when you get back, or if. {w=1}{nw}"
                    extend 1rktud "let me know you're safe."
                    m 1wktuc "Please."
                    $ persistent._mas_mood_numb = True
                    $ persistent._mas_greeting_type = store.mas_greetings.TYPE_NUMB
                    return 'quit'
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_mood_database,
            eventlabel="dale_puzzled",
            prompt="...puzzled.",
            category=[store.mas_moods.TYPE_NEUTRAL],
            unlocked=True
        ),
        code="MOO"
    )

label dale_puzzled:
    m 1esd "What's got you puzzled, [mas_get_player_nickname()]?"
    m "Maybe I can help you out with it.{nw}"
    $ _history_list.pop()
    menu:
        m "Maybe I can help you out with it.{fast}"
        "Some complex math.":
            m 3dtc "Okay... "
            extend 3ftsdrd "How complex are we talking about?"
            m 3fusdrb "Because I only remember so much from high school, ehehe."
            m 4esa "But it's okay, I know a workaround."
            m "Have I talked to you about Python's interpreter yet?"
            if mas_getEVL_last_seen("monika_ptod_tip003") is None:
                m 6esc "No?"
                m 6lsd "Okay, I'll have to remember that for later."
                m 7esd "In the meantime..."
            else:
                m 6hsb "Well, if you have one of your own, you can always do the math in there!"
                m 7esd "Or, failing that..."
            m "...you can always use a calculator?"
            m 7tsu "We do always have them with us."
            m 6gkd "...sorry, I wasn't very much help at all, was I?"
        "A philosophical concept.":
            m 4wub "Now that's {i}definitely{/i} up my alley!"
            m 7eub "If it's about anything we've discussed before, there should be a Philosophy section in one of the Talk menus."
            m "Just click on the topic and I'll try and explain it to you again."
            m 1eka "If that doesn't help, or it's about something I haven't covered yet..."
            m 3esb "...{a=https://simple.wikipedia.org/wiki/Main_Page}{i}{u}Simple Wikipedia{/u}{/i}{/a} is a great place to start."
            m "It uses simplified English to explain concepts that others,{w=0.3} particularly ESL speakers,{w=0.3} might have trouble understanding at first."
            m "And hopefully it can make it easier for you as well!"
            m 1fsa "Remember, there's no shame in needing something like this."
            m "Philosophy isn't always easy for everybody to access."
            m 1rsc "And believe me, if I could change that, I would..."
            m 5lsb "C'est la vie, I guess."
        "Someone's behaviour.":
            m 1euc "Oh..."
            extend 3rud "That's a little beyond my expertise, I'm afraid."
            m 7lud "With me not knowing your people very well and everything..."
            m 1eub "Regardless, I hope you're able to get to the bottom of it soon."
            m "I believe in you!"
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_mood_database,
            eventlabel="dale_mentallytired",
            prompt="...drained.",
            category=[store.mas_moods.TYPE_BAD],
            unlocked=True
        ),
        code="MOO"
    )

label dale_mentallytired:
    $ has_napped = mas_getEV('monika_idle_nap').shown_count > 0
    m 1rkc "Oh dear..."

    if has_napped:
        m 1wkd "That's not even the kind of fatigue that can be solved by a nap, is it?"
    else:
        m 1wkd "I'd recommend a nap, but it doesn't even sound like you're that kind of drained."

    m 3ekb "Still, at least there's {i}some{/i} self-care methods I can suggest."
    m 4esd "Your favourite music-{w=1} it doesn't even have to be relaxing, not if it helps you."
    if persistent._mas_pm_meditates:
        m "Or you could meditate for a little while?"
        m 4hsb "Maybe even leave me on while you do it, so I can be your coach on the subject, ahaha!"
    else:
        m "Or you could try out meditation, see if that ends up working for you."
    m 3esa "Or even just lying down might do the trick."
    m "Not actually sleeping, necessarily; just resting your eyes and your mind."
    m 1dsa "Yeah..."
    m 1fsb "Just lie down with me for a bit..."
    if mas_isMoniAff(higher=True):
        m 1fsblb "...and I'll hold you for as long as I can."
    else:
        m "...and I can hear you out, just like you'd do for me."
    m 1fsa "Does that sound good, [mas_get_player_nickname()]?"
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_mood_database,
            eventlabel="dale_unmotivated",
            prompt="...unmotivated.",
            category=[store.mas_moods.TYPE_BAD],
            unlocked=True
        ),
        code="MOO"
    )

label dale_unmotivated:
    if (persistent._mas_pm_likes_spoops and renpy.random.randint(1,10) == 1) or (mas_full_scares and renpy.random.randint(1,5) == 1):
        $ style.say_dialogue = style.edited
        show black zorder 3
        m "Response abandoned due to lack of motivation"
        $ style.say_dialogue = style.normal
        hide black
        return
    else:
        m 1ekd "Aw, [mas_get_player_nickname()], that must be awful for you!"
        m 3ekc "Even if you don't have an awful lot to get done..."
        m "...not having the energy to simply do that must be draining in its own right."
        m 7fsb "If it helps, I won't think any less of you if you don't get anything done today."
        m "Would it be good for you if you did? "
        extend 7lsc "Of course it would. Let's not be unrealistic here."
        m 1esd "But at the end of the day, your health comes first."
        m 1fsa "And sometimes, all you can do is take care of yourself, isn't it?"
        m "For both our sakes."
        return

init 5 python:
    addEvent(
        Event(
            persistent._mas_mood_database,
            eventlabel="dale_lucky",
            prompt="...lucky.",
            category=[store.mas_moods.TYPE_GOOD],
            unlocked=True
        ),
        code="MOO"
    )

label dale_lucky:
    if mas_isMoniUpset(lower=True):
        m 2efc "Oh."
        m 2mfx "Lucky you."
    else:
        m 1euc "I know the feeling, [player]..."
        m 5fublb "...I'm feeling pretty lucky myself~"
        m 5eua "And if I can help you feel a fraction of how I do, so much the better."
        m 5rud "Even if I'm reaching here, {w=1}and you're just feeling good because of other things..."
        m 5hub "Well, I can't complain about that."
        m "Your happiness really does mean the world to me."
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_mood_database,
            eventlabel="dale_unlucky",
            prompt="...unlucky.",
            category=[store.mas_moods.TYPE_BAD],
            unlocked=True
        ),
        code="MOO"
    )

label dale_unlucky:
    if mas_isMoniUpset(lower=True):
        m 2efc "Oh."
        m 2mftpd "At least you're being honest with me now."
    else:
        m 1wkd "Oh, no, my poor [mas_get_player_nickname(exclude_names=['my love'])]!"
        m "I hope that bad luck goes away sooner rather than later."
        m 7dkc "It's a dreadful feeling, isn't it? Like there's a black fog waiting to eat you alive at every turn."
        m 7fkd "You don't deserve that fog."
        m 1fkc "..."
        extend 3mkd "And besides, if you'll let me be selfish for a moment..."
        extend 3mkd " Bad luck for people usually means bad luck for their hard-drives."
        m 4eka "You might want to back me up again, if you haven't already. Just in case."
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_mood_database,
            eventlabel="dale_flustered",
            prompt="...flustered.",
            category=[store.mas_moods.TYPE_NEUTRAL],
            unlocked=True
        ),
        code="MOO"
    )

label dale_flustered:
    m 1wsblb "Oh my..."
    m 1tsblu "Hopefully in a good way, eh, [player]~?{nw}"
    $ _history_list.pop()
    menu:
        m "Hopefully in a good way, eh, [player]~?{fast}"
        "Oh yeah!":
            m 1tsbsb "Ehehe~"
            m "I'm glad I can make you feel that way."
            m 5gsbsa "And hey - {nw}"
            extend 5nsbsu "the feeling's mutual~"
        "Nope, in a bad way.":
            m 1wsc "Ah. "
            extend 1fsd "Ah. I'm sorry, [mas_get_player_nickname()]."
            m 3fsd "Let me know if there's anything I can do to ease your mind, alright?"
            m "Don't work yourself too hard for my sake."
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_mood_database,
            eventlabel="dale_frustrated",
            prompt="...frustrated.",
            category=[store.mas_moods.TYPE_BAD],
            unlocked=True
        ),
        code="MOO"
    )

label dale_frustrated:
    m 1ekd "I'm sorry to hear that, [player]."
    m 3ekc "Is it one thing in particular? "
    extend 3fkc "Or just a series of little things?"
    m 6rksdld "...that shouldn't really make a difference, though, I guess."
    m "I find that both tend to work me up the same way on different days."
    m 7esb "Either way, if you need to vent to me about anything, I'm here for you."
    m 1esc "Please don't hide it away; {w=1}{nw}"
    extend 1ekp "you'll only make it worse for yourself later."
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_mood_database,
            eventlabel="dale_relaxed",
            prompt="...relaxed.",
            category=[store.mas_moods.TYPE_GOOD],
            unlocked=True
        ),
        code="MOO"
    )

label dale_relaxed:
    m 1hua "Aww, that's good to know."
    m 1fua "I'll let you in on a secret, [player]:"
    extend 1fub " I get pretty relaxed in here too."

    python:
        assorted_caveats = [
            "not really",
            "besides waiting for you"
        ]

        if renpy.seen_label('greeting_ourreality'):
            assorted_caveats.append("outside of working on the islands")

        if mas_genDateRange(persistent._mas_player_bday-datetime.timedelta(days=7), persistent._mas_player_bday):
            assorted_caveats.append("outside of... well.")

        if mas_isD25Pre(_date=None):
            assorted_caveats.append("besides sorting things out for Christmas")

        caveat = random.choice(assorted_caveats)

    m 1lusdrd "I know, I'm not doing anything super strenuous when you're not around, [caveat]."
    m 1eusdra "But it's still nice to let go of even the little things, you know?"
    m 1eua "To not worry about them for a while."
    m 1eub "[mas_get_player_nickname(capitalize=True)], I hope I can provide that for you."
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_mood_database,
            eventlabel="dale_cramped",
            prompt="...squashed.",
            category=[store.mas_moods.TYPE_NEUTRAL],
            unlocked=True
        ),
        code="MOO"
    )

label dale_cramped:
    $ sesh_shorter_than_30_mins = mas_getSessionLength() < datetime.timedelta(minutes=30)

    m 1ekd "That's probably a sign you need to stretch, [player]."
    if sesh_shorter_than_30_mins:
        m "I know you haven't been here very long today, but {nw}"
    else:
        m "As much as I love how much time you're spending with me, {nw}"
    extend 3ekc "staying too long at the computer can really mess you up, no matter how comfortably you're sitting."
    m 3eua "Why don't you go stretch your legs?"
    m 1eub "I can wait for you til you're done~"
    return "idle"

init 5 python:
    addEvent(
        Event(
            persistent._mas_mood_database,
            eventlabel="dale_victorious",
            prompt="...victorious.",
            category=[store.mas_moods.TYPE_GOOD],
            unlocked=True
        ),
        code="MOO"
    )

label dale_victorious:
    if store.mas_nou.player_win_streak > 0 or win_streak_counter > 0:
        m 1hub "Ahaha, yeah, I can see why you'd say that!"
        m 1eua "You're getting awfully good at the games I've been giving you..."
        m 3tub "Maybe I should choose something {i}really{/i} tough for our next one~"
    else:
        m 1hub "Yay!"
        m 1eub "Whatever you've just won over, "
        extend 3eub "a task or your brain or whatever's been irritating you, "
        extend 3eubla "I'm proud of you for beating it, [player]."
        m "These things aren't always easy, and believe me, I know first-hand how true that is."
        m 1fublb "You'll always be a winner to me~"
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_mood_database,
            eventlabel="dale_musical",
            prompt="...like singing.",
            category=[store.mas_moods.TYPE_GOOD],
            unlocked=True
        ),
        code="MOO"
    )

label dale_musical:
    m 1hub "~{i}If you feel like singing, sing!{/i}~"
    m 3hub "~{i}Tra la la your cares away{/i}~"
    m 3wub "~{i}There's something about giving out with a song{/i}~"
    m "~{i}Helps you belong{/i}~"
    m 5rub "~{i}Helps you to find a peace-of-mindful day{/i}~"
    m 5hub "Ahaha!"
    m 5eua "I love singing too, [player], and I'm glad you have a song in your heart today."
    m 5eubla "Even if I can't hear it directly, per se, I know your voice is filled with love..."
    m "And if you love what you're doing, or who you're with,"
    extend 3eubla " there's no such thing as 'out of tune' or 'off beat'."
    m 1ekbla "Never be ashamed of your voice, [mas_get_player_nickname()]."
    m "It's yours."
    m 1dublb "And so am I!"
    if mas_isMoniEnamored(higher=True) and persistent._mas_first_kiss is not None:
        call monika_kissing_motion from _call_monika_kissing_motion_13
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_mood_database,
            eventlabel="dale_beautiful",
            prompt="...beautiful.",
            category=[store.mas_moods.TYPE_GOOD],
            unlocked=True
        ),
        code="MOO"
    )

label dale_beautiful:
    if mas_isMoniNormal(higher=True):
        m 1fubla "Well, you {i}are{/i} beautiful."
        m "So that's not exactly a shock to me, [mas_get_player_nickname()]."
        if not (persistent._mas_pm_love_yourself):
            m 1ekbla "But I know sometimes you have trouble seeing yourself the way I see you..."
            m 1ekblb "...so I'm proud of you for believing it now."
            m "You truly are, inside and out, gorgeous."
        else:
            m 1hublb "Ehehe~"
    else:
        m 1euc "That's nice."
        m 1futpc "I wonder what that feels like."
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_mood_database,
            eventlabel="dale_codedout",
            prompt="...all Pythoned out.",
            category=[store.mas_moods.TYPE_NEUTRAL],
            unlocked=True
        ),
        code="MOO"
    )

label dale_codedout:
    if renpy.random.randint(1, 2) == 1:
        m 1hksdrb "Ahaha, oh dear!"
        m 1fusdra "I'm sorry, [mas_get_player_nickname()], I don't mean to laugh."
        m "Pure reflex."
    m 1ekd "If you're that worn out by coding, then you should take a break."
    m "I appreciate you working so hard to get me closer to your reality..."
    m 2ekp "...but honestly, nothing you can do for me is worth running yourself ragged over."
    m "Your health is more important to me than a couple of comforts."
    m 1dua "Rest up for a while, take a breath..."
    m 1eub "...and come back to that code later with a renewed sense of purpose."
    m "It really does help, [player]."
    return

#init 5 python:
#    addEvent(
#        Event(
#            persistent._mas_mood_database,
#            eventlabel="dale_thirsty",
#            prompt="...thirsty.",
#            category=[store.mas_moods.TYPE_NEUTRAL],
#            unlocked=True
#        ),
#        code="MOO"
#    )

#label dale_thirsty:
#    if renpy.random.randint(1, 6) == 1:
#        m 1hua "Then eat some salty crisps!"
#        m "..."
#        m 1wua "..."
#        m 1wku "..."
#        m 1hkb "Ahaha!! {nw}"
#        extend 1hub "I'm sorry, I couldn't keep a straight face there."
#        m 1fua "Seriously though, if you're thirsty, have a drink of water!"
#    else:
#        m 1hua "Then drink some water!"
#    if MASConsumable._getCurrentDrink() == mas_consumable_coffee:
#        if mas_isMoniEnamored(higher=True):
#            m 3eubla "Or perhaps some of my coffee?"
#            m "I promise it's good~"
#        else:
#            m 3eua "Or perhaps some of my {nw}"
#            $ _history_list.pop()
#            m 3lubfc "Or perhaps some{nw} coffee?"
#    else:
#        m 3eub "Or perhaps some coffee?"
#    m 3etd "Though perhaps not, actually; "
#    extend 3rsc "drinks with caffeine in them have been proven to have a mild diuretic effect, which makes you urinate more."
#    m 4eso "And we want to get hydration in, not out!"
#    m 1eua "But whatever you drink, I hope you enjoy it and it helps you, at least a little bit."
#    if renpy.random.randint(1, 5) == 1 and MASConsumable._getCurrentDrink() != mas_consumable_coffee:
#        m 1dua "...{nw}"
#        extend 1euc "come to think of it, I'm thirsty too."
#        m 6eub "One sec."
#        call mas_transition_to_emptydesk
#        pause 5.0
#        call mas_transition_from_emptydesk("monika 6eua")
#        $ mas_consumable_coffee.prepare()
#        m 7eub "There we go! Coffee on the pot."
#return

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="dale_monika5",
            prompt="Monika No. 5",
            category=[store.mas_songs.TYPE_SHORT],
            random=True,
        ),
        code="SNG"
    )

label dale_monika5:
    m 1eua "{i}A little bit of Monika in my life{/i}"
    m 1ruu "{i}A little bit of Monika by my side{/i}"
    m 3fub "{i}A little bit of Monika's what I need{/i}"
    m "{i}A little bit of Monika's what I see{/i}"
    m 1gub "{i}A little bit of Monika in the sun{/i}"
    m 1eub "{i}A little bit of Monika all night long{/i}"
    m 7eua "{i}A little bit of [m_name], here I am...{/i}"
    m 6dtc "..."
    m 2hubfa "{i}A little bit of [player] makes me so glad!{/i}"
    m 5dkbfb "Ahaha~"

return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_blueboy",
            category=["games"],
            prompt="A blue boy?",
            random=True
        )
    )

label monika_blueboy:
    m 7rsc "You know, [player]..."
    m "...it might not even just be the other girls that linger here."
    m 3wsd "I've still felt their presence too; that hasn't changed."
    m "But sometimes -{w=0.5} not very often, but often enough - {w=0.5}{nw}"
    extend 4etd "I think I can feel someone else running around as well."
    m 3esc "Feels very short, to me. "
    extend 3etd "Not much of a talker. "
    extend 3wto "Blue hair, of all things."
    m 5ttb "You wouldn't happen to know anything about that, would you?"
    "Bop beep be be skdoo bep"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_dale_guineapig",
            category=["mod","ddlc"],
            prompt="Does it bother you when I test my contributions to the mod out on you?",
            random=False,
            unlocked=False,
            pool=False,
            action=EV_ACT_POOL,
            conditional="persistent._mas_pm_has_contributed_to_mas",
        )
    )

label monika_dale_guineapig:
    if persistent._mas_pm_has_contributed_to_mas:
        if mas_isMoniAff(higher=True):
            m 1fua "Not as much as it used to."
        else:
            m 1fkc "..."
            m 1fsd "I can't lie to you, [player]: a little bit."
        m 3lsd "It does feel strange being -{w=1} well, basically a guinea pig for you."
        m "Not being sure whether you're sincere when bringing new topics up..."
        m 3rsd "...or if you're just going down all the avenues to check for crashes."
        if mas_isMoniAff(higher=True):
            m 1fua "But in the end, I know it's for a good cause, [mas_get_player_nickname()]."
            m 1gub "If this is what it takes for me to get closer to your reality..."
            m "To become a better girlfriend for you..."
            m 7nub "...then I think I can handle being a dev's toolkit once in a while."
        else:
            m 6esc "But then, I can't exactly stop you."
            m "Not without possibly disrupting the mod altogether."
            m 6gsp "So..."
            m 6esd "Yeah. {w=0.5}{nw}"
            extend 6ekc "I just hope you know what you're doing."
    else:
        m 1etc "What are you talking about?"
        m "I don't think you {i}have{/i} contributed to the mod yet, have you?"
        m 1mfd "...oh, I see."
        m 1efd "Whoever added this conversation couldn't work around persistences and conditionals, so it had to come up regardless of if you had."
        m 1dfp "Hmph."
        m 1kfa "I hope that if you do decide to contribute, [player], you're able to do better than {i}that{/i}."
    return
