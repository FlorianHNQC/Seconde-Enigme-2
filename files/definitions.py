## Character Definitions #######################################################
#student
define t = Character("Takagi-san", color ="#ff9cb5") ## Takagi
define n = Character("",color ="#FFF") #Left as blank bc it is used in nameSelect
define k = Character("Kimura", color ="#318fb5") ## Kimura
define nka = Character("Nakai", color ="#318fb5") ## Nakai
define takao = Character("Takao", color ="#318fb5") ## Takao
define smr = Character("Sumire-san", color ="#ff9cb5") ## Sumire
define mano = Character("Mano-san", color ="#ff9cb5") ## Mano

#other
define na = Character(what_italic=True) ## narrator
define utchr = Character("???",color ="#318fb5") #unknown teacher
define pchar = Character("???", color ="#ff9cb5") #Pink unknown character
define tchr = Character("Tanabe-Sensei",color ="#318fb5")
define ev = Character("Everyone",color ="#FFF") ## everyone
define ol = Character("Old Lady", color ="#efbbcf") ## Old Lady
define mom = Character("Mom", color ="#efbbcf") ## Nishikta's Mom
define tkmom = Character("Takagi's Mom", color ="#efbbcf") ## Takagi's Mom

## Audio #######################################################################
## Sound effects
## TODO 23 Remove the #comment for the sound effects
#define audio.se1 = "audio/se/se1.ogg" #kiss

## BGM
define audio.EverydayLife = "<loop 0>audio/Everyday.ogg"
define audio.CriticalHit = "<loop 0>audio/CriticalHit.ogg"
define audio.SunnyHome = "<loop 0>audio/A-sunny-way-home.ogg"

define audio.a1 = "<loop 0>audio/1.ogg"
define audio.a2 = "<loop 0>audio/The-distance-between-us.ogg"

## Chapter 1 audio

define audio.c1 = "<loop 0>audio/1-1.ogg"
define audio.c1_2 = "<loop 0>audio/1-2.ogg" # 36 Candy Store
define audio.c1_3 = "<loop 0>audio/1-3.ogg" # 12 If you look closely takagi-san


## init ########################################################################
##Python variables

## persistent name
init python:
    n = Character("[persistent.customName]", color ="#FFF")
    name = n.name

## Right click as hide textbox
init:
    $ config.keymap['hide_windows'].append('mouseup_3') # To hide text on right click
    $ config.keymap['hide_windows'].remove('mouseup_2') # To remove keymapping of middle mouse button

##############################
#Shortcut calls for Transitions
##############################

init:
    $ ds01 = Dissolve(0.1)
    $ ds02 = Dissolve(0.2)
    $ sds = Dissolve(1.2) # Slow Dissolve

## Images ######################################################################
#/// Chapter SELECTION ///#
image ChSlBackground = im.Scale("images/chapter_select/background.png", 1280,720)

#///only a test///#
image mint test = "images/test.jpg"

#/// Character Creation ///#
image btn = im.Scale("gui/btn.png", 1280,720)

#hover button
image btnh = im.Scale("gui/btnh.png", 1280,720)

image nameqstn = im.Scale("gui/question.png", 1280,720)

image wyname = im.Scale("gui/wyname.png", 1280,720)

image wynameEmpty = im.Scale("gui/wynameEmpty.png", 1280,720)
#blurred bg of main menu
image blrdBG = im.Scale("gui/blurred.png", 1280,720)


################################################################################

#/// Splash screen logo ///#

transform logo_move_toleft:
    xalign 1.0 yalign 0.5
    rotate 0
    linear 1.0 xalign 0.3 rotate -360

image splash_logo = im.Scale("images/Logo.png", 278,277)

image splash_team_name:
    xalign 0.67
    yalign 0.5
    im.Scale("images/team_name.png", 412,265)

image splash_desc:
    xalign 0.5
    yalign 0.9
    Text("Giving the world a bundle of Sunshine.", size=20, color ="#000000")

image Disclaimer:
    xalign 0.5
    yalign 0.5
    Text("This is an unofficial fan work, Unaffiliated with Soichiro Yamamoto and Shin-Ei Animation.", size=26, color ="#000000")

#/// After splashscreen, press to start logo ///#
image press_to_start_logo = im.Scale("TLogo.png", 1280,720)

image click_to_start:
    xalign 0.5
    yalign 0.9
    Text("Press to start.", size=24, color ="#000000")

image titles= im.Scale("main_menu.png", 1280, 720)
image bg titles= im.Scale("main_menu.png", 1280, 720)
image black = "#000000"
image white = "#ffffff"

image dot:
    "dot.png"

##Preview images for creative visualization
##please ignore
### Takagi beach scenes
#image bg sc1 = im.Scale("1.png", 1280,720)
#image bg sc2 = im.Scale("2.png", 1280,720)

## Items & Dramatic Scenes
# handkerchief
image handkerchief_g = im.Scale("items/handkerchief_g.png", 1280,720)
image handkerchief_on_hand_blank = im.Scale("items/handkerchief_blank.png", 1280,720)
image handkerchief_close = im.Scale("items/handkerchief_close.png", 1280,720)
image handkerchief_close_fadein:
    im.Scale("items/handkerchief_close.png", 1280,720)
    on show:
        xpos 640 ypos 800 alpha 0 # We set the initial position, and visibility
        linear 1 xpos 640 ypos 720 alpha 1.0 # In a 1s interval, it moves to the new position, with a fadein in animation

# as scene
image bg handkerchief_scene = im.Scale("items/handkerchief_scene.png", 1280,720)

# blurred classroom
image bg b_classroom = im.Scale("sc/blurred_classroom_morning.png", 1282,720)


## Locations
#street
image bg streets_day = im.Scale("sc/streets-day.png", 1280,720)
image bg streets_afternoon = im.Scale("sc/streets_afternoon.png", 1280,720)
image bg shrine_s = im.Scale("sc/shrine_s.png", 1280,720)
image bg streets_seaside = im.Scale("sc/bg01.png", 1280,720)
#image bg c_park = im.Scale("sc/childrens_park_day.png", 1280,720)

##house
image bg nishi_room = im.Scale("sc/nishi-room.png", 1280,720)
image bg kitchen = im.Scale("sc/kitchen.png", 1280,720)
image bg tk_house = im.Scale("sc/tk-house.png", 1280,720)
image bg living_room = im.Scale("sc/lv_room.png", 1280,720)


#school
image bg school_gate = im.Scale("sc/school_gate_2.png", 1280,720)
image bg inside school_gate = im.Scale("sc/school_gate_inside.png", 1280,720)
image bg corridor = im.Scale("sc/corridor.png", 1280,720)
image bg bike_park = im.Scale("sc/bike-park.png", 1280,720)
image bg classroom_morning = im.Scale("sc/classroom_morning.png", 1280,720)
image bg s_classroom = im.Scale("sc/sunset_classroom.png", 1280,720)
image bg school_gymnasium = im.Scale("sc/gymnasium.png", 1280,720)


## Credits screeen
define audio.ed = "<loop 0>audio/ed.ogg"
image bg grass = im.Scale("credits/grass.png", 1280,720)
image cr1 = im.Scale("credits/1.png", 1280,720)
image cr2 = im.Scale("credits/2.png", 1280,720)
image cr3 = im.Scale("credits/3.png", 1280,720)
image cr4 = im.Scale("credits/4.png", 1280,720)
image cr5 = im.Scale("credits/5.png", 1280,720)
image cr6 = im.Scale("credits/6.png", 1280,720)
image cr7 = im.Scale("credits/7.png", 1280,720)
image cr8 = im.Scale("credits/8.png", 1280,720)
image cr9 = im.Scale("credits/9.png", 1280,720)
image cr91 = im.Scale("credits/9-1.png", 1280,720)
image cr92 = im.Scale("credits/9-2.png", 1280,720)
image cr10 = im.Scale("credits/10.png", 1280,720)

## Work in Progress Text
image WorkInProgress:
    xalign 0.2
    yalign 0.71
    alpha 0.3
    Text("Work in Progress", font=font1, size=46, color ="#ffffff")

## Character Sprites ###########################################################
## I tried arranging the sprites by usage and I created spaghetti code instead.
## Rip in peace.

transform transform_blink:
    linear 1.0 alpha 0.2
    linear 1.0 alpha 1.0
    repeat

transform slightright:
    xalign 1.25
    yalign 1.0

transform center:
    xalign 0.5
    yalign 1.0

#////////////////////////////// Takagi /////////////////////////////////////////

init:
    image tk leaning:
        "spr/tk/1.png"
        zoom 0.8

    image tk smug_o:
        "spr/tk/2.png"
        zoom 0.8

#Smug face / Gaming face
    image tk very_smugo:
        "spr/tk/3.png"
        zoom 0.8

    image tk very_smug:
        "spr/tk/4.png"
        zoom 0.8

    image tk smug:
        "spr/tk/5.png"
        zoom 0.8

    image tk poker_face:
        "spr/tk/6.png"
        zoom 0.8

#yes it's a poggers moment. now you're now my little pogchamp.
    image tk pog:
        "spr/tk/7.png"
        zoom 0.8

    image tk ts_4s:
        "spr/tk/8.png"
        zoom 0.75

    image tk ts_4:
        "spr/tk/9.png"
        zoom 0.75

    image tk ts_3s:
        "spr/tk/10.png"
        zoom 0.75

    image tk ts_3:
        "spr/tk/11.png"
        zoom 0.75

    image tk ts_2s:
        "spr/tk/12.png"
        zoom 0.75

    image tk ts_2:
        "spr/tk/13.png"
        zoom 0.75

    image tk ts_1s:
        "spr/tk/14.png"
        zoom 0.75

    image tk ts_1:
        "spr/tk/15.png"
        zoom 0.75

# Takagi with Bike
    image tk b_speaking:
        "spr/tk/16.png"
        zoom 0.8

    image tk b_smiling_open_mouth:
        "spr/tk/17.png"
        zoom 0.8

    image tk b_smiling:
        "spr/tk/18.png"
        zoom 0.8

    image tk bike:
        "spr/tk/19.png"
        zoom 0.8

    image tk smiling_closed_eyes:
        "spr/tk/20.png"
        zoom 0.7

#smiling but closed eyes
    image tk talking_closed_eyes:
        "spr/tk/21.png"
        zoom 0.7

# smile open mouth
    image tk eyes_open_talking:
        "spr/tk/22.png"
        zoom 0.7

# Takagi laughing out loud (lol)
    image tk lol:
        "spr/tk/23.png"
        zoom 0.8

# Leaning Takagi
    image tk lean_smile:
        "spr/tk/24.png"
        zoom 0.8

    image tk lean_speak:
        "spr/tk/25.png"
        zoom 0.8

# Takagi speaking
    image tk spksmile:
        "spr/tk/26.png"
        zoom 0.8

    image tk spk:
        "spr/tk/27.png"
        zoom 0.8

# Curious Takagi
    image tk crs1:
        "spr/tk/28.png"
        zoom 0.8

# Takagi Flustered
    image tf_s_1:
        "spr/tk/29.png"
        zoom 0.8

    image tf_1:
        "spr/tk/30.png"
        zoom 0.8

# Takagi in sunset
    image tk sunset_2:
        "spr/tk/31.png"
        zoom 0.8

    image tk sunset_1:
        "spr/tk/32.png"
        zoom 0.8

#////////////////////////////// Kimura /////////////////////////////////////////
    image kim t1:
        "spr/kimura/k1.png"
        zoom 0.7

#////////////////////////////// Tanabe /////////////////////////////////////////
    image tnb t1:
        "spr/tanabe/tn1.png"
        zoom 0.7



## text ########################################################################
define font1 = "fonts/RifficFree-Bold.ttf"

## Episode Title
image prologue_txt:
    ypos 380
    Text("Prologue", font=font1, size=70)

image Glico_txt:
    ypos 380
    Text("Glico", font=font1, size=70)

image EmpCans_txt:
    ypos 380
    Text("Empty Cans", font=font1, size=70)

image gift_txt:
    ypos 380
    Text("Gift", font=font1, size=70)

## End text
image end_txt:
    ypos 380
    Text("End", font=font1, size=70)
