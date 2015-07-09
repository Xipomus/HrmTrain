label howtoplay:
    $ end_u_1_pic =  "title3.jpg" #<---- SCREEN
    show screen end_u_1                                             #<---- SCREEN
    play music "music/silly_fun_loop.mp3" fadein 1 fadeout 1 # LOLA'S THEME.
    if not persistent.tut: #Turns TRUE after tutorial happened once already. EVENT_01
        
        
        
        
        $ lola_face = "03_hp/22_lola/01.png"
        $ lola_body = "03_hp/22_lola/body_01.png"
        
        $ l_things = True
        #$ l_blush = True
        $ lx = 490
        $ ly = 190
        show screen l_head
        l "Привет интернет-извращугам!"
        hide screen l_head
        a5 "Следи за языком, сучка!"
        $ l_things = False
        $ lola_face = "03_hp/22_lola/02.png"
        show screen l_head
        l "Хах...?"
        hide screen l_head
        a6 "Что я тебе говорил о слове на букву \"и\"?"
        $ l_question = True
        $ lola_face = "03_hp/22_lola/03.png"
        show screen l_head
        l "Эм... Использовать его как можно чаще..?"
        hide screen l_head
        pause.01
        with hpunch
        a7 "{size=+7}Нет!{/size}"
        $ l_question = False
        $ l_drop = True
        $ lola_face = "03_hp/22_lola/04.png"
        show screen l_head
        l "Гх!"
        hide screen l_head
        pause.01
        with hpunch
        a7 "{size=+7}Мы не используем его! Никогда!{/size}"
        $ lola_face = "03_hp/22_lola/01.png"
        $ l_drop = False
        show screen l_head
        l "Потому что самый самый большой здесь папочка?"
        hide screen l_head
        a6 "Гх!"
        a6 "Тебе понравилось сниматься в \"Тренер Принцессы\"?"
        $ l_hearts = True
        $ lola_face = "03_hp/22_lola/01.png"
        show screen l_head
        l "Лучшее событие в моей жизни!"
        hide screen l_head
        a1 "Хочешь попасть в \"Золотое издание\"?"
        $ l_hearts = False
        $ lola_face = "03_hp/22_lola/05.png"
        show screen l_head
        l "!!!"
        $ lola_face = "03_hp/22_lola/06.png"
        show screen l_head
        l "Дамы и гопода, добро пожаловать в обучающий режим \"Тренера Гермионы\"."
        hide screen l_head
        a1 "Умница, девочка."
        $ l_drop = True
    else: # EVENT_02
        $ lx = 490
        $ ly = 190
        $ lola_body = "03_hp/22_lola/body_01.png"
        $ lola_face = "03_hp/22_lola/05.png"
        show screen l_head
        l "Хм...?"
        l "Ты хочешь прослушать обучение снова?"
        $ lola_face = "03_hp/22_lola/09.png"
        l "Хм...."
        $ lola_face = "03_hp/22_lola/11.png"
        l "Ты не смущен?"
        $ lola_face = "03_hp/22_lola/10.png"
        l "Хм..."
        $ l_things = True
        $ lola_face = "03_hp/22_lola/08.png"
        l "*Хихикает!*"
        $ l_things = False
        $ lola_face = "03_hp/22_lola/01.png"
        l "Ты хочешь, чтобы я учила тебя топлесс?"
        hide screen l_head
        $ d_flag_01 = False
        menu:
            "\"Еще бы!\"":
                $ lola_face = "03_hp/22_lola/01.png"
                show screen l_head
                
                $ d_flag_01 = True
                l "Океюшки!"
                hide screen l_head
                pause.1
                show screen blkfade 
                with d3
                $ lola_body = "03_hp/22_lola/body_02.png"
                $ l_blush = True
                pause.5
                hide screen blkfade
                with d7
                
                
            "\"Нет.\"":
                $ lola_face = "03_hp/22_lola/12.png"
                show screen l_head
                l "Ты скучный..."
                $ lola_face = "03_hp/22_lola/09.png"
                l "Ладно, пофиг..."

                   
    ### THE TUTORIAL ###
    play music "music/Under-the-Radar by PhobyAk.mp3" fadein 1 fadeout 1 
    $ lola_face = "03_hp/22_lola/06.png"
    show screen l_head
    l "Вот краткий перечень вещей, которые стоит помнить..."
    with hpunch
    $ end_u_1_pic =  "03_hp/22_lola/tut_02.png" #<---- SCREEN
    $ renpy.play('sounds/boing02.mp3')   

    l "Гермиона захочет продавать сексуальные услуги в обмен на очки факультета, когда Гриффиндор отстает."
    
    with hpunch
    $ end_u_1_pic =  "03_hp/22_lola/tut_01.png" #<---- SCREEN
    $ renpy.play('sounds/boing02.mp3')   
    l "Дружба с профессором Снейпом увеличит количество очков, получаемых Слизереном."
    with hpunch
    $ end_u_1_pic =  "03_hp/22_lola/tut_03.png" #<---- SCREEN
    $ renpy.play('sounds/boing02.mp3') 
    if d_flag_01: # TOPLESS.
        $ lola_face = "03_hp/22_lola/07.png"
    l "Чтение образовательных книг позволит тебе зарабатывать, но это по желанию."

    with hpunch
    $ end_u_1_pic =  "03_hp/22_lola/tut_04.png" #<---- SCREEN
    $ renpy.play('sounds/boing02.mp3') 
    l "Покупка одной и той же сексуальной услуги может привести к разным последствиям, в зависимости от того, как далеко Гермиона зашла в своих тренировках."
    $ lola_face = "03_hp/22_lola/06.png"

    with hpunch
    $ end_u_1_pic =  "03_hp/22_lola/tut_07.png" #<---- SCREEN
    l "Все услуги разделены на две группы: \"приватные услуги\" и\"публичные услуги\"."
    l "Приватные услуги оказываются в кабинете и не сильно влияют на репутацию Гермионы."
    l "Публичные услуги оказываются во время уроков за пределами экрана."
    l "Каждая публичная услуга, не считая последней, имеет девять концовок."
    l "Кстати, несмотря на то, что покупка приватных услуг - необходима для тренировки Гермионы, публичные услуги не обязательны."

    with hpunch
    $ end_u_1_pic =  "03_hp/22_lola/tut_05.png" #<---- SCREEN

    $ renpy.play('sounds/boing02.mp3') 
    l "Если обращаться с ней плохо, то настроение Гермиона ухудшится, она может обидеться и стать очень неподатливой..."
    l "Она остынет со временем, но ты можешь ускорить процесс, если подаришь ей что-нибудь..."
    
    with hpunch
    $ end_u_1_pic =  "03_hp/22_lola/tut_06.png" #<---- SCREEN
    $ renpy.play('sounds/boing02.mp3') 
    l "Здесь нет временных ограничений. Так что можешь играть в нее столько дней, сколько захочешь."
 
    
    
    
    $ end_u_1_pic =  "03_hp/22_lola/tut_00.png" #<---- SCREEN
    $ l_drop = False
    
    if not persistent.tut: # FIRST TIME TUTORIAL. Turns TRUE after tutorial happened once already. EVENT_01
        $ persistent.tut = True #Turns TRUE after tutorial happened once already.
        hide screen l_head
        a1 "Ладно, этого хватит..."
        $ l_question = True
        $ lola_face = "03_hp/22_lola/05.png"
        show screen l_head
        l "Как я справилась?"
        hide screen l_head
        a1 "Ты отлично поработала. Хорошая девочка."
        $ l_question = False
        $ l_things = True
        $ lola_face = "03_hp/22_lola/08.png"
        show screen l_head
        l "Хе-хе-хе. Лола хорошая девочка!"
        $ l_things = False
        $ lola_face = "03_hp/22_lola/01.png"
        show screen l_head
        l "А что я получу?"
        hide screen l_head
        a1 "А что ты хочешь?"
        $ lola_face = "03_hp/22_lola/10.png"
        show screen l_head
        l "Хм..."
        $ l_exclamation = True
        $ lola_face = "03_hp/22_lola/01.png"
        l "Мы можем сделать сцену изнасилования со мной в \"Золотом издании\"?"
        hide screen l_head
        a6 "Не испытывай мое терпения, девочка."
        $ l_exclamation = False
        $ l_drop = True
        $ lola_face = "03_hp/22_lola/04.png"
        show screen l_head
        l "Извини, папочка."
        $ l_drop = False
        hide screen l_head
        a5 "............"

    else: ### NOT FIRST TUTORIAL. EVENT_02
        if d_flag_01: #TOPLESS.
            hide screen l_head
            stop music fadeout 1.0
            a1 "Что здесь происходит?"
            $ lola_face = "03_hp/22_lola/14.png"
            $ l_drop = True
            show screen l_head
            l "Упс!"
            hide screen l_head
            a1 "Что я говорил тебе о раздевании перед незнакомцами?"
            $ lola_face = "03_hp/22_lola/04.png"
            show screen l_head
            l "Это важная часть взросления?"
            hide screen l_head
            a6 "Нет!"
            $ l_drop = False
            $ l_tears = True
            $ lola_body = "03_hp/22_lola/body_01.png"
            $ lola_face = "03_hp/22_lola/04.png"
            show screen l_head
            l "Папочка, мне так жаль!"
            l "Этот случайный чувак из интернета заставил меня, я клянусь!"
            hide screen l_head
            a1 "Обучение закончено."
            $ l_blush = False
            $ l_tears = False
            $ lola_face = "03_hp/22_lola/15.png"
            show screen l_head
            l "Хе-хе! Ты попался!"
        else:
            $ lola_face = "03_hp/22_lola/09.png"
            l "И, это..."
            $ lola_face = "03_hp/22_lola/13.png"
            l "Может быть в следующий раз?"
            
return

### ABOUT GAME ####
label abouttrainer:
    $ end_u_1_pic =  "title3.jpg" #<---- SCREEN
    show screen end_u_1                                             #<---- SCREEN
    play music "music/GrapeSodaIsFuckingRawbyjrayteam6.mp3" fadein 1 fadeout 1 
    
    a1 "Хм... Посмотрим..."
    a1 "Я начал работу над \"Тренером Гермионы\" сразу после релиза \"Тренера Принцессы\"."
    a1 "У меня была идея создать маленькую милую игру, на разработку которой уйдет не больше, чем пара месяцев."
    a1 "Как мы все знаем, это заняло у меня больше полугода..." 
    a1 "И несмотря на бесконечные компромиссы, мне пришлось просто-напросто закончить разработку, чтобы эта чертовщина не убила у меня еще больше времени."
    a1 "Порой работать над игрой было весело..."
    a1 "Но также были и трудности..."
    a1 "Иногда мне приходилось бороться с некотрыми идеями и игровыми механиками, которые не хотели работать правильно..."
    a1 "Также работа над этой игрой рассказала мне много о моих способностях как разработчик игр и моих слабостях."
    a2 "Мне почти кажется, что я должен получить медаль или грамоту за это."
    a1 "Ладно, я сваливаю в мой следующий проект. {size=-4}(\"Тренер Принцессы Золотое Издание\"){/size}"
    a1 "Спасибо за поддержку, парни. И я надеюсь, что эта игра сделала ваши будни хоть чуточку светлее."
    a2 "До следующего раза..."

    return

### F.A.Q. ###
label faq:
    $ end_u_1_pic =  "title3.jpg" #<---- SCREEN
    show screen end_u_1 
    with flashbb#<---- SCREEN
    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 
    
    a1 "Привет. Меня зовут Акабур. Я создатель игры и я здесь, чтобы ответить на твои вопросы." 
label faq2:    
    menu:
        "Как я могу поддержать тебя?":
            a1 "Ну, есть несколько способов..."  
            a1 "Самый простой способов написать мне (akaburfake2@yahoo.com) и дать мне знать, что тебе понравилась игра."
            a1 "Также ты можешь поддержать меня лично на {a=http://www.patreon.com/akabur}www.patreon.com/akabur{/a}"
            a1 "Еще один способ поддержать меня это перейти по этой ссылке: {a=http://akabur.hentaiunited.com}akabur.hentaiunited.com{/a}."
            a1 "У таких независимых художников как я каждый бакс на счету..."
            a6 "Серьезно. Из-за моего стиля жизни, гребанный банк все еще не может выдать мне кредитную карту..."
#            label payments:
#            menu:
#                "-WebMoney info-":
#                    a1 "My RUBLES WebMoney purse: R133931000745"
#                    a1 "My USD WebMoney purse: Z319925489258"
#                    a1 "My EURO WebMoney purse: E800599783938"
#                    jump payments
#                "-YandexMoney Info-":
#                    a1 "My Yandex Purse Number: 41001849167270"
#                    jump payments
#                "-PayPal Info-":
#                    a1 "Contact me via email and i will give you my PayPal."
#                    jump payments
#                "-Credit Card-":
#                    a1 "Here: {a=http://www.test.akabur.com/donate}how to donate with Credit Card.{/a}"
#                    jump payments
#                "-Cancel-":
#                    jump faq2
            jump faq2
            
        "Как оставаться в курсе?":
            a1 "Ну, перейти по этой ссылке: {a=http://akabur.hentaiunited.com}akabur.hentaiunited.com{/a} и подписаться. Или посетить мой сайт: {a=http://akabur.com}akabur.com{/a}."
            a1 "Еще, конечно есть Patreon {a=http://www.patreon.com/akabur}www.patreon.com/akabur{/a}.\nи {a=https://twitter.com/AKABUR}мой twitter{/a}." 
            jump faq2
        "У меня есть другой вопрос.":
            a1 "Если у тебя есть вопрос, который не вошел в этот \"F.A.Q.\", не стесняйся и пиши: akaburfake2@yahoo.com"
            a1 "Или оставь вопрос здесь: {a=http://ask.fm/AKABUR}ask.fm/AKABUR{/a}"
            jump faq2
        "Я хочу сообщить о баге/ошибке.":
            a1 "Эта игра тестировалась много много много раз, но лучшими тестерами всегда были и остаются игроки."
            a1 "Так что, если вы встретили баг - пишите мне (akaburfake2@yahoo.com) и я исправлю проблеиу в следущей версии игры."
            jump faq2
        "Кто помог тебе создавать игру?":
            a1 "Никто не помогал мне! Я сделал все сам!"
            a1 "Я сам написал все скрипты, нарисовал все арты, и сыграл всю музыку!"
            a7 "Я! {size=+3}Я! {size=+3}Я создал все! {size=+3}Я!{/size}"
            a2 "Хех..."
            a1 "Ну, по правде, я сделал большую часть работу. Но мне много помогали."
            a1 "Мой друг и коллега Dahr обеспечил меня благородно (и бесплатно) разными художествами (помимо всего прочего)."
            a1 "Не бойтись кинуть парню монетки или две на {a=http://www.patreon.com/DAHR}www.patreon.com/DAHR{/a}"
            a1 "Xaljio всегда был рядом, когда у меня были проблемы с коддингом. (частенько). Посетите его страничку - {a=http://www.patreon.com/xaljio}www.patreon.com/xaljio{/a}"
            a1 "И, конечно, сообщества на patreon и hentaiunited. Парни, вы шикарны."
            a1 "Спасибо вам за моральную и финансовую поддержку разработки этой игры. Вы, ребята, делаете этот мир чуточку лучше."
            jump faq2
        "Будет ли продолжение этой игры?":
            a1 "Как я уже говорил, я не стою на месте."
            a1 "И уже начал разработку нового проекта. {size=-4}(\"Тренер Принцессы Золотое Издание\"){/size}"
            a1 "..."
            a1 "..."
            a1 "Но если тебе понравилась конкретно эта часть, ты можешь найти группу программистов-энтузиастов занимающихся модифицированием..."
            a1 "А возможно и продолжением клиента."
            a6 "И хоть я и против этого..."
            a2 "Но от них не избавиться."
        "Можно взломать и перевести эту игру?":
            a1 "..."
            a1 "..."
            a5 "Нет."
            define nyor = Character('Nyarkohotep', color="#9F42AB")
            nyor "Странный вопрос, не находишь?"
            nyor "И это после того, как я полтора гребанных часа возился, чтобы перевести никому не нужные FAQ и обучалки!"
            nyor "Агрх!"
            nyor "А вообще, молодец, что заглянул."
            nyor "Минута славы."
            nyor "Перевод для вас пилили \
            {a=http://pornolab.net/forum/profile.php?mode=viewprofile&u=14141420}Ave_Fletch{/a}, \
            {a=http://pornolab.net/forum/profile.php?mode=viewprofile&u=15155170}Discordnk90{/a}, \
            {a=http://pornolab.net/forum/profile.php?mode=viewprofile&u=8041771}maniac4a{/a}, \
            {a=http://pornolab.net/forum/profile.php?mode=viewprofile&u=4472572}Rio-Violente{/a}, \
            {a=http://pornolab.net/forum/profile.php?mode=viewprofile&u=16957111}MrFrost1991{/a}, \
            {a=http://pornolab.net/forum/profile.php?mode=viewprofile&u=18304384}babaylolxz{/a}, \
            {a=http://pornolab.net/forum/profile.php?mode=viewprofile&u=15179745}Khan32{/a}, \
            {a=http://pornolab.net/forum/profile.php?mode=viewprofile&u=11908608}sn0rk95{/a}, \
            и любимец публики {a=http://pornolab.net/forum/profile.php?mode=viewprofile&u=16733487}Nyarkohotep{/a}."
            nyor "Извините, если кого-то забыли :3!"
            nyor "Не забывайте пользоваться салфетками, ребята, пока-пока!"
            a1 "..."
            a5 "А спросить моего разрешения на перевод, не нужно?"
            felix "Ты вроде как ушел..."
            a1 "..."
            a6 "Это ничего не меняет..."
            felix "Да конечно..."
            jump faq2

        "Неважно. Выпусти меня отсюда!":
            return

    
    return


########################
# From developers

label devel:

    $ end_u_1_pic =  "title3.jpg" #<---- SCREEN
    show screen end_u_1                                             #<---- SCREEN
    play music "music/GrapeSodaIsFuckingRawbyjrayteam6.mp3" fadein 1 fadeout 1
    
    dr "Итак, вы уже обратили внимание, что это не оригинальная игра Акабура..."
    menu :
        "Что ???" :
            dr "(facepalm)"
            dr "Я так и знал, что нужно давать больше информации общественности..."
        
        "Это же шутка ?" :
            dr "..........."  
        
        "А разве ты не Акабур ?" :
            dr "В рот мне ноги..."
            
    dr "{size=+3}Т.е. вы все по-прежнему считаете, что игру для вас продолжает улучшать Акабур ?{/size}"
    dr "И это после того, как он сообщил, что считает ее законченной ?"
    dr "После того, как он решил никогда ее не переводить на русский ?"
    dr "После того, как я написал всю эту гору кода, не говоря уж об остальной команде разработчиков, переводчиков и художников, месяцами бесплатно трудящихся для вас ?"
    dr "{size=+4}Аргх...{/size}"
    dr "......."
    dr "Простите, наболело."
    
    dr "Итак, для вас трудились :"
    dr "Главный координатор (встречайте стоя !): {color=4F4F4F}Хан ( Khan ){/color}"
    dr "Главный разработчик : {color=00FF00}Дрон (dron12355){/color}"
    dr "Разработка и ивенты Дафны : {color=424FA5}Феликс (The Felix){/color}"
    dr "Поддержка игры (на плаву) : {color=0000FF}Сказочник{/color}"
    dr "Перевод на английский язык : {color=0089BE}Хан и Sezt{/color}"
    dr "Разработка и обучающие ивенты : {color=FF0000}Nyarkohopter{/color}"
    dr "Чибики Дафны : {color=2F2F2F}Grending{/color}"
    dr "Дафна : {color=6F6F6F}Zio Dyne{/color}"    
    
    dr "Список особых благодарностей :"
    dr "{color=0F0F0F}Евгений aka Afar{/color} - за великолепный кодинг и неоценимый вклад в развитие проекта !"
    
    $ hx = 370
    $ hy = 0
    $ h_red_angry = True
    $ h_angry = False
    $ h_smile = False
    
    dr "И несравненная Гермиона Грейнджер в роли офисной шл..."
    show screen l_hermiona
    her "Что-о-о-о ???"
    hide screen l_hermiona

    dr "Прости, в роли секретут..."
    $ h_red_angry = False
    $ h_angry = True
    $ h_smile = False
    show screen l_hermiona
    her "А на тебя давно в последний раз подавали в суд\n за половую дискриминацию ?"
    hide screen l_hermiona
    dr "Бхм. И наша главная офис-леди - мисс Грейнджер."
    $ h_red_angry = False
    $ h_angry = False
    $ h_smile = True
    show screen l_hermiona    
    her "Так то лучше !"
    her "Всем до встречи в игре."
    hide screen l_hermiona 
    dr "Недотрога..."
    dr "Ушла наконец."
    
    dr "Итак, приятной игры, друзья !"
    
    dr "А если хотите пообщаться с людьми, которые продолжают совершенствование и расширение игры, милости просим."
    dr "{a=http://wtrus.ixbb.ru}НАШ ФОРУМ ТУТ{/a}"


return

label forum:

    $ end_u_1_pic =  "title3.jpg" #<---- SCREEN
    show screen end_u_1                                             #<---- SCREEN
    
    dr "Итак, перед вами модификация игры, которая развивается независимой (от Акабура) командой разработчиков. Добро пожаловать на {a=http://wtrus.ixbb.ru}НАШ ФОРУМ{/a}."

return
