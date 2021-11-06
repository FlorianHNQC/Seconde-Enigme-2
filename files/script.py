# The game starts here.

label splashscreen:
#TODO LINE 3 Unskippable: how the heck do I make these work
#    $ config.keymap['game_menu'] = []
#    $ config.keymap['hide_windows'] = []
#    $ renpy.display.behavior.clear_keymap_cache()
#    $ quick_menu = False
#    $ config.skipping = False
#    $ config.allow_skipping = False

    scene black
    with Pause(2)

    play music "audio/main-menu-theme.ogg"
    show white with fade
    show splash_logo at logo_move_toleft with Pause(0.28)
    show splash_team_name with wipeleft
    pause 0.2
    show splash_desc with Dissolve(0.1)
    with Pause(3)
    scene white with Dissolve(0.070)
    show Disclaimer with Dissolve(0.010)
    with Pause(3)
    scene white with fade
    with Pause(0.010)
    # jump credits_screen # Uncomment to test credits screen

    return

label before_main_menu:
    scene white
    with Pause(0.010)
    scene titles with dissolve

    # Example of achievement unlocked after getting 50 points. Defined in definitions.rpy
    python:
        add(10) # It doesn't show anything
        add(49) # It reaches 50 points, so it shows


    with Pause(0.010)
    call screen press_to_start
    return

label start:
    $ quick_menu = False
    scene white with ds01
    scene blrdBG with dissolve
    pause 0.5
    $ renpy.call_screen("nameCreate")
    stop music fadeout 2
    #jump glico
    return

label end_game:
    $ quick_menu = False
    stop music fadeout 2
    scene black with fade
    show end_txt zorder 50
    with Dissolve(1.0)
    pause 4.0
    scene white with fade
    with Pause(0.010)
    scene titles with dissolve
    $ quick_menu = True
    $ renpy.end_replay()
    $ MainMenu(confirm=False)()
    return

################################################################################

label credits_screen:
    $ quick_menu = False

    define show_name = ""
    if (persistent.customName == "Nishikata"):
        $ show_name = "You, The Player."
    else:
        $ show_name = "[n]"

    image end_game_name:
        ypos 380
        Text(show_name, font=remissis, size=70, color ="#291542",outlines=[ (3, "#FFF",0,0)])

    stop music fadeout 2
    scene black with dissolve

    show end_game_name with dissolve

    pause 2.0
    play music ed
    scene white with dissolve
    show splash_logo at logo_move_toleft with Pause(0.28)
    show splash_team_name with wipeleft
    pause 0.2
    show splash_desc with Dissolve(0.1)
    pause 2.52
    scene white with dissolve
    pause 0.3
    scene grass with dissolve

    show cr1 with dissolve
    pause 4

    hide cr1 with dissolve
    show cr2 with dissolve
    pause 4

    hide cr2 with dissolve
    show cr3 with dissolve
    pause 4

    hide cr3 with dissolve
    show cr4 with dissolve
    pause 4

    hide cr4 with dissolve
    show cr5 with dissolve
    pause 4

    hide cr5 with dissolve
    show cr6 with dissolve
    pause 4

    hide cr6 with dissolve
    show cr7 with dissolve
    pause 4

    hide cr7 with dissolve
    show cr8 with dissolve
    pause 4

    hide cr8 with dissolve
    show cr9 with dissolve
    pause 0.5
    show cr91 with dissolve
    pause 0.5
    show cr92 with dissolve
    pause 4

    hide cr91 with dissolve
    hide cr92 with dissolve
    pause 1

    show end_game_name zorder 50
    with dissolve
    pause 4

    hide cr9 with dissolve
    hide end_game_name with dissolve


    show 10 with dissolve
    pause 5
    stop music fadeout 3
    scene white with Dissolve(4.0)

    return
$
