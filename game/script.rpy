## Обозначение персонажей
define Rick = Character('Рик', color="#c19400")
define Morti = Character('Морти', color="#c19400")
define Kristi = Character('Кристина', color="#c19400")
define Kolya = Character('Коля', color="#c19400")
define Students = Character('Пара студентов', color="#c19400")
define Stas = Character('Стас', color="#c19400")

## Флаг
define relationshipWithKristina1 = False
define knowledgeAboutGameMechanics = False
define knowledgeAboutUlearn = False
define knowledgeAboutDesign = False
define relationshipWithKristina2 = False
define wrongAnswerKristinaPath = False
define gameTest = False
define relationshipWithKristina3 = False
define wrongAnswerKolyaPath = False
define knowledgeAboutSoundDesign = False

define audio.normal = "main-normal.ogg"

## Среда разработки Новелы
label start:

    play music normal

    scene 01
    with fade
    scene 02
    with dissolve
    scene 03
    with dissolve
    scene 04
    with dissolve
    scene 05
    with dissolve
    scene 06
    with dissolve
    scene 07
    with dissolve
    scene 08
    with dissolve
    scene 09
    with dissolve
    scene 010
    with dissolve
        
    scene 1
    with fade
    Morti "Черт возьми, Рик! Куда мы попали?!"

    scene 2
    with fade
    Rick "Тише Морти, инопланетная тварь сломала мою телепортационную пушку, мы щас можем быть где угодно!"

    scene 3
    with fade
    Morti "О Рик! Кажется, эта вселенная населена совершенно обычными людьми"
    Rick "Ладно. Может быть, эта планета немного цивилизованней чем я ожидал"
    Rick "В любом случае нам нужно как можно скорее найти инструменты для починки портальной пушки, и сваливать с этого места"

    scene 4
    with fade 
    "Рик убирает пистолет"

    scene 5
    with fade
    Morti "Смотри тут кажется недалеко есть какой-то технический институт. Может быть, мы там найдем то, что нам нужно?"

    scene 6
    with fade
    Rick "Молодец, Морти. Пойдем посмотрим на технологии этого измерения"

    ## Scene 2

    scene 12
    with fade
    Rick "Ну хоть иногда бываешь полезен. Смотри может в этом месте и вправду будет что-нибудь полезное"
    
    ## Scene 3

    scene 13
    with fade
    "Рик и Морти идут по холлу ИРИТа"

    scene 23 
    with fade
    "Навстречу им идет неизвестная девушка"

    scene 33
    with fade
    "Морти спотыкается и роняет учебники студентки"

    scene 43
    with fade 
    Morti "Ой, изви..."
    "Смотрит на Кристину и впадает в состояние шока с красоты девушки"

    scene 53
    with fade 
    "Cреди упавших книг Морти видит открытый студенческий с именем Кристина"
    Morti "Кри-сти-на…"
    "Студентка подбирает свои учебники и убегает"

    scene 63
    with fade
    Rick "Мдаа…"
    Rick "Жизнь тебя ничему не учит"

    scene 73
    with fade
    Morti "Даже не думай"
    Rick "Послушай Морти я не хочу тебя расстраивать, но то, что люди называют любовью — это просто химическая реакция заставляющая людей размножаться"
    Rick "По началу это сильное чувство, Морти, но потом оно медленно слабеет, оставляя тебя в неудачном браке, прямо как у твоих родите…"
    Morti "ЗАТКНИСЬ!!!"

    scene 83
    with fade
    Rick "Как скажешь"
    Rick "Только потом не смей говорить о том, что я тебя не предупреждал"
    Morti "Чудак..."

    ## scene 4

    scene covok
    with fade 
    show rc and mr see
    with dissolve
    ""

    scene 24
    with fade
    Morti "Вау.."

    scene 34
    with fade
    show mr 34:
        yalign 1.0 xalign 0.2
    with dissolve
    Morti "Ура! Всегда хотел стать разработчиком игр!"

    show rc 34:
        yalign 3.6 xalign 1.0
    with dissolve
    "Рик неодобрительно смотрит на Морти"

    hide mr 34
    hide rc 34
    
    show rc and mr 35:
        xalign 1.1 yalign 1.1
    with dissolve
    Rick "О боже, Морти мы на неизвестной планете, за нами гонятся глобглобнавты, ты серьезно думаешь у нас есть время на твои хотелки?"
    Rick "Просто выиграем то, что нам надо на этом жалком конкурсе и свалим отсюда к чертовой матери"

    hide rc and mr 35

    show rc and mr 36
    with dissolve
    Morti "Погоди Рик, а как видеокарта поможет нам починить телепортационную пушку?"

    hide rc and mr 36

    show rc and mr 37
    with dissolve
    Rick "Твою мать, Морти, сколько раз я тебе объяснял, что в сердце пушки находится биологически сложная матрица телепортационного поля"
    Rick "Oснованная на комбинации миниатюрных червоточин, квантовых туннелей и розовых роботов, бьющихся с марсианскими пингвинами!"
    Rick "А внешне телепортационная пушка представляет собой изящное и сложное сочетание металла и электроники"

    hide rc and mr 37

    scene black1
    with fade
    ""
    scene 34
    with fade

    show rc 38:
        yalign 3.6 xalign 0.8
    with dissolve

    show mr 38:
        yalign -4.0 xalign 0.1
    with dissolve

    Rick "Владение таким устройством - равносильно неограниченной власти над пространством и временем и это всего лишь доля моей гениальности, Морти"
    Rick "И МЫ ПОТЕРЯЛИ ЕЕ ЛИШЬ ПОТОМУ, ЧТО ТЫ НЕ МОЖЕШЬ ДЕРЖАТЬ СВОЙ ГРЕБАННЫЙ РОТ ЗАКРЫТЫМ ПЕРЕД КУЧКОЙ ВООРУЖЕНЫХ УРОДЛИВЫХ КРЕТИНОВ"
    
    hide mr 38

    show mr 39:
        yalign 1.2 xalign 0.1
    with dissolve
    "Морти почти плачет..."
    Rick "Ладно, не ной, ты нас в дерьмо и похлеще ввязывал"

    hide mr 39
    hide rc 38

    show mr 40:
        yalign 1.7 xalign 0.5
    with dissolve
    Rick "Пойдем уже"

    hide mr 40
    
    ## Scene 5

    scene 15
    with fade 
    "Герои слушают диктора о конкурсе гейм-дизайнеров"

    scene 25
    with fade
    "Уважаемые участники! Добро пожаловать в великолепный мир разработки игр"
    "Сегодня мы собрались на этом  конкурсе, чтобы познакомиться с креативными умами и талантливыми разработчиками"
    "Вас ждет настоящий спектакль из творчества и инноваций. Участники этого конкурса представят свои гейм-дизайнерские проекты, в которых каждая деталь продумана до мельчайших подробностей"
    "Вы познакомитесь с удивительными персонажами, захватывающими сюжетами и интригующими геймплейными механиками"

    scene 35
    with fade
    show mr 34:
        yalign 1.0 xalign 0.2
    with dissolve
    show kristi:
        yalign 0.05 xalign 0.7
    with dissolve
    "Морти устает от речей диктора и погружается в свои мысли"

    hide mr 34
    hide kristi

    scene 45
    with fade 
    "Cпустя 10 минут мыслей о Кристине"
    "Участники конкурса, мы ждем ваших потрясающих презентаций и невероятных идей"
    "Покажите нам, что вы настоящие создатели миров, и дайте нам возможность попасть в ваши волшебные вселенные"

    scene 55
    with fade
    show mr 5_5:
        yalign 1.3 xalign 0.5
    Morti "А где Рик?"

    hide mr 5_5

    scene 655
    with fade
    show kolya 65:
        xalign 0.6
    with dissolve

    show stas 65:
        xalign 0.9
    with dissolve
    "Морти видит двух студентов гейм-developer"
    Students "У меня есть идея для новой игры, что скажете?"
    Students "Давай, рассказывай свою идею"
    Students "Так вот, я думал о создании приключенческой игры в жанре фэнтези"
    Students "Мы можем создать удивительный мир с магией, эпическими сражениями и увлекательными головоломками…"

    hide stas 65
    hide kolya 65

    scene 655
    with fade
    show kolya 85:
        xalign 0.7
    with dissolve

    show stas 65:
        xalign 1.1
    with dissolve

    show mr 85:
        xalign 0.2 yalign 1.5
    with dissolve
    Morti "Привет ребят!"
    Morti "Можете рассказать о том, как выиграть в конкурсе"
    Kolya "Я вижу ты тут новенький, пекус что-ли?"
    Morti "Ммм… Да…"

    hide stas 65
    hide kolya 85
    hide mr 85

    scene 95
    with fade
    show mr 95:
        yalign 1.1 xalign -0.4
    with dissolve
    Kolya "Мы со Стасом собираемся в кафешку, здесь в радике. Пошли с нами, по дороге расскажу о конкурсе"

    hide mr 95

    ## Scene 6

    scene 16
    with fade
    "Ребята идут в ресторан"
    show kolya 16:
        xalign 0.15
    with dissolve
    show mr 16
    with dissolve
    Kolya "Ну так вот соревнование разбито на 5 этапов"
    show stas 16:
        xalign 0.9
    with dissolve
    Stas "Сюжет, дизайн, программная часть, звук и тестирование"
    Kolya "И на финальном этапе все конкурсанты представляют финальный билд игры"

    hide kolya 16
    hide mr 16
    hide stas 16

    scene 26
    with fade
    show mr 39:
        yalign 1.5 xalign 0.3
    with dissolve
    show stas 26:
        xalign 0.8
    Stas "Садись, мы щас быстро закажем"

    hide mr 39
    hide stas 26

    scene 336
    with fade
    "Морти сел за стол"

    scene 46
    with fade
    show kolya 46:
        xalign 0.3 yalign 1.1
    with dissolve
    show stas 46:
        xalign 0.7 yalign 1.9
    with dissolve
    ""

    hide kolya 46
    hide stas 46

    scene 56
    with fade
    show kr 56:
        xalign 0.8 yalign 1.1
    with dissolve
    "Морти видит плачущую Кристину..."
    show mr 56:
        xalign 0.2 yalign 1.7
    with dissolve
    Morti "Эй ты чего? Что случилось?"

    hide mr 56
    hide kr 56

    show mr 66:
        xalign 0.2 yalign 1.1
    with dissolve
    show kr 66:
        xalign 0.8 yalign 1.1
    Kristi "Я не могу решить практику на юлерне. Эти коллекции так достали меня..."
    Morti "Колл… Что?"

    hide mr 66
    hide kr 66

    show kr 76:
        xalign 0.8 yalign 1.1
    with dissolve
    show mr 39:
        yalign 1.5 xalign 0.2
    with dissolve
    Kristi "Ты не в теме?"
    Kristi "Все радисты которые учат сишарп учат его на юлерне."
    Kristi "Коллекция это одна из самых труднейших тем для понимания"

    hide mr 39
    hide kr 76

    "Коля подзывает Морти"

    show kolya 85:
        xalign 0.8
    with dissolve
    Kolya "Мы тут решили затусить вечером. Как раз будет возможность рассказать тебе еще о играх"
    show mr 86:
        xalign 0.2 yalign 1.1
    with dissolve
    menu:
        Kolya "Ты пойдешь?"

        "Помочь Кристине с Ulearn":
            $ relationshipWithKristina1 = True
            jump ulearn

        "Тусить с Колей":
            jump tusit
    return
    

label tusit:

    scene 56
    with fade
    show kolya 85:
        xalign 0.8
    with dissolve
    show mr 95:
        xalign -0.1 yalign 1.1
    with dissolve
    Morti "Да конечно! Пошли"
    
    hide mr 95
    hide kolya 85

    scene 162
    with fade
    show people 162:
        xalign 0.5 yalign -0.5
    with dissolve
    "Группа студентов" "Рассказывают разные истории"

    hide people 162

    scene 262
    with fade
    show mr 262:
        xalign 0.5 yalign -8.0
    with dissolve 
    "Морти решает пойти осмотреть квартиру"

    hide mr 262

    scene 362
    with fade
    show mr 362:
        xalign 0.8 yalign 1.1
    with dissolve
    "Морти заходит в комнату где Коля с Стасом решают практику “Коллекции” на Ulearn"

    hide mr 362

    scene 462
    with fade
    "Рядом лежит книга про игровые механики"

    scene 562
    with fade
    show mr 562:
        xalign 0.7 yalign 1.1
    with dissolve
    "Мысли Морти" "Кажется эта книга может помочь нам с Риком разработать игру"
    "Мысли Морти" "Но если пацаны объяснят мне эту практику, я смогу помочь Кристине..."

    menu:
        "Прочитать книгу про игровые механики":
            $ knowledgeAboutGameMechanics =True
            jump readBook
        
        "Попросить объяснить решение практики":
            $ knowledgeAboutUlearn = True
            jump help

        "Забить на все и расслабиться":
            jump chill

    


    return


label ulearn:

    scene 56
    with fade 
    show mr 161:
        xalign 0.2 yalign 1.1
    with dissolve
    Morti "Я наверное пас, мне там нужно еще своего деда найти..."
    show kolya 161:
        xalign 0.8 yalign 1.1
    with dissolve
    Kolya "Жаль конечно, но ладно, только добавь меня в ВК на случай если помощь нужна будет"

    hide mr 161
    hide kolya 161

    show mr 261:
        xalign 0.2 yalign 1.1
    with dissolve
    Morti "Куда?"
    show kolya 261:
        xalign 0.8
    with dissolve
    "Коля объясняет за местные социальные сети и они обмениваются контактами"

    hide kolya 261
    hide mr 261

    scene 361
    with fade
    show kolya 361:
        yalign 1.1 xalign 0.7
    with dissolve
    "Коля уходит"

    hide kolya 361

    scene 461
    with fade
    show kr 461:
        xalign 0.1 yalign 1.1
    with dissolve
    "Морти подходит к Кристине"
    show mr 461:
        yalign 1.5 xalign 0.9
    with dissolve 
    Morti "Не против вместе подумать над этой практикой?"
    Kristi "Давай"

    hide kr 461
    hide mr 461

    with fade
    show kr 561:
        xalign 0.1 yalign 1.1
    with dissolve
    show mr 561:
        yalign 1.5 xalign 0.9
    with dissolve 
    "Морти и Кристина вместе думают над задачами"

    scene 661
    with fade
    ""
    scene 461
    with fade
    show mr 761:
        xalign 1.0 yalign 1.1
    with dissolve
    Morti "Наконец-то, мы прошли все тесты"
    show kr 761:
        yalign -1.0 xalign 0.2
    with dissolve 
    Kristi "Осталось только дождаться код-ревью от препода"

    hide mr 761
    hide kr 761

    show mr 861:
        yalign 1.1 xalign 0.9
    with dissolve 
    Morti "Уже вечер. Ты не знаешь где можно здесь переночевать?"
    show kr 861:
        xalign 0.1 yalign 1.1
    with dissolve
    Kristi "Да, я живу в общежитии неподалеку, думаю сможем договориться пустить тебя"

    hide kr 861
    hide mr 861

    scene 961
    with fade
    show mr 961:
        yalign -100.0 xalign 0.5
    with dissolve 
    show kr 961:
        xalign 0.3 yalign 1.5
    with dissolve
    "Морти и Кристина идут к общежитию и видят Рика"

    hide kr 961
    hide mr 961

    scene 1061
    with fade
    show rc and mr 1061
    with dissolve
    Morti "Рик! Где тебя все это время носило?"
    Rick "Я добывал нам ордера, чтобы было где переночевать"
    Rick "Пошли в нашу комнату"

    jump sceneSeven

    return


## Прочитать книгу про игровые механики
label readBook:

    scene r 1
    with fade
    "Морти подбирает книгу и садиться читать ее"
    show mr r 1:
        xalign 0.7 yalign 1.1
    with dissolve
    "Морти несколько часов изучает книгу"

    "Проектирование игровых механик: Разработчик должен уметь составлять и балансировать различные механики, чтобы создать интересный и увлекательный игровой процесс"
    "Это включает в себя учет сложности, баланс между различными средствами, временем, затратами игрока и другими факторами"

    "Прототипирование: Знание игровых механик поможет разработчику создавать прототипы игровых систем, чтобы оценить их эффективность и работоспособность"
    "Это позволяет проверить идеи и модифицировать их до начала полноценной разработки"

    "Исправление ошибок и оптимизация: Разработчик, зная игровые механики, может легко идентифицировать и исправить возникающие проблемы в игре, такие как баги, неравновесие или неправильное функционирование систем"
    "Это помогает улучшить качество и играбельность игры"

    "Инновации: Знание игровых механик позволяет разработчикам экспериментировать, добавлять новые и оригинальные игровые элементы"
    "Это может привлечь новых игроков и сделать игру уникальной"

    hide mr r 1

    show mr r 2:
        xalign 0.7 yalign 1.1
    with dissolve
    Morti "Вау, полезная книга. Думаю с помощью Рика я смогу перенять пару механик из этой книги в нашу игру"

    hide mr r 2

    jump tusaEnd

    return


## Попросить объяснить решение практики
label help:
    
    scene h 1
    with fade
    "Морти подходит к парням"
    Morti "Парни можете помочь с предыдущей практикой?"
    Kolya "С коллекциями что-ли? Мы их сами наугад решили, но ладно давай попробуем"

    scene h 2
    with fade
    "Парни объясняют Морти решения задач"

    scene h 3
    with fade
    Morti "Кажется я понял, спасибо"
    Kolya "Ладно, парни уже поздно пора по домам"
    
    jump tusaEnd

    return


## Забить на все и расслабиться
label chill:

    scene c 1
    with fade 
    show mr c 1:
        xalign 0.2 yalign 1.1
    with dissolve
    show kolya c 1:
        xalign 0.9 yalign -1.0
    with dissolve
    "Морти и Коля разговаривают о чём-то"

    hide kolya c 1
    hide mr c 1

    show mr c 2:
        xalign 0.3 yalign 1.1
    with dissolve
    show kolya c 2:
        xalign 0.9 yalign 1.1
    with dissolve 
    Morti "Ха-ха-ха, интересное у вас измерение конечно"
    Kolya "Измерение? Ты о чем вообще?"

    hide kolya c 2
    hide mr c 2

    show mr c 3:
        xalign 0.3 yalign 1.1
    with dissolve
    show kolya c 3:
        xalign 0.9 yalign 1.1
    with dissolve 
    Morti "Да неважно, я просто устал. Где тут кстати туалет?"
    Kolya "В коридоре левая дверь"

    hide mr c 3
    hide kolya c 3

    scene c 4
    with fade
    show mr c 4:
        xalign 0.2 yalign 1.0
    with dissolve
    "Морти идет в туалет"
    show nn c 4:
        xalign 0.7 yalign 1.1
    with dissolve
    "У входа стоит подозрительный парень"
    "Тосщий парень" "Проходи"

    menu:
        "Пройти в туалет":
            jump tualet
            
        "Отказаться":
            jump otkaz

    return


label tusaEnd:

    scene 162
    with fade
    show people leave
    with dissolve
    "Тусовка заканчивается"

    hide people leave

    scene rhc 7
    with fade
    show mr r 7:
        xalign 0.8 yalign 1.1
    with dissolve
    show rc r 7:
        yalign 1.1 xalign 0.2
    with dissolve
    "Морти идет по профессорской, где встречает Рика"

    hide mr r 7
    hide rc r 7

    show rc and mr r 8
    with dissolve
    Morti "Где тебя черт возьми носило?"
    Rick "Тише Морти, я искал нам ночлег"

    hide rc and mr r 8

    scene rhc 9
    with fade
    show ssk:
        xalign 0.5 yalign 0.1
    with dissolve
    "Рик показывает два ордена с фотками Рика и Морти"

    hide ssk

    scene rhc 7
    with fade
    show rc and mr r 10:
        xalign 0.3 yalign 1.1
    with dissolve
    Morti "Боже Рик, где ты достал ордера? Неужели ты их подделал?!"
    Rick "Меньше вопросов, Морти. Пойдем осмотрим наш временный дом"

    hide rc and mr r 120

    scene 961
    with fade
    "Герои отправляются в общежитие"
    show rc and mr see
    with dissolve
    ""
    jump sceneSeven

    return


label tualet:

    scene ural
    with fade
    show mr t 6
    with dissolve
    "Морти решил довериться таинственному незнакомцу и на следующий день проснулся неизвестно где, без телефона и головной болью"

    hide mr t 6

    scene black
    with fade
    "Конец.."

    return


label otkaz:

    scene c 1
    with fade
    "Морти возвращается к Коле"
    show t 1:
        xalign 0.2 yalign 1.0
    with dissolve
    Morti "Что это за странный тип около туалета?"
    show kolya 85:
        xalign 0.8
    with dissolve
    Kolya "Не знаю, в любом случае, пора идти по домам"

    hide kolya 85

    show kolya c 1:
        xalign 1.1
    with dissolve
    Kolya "Ты где живешь, кстати?"

    hide t1

    show t 2:
        xalign 0.2 yalign 1.0
    with dissolve
    Morti "Да на самом деле нигде, не знаешь где здесь можно переночевать?"
    Kolya "Да конечно, я живу в одном из общежитий, думаю смогу тебе помочь"

    hide t 2
    hide kolya c 1

    scene rhc 7
    with fade
    show mr t 3:
        xalign 0.6 yalign 1.1
    with dissolve
    show kolya t 3:
        xalign 0.9 yalign 1.1
    with dissolve
    "Морти и Коля идут по профессорской где видят Рика"
    show rc t 3:
        xalign 0.1 yalign 1.1
    with dissolve
    ""

    hide kolya t 3
    hide rc t 3
    hide mr t 3

    show rc r 7:
        xalign 0.3 yalign 1.0
    with dissolve
    show kolya 161:
        xalign 0.9 yalign 1.1
    with dissolve
    show mr t 4:
        xalign 0.6 yalign 1.1
    with dissolve
    Morti "Знакомься Коль это мой дед Рик"
    Morti "Коля поможет нам с жильем"

    hide kolya 161

    show kolya t 5:
        xalign 0.95 yalign 1.1
    with dissolve
    Kolya "Здравствуйте, пойдемте с нами я найду вам в комнату в общежитии"

    hide kolya t 5
    hide mr t 4
    hide rc r 7

    scene 961
    with fade
    show t 6
    with dissolve
    ""

    jump sceneSeven

    return


## Scene 7
label sceneSeven:

    scene 17
    with fade
    show rc and mr see
    with dissolve
    "Герои осматривают комнату"

    hide rc and mr see

    show rc 34:
        xalign 0.7 yalign 2.7
    with dissolve
    Rick "Ну в целом неплохо"

    hide rc 34

    show rc and mr 35:
        xalign 1.1 yalign 1.1
    with dissolve
    Morti "Неплохо? Где тебя черт возьми носило?"

    hide rc and mr 35

    show rc and mr 1061
    with dissolve
    Rick "Я познакомился с писателем, вроде толковый мужик"
    Rick "Мы должны сегодня встретиться с ним в баре, где он мне пообещал помочь с сюжетом, взамен на кристаллы смерти"
    Rick "Ну а ты? Сделал хоть что-нибудь?"

    hide rc and mr 1061

    show mr 561:
        xalign 0.3 yalign 1.1
    with dissolve
    show rc 57:
        xalign 0.7 yalign 1.1
    with dissolve
    "Мысли Морти" "Черт! Нужно что-то ответить Рику, иначе опять будет гнать на меня что я бесполезный"

    hide rc 57
    hide mr 561

    if knowledgeAboutUlearn:

        scene 171
        with fade
        show nout:
            xalign 0.8 yalign 0.3
        with dissolve
        show mr 171:
            xalign 0.3 yalign 1.1
        with dissolve
        "Мысли Морти" "Точно, я видел у Кристины на ноутбуке приложения для дизайна!"

        hide mr 171
        hide nout

        scene 17
        with fade
        show mr c 2:
            xalign 0.3 yalign 1.1
        with dissolve
        Morti "Да, я думаю я решил проблему с дизайном для нашей игры"


    if knowledgeAboutGameMechanics:

        show mr 172:
            xalign 0.3 yalign 1.1
        with dissolve
        show rc 38:
            xalign 0.8 yalign 1.1
        with dissolve
        Morti "Да, я изучил книгу про игровые механики"
        Morti "Я ее немного почитал, думаю будет полезно для нас"
    
    if knowledgeAboutGameMechanics == False and knowledgeAboutUlearn == False:
        
        show mr 861:
            xalign 0.3 yalign 1.1
        with dissolve
        Morti "Мммм. Нууууу"

        hide mr 861

        show rc and mr 36
        with dissolve
        Rick "Я тебя понял"
        Rick "Впрочем как всегда"



    scene 17                                
    with fade
    show rc 273:
        xalign 0.5 yalign 1.1
    with dissolve
    "Рик смотрит на время" 

    Rick "Черт, я опаздываю"                
    Rick "Я пошел в бар"                    

    hide rc 273

    show rc 373:
        xalign 0.05 yalign 1.1
    with dissolve
    show mr 373:
        xalign 0.8 yalign 1.6
    with dissolve
    "Рик уходит"   

    hide mr 373
    hide rc 373

    show mr 5_5:
        xalign 0.5 yalign 1.1
    with dissolve

    Morti "Ладно, все равно делать нечего"
    Morti "Пойду прогуляюсь по общаге"    

    ## Scene 8
    scene 81
    with fade 
    show mr t 3:
        xalign 0.7 yalign 1.1
    with dissolve
    "Морти идет по коридору"     
    show kr 81:
        xalign 0.53 yalign 0.3
    with dissolve
    "В коридоре идет Кристина"        

    hide mr t 3
    hide kr 81

    show mr 82:
        xalign 0.85 yalign 2.5
    with dissolve
    show kr 82:
        xalign 0.2 yalign 1.1
    with dissolve
    Morti "Привет. Как дела?"     

    hide mr 82
    hide kr 82

    show kr 83:
        xalign 0.2 yalign 1.1
    with dissolve
    show mr 83:
        xalign 0.95 yalign 1.1
    with dissolve
    Kristi "Привет, Морти. Уже освоился в общаге?"
    Morti "Да, мы с моим дедом уже заселились"

    hide mr 83

    if knowledgeAboutUlearn:
        $ knowledgeAboutDesign = True;
        $ relationshipWithKristina2 = True;
        
        show mr 84:
            xalign 0.8 yalign 1.1
        with dissolve
        Morti "Кстати, ты уже решила ту практику на юлерне?"
        
        hide kr 83
        
        show kr 85:
            xalign 0.2 yalign 1.1
        with dissolve
        Kristi "Ну нет, а что?"

        hide mr 84
        
        show mr 82:
            xalign 0.8 yalign 2.5
        with dissolve
        Morti "Да мне тут пару идей насчет решения пришли. Думаю смогу помочь тебе ее решить"

        hide kr 85

        show kr 86:
            xalign 0.2 yalign 1.1
        with dissolve
        Kristi "Правда? Круто, пошли!"

        hide kr 86
        hide mr 82

        show kr 961:
            xalign 0.3 yalign 1.1
        with dissolve
        show mr 87:
            xalign 0.6 yalign 1.1
        with dissolve
        "Морти и Кристина идут в комнату"

        hide mr 87
        hide kr 961

        scene 88
        with fade
        ""

        scene 89
        with fade
        show kr 89:
            xalign 0.15 yalign 1.1
        with dissolve
        show mr 88:
            xalign 0.85 yalign 1.1
        with dissolve
        "Герои вместе думают над практикой"

        hide kr 89
        hide mr 88

        show kr 86:
            xalign 0.15 yalign 1.1
        with dissolve
        show mr 810:
            xalign 0.85 yalign 1.1
        with dissolve
        Kristi "Ураа! Все тесты пройдены!"
        Kristi "Спасибо большое"

        hide mr 810

        show mr 84:
            xalign 0.85 yalign 1.1
        with dissolve
        Morti "Да не за что"
        Morti "Кстати я у тебя тут вижу всякие графические редакторы. Ты случайно не дизайнер?"

        hide kr 86

        show kr 89:
            xalign 0.15 yalign 1.2
        with dissolve
        Kristi "Ну да, иногда увлекаюсь"

        hide mr 84

        show mr 82:
            xalign 0.85 yalign 2.5
        with dissolve
        Morti "Я тут со своим дедом участвую в конкурсе гейм-девелоперов. И нам нужен дизайн для нашей игры. Можешь подсказать нам как лучше оформить дизайн нашей игры?"
        Kristi "Да конечно"

        hide mr 82

        show mr 89:
            xalign 0.85 yalign 1.1
        with dissolve
        ""

        hide mr 89
        with dissolve
        hide kr 89
        with dissolve

        "Кристина рассказывает Морти про роль дизайна в разработке игр"
        show kr 812:
            xalign 0.5 yalign 1.1
        with dissolve
        Kristi "Ну вообще дизайн в играх играет очень важную роль"
        Kristi "Создания графики, пользовательского интерфейса, игровых механик и анимации, которые влияют на визуальную и функциональную стороны игры"

        hide kr 812

        show kr 813:
            xalign 0.5 yalign 1.1
        with dissolve
        Kristi "Также важно на начальном этапе разработать концепт игр. Где будут определяться основные идеи, стиль, жанр игры"
        Kristi "Дизайнеры обычно работают с Photoshop, Illustrator или создают сами модели в движке игры"
        Kristi "Они разрабатывают уровни, миры, персонажей и предметы, необходимые для визуализации игрового мира"

        hide 813 

        show kr 85:
            xalign 0.5 yalign 1.1
        with dissolve
        Kristi "В целом, дизайн в разработке игр нацелен на создание привлекательных визуальных эффектов, погружение в игровой мир и эмоциональное взаимодействие между игроком и игрой"
        
        hide kr 85

        show kr 83:
            xalign 0.5 yalign 1.1
        with dissolve
        Kristi "Он имеет существенное значение для успеха и популярности игры, поскольку в большой степени определяет первое впечатление и продолжительность игрового опыта"

        hide kr 83
        with dissolve

        scene 816
        with fade 
        ""

        scene 89
        with dissolve
        show mr 861:
            xalign 0.85 yalign 1.1
        with dissolve
        show kr 89:
            xalign 0.15 yalign 1.1
        with dissolve
        Morti "Уже поздно. Я наверное пойду в свою комнату"

        hide kr 89
        hide mr 861

        scene 81
        with fade
        show mr 87:
            xalign 0.55 yalign 1.1
        with dissolve
        "Морти уходит спать"
    
    
    if not knowledgeAboutUlearn:

        show mr 84:
            xalign 0.8 yalign 1.1
        with dissolve
        Kristi "Круто"
        Morti "Чем планируешь заниматься сегодня?"

        hide kr 83
        
        show kr 85:
            xalign 0.2 yalign 1.1
        with dissolve
        Kristi "Да ничем, наверное"
        Morti "Может сходим куда-нибудь?"

        hide kr 85

        show kr 86:
            xalign 0.2 yalign 1.1
        with dissolve
        Kristi "Уже поздно, может просто у меня чай попьем?"

        hide kr 86
        hide mr 82

        show kr 961:
            xalign 0.3 yalign 1.1
        with dissolve
        show mr 87:
            xalign 0.6 yalign 1.1
        with dissolve
        "Морти и Кристина пьют чай и болтают о жизни"

        hide kr 961
        with dissolve
        hide mr 87
        with dissolve

        scene 88
        with fade
        ""

        scene 816
        with dissolve
        ""

        scene 89
        with dissolve
        show mr 861:
            xalign 0.85 yalign 1.1
        with dissolve
        show kr 89:
            xalign 0.15 yalign 1.1
        with dissolve
        Morti "Уже поздно. Я наверное пойду в свою комнату"

        hide kr 89
        hide mr 861

        scene 81
        with fade
        show mr 87:
            xalign 0.55 yalign 1.1
        with dissolve
        "Морти уходит спать"
    
    ## Scene 9
    scene 91
    with fade
    "Утро"
    "Рик сидит за компьютером"

    scene 92
    with fade
    show rc 92:
        xalign 0.79 yalign 1.1
    with dissolve
    Rick "Эй, Морти, просыпайся! У меня отличная идея! Ну, скорее!"
    
    hide rc 92

    scene 93
    with fade 
    Morti "Что-что? Рик, что происходит? Сколько время?"
    Rick "Я встретился с тем самым писателем. И многое понял"

    scene 94
    with fade
    show rc 94:
        xalign 0.15 yalign -0.1
    with dissolve
    show mr 94:
        xalign 0.95 yalign 1.1
    with dissolve
    Morti "Э-э, хорошо, Рик. Только может забьем на сюжет?"
    Morti "Может просто сделаем какую-то стрелялку и улетим отсюда?"

    Rick "Смотри, Морти, видеоигры - это не просто развлечение. Они - это сюжеты, миры, истории, в которые ты можешь погрузиться"
    Rick "Это нечто большее, чем просто нажимание кнопок и движение персонажем"

    hide mr 94

    show mr 965:
        xalign 0.95 yalign 1.1 
    with dissolve
    Morti "А-а, понятно. Но почему сюжет так важен? Нельзя просто поиграть и расслабиться?"

    hide rc 94

    show rc 963:
        xalign 0.15 yalign -0.1
    with dissolve
    Rick "Конечно, можно всё время бегать по вселенной, прыгать, убивать монстров и избегать ловушек"
    Rick "Но вся эта беготня не имеет смысла, если нет хорошо продуманного сюжета, Морти. Сюжет формирует наше понимание, наши чувства, нашу жажду приключений"

    hide mr 965

    show mr 964:
        xalign 0.95 yalign 1.1
    with dissolve
    Morti "То есть, сюжет должен быть интересным и захватывающим?"

    hide rc 963

    show rc 962:
        xalign 0.15 yalign -0.1
    with dissolve
    Rick "Именно! Сюжет в видеоиграх делает нас частичкой этого фантастического мира"
    Rick "Он погружает нас в удивительные приключения, дает нам возможность испытать эмоции, сопереживать персонажам и осознавать наши действия"

    hide mr 964

    show mr 965:
        xalign 0.95 yalign 1.1
    with dissolve
    Morti "Но я просто играю и наслаждаюсь геймплеем, Рик. Зачем мне заморачиваться сюжетом?"

    hide rc 962

    show rc 965:
        xalign 0.15 yalign -0.1
    with dissolve
    Rick "Смысл игр вовсе не сводится к развлечению; они предлагают глубокие повествования, которые извлекают игрока из его реальности и погружают его в другой мир"
    Rick "Именно писатель сюжета лепит этот мир кирпичик за кирпичиком, создавая фантастическое путешествие, где игроки могут познакомиться с проблемами, идеалами и новыми местами"

    hide mr 965

    show mr 962:
        xalign 0.95 yalign 1.1
    with dissolve
    Morti "Я начинаю понимать, Рик"
    Morti "Сюжет - это то, что превращает простую игру во что-то большее"

    hide rc 965

    show rc 966:
        xalign 0.15 yalign 1.1
    with dissolve
    Rick "Именно, кстати пока ты дрых, я уже закончил работу с сюжетом для нашей игры"

    hide mr 962

    show mr 966:
        xalign 0.95 yalign 1.1
    with dissolve
    Morti "Круто"
    Rick "Кстати собирайся, мне нужно тебя познакомить с одним человеком"

    hide mr 966

    show mr 962:
        xalign 0.95 yalign 1.1
    with dissolve
    Morti "Ну я только проснулся..."

    hide mr 962
    hide rc 966


    ## Scene 10
    scene 10
    with fade
    "Рик и Морти идут по улице"
    show mr 101:
        xalign 0.15 yalign 1.1
    with dissolve
    Morti "Кажется мне начинает нравиться работать над нашей видеоигрой"
    show rc 101:
        xalign 0.9 yalign -3.0
    with dissolve
    Rick "Да? Ну может удастся тебя пристроить в какую-нибудь компанию?"

    hide mr 101

    show mr 102:
        xalign 0.15 yalign 1.1
    with dissolve
    Morti "Да ладно, я думаю сам смогу их делать"

    hide rc 101

    show rc 102:
        xalign 0.9 yalign 1.1
    with dissolve  
    Rick "Это вряд-ли Морти..."
    Rick "В геймдеве есть еще кое-что важное помимо самого процесса разработки игры"

    hide mr 102

    show mr 103:
        xalign 0.15 yalign 1.1
    with dissolve
    Morti "И что же?"

    hide rc 102

    show rc 103:
        xalign 0.9 yalign 1.1
    with dissolve
    Rick "Я говорю о командной работе"

    hide mr 103

    show mr 104:
        xalign 0.15 yalign 1.1
    with dissolve
    Morti "Командная работа?"
    Morti "Что ты имеешь в виду, Рик?"

    hide rc 103

    show rc 104:
        xalign 0.9 yalign 1.1
    with dissolve
    Rick "Все гениальное создается совместными усилиями, Морти."
    Rick "Когда люди собираются вместе и объединяют свои таланты, результаты бывают удивительными"

    hide rc 104

    show rc 105:
        xalign 0.9 yalign 1.1
    with dissolve
    Rick "Все видеоигры, когда-либо созданные, являются плодом коллективной работы"
    Rick "От программистов и дизайнеров до художников и сценаристов - каждый внес свой вклад, и именно это сделало их такими прекрасными"
    Morti "Да? Но например ты же сам делаешь все свои невероятные изобретения"

    hide rc 105

    show rc 106:
        xalign 0.9 yalign 1.1
    with dissolve
    Rick "Да, Морти, ты можешь быть одарённым и способен делать многое самостоятельно" 
    Rick "Но представь что если бы в нашей команде было два человека с умом как у меня"

    hide rc 106

    show rc 107:
        xalign 0.9 yalign 1.1
    with dissolve
    Rick "Часто лучшие идеи появляются именно в результате взаимодействия с другими людьми" 
    Rick "Командная работа позволяет объединять разные точки зрения и опыт, что в конечном итоге приводит к неповторимым и инновационным результатам"

    hide mr 104

    show mr 106:
        xalign 0.15 yalign 1.2
    with dissolve
    Morti "Непривычно это говорить, но спасибо за наставления, Рик"

    hide rc 107

    show rc 108:
        xalign 0.9 yalign 1.1
    with dissolve
    Rick "Да не за что. Мы кстати почти подошли"

    hide mr 106

    show mr 108:
        xalign 0.1 yalign 1.1
    with dissolve
    ""


    ## Scene 11
    if relationshipWithKristina2 or relationshipWithKristina1:

        scene 111
        with fade
        "За столом сидит Кристина"

        scene 112
        with fade
        show rc and mr 112
        with dissolve
        Rick " Морти, знакомься это еще один член нашей команды"
        Rick "Я позвал Кристину, чтобы она нам помогла с графическим и аудио дизайном"

        Morti "..."
        Morti "Ты еще и музыкой увлекаешься?"

        hide rc and mr 112

        scene 113
        with fade
        show mr 113:
            xalign 0.05 yalign 1.3
        with dissolve
        show rc 113:
            xalign 0.9 yalign -0.5
        with dissolve
        Kristi "Да, я узнала что вы участвуете в конкурсе и решила помочь вам с вашей игрой"

        hide rc 113
        hide mr 113

        scene 114
        with fade
        show mr 114:
            xalign 0.1 yalign 1.1
        with dissolve
        Morti "Круто. Только времени уже остается мало, нам точно сейчас стоит тратить время на звук?"
        show kr 114:
            xalign 0.9 yalign 1.1
        with dissolve
        Kristi "Ну, видеоигра - это не только графика, Морти"
        Kristi "Каждый звук в игре должен быть тщательно продуман и создан таким образом, чтобы подчеркнуть сюжетные моменты, акцентировать важные события и передать эмоции"
        Kristi "Звуки окружения, звучание оружия, голоса персонажей - все это должно быть согласовано и привлекательно для игрока"

        hide mr 114

        show mr 115:
            xalign 0.1 yalign 1.1
        with dissolve
        Morti "Вот это да, я даже не задумывался об этом"
        Morti "Но зачем всё это нужно?"

        hide kr 114

        show kr 115:
            xalign 0.9 yalign 1.1
        with dissolve
        Kristi "Ну, представь, Морти, что ты играешь в какую-то увлекательную историю"
        Kristi "Звуки и музыка могут создать сильную эмоциональную связь между игроком и игрой"
        Kristi "Они могут поставить тебя на ноги, вызвать ощущение реальности и захватить тебя настолько, что ты будешь жить в игровом мире"
        Kristi "Звуки и музыка - это как дополнительный уровень восприятия и атмосферы в игре"

        hide mr 115

        show mr 116:
            xalign 0.1 yalign 1.1
        with dissolve
        Morti "Верно, в таком случае аудиодизайнеры действительно играют огромную роль!"
        Morti "Я теперь понимаю, что без них мир видеоигр был бы гораздо менее захватывающим и реалистичным"
        
        hide mr 116
        hide kr 115

        show mr 117:
            xalign 0.1 yalign 1.1
        with dissolve
        show kr 117:
            xalign 0.9 yalign 1.1
        with dissolve
        "Герои занимаются аудиодизайном"

        hide mr 117
        hide kr 117

        show rc 118:
            xalign 0.95 yalign 1.1
        with dissolve
        show mr 118:
            xalign 0.1 yalign 1.0   
        with dissolve
        show kr 118:
            xalign 0.4 yalign 1.1
        with dissolve
        Rick "Ну что-ж детишки раз уже обо всем позаботились можно и отдохнуть"
        Morti "Да было-бы круто"

        hide kr 118

        show kr 119:
            xalign 0.4 yalign 1.1
        with dissolve
        Kristi "Думаю я знаю кафе куда можно сходить"

        hide rc 118

        show rc 119:
            xalign 0.95 yalign 1.1
        with dissolve
        Rick "Пойдем скорее я есть хочу"

        hide rc 119
        hide mr 118
        hide kr 119

        scene 1101
        with fade
        show rc and mr 1101
        show kr 1101:
            xalign 0.5 yalign 1.1
        with dissolve
        "Герои отправляются в кафе"

        hide kr 1101
        hide rc and mr 1101

        scene 1102
        with fade
        show kr 1102:
            xalign 0.3 yalign 0.6
        with dissolve
        "Герои празднуют окончание разработки игры"

        hide kr 1102
        
        scene 1103
        with fade
        ""

        scene 1104
        with fade
        show mr 1104:
            xalign 0.3 yalign 1.1
        with dissolve
        ""

        scene 1110
        with fade

        menu:
            "Спросить Рика, о чем он задумался":
                jump rick

            "Пойти поискать Кристину":
                $ relationshipWithKristina3 = True
                jump searchKristi

    if not relationshipWithKristina2:

        scene e1
        with fade
        "За столом сидит Коля"
        
        scene e3
        with fade
        show rc e2:
            xalign 0.95 yalign -0.6
        with dissolve
        Rick "Морти, знакомься это еще один член нашей команды"
        show kolya e2:
            xalign 0.5 yalign 1.1
        with dissolve
        Rick " Я позвал Колю, чтобы он нам помог нам с программной частью игры"
        show mr e2:
            xalign 0.07 yalign 1.1
        with dissolve
        Morti "Привет, Коль"
        Morti "Мы если что уже знакомы"

        hide rc e2 

        show rc e3:
            xalign 0.95 yalign 1.1
        with dissolve
        Rick "Хорошо, тогда не будем отвлекаться"
        Rick "Итак, я уже написал готовый сюжет"

        hide rc e3

        show rc e4:
            xalign 0.95 yalign 1.1
        with dissolve 

        if knowledgeAboutGameMechanics:

            Rick "Морти, позаботился о игровых механиках"

        Rick "Кажется нам осталось сделать дизайн и протестировать"

        Rick "Значит я и Морти занимаемся дизайном, а Коля параллельно будет превращать это в рабочий код"

        hide kolya e2 

        show kolya e5:
            xalign 0.5 yalign 1.1
        with dissolve
        Kolya "А как же звук?"

        hide rc e4

        show rc e6:
            xalign 0.95 yalign 1.1
        with dissolve 
        Rick "Звук? Чего это тебя так взбудоражило?"
        Rick "Думаю, можно просто добавить несколько звуковых эффектов и забить"

        hide kolya e5

        show kolya e6:
            xalign 0.5 yalign 1.1
        with dissolve
        Kolya "О нет, Рик, это далеко не так"
        Kolya "Звук играет огромнейшую роль в создании атмосферы и эмоций в играх"
        Kolya "Он помогает погрузить игрока в виртуальный мир и создает уникальный опыт"
        
        hide mr e2

        show mr e8:
            xalign -0.1 yalign 1.1
        with dissolve
        Morti "Погоди, Коль, я все еще не думаю, что этот звук так важен"

        hide kolya e6

        show kolya e10:
            xalign 0.4 yalign 1.1
        with dissolve
        Kolya "Это то, что называется аудиодизайном, Морти"
        Kolya "Звуки в игре могут передавать информацию о окружении, событиях, позволяют узнать о наличии врагов или ценных предметов"
        Kolya "Без звуков игровой мир будет плоским и невыразительным"

        hide rc e6

        show rc e9:
            xalign 0.95 yalign 1.1
        with dissolve 
        Rick "Ну так добавь пару взрывов и пускай все будет в порядке"

        hide kolya e10

        show kolya e11:
            xalign 0.4 yalign 1.1
        with dissolve
        Kolya "Нет, Рик"
        Kolya "Звук важен не только для отдельных моментов"
        Kolya "Например, звуки шагов персонажа могут дать игроку ощущение присутствия в игровом мире, а музыкальное сопровождение может создавать настроение и повышать эмоциональную интенсивность"

        hide rc e9

        show rc e11:
            xalign 0.95 yalign 1.1
        with dissolve 
        Rick "Ладно, ладно, наверное, не так все просто, как я думал"

        hide kolya e11

        show kolya t 4:
            xalign 0.4 yalign 1.1
        with dissolve
        Kolya "Именно, Рик"
        Kolya "Звук – это еще один инструмент геймдева, который мы можем использовать для создания уникального и неповторимого игрового опыта"
        Kolya "Так что, Морти если собираешься и дальше работать в сфере разработки игр не забывай об этом"

        hide rc e11

        show rc e9:
            xalign 0.95 yalign 1.1
        with dissolve 
        Rick "Ладно, значит после дизайна занимаемся звуком"

        hide mr e8

        show mr e11:
            xalign 0.15 yalign 1.1
        with dissolve
        Morti "Это вас этим знаниям в этом радиофаке учат?"

        Kolya "Что, заинтересовало?"

        hide mr e11

        show mr e2:
            xalign 0.15 yalign 1.1
        with dissolve
        Morti "Да, похоже круто у вас учиться"

        hide rc e9

        show rc e11:
            xalign 0.95 yalign 1.1
        with dissolve
        Rick "Хватит трепаться, у нас работы еще полный вагон"
        Rick "Доставайте свои девайсы, будем делать дизайн для игры"

        scene black k
        with fade
        ""

        scene 112
        with fade
        show rc e15:
            xalign 1.0 yalign 1.1
        with dissolve
        show kolya e15:
            xalign 0.6 yalign -0.1
        with dissolve
        show mr e15:
            xalign -0.1 yalign 1.1
        with dissolve
        "Герои занимаются разработкой дизайна"

        hide mr e15

        show mr e16:
            xalign 0.03 yalign 1.1
        with dissolve
        Morti "О боже, я не могу поверить"
        Morti "Мы закончили с этим гребанным дизайном"

        hide rc e15

        show rc e16:
            xalign 1.0 yalign 1.1
        with dissolve
        Rick "Черт, как же я устал..."

        hide kolya e15

        show kolya e16:
            xalign 0.4 yalign 1.1
        with dissolve
        Kolya "Не падайте духом, друзья"
        Kolya "Перед нами еще стоит задача протестировать наш готовый продукт"

        hide mr e16

        show mr e17:
            xalign 0.03 yalign 1.1
        with dissolve
        Morti "О нееееееет..."

        scene black k1 
        with fade
        ""

        scene e3
        with fade 
        show kolya e6:
            xalign 1.0 yalign 1.1
        with dissolve
        Kolya "Нет, что-то не сходится"
        show mr e8:
            xalign 0.1 yalign 1.1
        with dissolve
        Morti "Что-то не так?"
        Kolya "Я не могу понять. Нашей игре чего-то нехватает"

        hide mr e8
        hide kolya e6

        show rc e19:
            xalign 0.95 yalign 1.1
        with dissolve
        show kolya e11:
            xalign 0.05 yalign 1.1
        with dissolve
        Rick "Меня тоже не покидает это чувство"

        scene e20
        with fade
        show mr e11:
            xalign 0.3 yalign 1.1
        with dissolve
        ""

        scene 655
        with fade

        menu:
            Morti "Но что же?"
            
            "Дизайн":
                $ wrongAnswerKolyaPath = True
                jump design2

            "Звук":
                $ knowledgeAboutSoundDesign = True
                jump sound2

            "Код игры":
                $ wrongAnswerKolyaPath = True
                jump code
        
    return



label design2:

    scene 655
    with fade
    show mr d1:
        xalign 0.1 yalign 1.1 
    with dissolve
    Morti "Может стоит еще поработать над дизайном?"
    show rc d1:
        xalign 0.95 yalign 1.1
    with dissolve
    Rick "О боже..."

    hide mr d1

    show kolya d2:
        xalign 0.1 yalign 1.1
    with dissolve
    Kolya "Нет, наши модели получились довольно качественными да и времени на это нет"
    Kolya "Ладно кажется мы просто перетрудились"

    hide rc d1

    show rc d2:
        xalign 0.95 yalign 1.1
    with dissolve
    Rick "Да"
    Rick "Время уже поздно, пора отправлять игру на оценивание и отдыхать"

    jump test 

    return 

label sound2:

    scene 655
    with fade
    show mr d1:
        xalign 0.1 yalign 1.1 
    with dissolve
    Morti "Может стоит поработать над аудиодизайном?"
    show rc d1:
        xalign 0.95 yalign 1.1
    with dissolve
    Rick "Твою мать, мы столько об этом говорили, но совсем забыли про него!"

    hide mr d1

    show kolya d2:
        xalign 0.1 yalign 1.1
    with dissolve
    Kolya "Спокойно, время еще есть"
    Kolya "Предлагаю поискать в открытых источниках готовую музыку для саундтрека нашей игры"

    hide rc d1

    show rc d2:
        xalign 0.95 yalign 1.1
    with dissolve
    Rick "Давайте уже покончим с этим"
    
    scene e1
    with fade
    show mr d4:
        xalign 0.1 yalign 1.1
    with dissolve
    show rc d4:
        xalign 1.0 yalign 1.1
    with dissolve
    "Герои копают весь интернет в поисках подходящих музыкальных композиций"

    scene 655
    with fade 
    show kolya d5:
        xalign 0.1 yalign 1.1
    with dissolve
    Kolya "Похоже это все"
    show mr r 2:
        xalign 0.9 yalign 1.1
    with dissolve
    Morti "Наконец-то"

    hide mr r 2

    show rc d5:
        xalign 0.9 yalign 1.1
    with dissolve
    Rick " Отправляем наш проект на оценивание и я пойду нажрусь"

    jump test

    return

label code:

    scene 655
    with fade
    show mr d1:
        xalign 0.1 yalign 1.1 
    with dissolve
    Morti "Может стоит поиграться с оптимизацией игры?"
    show rc d1:
        xalign 0.95 yalign 1.1
    with dissolve
    Rick "О боже..."

    hide mr d1

    show kolya d2:
        xalign 0.1 yalign 1.1
    with dissolve
    Kolya "Нет, наша игра и на калькуляторе запуститься"
    Kolya "Кажется мы просто немного перетрудились"

    hide rc d1

    show rc d2:
        xalign 0.95 yalign 1.1
    with dissolve
    Rick "Да"
    Rick "Время уже поздно, пора отправлять игру на оценивание и отдыхать"

    jump test

    return


label rick:

    scene 1110
    with fade 
    show mr 1110:
        xalign 0.95 yalign 1.1
    with dissolve
    Morti "Рик, все в порядке?"
    show rc 1110:
        xalign 0.15 yalign -0.1
    with dissolve
    Rick "Меня не покидает мысль, что мы о чем-то забыли"
    Rick "Ты как думаешь?"

    hide mr 1110

    show mr 1111:
        xalign 0.95 yalign 1.1
    with dissolve
    Morti "Ты про игру что-ли?"

    hide rc 1110

    show rc 1111:
        xalign 0.15 yalign -0.1
    with dissolve
    Rick "Да, мы кажется мы упускаем что-то очень важное"

    hide rc 1111
    hide mr 1111

    scene 1112
    with fade 
    show mr 1112:
        xalign 0.3 yalign 1.3
    with dissolve
    ""

    scene 1110
    with fade 

    menu:
        Morti "О чем же мы могли забыть?"

        "Дизайн":
            $ wrongAnswerKristinaPath = True
            jump incorrectСhoice

        "Сюжет":
            $ wrongAnswerKristinaPath = True
            jump incorrectСhoice

        "Звук":
            $ wrongAnswerKristinaPath = True
            jump incorrectСhoice

        "Тестирование":
            $ gameTest = True
            jump testing

    return


label searchKristi:

    scene 1110
    with fade
    show mr big 6:
        xalign 0.9 yalign 1.3
    with dissolve
    Morti "Что-то Кристины не видно"
    Morti "Пойду поищу её"
    show rc 1110:
        xalign 0.15 yalign -0.1
    with dissolve
    Rick "Иди иди"

    hide mr big 6

    show mr 962:
        xalign 0.9 yalign 1.1
    with dissolve
    ""

    scene big
    with fade
    show kr big 1:
        xalign 0.8 yalign 2.0
    with dissolve
    "Кристина выглядит взволнованной"
    show mr 39:
        xalign 0.15 yalign 1.3
    with dissolve
    Morti "Эй, все в порядке?"

    hide kr big 1

    show kr big 2:
        xalign 0.8 yalign 2.0
    with dissolve
    Kristi "Нет, Морти, я в ужасе! Участие в этом конкурсе видеоигр — это для меня огромный шаг"
    Kristi "Я даже не знаю, что мне делать, если что-то пойдет не так..."

    hide mr 39

    show mr big 2:
        xalign 0.15 yalign 1.1
    with dissolve
    Morti "Я понимаю, Кристина"
    Morti "Может быть тяжело, особенно когда нам приходится соревноваться с другими"
    Morti "Но знаешь что? Мы есть у друг друга, и я верю в нас"

    hide kr big 2

    show kr big 3:
        xalign 0.8 yalign 1.1
    with dissolve
    Kristi "Правда?"
    Kristi "Ты так уверен, Морти?"

    hide mr big 2 

    show mr big 3:
        xalign 0.15 yalign 1.1
    with dissolve
    Morti "Именно так, Кристина! Мы здесь для того, чтобы получить удовольствие и насладиться временем, проведенным вместе"
    Morti "Если мы выиграем, это будет здорово, но даже если нет, наше дружба останется неизменной"

    hide kr big 3

    show kr big 4:
        xalign 0.8 yalign 1.1
    with dissolve
    "Кристина улыбается"
    Kristi "Морти..."
    Kristi "Спасибо, что успокоил меня"

    scene black big
    with fade
    ""

    scene 1110
    with fade
    show mr 1115:
        xalign 0.95 yalign 1.1
    with dissolve  
    Morti "Кажется пора отправлять игру на оценивание"
    show kr 813:
        xalign 0.15 yalign 1.1
    with dissolve
    Kristi "Да, пора уже"
    
    scene black
    with fade
    "Герои отправляют игру на оценивание"

    scene 1101
    with fade
    show rc 1115:
        xalign 0.5 yalign 1.3
    with dissolve
    Rick "На сегодня все"

    scene 1110
    with fade 
    show mr 1116:
        xalign 0.8 yalign 1.1
    with dissolve
    Morti "Когда будут результаты конкурса?"
    show kr 813:
        xalign 0.2 yalign 1.1
    with dissolve
    Kristi "Уже завтра"

    hide kr 813

    show kr 1116:
        xalign 0.2 yalign 1.1
    with dissolve
    Kristi "Кстати мне уже пора идти"
    Kristi "Пока"

    scene 1101
    with fade
    show rc 1115:
        xalign 0.5 yalign 1.3
    with dissolve
    Rick "Я тоже сваливаю, Морти, не ищи меня до завтра"
    Rick "Мне нужно отдохнуть от этих игр"

    jump scene12

    return


label incorrectСhoice:

    scene 1110
    with fade
    show rc 1110:
        xalign 0.15 yalign -0.1
    with dissolve
    show mr 1113:
        xalign 0.9 yalign 1.3
    with dissolve
    Rick "Ну нет Морти, это у нас уже готово"
    Rick "Ладно, проехали"

    jump continuee

    return


label testing:

    scene 1110
    with fade 
    show mr 1113:
        xalign 0.9 yalign 1.3
    with dissolve
    show rc 1113:
        xalign 0.15 yalign -0.1
    with dissolve
    Rick "Черт возьми, Морти!"
    Rick "Точно! Мы же даже не провели тесты нашей игры!"
    Rick "Тащи сюда Кристину и ноутбуки"
    Rick "Будем тестировать"

    scene 1102
    with fade
    show kr 1102:
        xalign 0.3 yalign 0.6
    with dissolve
    "Герои проводят время за тестированием игры"

    jump continuee



    return


label continuee:

    scene 1103
    with fade
    ""

    scene 1110
    with fade
    show mr 1115:
        xalign 0.95 yalign 1.1
    with dissolve  
    Morti "Кажется пора отправлять игру на оценивание"
    show kr 813:
        xalign 0.15 yalign 1.1
    with dissolve
    Kristi "Да, пора уже"
    
    scene black
    with fade
    "Герои отправляют игру на оценивание"

    scene 1101
    with fade
    show rc 1115:
        xalign 0.5 yalign 1.3
    with dissolve
    Rick "На сегодня все"

    scene 1110
    with fade 
    show mr 1116:
        xalign 0.8 yalign 1.1
    with dissolve
    Morti "Когда будут результаты конкурса?"
    show kr 813:
        xalign 0.2 yalign 1.1
    with dissolve
    Kristi "Уже завтра"

    hide kr 813

    show kr 1116:
        xalign 0.2 yalign 1.1
    with dissolve
    Kristi "Кстати мне уже пора идти"
    Kristi "Пока"

    jump scene12


    return


label test:

    scene 1010
    with fade
    "Рик отправляет готовую игру на оценивание"

    scene 655
    with fade 
    show rc e2:
        xalign 0.95 yalign 1.1
    with dissolve
    Rick "Готово"
    Rick "Я сваливаю, Морти, не звони мне до завтра"
    Rick "Мне нужно отойти от этих игр"

    show mr e8:
        xalign 0.1 yalign 1.1
    with dissolve
    Morti "Фиг с тобой, я просто пойду в общагу спать"

    jump scene12

    return 


label scene12:
    
    scene end 1
    with fade
    "Морти просыпается"

    scene end 2
    with fade
    ""

    scene end 3
    with fade
    show mr end 3:
        xalign 0.5 yalign -0.3
    with dissolve
    Morti "О черт! До оглашения результатов всего полчаса!"
    Morti "Мне нужно бежать"

    scene black big 
    with fade
    ""

    if relationshipWithKristina2:

        scene end 4
        with fade
        show rc end 4:
            xalign 0.02 yalign 1.1
        with dissolve
        show kr end 4:
            xalign 0.35 yalign -1.0
        with dissolve
        Rick "Где тебя носило?"
        show mr end 5:
            xalign 0.8 yalign 1.1
        with dissolve
        Morti "Ну что еще не огласили результаты?"

        hide kr end 4

        show kr end 6:
            xalign 0.35 yalign 1.1
        with dissolve
        Kristi "Еще нет, вот вот начнут оглашать"

        hide mr end 5 

        show mr end 6:
            xalign 0.8 yalign 1.1
        with dissolve
        ""

        jump End

    if not relationshipWithKristina2:

        scene end 4
        with fade
        show rc end 4:
            xalign 0.02 yalign 1.1
        with dissolve
        show kolya end 4:
            xalign 0.35 yalign 1.1
        with dissolve
        Rick "Где тебя носило?"
        show mr end 5:
            xalign 0.8 yalign 1.1
        with dissolve
        Morti "Ну что еще не огласили результаты?"

        hide kolya end 4

        show kolya end 6:
            xalign 0.35 yalign 1.1
        with dissolve
        Kolya "Ждем, еще пару минут"

        hide mr end 5 

        show mr end 6:
            xalign 0.8 yalign 1.1
        with dissolve
        ""

        jump End

    return

label End:

    scene end
    with fade
    show dc 1:
        xalign 0.5 yalign -0.4
    with dissolve
    "За последние дни каждая команда превратила свои фантазии в цифровую реальность, в игры, которые захватывали нас, заставляли волноваться, радоваться и бросаться вызовам"
    "Мы были удивлены непредсказуемыми историями, талантливой графикой, прекрасным звуковым сопровождением и инновационными механиками"
    "Мы тщательно изучили каждую игру и приняли нелегкое решение выбрать команду победителей"

    hide dc 1

    show dc 2:
        xalign 0.5 yalign 1.3
    with dissolve
    "Итак, мои дамы и господа, нашему победителю предстоит забрать факел и зажечь огонь победы!"
    "Да, это время, которое вы все ожидали - момент, когда один разработчик станет главным героем!"
    "Не будем тянуть момент итогов"
    "Именно сейчас я объявляю, что победителем конкурса разработчиков игр становится"
    "..."

    if relationshipWithKristina3:

        scene end 
        with fade
        show dc 3:
            xalign 0.5 yalign 1.1
        with dissolve
        "Поздравляю вас, Шцмейстз интертейнмент, вы - достойнейший победитель этого блестящего конкурса"
        "Ваша игра не только завоевала сердца жюри, но и восхитила всех нас своей уникальностью и креативностью"
        "Вы создали нечто особенное, что добавит яркость в мир игр!"

        scene end 4
        with fade
        show rc end1:
            xalign 0.02 yalign 1.1
        with dissolve
        show kr end1:
            xalign 0.35 yalign 1.1
        with dissolve
        show mr end1:
            xalign 0.8 yalign 1.1
        with dissolve
        "..."
        Rick "Да бл..."

        scene black
        with fade
        "Спустя время"

        scene end1
        with fade
        show mr end12:
            xalign 0.4 yalign -0.5
        with dissolve
        show kr end12:
            xalign 0.6 yalign -0.2
        with dissolve
        "Морти не удалось выиграть конкурс и сбежать из этой вселенной"
        "Однако та связь которую он обрел с Кристиной заставила его оставить попытки побега с этой планеты"
        "Они вместе создают инди-студию, и счастливо живут вместе"

        scene black
        with dissolve
        "Вау, вот и наш рассказ подошел к концу, благодарим за внимание :)"

    if wrongAnswerKristinaPath:

        scene end 
        with fade
        show dc 3:
            xalign 0.5 yalign 1.1
        with dissolve
        "Поздравляю вас, Шцмейстз интертейнмент, вы - достойнейший победитель этого блестящего конкурса"
        "Ваша игра не только завоевала сердца жюри, но и восхитила всех нас своей уникальностью и креативностью"
        "Вы создали нечто особенное, что добавит яркость в мир игр!"

        scene end 4
        with fade
        show rc end1:
            xalign 0.02 yalign 1.1
        with dissolve
        show kr end1:
            xalign 0.35 yalign 1.1
        with dissolve
        show mr end1:
            xalign 0.8 yalign 1.1
        with dissolve
        "..."
        Rick "Да бл..."

        scene black
        with fade
        "Спустя время"

        scene end2
        with fade
        ""

        scene end21
        with fade
        "Морти не удалось выиграть конкурс и сбежать из этой вселенной"
        "Герои решили подзаработать денег и после продолжить попытки возврата домой"

        scene black
        with dissolve
        "Вау, вот и наш рассказ подошел к концу, благодарим за внимание :)"

    if gameTest:

        scene end 
        with fade
        show dc 3:
            xalign 0.5 yalign 1.1
        with dissolve
        "Поздравляю вас, команда Санчезов, вы - достойнейший победитель этого блестящего конкурса"
        "Ваша игра не только завоевала сердца жюри, но и восхитила всех нас своей уникальностью и креативностью"
        "Вы создали нечто особенное, что добавит яркость в мир игр!"

        scene end 4
        with fade
        show kr end3:
            xalign 0.35 yalign 1.1
        with dissolve
        show rc end3:
            xalign 0.02 yalign 1.1
        with dissolve
        show mr end3:
            xalign 0.8 yalign 1.1
        with dissolve
        Rick "УРАА!!!!!"

        scene black
        with fade
        "Спустя время"

        scene end3
        with fade
        "Рику и Морти удалось выиграть конкурс и сбежать из этой вселенной"
        "Морти в недалеком будущем удается поступить в IT колледж, где ему удается сделать популярную игру и заработать себе имя"
        "Однако воспоминания о Кристине, все еще посещают его разум"

        scene black
        with dissolve
        "Вау, вот и наш рассказ подошел к концу, благодарим за внимание :)"

    if wrongAnswerKolyaPath:

        scene end 
        with fade
        show dc 3:
            xalign 0.5 yalign 1.1
        with dissolve
        "Поздравляю вас, Шцмейстз интертейнмент, вы - достойнейший победитель этого блестящего конкурса"
        "Ваша игра не только завоевала сердца жюри, но и восхитила всех нас своей уникальностью и креативностью"
        "Вы создали нечто особенное, что добавит яркость в мир игр!"

        scene end 4
        with fade
        show kolya end4:
            xalign 0.35 yalign 1.1
        with dissolve
        show rc end1:
            xalign 0.02 yalign 1.1
        with dissolve
        show mr end1:
            xalign 0.8 yalign 1.1
        with dissolve
        Rick "Да бл..."

        scene black
        with fade
        "Спустя время"

        scene end4
        with fade
        "Морти не удалось сбежать с этого измерения"
        "Однако вскоре Морти осознал, что вовсе и не желает сбегать"
        "Его заинтересовал институт и он остается учиться в ИРИТ-РТФ, периодически посещая свою семью в оригинальном измерении"

        scene black
        with dissolve
        "Вау, вот и наш рассказ подошел к концу, благодарим за внимание :)"

    if knowledgeAboutSoundDesign and knowledgeAboutGameMechanics:

        scene end 
        with fade
        show dc 3:
            xalign 0.5 yalign 1.1
        with dissolve
        "Поздравляю вас, команда Санчезов, вы - достойнейший победитель этого блестящего конкурса"
        "Ваша игра не только завоевала сердца жюри, но и восхитила всех нас своей уникальностью и креативностью"
        "Вы создали нечто особенное, что добавит яркость в мир игр!"

        scene end 4
        with fade
        show kolya end5:
            xalign 0.35 yalign 1.1
        with dissolve
        show rc end3:
            xalign 0.02 yalign 1.1
        with dissolve
        show mr end3:
            xalign 0.8 yalign 1.1
        with dissolve
        Rick "УРАА!!!!!"

        scene black
        with fade
        "Спустя время"

        scene end5
        with fade
        "Морти удалось выиграть главный приз и он вернулся домой"
        "Герои вернулись к привычным, безумным приключениям"
        "Вскоре события во вселенной ИРИТ-РТФ забылись героями"

        scene black
        with dissolve
        "Вау, вот и наш рассказ подошел к концу, благодарим за внимание :)"

    if knowledgeAboutSoundDesign and not knowledgeAboutGameMechanics:

        scene end 
        with fade
        show dc 3:
            xalign 0.5 yalign 1.1
        with dissolve
        "Поздравляю вас, Шцмейстз интертейнмент, вы - достойнейший победитель этого блестящего конкурса"
        "Ваша игра не только завоевала сердца жюри, но и восхитила всех нас своей уникальностью и креативностью"
        "Вы создали нечто особенное, что добавит яркость в мир игр!"

        scene end 4
        with fade
        show kolya end4:
            xalign 0.35 yalign 1.1
        with dissolve
        show rc end1:
            xalign 0.02 yalign 1.1
        with dissolve
        show mr end1:
            xalign 0.8 yalign 1.1
        with dissolve
        Rick "Да бл..."

        scene black
        with fade
        "Спустя время"

        scene end6
        with fade
        "Морти не удалось выиграть главный приз"
        "Однако возвращение домой не волновало Морти"
        "Он решил остаться учиться в ИРИТ-РТФ"
        "И стал успешным учеником, что позволило ему вместе с колей реализовать успешный стартап"

        scene black
        with dissolve
        "Вау, вот и наш рассказ подошел к концу, благодарим за внимание :)"
        





    return